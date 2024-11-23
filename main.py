import tkinter as tk
from tkinter import *

# Window setup
root = tk.Tk()
root.title("BMI Calculator")
root.minsize(width=400, height=300)

# Label for weight
tk.Label = Label(root, text="Enter your weight(kg)")
tk.Label.config(fg="black")
tk.Label.config(padx=20, pady=50)
tk.Label.pack()

# Entry for weight
weight_entry = Entry(root, width=30)
weight_entry.place(x=110, y=70)

# Label for height
tk.Label = Label(root, text="Enter your height(cm)")
tk.Label.config(fg="black")
tk.Label.config(padx=40, pady=0)
tk.Label.pack()

# Entry for height
height_entry = Entry(root, width=30)
height_entry.place(x=110, y=140)

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get the values from the entry fields
        weight = weight_entry.get().strip()
        height = height_entry.get().strip()

        # Check if both fields are filled
        if weight == "" or height == "":
            error_message.set("Both fields must be filled")  # Set specific error message
            bmi_result.set("")  # Clear BMI result
            return  # Exit the function early

        weight = float(weight)  # Convert weight to float
        height = float(height) / 100  # Convert height from cm to meters

        bmi = weight / (height ** 2)  # Calculate BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display BMI result and clear error message
        bmi_result.set(f"Your BMI is: {bmi:.2f} ({category})")
        error_message.set("")  # Clear error message
    except ValueError as e:
        # Show error message when invalid input is provided
        bmi_result.set("")
        error_message.set("Please enter valid numbers!")  # Show custom error message

# Add a label to display the BMI result
bmi_result = tk.StringVar()
Label(root, textvariable=bmi_result, bg='lightblue').place(x=120, y=200)

# Add a label for error messages (start with no message)
error_message = tk.StringVar()
error_label = Label(root, textvariable=error_message, fg="red")
error_label.place(x=120, y=230)

# Button to trigger BMI calculation
my_button = Button(root, text="Calculate", command=calculate_bmi)
my_button.place(x=170, y=170)

#main loop
root.mainloop()



