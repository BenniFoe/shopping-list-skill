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

    @intent_handler('add.thing.intent')
    def handle_add_thing(self, message):
        thing = message.data.get('thing')
        if thing is not None:
            self.speak_dialog('add.thing', {'thing': thing})
            self.shoppinglist.append(thing)
        else:
            self.speak_dialog('do.not.understand')

    @intent_handler('read.shoppinglist.intent')
    def handle_read_shoppinglist(self):
        if self.shoppinglist:
            self.speak_dialog('read.shoppinglist')
            for thing in self.shoppinglist:
                self.speak(thing)
        else:
            self.speak_dialog('shoppinglist.is.empty')

    @intent_handler('remove.thing.intent')
    def handle_remove_thing(self, message):
        thing = message.data.get('thing')
        if thing in self.shoppinglist:
            self.shoppinglist.remove(thing)
            self.speeak_dialog('remove.thing', {'thing': thing})
        else:
            self.speak_dialog('not.in.shoppinglist', {'thing': thing})

    @intent_handler('clear.shoppinglist.intent')
    def handle_clear_shoppinglist(self):
        clear = self.ask_yesno('should.clear.shoppinglist')
        if clear == 'yes':
            self.speak_dialog('cleared.shoppinglist')
        elif clear == 'no':
            self.speak_dialog('shoppinglist.consists')

        else:
            self.speak_dialog('do.not.understand')


    @intent_handler('add.things.intent')
    def handle_add_things(self):
        stillask = True
        answer = self.get_response('what.should.add')
        if answer in ['stop', 'exit', 'back', 'get back']:
            stillask = False
        else:
            self.shoppinglist.append(answer)
            self.speak_dialog('add.thing', {'thing': answer})

        while stillask:
            answer = self.get_response('add.thing', {'thing': answer})
            if answer in ['stop', 'exit', 'back', 'get back']:
                stillask = False
            else:
                self.shoppinglist.append(answer)



def create_skill():
    return ShoppingList()
