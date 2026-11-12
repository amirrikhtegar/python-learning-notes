from termcolor import colored
# all board hose
board = list(range(1,10))
# win hose
winners = ((0, 1, 2), (3, 4, 5),
    (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6))

moves = ((1, 3, 7, 9), (5, ), (2, 4, 6, 8))


print(board)


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "Attila":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "Parsia":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def make_move(brd, play, mv, undo=False):
    if can_move(brd, mv):
        brd[mv-1] = play
        win = is_winner(brd, play)
        if undo:
            brd[mv-1] = mv
        return True, win
    return False, False


def can_move(brd, mv):
    if mv in range(1, 10) and isinstance(brd[mv-1], int):
        return True
    return False


def has_empty_space():
    return board.count("Attila") + board.count("Parsia") != 9


def is_winner(brd, play):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != play:
                win = False
                break
        if win:
            break
    return win


def comuter_move():
    mv = -1
    # ایا خود کامپیوتر می تواند برنده شود؟
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # اگر کاربر می تواند برنده شود جلوش رو بگیر 
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    # اگر نه کاربر می تواند برنده شود نه کامپیوتر
    if mv == -1:
        for tup in moves:
            for am in tup:
                if mv == -1 and can_move(board, am):
                    print("mmmmmm", am)
                    mv = am
                    break
    return make_move(board, computer, mv)



player, computer = "Attila", "Parsia"
print(f"Player: {player}\nComputer: {computer}\n", "*"*30)



while has_empty_space():
    
    print_board()
    move = int(input("choose :"))
    moved, won = make_move(board, player, move)
    if not moved:
        print("\nInvalid number! try again!")
        continue
    if won:
        print(colored("\nYou Won!\n", "green"))
        break
    elif comuter_move()[1]:
        print(colored("\nYou loser!\n", "yellow"))
        break
    

# برای دیدن وضعیت بورد
print_board()

# versin 2

from termcolor import colored

# ========== تعریف تخته بازی و قوانین ==========

# تخته بازی: یه لیست از اعداد 1 تا 9 که نشون‌دهنده 9 خونه‌ست
# هر خونه یا یه عدد هست (خالیه) یا اسم بازیکن (پر شده)
board = list(range(1,10))

# حالت‌های برنده شدن: هر تاپل نشون میده کدوم 3 تا خونه باید یکی باشن تا برنده بشی
# مثلاً (0,1,2) یعنی سطر اول، (0,4,8) یعنی قطر اصلی
winners = ((0, 1, 2), (3, 4, 5),  # سطرهای افقی
    (6, 7, 8), (0, 3, 6),          # ستون‌های عمودی
    (1, 4, 7), (2, 5, 8),          # ستون‌های عمودی
    (0, 4, 8), (2, 4, 6))          # قطرها (مورب‌ها)

# اولویت حرکت کامپیوتر: اول گوشه‌ها (1,3,7,9)، بعد وسط (5)، آخر لبه‌ها (2,4,6,8)
# چون گوشه‌ها استراتژیک‌ترن!
moves = ((1, 3, 7, 9), (5, ), (2, 4, 6, 8))


print(board)  # یه بار تخته رو چاپ می‌کنیم ببینیم درست شروع شده


def print_board():
    """
    تخته بازی رو با رنگ‌های قشنگ چاپ می‌کنه.
    
    حرکت‌های Attila رو قرمز و Parsia رو آبی نشون میده.
    خونه‌های خالی رو با شماره‌شون نمایش میده.
    """
    j = 1  # شمارنده برای فهمیدن کِی باید سطر بعدی رو شروع کنیم
    
    # حالا می‌ریم رو هر خونه از تخته
    for i in board:
        end = " "  # معمولاً بعد از هر خونه یه فاصله میذاریم
        
        # اگه خونه سوم سطر بود، باید بریم سطر بعد
        if j % 3 == 0:
            end = "\n\n"  # دو تا خط خالی برای قشنگی!
        
        # اگه این خونه مال Attila بود، قرمز چاپش کن
        if i == "Attila":
            print(colored(f"[{i}]", "red"), end=end)
        # اگه مال Parsia بود، آبی چاپش کن
        elif i == "Parsia":
            print(colored(f"[{i}]", "blue"), end=end)
        # اگه خالی بود، فقط شماره‌ش رو نشون بده
        else:
            print(f"[{i}]", end=end)
        
        j += 1  # بریم سراغ خونه بعدی


