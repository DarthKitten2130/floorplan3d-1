#import blender
from lib2to3.pytree import convert
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.screen import Screen
from kivy.uix.image import Image
#from kivy.uix.widget import Widget



kivy.require('2.1.0')
screen= Screen()


#App Class
class Kivyapp(App):
    
    def build(self):
        #Title Label
        l1 = Label(text="Welcome to 3D Floor Planner! This project was created by Sathvik Mulukutla,\n          Aditya Prasoon,  Aditya Srivastava and Bhaargavi Sreya Jha.",
        pos_hint={'center_x':0.5, 'center_y':0.9}, font_size='17sp',
        color=[0.6,1,0,1],  font_name='Cour'
        )

        #Instruction Label
        l2 = Label(text="Please save your displacement map in the floorplan\n         directory, located on your Desktop",
        pos_hint={'center_x':0.5, 'center_y':0.8}, font_size='17sp',
        color=[0.6,1,0,1],  font_name='Cour')

        

        p1 = Image(source='dog.jpg')

        b1 = Button(text ='Convert to 3D', size=(1,1), size_hint=(.15,.08),
        pos =(430,50))

        #Lambda Functions
        up = lambda x: screen.add_widget(p1) 
        down = lambda y: screen.remove_widget(p1)

        b1.bind(on_press = self.convert)
        #Image Opener
        b2 = Button(text ='Image', size=(1,1), size_hint=(.15,.08),
        pos =(250,50))
        b2.bind(on_press = up)
        
        try:
            os.mkdir("C:\\Users\\Student\\Desktop\\floorplan")
        except:
            pass
   
        

        screen.add_widget(l1)
        screen.add_widget(l2)
        screen.add_widget(b1)
        screen.add_widget(b2)
        return screen
    
    def convert(*args):
        l3 = Label(text='Converting Map to 3D Model; this may take a while...',
                pos_hint={'center_x':0.5, 'center_y':0.2}, font_size='17sp',
                color=[0.6,1,0,1],  font_name='Cour')
        screen.add_widget(l3)

Kivyapp().run()
        


Kivyapp().run()
