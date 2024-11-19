import tkinter as tk
import pyttsx3
import webbrowser
from datetime import datetime
from plyer import notification

engine = pyttsx3.init()

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
    )

def process_query():
    query = entry.get().lower()
    display_message(f"You: {query}")
    entry.delete(0, tk.END)

    if "open youtube" in query:
        open_youtube()
        speak("Opening YouTube boss!")
    elif "open instagram" in query:
        open_instagram()
        speak("Opening Instagram boss!")
    elif "thanks jarvis" in query:
        speak("You're welcome boss!")
    elif "set reminder" in query:
        set_reminder(query)
    else:
        speak("Sorry, boss. I cannot help with that.")
        
def open_youtube():
    webbrowser.open("https://www.youtube.com/")
def open_instagram():
    webbrowser.open("https://www.instagram.com/")

def speak(text):
    print(f"JARVIS: {text}")
    current_time = datetime.now().strftime("%I:%M %p")
    send_notification("JARVIS", f"{text} ({current_time})")
    engine.say(text)
    engine.runAndWait()

def display_message(message):
    text_box.configure(state=tk.NORMAL)
    text_box.insert(tk.END, message + "\n")
    text_box.configure(state=tk.DISABLED)
    text_box.see(tk.END)

def set_reminder(query):
    try:
        
        parts = query.split("set reminder")
        reminder_text = parts[1].strip()

        time_str = reminder_text.split("at")[1].strip()
        reminder_time = datetime.strptime(time_str, "%H:%M")

        current_time = datetime.now()
        delay_seconds = (reminder_time - current_time).total_seconds()

        if delay_seconds > 0:
            
            tk.after(int(delay_seconds * 1000), send_reminder_notification, reminder_text)
            speak(f"Reminder set for {time_str}.")
            
        else:
            speak("Invalid reminder time. Please specify a future time.")

    except Exception as e:
        speak("Error setting reminder. Please try again.")

def send_reminder_notification(reminder_text):
    send_notification("Reminder", reminder_text)
    speak(f"Reminder: {reminder_text}")

window = tk.Tk()
window.title("JARVIS")


text_box = tk.Text(window, width=60, height=10, bg="black", fg="white", font=("Arial", 12))
text_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


entry = tk.Entry(window, width=50, font=("Arial", 12), bg="white")
entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry.focus()


send_button = tk.Button(window, text="send", font=("Arial", 12), command=process_query)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")


window.configure(bg="black")


window.mainloop()
