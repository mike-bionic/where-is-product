from tkinter import *
import webview

tk = Tk()

def runview():
	tk.geometry('1520x840')
	webview.create_window("Ýaş oýlap tapyjylar", "http://localhost:5000/")
	webview.start()

runview()
