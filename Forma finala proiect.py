import tkinter as tk
from time import time

# calculate the accuracy of input prompt
def typingErrors(prompt, iprompt):
    iwords = prompt.split()
    words = iprompt.split()
    errors = 0
    wrong_words = []

    for i in range(len(iwords)):
        if i >= len(words):  # Handles cases where user types fewer words
            errors += 1
            wrong_words.append(iwords[i])
        elif iwords[i] != words[i]:
            errors += 1
            wrong_words.append(iwords[i])

    return errors, wrong_words

# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / (etime - stime) * 60  # Calculate speed as words per minute

    return speed

# calculate total time elapsed
def timeElapsed(stime, etime):
    return etime - stime

# count total letters typed
def letterCount(iprompt):
    return sum(1 for char in iprompt if char.isalpha())

def start_typing_test():
    prompt = ("Tehnologia informatiei evolueaza rapid, conectand lumi diferite si oferind "
              "solutii inovative care transforma modul in care lucram si traim.")

    def start_test():
        global stime
        stime = time()
        input_text.delete(1.0, tk.END)
        input_text.config(state=tk.NORMAL)
        input_text.focus()
        start_button.config(state=tk.DISABLED)

    def finish_test(event=None):
        etime = time()
        iprompt = input_text.get(1.0, tk.END).strip()
        elapsed_time = round(timeElapsed(stime, etime), 2)
        speed = typingSpeed(iprompt, stime, etime)
        errors, wrong_words = typingErrors(prompt, iprompt)
        total_letters = letterCount(iprompt)

        result_label.config(text=(
            f"Total Time Elapsed: {elapsed_time} s\n"
            f"Your Average Typing Speed: {round(speed, 2)} words/min\n"
            f"Total Errors: {errors}\n"
            f"Total Letters Typed: {total_letters}\n"
            f"Incorrect Words: {', '.join(wrong_words) if wrong_words else 'None'}"
        ))
        input_text.config(state=tk.DISABLED)
        start_button.config(state=tk.NORMAL)

    def show_elapsed_time():
        result_label.config(text=f"Total Time Elapsed: {round(timeElapsed(stime, time()), 2)} s")

    def show_speed():
        etime = time()
        iprompt = input_text.get(1.0, tk.END).strip()
        speed = typingSpeed(iprompt, stime, etime)
        result_label.config(text=f"Your Current Typing Speed: {round(speed, 2)} words/min")

    def show_error_details():
        iprompt = input_text.get(1.0, tk.END).strip()
        errors, wrong_words = typingErrors(prompt, iprompt)
        result_label.config(text=(
            f"Total Errors: {errors}\n"
            f"Incorrect Words: {', '.join(wrong_words) if wrong_words else 'None'}"
        ))

    # Create GUI window
    root = tk.Tk()
    root.title("Typing Speed Test")

    # Prompt text
    prompt_label = tk.Label(root, text="Type this:", font=("Arial", 12))
    prompt_label.pack(pady=5)

    prompt_text = tk.Label(root, text=prompt, wraplength=600, font=("Arial", 10), justify="left")
    prompt_text.pack(pady=5)

    # Text input area
    input_text = tk.Text(root, height=5, width=80, state=tk.DISABLED, font=("Arial", 10))
    input_text.pack(pady=10)
    input_text.bind("<Return>", finish_test)

    # Buttons
    start_button = tk.Button(root, text="Start Test", command=start_test, font=("Arial", 12))
    start_button.pack(pady=5)

    elapsed_time_button = tk.Button(root, text="Show Elapsed Time", command=show_elapsed_time, font=("Arial", 12))
    elapsed_time_button.pack(pady=5)

    speed_button = tk.Button(root, text="Show Speed", command=show_speed, font=("Arial", 12))
    speed_button.pack(pady=5)

    error_details_button = tk.Button(root, text="Show Error Details", command=show_error_details, font=("Arial", 12))
    error_details_button.pack(pady=5)

    # Result area
    result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_typing_test()