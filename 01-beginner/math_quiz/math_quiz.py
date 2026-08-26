import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10
correct_answers = 0
incorrect_answers = 0

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{str(left)} {str(operator)} {right}"
    answer = eval(expr)
    return expr, answer

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem # {str(i + 1)} ------> {expr} = ")
        if guess == str(answer):
            correct_answers += 1
            break
        elif guess == "no":
            print(f"Correct answers: {correct_answers} incorrect answers: {incorrect_answers}")
            exit()
        elif guess != str(answer):
            incorrect_answers += 1


end_time = time.time()
total_time = end_time - start_time
print(f"nice work you finished in {round(total_time, 2)} seconds")

print(f"Correct answers: {correct_answers} incorrect answers: {incorrect_answers}")
