class Question:

    def __init__(self, id, text, answers):
        self.answer_dict = {}
        self.id = id
        self.text = text
        self.answers = answers

    def ask(self):
        print(self.text)
        answer_no = 1
        for answer in self.answers:
            print(str(answer_no) + ". " + answer)
            self.answer_dict[str(answer_no)] = answer
            answer_no += 1
        
    def get_answer(self):
        selected_answer = input("Enter option: ")
        if not selected_answer in self.answer_dict:
            print(selected_answer + " is not a valid option")
        else:
            print("You selected " + selected_answer + ", which is " + \
              self.answer_dict[selected_answer])
