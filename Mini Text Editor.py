import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Mini Text Editior')



######################## Main Menu ########################
#------------------------ End Main -------------------------
main_menu = tk.Menu()
#File Icons

new_icon = tk.PhotoImage(file='Icons/new.png')
open_icon = tk.PhotoImage(file='Icons/open.png')
save_icon = tk.PhotoImage(file='Icons/save.png')
save_as_icon = tk.PhotoImage(file='Icons/save as.png')
exit_icon = tk.PhotoImage(file='Icons/exit.png')

file = tk.Menu(main_menu, tearoff=False)


###Edit
###Edit Icons
copy_icon = tk.PhotoImage(file='Icons/copy.png')
paste_icon = tk.PhotoImage(file='Icons/paste.png')
cut_icon = tk.PhotoImage(file='Icons/cut.png')
clear_icon = tk.PhotoImage(file='Icons/clear.png')
find_icon = tk.PhotoImage(file='Icons/find.png')

edit = tk.Menu(main_menu, tearoff=False)


###View
###View Icons
tool_bar_icon = tk.PhotoImage(file='Icons/tool.png')
status_bar_icon = tk.PhotoImage(file='Icons/status.png')

view = tk.Menu(main_menu, tearoff=False)

###ColorTheme
red_icon = tk.PhotoImage(file='Icons/red.png')
blue_icon = tk.PhotoImage(file='Icons/blue.png')
green_icon = tk.PhotoImage(file='Icons/green.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (red_icon, blue_icon, green_icon)

color_dict = {
    'red_icon' : ('	#FFFFFF, #FF0000'),
    'blue_icon' : ('#FFFFFF, #00FFFF'),
    'green_icon' : ('	#FFFFFF, #008000')
}

# Cascade #
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)
######################## Tool Baar ########################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

###Font Box
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariables=font_family, state='readonly')
font_box['values'] = font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0, column=0, padx=7)

###Size Box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariables = size_var, state='readonly')
font_size[value] = tuple(range(8,100,3))
font_size.current(4)
font_size.grid(row=0, column=1, padx=7)

###Bold Button
bold_icon = tk.PhotoImage(file='Icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=7)

###Italic Button
italic_icon = tk.PhotoImage(file='Icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=2, padx=7)

###Underline Button
underline_icon = tk.PhotoImage(file='Icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=3, padx=7)


####Font Color Button
font_color_icon = tk.PhotoImage(file='Icons/text.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=4, padx=7)

###Align Left Button
align_left_icon = tk.PhotoImage(file='Icons/left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=5, padx=7)

###Align Right Button
align_center_icon = tk.PhotoImage(file='Icons/center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=6, padx=7)

###Align Center Button
align_right_icon = tk.PhotoImage(file='Icons/right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=7, padx=7)
#------------------------ End Toolbar -------------------------

######################## Txt Editor ########################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', releif=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


###Font Family and Font Size functionality
current_font_family = 'Arial'
current_font_size = 14

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

###Button Functionality
####Bold Button Fuctionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'noraml'))

bold_btn.configure(command=change_bold)

###Italic Button Fuctionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'noraml'))

italic_btn.configure(command=change_italic)

###Underline Button Fuctionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == '1':
        text_editor.configure(font=(current_font_family, current_font_size, 'noraml'))

underline_btn.configure(command=change_underline)

###Font Color Functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

###Align Functionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)

###Button Functionality End

text_editor.configure(font=('Arial', 14))

#------------------------ End Txt Editor -------------------------


######################## Status Bar ########################

status_bar = ttk.label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', changed)
#------------------------ End Status bar -------------------------

######################## Main Menu Functionality########################



###Variable
url = ''

##New Functionaly
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

###File Commands
file.add_command(label='New', image=new_icon , compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


###Open Functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.delete(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
file.add_command(label='Open', image=open_icon , compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)



####Save Functionality

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode= 'w', defaultextenstion='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.wirte(content2)
            url.close()
    except:
        return
file.add_command(label='Save', image=save_icon , compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)


#####Save As Functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode= 'w', defaultextenstion='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save as', image=save_as_icon , compound=tk.LEFT, accelerator='Ctrl+Alt+N', command=save_as)

###Exit Functionality
def exit_func(event=None):
    global url, text_changed
    try: 
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8',) as fw:
                        fw.write(content)
                        main_application.destroy()
            else:
                content2 = str(text_editor.get(1.0, tk.END))
                url = filedialog.asksaveasfile(mode= 'w', defaultextenstion='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                url.write(content2)
                url.close()
                main_application.destroy()
        elif mbox is False:
               main_application.destroy()
        else:
            main_application()
    except:
        return
file.add_command(label='Exit', image=exit_icon , compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)

####Find Functionality
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                 break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)



find_dialogue = tk.Toplevel()
find_dialogue.geometry('450x250+500+200')
find_dialogue.title('Find')
find_dialogue.resizable(0,0)



###Frame
find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
find_frame.pack(pady=20)



###Labels
text_find_label = ttk.Label(find_frame, text='Find : ')
text_replace_label = ttk.Label(find_frame, text='Replace')



###Entry Boxxes
find_input = ttk.Entry(find_frame, width=30)
replace_input = ttk.Entry(find_frame, width=30)



###Button
find_button = ttk.button(find_frame, text='find', command=find)
replace_button = ttk.button(find_frame, text='replace', command=replace)



#Label grid
text_find_label.grid(row=0, column=0, padx=5, pady=5)
text_replace_label.grid(row=1, column=0, padx=5, pady=5)



##Entry grid
find_input.grid(row=0, column=1, padx=4,pady=4)
replace_input.grid(row=1, column=1, padx=4,pady=4)



##button grid
find_button.grid(row=2, column=0, padx=8,pady=4)
replace_button.grid(row=2, column=1, padx=4,pady=4)


#####Edit Commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+c', command=lambda:text_editor.event_generate("<Control c"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+v',command=lambda:text_editor.event_generate("<Control v"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+x', command=lambda:text_editor.event_generate("<Control x"))
edit.add_command(label='Clear All', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+x', command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+f', command=find_func)



show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


####View Checkbutton
view.add_checkbutton(label='Toolbar', image=tool_bar_icon, compound=tk.LEFT, onvalue=True, offvalue=0, variable=show_toolbar, command=hide_toolbar)
view.add_checkbutton(label='Statusbar', image=status_bar_icon, compound=tk.LEFT,onvalue=1, offvalue=False, variable=show_statusbar, command=hide_statusbar)

####Color theme

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(backgound= bg_color, fg=fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image = color_icons[count], variable =theme_choice, copmound= tk.LEFT, command=change_theme)
    count += 1

#------------------------ End Main -------------------------



####Shortcuts Keys
main_application.bind("<Control-n", new_file)
main_application.bind("<Control-o", open_file)
main_application.bind("<Control-s", save_file)
main_application.bind("<Control-Alt-s", save_as)
main_application.bind("<Control-q", exit_func)
main_application.bind("<Control-f", find_func)


main_application.config(menu=main_menu)
main_application.mainloop