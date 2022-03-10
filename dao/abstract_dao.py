from abc import ABC, abstractmethod
import pickle


class AbstractDAO(ABC):

    @abstractmethod
    def__init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasourc, 'rb'))

    def persist(self, key, object):
        self.__cache[key] = object
        self.__dump()

    def remove(self, key):
        self.__cache.pop(key)
        self.__dump()

    def get_all(self):
        return self.__cache.values()
