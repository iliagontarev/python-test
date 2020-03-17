'''
CHAPTER I
Car class that has the following attributes:
 pax_count -- number of passengers riding in the car (including the driver),
 car_mass -- mass of the empty car (in kg),
 gear_count -- number of gears.
 
It is possible to retrieve the total mass estimate of a car instance, assuming that an average person weight is 70 kg:
The requirements in this case are the following: passanger count cannot be greater than 5, or less than 1, Car mass (excluding the passengers) cannot be greater than 2000 kg.
In case one tries to create a car instance which does not meet these requirements, IllegalCarError is raised.
'''

class IllegalCarError(Exception):
    pass


class Car(object):
    avg_person_mass = 70

    def init(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    # a getter function
    @property
    def total_mass(self):
        return self.car_mass + (self.avg_person_mass * self.pax_count)

    # a getter function
    @property
    def pax_count(self):
        return self.__pax_count


    @pax_count.setter
    def pax_count(self, count):
        if count < 1:
            raise IllegalCarError('Minimum passanger required: 1')
        elif count > 5:
            raise IllegalCarError('Maximum number of passanger is 5!')
        else:
            self.__pax_count = count

    # a getter function
    @property
    def car_mass(self):
        return self.__car_mass

    @car_mass.setter
    def car_mass(self, mass):
        if mass > 2000:
            raise IllegalCarError("Car mass exceeds the maximum legal weight, sould be less than 2000.")
        else:
            self.__car_mass = mass

    # a getter function
    @property
    def gear_count(self):
        return self.__gear_count

    @gear_count.setter
    def gear_count(self, count):
        self.__gear_count = count




c = Car(3, 1600, 5)
