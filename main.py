import sys
import argparse
import ProjectEuler

MAX_SOLVED = 30 #indicates the amount of problems in ProjectEuler.net I have
                #currently solved

def main():
    head_description = "Solves any problem below number {} in Project Euler\n".format(MAX_SOLVED)
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=head_description)
    parser.add_argument("-n", "--prob-num", metavar='STR', required=True, help='Problem number')
    args = parser.parse_args()

    
    if not args.prob_num.isnumeric():
        sys.exit('Enter a numeric value for problem')
    if int(args.prob_num) > MAX_SOLVED:
        sys.exit('This problem has not yet been solved')
    if int(args.prob_num) <= 0:
        sys.exit('Problem must be a positive number')

    print("Solving problem", args.prob_num)
    func_name = "prob" + args.prob_num
    method_to_call = getattr(ProjectEuler, func_name)
    result = method_to_call()
    print("answer =", result)
    
    return 0

if __name__ == '__main__':
    main()
