import tkinter as tk
import sys
from tkinter import messagebox

class MainApp(tk.Frame):
	whichPlayerTurn = "Player1"
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		
		fullWindow = tk.Label(self)
		fullWindow.pack()
		
		playersLabel = tk.Label(fullWindow, height = 3, text="Player1 vs Player2" + "\n" + "Your turn, " + MainApp.whichPlayerTurn)
		playersLabel.pack(side=tk.TOP)

		playgroundFrame = tk.Frame(fullWindow)
		playgroundFrame.pack()
		
		playgroundRow1 = tk.Frame(playgroundFrame)
		playgroundRow1.pack()
		playgroundRow2 = tk.Frame(playgroundFrame)
		playgroundRow2.pack()
		playgroundRow3 = tk.Frame(playgroundFrame)
		playgroundRow3.pack()


		pole1 = tk.Button(playgroundRow1, height=3, width=3, text = "", command = lambda: playerClick(pole1))
		pole1.pack(side=tk.LEFT)
		pole2 = tk.Button(playgroundRow1, height=3, width=3, text = "", command = lambda: playerClick(pole2))
		pole2.pack(side=tk.LEFT)
		pole3 = tk.Button(playgroundRow1, height=3, width=3, text = "", command = lambda: playerClick(pole3))
		pole3.pack(side=tk.LEFT)
		pole4 = tk.Button(playgroundRow2, height=3, width=3, text = "", command = lambda: playerClick(pole4))
		pole4.pack(side=tk.LEFT)
		pole5 = tk.Button(playgroundRow2, height=3, width=3, text = "", command = lambda: playerClick(pole5))
		pole5.pack(side=tk.LEFT)
		pole6 = tk.Button(playgroundRow2, height=3, width=3, text = "", command = lambda: playerClick(pole6))
		pole6.pack(side=tk.LEFT)
		pole7 = tk.Button(playgroundRow3, height=3, width=3, text = "", command = lambda: playerClick(pole7))
		pole7.pack(side=tk.LEFT)
		pole8 = tk.Button(playgroundRow3, height=3, width=3, text = "", command = lambda: playerClick(pole8))
		pole8.pack(side=tk.LEFT)
		pole9 = tk.Button(playgroundRow3, height=3, width=3, text = "", command = lambda: playerClick(pole9))
		pole9.pack(side=tk.LEFT)




		def playerClick(button):
			if(MainApp.whichPlayerTurn == "Player1"):
				button.config(text="X", state=tk.DISABLED)
				MainApp.whichPlayerTurn = "Player2"
				playersLabel.config(fullWindow, height = 3, text="Player1 vs Player2" + "\n" + "Your turn, " + MainApp.whichPlayerTurn)
				checkIfPlayer1Win()
				checkIfPlayer2Win()
			elif(MainApp.whichPlayerTurn == "Player2"):
				button.config(text="O", state=tk.DISABLED)
				MainApp.whichPlayerTurn = "Player1"
				playersLabel.config(fullWindow, height = 3, text="Player1 vs Player2" + "\n" + "Your turn, " + MainApp.whichPlayerTurn)
				checkIfPlayer1Win()
				checkIfPlayer2Win()

		def checkIfPlayer1Win():
			if( (pole1['text'] == "X" and pole2['text'] == "X" and pole3['text'] == "X") or
				(pole4['text'] == "X" and pole5['text'] == "X" and pole6['text'] == "X") or
				(pole7['text'] == "X" and pole8['text'] == "X" and pole9['text'] == "X") or
				(pole1['text'] == "X" and pole4['text'] == "X" and pole7['text'] == "X") or
				(pole2['text'] == "X" and pole5['text'] == "X" and pole8['text'] == "X") or
				(pole3['text'] == "X" and pole6['text'] == "X" and pole9['text'] == "X") or
				(pole1['text'] == "X" and pole5['text'] == "X" and pole9['text'] == "X") or
				(pole3['text'] == "X" and pole5['text'] == "X" and pole7['text'] == "X")):
				message = messagebox.showinfo("We have a winner!", "Player1 wins!")
				root.destroy()
				sys.exit(1)

		def checkIfPlayer2Win():
			if( (pole1['text'] == "O" and pole2['text'] == "O" and pole3['text'] == "O") or
				(pole4['text'] == "O" and pole5['text'] == "O" and pole6['text'] == "O") or
				(pole7['text'] == "O" and pole8['text'] == "O" and pole9['text'] == "O") or
				(pole1['text'] == "O" and pole4['gtext'] == "O" and pole7['text'] == "O") or
				(pole2['text'] == "O" and pole5['text'] == "O" and pole8['text'] == "O") or
				(pole3['text'] == "O" and pole6['text'] == "O" and pole9['text'] == "O") or
				(pole1['text'] == "O" and pole5['text'] == "O" and pole9['text'] == "O") or
				(pole3['text'] == "O" and pole5['text'] == "O" and pole7['text'] == "O")):
				message = messagebox.showinfo("We have a winner!", "Player2 wins!")
				root.destroy()
				sys.exit(1)



root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Tic Tac Toe")
MainApp(root).pack()
root.mainloop()