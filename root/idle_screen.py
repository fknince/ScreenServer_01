import tkinter as tk
import threading


def showScreen(screen_id, screen_url, screen_port, safety_code,call_endpoint):
    def start_mainloop():
        ROOT = tk.Tk()
        ROOT.title("Waiting To Connection...")
        ROOT.geometry("1000x600")

        server_info = {
            "Screen Id": screen_id,
            "Screen Access URL": screen_url,
            "Screen Access Port": screen_port,
            "Safety Token": safety_code
        }

        container = tk.Frame(ROOT, width=700, height=500)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        for i, (label, value) in enumerate(server_info.items()):
            tk.Label(container, text=label, font=("Arial", 12)).grid(row=i, column=0)
            entry = tk.Entry(container, textvariable=tk.StringVar(value=value), state='readonly', font=("Arial", 16))
            entry.grid(row=i, column=1)
            entry.config(width=50)
        entry = tk.Entry(container, textvariable=tk.StringVar(value=call_endpoint), state='readonly', font=("Arial", 16))
        entry.grid(row=i, column=0, columnspan=2)
        entry.config(width=70, justify='center')
        # Do any initialization here
        # ...

        # Start the mainloop
        ROOT.mainloop()

    mainloop_thread = threading.Thread(target=start_mainloop)
    mainloop_thread.start()

    # Continue with the rest of your code here

    # Wait for the mainloop thread to finish
    mainloop_thread.join()


