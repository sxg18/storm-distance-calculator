import tkinter as tk
from tkinter import messagebox

def calculate_distance(time_in_seconds):
    distance_in_miles = round((time_in_seconds * 1100) / 5280, 2)
    distance_in_km = round(distance_in_miles * 1.60934, 2)
    return distance_in_miles, distance_in_km


def calculate_distance_in_gui(event=None):
    time_elapsed = float(time_entry.get())
    distance_in_miles, distance_in_km = calculate_distance(time_elapsed)
    result_label.config(text=f"The distance of the lightning strike is {distance_in_miles} miles (or {distance_in_km} kilometers).")

window = tk.Tk()
window.title("Lightning Distance Calculator")

time_label = tk.Label(window, text="Please enter the time elapsed after the lightning in seconds:")
time_label.pack()

time_entry = tk.Entry(window, width=20)
time_entry.pack()
time_entry.focus_set()
time_entry.bind("<Return>", calculate_distance_in_gui)

calculate_button = tk.Button(window, text="Calculate", command=calculate_distance_in_gui)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

icon = tk.PhotoImage(file='StormDistanceCalculator.png')
window.iconphoto(False, icon)

window.mainloop()
