class MyClass:
    X = 5
    Y = 10

object1 = MyClass()
object1.X = 50
object1.Y = 15

object2 = MyClass()
object2.X = 64
object2.Y = 25

print(object1.X)
print(object1.Y)
print(object2.X)
print(object2.Y)


class Chair:
    def __init__(self, ChairType, NumOfLegs, Color, Height):
        self.cType = ChairType
        self.nLegs = NumOfLegs
        self.color = Color
        self.height = Height

    def __str__(self):
        return "A/An " +  self.color +" "+ self.cType +" chair with " + str(self.nLegs) + " legs."

    def paint_chair(self, NewColor):
        self.color = NewColor
        print("The chair has been painted", NewColor)

    def reshape_chair(self, NewNoOfLegs, NewHeight):
        self.nLegs = NewNoOfLegs
        self.height = NewHeight
        print("The chair is now", NewHeight,"inches tall, and it has", NewNoOfLegs, "leg/s.")

chair1 = Chair("Standard", 4, "Brown", 40)
chair2 = Chair("Dining", 3, "Black", 45)
chair3 = Chair("Bar", 1, "White", 50)

print()
print(chair1)
print(chair2)
print(chair3)

print(chair1.height)
print(chair2.height)
print(chair3.height)


class Document:
    def __init__(self, Ext, Name, Size, Length, Encripted):
        self.docExt = Ext
        self.docName = Name
        self.docSize = Size
        self.docLength = Length
        self.docEnc = Encripted

    def __str__(self):
        return (self.docExt +" Document: " + self.docName)

    def printDoc(self):
        print("Document was sent to the printer. Document: ", self.docName,".", self.docExt, sep = "")

    def emailDoc(self):
        toEmail = input("Email of the Recipient: ")
        print("Document was emailed to: ", toEmail, ". Document: ", self.docName,".", self.docExt, sep = "")



doc1 = Document('pdf', 'Resume', 385, 2, False)
doc2 = Document('word', 'CoverLetter', 253, 1, True)

print()
print(chair1)
print(chair2)
print(chair3)

print()
print(doc1)
print(doc2)

print()
print(chair1)
print(chair2)
print(chair3)
print()

chair1.reshape_chair(3, 36)
print(chair1)

chair1.paint_chair("Black")
print(chair1)

print()
print(chair2)
print(chair3)

doc1.printDoc()
doc2.emailDoc()


print()
print(type(doc1))
print(isinstance(doc1, Document))



class Vehicle:
    def __init__(self, reg_no, odometer, top_speed):
        self.reg_no = reg_no
        self.odometer = odometer
        self.top_speed = top_speed

    def drive(self, distance):
        self.odometer += distance
        print(f"The vehicle's current odometer: {self.odometer}")


class Bicycle(Vehicle):
    def __init__(self, reg_no, odometer, top_speed, dist_per_paddle):
        Vehicle.__init__(self, reg_no, odometer, top_speed)
        self.dist_per_paddle = dist_per_paddle
                
    def paddle(self, distance):
        print(f"BICYCLE {self.reg_no} - Average paddle rotations for the ride: {distance / self.dist_per_paddle}")
        super().drive(distance)

class Car(Vehicle):
    def __init__(self, reg_no, odometer, top_speed, trans_system, km_per_fuel_unit):
        Vehicle.__init__(self, reg_no, odometer, top_speed)
        self.trans_system = trans_system
        self.km_per_fuel_unit = km_per_fuel_unit

    def drive(self, distance):
        print(f"CAR {self.reg_no} - Fuel used for the drive: {distance / self.km_per_fuel_unit}")
        super().drive(distance)

print()
v1 = Vehicle("V11", 0, 10)
v1.drive(20)

print()
c1 = Car("C11", 100, 180, "auto",10)
c1.drive(100)

print()
b1 = Bicycle("B11",10,30,1)
b1.paddle(10)

