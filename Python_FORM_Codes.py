...test_function([2,4])
...tühi nimekiri seadistatakse nii >>> a = []
...suva asja saab sisse panna  >>> a = [1,2,3,7,9]

minu_asi = [1,2,3,7,9]
print(minu_asi)

# KAS NUMBER ON PAARIS PAARITU
my_number = 3
if my_number % 2 == 0:
    print("even")
else:
    print("odd")

 #also this works
my_number = 10
if my_number % 2 == 0:
    print("even")
elif my_number == 1:
    print("is 1")
else:
    print("odd")

# KAS NUMBER ON PAARIS PAARITU Töötab kenasti, kas number on aaritu või paaris:
my_number = 9
def is_even(n):
    if my_number % 2 == 0:
        return True
    else:
        return False
if is_even(my_number):      #NB! Siin on ühe asja teise kõhtu asetamine
    print("even")
else:
    print("ei ole")
    
    

#LOOP, TULEMUSEKS TEEB LOETELU ALATES 0 KUNI 10
for i in range(10):
    print(i)
    
#LOOP, TULEMUSEKS loetleb tähehaaval mis palutud
for i in "Hello":
    print(i)nc
    


    
   

# PROVIDE TODAY' DATE; HOW MANY DAYS FROM THE YEAR START
# IT RESULTS AS:
# 2017-05-24
# 143 days, 0:00:00
# 2017-05-25 00:00:00
# 2017-05-24 21:56:42.123157
# 2:03:17.876843
import datetime as dt
print(dt.datetime.utcnow().strftime("%Y-%m-%d"))
today = dt.date.today()
first_of_the_year = dt.date(year=2017, month=1, day=1)
print(today - first_of_the_year)
now = dt.datetime.now()
midnight = dt.datetime(year=now.year, month=now.month, day=(now.day +1))
print(midnight)
print(now)
print(midnight - now)
