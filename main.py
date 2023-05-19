'''
E-mail: mohammad78.seif@yahoo.com
tellgram id: @seifmohammad
'''
#1----------
from tkinter import *
import random
import datetime
from tkinter import messagebox
import os
#----------------------------------------


#2-------Create main window
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x780")
        self.root.title("Restaurant Billing Sotware")
        bgcolor = "#a9c9fc"
        title = Label(self.root, text="Restaurant Billing Software", bd=12, relief=GROOVE, bg=bgcolor, fg="white",
                      font=("algerian", 30, "bold"), pady=2).pack(fill=X)
        # self.root.wm_iconbitmap("favicon.ico")
        #----------------------------------------

#4 ================== Variables ++++++++++++++++++++

        self.GreekPizza = IntVar()
        self.ChicagoPizza = IntVar()
        self.MargheritaPizza = IntVar()
        self.cheeseburger = IntVar()
        self.eggsBenedict = IntVar()
        self.spaghetti = IntVar()
        self.lasagna = IntVar()
        self.fishandchips = IntVar()
        self.sushi = IntVar()
        self.biryani = IntVar()
        self.Greeksalad = IntVar()
        self.kebab = IntVar()
        self.shishkebab = IntVar()
        self.hotdog = IntVar()
        #drinks
        self.Coffee = IntVar()
        self.Fanta = IntVar()
        self.Sprite = IntVar()
        self.Lemonade = IntVar()
        self.Milkshake = IntVar()
        self.Icedtea = IntVar()
        self.Pepsi = IntVar()




        #11 ================== set per unit ++++++++++++++++++++
        self.uGreekPizza = 150
        self.uChicagoPizza = 140
        self.uMargheritaPizza = 130
        self.ucheeseburger = 160
        self.ueggsBenedict = 180
        self.uspaghetti = 150
        self.ulasagna = 160
        self.ufishandchips = 200
        self.usushi = 180
        self.ubiryani = 210
        self.uGreeksalad = 170
        self.ukebab = 175
        self.ushishkebab = 180
        self.uhotdog = 150
        #---drink
        self.uCoffee  = 50
        self.ufanta = 50
        self.usprite = 50
        self.uLemonade = 40
        self.uMilkshake = 40
        self.uIcedtea =45
        self.upepsi = 55

        # ===================== Total item price  +++++++++++++++++++

        self.Total_momo = StringVar()
        self.Total_cd = StringVar()
        self.Service_charge = StringVar()
        self.Total_pay = StringVar()

        # +++++++++++++++++ customer details variables ++++++++++++++++

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        xt = random.randint(10000, 99999)
        self.bill_no.set(str(xt))
        self.search_bill = StringVar()
        #----------------------------------------

        #5----------------------------------------
        f1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg="black")
        f1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1, width=20, textvariable=self.c_name, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                column=1,
                                                                                                                pady=5,
                                                                                                                padx=10)

        cphone_lbl = Label(f1, text="Phone Number", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(f1, width=20, textvariable=self.c_phone, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  pady=5,
                                                                                                                  padx=10)

        cbill_lbl = Label(f1, text="Bill Number", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1, width=20, textvariable=self.search_bill, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(f1, text="Search", width=10, bd=7, font="arial 12 bold", command=self.find_bill).grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=60,
                                                                                                                pady=10)
        #----------------------------------------
        #6+++++++++++Momo frame +++++++++++++
        f2 = LabelFrame(self.root, text="MENU", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f2.place(x=5, y=185, width=665, height=430)



        GreekPizza_lbl = Label(f2, text="Greek Pizza", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(
            row=0, column=0, padx=10, pady=10, sticky=W)
        GreekPizza_txt = Entry(f2, width=10, textvariable=self.GreekPizza, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        #-------

        ChicagoPizza_lbl = Label(f2, text="Chicago Pizza", font=("times new roman", 16, "bold"), bg=bgcolor,
                                fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ChicagoPizza_txt = Entry(f2, width=10, textvariable=self.ChicagoPizza, font=("times new roman", 16, "bold"), bd=5,
                                relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        

        #-------

        MargheritaPizza_lbl = Label(f2, text="Margherita Pizza", font=("times new roman", 16, "bold"), bg=bgcolor,
                                fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        MargheritaPizza_txt = Entry(f2, width=10, textvariable=self.MargheritaPizza, font=("times new roman", 16, "bold"), bd=5,
                                relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        

        #-------

        cheeseburger_lbl = Label(f2, text="cheese burgerl", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        cheeseburger_txt = Entry(f2, width=10, textvariable=self.cheeseburger, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

#-------


        eggsBenedict_lbl = Label(f2, text="eggs Benedict", font=("times new roman", 16, "bold"), bg=bgcolor,
                                fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        eggsBenedict_txt = Entry(f2, width=10, textvariable=self.eggsBenedict, font=("times new roman", 16, "bold"), bd=5,
                                relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        

        #-------

        spaghetti_lbl = Label(f2, text="spaghetti", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        spaghetti_txt = Entry(f2, width=10, textvariable=self.spaghetti, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


#-------

        lasagna_lbl = Label(f2, text="lasagna", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        lasagna_txt = Entry(f2, width=10, textvariable=self.lasagna, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)


#-------
        fishandchips_lbl = Label(f2, text="fishandchips", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        fishandchips_txt = Entry(f2, width=10, textvariable=self.fishandchips, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)

#-------
        sushi_lbl = Label(f2, text="sushi", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        sushi_txt = Entry(f2, width=10, textvariable=self.sushi, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)


        biryani_lbl = Label(f2, text="biryani", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        biryani_txt = Entry(f2, width=10, textvariable=self.biryani, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        #-------#-------

        Greeksalad_lbl = Label(f2, text="Greek salad", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=3, column=2, padx=10, pady=10, sticky="w")
        Greeksalad_txt = Entry(f2, width=10, textvariable=self.Greeksalad, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3, column=3, padx=10, pady=10)

        #-------

        kebab_lbl = Label(f2, text="kebab", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=4, column=2, padx=10, pady=10, sticky="w")
        kebab_txt = Entry(f2, width=10, textvariable=self.kebab, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=4, column=3, padx=10, pady=10)
        

        #--shishkebab

        shishkebab_lbl = Label(f2, text="shish kebab", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=5, column=2, padx=10, pady=10, sticky="w")
        shishkebab_txt = Entry(f2, width=10, textvariable=self.shishkebab, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=3, padx=10, pady=10)
        

        #-------#-------

        hotdog_lbl = Label(f2, text="hotdog", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="black").grid(row=6, column=2, padx=10, pady=10, sticky="w")
        hotdog_txt = Entry(f2, width=10, textvariable=self.hotdog, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=6, column=3, padx=10, pady=10)
        
        #-------#------- 
        #----------------------------------------
        #7 ++++++++++++ Cold Drinks frame +++++++
        f4 = LabelFrame(self.root, text="Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f4.place(x=675, y=185, width=325, height=430)

        Coffee_lbl = Label(f4, text="Coffee", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        Coffee_txt = Entry(f4, width=10, textvariable=self.Coffee, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        

        #-------#-------#-------

        Fanta_lbl = Label(f4, text="fanta", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Fanta_txt = Entry(f4, width=10, textvariable=self.Fanta, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        #-------#-------#-------#-------

        Sprite_lbl = Label(f4, text="Sprite", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Sprite_txt = Entry(f4, width=10, textvariable=self.Sprite, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        #-------#-------#-------#-------

        Lemonade_lbl = Label(f4, text="Lemonade", font=("times new roman", 16, "bold"), bg=bgcolor,
                        fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Lemonade_txt = Entry(f4, width=10, textvariable=self.Milkshake, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        

        #-------#-------#-------

        Milkshake_lbl = Label(f4, text="Milkshake", font=("times new roman", 16, "bold"), bg=bgcolor,
                        fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Milkshake_txt = Entry(f4, width=10, textvariable=self.Icedtea, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        

        #-------#-------#-------#-------

        Icedtea_lbl = Label(f4, text="Icedtea", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        Icedtea_txt = Entry(f4, width=10, textvariable=self.Icedtea, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        
        #-------#-------#-------#-------#-------

        Pepsi_lbl = Label(f4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bgcolor, fg="black").grid(
            row=6, column=0, padx=10, pady=10, sticky="w")
        Pepsi_txt = Entry(f4, width=10, textvariable=self.Pepsi, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)
        
        #-------#-------#-------#-------#-------
        
        #----------------------------------------
        # 8 ++++++++++++ Bill area frame ++++++++++++++

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1010, y=185, width=585, height=430)
        bill_title = Label(f5, text="Details", font=("arial 15 bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        #----------------------------------------
        # 9 +++++++++++ Button Frame +++++++++++++

        f6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f6.place(x=0, y=625, relwidth=1, height=160)

        m1_lbl = Label(f6, text="Total  Price", bg=bgcolor, fg="white",
                    font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky="w")
        m1_txt = Entry(f6, width=18, textvariable=self.Total_momo, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=2)

        m2_lbl = Label(f6, text="Total Drinks Price", bg=bgcolor, fg="white",
                    font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        m2_txt = Entry(f6, width=18, textvariable=self.Total_cd, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=2)

        t1_lbl = Label(f6, text="Service Charge", bg=bgcolor, fg="white",
                    font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky="w")
        t1_txt = Entry(f6, width=18, textvariable=self.Service_charge, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=2)

    

        t2_lbl = Label(f6, text="Total Payment", bg=bgcolor, fg="white",
                    font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=5, sticky="w")
        t2_txt = Entry(f6, width=18, textvariable=self.Total_pay, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=2)
        #----------------------------------------
        #10 +++++++++++++++ main button frame
        
        btn_frame = Frame(f6, bd=7, relief=GROOVE)
        btn_frame.place(x=1000, width=580, height=100)

        total_btn = Button(btn_frame, text="Total", bg="#00F9FF", fg="black", pady=10, bd=5,
                        width=8,font=("arial 15 bold"), command=self.total).grid(row=0, column=0, padx=5, pady=5)
        
        Bill_btn = Button(btn_frame, text=("Generate Bill"), bg="yellow", fg="black", pady=10,
                        width=12,bd=5,  font=("arial 15 bold"), command=self.bill_area).grid(row=0, column=1, padx=5, pady=5)
        
        Clear_btn = Button(btn_frame, text="Clear", bg="#F66323", fg="black", pady=10, bd=5,
                        width=10,font=("arial 15 bold"), command=self.clear_data).grid(row=0, column=2, padx=5, pady=5)
        
        Exit_btn = Button(btn_frame, text="Exit", bg="red", fg="black", pady=10, bd=5,
                        width=8,font=("arial 15 bold"), command=self.exit_app).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
        
#12_____________ functions_____________________________
#####----12-----######
    def total(self):
        self.Total_momoo = float(
            (self.GreekPizza.get() * self.uGreekPizza) +
            (self.ChicagoPizza.get() * self.uChicagoPizza) +
            (self.MargheritaPizza.get() * self.uMargheritaPizza) +
            (self.cheeseburger.get() * self.ucheeseburger) +
            (self.eggsBenedict.get() * self.ueggsBenedict) +
            (self.spaghetti.get() * self.uspaghetti) +
            (self.lasagna.get() * self.ulasagna)+
            (self.fishandchips.get() * self.ufishandchips)+
            (self.sushi.get() * self.usushi) +
            (self.biryani.get() * self.ubiryani) +
            (self.Greeksalad.get() * self.uGreeksalad) +
            (self.kebab.get() * self.ukebab) +
            (self.shishkebab.get() * self.ushishkebab) +
            (self.hotdog.get() * self.uhotdog)
        )
        self.Total_momo.set("$ " + str(self.Total_momoo))

        # calculating total for cold drinks products
        self.total_cdrinks_price = float(
            (self.Coffee.get() * self.uCoffee) +
            (self.Sprite.get() * self.usprite) +
            (self.Fanta.get() * self.ufanta) +
            (self.Lemonade.get() * self.uLemonade) +
            (self.Milkshake.get() * self.uMilkshake) +
            (self.Icedtea.get() * self.uIcedtea) +
            (self.Pepsi.get() * self.upepsi)
        )
        self.Total_cd.set("$ " + str(self.total_cdrinks_price))

        self.Service_charge.set("$ " + str(round((self.total_cdrinks_price+self.Total_momoo) * 0.10, 2)))
        self.Total_pay.set(self.Total_momoo + self.total_cdrinks_price + round(
            (self.total_cdrinks_price + self.Total_momoo) * 0.10, 2))
        self.Total_payy = self.Total_momoo + self.total_cdrinks_price + round((self.total_cdrinks_price+self.Total_momoo) * 0.10, 2)



    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tWELLCOME OUSA CENTER\n")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        x = datetime.datetime.now()
        datee = x.strftime("%Y/%m/%d\t%H:%M:%S")
        self.txtarea.insert(END, f"\nDate:{datee}")
        self.txtarea.insert(END, "\n=========================================================")
        self.txtarea.insert(END, "\nItems \t\t QTY \t Unit_Price\t\tTotal_Price")
        self.txtarea.insert(END, "\n=========================================================")



    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif (self.Total_momo.get() == "$ 0.0" and self.Total_cd.get() == "$ 0.0"):
            messagebox.showerror("Error", "No products purchased")
        else:
            self.welcome_bill()

            if (self.GreekPizza.get() != 0):
                self.txtarea.insert(END,
                                    f"\nGreek Pizza  \t\t {self.GreekPizza.get()} \t $ {self.uGreekPizza}\t\t$ {self.GreekPizza.get() * self.uGreekPizza} ")

            if (self.ChicagoPizza.get() != 0):
                self.txtarea.insert(END,
                                    f"\nChicago Pizza \t\t {self.ChicagoPizza.get()} \t $ {self.uChicagoPizza}\t\t$ {self.ChicagoPizza.get() * self.uChicagoPizza} ")

            if (self.MargheritaPizza.get() != 0):
                self.txtarea.insert(END,
                                    f"\nMargherita Pizza  \t\t {self.MargheritaPizza.get()} \t $ {self.uMargheritaPizza}\t\t$ {self.MargheritaPizza.get() * self.uMargheritaPizza} ")

            if (self.cheeseburger.get() != 0):
                self.txtarea.insert(END,
                                    f"\ncheese burger \t\t {self.cheeseburger.get()} \t $ {self.ucheeseburger}\t\t$ {self.cheeseburger.get() * self.ucheeseburger} ")

            if (self.eggsBenedict.get() != 0):
                self.txtarea.insert(END,
                                    f"\neggs Benedict \t\t {self.eggsBenedict.get()} \t $ {self.ueggsBenedict}\t\t$ {self.eggsBenedict.get() * self.ueggsBenedict} ")

            if (self.spaghetti.get() != 0):
                self.txtarea.insert(END,
                                    f"\nspaghetti \t\t {self.spaghetti.get()} \t $ {self.uspaghetti}\t\t$ {self.spaghetti.get() * self.uspaghetti} ")

            if (self.lasagna.get() != 0):
                self.txtarea.insert(END,
                                    f"\nlasagna  \t\t {self.lasagna.get()} \t $ {self.ulasagna}\t\t$ {self.lasagna.get() * self.ulasagna} ")

            if (self.fishandchips.get() != 0):
                self.txtarea.insert(END,
                                    f"\nfish and chips  \t\t {self.fishandchips.get()} \t $ {self.ufishandchips}\t\t$ {self.fishandchips.get() * self.ufishandchips} ")

            if (self.sushi.get() != 0):
                self.txtarea.insert(END,
                                    f"\nsushi  \t\t {self.sushi.get()} \t $ {self.usushi}\t\t$ {self.sushi.get() * self.usushi} ")

            if (self.biryani.get() != 0):
                self.txtarea.insert(END,
                                    f"\nbiryani  \t\t {self.biryani.get()} \t $ {self.ubiryani}\t\t$ {self.biryani.get() * self.ubiryani} ")

            if (self.Greeksalad.get() != 0):
                self.txtarea.insert(END,
                                    f"\nGreek salad  \t\t {self.Greeksalad.get()} \t $ {self.uGreeksalad}\t\t$ {self.Greeksalad.get() * self.uGreeksalad} ")

            if (self.kebab.get() != 0):
                self.txtarea.insert(END,
                                    f"\nkebab  \t\t {self.kebab.get()} \t $ {self.ukebab}\t\t$ {self.kebab.get() * self.ukebab} ")

            if (self.shishkebab.get() != 0):
                self.txtarea.insert(END,
                                    f"\nshish kebab  \t\t {self.shishkebab.get()} \t $ {self.ushishkebab}\t\t$ {self.shishkebab.get() * self.ushishkebab} ")

            if (self.hotdog.get() != 0):
                self.txtarea.insert(END,
                                    f"\nhotdog  \t\t {self.hotdog.get()} \t $ {self.uhotdog}\t\t$ {self.hotdog.get() * self.uhotdog} ")

            # =============== for cold drinks ==================

            if (self.Coffee.get() != 0):
                self.txtarea.insert(END,
                                    f"\nCoffee \t\t {self.Coffee.get()} \t $ {self.uCoffee}\t\t$ {self.Coffee.get() * self.uCoffee} ")

            if (self.Fanta.get() != 0):
                self.txtarea.insert(END,
                                    f"\nFanta \t\t {self.Fanta.get()} \t $ {self.ufanta}\t\t$ {self.Fanta.get() * self.ufanta} ")

            if (self.Sprite.get() != 0):
                self.txtarea.insert(END,
                                    f"\nSprite \t\t {self.Sprite.get()} \t $ {self.usprite}\t\t$ {self.Sprite.get() * self.usprite} ")

            if (self.Lemonade.get() != 0):
                self.txtarea.insert(END,
                                    f"\n Lemonade \t\t {self.Lemonade.get()} \t $ {self.uLemonade}\t\t$ {self.Lemonade.get() * self.uLemonade} ")

            if (self.Milkshake.get() != 0):
                self.txtarea.insert(END,
                                    f"\nMilkshake \t\t {self.Milkshake.get()} \t $ {self.uMilkshake}\t\t$ {self.Milkshake.get() * self.uMilkshake} ")

            if (self.Icedtea.get() != 0):
                self.txtarea.insert(END,
                                    f"\nIced tea \t\t {self.Icedtea.get()} \t $ {self.uIcedtea}\t\t$ {self.Icedtea.get() * self.uIcedtea} ")

            if (self.Pepsi.get() != 0):
                self.txtarea.insert(END,
                                    f"\nPepsi \t\t {self.Pepsi.get()} \t $ {self.upepsi}\t\t$ {self.Pepsi.get() * self.upepsi} ")

            self.txtarea.insert(END, "\n---------------------------------------------------------")
            if (self.Total_momo.get() != " 0.0 $"):
                self.txtarea.insert(END, f"\nTotal MOMO Payment:\t\t{self.Total_momo.get()}")

            if (self.Total_cd.get() != " 0.0 $"):
                self.txtarea.insert(END, f"\nTotal Cold Drinks Payment:\t\t{self.Total_cd.get()}")

            if (self.Service_charge.get() != " 0.0 $"):
                self.txtarea.insert(END, f"\nTotal Service Charge(10%):\t\t{self.Service_charge.get()}")

            self.txtarea.insert(END, "\n---------------------------------------------------------")

            self.txtarea.insert(END, f"\nTotal Payment: {self.Total_payy} \t\t$")
            self.txtarea.insert(END, "\n---------------------------------------------------------")
            self.save_bill()

    #+============== Function for saving the bill +++++++++++++++++++++

    def save_bill(self):
        op = messagebox.askyesno("Save", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/Bill" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill: {self.bill_no.get()} saved successfully")
        else:
            return
    #++++++++++++++++++= Function for searching the bill ++++++++++++++++++++++


    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills"):    
            if i.split(".")[0] == 'Bill'+self.search_bill.get():
                #f1 = open(f"Bills{i}", "r")
                f1 = open("Bills/"+i, "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Bill Not Found")

    #++++++++++++++++++++++ Function for clearing the data ++++++++++++++++++++

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data?")
        if op > 0:
            # ==================set Variables to 0 ++++++++++++++++++++
            self.GreekPizza.set(0)
            self.ChicagoPizza.set(0)
            self.MargheritaPizza.set(0)
            self.cheeseburger.set(0)
            self.eggsBenedict.set(0)
            self.spaghetti.set(0)
            self.lasagna.set(0)
            self.fishandchips.set(0)
            self.sushi.set(0)
            self.biryani.set(0)
            self.Greeksalad.set(0)
            self.kebab.set(0)
            self.shishkebab.set(0)
            self.hotdog.set(0)
            self.Coffee.set(0)
            self.Fanta.set(0)
            self.Sprite.set(0)
            self.Lemonade.set(0)
            self.Milkshake.set(0)
            self.Icedtea.set(0)
            self.Pepsi.set(0)

            self.Total_momo.set("")
            self.Total_cd.set("")
            self.Service_charge.set("")
            self.Total_pay.set("")

            # +++++++++++++++++ customer details  ++++++++++++++++
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            xt = random.randint(10000, 99999)
            self.bill_no.set(str(xt))
            self.search_bill.set("")
            self.welcome_bill()

    #++++++++++++++ Function for exiting the app++++++++++++++++++

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op > 0:
            self.root.destroy()



#3---------------Run
if __name__ == "__main__":
    root = Tk()
    root.attributes("-topmost", True)
    obj = Bill_App(root)
    root.mainloop()