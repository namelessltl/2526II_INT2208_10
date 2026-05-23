class triAngle:
    is_Valid_Input = True
    def __init__ (self, a = 0, b = 0, c = 0):
        if self._is_valid(a ,b, c):
            self.a = a
            self.b = b
            self.c = c
            self.is_Valid_Input = True
        else:
            self.is_Valid_Input = False
    def _is_valid(self, a, b, c):
        is_int = isinstance(a, int) and isinstance(b, int) and isinstance(c, int)
        if not is_int:
            return False
        in_range = (1 <= a <= 100) and (1 <= b <= 100) and (1 <= c <= 100)
        return in_range

def triAngle_check(t : triAngle):
    if not t.is_Valid_Input:
        return "Invalid Input"
    elif (t.a + t.b <= t.c) or (t.a + t.c <= t.b) or (t.b + t.c <= t.a):
        return "Not a Triangle"
    elif t.a == t.b == t.c:
        return "Equilateral"    
    elif t.a == t.b or t.a == t.c or t.b == t.c:
        return "Isosceles"
    else:
        return "Scalene"