from Question import Question

class DecisionTree:

    def __init__(self):
        self.main_question = Question(1, "What do you want out of life?", \
                                      ("Nothing", "Everything"))
        self.main_question.ask()
        self.main_question.get_answer()