def make_move(brd, play, mv, undo=False):
    """
    یه حرکت رو روی تخته انجام میده (یا شبیه‌سازی می‌کنه).
    
    Args:
        brd (list): تخته بازی
        play (str): نام بازیکن ("Attila" یا "Parsia")
        mv (int): شماره خونه‌ای که می‌خوایم حرکت کنیم (1 تا 9)
        undo (bool): اگه True باشه، حرکت رو فقط شبیه‌سازی می‌کنه و برمی‌گردونه
    
    Returns:
        tuple: (آیا حرکت معتبر بود؟, آیا این حرکت برنده شد؟)
    """
    # اول چک کن ببین اصلاً می‌شه این حرکت رو انجام داد یا نه
    if can_move(brd, mv):
        # خب میشه! پس اسم بازیکن رو بذار تو اون خونه
        brd[mv-1] = play  # mv-1 چون لیست از 0 شروع میشه ولی خونه‌ها از 1
        
        # حالا چک کن ببین با این حرکت برنده شدیم یا نه
        win = is_winner(brd, play)
        
        # اگه فقط می‌خواستیم تست کنیم (undo=True)، حرکت رو برگردون
        if undo:
            brd[mv-1] = mv  # شماره خونه رو دوباره بذار سرجاش
        
        return True, win  # حرکت معتبر بود و نتیجه برد رو برگردون
    
    # اگه نمیشه این حرکت رو انجام داد، False برگردون
    return False, False


def can_move(brd, mv):
    """
    چک می‌کنه که آیا می‌شه تو این خونه حرکت کرد یا نه.
    
    Args:
        brd (list): تخته بازی
        mv (int): شماره خونه (1 تا 9)
    
    Returns:
        bool: True اگه خونه خالی باشه، وگرنه False
    """
    # دو تا شرط: 1) عدد بین 1 تا 9 باشه  2) خونه هنوز خالی باشه (عدد باشه نه اسم)
    if mv in range(1, 10) and isinstance(brd[mv-1], int):
        return True
    return False


def has_empty_space():
    """
    چک می‌کنه که آیا هنوز جای خالی تو تخته هست یا نه.
    
    Returns:
        bool: True اگه جای خالی باشه، وگرنه False
    """
    # اگه مجموع حرکت‌های دو بازیکن برابر 9 نباشه، یعنی هنوز جا داریم
    return board.count("Attila") + board.count("Parsia") != 9


def is_winner(brd, play):
    """
    چک می‌کنه که آیا این بازیکن برنده شده یا نه.
    
    بررسی می‌کنه که آیا بازیکن تونسته 3 تا خونه رو تو یه خط (افقی، عمودی یا مورب) پر کنه.
    
    Args:
        brd (list): تخته بازی
        play (str): نام بازیکن
    
    Returns:
        bool: True اگه برنده شده باشه، وگرنه False
    """
    win = True  # فرض می‌کنیم برنده شده (بعداً چک می‌کنیم)
    
    # بریم رو هر حالت برنده (هر تاپل از winners)
    for tup in winners:
        win = True  # برای این حالت فرض کن برنده شده
        
        # حالا چک کن هر 3 تا خونه این حالت رو
        for j in tup:
            # اگه یکیش مال این بازیکن نبود، پس این حالت برنده نیست
            if brd[j] != play:
                win = False
                break  # نیازی نیست بقیه رو چک کنیم
        
        # اگه یه حالت برنده پیدا کردیم، دیگه نیازی به چک کردن بقیه نیست
        if win:
            break
    
    return win


