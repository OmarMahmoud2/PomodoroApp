from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ' '
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  global mark
  global reps
  window.after_cancel(timer)
  label1.config(text='Timer')
  label2.config(text=' ')
  canvas.itemconfig(text_counter, text='00:00')
  mark = ' '
  reps = 0
  
# ---------------------------- TIMER MECHANISM ------------------------------- #
def initiate():
  global reps
  reps = 0
  if reps < 1:
    work = WORK_MIN * 60
    count(work)
    label1.config(text='Work Timer')
    reps = 1
    
def start_timer():
  global reps
  global mark
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  
  if reps in [0, 2, 4, 6]:
    count(work_sec)
    reps += 1
    label1.config(text='Work Timer')
    #canvas.itemconfig(image, image = work)
  elif reps in [1, 3, 5]:
    mark += '✔'
    label2.config(text= mark)
    count(short_break_sec)
    reps += 1
    label1.config(text='Short Break Timer')
    #canvas.itemconfig(image, image='short.png')
  elif reps == 7:
   # canvas.itemconfig(image, image='long.png')
    mark += '✔'
    label2.config(text= mark)
    count(long_break_sec)
    reps =0
    label1.config(text='Long Break Timer')
  


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count(num):
  countmin = math.floor(num / 60)
  countsec = num % 60  
  if countsec == 0:
    countsec = '00'
  elif countsec < 10:
    countsec = f'0{countsec}'
  canvas.itemconfig(text_counter, text = f'{countmin}:{countsec}')
  if num > 0:
    global timer
    timer = window.after(1000, count, num -1)
  else: 
    start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro App')
window.minsize(350, 180)
window.config(padx=30, pady=20, bg= YELLOW)



canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
img = PhotoImage(file='tomato.png')
#work = PhotoImage(file='short.png')
image = canvas.create_image(100, 112, image=img)
text_counter = canvas.create_text(100, 140, text='00:00', fill='white', font=('papyrus', 20, 'bold'))
canvas.grid(column= 1, row=1)


label1= Label(text='Timer',fg= RED, bg= YELLOW, font=('Times New Roman', 15, 'bold'))
label1.grid(column= 1, row= 0)

label2= Label(text= mark , bg= YELLOW, fg=GREEN, font=('ariel', 15, 'normal'))
label2.grid(column=1, row=2)

button1 = Button(text= 'Start', height= 2, width= 5, highlightthickness= 0, command = initiate)
button1.grid(column=0, row= 2)
button2 = Button(text='Reset', highlightthickness= 0, command= reset)
button2.grid(column=2, row=2)

button3 = Button(text='Exit', highlightthickness= 0,  command= window.destroy)
button3.grid(column=1, row=4)









window.mainloop()

