import tkinter as tk
from tkinter import ttk, INSERT, DISABLED, GROOVE, CURRENT, Radiobutton, \
    NORMAL, ACTIVE, messagebox, Menu, IntVar, Checkbutton, FLAT, PhotoImage, Label,\
        SOLID, N, S, W, E, END, LEFT, Scrollbar, RIGHT, Y, BOTH
import Globals
import re
import CoMet_functions, intro_tab_functions, Map_Dose
import Dose_response_functions
from PIL import Image, ImageTk
import os
import sys



Globals.form.title("FIDORA")
#lobals.form.geometry("1250x600")
Globals.form.configure(bg='#ffffff')
Globals.form.state('zoomed')

Globals.form.tk.call('wm', 'iconphoto', Globals.form._w, PhotoImage(file='logo_fidora.png'))
Globals.form.iconbitmap(default='logo_fidora.png')

load = Image.open("fidora_logo.png")
render = ImageTk.PhotoImage(load)
label = Label(Globals.form, image=render)
label.image = render
label.grid(row = 0, column = 0, sticky=W)# place(relwidt=0.61,relheight=0.15, relx=0.02, rely=0.0)
label.config(bg='#FFFFFF') 

Globals.tab_parent.add(Globals.intro_tab, text='FIDORA')
Globals.tab_parent.add(Globals.tab1, text='CoMet')
Globals.tab_parent.add(Globals.tab2, text='Dose-response')
Globals.tab_parent.add(Globals.tab3, text='Map dose')
Globals.tab_parent.add(Globals.tab4, text='Profiles')

style = ttk.Style()
style.theme_create('MyStyle', parent= 'classic', settings={
    ".": {
        "configure": {
            "background": '#FFFFFF', # All colors except for active tab-button
            "font": 'red'
        }
    },
    "Horizontal.TProgressbar":{
        "configure": {
            "background": '#2C8EAD',
            "bordercolor": '#32A9CE',
            "troughcolor": "#ffffff",
        }
    },
    "TNotebook": {
        "configure": {
            "background":'#ffffff', # color behind the notebook
            "tabmargins": [5, 5, 10, 10], # [left margin, upper margin, right margin, margin beetwen tab and frames]
            "tabposition": 'wn',
            "borderwidth": 0,

        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#0A7D76', # Color of non selected tab-button
            "foreground": '#ffffff',
            "padding": [30,35, 20,35], # [space beetwen text and horizontal tab-button border, space between text and vertical tab_button border]
            "font": ('#FFFFFF', '15'),
            "borderwidth": 1,
            "equalTabs": True,
            "width": 13
            
        },
        "map": {
            "background": [("selected", '#02B9A5')], # Color of active tab
            "expand": [("selected", [1, 1, 1, 0])] # [expanse of text]
        }
    }
})

style.theme_use('MyStyle')


menubar = Menu(Globals.form)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=CoMet_functions.nothingButton)
filemenu.add_command(label="Open", command=CoMet_functions.nothingButton)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Globals.form.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=CoMet_functions.nothingButton)
helpmenu.add_command(label="About", command=CoMet_functions.nothingButton)
menubar.add_cascade(label="Help", menu=helpmenu)
Globals.form.config(menu=menubar)

upload_button_file = "uploadbutton2.png"
upload_button_image = ImageTk.PhotoImage(file=upload_button_file)

select_folder_button_file = "select_folder.png"
select_folder_image = ImageTk.PhotoImage(file=select_folder_button_file)

CoMet_border_dark_file = "border.png"
CoMet_border_dark = ImageTk.PhotoImage(file=CoMet_border_dark_file)

CoMet_border_light_file = "border_light.png"
CoMet_border_light = ImageTk.PhotoImage(file=CoMet_border_light_file)

CoMet_save_button_file = "save.png"
CoMet_save_button = ImageTk.PhotoImage(file=CoMet_save_button_file)

CoMet_correct_button_file = "correct_button.png"
CoMet_correct_button_image= ImageTk.PhotoImage(file=CoMet_correct_button_file)

###################################### INTRO TAB #################################################


