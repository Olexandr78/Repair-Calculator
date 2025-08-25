from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class RepairCalcApp(App):
    def build(self):
        tp = TabbedPanel(do_default_tab=False)

        # Экран
        screen_tab = TabbedPanelItem(text='Экран')
        screen_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        screen_layout.add_widget(Label(text='Экран: перевод дюймов в см и расчёт площади', font_size=18))
        screen_input = TextInput(hint_text='Диагональ в дюймах', multiline=False, input_filter='float')
        screen_result = Label(text='Результат появится здесь')
        screen_button = Button(text='Посчитать', size_hint=(1, 0.3))

        def screen_calc(instance):
            try:
                inches = float(screen_input.text)
                cm = inches * 2.54
                aspect_w, aspect_h = 16, 9
                k = (inches ** 2) / (aspect_w**2 + aspect_h**2)
                width_inch = (k ** 0.5) * aspect_w
                height_inch = (k ** 0.5) * aspect_h
                width_cm = width_inch * 2.54
                height_cm = height_inch * 2.54
                area_cm2 = width_cm * height_cm
                screen_result.text = (
                    f'Диагональ: {cm:.2f} см\n'
                    f'Ширина: {width_cm:.1f} см, Высота: {height_cm:.1f} см\n'
                    f'Площадь: {area_cm2:.1f} см²'
                )
            except ValueError:
                screen_result.text = 'Ошибка: введите число'

        screen_button.bind(on_press=screen_calc)
        screen_layout.add_widget(screen_input)
        screen_layout.add_widget(screen_result)
        screen_layout.add_widget(screen_button)
        screen_tab.add_widget(screen_layout)
        tp.add_widget(screen_tab)

        # Аккумулятор
        battery_tab = TabbedPanelItem(text='Аккумулятор')
        battery_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        battery_layout.add_widget(Label(text='Аккумулятор: расчёт Вт·ч и совместимости', font_size=18))
        volt_input = TextInput(hint_text='Напряжение (V)', multiline=False, input_filter='float')
        cap_input = TextInput(hint_text='Ёмкость (мА·ч)', multiline=False, input_filter='float')
        battery_result = Label(text='Результат появится здесь')
        battery_button = Button(text='Посчитать', size_hint=(1,0.3))

        def battery_calc(instance):
            try:
                v = float(volt_input.text)
                mah = float(cap_input.text)
                wh = v * mah / 1000
                battery_result.text = f'Мощность: {wh:.2f} Вт·ч'
            except ValueError:
                battery_result.text = 'Ошибка: введите число'

        battery_button.bind(on_press=battery_calc)
        battery_layout.add_widget(volt_input)
        battery_layout.add_widget(cap_input)
        battery_layout.add_widget(battery_result)
        battery_layout.add_widget(battery_button)
        battery_tab.add_widget(battery_layout)
        tp.add_widget(battery_tab)

        # Питание
        power_tab = TabbedPanelItem(text='Блок питания')
        power_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        power_layout.add_widget(Label(text='Блок питания: мощность W = V × A', font_size=18))
        v_input = TextInput(hint_text='Вольтаж (V)', multiline=False, input_filter='float')
        a_input = TextInput(hint_text='Сила тока (A)', multiline=False, input_filter='float')
        power_result = Label(text='Результат появится здесь')
        power_button = Button(text='Посчитать', size_hint=(1,0.3))

        def power_calc(instance):
            try:
                v = float(v_input.text)
                a = float(a_input.text)
                w = v * a
                power_result.text = f'Мощность: {w:.2f} Вт'
            except ValueError:
                power_result.text = 'Ошибка: введите число'

        power_button.bind(on_press=power_calc)
        power_layout.add_widget(v_input)
        power_layout.add_widget(a_input)
        power_layout.add_widget(power_result)
        power_layout.add_widget(power_button)
        power_tab.add_widget(power_layout)
        tp.add_widget(power_tab)

        return tp

if __name__ == "__main__":
    RepairCalcApp().run()