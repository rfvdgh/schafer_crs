try:
    f = open("31_test_file.txt")
    # var = bad_var
# except FileNotFoundError:
#     print("Sorry this file does not exist")
# except Exception:
#     print("Sorry. Something went wrong")

# if you wanted to print the exception that it threw instead of custom messages
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

# else clause runs code if try block doesn't run exception
else:
    print(f.read())
    f.close()

# finally runs no matter what happens.
# useful when you want to release certain resources like a database.
finally:
    print("Executing Finally...")

# except Exception: # this will catch any and all
# pass

# if wanted to raise your own exception
try:
    f = open("31_corrupt_file.txt")
    if f.name == "31_corrupt_file.txt":
        # raising exception manually... raise,then exception you want to raise
        raise Exception
# and then it goes down to the Exception
except Exception:
    print("Error!")
