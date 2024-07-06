import requests


# URL de votre API
url = 'http://localhost:8000/api/predict-animal/'

# Chemin vers votre image d'empreinte animale
image_path = 'cat.jpg'

# Envoi de la requête POST avec l'image
files = {'image': open(image_path, 'rb')}
response = requests.post(url, files=files)

# Vérification du code de réponse
if response.status_code == 200:
    # Affichage de la réponse JSON
    print(response.text)
else:
    print(f"Erreur lors de la requête : {response.status_code}, {response.text}")
