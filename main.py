
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        # Layout principal vertical
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Pantalla de resultados (solo lectura)
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=40,
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.solution)

        # Grid para los botones (4 columnas)
        button_layout = GridLayout(cols=4, spacing=5)

        # Definición de los botones en orden
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Crear cada botón y agregarlo al grid
        for button in buttons:
            btn = Button(
                text=button,
                font_size=30,
                background_color=(0.5, 0.5, 0.5, 1)
            )
            btn.bind(on_press=self.on_button_press)
            button_layout.add_widget(btn)

        main_layout.add_widget(button_layout)
        return main_layout

    # Función que maneja los clics en los botones
    def on_button_press(self, instance):
        current = self.solution.text

        if instance.text == 'C':
            # Botón Clear: limpiar pantalla
            self.solution.text = ''
        elif instance.text == '=':
            # Botón Igual: calcular resultado
            try:
                self.solution.text = str(eval(current))
            except:
                self.solution.text = 'Error'
        else:
            # Botones numéricos y operadores
            if current == 'Error':
                self.solution.text = instance.text
            else:
                self.solution.text = current + instance.text

# Punto de entrada de la aplicación
if __name__ == '__main__':
    CalculatorApp().run()
