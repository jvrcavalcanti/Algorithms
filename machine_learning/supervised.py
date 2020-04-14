from abc import abstractmethod


class Supervised(object):
    @abstractmethod
    def format(self, datas):
        pass