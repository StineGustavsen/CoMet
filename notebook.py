import tkinter as tk
from tkinter import ttk, INSERT, DISABLED, GROOVE, CURRENT, Radiobutton, NORMAL, ACTIVE, messagebox, Menu, IntVar, Checkbutton
import Globals
import re
import CoMet_functions
import Dose_response_functions



Globals.form.title("Master")
Globals.form.geometry("1100x600")

Globals.tab_parent.add(Globals.tab1, text='CoMet')
Globals.tab_parent.add(Globals.tab2, text='Dose-response')
Globals.tab_parent.add(Globals.tab3, text='Map dose')

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

##################################### TAB 1 - CoMet ############################################


## Text and button for uploading image 
upload_file = tk.Text(Globals.tab1, height=1, width=1)
upload_file.place(relwidth=0.25, relheight=0.05, relx=0.007, rely=0.11)
upload_file.insert(INSERT,"Upload file you want to correct:")
upload_file.config(state=DISABLED, bd=0, font=('calibri', '15')) 
upload_box = tk.Text(Globals.tab1, height=1, width=1)
upload_box.place(relwidth=0.2, relheight=0.05, relx=0.28, rely=0.11)
upload_box.insert(INSERT," ")
upload_box.config(state=DISABLED, bd=0)
upload_button = tk.Button(Globals.tab1, text='Browse',cursor='hand2',font=('calibri', '14'),\
    highlightthickness= 7,overrelief=GROOVE, state=tk.ACTIVE, width = 15, command=CoMet_functions.UploadAction)
upload_button.place(relwidth=0.15, relheight=0.06, relx=0.5, rely=0.105)


## Text and buttons for the user to choose DPI
choose_CoMet_dpi = tk.Text(Globals.tab1, height=1, width=1)
choose_CoMet_dpi.place(relwidth=0.35, relheight=0.05, relx=0.07, rely=0.23)
choose_CoMet_dpi.insert(tk.CURRENT,"Dots per inch (dpi) used during scanning: ")
choose_CoMet_dpi.config(state=DISABLED, bd=0, font=('calibri', '15'))
Radiobutton(Globals.tab1, text='72 dpi',cursor='hand2',font=('calibri', '14'), \
    variable=Globals.CoMet_dpi, value=72, command=CoMet_functions.setCoMet_dpi).place(relwidth=0.075, relheight=0.05, relx=0.13, rely=0.3)
Radiobutton(Globals.tab1, text='127 dpi',cursor='hand2',font=('calibri', '14'), \
    variable=Globals.CoMet_dpi, value=127, command=CoMet_functions.setCoMet_dpi).place(relwidth=0.077, relheight=0.05, relx= 0.23, rely=0.3)


## Text and button for the user to select folder to save corrected image
save_to_folder = tk.Text(Globals.tab1, height=1, width=1)
save_to_folder.place(relwidth=0.28, relheight=0.05, relx=0.003, rely=0.4)
save_to_folder.insert(INSERT,"Folder to save the corrected image:")
save_to_folder.config(state=DISABLED, bd=0, font=('calibri', '15')) 
folder_box = tk.Text(Globals.tab1, height=1, width=1)
folder_box.place(relwidth=0.2, relheight=0.05, relx=0.29, rely=0.4)
folder_box.insert(INSERT," ")
folder_box.config(state=DISABLED, bd=0, font=('calibri', '12')) 
toFolder = tk.Button(Globals.tab1, text='Browse', cursor='hand2',font=('calibri', '14'),\
   highlightthickness= 7,overrelief=GROOVE, state=tk.ACTIVE, width = 15, command=CoMet_functions.setCoMet_export_folder)
toFolder.place(relwidth=0.15, relheight=0.06, relx=0.5, rely=0.395)

