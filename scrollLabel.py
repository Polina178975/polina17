# Модуль с классом-наследником ScrollView для создания инс(трукции, у которой при необходимости включается полоса прокруткиc
class ScrollLabel(ScrollView):
    def __init__(self, ltext, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text)

# Здесь должен быть твой код