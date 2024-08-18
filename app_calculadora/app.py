from kivy.app import App 
from kivy.lang import Builder

gui = Builder.load_file('tela.kv') #interface

#armazenar todas as funcoes do aplicativo
class MeuApp(App):
    def build(self):
        return gui


MeuApp().run() #rodar a tela do aplicativo