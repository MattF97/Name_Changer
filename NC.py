import tkinter as tk



# Function to convert name to numbers
def name_to_numbers():
    name = entry.get()  # Get the name entered by the user
    
    result = ""
    
    # Convert each letter to its corresponding number
    for letter in name:
        result += str(ord(letter) - ord('a') + 1) + " "
    
    # Display the result
    result_label.config(text="Result: " + result)

# Create the main window
root = tk.Tk()
root.title("Name to Number Converter")

# Create a label, entry field, and button
label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Convert", command=name_to_numbers)
button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Run the application
root.mainloop()


