from fasthtml import HTML, Body, H1, P, A
from datetime import datetime

# Create the home page
home_page = HTML(
    Body(
        H1("Hello, World!")
    )
)

# Create the second page with current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
second_page = HTML(
    Body(
        H1("Current Date and Time"),
        P(now),
        P(A("Go back to home page", href="index.html"))
    )
)

# Save the HTML files
with open("index.html", "w") as file:
    file.write(str(home_page))

with open("second_page.html", "w") as file:
    file.write(str(second_page))