# from pydoc import text
# from tkinter import N, Image
# from tkinter.messagebox import NO
# import cv2
# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.button import MDRaisedButton
# from kivy.uix.image import Image
# from matplotlib import image
# from kivy.clock import Clock
# from pyscreeze import center


# class MainApp(MDApp):

#      def build(self):
#           layout = MDBoxLayout(orientation='vertical')
#           self.image = Image()
#           layout.add_widget(self,image)
#           layout.add_widget(MDRaisedButton(
#                text="CLICK HERE",
#                pos_hint={'center_x': .5,'center_y': .5},
#                size_hint = (None,None)
#           ))

#           self.capture = cv2.VideoCapture(0)
#           Clock.schedule_interval(self.load_video, 1.0/30.0)

#           return layout



#      def load_video(self,*args):
#           ret, frame = self.capture.read()
#           self.image_frame=frame
#           # buffer = cv2.flip(frame, 0).tostring()
#           # texture = Texture.create()
          











          



# if __name__ == '__main__':
#      MainApp().run()



# import datetime
# from kivy.lang import Builder
# from kivy.app import App

# kv = """
# #:import XCamera kivy.garden.xcamera.XCamera

# FloatLayout:
#     orientation: 'vertical'

#     XCamera:
#         id: xcamera
#         on_picture_taken: app.picture_taken(*args)

#     BoxLayout:
#         orientation: 'horizontal'
#         size_hint: 1, None
#         height: sp(50)

#         Button:
#             text: 'Set landscape'
#             on_release: xcamera.force_landscape()

#         Button:
#             text: 'Restore orientation'
#             on_release: xcamera.restore_orientation()
# """


# class CameraApp(App):
#     def build(self):
#         return Builder.load_string(kv)

#     def picture_taken(self, obj, filename):
#         print('Picture taken and saved to {}'.format(filename))

# if __name__ == '__main__':
#     CameraApp().run()

















