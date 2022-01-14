from tkinter import *
import os

# askopenfilena
# asksaveasfile
# asksaveasfile
from tkinter import messagebox,filedialog,font, colorchooser,ttk
root = Tk()
root.geometry("1000x100")
root.title("untitled-notepad")
root.wm_iconbitmap('notepad.ico')
root.minsize(100, 100)
root.maxsize(2000, 2000)

def get_me():
	entry_value = entry.get()
	answer_value = wikipedia.summary(entry_value)

	answer.insert(INSERT, answer_value)
########################## new function
def new(event=None):
	text.delete(1.0,END)
	root.title("Untitled")
######################### open function
def open1(event=None):
	global file
	# if file:
	# 	messagebox.askyesnocancel(file,"Do you want to save file")
	try:

		file = filedialog.askopenfilename(filetypes=[("All files","*.*"),("text document",".txt")])
		with open(file,"r") as op:
			text.delete(1.0,END)
			text.insert(1.0,op.read())
		root.title(os.path.basename(file))	
	except Exception as r:
		pass	

######################### save function
def save(event=None):
	global file
	try:
		code = text.get(1.0,END)
		with open(file,"w") as op:
			op.write(str(code))
	except Exception as w:
		pass

######################### save as function
def saveas(event=None):
	try:
		file = filedialog.asksaveasfile(mode="w",initialdir=os.getcwd(),defaultextension=".txt",
										filetypes=[
											("Text document as",".txt"),
											("All files","*.*")											
										])	
		filetext = str(text.get(1.0,END))
		file.write(filetext)
		file.close()
	except Exception as e:
		pass	

######################### print function
def print1():
	pass

######################### exit function
def exit_func(event=None):
	global file, text_changed
	try:
		if text_changed:
			mbox = messagebox.askyesnocancel("warning", "do you want to save it")
			
			if mbox is True:
				if file:
					with open(file,"w") as op:
						op.write(str(text.get(1.0,END)))
						root.destroy()
				else:

					file = filedialog.asksaveasfile(mode="w",initialdir=os.getcwd(),defaultextension=".txt",
													filetypes=[
														("Text document as",".txt"),
														("All files","*.*")									
													])	
					filetext = str(text.get(1.0,END))
					file.write(filetext)
					file.close()
			else:
				root.destroy()	
	except Exception as w:
		pass

######################### undo function
def undo():
	pass


def cut():
	text.event_generate("<<Cut>>")


def copy():
	text.event_generate("<<Copy>>")


def paste():
	text.event_generate("<<Paste>>")


def delete():
	text.event_generate("<<Delete>>")

###################find

def find(event=None):

	def find1():
		word = find_input.get()
		text.tag_remove("match", 1.0,END)
		matches = 0
		if word:
			start_pos = 1.0
			while True:
				start_pos = text.search(word, start_pos, stopindex=END)
				if not start_pos:
					break
				end_pos = f"{start_pos}+{len(word)}c"
				text.tag_add("match", start_pos, end_pos)
				matches +=1
				start_pos = end_pos
				text.tag_config("match", foreground='red', background='yellow')


	def replace1():
		word = find_input.get()
		replace_text = replace_input.get()
		content = text.get(1.0,END)
		new_content = content.replace(word, replace_text)
		text.delete(1.0,END)
		text.insert(1.0, new_content)
 
	find_dialog = Toplevel()
	find_dialog.geometry("450x250+500+200")
	find_dialog.title("Find")
	find_dialog.resizable(0,0)

	#frame
	find_frame = ttk.Labelframe(find_dialog, text="Find/Replace")
	find_frame.pack(pady=20)

	#label
	text_find_label = Label(find_frame, text="Find :")
	text_replace_label = Label(find_frame, text="Replace :")

	#entry
	find_input = Entry(find_frame, width=30)
	replace_input = Entry(find_frame, width=30)

	#button
	find_button = Button(find_frame, text="Find", command=find1)
	replace_button = Button(find_frame, text="Replace", command=replace1)

	#labelgrid
	text_find_label.grid(row=0, column=0, padx=4, pady=4)
	text_replace_label.grid(row=1, column=0, padx=4, pady=4)

	#entry grid
	find_input.grid(row=0, column=1, padx=4, pady=4)
	replace_input.grid(row=1, column=1, padx=4, pady=4)

	#buttongrid
	find_button.grid(row=2, column=0, padx=8, pady=4)
	replace_button.grid(row=2, column=1, padx=8, pady=4)

	find_dialog.mainloop()



