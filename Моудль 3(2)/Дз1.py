class Editor:
    def __init__(self, document):
        self.document = document

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии")

    def view_document(self):
        print(f'{self.document}')


class ProEditor(Editor):
    def edit_document(self):
        KEY = 555
        x = int(input("Введите ключ\n"))
        if x == KEY:
            print(f'Оригинальный документ:\n{self.document}')
            self.document = input("Внесите ваши изменения:\n")
            print(f'{self.document}')
        else:
            print('Ключ неправильный')


a1 = Editor('Здраствуйте')
Editor.view_document(a1)
Editor.edit_document(a1)
ProEditor.view_document(a1)
ProEditor.edit_document(a1)

