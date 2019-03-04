import ProjectEuler

def main():
    prob_num = input("Which problem from Project Euler would you like to solve? ")
    if prob_num > 25:
        print("Problem has not been solved yet.")
        return -1
    print("Solving problem", prob_num)
    func_name = "prob" + prob_num
    method_to_call = getattr(ProjectEuler, func_name)
    result = method_to_call()
    print(result)
    return 0

if __name__ == '__main__':
    main()