#scrollbar = Scrollbar(Globals.intro_tab)
#scrollbar.pack(side=RIGHT, fill=Y)#grid(row=0, column=1, sticky=N+S+E)#pack(side=RIGHT, fill=Y)
#Globals.intro_tab.grid_columnconfigure(0, weight=0)
#Globals.intro_tab.grid_rowconfigure(0, weight=0)
intro_tab_canvas = tk.Canvas(Globals.intro_tab)#, yscrollcommand=scrollbar.set)
intro_tab_canvas.config(bg='#ffffff', bd = 0, relief=FLAT, highlightthickness=0)


tab1_text_box = tk.Frame(intro_tab_canvas, height=230, width=400)
tab1_text_box.grid(row=0, column=0, pady=(30,30), padx=(95,0))
tab1_text_box.config(bd=0, bg='#E5f9ff')


tab1_title_text = tk.Text(tab1_text_box, height=1, width=6)
tab1_title_text.insert(END, "CoMet")
tab1_title_text.grid(in_=tab1_text_box, row=0, column = 0, pady=(15,5), padx=(10,10))
tab1_title_text.config(state=DISABLED, bd=0, bg ='#E5f9ff', fg='#130e07', font=('calibri', '25', 'bold'))
tab1_text_box.grid_columnconfigure(0,weight=1)
tab1_text_box.grid_rowconfigure(0,weight=1)

tab1_text = tk.Text(tab1_text_box, height=4, width=43)
tab1_text.grid(in_=tab1_text_box, row=1, column=0, sticky=N+S+W+E, pady=(0,0), padx=(20,20))
tab1_text.insert(INSERT,"Correct your scanned images using CoMet. A method \ndeveloped to correct for non-uniformity introduced\n\
by the scanner. The correction is based on absolute \nsubtraction.")
tab1_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '13'))
tab1_text_box.grid_columnconfigure(1,weight=1)
tab1_text_box.grid_rowconfigure(1,weight=1) 

tab1_readmore_text = tk.Text(tab1_text_box, height=1, width=1)
tab1_readmore_text.grid(row=1, column=0, sticky = N+S+W+E, pady=(65,0), padx = (110,0))
tab1_readmore_text.insert(INSERT,"Read more...")
tab1_readmore_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '12', 'bold')) 
tab1_text_box.grid_columnconfigure(2,weight=1)
tab1_text_box.grid_rowconfigure(2,weight=1)

tab1_box_figure = Image.open("CoMet_ikon.PNG")
tab1_figure = ImageTk.PhotoImage(tab1_box_figure)
tab1_figure_label = Label(tab1_text_box, image=tab1_figure)
tab1_figure_label.image = tab1_figure
tab1_figure_label.grid(row=3, sticky=N+S+W+E, pady=(0,10))
tab1_figure_label.config(bg='#E5f9ff')
tab1_text_box.grid_columnconfigure(3, weight=1)
tab1_text_box.grid_rowconfigure(3, weight=1)

"""
tab1_readmore = tk.Button(tab1_text_box, text='Read more',cursor='hand2',font=('calibri', '12', 'bold'),\
    relief=FLAT, state=tk.ACTIVE, width = 15, command=intro_tab_functions.readMore)
tab1_readmore.place(relwidth=0.25, relheight=0.13, relx=0.27, rely=0.054)
"""
tab2_text_box = tk.Frame(intro_tab_canvas, height=230, width=400)
tab2_text_box.grid(row=0, column=1, pady=(30,30), padx=(85,40))
tab2_text_box.config(bd=0, bg='#E5f9ff')

tab2_title = tk.Text(tab2_text_box, height=1, width=12)
tab2_title.grid(in_=tab2_text_box, row=0, column = 0, pady=(15,5), padx=(10,10))
tab2_title.insert(INSERT, "Dose response")
tab2_title.config(state=DISABLED, bd=0, bg = '#E5f9ff', fg='#130e07', font=('calibri', '25', 'bold'))
tab2_text_box.grid_columnconfigure(0, weight=1)
tab2_text_box.grid_rowconfigure(0, weight=1)

tab2_text = tk.Text(tab2_text_box, height=4, width=43)
tab2_text.grid(in_=tab2_text_box, row=1, column=0, sticky=N+S+W+E, pady=(0,0), padx=(20,20))
tab2_text.insert(INSERT,"Make a calibration curve and read the dose response \nfunction. For every new batch of GafChromic film\
    \nthere is a need to update the dose response. All three \nchannels (RGB) are read and calculated.")
