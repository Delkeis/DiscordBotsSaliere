import json
# import de configMod pour récupérer le chmin des fichiers de config 
from GameApp.gameApp.PyInclude import *

class ErrorController:
    def __init__(self, errorCode: int):
        self.errorCode = errorCode
        self.path = ".\\GameApp\\gameApp\\controllers\\errorsController\\errorCode.json"
        with open(self.path, 'r') as f:
            self.codeDd = json.load(f)
        self.callErrorCode(errorCode)

    def callErrorCode(self, errorCode: int):
        
        for i in self.codeDd.get('Error_Code'):
            if i['code'] == errorCode:
                print("Code erreur "+errorCode+" : "+i['message'])