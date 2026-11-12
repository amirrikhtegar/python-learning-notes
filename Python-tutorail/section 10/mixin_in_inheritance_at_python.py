# * mixin

# رابطه = not is a

# از کلاس mixin شی ایجاد نیمشود


class AMixin:
    pass


class A:
    pass


class B:
    pass


# ----


class WiFiMixin:
    def wifi(self):
        print("wifi  " * 5)


class KosCher:
    def pa(self):
        print("code")


class Vehicle:
    def move(self):
        pass


class Car(Vehicle, WiFiMixin):
    pass


class AirPlane(Vehicle, WiFiMixin):
    pass


class MotorCycle(Vehicle, KosCher):
    pass


car = Car()

car.wifi()

m = MotorCycle()
# m.wifi() #'MotorCycle' object has no attribute 'wifi'
m.pa()

# car.pa() # 'Car' object has no attribute 'pa'

print("nvim")
