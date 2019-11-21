import random

def rock_sizer_paper():
    rsp_list = ['rock', 'sizer', 'paper']
    
    user_input = input("Please enter your choice(rock, sizer, paper): ").lower()
    if user_input not in rsp_list:
        print('[ERR] Input is incorrect')
        return

    computer_input = random.choice(rsp_list)
 
    user_index = rsp_list.index(user_input)
    computer_index = rsp_list.index(computer_input)
    
    num = user_index - computer_index
    if num < 0: num = num + 3

    result = ''
    if num == 0:
        result = 'DRAW!!'
    elif num == 1:
        result = 'COM WIN!!'
    elif num == 2:
        result = 'USER WIN!!'

    print("USER (%s) <===> (%s) COM" % (user_input, computer_input))
    print(result)

if __name__ == "__main__":
    rock_sizer_paper()