def fonts():
	
	main=Toplevel()
	main.resizable(0,0)
	main.geometry("500x600")
	# main.resizable(0)
	font_changing_family = 'Arial'
	font_changing_size = 20
	font_style =  "bold"
	family_value = StringVar()
	font_family = font.families()

	# print(font_family)
	family = ttk.Combobox(main,width=24,state="readonly",textvariable=family_value)
	family['values'] = font_family
	family.current(font_family.index('Arial'))
	family.grid(row=0,column=0,padx=5)


	font_value = IntVar()
	font_size_box = ttk.Combobox(main,width=12,textvariable=font_value)
	font_size_box['values'] = tuple(range(8,100,2))
	font_size_box.current(4)
	font_size_box.grid(row=0,column=3,padx=4)



	my_value = StringVar()
	my_size_box = ttk.Combobox(main,width=12,textvariable=my_value)
	my_size_box['values'] =("bold",'italic','underline')
	my_size_box.current(1)
	my_size_box.grid(row=0,column=6,padx=4)


	sample = Label(main,text="Sample",relief=SUNKEN,borderwidth=3,width=34)
	sample.place(x=100,y=100)
	sample_label = Label(sample,text="AaBbYyZz",font=f"{font_changing_family} {font_changing_size} {font_style}")
	sample_label.grid(row=0,column=0)
	
	def change_font_family(event=None):
		global font_changing_family
		font_changing_family = family_value.get()
		print(font_changing_family)
		# sample_label.update()
		sample_label.configure(font=(font_changing_family,font_changing_size,font_style))
		# sample_label.update()	

	def change_font_size(event=None):
		global font_changing_size
		font_changing_size = font_value.get()	
		sample_label.configure(font=(font_changing_family,font_changing_size,font_style))

	def change_style(event=None):
		global font_style
		font_style = my_value.get()
		sample_label.configure(font=(font_changing_family,font_changing_size,font_style))


	family.bind("<<ComboboxSelected>>",change_font_family)
	font_size_box.bind("<<ComboboxSelected>>",change_font_size)
	my_size_box.bind("<<ComboboxSelected>>",change_style)

	def set_text():
		global font_changing_family,font_changing_size,font_style
		font_changing_family = family_value.get()
		font_changing_size = font_value.get()
		font_style = my_value.get()
		text.configure(font=(font_changing_family,font_changing_size,font_style))
		main.destroy()

	def cancel():
		main.destroy()	

	ok_button = Button(main,text="ok",bg="red",fg="white",width=12,font="auto 16 normal",command=set_text)
	ok_button.place(x=230,y=500)

	cancel_btn = Button(main,text="cancel",bg="red",fg="white",width=12,font="auto 16 normal",command=cancel)
	cancel_btn.place(x=370,y=500)
	main.mainloop()



def fontcolor():
    color_var = colorchooser.askcolor()
    text.configure(fg=color_var[1])



def abounotepad():
	main1=Toplevel()

	satyam = Label(main1, text="""	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodtempor incididunt ut labore 
		et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut 
		aliquip ex ea commodo""", 
	bg="white", fg="black",
	font=("algerian", 18, "bold"), pady=23, relief=SUNKEN)

	satyam.pack(side="top", fill=X)
	main1.mainloop()


mymenu=Menu(root)

m1=Menu(mymenu, tearoff=0)

file = ""
modified = False

new_icon = PhotoImage(file="new.png")
open_icon = PhotoImage(file="open.png")
save_icon = PhotoImage(file="save.png")
saveas_icon = PhotoImage(file="save_as.png")
exit_icon = PhotoImage(file="exit.png")
print_icon = PhotoImage(file="myprint.png")

m1.add_command(label='New', image=new_icon, compound=LEFT,
 accelerator='Ctrl+n', command=new)
m1.add_command(label='Open', image=open_icon, compound=LEFT, 
	accelerator='Ctrl+o', command=open1)
