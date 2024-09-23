import flet as ft
import pandas as pd
import webbrowser

def main(page: ft.Page):
    try:
        # Read the JSON file
        df = pd.read_json('default.json')
    except ValueError as e:
        page.add(ft.Text(f"Error loading JSON: {e}", color=ft.colors.RED))
        page.update()
        return
    
    # Set page title
    page.title = "DataFrame Display"
    
    # Add DataFrame rows to the page as text with clickable URLs
    page.add(ft.Text("DataFrame Content:"))
    
    # Create a scrollable container
    scrollable_container = ft.Container(
        content=ft.Text("Hello, World! in web\n" * 20),  # Repeated text to demonstrate scrolling
        width=300,
        height=200,
        scroll=ft.ScrollMode.AUTO
    )
    
    page.add(scrollable_container)
    
    # Update the page
    page.update()

ft.app(target=main)


