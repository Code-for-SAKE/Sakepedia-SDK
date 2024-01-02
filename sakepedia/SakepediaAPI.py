import urllib.request
from bs4 import BeautifulSoup
import json
from . import SakeData

class SakepediaAPI:
  BASE_URL = "https://sakepedia.code4sake.org/api/"
  HEADERS = {}

  #ヘッダーにJWTを設定
  def __init__(self, jwt):
    self.HEADERS = {
      "Content-Type" : "application/json",
      "authorization": "Bearer " + jwt
    }    

  #酒蔵データ取得
  def getBrewery(self, name):
    try:
      url = self.BASE_URL + "breweries/"
      request = urllib.request.Request(url=url+urllib.parse.quote(name), headers=self.HEADERS, method="GET")
      try:
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, features="lxml")
        return json.loads(soup.text)
      except:
        print("オブジェクトIDが指定されていません")
      url = self.BASE_URL + "list/breweries?keyword="
      request = urllib.request.Request(url=url+urllib.parse.quote(name), headers=self.HEADERS, method="GET")
      response = urllib.request.urlopen(request)
      soup = BeautifulSoup(response, features="lxml")
      response.close()
      if (len(json.loads(soup.text)) > 1):
        print("酒蔵名が複数存在するためオブジェクトID指定が必要です")
        return None
      else:
        return json.loads(soup.text)[0]
    except Exception as e:
      print('getBrewery', e)

  #銘柄データ取得
  def getBrand(self, name):
    try:
      url = self.BASE_URL + "brands/"
      request = urllib.request.Request(url=url+urllib.parse.quote(name), headers=self.HEADERS, method="GET")
      try:
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, features="lxml")
        return json.loads(soup.text)
      except:
        print("オブジェクトIDが指定されていません")
      url = self.BASE_URL + "list/brands?keyword="
      request = urllib.request.Request(url=url+urllib.parse.quote(name), headers=self.HEADERS, method="GET")
      response = urllib.request.urlopen(request)
      soup = BeautifulSoup(response, features="lxml")
      response.close()
      if (len(json.loads(soup.text)) > 1):
        print("銘柄名が複数存在するためオブジェクトID指定が必要です")
        return None
      else:
        return json.loads(soup.text)[0]
    except Exception as e:
      print('getBrand', e)

  #日本酒データ取得
  def getSakeData(self, name):
    url = self.BASE_URL + "list/sakes?keyword="
    try:
      request = urllib.request.Request(url=url+urllib.parse.quote(name), headers=self.HEADERS, method="GET")
      response = urllib.request.urlopen(request)
      soup = BeautifulSoup(response, features="lxml")
      response.close()
      if (len(json.loads(soup.text)) > 0):
        return json.loads(soup.text)[0]
      else:
        return None
    except Exception as e:
      print('getSakeData', e)

  #日本酒データの酒蔵名、銘柄名をIDに変換
  def name2IdSakeData(self, data: SakeData):
    data.brand = self.getBrand(data.brand)
    data.brewery = self.getBrewery(data.brewery)
    return data

  #日本酒データをSakepediaに登録
  def addSakeData(self, data: SakeData):
    data = self.name2IdSakeData(data)
    if (data.brewery==None) or (data.brand==None):
      print("addSakeData ERROR")
      return
    url = self.BASE_URL + "sakes"
    saveData = {
        "name": data.name,
        "kana": data.kana,
        "brand": data.brand, 
        "brewery": data.brewery, 
        "subname": data.subname, 
        "type": None, 
        "mariages": None, 
        "url": data.url, 
        "description": data.description, 
    }
    json_data = json.dumps(saveData, ensure_ascii=False).encode('utf-8')
    try:
      request = urllib.request.Request(url=url, data=json_data, headers=self.HEADERS, method="POST")
      response = urllib.request.urlopen(request)
      soup = BeautifulSoup(response, features="lxml")
      response.close()
      return soup.text
    except Exception as e:
      print("ERROR")
      print(e)
  
  #Sakepediaの日本酒データを更新
  def updateSakeData(self, id, data: SakeData):
    data = self.name2IdSakeData(data)
    if (data.brewery==None) or (data.brand==None):
      print("addSakeData ERROR")
      return
    url = self.BASE_URL + "sakes/" + id
    saveData = {
        "name": data.name,
        "kana": data.kana,
        "brand": data.brand, 
        "brewery": data.brewery, 
        "subname": data.subname, 
        "type": None, 
        "mariages": None, 
        "url": data.url, 
        "description": data.description, 
    }
    json_data = json.dumps(saveData, ensure_ascii=False).encode('utf-8')
    try:
      request = urllib.request.Request(url=url, data=json_data, headers=self.HEADERS, method="PUT")
      response = urllib.request.urlopen(request)
      soup = BeautifulSoup(response, features="lxml")
      response.close()
      return soup.text
    except Exception as e:
      print("ERROR")
      print(e)

  def saveSakeData(self, data: SakeData):
    search = self.getSakeData(data.name)
    if(search == None):
      return self.addSakeData(data)
    else:
      return self.updateSakeData(search["_id"], data)