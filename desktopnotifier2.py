from win10toast import ToastNotifier
import time
tos=ToastNotifier()

i=1
while i < 10:
    tos.show_toast("Thank God for life","The Inner Mukonge Eric(TIME) is here" )
    i+1
    time.sleep(1)
