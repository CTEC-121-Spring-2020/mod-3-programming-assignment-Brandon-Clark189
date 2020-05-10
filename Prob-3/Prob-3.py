# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Brandon Norton

def letterGrade(score):
    

    if score == 0:
        print("You got a F!")
    elif score == 1:
        print("You got a F!")
    elif score == 2:
        print("You got a D!")
    elif score == 3:
        print("You got a C!")
    elif score == 4:
        print("you got a B!")
    elif score == 5:
        print("you got an A!")

    return letterGrade

def unitTest():
    # testing
    print("your score was 0", letterGrade(0))
    print()
    print("your score was 1", letterGrade(1))
    print()
    print("your score was 2", letterGrade(2))
    print()
    print("your score was 3", letterGrade(3))
    print()
    print("your score was 4", letterGrade(4))
    print()
    print("your score was 5", letterGrade(5))
    print()

if __name__ == "__main__":
    unitTest()