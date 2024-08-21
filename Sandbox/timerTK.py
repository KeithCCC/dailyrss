 

 # Create a Tkinter window
import tkinter as tk


# Create a function to calculate elapsed time
def calculate_elapsed_time():
    # Get the selected date and time
    date_str = selected_date.get()
    time_str = selected_time.get()

    # Convert the date and time strings to datetime objects
    selected_datetime = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M:%S")

    # Get the current datetime
    now = datetime.now()

    # Check if the selected datetime is in the future
    if selected_datetime > now:
        result_label.config(text="選択した日時は未来です。過去の日時を選択してください。")
    else:
        # Calculate the elapsed time
        elapsed_time = now - selected_datetime

        days = elapsed_time.days
        hours, remainder = divmod(elapsed_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        result_label.config(text=f"{days}日 {hours}時間 {minutes}分 {seconds}秒")

    # Create a button to calculate elapsed time
    calculate_button = tk.Button(window, text="Calculate", command=calculate_elapsed_time)
    calculate_button.pack()

    # Create a label to display the result
    result_label = tk.Label(window, text="")
    result_label.pack()

    # Run the Tkinter event loop
    window.mainloop()

window = tk.Tk()
window.title("経過時間計算アプリ")

# Create a label for the title
title_label = tk.Label(window, text="経過時間計算アプリ")
title_label.pack()

# Create a label and entry for date input
date_label = tk.Label(window, text="Select a date")
date_label.pack()
selected_date = tk.StringVar()
date_entry = tk.Entry(window, textvariable=selected_date)
date_entry.pack()

# Create a label and entry for time input
time_label = tk.Label(window, text="Select a time")
time_label.pack()
selected_time = tk.StringVar()
time_entry = tk.Entry(window, textvariable=selected_time)
time_entry.pack()
