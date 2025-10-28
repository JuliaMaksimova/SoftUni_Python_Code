# class Vehicle:
#     def __init__(self, mileage, max_speed=150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#
# car = Vehicle(20)
#
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append("Hudly Wireless")
# print(car.gadgets)

#####################################

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"
#
# point1 = Point(2, 4)
# print(point1)
# point1.set_x(3)
# point1.set_y(5)
# print(point1)

###################################

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         return Circle.pi*self.radius**2
#
#     def get_circumference(self):
#         return 2*Circle.pi*self.radius
#
# circle1 = Circle(10)
#
# print(f"{circle1.get_area():.2f}")
# print(f"{circle1.get_circumference():.2f}")
#
# circle1.set_radius(12)
#
# print(circle1.get_area())
# print(circle1.get_circumference())


##################################
#
# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if self.content+ml <= Glass.capacity:
#             self.content += ml
#             return f"Glass filled with {self.content} ml"
#         return f"Cannot add {ml} ml"
#
#     def empty(self):
#         self.content = 0
#         return "The glass is now empty"
#
#     def info(self):
#         return f"{Glass.capacity - self.content} ml left."
#
# glass = Glass()
#
# print(glass.fill(100))
#
# print(glass.fill(200))
#
# print(glass.empty())
#
# print(glass.fill(200))
#
# print(glass.info())


##################################


class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = False if self.is_on else True

    def install(self, app, app_memory):
        if self.is_on == True:
            if self.memory >= app_memory:
                self.memory = self.memory - app_memory
                self.apps.append(app)
                return f"App {app} is installed"
            else:
                return "Not enough memory."
        return "Turn on the phone."

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)

print(smartphone.install("Facebook", 60))

smartphone.power()

print(smartphone.install("Facebook", 60))

print(smartphone.install("Messenger", 20))

print(smartphone.install("Instagram", 40))

print(smartphone.status())