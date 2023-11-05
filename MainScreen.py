from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from gradio_client import Client
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from dotenv import load_dotenv
load_dotenv()
import replicate
import webbrowser


#Defining different screens:

class FirstWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class SecondWindow(Widget):
    text=''
    text1=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def acceptText(self):
        self.text = self.ids.input.text
        print(self.text)

    def acceptGerman(self):
        self.text1='Speaker 1 (de)'
    
    def acceptFrench(self):
        self.text1 = 'Speaker 1 (fr)'


    def runSuno(self):
        global audioPath
        client = Client("https://suno-bark.hf.space/")
        result = client.predict(
                        self.text,	# str representing string value in 'Input Text' Textbox component
                        self.text1,	# str representing Option from: ['Unconditional', 'Announcer', 'Speaker 0 (en)', 'Speaker 1 (en)', 'Speaker 2 (en)', 'Speaker 3 (en)', 'Speaker 4 (en)', 'Speaker 5 (en)', 'Speaker 6 (en)', 'Speaker 7 (en)', 'Speaker 8 (en)', 'Speaker 9 (en)', 'Speaker 0 (de)', 'Speaker 1 (de)', 'Speaker 2 (de)', 'Speaker 3 (de)', 'Speaker 4 (de)', 'Speaker 5 (de)', 'Speaker 6 (de)', 'Speaker 7 (de)', 'Speaker 8 (de)', 'Speaker 9 (de)', 'Speaker 0 (es)', 'Speaker 1 (es)', 'Speaker 2 (es)', 'Speaker 3 (es)', 'Speaker 4 (es)', 'Speaker 5 (es)', 'Speaker 6 (es)', 'Speaker 7 (es)', 'Speaker 8 (es)', 'Speaker 9 (es)', 'Speaker 0 (fr)', 'Speaker 1 (fr)', 'Speaker 2 (fr)', 'Speaker 3 (fr)', 'Speaker 4 (fr)', 'Speaker 5 (fr)', 'Speaker 6 (fr)', 'Speaker 7 (fr)', 'Speaker 8 (fr)', 'Speaker 9 (fr)', 'Speaker 0 (hi)', 'Speaker 1 (hi)', 'Speaker 2 (hi)', 'Speaker 3 (hi)', 'Speaker 4 (hi)', 'Speaker 5 (hi)', 'Speaker 6 (hi)', 'Speaker 7 (hi)', 'Speaker 8 (hi)', 'Speaker 9 (hi)', 'Speaker 0 (it)', 'Speaker 1 (it)', 'Speaker 2 (it)', 'Speaker 3 (it)', 'Speaker 4 (it)', 'Speaker 5 (it)', 'Speaker 6 (it)', 'Speaker 7 (it)', 'Speaker 8 (it)', 'Speaker 9 (it)', 'Speaker 0 (ja)', 'Speaker 1 (ja)', 'Speaker 2 (ja)', 'Speaker 3 (ja)', 'Speaker 4 (ja)', 'Speaker 5 (ja)', 'Speaker 6 (ja)', 'Speaker 7 (ja)', 'Speaker 8 (ja)', 'Speaker 9 (ja)', 'Speaker 0 (ko)', 'Speaker 1 (ko)', 'Speaker 2 (ko)', 'Speaker 3 (ko)', 'Speaker 4 (ko)', 'Speaker 5 (ko)', 'Speaker 6 (ko)', 'Speaker 7 (ko)', 'Speaker 8 (ko)', 'Speaker 9 (ko)', 'Speaker 0 (pl)', 'Speaker 1 (pl)', 'Speaker 2 (pl)', 'Speaker 3 (pl)', 'Speaker 4 (pl)', 'Speaker 5 (pl)', 'Speaker 6 (pl)', 'Speaker 7 (pl)', 'Speaker 8 (pl)', 'Speaker 9 (pl)', 'Speaker 0 (pt)', 'Speaker 1 (pt)', 'Speaker 2 (pt)', 'Speaker 3 (pt)', 'Speaker 4 (pt)', 'Speaker 5 (pt)', 'Speaker 6 (pt)', 'Speaker 7 (pt)', 'Speaker 8 (pt)', 'Speaker 9 (pt)', 'Speaker 0 (ru)', 'Speaker 1 (ru)', 'Speaker 2 (ru)', 'Speaker 3 (ru)', 'Speaker 4 (ru)', 'Speaker 5 (ru)', 'Speaker 6 (ru)', 'Speaker 7 (ru)', 'Speaker 8 (ru)', 'Speaker 9 (ru)', 'Speaker 0 (tr)', 'Speaker 1 (tr)', 'Speaker 2 (tr)', 'Speaker 3 (tr)', 'Speaker 4 (tr)', 'Speaker 5 (tr)', 'Speaker 6 (tr)', 'Speaker 7 (tr)', 'Speaker 8 (tr)', 'Speaker 9 (tr)', 'Speaker 0 (zh)', 'Speaker 1 (zh)', 'Speaker 2 (zh)', 'Speaker 3 (zh)', 'Speaker 4 (zh)', 'Speaker 5 (zh)', 'Speaker 6 (zh)', 'Speaker 7 (zh)', 'Speaker 8 (zh)', 'Speaker 9 (zh)'] in 'Acoustic Prompt' Dropdown component
                        fn_index=3
        )
        print(result)
        ThirdWindow.audioPath=result
        
        
