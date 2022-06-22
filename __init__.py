from mycroft import MycroftSkill, intent_handler


class ShoppingList(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.shoppinglist = ['bread', 'milk']

    def initialize(self):
        pass

    '''
    @intent_file_handler('list.shopping.intent')
    def handle_list_shopping(self, message):
        self.speak_dialog('list.shopping')
    '''


    @intent_handler('list.shopping.add.intent')
    def handle_list_shopping_add(self, message):
        thing = message.data.get('thing')
        if thing is not None:
            self.speak_dialog('list.shopping.add', {'thing': thing})
            self.shoppinglist.append(thing)
        else:
            self.speak_dialog('list.shopping.not.understand')

    @intent_handler('list.shopping.read.intent')
    def handle_list_shopping_read(self):
        if not self.shoppinglist:
            self.speak_dialog('list.shopping.read')
        else:
            self.speak_dialog('list.shopping.empty.list')
            self.speak('list contains ' + str(len(self.shoppinglist)) + 'elements')




def create_skill():
    return ShoppingList()

