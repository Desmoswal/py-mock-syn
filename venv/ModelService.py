import TestRepository

repo = TestRepository.TestRepository()

class ModelService:

    def getModel(id:int):
        return repo.getModelById(1)