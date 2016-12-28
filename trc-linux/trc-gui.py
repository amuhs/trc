"""Note Check: Locates any missing notes from an Excel workbook."""
import tkinter as tk
import backend
import datetime

BTN_LFT_CORNER = 460


def del_file():
    backend.secure_delete_file(tp)


def del_directory():
    backend.secure_delete_dir(tp)


def del_trash():
    backend.secure_delete_trash(tp)


def stayup_hour():
    backend.stay_awake('hour', time_text.get(), tp)


def stayup_min():
    backend.stay_awake('min', time_text.get(), tp)


def clear_text():
    tp.delete(1.0, tk.END)


# #################################################################
# CREATE TKINTER OBJECT
# #################################################################

# Create the window and configure
root = tk.Tk()
root.minsize(width=640, height=300)
root.configure(background='#21252b')
root.title('TRC')

# #################################################################
# BUTTONS
# #################################################################

# Secure Delete Trash
sdtb = tk.Button(root, text='Securely Delete Trash',
                 command=del_trash,
                 bg='#424855', fg='#adb2bc',
                 highlightthickness=0, bd=0)
sdtb.pack()
sdtb.place(x=BTN_LFT_CORNER, y=20, width=160, height=40)

# Secure Delete File
sdfb = tk.Button(root, text='Securely Delete File',
                 command=del_file,
                 bg='#424855', fg='#adb2bc',
                 highlightthickness=0, bd=0)
sdfb.pack()
sdfb.place(x=BTN_LFT_CORNER, y=65, width=160, height=40)

# Secure Delete Directory
sddb = tk.Button(root, text='Securely Delete Folder',
                 command=del_directory,
                 bg='#424855', fg='#adb2bc',
                 highlightthickness=0, bd=0)
sddb.pack()
sddb.place(x=BTN_LFT_CORNER, y=110, width=160, height=40)

# Keep computer awake buttons and labels
kca_label = tk.Label(root, text="Stay Awake",
                     bg='#424855', fg='#adb2bc',
                     highlightthickness=0, bd=0)
time_text = tk.StringVar()
time_field = tk.Entry(root, textvariable=time_text,
                      bg='#424855', fg='#797c82',
                      highlightthickness=0, bd=0)
time_field.insert(tk.END, '     -- Enter time here -- ')
kca_hour = tk.Button(root, text='Hours',
                     command=stayup_hour,
                     bg='#424855', fg='#adb2bc',
                     highlightthickness=0, bd=0)
kca_mins = tk.Button(root, text='Minutes',
                     command=stayup_min,
                     bg='#424855', fg='#adb2bc',
                     highlightthickness=0, bd=0)
kca_label.pack()
time_field.pack()
kca_hour.pack()
kca_mins.pack()

kca_label.place(x=BTN_LFT_CORNER, y=155, width=160, height=20)
time_field.place(x=BTN_LFT_CORNER, y=175, width=160, height=20)
kca_hour.place(x=BTN_LFT_CORNER, y=195, width=80, height=40)
kca_mins.place(x=BTN_LFT_CORNER + 80, y=195, width=80, height=40)

# Quit button
q = tk.Button(root, text='Quit', command=root.destroy, bg='#528bff',
              highlightthickness=0, bd=0)
q.pack()
q.place(x=BTN_LFT_CORNER, y=240, width=160, height=40)

# #################################################################
# TEXT BOX
# #################################################################

tp = tk.Text(root, bg='#424855', fg='#adb2bc',
             highlightthickness=0, bd=0)
date = datetime.datetime.now()
sdate = '{}.{}.{}'.format(date.month, date.day, date.year)
# tp.insert(tk.END, '{}\n'.format(sdate))
tp.insert(tk.END, '{}\t\tWelcome to TRC -- {}\n'.format('\n' * 8, sdate))
tp.insert(tk.END, '{}v1.0.0'.format('\t' * 3 + '   '))
tp.pack()
tp.place(x=20, y=20, width=420, height=260)

# #################################################################
# Initialize window
# #################################################################

root.mainloop()
