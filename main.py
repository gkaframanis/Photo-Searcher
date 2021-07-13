"""Kivy: App - ScreenManager - Screen - Widgets
In the frontend.kv file we write the code of how the screen looks like.
"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# So we can communicate with the frontend.kv file
from kivy.lang import Builder
# We will use the wikipedia library to get images based on the search term.
import wikipedia
# To download the images from the Wikipedia image
import requests

Builder.load_file("frontend.kv")


# We create as many Screen Classes as the number of screens we will have in our app
class FirstScreen(Screen):

    def get_image_link(self):
        # Get user query from the TextInput widget
        query = self.manager.current_screen.ids.user_query.text
        # Get from the wikipedia page a list of image urls based on the query and we get the first image url.
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image and save it to a file
        req = requests.get(self.get_image_link())
        image_path = "files/image.jpg"
        with open(image_path, "wb") as file:
            file.write(req.content)
        return image_path

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


# It's convention this class to be named RootWidget and it's usually an empty class
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
