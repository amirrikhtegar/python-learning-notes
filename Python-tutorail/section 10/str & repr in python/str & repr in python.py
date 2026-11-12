
# * str -> string -> __str__ -> غیر رسمی 

# زمانی از str استفاده میکنیم که میخواهیم به کاربر نشان دهیم

# * repr -> representation => output : string representation -> __repr__ -> رسمی

# repr : باعث میشود قابلیت ساخت دوباره obj رو داشته باشیم 
# برخی مواقع^

# زمانی از repr استفاده میشود که بار توسعه دهنده هست 

print(str("ali"))
print(repr("ali"))

print(dir("ali")) # output: __str__, __repr__

import datetime

today = datetime.datetime.now()

print(str(today)) # 2026-09-19 09:05:25.482789 # کاربر

print(repr(today)) # datetime.datetime(2026, 9, 19, 9, 5, 25, 482789) # توسعه دهنده

print(datetime.datetime(2026, 9, 19, 9, 5, 25, 482789))

# در حالت تعاملی repr دیفالت هست

# در vscode str حالت defalt هست

