
# ! part 1

# * Object-oriented programming (oop)
# ! Attributes / Properties (خصوصیات)
# ! Methods / Functions (رفتار)

# ? class in (class attributes and behavior) -> object or instance
# ? Class (Attributes + Behaviors) -> Instantiating (ساختن) -> Object / Instance


# * Instance

# 1) Class Definition (Attributes + Behaviors)
class Player:
    def __init__(self, username, level):
        self.username = username  # Attribute
        self.level = level        # Attribute

    def level_up(self):           # Behavior
        self.level += 1


# 2) Object / Instance Creation
p1 = Player("attila", 1)  # object 1
p2 = Player("jack", 5)    # object 2

# 3) Behavior execution
p1.level_up()

print(p1.level)  # 2 (تغییر کرد)
print(p2.level)  # 5 (بدون تغییر ماند، چون هر شیء ایزوله‌ست)

# * Object-oriented analysis (ooa)
# * Object-oriented deasign (ood)
# * Object-oriented programming (oop)

x = 5
y = 10
print(type(x)) # ! <class 'int'>
print(id(x)) # ? 11759912 ثابت هست id و اختصاصی
print(type(y)) # ! <class 'int'>
d = [1, 2, 3, 4]
print(type(d)) # ! <class 'list'>

# ! part 2

# * Encapsulation (مفهموم کپسول سازی)
# ? methods + attributes in class = object
# * Data Hiding (مفهموم پنهان سازی داده)
# ? + plus on encapsulation
# * Interface (مفهموم رابطه)


# ! part 3

# * abstraction (مفهموم انتزاع)
# ? توجه به کلیات، بدون توجه زیاد به جزيیات
# ? هرچی جزيیات کمتر ، سطح انتزاع بالاتر

# * inheritance (ارث بری)

# ? یعنی استفاده از یک کلاس دیگر برای نوشتن یک کلاس دیگر که کلاس دوم ما تمام تایع های کلاس اول رو دارد ولی خودش هم تابع های جدیدی دارد 

# -------------------------

# ? class=> برای نگاه انتزاعی تر هست یه این دلیل که ما به جای دسترسی دادن به کاربر به تابع ها یک کلاس در دسترس کاربر میگذاریم 

# * abstrac class
# ? هرچی به کلاس های بالا تر برمی انتزاعی تر هست 

# !            <= انتزعی بیشتر
# ? متغیر، حلقه و شرط،‌توابع ،‌کلاس ،‌کلاس های انتزاعی تر

# ? abstract class => کلاس های انتزاعی تر
# ? concrete class => کلاس

# ! part 4

# * association, aggregation, composition

# * composition => ترکیب
# ? for abstraction use composition or inheritanc
# ? composition => جمع آوری چندین شی با هم،‌برای ایجاد یک شی جدید. برای زمانی استفاده میشود ، که یک شی بخشی از شی دیگر باشد 
# ? در ارث بری رابطه ما (IS-A) هست
# ? در ترکیب رابطه ما (HAS-A) هست

# ! association > aggregation > composition

# ? association : دقت کنید در این نوع رابطه معمولا شی اول جزیی از شی دوم نیست , در صورت نبود ارتباط شی از بین نمیرود
#        ^
# ? aggregation : در این نوع رابطه شی اول جزیی از شی دوم است , ولی دو شی جدا از هم معنی میدهند
#        ^
# ? composition : در این نوع رابطه شی اول جزیی از شی دوم است و دو شی جدا از هم معنی نمیدهند و دو شی جدا از هم وجود ندارن و به رابطه مرگ معروف هست

# ! در اخر با تغیر نوع دیدگاه به شی ها رابطه انها ممکن هست تغییر کند

# ! part 5

# * inheritance (ارث بری)

# ? پر استفاده ترین رابطه و معروف ترین هست(inheritance (ارث بری))

# ? in inheritance => (Is-A)
# ? ^= ClassA(Parent class, Base class, Superclass) + ClassB(Child class, Derived class, Subclass)

# ? انواع وراثت => single, hierarchial, multilevel, hybrid, multiple

# * Method Resolution Order (MRO)

# ? MRO => علویت بندی در ارث بری که از پایین به بالا و چپ به راست است و در نهایت کلاس ابجکت را بررسی میکند  

# ? method mro وجود دارد  

# ! part 6

# * Polymorphism (چند ریختی)

# ? بتوانیم با اشیاء متفاوت، از یک رابط مشترک استفاده کنیم؛ ولی هر شیء همان درخواست را به شیوه‌ی خودش انجام دهد.

# ? 4 type of Polymorphism => subtype(runtime), parametric(overloading), ad hoc(compile-time), coercion(casting)
# ? override , template, mthode/ operator overloading, ....

# ? (override, overloading)برای ما این دوتا مهم تر هست 

# * Duck Typing
# * if it looks like a duck walks like a duck and quacks like a duck it is a duck
