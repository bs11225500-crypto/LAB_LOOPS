while True:
    answer = input("What is the product of 7 * 24? ")
    
    if answer.isdigit() and int(answer) == 7 * 24:
        print("You answered this Question correctly")
        break  
    else:
        print("Your Answer is wrong, try again..")