import webbrowser;
import time;

breaks_no = 3;
break_count = 0;

print("This Program Started at: " + time.ctime());
while(break_count < breaks_no):
    time.sleep(5); #Delay program for x-sec
    webbrowser.open("https://www.google.com"); #Launch Web browser
    break_count = break_count + 1;
