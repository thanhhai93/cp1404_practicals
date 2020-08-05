import random

def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score>=90:
        result = "Excellent"
    elif score >= 50 and score < 90:
        result = "Passable"
    else:
        result = "Bad"

    return result

def main():

    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)

    score = random.randint(1,100)
    print("Random score: {}".format(score))
    result = check_score(score)
    print(result)


if __name__ == '__main__':
    main()