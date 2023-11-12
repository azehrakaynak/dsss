import random


def randomInteger(min, max):
    """
     Generates Random integer.
    """
    return random.randint(min, max)


def randomSign():

    """
     Generates Random operation.
    """
    return random.choice(['+', '-', '*'])


def problemGenerator(n1, n2, o):
    """
     Generates problem.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        try:
            n1 = randomInteger(1, 10); n2 = randomInteger(1, 5); o = randomSign()

            PROBLEM, ANSWER = problemGenerator(n1, n2, o)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                s += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except Exception as k:
            print('Error : ' + str(k))

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
