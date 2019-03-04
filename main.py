import ProjectEuler
MAX_SOLVED = 25 #indicates the amount of problems in ProjectEuler.net I have
                #currently solved


def validate_string(str_num):
    if not (str_num.isdigit()):
        print("Re-enter a valid numerical input.")
        return True
    if int(str_num) > MAX_SOLVED:
        print("Problem has not been solved yet.")
        return True
    if int(str_num) <= 0:
        print("Enter an integer value greater than 0.")
        return True
    return False
        

def main():
    while True:
        prob_num = input("Which problem from Project Euler would you like to solve?\n")
        #validation loop
        while(validate_string(prob_num)):
            prob_num = input();
        
        print("Solving problem", prob_num)
        func_name = "prob" + prob_num
        method_to_call = getattr(ProjectEuler, func_name)
        result = method_to_call()
        print(result, "\n")
        resolve = input("Enter 'r' to solve another problem, or any other key to quit\n")
        if resolve != "r":
            break;
        
    return 0

if __name__ == '__main__':
    main()
