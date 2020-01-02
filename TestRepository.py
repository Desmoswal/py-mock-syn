from model import TestModel
import random


class TestRepository:

    def getModelById(self,id):
        return TestModel.TestModel(1, "itsworking", random.random())
