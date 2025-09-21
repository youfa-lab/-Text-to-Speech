import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3

# ألوان التصميم
BG_MAIN = "#101c11"
FG_MAIN = "#00ff55"
BG_BOX = "#181d1b"
BTN_BG = FG_MAIN
BTN_FG = BG_MAIN
BTN_ACTIVE_BG = "#222"
BTN_ACTIVE_FG = FG_MAIN

# دالة تحويل النص إلى صوت
def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to convert.")
        return
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def save_audio():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.save_to_file(text, file_path)
        engine.runAndWait()
        engine.stop()
        messagebox.showinfo("Success", f"Audio saved to:\n{file_path}")

root = tk.Tk()
root.title("wiki - Text to Speech")
root.geometry("650x400")
root.configure(bg=BG_MAIN)
root.resizable(False, False)

header = tk.Label(root, text="wiki", font=("Arial", 22, "bold"), bg=BG_MAIN, fg=FG_MAIN)
header.pack(pady=(18, 2))

label = tk.Label(root, text="Enter text to convert to speech:", font=("Arial", 14, "bold"), bg=BG_MAIN, fg=FG_MAIN)
label.pack(pady=6)

text_box = tk.Text(root, font=("Arial", 13), width=62, height=7, bg=BG_BOX, fg=FG_MAIN, insertbackground=FG_MAIN, borderwidth=2, relief=tk.FLAT, wrap=tk.WORD)
text_box.pack(pady=5, padx=16)

btn_frame = tk.Frame(root, bg=BG_MAIN)
btn_frame.pack(pady=18)

speak_btn = tk.Button(
    btn_frame, text="🔊 Speak", font=("Arial", 12, "bold"),
    bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_ACTIVE_FG,
    command=speak_text, borderwidth=0, height=2, width=14, cursor="hand2"
)
speak_btn.pack(side=tk.LEFT, padx=16)

save_btn = tk.Button(
    btn_frame, text="💾 Save Audio", font=("Arial", 12, "bold"),
    bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_ACTIVE_FG,
    command=save_audio, borderwidth=0, height=2, width=14, cursor="hand2"
)
save_btn.pack(side=tk.LEFT, padx=16)

footer = tk.Label(root, text="Name:Youssef Ait Abbas", font=("Arial", 10), bg=BG_MAIN, fg=FG_MAIN)
footer.pack(side=tk.BOTTOM, pady=6)

root.mainloop()