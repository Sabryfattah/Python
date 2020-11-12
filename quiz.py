class Quiz():
    def __init__(self, score = 0):
        "initialize the score value"
        self.score = score

    def Read_mcqas(self):
        "read the json file containing MCQs and answers in key:value pairs and return a dictionary"
        import json
        global mcas
        with open("MCQs.json", 'r') as f:
            mcas = json.load(f)
            return mcas
    def Display_MCQs(self):
        "Display each MCQ and get answer, compare to value and add to score"
        mcqs = self.Read_mcqas()
        for mcq in mcqs:
            print(mcq)
            ans = input("Select number of correct answer: ")
            if ans == mcqs[mcq]:
                self.score += 1
        self.Result()
    def Result(self):
        "display result and advice"
        print("Here is the total score ...:", self.score)
        print("This is a percentage of ...", (self.score/len(mcas))*100, "%")

m = Quiz() 
print(m.Display_MCQs())

