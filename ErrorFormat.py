try:
    a = int(input("enter a= \n"))
    b = int(input("enter b = \n"))
    print(a / b)
except IndentationError as e:
    print("IndentationError", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
except ValueError as e:
    print("invalid input", e)
except SyntaxError as e:
    print(e)
except SyntaxWarning as e:
    print(e)
except OSError as e:
    print(e)
except BaseException as e:
    print(e)
except Exception as e:
    print("Error", e)
finally:
    print("completed")

print("Finished")