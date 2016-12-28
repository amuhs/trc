"""Backend for trc-gui."""
from tkinter import filedialog as fdialog
from tkinter import messagebox as msgbx
import tkinter as tk
import os


def stay_awake(time_type, time_length, text_box):
    if time_length != '     -- Enter time here -- ':
        if time_type == 'hour':
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, 'Keeping your computer up for {} hours.\n'.
                            format(time_length))
            text_box.insert(tk.END, 'You may close TRC.\n')
            os.system('nohup caffeinate -t {} &'.
                      format(float(time_length) * 60 * 60))
            text_box.insert(tk.END, '\n[ COMPLETE ]\n')
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Keeping your computer up for {} minutes.\n'.
                            format(time_length))
            text_box.insert(tk.END, 'You may close TRC.\n')
            os.system('nohup caffeinate -t {} &'.
                      format(float(time_length) * 60))
            text_box.insert(tk.END, '\n[ COMPLETE ]\n')
    else:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, 'Please supply an amount of time.\n')


def secure_delete_trash(text_box):
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, 'Securely deleting trash...\n')
    os.system('srm -rfv ~/.Trash/*')
    text_box.insert(tk.END, '\n[ COMPLETE ]\n')


def secure_delete_file(text_box):
    file_name = fdialog.askopenfilename()
    if file_name:
        ind = file_name.rfind('/')
        file_name_short = file_name[ind + 1:]
        answer = msgbx.askyesno('',
                                'Remove "{}"?\nThis cannot be undone.'.
                                format(file_name_short))
        if answer:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Securely removing "{}"...\n'.
                            format(file_name_short))
            os.system('srm -v {}'.format(file_name))
            text_box.insert(tk.END,
                            '\n[ COMPLETE ]\n'.format(file_name))
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Secure file delete canceled.\n'.format(file_name))


def secure_delete_dir(text_box):
    dir_name = fdialog.askdirectory()
    if dir_name:
        ind = dir_name.rfind('/')
        dir_name_short = dir_name[ind + 1:]
        answer = msgbx.askyesno('',
                                'Remove "{}"?\nThis cannot be undone.'.
                                format(dir_name_short))
        if answer:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Securely removing "{}"...\n'.
                            format(dir_name_short))
            os.system('srm -rv {}'.format(dir_name))
            text_box.insert(tk.END,
                            '\n[ COMPLETE ]\n'.format(dir_name))
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Secure folder delete canceled.\n'.
                            format(dir_name))
