questions= [
    {
        "Prompt": "what is the captial of france?",
        "options":["A: paris","B. London", "c. berlin" ,"D. mardis"],
        "answer":"A"
    },

    {
       "Prompt" : "which language is primarily spoken in brazil ?",
       "options":["A. spanish","B. portuguese", "C. English" ,"D. Franch"],
       "answer":"B"
    },

    {   "Prompt" : "what is smallest prime number",
        "options":["A: 1","B. 2", "c. 3" "D.4"],
        "answer":"B"

   },

    {
        "Prompt" : "who wrote to kill a Hockingbird ?",
        "options":["A: paris","B. London", "c. berlin" "D. mardis"],
        "answer":"A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["Prompt"])
        for option in question["options"]:
            print(option)
        answer = input("enter your answer(A,B,C,or D):")
        if answer == question["answer"]:
            print("correct,hoory!\n")
            score +=1

        else:
            print("Wrong, Losser!!!! The correct was",question["answer"],"/n")

    print(f"you got{score} out of{len(question)} questions correct.")

run_quiz(questions)
