import customtkinter



def CheckCashOut(yourOriginalBet, ogBetProfit, cashoutProfit,hedgedAgainstOdds,label):
    maxWinnings = 0
    amountHedged = 0
    testWinnings = 0
    bestHedge = 0

    if hedgedAgainstOdds > 0:
        internalOdds = hedgedAgainstOdds / 100
    else:
        hedgedAgainstOdds *= -1
        internalOdds = 100 / hedgedAgainstOdds

    while yourOriginalBet > amountHedged:
        amountHedged += 0.01
        amountHedged = round(amountHedged, 2)
        # print(amountHedged)
        hedgedPotentialWinningsCase1 = (internalOdds * amountHedged) - yourOriginalBet
        hedgedPotentialWinningsCase2 = ogBetProfit - amountHedged

        guaranteedFromTheseCases = min(hedgedPotentialWinningsCase1, hedgedPotentialWinningsCase2)
        if guaranteedFromTheseCases > maxWinnings:
            maxWinnings = guaranteedFromTheseCases
            bestHedge = amountHedged
        hedgedPotentialWinningsCase1 = 0
        hedgedPotentialWinningsCase2 = 0
        guaranteedFromTheseCases = 0

    if maxWinnings > cashoutProfit:
        returnText = (
    	"You could take ${0:.2f} right now\n Instead you should hedge against yourself and guarantee ${1:.2f}\n Bet ${2:.2f} against yourself to win more".format(cashoutProfit,maxWinnings,bestHedge)
		)

    else:
        returnText = "There is no better hedge available, cash out if you are too scared to stay on your original bet..."
    
    print(returnText)

    label.configure(text=returnText)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.geometry("650x800")
root.title("Cash Out Helper")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=30,padx=75,fill="both",expand=True)

label1Font=("Comic Sans",24)
label1 = customtkinter.CTkLabel(master=frame, text="Find out whether you should cash out or not!",font=label1Font)
label1.pack(pady=8, padx=10,expand=True)

label2Font=("Comic Sans",16)
label2 = customtkinter.CTkLabel(master=frame, text="Time to make Money",font=label2Font)
label2.pack(pady=12, padx=10,expand=True)

entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Original Bet")
entry1.pack(pady=12,padx=10,expand=True)

entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Original Bet Profit")
entry2.pack(pady=12,padx=10,expand=True)

entry3=customtkinter.CTkEntry(master=frame,placeholder_text="Cashout Profit")
entry3.pack(pady=12,padx=10,expand=True)

entry4=customtkinter.CTkEntry(master=frame,placeholder_text="Odds against")
entry4.pack(pady=12,padx=10,expand=True)

button=customtkinter.CTkButton(master=frame,text="Enter",command=lambda: CheckCashOut(float(entry1.get()),float(entry2.get()),float(entry3.get()),float(entry4.get()),label2))
button.pack(pady=20,padx=14,expand=True)

root.mainloop()


