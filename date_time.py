from datetime import datetime , date , timedelta , timezone
import time


# # for get current time & date

# def current_date_time():
    
#     now = datetime.now()
#     print("Today (time and Date) : ",now)
#     print("year : ",now.year)
#     print("month : ",now.month)
#     print("day : ",now.day)
#     print("hour : ",now.hour)
#     print("minute : ",now.minute)
#     print("second : ",now.second)
    
# current_date_time() 

# # formatinf date time value 

# def datetime_formate():
    
#     now = datetime.now()
    
#     print("dd-mm-yyyy : ",now.strftime("%d-%m-%Y"))
#     print("dd-mm-yy : ",now.strftime("%d-%m-%y"))
#     print("mm-dd-yyyy : ",now.strftime("%m-%d-%Y"))
#     print("yyyy-mm-dd : ",now.strftime("%Y-%m-%d"))

# datetime_formate()


# # difference between 2 dates 

# def date_difference():
    
#     now = datetime.now()
    
#     start = "12-09-2026"
#     end = "12-10-2026"
    
#     start_date = datetime.strptime(start,"%d-%m-%Y")
#     end_date = datetime.strptime(end,"%d-%m-%Y")

#     difference = abs(end_date - start_date).days

#     print(f"days : {difference}")    
# date_difference()


# # time in seconds

# def seconds_time():
     
#     value = time.time()
#     print("seconds : ",value)
    
# seconds_time()

# # calculate execution time

# def calculate_execution_time():
    
#     def print_numbers():
#         total = 0
#         for i in range(1,101):
#             total += i
#         print("total of 1 to 100 : ",total)
            
#     start = time.time()
#     print_numbers()
#     end = time.time()
    
#     execution_time = start - end
    
#     print("execution time : ",execution_time)
# calculate_execution_time()


# def current_time():

#     now = datetime.now()
#     print("current time : ",now.strftime("%d-%m-%Y %H:%M:%S"))
    
# current_time()


# lab questions

# 1.

# def current_time():
#     now = datetime.now()
#     print("year : ",now.year)
#     print("month : ",now.month)
#     print("day : ",now.day)
#     print("hour : ",now.hour)
#     print("minute : ",now.minute)
#     print("second : ",now.second)
# current_time()

# 2.

# def show_time():
#     now = datetime.now()
#     print("current time : ",now)
#     print("timestamp : ",time.time())
#     print("readabletime : ",time.ctime())
# show_time()

# 3.

# def date_time():
#     now = datetime.now()
    
#     date = now.date()
#     time = now.time()
#     date_1 = date.strftime("%d/%m/%Y")
#     date_2 = date.strftime("%m/%d/%Y")
#     time_1 = time.strftime("%H:%M:%S")
#     time_2 = time.strftime("%I:%M:%S")
    
#     print("date formate 1 :",date_1)
#     print("date formate 2 :",date_2)
#     print("time (24 hours) :",time_1)
#     print("time (12 hours) :",time_2)
    
# date_time()

# 4.

# def date_time():
    
#     date1 = date(2026,11,8)    
#     date2 = date(2026,10,14)    
#     date_difference = ((date1 - date2).days)
#     print("difference between two dates : ",date_difference)
    
#     today = date.today()
#     add_days = today + timedelta(days=7)
#     print(today)
#     print("added days date : ",add_days)
    
# date_time()

# 5.

# def date_time():
    
#     date = "2024-01-01"
#     date_object = datetime.strptime(date,"%Y-%m-%d")
#     date_str = date_object.strftime("%Y-%m-%d %H:%M:%S")
#     print(date_str)
    
# date_time()

# 6.

# def calculate_time():
    
#     def total_calculate():
        
#         total =  0
#         for i in range(0,101):
#             total += i
#         return total  
           
#     start_time = time.time()
#     result = total_calculate()
#     end_time = time.time()
        
#     time_difference = end_time - start_time
    
#     print("result : ",result)
#     print("time difference : ",time_difference)
        
# calculate_time()    

# 7.

# def time_formate():
    
#     localtime = time.localtime()
#     utctime = time.gmtime()
#     print("localtime : ",time.strftime("%Y-%m-%d %H:%M:%S",localtime))
#     print("utctime : ",time.strftime("%Y-%m-%d %H:%M:%S",utctime))

# time_formate()

# 8.

# def stopwatch():
    
#     start_time = None
#     elapsd_time = 0
        
#     while True:
        
#         print("1. start stopwatch")
#         print("2. stop stopwatch")
#         print("3. reset stopwatch")
#         print("4. exit")
        
#         choice = int(input("enter your choice : "))
    
#         if choice == 1:
           
#            if start_time is None:
               
#                start_time = time.time()
#                print("stop start.............")
            
#            else:
#                print("stop watch already running !!")
        
#         elif choice == 2 :
            
#             if start_time is not None:
                
#                 elapsd_time = elapsd_time + (time.time() - start_time)
#                 start_time = None
                
#                 print("stop watch stoped............")
#                 print("Time : ",round(elapsd_time,2),"seconds")
#             else:
                
#                 print("first start stopwatch with choice 1")
        
#         elif choice == 3:
            
#             start_time = None
#             elapsd_time = 0
#             print("stop watch reset..........")
        
        
#         elif choice == 4 :
            
#             print("existing the program ! bye !")
            
#             break
        
#         else:
#             print("invalid choice enterted !!")        

# stopwatch()

# 9.

# def countdown():
    
#     seconds = int(input("enter seconds value : "))

#     while seconds > 0:
        
#         print(seconds)
#         time.sleep(1)
        
#         seconds -= 1
#     print("Time's up !")
    
# countdown()

# 10.

# def leap_year():
#     while True : 
#         year = int(input("Enter a year : "))
        
#         last_day = date(year,3,1) - timedelta(days=1)
        
#         last_feb_date = datetime.strftime(last_day,"%d")

#         if int(last_feb_date) == 29 :
#             print("This year is Leap year !")
#         else:
#             print("This year is not Leap year !")
    
# leap_year()

# 11.

# def get_date():
    
#     date = input("enter date (YYYY-MM-DD) : ")
    
#     str_date = datetime.strptime(date,"%Y-%m-%d")

#     print(f"Day of the week : {datetime.strftime(str_date,"%A")}")
    
# get_date()

# 12.

# def reminder_time():
#     seconds = int(input("enter the seconds (after completing those seconds , i will give the reminder to you !! : "))
#     print("time starts now ! ")
#     time.sleep(seconds)
#     print(f"yeh !! it's your reminder after {seconds} seconds !")
# reminder_time()