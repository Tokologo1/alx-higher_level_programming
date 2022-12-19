#!usr/bin/python3
defsafe_print_division(a, b):
    retults = 0
    try:
        results = a / b
    except ZeroDivisionError:
        results = None
        finally:
            print("Inside results: {}".format(results));
            return (results)
        return
