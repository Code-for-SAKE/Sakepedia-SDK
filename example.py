
import sakepedia

JWT = "JWT issued with your own Sakepedia account"
api = sakepedia.SakepediaAPI(JWT)

brewery = api.getBrewery("菊水酒造")
print(brewery)