tab2_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '13')) 
tab2_text_box.grid_columnconfigure(1, weight=1)
tab2_text_box.grid_rowconfigure(1, weight=1)

tab2_readmore_text = tk.Text(tab2_text_box, height=1, width=1)
tab2_readmore_text.grid(row=1, column=0, sticky = N+S+W+E, pady=(65,0), padx = (300,0))
tab2_readmore_text.insert(INSERT,"Read more...")
tab2_readmore_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '12', 'bold'))
tab2_text_box.grid_columnconfigure(2, weight=1)
tab2_text_box.grid_rowconfigure(2, weight=1)

tab2_box_figure = Image.open("kalibrering_ikon.PNG")
tab2_figure = ImageTk.PhotoImage(tab2_box_figure)
tab2_figure_label = Label(tab2_text_box, image=tab2_figure)
tab2_figure_label.image = tab2_figure
tab2_figure_label.grid(row=3, sticky=N+S+W+E, pady=(0,10))
tab2_figure_label.config(bg='#E5f9ff')
tab2_text_box.grid_columnconfigure(3, weight=1)
tab2_text_box.grid_rowconfigure(3, weight=1)

tab3_text_box = tk.Frame(intro_tab_canvas, height=230, width=400)
tab3_text_box.grid(row=1, column=0, pady=(0,30), padx=(95,0))
tab3_text_box.config(bd=0, bg='#E5f9ff')

tab3_title = tk.Text(tab3_text_box, height=1, width=8)
tab3_title.grid(in_=tab3_text_box, row=0, column = 0, pady=(15,5), padx=(10,10))
tab3_title.insert(INSERT, "Map dose")
tab3_title.config(state=DISABLED, bd=0, bg = '#E5f9ff', fg='#130e07', font=('calibri', '25', 'bold'))
tab3_text_box.grid_columnconfigure(0, weight=1)
tab3_text_box.grid_rowconfigure(0, weight=1)

tab3_text = tk.Text(tab3_text_box, height=4, width=43)
tab3_text.grid(in_=tab3_text_box, row=1, column=0, sticky=N+S+W+E, pady=(0,0), padx=(20,20))
tab3_text.insert(INSERT,"Compare dose distribution in your treatment plan \nwith the measures distribution by the Gafchromic \nfilm.\
 Using the gamma evaluation index a map of \npass/fail and variations is visualised.")
tab3_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '13'))
tab3_text_box.grid_columnconfigure(1, weight=1)
tab3_text_box.grid_rowconfigure(1, weight=1)

tab3_readmore_text = tk.Text(tab3_text_box, height=1, width=1)
tab3_readmore_text.grid(row=1, column=0, sticky = N+S+W+E, pady=(65,0), padx = (285,0))
tab3_readmore_text.insert(INSERT,"Read more...")
tab3_readmore_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '12', 'bold'))
tab3_text_box.grid_columnconfigure(2, weight=1)
tab3_text_box.grid_rowconfigure(2, weight=1)

tab3_box_figure = Image.open("gammaTest_ikon.PNG")
tab3_figure = ImageTk.PhotoImage(tab3_box_figure)
tab3_figure_label = Label(tab3_text_box, image=tab3_figure)
tab3_figure_label.image = tab3_figure
tab3_figure_label.grid(row=3, sticky=N+S+W+E, pady=(0,10))
tab3_figure_label.config(bg='#E5f9ff')
tab3_text_box.grid_columnconfigure(3, weight=1)
tab3_text_box.grid_rowconfigure(3, weight=1)

tab4_text_box = tk.Frame(intro_tab_canvas, height=230, width=400)
tab4_text_box.grid(row=1, column=1, pady=(0,30), padx=(85,40))
tab4_text_box.config(bd=0, bg='#E5f9ff')

tab4_title = tk.Text(tab4_text_box, height=1, width=7)
tab4_title.grid(in_=tab4_text_box, row=0, column = 0, pady=(15,5), padx=(10,10))
tab4_title.insert(INSERT, "Profiles")
tab4_title.config(state=DISABLED, bd=0, bg = '#E5f9ff', fg='#130e07', font=('calibri', '25', 'bold'))
tab4_text_box.grid_columnconfigure(0,weight=1)
tab4_text_box.grid_rowconfigure(0, weight=1)

