import datetime
import smtplib

#get current time
current_time = datetime.datetime.now()

#get previous time from database
prev_time = datetime.datetime.fromisoformat(database.get_prev_time())

#calculate total time spent in current session
total_time = current_time - prev_time

#calculate percentage change with previous session
percent_change = (total_time - database.get_prev_total_time()) / database.get_prev_total_time()

#send email with current session time and percentage change
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your email", "your password")

msg = "Current session time: " + str(total_time) + "\nPercentage change with previous session: " + str(percent_change)
server.sendmail("your email", "receiver email", msg)

server.quit()

#update database with current time and total time spent in current session
database.update_time(current_time, total_time)



