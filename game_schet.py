from tkinter import *
from tkinter import messagebox as mb
import random as r

class won():
    
    def __init__(self):

        self.otv1Var = StringVar()
        self.otv2Var = StringVar()
        self.txtVar = StringVar()
        self.resVar = StringVar()
        self.kol = 0
        self.mist = 5
        self.resVar.set(f"{self.kol}:{self.mist}")
        
        self.cVar = StringVar()
        self.sp = ["+", "-", "/", "*"]
        self.n = r.choice(self.sp)
        self.cVar.set(self.n)

        if self.n == "+":
            self.a = r.randint(10, 99)
            self.b = r.randint(10, 99)
            self.result = self.a + self.b
        if self.n == "-":
            self.a = r.randint(10, 99)
            self.b = r.randint(10, 99)
            self.result = self.a - self.b
        if self.n == "/":
            self.a = r.randint(1, 20)
            self.b = r.randint(1, 20)
            self.result = self.a // self.b
        if self.n == "*":
            self.a = r.randint(1, 20)
            self.b = r.randint(1, 20)
            self.result = self.a * self.b

        self.otv1Var.set(self.a)
        self.otv2Var.set(self.b)              
        self.lbl1 = Label(tk, textvariable = self.otv1Var, width = 5, height = 2, anchor = "nw", font = "arial 30 bold", bg = "#8cbd95")
        self.lbl1.place(x = 50, y = 50)
        self.lbl3 = Label(tk, textvariable = self.cVar, width = 5, height = 2, anchor = "nw", font = "arial 30 bold", bg = "#8cbd95")
        self.lbl3.place(x = 123, y = 50)
        self.lbl2 = Label(tk, textvariable = self.otv2Var, width = 5, height = 2, anchor = "nw", font = "arial 30 bold", bg = "#8cbd95")
        self.lbl2.place(x = 180, y = 50)
        self.lbl4 = Label(tk, text = "=", width = 5, height = 2, anchor = "nw", font = "arial 30 bold", bg = "#8cbd95")
        self.lbl4.place(x = 230, y = 50)
        self.lbl5 = Label(tk, textvariable = self.resVar, width = 10, font = "arial 20 bold", bg = "#8cbd95")
        self.lbl5.place(x = 290, y = 2)
        self.lbl10 = Label(tk, textvariable = self.txtVar, width = 28, anchor = "nw", font = "arial 10 bold", bg = "#8cbd95")
        self.lbl10.place(x = 130, y = 20)
        
        self.ent1 = Entry(tk, width = 5, font = "arial 30 bold", bg = "#cfefa9")
        self.ent1.place(x = 280, y = 50)

        self.btn1 = Button(tk, text = "ПРОВЕРИТЬ", width = 10, bg = "#cfefa9", command = self.summ)
        self.btn1.place(x = 170, y = 115)
        self.btn2 = Button(tk, text = "Правила", width = 7, bg = "#cfefa9", command = self.check)
        self.btn2.place(x = 2, y = 2)
        self.btn2 = Button(tk, text = "Выход", width = 5, bg = "#cfefa9", command = tk.destroy)
        self.btn2.place(x = 61, y = 2)
        
    def check(self):
        mb.showinfo("Правила", "1.В приложении будут выходить цифры и знак между ними.\n2.Тебе нужно будет посчитать результат и написать его в строку ввода и после нажать на кнопку проверить(если деление то в ответ нужно написать целую часть).\n3.Также у тебя будут жизни)")
                    
    def summ(self):
        self.res = self.ent1.get()
        if self.mist != 0:
            if str(self.result) == self.res:
                self.kol += 1
                self.resVar.set(f"{self.kol}:{self.mist}")
                self.txtVar.set("Ты угадал,молодец!")
                self.ent1.delete(0, END)
                self.res = ""
                self.result = 0
                self.n = r.choice(self.sp)
                self.cVar.set(self.n)
                if self.n == "+":
                    self.a = r.randint(10, 99)
                    self.b = r.randint(10, 99)
                    self.result = self.a + self.b
                if self.n == "-":
                    self.a = r.randint(10, 99)
                    self.b = r.randint(10, 99)
                    self.result = self.a - self.b
                if self.n == "/":
                    self.a = r.randint(1, 20)
                    self.b = r.randint(1, 20)
                    self.result = self.a // self.b
                if self.n == "*":
                    self.a = r.randint(1, 20)
                    self.b = r.randint(1, 20)
                    self.result = self.a * self.b            
                self.otv1Var.set(self.a)
                self.otv2Var.set(self.b)
            else:
                self.kol += 1
                self.mist -= 1
                self.resVar.set(f"{self.kol}:{self.mist}")
                self.txtVar.set("Не правильно,попробуй ещё раз!")
                self.ent1.delete(0, END)
                self.res = ""
                self.result = 0
                self.n = r.choice(self.sp)
                self.cVar.set(self.n)
                if self.n == "+":
                    self.a = r.randint(10, 99)
                    self.b = r.randint(10, 99)
                    self.result = self.a + self.b
                if self.n == "-":
                    self.a = r.randint(10, 99)
                    self.b = r.randint(10, 99)
                    self.result = self.a - self.b
                if self.n == "/":
                    self.a = r.randint(1, 20)
                    self.b = r.randint(1, 20)
                    self.result = self.a // self.b
                if self.n == "*":
                    self.a = r.randint(1, 20)
                    self.b = r.randint(1, 20)
                    self.result = self.a * self.b            
                self.otv1Var.set(self.a)
                self.otv2Var.set(self.b)
        else:
            a = mb.askyesno("Вопрос", "Ты проиграл,хочешь начать заново?")
            if a == True:
                self.kol = 0
                self.mist = 5
                self.resVar.set(f"{self.kol}:{self.mist}")
            else:
                tk.destroy()
            
tk = Tk()
tk.geometry("400x150+500+180")
tk.resizable(False,False)
tk.title("Посчитайка")
tk["bg"] = "#8cbd95"
wn = won()
tk.mainloop()





        
