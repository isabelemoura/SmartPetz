from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp

Window.size = (350, 580)

class Monitor(Screen):
    water_level = NumericProperty(75)
    temperature = NumericProperty(25)
    food_level = NumericProperty(41)

    def update_levels(self, dt):
        self.water_level = max(0, self.water_level - 1)
        self.temperature = min(100, self.temperature + 0.5)
        self.food_level = max(0, self.food_level - 0.5)

class Menu(Screen):
    pass # Defina o conteúdo da tela se necessário

class WifiScreen(Screen):
    pass  # Defina o conteúdo da tela se necessário

class BluetoothScreen(Screen):
    pass  # Defina o conteúdo da tela se necessário

class ConfigScreen(Screen):
    pass  # Defina o conteúdo da tela se necessário

class RegistrarAnimal(Screen):
    pass  # Defina o conteúdo da tela se necessário

class DefinirRefeicao(Screen):
    pass  # Defina o conteúdo da tela se necessário


class SmartPetz(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        
        Builder.load_file("refeicao.kv")
        Builder.load_file("config.kv")
        Builder.load_file("wifi_screen.kv")
        Builder.load_file("bluetooth_screen.kv")
        Builder.load_file("monitor_qualidade.kv")
        Builder.load_file("registrar_usuario.kv")
        Builder.load_file("registrar_animal.kv")
        Builder.load_file("pre-splash.kv")
        Builder.load_file("login.kv")
        
        self.screen_manager.add_widget(Builder.load_file("login.kv"))
        self.screen_manager.add_widget(DefinirRefeicao(name="refeicao"))
        self.screen_manager.add_widget(Monitor(name="monitor"))
        self.screen_manager.add_widget(RegistrarAnimal(name="registrar_animal"))
        self.screen_manager.add_widget(Builder.load_file("registrar_usuario.kv"))
        self.screen_manager.add_widget(ConfigScreen(name="config"))
        self.screen_manager.add_widget(WifiScreen(name="wifi"))
        self.screen_manager.add_widget(BluetoothScreen(name="bluetooth"))
        self.screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        self.screen_manager.add_widget(Menu(name="menu"))
        
        return self.screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.show_login_screen, 5)
    
    def show_login_screen(self, *args):
        self.screen_manager.current = "login"
    
    def registrar(self):
        self.screen_manager.current = "registrar"

    def go_back_to_pre_splash(self):
        self.screen_manager.current = "pre-splash"
    
    def go_back_to_login(self):
        self.screen_manager.current = "login"

    def go_back_to_registrar_animal(self):
        self.root.current = "registrar_animal"

    def go_back_to_config(self):
        self.root.current = "config"
    
    def go_back_to_wifi(self):
        self.root.current = "wifi"
    
    def go_back_to_bluetooth(self):
        self.root.current = "bluetooth"

    def open_menu(self, button):
        menu_items = [
            {
                "text": f"Opção {i+1}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Opção {i+1}": self.menu_callback(x),
            } for i in range(3)
        ]
        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        print(f"Selecionado: {text_item}")
        self.root.ids.tipo_button.text = text_item

    def go_to_menu(self, *args):
        self.screen_manager.current = 'menu'

if __name__ == "__main__":
    SmartPetz().run()
