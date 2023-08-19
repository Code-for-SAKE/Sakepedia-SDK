import json

class SakeData:
    name:str = None
    kana:str = None
    brand:str = None
    brewery:str = None
    subname:str = None
    mariages:list = []
    sake_type:list = []
    description:str = None
    url:str = None

    def __str__(self):
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)
