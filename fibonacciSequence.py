import customtkinter as ctk

def run():
    try:
        seeds = [int(seedOneEntry.get()), int(seedTwoEntry.get())]
        iterate = iterateEntry.get()
        i = 0
        while i < int(iterate)-2:
            seeds.append(seeds[-1] + seeds[-2])
            i += 1
        resultWin = ctk.CTkToplevel()
        resultWin.title("Result")
        resultWin.resizable(False, False)
        if checkbox.get() == 1:
            result = ctk.CTkLabel(resultWin, bg_color = "transparent", text = str(seeds).strip("[]"), font = ("Arial", 35))
        else:
            result = ctk.CTkLabel(resultWin, bg_color = "transparent", text = str(seeds[-1]), font = ("Arial", 35))
        result.pack(padx = 10 , pady = 10)
    except:
        resultWin = ctk.CTkToplevel()
        resultWin.title("Error")
        resultWin.resizable(False, False)
        result = ctk.CTkLabel(resultWin, bg_color = "transparent", text = "Invalid Input", font = ("Arial", 35))
        result.pack(padx = 10, pady = 10)

ctk.set_appearance_mode("dark")

window = ctk.CTk()
window.title("Fibonacci Sequence")
window.geometry("500x280")
window.resizable(False, False)

title = ctk.CTkLabel(window, width = 35, height = 35, bg_color = "transparent", text = "Fibonacci Sequence", font = ("Arial", 35))
title.pack(pady = 10)

seedOneEntry = ctk.CTkEntry(window, placeholder_text = "First seed number", font = ("Arial", 12))
seedOneEntry.pack(pady = 10)

seedTwoEntry = ctk.CTkEntry(window, placeholder_text = "Second seed number", font = ("Arial", 12))
seedTwoEntry.pack()

iterateEntry = ctk.CTkEntry(window, placeholder_text = "Iteration amount", font = ("Arial", 12))
iterateEntry.pack(pady = 10)

checkbox = ctk.CTkCheckBox(window, text = "Show the whole sequence", font = ("Arial", 12))
checkbox.pack()

enter = ctk.CTkButton(window, text = "Enter", text_color = "#ffffff", command = run)
enter.pack(pady = 15)

window.mainloop()