class ThirdWindow(Widget):
    
    imgPath=''
    audioPath=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def select_imagefile(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.imgselected)


    def imgselected(self, selection):
        self.imgPath=selection[0]
        print(self.imgPath)
    
    def runSadTalker(self):
        print(self.audioPath)
        output = replicate.run("cjwbw/sadtalker:3aa3dac9353cc4d6bd62a8f95957bd844003b401ca4e4a9b33baa574c549d376",
        input={"source_image": open(self.imgPath, "rb"),
                "driven_audio": open(self.audioPath,"rb")})
        print(output)
        FourthWindow.url=output


class FourthWindow(Widget):
    url=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def openVid(self):
        webbrowser.open_new(self.url)

class FifthWindow(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def select_audiofile(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.audioselected)

    def audioselected(self, selection):
        self.audioPath=selection[0]
        print(self.audioPath)

    def select_imagefile(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.imgselected)


    def imgselected(self, selection):
        self.imgPath=selection[0]
        print(self.imgPath)

    def runSadTalker(self):
        output = replicate.run("cjwbw/sadtalker:3aa3dac9353cc4d6bd62a8f95957bd844003b401ca4e4a9b33baa574c549d376",
        input={"source_image": open(self.imgPath, "rb"),
                "driven_audio": open(self.audioPath,"rb")})
        print(output)
        FourthWindow.url=output
        
    


kv = Builder.load_file('window.kv')


class SadTalkerGui(App):
    def build(self):
        self.ScreenM = ScreenManager() 
        
        self.FirstWin = FirstWindow()
        screen = Screen(name = "first")
        screen.add_widget(self.FirstWin)
        self.ScreenM.add_widget(screen)

        self.SecondWin = SecondWindow()
        screen = Screen(name = "second")
        screen.add_widget(self.SecondWin)
        self.ScreenM.add_widget(screen)

        self.ThirdWin = ThirdWindow()
        screen = Screen(name = "third")
        screen.add_widget(self.ThirdWin)
        self.ScreenM.add_widget(screen)

        self.FourthWin = FourthWindow()
        screen = Screen(name = "fourth")
        screen.add_widget(self.FourthWin)
        self.ScreenM.add_widget(screen)

        self.FifthWin = FifthWindow()
        screen = Screen(name = "fifth")
        screen.add_widget(self.FifthWin)
        self.ScreenM.add_widget(screen)

        
        
        return self.ScreenM
    


if __name__ == '__main__':
    SadApp = SadTalkerGui()
    SadApp.run()