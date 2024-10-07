import RPi.GPIO as GPIO  # Import the GPIO library to control the Raspberry Pi's GPIO pins
import tkinter as tk    # Import the Tkinter library to create the GUI

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LEDs
RED_PIN = 11
GREEN_PIN = 13
BLUE_PIN = 15

# Configure the GPIO pins as outputs
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all_leds():
    GPIO.output(RED_PIN, GPIO.LOW)    # Turn off Red LED
    GPIO.output(GREEN_PIN, GPIO.LOW)  # Turn off Green LED
    GPIO.output(BLUE_PIN, GPIO.LOW)   # Turn off Blue LED

# Function to turn on a specific LED
def turn_on_led(led_choice):
    turn_off_all_leds()  # Ensure all LEDs are off before turning on the selected one
    if led_choice == 1:
        GPIO.output(RED_PIN, GPIO.HIGH)    # Turn on Red LED
    elif led_choice == 2:
        GPIO.output(GREEN_PIN, GPIO.HIGH)  # Turn on Green LED
    elif led_choice == 3:
        GPIO.output(BLUE_PIN, GPIO.HIGH)   # Turn on Blue LED

# Function to handle LED selection from radio buttons
def handle_led_selection():
    selected_led = led_var.get()  # Get the selected LED from the radio buttons
    turn_on_led(selected_led)     # Turn on the selected LED

# Function to clean up GPIO and close the application
def close_application():
    turn_off_all_leds()  # Turn off all LEDs before exiting
    GPIO.cleanup()       # Reset GPIO settings to default
    app.quit()           # Close the GUI window

# Create the main application window
app = tk.Tk()
app.title("LED Controller")  # Set the title of the window

# Variable to store the selected LED choice
led_var = tk.IntVar()

# Create and pack the widgets
# Label for the GUI
tk.Label(app, text="Control LEDs", font=("Arial", 20)).pack(pady=10)  

# Radio button for Red LED
tk.Radiobutton(app, text="Red LED", variable=led_var, value=1, command=handle_led_selection).pack(anchor=tk.W, padx=20) 
# Radio button for Green LED
tk.Radiobutton(app, text="Green LED", variable=led_var, value=2, command=handle_led_selection).pack(anchor=tk.W, padx=20)  
# Radio button for Blue LED
tk.Radiobutton(app, text="Blue LED", variable=led_var, value=3, command=handle_led_selection).pack(anchor=tk.W, padx=20)
# Button to turn off all LEDs
tk.Button(app, text="Turn Off All", command=turn_off_all_leds).pack(pady=10)  

# Button to exit the application
tk.Button(app, text="Exit", command=close_application).pack(pady=10)  

# Start the Tkinter event loop
app.mainloop()
