def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > len(range(1, 3)):
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except:
            result = b + a
            break
        return result
