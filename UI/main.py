from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp

Window.size = (350, 580)

class Monitor(Screen):
    water_level = NumericProperty(75)
    temperature = NumericProperty(50)
    food_level = NumericProperty(41)

    def on_pre_enter(self):
        # Bind the properties to check_levels method
        self.bind(water_level=self.check_levels, food_level=self.check_levels)

    def update_levels(self, dt):
        self.water_level = max(0, self.water_level - 1)
        self.temperature = min(100, self.temperature + 0.5)
        self.food_level = max(0, self.food_level - 0.5)
    
    def check_levels(self, *args):
        if self.water_level < 40:
            self.ids.water_warning.text = "Nível de água está baixo!"
        elif 40 <= self.water_level <= 60:
            self.ids.water_warning.text = "Nível de água está normal."
        else:
            self.ids.water_warning.text = "Nível de água está bom!"

        if self.food_level < 40:
            self.ids.food_warning.text = "Nível de ração está baixo!"
        elif 40 <= self.food_level <= 60:
            self.ids.food_warning.text = "Nível de ração está normal."
        else:
            self.ids.food_warning.text = "Nível de ração está bom!"

class Menu(Screen):
    pass  # Defina o conteúdo da tela se necessário

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

class Login(Screen):
    pass  # Defina o conteúdo da tela se necessário


class HomeScreen(Screen):
    water_level = NumericProperty(41)  # Exemplo de valor inicial
    food_level = NumericProperty(50)   # Exemplo de valor inicial
    
    def on_pre_enter(self):
        # Bind the properties to check_levels method
        self.bind(water_level=self.check_levels, food_level=self.check_levels)
        self.check_levels()  # Run check_levels when the screen is entered

    def check_levels(self, *args):
        water_diff = max(0, 41 - self.water_level)  # Quantidade necessária para atingir 41%
        food_diff = max(0, 41 - self.food_level)    # Quantidade necessária para atingir 41%
        
        # Configurando o texto e a cor para o nível de água
        if self.water_level < 40:
            self.ids.water_warning.text = f"Nível de água está baixo! Faltam {water_diff}% para o normal."
            self.ids.water_warning.text_color = [1, 0, 0, 1]  # Vermelho
        elif 40 <= self.water_level <= 60:
            self.ids.water_warning.text = "Nível de água está normal."
            self.ids.water_warning.text_color = [1, 1, 0, 1]  # Amarelo
        else:
            self.ids.water_warning.text = "Nível de água está bom!"
            self.ids.water_warning.text_color = [0, 1, 0, 1]  # Verde

        # Configurando o texto e a cor para o nível de ração
        if self.food_level < 40:
            self.ids.food_warning.text = f"Nível de ração está baixo! Faltam {food_diff}% para o normal."
            self.ids.food_warning.text_color = [1, 0, 0, 1]  # Vermelho
        elif 40 <= self.food_level <= 60:
            self.ids.food_warning.text = "Nível de ração está normal."
            self.ids.food_warning.text_color = [1, 1, 0, 1]  # Amarelo
        else:
            self.ids.food_warning.text = "Nível de ração está bom!"
            self.ids.food_warning.text_color = [0, 128, 0, 1]  # Verde
        
        # Exibir a quantidade faltante para o nível normal (amarelo)
        if water_diff > 0 or food_diff > 0:
            self.ids.quantidade_faltante_label.text = (
                f"Faltam {water_diff}% de água e {food_diff}% de ração para o nível normal (amarelo)."
            )
        else:
            self.ids.quantidade_faltante_label.text = "Níveis de água e ração estão no normal ou acima."

class SmartPetz(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        
        Builder.load_file("home_screen.kv")
        Builder.load_file("refeicao.kv")
        Builder.load_file("config.kv")
        Builder.load_file("wifi_screen.kv")
        Builder.load_file("bluetooth_screen.kv")
        Builder.load_file("monitor_qualidade.kv")
        Builder.load_file("registrar_usuario.kv")
        Builder.load_file("registrar_animal.kv")
        Builder.load_file("pre-splash.kv")
        Builder.load_file("login.kv")
        
        self.screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        self.screen_manager.add_widget(HomeScreen(name="home"))
        self.screen_manager.add_widget(Monitor(name="monitor"))
        self.screen_manager.add_widget(RegistrarAnimal(name="registrar_animal"))
        self.screen_manager.add_widget(Login(name="login"))
        self.screen_manager.add_widget(Builder.load_file("registrar_usuario.kv"))
        self.screen_manager.add_widget(DefinirRefeicao(name="refeicao"))
        self.screen_manager.add_widget(ConfigScreen(name="config"))
        self.screen_manager.add_widget(WifiScreen(name="wifi"))
        self.screen_manager.add_widget(BluetoothScreen(name="bluetooth"))
        self.screen_manager.add_widget(Menu(name="menu"))
        
        return self.screen_manager
    
    def registrar(self):
        self.screen_manager.current = "registrar"

    def go_back_to_pre_splash(self):
        self.screen_manager.current = "pre-splash"
    
    def go_back_to_login(self):
        self.root.current = "login"

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
