from abc import abstractmethod


class UITemplate(object):
    @abstractmethod
    def show(self):
        pass
    
    
    @abstractmethod
    def process_input(self):
        pass