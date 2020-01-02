class TestModel:
    id = 0
    content =""
    randomNumber = 0.0

    def __init__(self, id, content, randomNumber):
        self.id = id
        self.content = content
        self.randomNumber = randomNumber

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

    def getRandomNumber(self):
        return self.randomNumber

    def setRandomNumber(self, randomNumber):
        self.randomNumber = randomNumber
