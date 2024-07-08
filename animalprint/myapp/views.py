import os
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Charger le modèle
model_path = r'C:\Users\Salah\Desktop\DevIA\animalprint\projet MSPR\animal_footprint_model2.h5'
model = load_model(model_path)


@csrf_exempt
def predict_animal(request):
    if request.method == 'POST' and request.FILES['image']:
        # Récupérer l'image à partir de la requête POST
        image_file = request.FILES['image']

        # Sauvegarder l'image temporairement (optionnel)
        image_path = 'temp_image.jpg'  # Chemin temporaire pour sauvegarder l'image
        with open(image_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        # Prédire la classe de l'animal
        predicted_class = predict_animal_from_path(image_path, model)



        if predicted_class is not None:
            # Mapper les indices de classes aux noms des animaux
            class_indices = {'bear': 0, 'beaver': 1, 'cat': 2, 'chien': 3, 'coyote': 4,
                             'ecureuil': 5, 'lapin': 6, 'loup': 7, 'raccoon': 8, 'rat': 9}
            class_names = list(class_indices.keys())

            predicted_animal = class_names[predicted_class]
            return JsonResponse({'predicted_animal': predicted_animal})
        else:
            return JsonResponse({'error': 'Failed to predict animal'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def predict_animal_from_path(image_path, model):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None
    img = image.load_img(image_path, target_size=(224, 224))  # Redimensionner à (224, 224)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return predicted_class
