"""Backend for trc."""
from tkinter import filedialog as fdialog
from tkinter import messagebox as msgbx
import tkinter as tk
import os
import threading


def stay_awake(time_type, time_length, text_box):
    if time_length != '  Enter time here':
        if time_type == 'hour':
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, 'Keeping your computer up for {} hours.\n'.
                            format(time_length))
            time_length = float(time_length) * 60 * 60
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,
                            'Keeping your computer up for {} minutes.\n'.
                            format(time_length))
            time_length = float(time_length) * 60

        text_box.insert(tk.END, 'nohup caffeinate -t {} &> /dev/null &\n'.format(time_length))
        text_box.insert(tk.END, 'You may close TRC.\n')
        os.system('nohup caffeinate -t {} &> /dev/null &'.format(time_length))
    else:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, 'Please supply an amount of time.\n')


def secure_delete_trash(text_box):
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, 'Securely deleting trash...\n')
    text_box.insert(tk.END, 'nohup srm -rfv ~/.Trash/* &> /dev/null &\n')
    text_box.insert(tk.END, 'You may close TRC.\n')
    os.system('nohup srm -rfv ~/.Trash/* &> /dev/null &')


def secure_delete(ftype, text_box):
    if ftype == 'file':
        file_name = fdialog.askopenfilename()
        if file_name:
            index = file_name.rfind('/')
            short_file_name = file_name[index + 1:]
            new_file_name = '{}/"{}"'.format(file_name[:index], short_file_name)
            uid = os.stat(file_name).st_uid
            if uid == 0:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'Must have root access to remove "{}".\n'.format(short_file_name))
                text_box.insert(tk.END, '[ PERMISSION DENIED ]')
                return False
            msg_response = msgbx.askyesno(None, 'Remove "{}"?\nThis cannot be undone.'.format(short_file_name))
            if msg_response:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'Removing "{}"\n'.format(short_file_name))
                text_box.insert(tk.END, 'Executed: srm {}\n'.format(new_file_name))
                text_box.insert(tk.END, '[ PLEASE WAIT ]')
                os_thread = threading.Thread(name='os_thread', target=sd_file, args=(new_file_name, text_box))
                os_thread.start()
            else:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'File removal aborted')
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, 'File removal aborted')
    else:
        dir_name = fdialog.askdirectory()
        if dir_name:
            index = dir_name.rfind('/')
            short_dir_name = dir_name[index + 1:]
            new_dir_name = '{}/"{}"'.format(dir_name[:index], short_dir_name)
            uid = os.stat(dir_name).st_uid
            if uid == 0:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'Must have root access to remove "{}".\n'.format(short_dir_name))
                text_box.insert(tk.END, '[ PERMISSION DENIED ]')
                return False
            msg_response = msgbx.askyesno(None, 'Remove "{}"?\nThis cannot be undone.'.format(short_dir_name))
            if msg_response:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'Removing "{}".\n'.format(short_dir_name))
                text_box.insert(tk.END, 'Executed: srm -r {}\n'.format(new_dir_name))
                text_box.insert(tk.END, '[ PLEASE WAIT ]')
                os_thread = threading.Thread(name='os_thread', target=sd_folder, args=(new_dir_name, text_box))
                os_thread.start()
            else:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, 'Folder removal aborted')
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, 'Folder removal aborted')


def sd_file(f, tb):
    os.system('srm {}'.format(f))
    tb.delete(3.0, tk.END)
    tb.insert(tk.END, '\n[ COMPLETE ]')


def sd_folder(d, tb):
    os.system('srm -r {}'.format(d))
    tb.delete(3.0, tk.END)
    tb.insert(tk.END, '\n[ COMPLETE ]')
