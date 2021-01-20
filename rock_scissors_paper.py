import random


def rock_scissors_paper():
    rsp_list = ['rock', 'scissors', 'paper']

    user_input = input(
        "Please enter your choice(rock, scissors, paper): ").lower()
    if user_input not in rsp_list:
        print('[ERR] Input is incorrect')
        return

    computer_input = random.choice(rsp_list)

    print("USER (%s) <===> (%s) COM" % (user_input, computer_input))
    if user_input == computer_input:
        print("DRAW!")
    elif (user_input == "rock" and computer_input == "scissors") \
            or (user_input == "scissors" and computer_input == "paper") \
            or (user_input == "paper" and computer_input == "rock"):
        print("USER WIN!")
    else:
        print("Com WIN!")


if __name__ == "__main__":
    rock_scissors_paper()