tab4_text = tk.Text(tab4_text_box, height=4, width=43)
tab4_text.grid(in_=tab4_text_box, row=1, column=0, sticky=N+S+W+E, pady=(0,0), padx=(20,20))
tab4_text.insert(INSERT,"Investigate the profiles measured using GafChromic \nfilm and compare with the profiles in your treatment \nplan.\
 Using gamma evaluation an acceptance tube \ncan be places over the profile.")
tab4_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '13')) 
tab4_text_box.grid_columnconfigure(1, weight=1)
tab4_text_box.grid_rowconfigure(1, weight=1)

tab4_readmore_text = tk.Text(tab4_text_box, height=1, width=1)
tab4_readmore_text.grid(row=1, column=0, sticky = N+S+W+E, pady=(65,0), padx = (235,0))
tab4_readmore_text.insert(INSERT,"Read more...")
tab4_readmore_text.config(state=DISABLED, bd=0, bg='#E5f9ff', fg='#130E07', font=('calibri', '12', 'bold'))
tab4_text_box.grid_columnconfigure(2, weight=1)
tab4_text_box.grid_rowconfigure(2, weight=1)

tab4_box_figure = Image.open("profil_ikon.PNG")
tab4_figure = ImageTk.PhotoImage(tab4_box_figure)
tab4_figure_label = Label(tab4_text_box, image=tab4_figure)
tab4_figure_label.image = tab4_figure
tab4_figure_label.grid(row=3, sticky=N+S+W+E, pady=(0,10))
tab4_figure_label.config(bg='#E5f9ff')
tab4_text_box.grid_columnconfigure(3, weight=1)
tab4_text_box.grid_rowconfigure(3, weight=1)

#intro_tab_canvas.configure(scrollregion = intro_tab_canvas.bbox("all"))
intro_tab_canvas.grid(row=0, column=0, sticky=N+S+W)#pack(side=LEFT, fill=BOTH)
#Globals.intro_tab.grid_columnconfigure(1, weight=2)
#Globals.intro_tab.grid_rowconfigure(1, weight=2)
#scrollbar.config(command=intro_tab_canvas.yview)

##################################### TAB 1 - CoMet ############################################

Globals.tab1_canvas.config(bg='#ffffff', bd = 0, relief=FLAT, highlightthickness=0)

CoMet_explained = tk.Text(Globals.tab1_canvas, height=4)#, width=200)
CoMet_explained.insert(INSERT, \
"A linear accelerator is a tool used to generate ionizing radiation, which can be used in radiotherapy\n\
treatment. Using a modulator, electron gun and RF power source electrons are released and \n\
accelerated through a waveguide. The modulator provide high voltage pulses to the RF pulse which\n\
leads to a propagating electromagnetic ﬁeld inside the waveguide.")
CoMet_explained.grid(row=0, column = 0, columnspan=4, sticky=N+S+E+W, padx=(20,20), pady=(10,20))
Globals.tab1_canvas.grid_columnconfigure(0, weight=0)
Globals.tab1_canvas.grid_rowconfigure(0, weight=0)
CoMet_explained.config(state=DISABLED, bg='#ffffff', font=('calibri', '13'), relief=FLAT)

Globals.CoMet_border_1_label = Label(Globals.tab1_canvas, image = CoMet_border_dark,width=50)
Globals.CoMet_border_1_label.image=CoMet_border_dark
Globals.CoMet_border_1_label.grid(row=1, column=0, columnspan=3, sticky = W+E, padx = (0, 50), pady=(10,15))
Globals.tab1_canvas.grid_columnconfigure(1, weight=0)
Globals.tab1_canvas.grid_rowconfigure(1, weight=0)
Globals.CoMet_border_1_label.config(bg='#ffffff', borderwidth=0)

CoMet_upload_button_frame = tk.Frame(Globals.tab1_canvas)
CoMet_upload_button_frame.grid(row=1, column = 2, padx = (60, 0), pady=(10,15))
Globals.tab1_canvas.grid_columnconfigure(2, weight=0)
Globals.tab1_canvas.grid_rowconfigure(2, weight=0)
CoMet_upload_button_frame.config(bg = '#ffffff')

CoMet_upload_button = tk.Button(CoMet_upload_button_frame, text='Browse', image = upload_button_image ,cursor='hand2',font=('calibri', '14'),\
    relief=FLAT, state=ACTIVE, command=CoMet_functions.UploadAction)
