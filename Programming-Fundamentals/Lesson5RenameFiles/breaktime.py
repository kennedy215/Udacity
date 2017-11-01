import webbrowser
import time


def break_time():
    count = 0
    number_breaks = 3
    print("This program started on "+time.ctime())
    while(count < number_breaks):
        time.sleep(5)
        webbrowser.open("https://youtu.be/KBVskvS7-vo")
        print("break "+str(count+1))
        count = count + 1
break_time()
