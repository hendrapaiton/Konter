from .view.counter_ui import render_view
from .update.counter_update import update
from .model.counter import Counter
from .message.counter_msg import CounterMessage
import flet as ft
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main(page: ft.Page):
    page.title = "Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 320
    page.window.height = 480

    model = Counter()

    def dispatch(msg):
        nonlocal model
        model = update(msg, model)
        page.controls.clear()
        page.controls.extend(render_view(model, dispatch))
        page.update()

    dispatch(CounterMessage.INIT)
