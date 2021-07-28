from tkinter import *
import random

#Main
root = Tk()
root.title('Name Generator')
root.geometry('1280x720')
root.resizable(False, False)
root.configure(bg='white')
#Variables
firstnames_list = ['Mary',  'John' , 'Patricia' , 'Robert' , 'Jennifer' , 'Michael' , 'Linda' , 'William' , 'Elizabeth' , 'David' , 'Barbara' , 'Richard' , 'Susan' , 'Joseph' , 'Jessica' , 'Thomas' , 'Sarah' , 'Charles', 'Karen',  'Christopher' ,  'Nancy',  'Daniel',   'Lisa',  'Matthew' , 'Margaret', 'Anthony' , 'Betty', 'Donald',  'Sandra',  'Mark',   'Ashley',  'Paul',   'Dorothy',  'Steven',   'Kimberly' , 'Andrew',   'Emily',  'Kenneth',   'Donna', 'Joshua',  'Michelle', 'Kevin',  'Carol' , 'Brian',   'Amanda',  'George',  'Melissa', 'Edward',  'Deborah', 'Ronald',  'Stephanie', 'Timothy',  'Rebecca', 'Jason',  'Laura', 'Jeffrey' ,'Sharon','Ryan','Cynthia','Jacob','Kathleen','Gary','Amy','Nicholas','Shirley','Eric','Angela','Jonathan','Helen','Stephen','Anna','Larry','Brenda','Justin','Pamela','Scott','Nicole','Brandon','Samantha','Benjamin','Katherine']
last_names_list = ['Smith', 'Williams', 'Brown', 'Davis', 'Rodriguez', 'Martinez', 'Taylor', 'Thomas', 'Anderson', 'Wilson', 'White', 'Howard', 'Thompson', 'Jackson', 'Lee', 'Perez', 'Young', 'Walker']


#Functions
def generate():
    fn_rnd = random.choice(firstnames_list)
    ln_rnd = random.choice(last_names_list)
    output_name.configure(text=str(fn_rnd) + ' ' + str(ln_rnd))




#Widgets
title_label = Label(root)
title_generate = Label(root)
generate_button = Button(root)
output_title = Label(root)
output_name = Label(root)


#Widgets Configurations
title_label.config(text='Name Generator', fg='darkred', bg='lightgray', font=('Helvetica', 28, 'italic', 'bold'), padx=500, pady=10, border=5)
title_generate.config(text='Generate', font=('Helvetica', 18, 'bold'), fg='black', bg='white')
generate_button.config(text='Generate name', font=('Roboto', 15), fg='red', bg='black', padx=10, pady=12, border=10, command=generate)
output_title.config(text='Output Name: ', font=('Helvetica', 18, 'bold'), fg='black', bg='white')
output_name.config(font=('Helvetica', 18, 'bold'), fg='green', bg='black')

#Widgets Display
title_label.pack(anchor=CENTER)
#title_generate.place(x=100, y=200)
generate_button.place(x=500, y=600)
output_title.place(x=100, y=200)
output_name.place(x=400, y=200)

#Mainloop
root.mainloop()