m1.add_command(label='Save', image=save_icon, compound=LEFT,
 accelerator='Ctrl+s', command=save)
m1.add_command(label='Save as', image=saveas_icon, compound=LEFT, command=saveas)
m1.add_separator()

m1.add_command(label="print", image=print_icon, compound=LEFT, accelerator='Ctrl+v', command=print1 )
m1.add_separator()
m1.add_command(label='Exit', image=exit_icon, compound=LEFT, command=exit_func)


mymenu.add_cascade(label="File",menu=m1)



m2=Menu(mymenu, tearoff=0)


file = ""

cut_icon = PhotoImage(file="cut.png")
copy_icon = PhotoImage(file="copy.png")
paste_icon = PhotoImage(file="paste.png")

clear_icon = PhotoImage(file="clear_all.png")



m2.add_separator()

m2.add_command(label='Cut', image=cut_icon, compound=LEFT,
 accelerator='Ctrl+x', command=cut)

m2.add_command(label='Copy', image=copy_icon, compound=LEFT,
 accelerator='Ctrl+c', command=copy)

m2.add_command(label='Paste', image=paste_icon, compound=LEFT,
 accelerator='Ctrl+v', command=paste)


m2.add_command(label='clearall', image=clear_icon, compound=LEFT,
 accelerator='Ctrl+', command=cut)



mymenu.add_cascade(label="Edit",menu=m2)



m3=Menu(mymenu, tearoff=0)


file = ""

font_icon = PhotoImage(file="myfont.png")

fontcolor_icon = PhotoImage(file="font_color.png")



m3.add_command(label='Font styles', image=font_icon, compound=LEFT,
 command=fonts)


m3.add_command(label='Font color', image=fontcolor_icon, compound=LEFT,
 command=fontcolor)

mymenu.add_cascade(label="Format",menu=m3)



m4=Menu(mymenu, tearoff=0)


file = ""
find_icon = PhotoImage(file="find.png")

m4.add_command(label='Find', image=find_icon, compound=LEFT,
 accelerator='Ctrl+f', command=find)


mymenu.add_cascade(label="FIND",menu=m4)




m5=Menu(mymenu, tearoff=0)



file = ""


aboutnotepad_icon = PhotoImage(file="mynotepad.png")



m5.add_separator()

m5.add_command(label='abounotepad', image=aboutnotepad_icon, compound=LEFT,
 command=abounotepad)


mymenu.add_cascade(label="Help",menu=m5)



text = Text(root,font="Playbill 48",undo=True)
text.pack(expand=True,fill=BOTH,padx=12)
def exit_func(event=None):
	global file, text_changed
	try:
		if text_changed:
			mbox = messagebox.askyesnocancel("warning", "do you want to save it")
			
			if mbox is True:
				if file:
					with open(file,"w") as op:
						op.write(str(text.get(1.0,END)))
						root.destroy()
				else:

					file = filedialog.asksaveasfile(mode="w",initialdir=os.getcwd(),defaultextension=".txt",
													filetypes=[
														("Text document as",".txt"),
														("All files","*.*")									
													])	
					filetext = str(text.get(1.0,END))
					file.write(filetext)
					file.close()
			else:
				root.destroy()	
	except Exception as w:
		pass
scroll = Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)




statusbar_bar = Label(root,text="Status bar")
statusbar_bar.pack(side=BOTTOM,fill=X)


def changed(event=None):
    global text_changed
    if text.edit_modified():
        text_changed = True
        words = len(text.get(1.0, 'end-1c').split())
        characters = len(text.get(1.0, 'end-1c'))
        statusbar_bar.config(text=f'Characters : {characters} Words : {words}')
    text.edit_modified(False)

text.bind('<<Modified>>', changed)


root.config(menu=mymenu)



# def on_closing():
# 	exit_func()

# root.protocol("WM_DELETE_WINDOW",on_closing)


root.bind("<Control-n>", new)
root.bind("<Control-o>", open1)
root.bind("<Control-s>", save)
root.bind("<Control-Alt-s>",saveas)
root.bind("<Control-q>", exit_func)
root.bind("<Control-f>", find)

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()