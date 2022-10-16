from kivy.app import App
from kivy.lang import Builder



class Main(App):
     def build(self):
          return Builder.load_file("cam.kv")

     def picture_taken(self):
          print("Got the pic")

     def change_cam(self):
          pass
     










Main().run()























