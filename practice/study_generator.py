from random import randint

from practice.user_messenger import UserMessenger


class Study:
    def __init__(self):
        self.context = 'Study'
        self.msg = UserMessenger()
        self.study = {
            'Still Life': 'Study from still life',
            'Human Figure': 'Study the Human Figure',
            'Human Anatomy': 'Study human anatomy',
            'Dog Anatomy': 'Study dog anatomy',
            'Cat Anatomy': 'Study cat anatomy',
            'Fashion': 'Study Fashion',
            'Fabrics': 'Study fabrics',
            'Glass': 'Study the effects of glass',
            'Clothing': 'Study fabric on the human or animal figures',
        }

        self.anatomy_features = [
            'Hair',
            'Eyes',
            'Nose',
            'Ears',
            'Mouth',
            'Face',
            'Arm',
            'Leg',
            'torso',
            'Shoulders',
            'Pecks',
            'Stomach',
            'Pelvis',
            'Back',
            'Neck',
            'Hands',
            'Feet'
        ]

        self.emotion = [
            'Laughing',
            'Crying',
            'Hope',
            'Fear',
            'Joy'
        ]

    def generate(self):
        keys_lst = list(self.study.keys())
        rand_num = randint(0, len(keys_lst)-1)
        rand_key = keys_lst[rand_num]

        tmp_dict = {rand_key: self.study[rand_key]}
        self.msg.print_result_dict(tmp_dict, self.context)
        rand_key = keys_lst[rand_num]
        lst = []
        if 'anatomy' in rand_key.lower():
            for i in range(0, 4):
                rand_anatomy_feature = randint(0, len(self.anatomy_features) -1)
                lst.append(self.anatomy_features[rand_anatomy_feature])

            self.msg.print_result(lst, 'Anatomy Features')
