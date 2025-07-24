import flet as ft
from ..message.counter_msg import CounterMessage
from ..model.counter import Counter


def render_view(model: Counter, dispatch) -> list:
    return [
        ft.Text(f"Counter: {model.count}", size=30),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.ElevatedButton(
                    "➕", on_click=lambda e: dispatch(CounterMessage.INCREMENT)
                ),
                ft.ElevatedButton(
                    "➖", on_click=lambda e: dispatch(CounterMessage.DECREMENT)
                ),
                ft.ElevatedButton(
                    "🔁 Reset", on_click=lambda e: dispatch(CounterMessage.RESET)
                ),
            ]
        )
    ]
