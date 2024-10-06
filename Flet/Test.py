from time import sleep
import flet as ft
import json
import pandas as pd

def main(page: ft.Page):
    
    def handle_change(e: ft.ControlEvent):
        # print(f"change on panel with index {e.data}")
    #    if e.control.expand:
            # Perform action for the clicked panel
        print(f"Panel {e.data} clicked!")  # Replace with your specific action
    # ... existing code ...
        
    def handle_delete(e: ft.ControlEvent):
        panel.controls.remove(e.control.data)
        page.update()
        
    page.scroll = "auto"
    page.title = "Auto-scrolling ExpansionPanelList"
    filename = "default.json"
    with open(filename, "r", encoding="utf-8") as f:
        df = pd.read_json(f)

    # Create an empty ExpansionPanelList
    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.colors.AMBER,
        elevation=8,
        divider_color=ft.colors.AMBER,
        on_change=handle_change,
        controls=[
            ft.ExpansionPanel(
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.BLUE_400,
                expanded=True,
            )
        ],
    )

    for _, row in df.iterrows():
        url = row['url']
        label = row['label']
        title = row['title']
        
        # Create an ExpansionPanel for each item
        exp = ft.ExpansionPanel(
            header=ft.Text(title),
            # body=ft.Text(f"{title} {url}"),
            # is_expanded=False  # Initial state can be set here
        )
        
        exp.content = ft.Text(f"{label} {url}")
        
        
        panel.controls.append(exp)  # Add the panel to the list

    page.add(panel)
    page.update()

    # for i in range(0, 60):
    #     sleep(1)
    #     lv.controls.append(ft.Text(f"Line {count}"))
    #     count += 1
    #     page.update()

ft.app(main)
        # content=ft.Text("Hello, World! in web" * 50),  # Example long text
