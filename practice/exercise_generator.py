from random import randint

from practice.user_messenger import UserMessenger


class Exercise:
    def __init__(self):
        self.msg = UserMessenger()
        self.context = 'Exercise'
        self.exercise_dict = {
            'Composition': 'Practice using different composition techniques',
            'Contour': 'Draw the contour',
            'Negative Space': 'Draw the negative space.',
            'Shading': 'Practice Shading using different shading techniques',
            'Perspective': 'Practice drawing 2D and 3D objects in perspective rotating them on the canvas',
            'Color': 'Practice choosing color',
        }

    def generate(self):
        keys_lst = list(self.exercise_dict.keys())
        rand_num = randint(0, len(keys_lst)-1)
        rand_key = keys_lst[rand_num]
        tmp_dict = {rand_key: self.exercise_dict[rand_key]}
        self.msg.print_result_dict(tmp_dict, self.context)
