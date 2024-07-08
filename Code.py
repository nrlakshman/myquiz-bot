class QuizHandler:
    def __init__(self, quiz):
        self.quiz = quiz

    def record_current_answer(self, user_response):
        current_question = self.quiz.current_question
        if current_question is None:
            return
        
        # Validate the answer
        if current_question.is_valid_answer(user_response):
            self.quiz.record_answer(user_response)
            return True
        else:
            self.quiz.record_answer(None)
            return False

    def get_next_question(self):
        next_question = self.quiz.get_next_question()
        if next_question is None:
            return self.generate_final_response()
        
        return next_question.text

    def generate_final_response(self):
        score = self.quiz.calculate_score()
        total_questions = len(self.quiz.questions)  # Assuming self.quiz.questions is a list of questions
        response = f"Quiz completed! You scored {score} out of {total_questions}."
        
        return response
