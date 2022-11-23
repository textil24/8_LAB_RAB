class Zhukov():

    def __init__(self):

        self.__description = {
            'name': 'Nick',
            'surname': 'Zhukov',
            'repllink': '@zhukov'
        }

    def __str__(self):
        return f""" {str(self.__description.get('name'))}
                    {str(self.__description.get('surname'))}
                    {str(self.__description.get('repllink'))}
                """

    @property
    def full_name(self):
        return f'{self.__description.get("name")} {self.__description.get("surname")} '
