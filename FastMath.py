from random import randint

def getRandom():
    return randint(0,100)

def getRandomSign():
    return randint(0,1)

def Main():
    sign = ["+", "-"]
    rightAnswers = 0
    wrongAnswers = 0
    answer = 0
    print("\n\nWelcome to Fast Math.")
    print("Here are 20 quick problems to sharpen your math skills.\n")
    for i in range(1,21):
        number1 = getRandom()
        number2 = getRandom()
        randomOperation = getRandomSign()
        print("%d.   %d %s %d = " % (i, number1, sign[randomOperation], number2)),
        try:
            answer = int(raw_input())
            if(randomOperation == 0):
                if(number1 + number2 == answer):
                    print("Well Done! The answer was %d." % answer)
                    rightAnswers += 1
                else:
                    print("Wrong, the answer was %d."% (number1 + number2))
                    wrongAnswers += 1
            else:
                if(number1 - number2 == answer):
                    print("Well Done! The answer was %d." % answer)
                    rightAnswers += 1
                else:
                    print("Wrong, the answer was %d."% (number1 - number2))
                    wrongAnswers += 1
        except:
            print("Invalid Response!")
    print("\nRight answer: %d  wrong answer: %d" % (rightAnswers, wrongAnswers))
    print("Have a good day.")
    
if __name__ == "__main__":
    Main()
