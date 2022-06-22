from mycroft import MycroftSkill, intent_handler


class ShoppingList(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.shoppinglist = []

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
        if self.shoppinglist:
            self.speak_dialog('list.shopping.read')
            for thing in self.shoppinglist:
                self.speak(thing)
        else:
            self.speak_dialog('list.shopping.empty.list')

    @intent_handler('list.shopping.remove.intent')
    def handle_list_shopping_remove(self, message):
        thing = message.data.get('thing')
        if thing in self.shoppinglist:
            self.shoppinglist.remove(thing)
            self.speeak_dialog('list.shopping.removed', {'thing': thing})
        else:
            self.speak_dialog('list.shopping.not.in.list', {'thing': thing})




def create_skill():
    return ShoppingList()

