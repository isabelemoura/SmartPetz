from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivy.properties import StringProperty

# Define o tamanho da janela principal
Window.size = (350, 580)

class Monitor(Screen):
    # Propriedades que representam os níveis de água, temperatura e ração
    water_level = NumericProperty(75)
    temperature = NumericProperty(50)
    food_level = NumericProperty(41)

    def on_pre_enter(self):
        # Bind as propriedades water_level e food_level ao método check_levels
        self.bind(water_level=self.check_levels, food_level=self.check_levels)

    def update_levels(self, dt):
        # Atualiza os níveis de água, temperatura e ração com o tempo
        self.water_level = max(0, self.water_level - 1)  # Reduz o nível de água
        self.temperature = min(100, self.temperature + 0.5)  # Aumenta a temperatura
        self.food_level = max(0, self.food_level - 0.5)  # Reduz o nível de ração
    
    def check_levels(self, *args):
        # Verifica e atualiza os avisos de nível de água e ração
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
    # Tela de Menu - definir o conteúdo conforme necessário
    pass

class WifiScreen(Screen):
    # Tela de Wi-Fi - definir o conteúdo conforme necessário
    pass

class BluetoothScreen(Screen):
    # Tela de Bluetooth - definir o conteúdo conforme necessário
    pass

class ConfigScreen(Screen):
    # Tela de Configurações - definir o conteúdo conforme necessário
    pass

class RegistrarAnimal(Screen):
    # Tela de Registro de Animal - definir o conteúdo conforme necessário
    pass

class DefinirRefeicao(Screen):
    # Tela de Definir Refeição - definir o conteúdo conforme necessário
    pass

class Login(Screen):
    # Tela de Login - definir o conteúdo conforme necessário
    pass

class AgendarRefeicao(Screen):
    # Tela de Agendar Refeição - definir o conteúdo conforme necessário
    pass

class VacinaScreen(Screen):
    # Tela de Listagem de Vacina - definir o conteúdo conforme necessário
    pass

class DefinirPorcao(Screen):
    # Propriedade para o peso da porção
    weight = NumericProperty(100)  # Utilize NumericProperty para facilidade de cálculo

    def increment_weight(self):
        # Incrementa o peso da porção em 1
        self.weight += 1

    def decrement_weight(self):
        # Decrementa o peso da porção em 1, garantindo que não seja negativo
        if self.weight > 0:
            self.weight -= 1

    def cancel(self):
        # Lógica para cancelar a configuração
        pass

    def save(self):
        # Lógica para salvar a configuração
        pass

class HomeScreen(Screen):
    # Propriedades que representam os níveis de água e ração na tela inicial
    water_level = NumericProperty(80)  # Exemplo de valor inicial
    food_level = NumericProperty(90)   # Exemplo de valor inicial
    
    def on_pre_enter(self):
        # Bind as propriedades water_level e food_level ao método check_levels
        self.bind(water_level=self.check_levels, food_level=self.check_levels)
        self.check_levels()  # Executa check_levels quando a tela é exibida

    def check_levels(self, *args):
        # Calcula a quantidade necessária para atingir 41% de água e ração
        water_diff = max(0, 41 - self.water_level)
        food_diff = max(0, 41 - self.food_level)
        
        # Configura o texto e a cor para o nível de água
        if self.water_level < 40:
            self.ids.water_warning.text = f"Nível de água está baixo! Faltam {water_diff}% para o normal."
            self.ids.water_warning.text_color = [1, 0, 0, 1]  # Vermelho
        elif 40 <= self.water_level <= 60:
            self.ids.water_warning.text = "Nível de água está normal."
            self.ids.water_warning.text_color = [1, 1, 0, 1]  # Amarelo
        else:
            self.ids.water_warning.text = "Nível de água está bom!"
            self.ids.water_warning.text_color = [0, 1, 0, 1]  # Verde

        # Configura o texto e a cor para o nível de ração
        if self.food_level < 40:
            self.ids.food_warning.text = f"Nível de ração está baixo! Faltam {food_diff}% para o normal."
            self.ids.food_warning.text_color = [0.8, 0.2, 0.2, 1]  # Vermelho
        elif 40 <= self.food_level <= 60:
            self.ids.food_warning.text = "Nível de ração está normal."
            self.ids.food_warning.text_color = [1, 1, 0, 1]  # Amarelo
        else:
            self.ids.food_warning.text = "Nível de ração está bom!"
            self.ids.food_warning.text_color = [0.2, 0.8, 0.2, 1]  # Verde
        
        # Exibe a quantidade faltante para o nível normal (amarelo)
        if water_diff > 0 or food_diff > 0:
            self.ids.quantidade_faltante_label.text = (
                f"Faltam {water_diff}% de água e {food_diff}% de ração para o nível normal (amarelo)."
            )
        else:
            self.ids.quantidade_faltante_label.text = "Níveis de água e ração estão no normal e bom."

