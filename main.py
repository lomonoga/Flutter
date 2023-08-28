import flet as ft


def main(page: ft.Page):

    def add_text(text: str):
        if text_field.value == "": return
        box = ft.Text(value=text_field.value, size=16, width=350)
        second_row = ft.Row(controls=[box], alignment=ft.MainAxisAlignment.START)
        page.add(second_row)

    page.window_width = 500
    page.window_height = 700
    page.window_resizable = False

    page.bgcolor = '#45FFCA'
    page.title = 'by Lomonoga'
    page.window_maximizable = False

    text_field = ft.TextField(border_radius=25,
                              label="Введи сюда что то сука!!!",
                              width=300,
                              label_style=ft.TextStyle(size=20))

    button = ft.ElevatedButton(text='ЖМИ', on_click=add_text)
    first_row = ft.Row(controls=[text_field, button], alignment=ft.MainAxisAlignment.SPACE_AROUND)
    page.add(first_row)


ft.app(target=main)