def comuter_move():
    """
    هوش مصنوعی کامپیوتر! استراتژی حرکت رو تعیین می‌کنه.
    
    اولویت‌ها:
    1. اگه می‌تونه برنده بشه، برنده میشه
    2. اگه بازیکن داره می‌بره، جلوش رو می‌گیره
    3. وگرنه بهترین حرکت ممکن رو انجام میده (گوشه‌ها، وسط، لبه‌ها)
    
    Returns:
        tuple: (آیا حرکت معتبر بود؟, آیا کامپیوتر برنده شد؟)
    """
    mv = -1  # هنوز حرکتی انتخاب نکردیم
    
    # ========== اولویت 1: آیا خود کامپیوتر می‌تواند برنده شود؟ ==========
    # بریم رو همه خونه‌ها و ببینیم کدوم یکی برنده‌مون می‌کنه
    for i in range(1, 10):
        # این حرکت رو تست کن (undo=True یعنی فقط شبیه‌سازی)
        if make_move(board, computer, i, True)[1]:  # [1] یعنی بخش "برنده شدن"
            mv = i  # این حرکت برنده‌مون می‌کنه! انتخابش کن
            break  # پیدا کردیم، دیگه نیازی به جستجو نیست
    
    # ========== اولویت 2: اگر کاربر می‌تواند برنده شود، جلوش رو بگیر ==========
    if mv == -1:  # اگه هنوز حرکتی انتخاب نکردیم
        for j in range(1, 10):
            # ببین اگه کاربر این حرکت رو بزنه، برنده میشه؟
            if make_move(board, player, j, True)[1]:
                mv = j  # باید جلوش رو بگیریم!
                break
    
    # ========== اولویت 3: اگر نه ما برنده میشیم نه اون، حرکت استراتژیک بزن ==========
    if mv == -1:  # هنوز حرکتی انتخاب نکردیم
        # بریم رو اولویت‌ها: اول گوشه‌ها، بعد وسط، آخر لبه‌ها
        for tup in moves:
            for am in tup:
                # اولین خونه خالی که پیدا کردیم رو انتخاب کن
                if mv == -1 and can_move(board, am):
                    print("mmmmmm", am)  # یه پیام دیباگ (می‌تونی حذفش کنی)
                    mv = am
                    break
    
    # حالا حرکت انتخابی رو واقعاً انجام بده (نه شبیه‌سازی)
    return make_move(board, computer, mv)



# ========== تعریف بازیکنها ==========
player, computer = "Attila", "Parsia"
print(f"Player: {player}\nComputer: {computer}\n", "*"*30)



# ========== حلقه اصلی بازی ==========
while has_empty_space():  # تا وقتی جای خالی داریم، بازی ادامه داره
    
    # تخته رو نشون بده
    print_board()
    
    # از کاربر بپرس کدوم خونه رو می‌خواد
    move = int(input("choose :"))
    
    # حرکت کاربر رو انجام بده
    moved, won = make_move(board, player, move)
    
    # اگه حرکت نامعتبر بود (خونه پر بود یا عدد اشتباه)
    if not moved:
        print("\nInvalid number! try again!")
        continue  # دوباره از کاربر بپرس
    
    # اگه کاربر برنده شد، تبریک بگو و بازی رو تموم کن
    if won:
        print(colored("\nYou Won!\n", "green"))
        break
    
    # حالا نوبت کامپیوتره! اگه کامپیوتر برنده شد، بهش بگو بازنده‌ای! 😈
    elif comuter_move()[1]:
        print(colored("\nYou loser!\n", "yellow"))
        break
    

# ========== پایان بازی: وضعیت نهایی تخته رو نشون بده ==========
print_board()