## Function to test the filename the user chooses for the corrected image
def testFilename():   
    Globals.CoMet_corrected_image_filename.set(Globals.CoMet_corrected_image_filename_box.get("1.0",'end-1c'))
    if(Globals.CoMet_corrected_image_filename.get() == " "):
        Globals.CoMet_corrected_image_filename.set("Error!")
    elif(len(Globals.CoMet_corrected_image_filename.get()) >21):
        messagebox.showerror("Error", "The filename must be under 20 characters")
        Globals.CoMet_corrected_image_filename.set("Error!")
    elif(re.match("^[A-Za-z0-9_]*$", (Globals.CoMet_corrected_image_filename.get()).lstrip())==None):
        messagebox.showerror("Error","Filename can only contain letters and/or numbers")
        Globals.CoMet_corrected_image_filename.set("Error!")
    else:
        load_corrected_image_filename.config(state=DISABLED)
        Globals.CoMet_corrected_image_filename_box.config(state=DISABLED)
    

## Text and box for the user to write in a filename for the corrected image, and lock it
corrected_image_filename_text = tk.Text(Globals.tab1, height=1, width=1)
corrected_image_filename_text.place(relwidt=0.24, relheight=0.05, relx=0.004, rely=0.5)
corrected_image_filename_text.insert(INSERT, "Write filename of saved image:" )
corrected_image_filename_text.config(state=DISABLED, bd=0, font=('calibri', '15'))
Globals.CoMet_corrected_image_filename_box= tk.Text(Globals.tab1, height=1, width=1)
Globals.CoMet_corrected_image_filename_box.place(relwidth=0.24, relheight=0.05, relx=0.25, rely=0.5)
Globals.CoMet_corrected_image_filename_box.insert(INSERT, " " )
Globals.CoMet_corrected_image_filename_box.config(state=NORMAL, bd=0, font=('calibri', '12'))
load_corrected_image_filename=tk.Button(Globals.tab1, text='Save filename', cursor='hand2', font=('calibri', '14'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=15, command=testFilename)
load_corrected_image_filename.place(relwidth=0.15, relheight=0.06, relx=0.5, rely=0.495)

#Tell filetype
out_filetype_text = tk.Text(Globals.tab1, height=1, width=1)
out_filetype_text.place(relwidth=0.2, relheight=0.05, relx=0.21, rely=0.57)
out_filetype_text.insert(tk.CURRENT,"Will be saved as *.dcm")
out_filetype_text.config(state=DISABLED, bd=0, font=('calibri', '13'))

#Functioin to validate the patient name written in by the user
def testName():   
    Globals.CoMet_patientName.set(Globals.CoMet_patientName_box.get("1.0",'end-1c'))
    if(Globals.CoMet_patientName.get() == " "):
        Globals.CoMet_patientName.set("Error!")
    elif(len(Globals.CoMet_patientName.get()) >31):
        messagebox.showerror("Error", "The Name must be under 30 characters")
        Globals.CoMet_patientName.set("Error!")
    elif(re.match("^[A-Za-z0-9_]*$", (Globals.CoMet_patientName.get()).lstrip())==None):
        messagebox.showerror("Error","Name can only contain letters (not æ,ø,å) and no spaces")
        Globals.CoMet_patientName.set("Error!")
    else:
        loadName.config(state=DISABLED)
        Globals.CoMet_patientName_box.config(state=DISABLED)


## Text and box for the user to write patient name
patientName_text = tk.Text(Globals.tab1, height=1, width=1)
patientName_text.place(relwidt=0.23, relheight=0.05, relx=0.007, rely=0.65)
patientName_text.insert(INSERT, "Write name of patient:" )
patientName_text.config(state=DISABLED, bd=0, font=('calibri', '15'))
Globals.CoMet_patientName_box= tk.Text(Globals.tab1, height=1, width=1)
Globals.CoMet_patientName_box.place(relwidth=0.23, relheight=0.05, relx=0.25, rely=0.65)
Globals.CoMet_patientName_box.insert(INSERT, " " )
Globals.CoMet_patientName_box.config(state=NORMAL, bd=0, font=('calibri', '12'))
loadName=tk.Button(Globals.tab1, text='Save name', cursor='hand2', font=('calibri', '14'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=15, command=testName)
loadName.place(relwidth=0.15, relheight=0.06, relx=0.49, rely=0.6495)


## Creating a button-widget to perform the correction
correct_button = tk.Button(Globals.tab1, text='Correct', cursor='hand2',font=('calibri', '18'),highlightthickness= 7,\
    overrelief=GROOVE, state=ACTIVE, width = 15, command=CoMet_functions.Correct)
correct_button.place(relwidth=0.2, relheight=0.14, relx=.18, rely=0.75)


##################################### TAB 2 - Dose response ############################################
#img_file_name="default.png"
#path_img=db_config.photo_directory + img_file_name

## Text and button for uploading image
upload_file = tk.Text(Globals.tab2, height=1, width=1)
upload_file.place(relwidth=0.21, relheight=0.05, relx=0.007, rely=0.51)
upload_file.insert(INSERT,"Upload image for calibration:")
upload_file.config(state=DISABLED, bd=0) 
upload_box = tk.Text(Globals.tab2, height=1, width=1)
upload_box.place(relwidth=0.18, relheight=0.05, relx=0.23, rely=0.51)
upload_box.insert(INSERT," ")
upload_box.config(state=DISABLED, bd=0)
upload_button = tk.Button(Globals.tab2, text='Browse',cursor='hand2',font=('calibri', '14'),\
    highlightthickness= 7,overrelief=GROOVE, state=tk.ACTIVE, width = 15, command=CoMet_functions.UploadAction)
upload_button.place(relwidth=0.12, relheight=0.06, relx=0.4, rely=0.505)

## Text and buttons for the user to choose DPI
choose_doseResponse_dpi = tk.Text(Globals.tab2, height=1, width=1)
choose_doseResponse_dpi.place(relwidth=0.35, relheight=0.5, relx=0.07, rely=0.61)
choose_doseResponse_dpi.insert(tk.CURRENT,"Dots per inch (dpi) used during scanning: ")
choose_doseResponse_dpi.config(state=DISABLED, bd=0, font=('calibri', '15'))
Radiobutton(Globals.tab2, text='72 dpi',cursor='hand2',font=('calibri', '14'), \
    variable=Globals.doseResponse_dpi, value=72, command=CoMet_functions.nothingButton).place(relwidth=0.075, relheight=0.05, relx=0.13, rely=0.66)
Radiobutton(Globals.tab2, text='127 dpi',cursor='hand2',font=('calibri', '14'), \
    variable=Globals.doseResponse_dpi, value=127, command=CoMet_functions.nothingButton).place(relwidth=0.077, relheight=0.05, relx= 0.23, rely=0.66)

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

dose_text = tk.Text(Globals.tab2, height=1, width=1)
dose_text.place(relwidth=0.12, relheight=0.05, relx=0.6, rely=0.5)
dose_text.insert(INSERT, "Write dose (cGy): ")
dose_text.config(state=NORMAL, bd=0, font=('calibri', '12'))

dose1_box= tk.Text(Globals.tab2, height=1, width=1)
dose1_box.place(relwidth=0.08, relheight=0.04, relx=0.62, rely=0.56)
dose1_box.insert(INSERT, " " )
dose1_box.config(state=NORMAL, bd=0, font=('calibri', '12'))

dose2_box = tk.Text(Globals.tab2, height=1, width=1)
dose2_box.place(relwidt=0.08, relheight=0.04, relx=0.62, rely=0.61)
dose2_box.insert(INSERT, " ")
dose2_box.config(state=NORMAL, bd=0, font=('calibri', '12'))

dose3_box = tk.Text(Globals.tab2, height=1, width=1)
dose3_box.place(relwidt=0.08, relheight=0.04, relx = 0.62, rely=0.66)
dose3_box.insert(INSERT, " ")
dose3_box.config(state=NORMAL, bd=0, font=('calibri', '12'))

dose4_box = tk.Text(Globals.tab2, height=1, width=1)
dose4_box.place(relwidt=0.08, relheight=0.04, relx = 0.62, rely = 0.71)
dose4_box.insert(INSERT, " ")
dose4_box.config(state=NORMAL, bd=0, font=('calibri', '12'))

dose5_box = tk.Text(Globals.tab2, height=1, width=1)
dose5_box.place(relwidt=0.08, relheight=0.04, relx=0.62, rely=0.76)
dose5_box.insert(INSERT, " ")
dose5_box.config(state=NORMAL, bd=0, font=('calibri', '12'))


upload_button1 = tk.Button(Globals.tab2, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.nothingButton)
upload_button1.place(relwidth=0.1, relheight=0.04, relx=0.72, rely=0.56)

upload_button2 = tk.Button(Globals.tab2, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.nothingButton)
upload_button2.place(relwidth=0.1, relheight=0.04, relx=0.72, rely=0.61)

upload_button3 = tk.Button(Globals.tab2, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.nothingButton)
upload_button3.place(relwidth=0.1, relheight=0.04, relx=0.72, rely=0.66)

upload_button4 = tk.Button(Globals.tab2, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.nothingButton)
upload_button4.place(relwidth=0.1, relheight=0.04, relx=0.72, rely=0.71)

upload_button5 = tk.Button(Globals.tab2, text='Upload file', cursor='hand2', font=('calibri', '12'), highlightthickness=7, \
    overrelief=GROOVE, state=ACTIVE, width=12, command=Dose_response_functions.nothingButton)
upload_button5.place(relwidth=0.1, relheight=0.04, relx=0.72, rely=0.76)

uploaded_file_print1 = tk.Text(Globals.tab2, height=1, width=1)
uploaded_file_print1.place(relwidt=0.08, relheight=0.04, relx=0.84, rely=0.56)
uploaded_file_print1.insert(INSERT, " ")
uploaded_file_print1.config(state=DISABLED, bd=0, font=('calibri', '12'))

uploaded_file_print2 = tk.Text(Globals.tab2, height=1, width=1)
uploaded_file_print2.place(relwidt=0.08, relheight=0.04, relx=0.84, rely=0.61)
uploaded_file_print2.insert(INSERT, " ")
uploaded_file_print2.config(state=DISABLED, bd=0, font=('calibri', '12'))

uploaded_file_print3 = tk.Text(Globals.tab2, height=1, width=1)
uploaded_file_print3.place(relwidt=0.08, relheight=0.04, relx=0.84, rely=0.66)
uploaded_file_print3.insert(INSERT, " ")
uploaded_file_print3.config(state=DISABLED, bd=0, font=('calibri', '12'))

uploaded_file_print4 = tk.Text(Globals.tab2, height=1, width=1)
uploaded_file_print4.place(relwidt=0.08, relheight=0.04, relx=0.84, rely=0.71)
uploaded_file_print4.insert(INSERT, " ")
uploaded_file_print4.config(state=DISABLED, bd=0, font=('calibri', '12'))

uploaded_file_print5 = tk.Text(Globals.tab2, height=1, width=1)
uploaded_file_print5.place(relwidt=0.08, relheight=0.04, relx=0.84, rely=0.76)
uploaded_file_print5.insert(INSERT, " ")
uploaded_file_print5.config(state=DISABLED, bd=0, font=('calibri', '12'))


check1 = Checkbutton(Globals.tab2, variable=Globals.dose_response_var1)
check1.place(relx=0.94, rely=0.56)

check2 = Checkbutton(Globals.tab2, variable=Globals.dose_response_var2)
check2.place(relx=0.94, rely=0.61)

check3 = Checkbutton(Globals.tab2, variable=Globals.dose_response_var3)
check3.place(relx=0.94, rely=0.66)

check4 = Checkbutton(Globals.tab2, variable=Globals.dose_response_var4)
check4.place(relx=0.94, rely=0.71)

check5 = Checkbutton(Globals.tab2, variable=Globals.dose_response_var5)
check5.place(relx=0.94, rely=0.76)
##################################### TAB 3 - Map dose ############################################

temp_text = tk.Text(Globals.tab3, height=1, width=1)
temp_text.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.31)
temp_text.insert(INSERT,"lage en ny fane der en kan scanne en ukjent film og finne dose vha kalibreringskurva")
temp_text.config(state=DISABLED, bd=0) 




##################################### End statements ############################################
Globals.tab_parent.pack(expand=1, fill='both')
Globals.form.mainloop()