CoMet_upload_button.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
CoMet_upload_button.config(bg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff', highlightthickness=0)
CoMet_upload_button.image = upload_button_image

Globals.CoMet_uploaded_file_text = tk.Text(Globals.CoMet_border_1_label, height=1, width=31)
Globals.CoMet_uploaded_file_text.grid(row=0, column=0, columnspan=3, sticky=E+W, pady=(20,20), padx=(80,0))
Globals.CoMet_uploaded_file_text.insert(INSERT, "Upload the image you want to correct")
Globals.CoMet_uploaded_file_text.config(state=DISABLED, bd=0, font=('calibri', '12'), fg='gray', bg='#ffffff')

Globals.CoMet_border_2_label = Label(Globals.tab1_canvas, image = CoMet_border_dark)
Globals.CoMet_border_2_label.image=CoMet_border_dark
Globals.CoMet_border_2_label.grid(row=2, column=0, columnspan=3, sticky=N+S+E+W, padx = (0, 50), pady=(10,15))
Globals.tab1_canvas.grid_columnconfigure(3, weight=0)
Globals.tab1_canvas.grid_rowconfigure(3, weight=0)
Globals.CoMet_border_2_label.config(bg='#ffffff', borderwidth=0)

CoMet_folder_button_frame = tk.Frame(Globals.tab1_canvas)
CoMet_folder_button_frame.grid(row=2, column = 2, padx = (60, 0), pady=(10,15))
Globals.tab1_canvas.grid_columnconfigure(4, weight=0)
Globals.tab1_canvas.grid_rowconfigure(4, weight=0)
CoMet_folder_button_frame.config(bg = '#ffffff')

CoMet_folder_button = tk.Button(CoMet_folder_button_frame, text='Browse', image = select_folder_image ,cursor='hand2',font=('calibri', '14'),\
    relief=FLAT, state=ACTIVE, command=CoMet_functions.setCoMet_export_folder)
CoMet_folder_button.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
CoMet_folder_button.config(bg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff', highlightthickness=0)
CoMet_folder_button.image=select_folder_image

CoMet_save_to_folder = tk.Text(Globals.CoMet_border_2_label, height=1, width=32)
CoMet_save_to_folder.grid(row=0, column=0, columnspan=3, sticky=E+W, pady=(20,20), padx=(80,0))
CoMet_save_to_folder.insert(INSERT,"Folder to save the corrected image:")
CoMet_save_to_folder.config(state=DISABLED, bd=0, font=('calibri', '12'), fg='gray', bg='#ffffff') 

## Function to test the filename the user chooses for the corrected image
def testFilename():   
    Globals.CoMet_corrected_image_filename.set(CoMet_save_filename.get("1.0",'end-1c'))
    if(Globals.CoMet_corrected_image_filename.get() == " " or Globals.CoMet_corrected_image_filename.get() == "Filename"):
        Globals.CoMet_corrected_image_filename.set("Error!")
    elif(len(Globals.CoMet_corrected_image_filename.get()) >21):
        messagebox.showerror("Error", "The filename must be under 20 characters")
        Globals.CoMet_corrected_image_filename.set("Error!")
    elif(re.match("^[A-Za-z0-9_]*$", (Globals.CoMet_corrected_image_filename.get()).lstrip())==None):
        messagebox.showerror("Error","Filename can only contain letters and/or numbers")
        Globals.CoMet_corrected_image_filename.set("Error!")
    else:
        CoMet_save_button_1.config(state=DISABLED)
        CoMet_save_filename.config(state=DISABLED)
        Globals.CoMet_progressbar_counter += 1
        Globals.CoMet_progressbar["value"] = Globals.CoMet_progressbar_counter*25
    

Globals.CoMet_border_3_label = Label(Globals.tab1_canvas, image = CoMet_border_light)
Globals.CoMet_border_3_label.image=CoMet_border_light
Globals.CoMet_border_3_label.grid(row=3, column=0, columnspan=3, sticky=N+S+E+W, padx = (0, 50), pady=(10,0))
Globals.tab1_canvas.grid_columnconfigure(5, weight=0)
Globals.tab1_canvas.grid_rowconfigure(5, weight=0)
Globals.CoMet_border_3_label.config(bg='#ffffff', borderwidth=0)

CoMet_save_button_frame_1 = tk.Frame(Globals.tab1_canvas)
CoMet_save_button_frame_1.grid(row=3, column = 2, padx = (60, 0), pady=(10,0))
Globals.tab1_canvas.grid_columnconfigure(6, weight=0)
Globals.tab1_canvas.grid_rowconfigure(6, weight=0)
CoMet_save_button_frame_1.config(bg = '#ffffff')

CoMet_save_button_1 = tk.Button(CoMet_save_button_frame_1, text='Save', image = CoMet_save_button ,cursor='hand2',font=('calibri', '14'),\
    relief=FLAT, state=ACTIVE, command=testFilename)
CoMet_save_button_1.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
CoMet_save_button_1.config(bg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff', highlightthickness=0)
CoMet_save_button_1.image = CoMet_save_button

CoMet_save_filename = tk.Text(Globals.CoMet_border_3_label, height=1, width=30)
CoMet_save_filename.grid(row=0, column=0, columnspan=3, sticky=E+W, pady=(20,20), padx=(80,0))
CoMet_save_filename.insert(END,"Filename (will be saved as *.dcm)")
CoMet_save_filename.config(state=NORMAL, bd=0, font=('calibri', '12'), fg='gray', bg='#ffffff')


def writeFilename(event):
    current = CoMet_save_filename.get("1.0", tk.END)
    if(current == "Filename (will be saved as *.dcm)\n"):
        CoMet_save_filename.delete("1.0", tk.END)
    else:
        CoMet_save_filename.insert("1.0", "Filename (will be saved as *.dcm)")

CoMet_save_filename.bind("<FocusIn>", writeFilename)
CoMet_save_filename.bind("<FocusOut>", writeFilename)


#Functioin to validate the patient name written in by the user
def testName():   
    Globals.CoMet_patientName.set(CoMet_save_patientName.get("1.0",'end-1c'))
    if(Globals.CoMet_patientName.get() == " " or Globals.CoMet_patientName.get() == "Patient name"):
        Globals.CoMet_patientName.set("Error!")
    elif(len(Globals.CoMet_patientName.get()) >31):
        messagebox.showerror("Error", "The Name must be under 30 characters")
        Globals.CoMet_patientName.set("Error!")
    elif(re.match("^[A-Za-z0-9_]*$", (Globals.CoMet_patientName.get()).lstrip())==None):
        messagebox.showerror("Error","Name can only contain letters (not æ,ø,å) and no spaces")
        Globals.CoMet_patientName.set("Error!")
    else:
        CoMet_save_button_2.config(state=DISABLED)
        CoMet_save_patientName.config(state=DISABLED)


Globals.CoMet_border_4_label = Label(Globals.tab1_canvas, image = CoMet_border_light)
Globals.CoMet_border_4_label.image=CoMet_border_light
Globals.CoMet_border_4_label.grid(row=4, column=0, columnspan=3, sticky=E+W, padx = (0, 50), pady=(0,0))
Globals.tab1_canvas.grid_columnconfigure(7, weight=0)
Globals.tab1_canvas.grid_rowconfigure(7, weight=0)
Globals.CoMet_border_4_label.config(bg='#ffffff', borderwidth=0)

CoMet_save_button_frame_2 = tk.Frame(Globals.tab1_canvas)
CoMet_save_button_frame_2.grid(row=4, column = 2, padx = (60, 0), pady=(0,0))
Globals.tab1_canvas.grid_columnconfigure(8, weight=0)
Globals.tab1_canvas.grid_rowconfigure(8, weight=0)
CoMet_save_button_frame_2.config(bg = '#ffffff')

CoMet_save_button_2 = tk.Button(CoMet_save_button_frame_2, text='Save', image = CoMet_save_button ,cursor='hand2',font=('calibri', '14'),\
    relief=FLAT, state=ACTIVE, command=testName)
CoMet_save_button_2.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
CoMet_save_button_2.config(bg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff', highlightthickness=0)
CoMet_save_button_2.image = CoMet_save_button

CoMet_save_patientName = tk.Text(Globals.CoMet_border_4_label, height=1, width=30)
CoMet_save_patientName.grid(row=0, column=0, columnspan=3, sticky=E+W, pady=(20,20), padx=(80,0))
CoMet_save_patientName.insert(END,"Patient name")
CoMet_save_patientName.config(state=NORMAL, bd=0, font=('calibri', '12'), fg='gray', bg='#ffffff')

def writePname(event):
    current = CoMet_save_patientName.get("1.0", tk.END)
    if(current == "Patient name\n"):
        CoMet_save_patientName.delete("1.0", tk.END)
    else:
        CoMet_save_patientName.insert("1.0", "Patient name")

CoMet_save_patientName.bind("<FocusIn>", writePname)
CoMet_save_patientName.bind("<FocusOut>", writePname)

CoMet_correct_button_frame = tk.Frame(Globals.tab1_canvas)
CoMet_correct_button_frame.grid(row=4, column = 4,rowspan=2, padx = (0, 0), pady=(0,0))
Globals.tab1_canvas.grid_columnconfigure(9, weight=0)
Globals.tab1_canvas.grid_rowconfigure(9, weight=0)
CoMet_correct_button_frame.config(bg = '#ffffff')

CoMet_correct_button = tk.Button(CoMet_correct_button_frame, text='Save', image = CoMet_correct_button_image ,cursor='hand2',font=('calibri', '14'),\
    relief=FLAT, state=ACTIVE, command=CoMet_functions.Correct)
CoMet_correct_button.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
CoMet_correct_button.config(bg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff', highlightthickness=0)
CoMet_correct_button.image = CoMet_correct_button_image

Globals.CoMet_print_corrected_image = tk.Canvas(Globals.tab1_canvas , width=240, height=290)
Globals.CoMet_print_corrected_image.grid(row=0, column=4, rowspan=3, sticky=N+W+S+E, pady=(20,0))
Globals.CoMet_print_corrected_image.config(bg='#ffffff', bd = 0, relief=FLAT)
Globals.tab1_canvas.grid_columnconfigure(11,weight=0)
Globals.tab1_canvas.grid_rowconfigure(11, weight=0)

Globals.tab1_canvas.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(expand=True, fill=BOTH)
##### teste scrollbar ##########
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

vsb = tk.Scrollbar(Globals.form, orient="vertical", command=Globals.tab1_canvas.yview)
Globals.tab1_canvas.configure(yscrollcommand=vsb.set)

vsb.grid(row=0,column=5,rowspan=5, sticky=N+S)#pack(side="right", fill="y")
Globals.tab1_canvas.grid(row=0,column=5,rowspan=5, sticky=N+S) #(side="left", fill="both", expand=True)
Globals.tab1_canvas.create_window((4,4), window=Globals.form, anchor="nw")

Globals.form.bind("<Configure>", lambda event, canvas=Globals.tab1_canvas: onFrameConfigure(Globals.tab1_canvas))

#populate(Globals.form)


##################################### TAB 2 - Dose response ############################################
#img_file_name="default.png"
#path_img=db_config.photo_directory + img_file_name


## Text and buttons for the user to choose DPI
#choose_doseResponse_dpi = tk.Text(Globals.tab2, height=1, width=1)
#choose_doseResponse_dpi.place(relwidth=0.35, relheight=0.5, relx=0.07, rely=0.61)
#choose_doseResponse_dpi.insert(tk.CURRENT,"Dots per inch (dpi) used during scanning: ")
#choose_doseResponse_dpi.config(state=DISABLED, bd=0, font=('calibri', '15'))
#Radiobutton(Globals.tab2, text='72 dpi',cursor='hand2',font=('calibri', '14'), \
#    variable=Globals.doseResponse_dpi, value=72, command=CoMet_functions.nothingButton).place(relwidth=0.075, relheight=0.05, relx=0.13, rely=0.66)
#Radiobutton(Globals.tab2, text='127 dpi',cursor='hand2',font=('calibri', '14'), \
#    variable=Globals.doseResponse_dpi, value=127, command=CoMet_functions.nothingButton).place(relwidth=0.077, relheight=0.05, relx= 0.23, rely=0.66)

#openImageTabOne=Image.open(path_img)
#imgTabOne=ImageTk.PhotoImage(openImageTabOne)
#imgLabelTabOne=tk.Label(tab2,image=imgTabOne)


why_dose_response_text = tk.Text(Globals.tab2, height=1, width=1)
why_dose_response_text.place(relwidt=0.48, relheight=0.4, relx=0.004, rely=0.005)
why_dose_response_text.insert(INSERT,\
"To be able to perform an accurate dose caluclations using GafChromic film EBT3 \n\
it is necessary to create a dose-respons curve for each batch of film, in addition\n\
to a calibration scan before/along every use. The respons of GafChromic film \n\
EBT3 is modelled using a rational function, X(D,n) = a + b/(D-c), as this has \n\
proven to fit well with the film behavior. In the model X(D,n) is the scanner \n\
respons in color channel n and a, b and c are constants. Because of the nature \n\
of asymptotic fitting functions a good fit will be achieved by using doses in \n\
geomteric progression, D, nD, nnD, etc.. Also, to avoid scanner uncertainties\n\
each dose should be scannet three times and uploaded here where an average will be used." )
why_dose_response_text.config(state=DISABLED, bd=0, font=('calibri', '12'))

how_dose_response_text = tk.Text(Globals.tab2, height=1, width=1)
how_dose_response_text.place(relwidt=0.48, relheight=0.4, relx=0.51, rely=0.005)
how_dose_response_text.insert(INSERT,\
"Irradiate film piece of size (Bestemt med maske?) with known doses. Place one and one\n\
film piece in the center of the scanner and perfom three scans per dose.  " )
how_dose_response_text.config(state=DISABLED, bd=0, font=('calibri', '12'))


upload_button1 = tk.Button(Globals.dose_response_scroll_window_1, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.create_window)
upload_button1.place(relwidth=0.5, relheight=0.1, relx=0.3, rely=0.03)

red = tk.Text(Globals.dose_response_scroll_window_1, height=1, width=1)
red.place(relwidth=0.1, relheight=0.08, relx=0.3, rely=0.2)
red.insert(INSERT, "Red")
red.config(state=DISABLED, bd=0, font=('calibri', '12'))

green = tk.Text(Globals.dose_response_scroll_window_1, height=1, width=1)
green.place(relwidth=0.1, relheight=0.08, relx=0.5, rely=0.2)
green.insert(INSERT, "Green")
green.config(state=DISABLED, bd=0, font=('calibri', '12'))

blue = tk.Text(Globals.dose_response_scroll_window_1, height=1, width=1)
blue.place(relwidth=0.1, relheight=0.08, relx=0.75, rely=0.2)
blue.insert(INSERT, "Blue")
blue.config(state=DISABLED, bd=0, font=('calibri', '12'))

dose_title = tk.Text(Globals.dose_response_scroll_window_1, height=1, width=1)
dose_title.place(relheight=0.08, relwidth=0.15, relx= 0.05, rely=0.2)
dose_title.insert(INSERT, "Dose (cGy)")
dose_title.config(state=DISABLED, bd=0, font=('calibri', '12'))

check1 = Checkbutton(Globals.dose_response_scroll_window_1, variable=Globals.dose_response_var1, command=Dose_response_functions.plot_dose_response)
check1.place(relx=0.4, rely=0.19)

check2 = Checkbutton(Globals.dose_response_scroll_window_1, variable=Globals.dose_response_var2, command=Dose_response_functions.plot_dose_response)
check2.place(relx=0.6, rely=0.19)

check3 = Checkbutton(Globals.dose_response_scroll_window_1, variable=Globals.dose_response_var3, command=Dose_response_functions.plot_dose_response)
check3.place(relx=0.85, rely=0.19)

Globals.dose_response_save_calibration_button = tk.Button(Globals.tab2, text='Save calibration', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=DISABLED, width=12, command=Dose_response_functions.saveCalibration)
Globals.dose_response_save_calibration_button.place(relwidth=0.1, relheight=0.05, relx=0.4, rely=0.4)

##################################### TAB 3 - Map dose ############################################

#path = os.path.dirname(sys.argv[0])
#path= "upload.png"
#upload_button_image = ImageTk.PhotoImage(file=path)



upload_film_data = tk.Button(Globals.tab3, text='Upload',image=upload_button_image, cursor='hand2', font=('calibri', '12'), \
    relief=FLAT, state=ACTIVE, width=12, command=lambda: Map_Dose.UploadAction("FILM"))
upload_film_data.place(relwidth=0.17, relheight=0.11, relx=0.3, rely=0.03)
upload_film_data.image = upload_button_image
##################################### TAB 4 - Profiles ###########################################



##################################### End statements ############################################
#Globals.tab_parent.place(relwidth=1, relheight=0.9, relx=0, rely=0.15)
Globals.form.mainloop()