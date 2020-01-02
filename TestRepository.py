from model.TestModel import TestModel
import random


class TestRepository:

    def getModelById(self,id):
        return TestModel(1, "itsworking", random.random())
