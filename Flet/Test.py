from time import sleep
import flet as ft
import json
import pandas as pd

def main(page: ft.Page):
    page.title = "Auto-scrolling ListView"
    filename = "default.json"
    with open(filename, "r", encoding="utf-8") as f:
        df = pd.read_json(f)

    lv = ft.ListView(expand=1, spacing=10, padding=20)

    count = 1
    
    for _, row in df.iterrows():
        url = row['url']
        label = row['label']
        title = row['title']
        lv.controls.append(ft.Text(f"{label} {title} {url}"))

    page.add(lv)
    page.update()

    # for i in range(0, 60):
    #     sleep(1)
    #     lv.controls.append(ft.Text(f"Line {count}"))
    #     count += 1
    #     page.update()

ft.app(main)
        # content=ft.Text("Hello, World! in web" * 50),  # Example long text
