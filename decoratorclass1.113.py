from fractions import Fraction

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)


Fraction.is_integral = lambda self: self.denominator == 1

f = Fraction(2, 3)
print(f.speak("this is stupid"))
print(f.is_integral())


def dec_speak(cls):
    cls.speak = lambda self, message: '{0} says {1}'.format(self.__class__.__name__, message)
    return cls


Fraction = dec_speak(Fraction)
print(f.speak('hello'))