class SmartPetz(MDApp):
    def build(self):
        # Cria o gerenciador de telas
        self.screen_manager = ScreenManager()
        
        # Carrega os arquivos KV para as telas
        Builder.load_file("add_vacina.kv")
        Builder.load_file("vacina_screen.kv")
        Builder.load_file("definir_porcao.kv")
        Builder.load_file("agendar_refeicao.kv")
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

        # Adiciona as telas ao ScreenManager
        self.screen_manager.add_widget(BluetoothScreen(name="bluetooth"))
        self.screen_manager.add_widget(WifiScreen(name="wifi"))
        self.screen_manager.add_widget(RegistrarAnimal(name="registrar_animal"))
        self.screen_manager.add_widget(Monitor(name="monitor"))
        self.screen_manager.add_widget(DefinirRefeicao(name="refeicao"))
        self.screen_manager.add_widget(DefinirPorcao(name="definir_porcao"))
        self.screen_manager.add_widget(HomeScreen(name="home"))
        self.screen_manager.add_widget(AgendarRefeicao(name="agendar_refeicao"))
        self.screen_manager.add_widget(ConfigScreen(name="config"))
        self.screen_manager.add_widget(Builder.load_file("registrar_usuario.kv"))
        self.screen_manager.add_widget(Login(name="login"))
        self.screen_manager.add_widget(Builder.load_file("add_vacina.kv"))
        self.screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        self.screen_manager.add_widget(VacinaScreen(name="vacina"))
        self.screen_manager.add_widget(Menu(name="menu"))
        
        return self.screen_manager
    
    def go_back_to_home(self):
        # Volta para a tela de Definir Porção
        self.root.current = "home"

    def registrar(self):
        # Muda para a tela de registro
        self.screen_manager.current = "registrar"

    def go_back_to_pre_splash(self):
        # Volta para a tela de pré-carregamento
        self.screen_manager.current = "pre-splash"
    
    def go_back_to_login(self):
        # Volta para a tela de login
        self.root.current = "login"

    def go_back_to_registrar_animal(self):
        # Volta para a tela de registro de animal
        self.root.current = "registrar_animal"

    def go_back_to_config(self):
        # Volta para a tela de configurações
        self.root.current = "config"
    
    def go_back_to_wifi(self):
        # Volta para a tela de Wi-Fi
        self.root.current = "wifi"
    
    def go_back_to_bluetooth(self):
        # Volta para a tela de Bluetooth
        self.root.current = "bluetooth"
    
    def go_back_to_definir_porcao(self):
        # Volta para a tela de Definir Porção
        self.root.current = "definir_porcao"
    
    def go_back_to_agendar_refeicao(self):
        # Volta para a tela de Definir Porção
        self.root.current = "agendar_refeicao"
    
    def go_back_to_monitor(self):
        # Volta para a tela de Definir Porção
        self.root.current = "monitor"
    
    def checkbox_toggle(self, checkbox, is_active):
        if is_active:
            print("Checkbox está marcado")
        else:
            print("Checkbox está desmarcado")
    
    def open_animal_selector(self, dropdown_item):
        # Abre o menu dropdown para seleção de opções após selecionar o animal
        menu_items = [
            {
                "text": f"Opção {i+1}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Opção {i+1}": self.menu_callback(x),
            } for i in range(4)  # Adicione aqui o número de opções que deseja
        ]
        self.animal_menu = MDDropdownMenu(
            caller=dropdown_item,
            items=menu_items,
            width_mult=4,
        )
        self.animal_menu.open()

    def menu_callback(self, text_item):
        # Manipula a seleção do item no menu dropdown
        self.animal_menu.dismiss()
        print(f"Selecionado: {text_item}")
        # Atualiza o texto do label com o item selecionado
        self.root.ids.animal_menu_label.text = f"Selecionado: {text_item}"

    def open_menu(self, button):
        # Abre o menu dropdown quando um botão é clicado
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
        # Manipula a seleção do item no menu dropdown
        self.menu.dismiss()
        print(f"Selecionado: {text_item}")
        self.root.ids.tipo_button.text = text_item

    def go_to_menu(self, *args):
        # Muda para a tela de menu
        self.screen_manager.current = 'menu'

if __name__ == "__main__":
    SmartPetz().run()
