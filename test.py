import schedule
import datetime
import time


# def myprint():
#     print("hi" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# schedule.every().day.at("04:06:10").do(myprint)


# while True:
#     schedule.run_pending()
#     time.sleep(1)

# textstr = "{:.0f} %".format(2/3*100)

# print(textstr)


datetime1 = datetime.datetime.now()
# time.sleep(4)
datetime2 = datetime.datetime.now()

# print(datetime1.strftime("%Y%m%d%H%M"))
# print(datetime2)
# print(datetime1.strftime("%Y-%m-%d %H:%M:%S") < datetime2.strftime("%Y-%m-%d %H:%M:%S"))

print(datetime1.strftime("%Y-%m-%d %H:%M:%S") > "2022-08-18 01:44:00")

# x = datetime.datetime(2018, 6, 1, 23, 14, 39)
# print(x)

# print(x > datetime1)