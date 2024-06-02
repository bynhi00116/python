from tkinter import *
from PyDictionary import PyDictionary


def buttonClick():
    dictionary = PyDictionary()
    meaning = dictionary.meaning(input_value.get())
    print(meaning)
    text = ""
    b = "•"
    for key in meaning.keys():
        text += key.capitalize()+":\n"
        for value in meaning[key]:
            text += b+value+"\n"
    print(text)
    output.delete(CURRENT, END)
    output.insert(CURRENT, text)


main = Tk()
main.title('Dictionary')
input_value = StringVar()
title = Label(main, font=("arial", 20, "bold"), text="Dictonary")
title.grid(columnspan=2)
text_entry = Entry(main, font=("arial", 16, "normal"),
                   textvariable=input_value)
text_entry.grid(row=1, column=0)
search_btn = Button(main, font=("arial", 14, "normal"),
                    text="Search", command=buttonClick)
search_btn.grid(row=1, column=1)
output = Text(main, width=40, font=("arial", 12, "normal"))
output.grid(columnspan=2)

main.mainloop()
