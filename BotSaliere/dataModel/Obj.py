
########################################
#   obj est la classe/structure de données 
#   parents des classe user et tweet
########################################
class obj:
    def __init__(self, id, created_at=None):
        self.id = id
        self.created_at = created_at

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

    def getCreated_At(self):
        return self.created_at
    def setCreated_At(self, created_at):
        self.created_at = created_at