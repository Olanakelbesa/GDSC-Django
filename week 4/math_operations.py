def basic_operations(a, b):
    arthimetic_dict = {
        "a + b" : a + b,
        "a - b" : a - b,
        "a * b" : a * b,
        "a / b" : a / b
    }
    return arthimetic_dict

def power_operation(base, exponent, **kwargs):
    result = base**exponent

    if 'modulo' in kwargs:
        modulo_value = kwargs['modulo']
        result %= modulo_value

    return result



def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent

        if 'modulo' in kwargs:
            modulo_value = kwargs['modulo']
            if modulo_value == 0:
                raise ValueError("Modulo value cannot be zero.")
            result %= modulo_value

        return result

    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results

    except Exception as e:
        print(f"Error in apply_operations: {e}")
        return None

operations = [
    (power_operation, (2, 3)),
    (power_operation, (2, 3, {'modulo': 0})),
    (power_operation, (2, 'invalid')),
]


