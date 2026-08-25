ques = [
    'What is the capital city of France?',
    'How many days are there in a week?',
    'Which planet is known as the Red Planet?',
    'What is 5 + 3?',
    "Which animal is commonly known as man's best friend?"
    ]

opts = [
    ['A. Madrid', 'B. Berlin', 'C. Paris', 'D. Rome'],
    ['A. Five', 'B. Eight', 'C. Seven', 'D. Six'],
    ['A. Saturn', 'B. Jupiter', 'C. Mars', 'D. Venus'],
    ['A. 7', 'B. 6', 'C. 8', 'D. 9'],
    ['A. Rabbit', 'B. Horse', 'C. Dog', 'D. Cat']
    ]

ans = ['c', 'c', 'c', 'c', 'c']
correct = 0

for i, que in enumerate(ques):
    print("Question" , (i+1) , ":", que)
    for opt in opts[i]:
        print(opt)
    get_ans = input("Enter your answer: ").lower()
    if get_ans == ans[i]:
        print("Correct!!")
        correct += 1
    else:
        print("False")

print("Your final Score is: ", correct, "/ 5")