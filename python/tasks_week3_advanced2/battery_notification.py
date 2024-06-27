from plyer import notification
import psutil


battery=psutil.sensors_battery()
percent=battery.percent
print(percent)
notification.notify("Battery percentage",str(percent)+"%percent remaining")

# i did not fine pynotifier and .send i did it by plyer
#otification.notify("Battery percentage",str(percent)+"%percent remaining").send()