import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Charger le modèle
model = load_model('animal_footprint_classifier.h5')

# Fonction pour prédire la classe d'une nouvelle image
def predict_animal(image_path, model):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return predicted_class

# Spécifiez le chemin de l'image que vous souhaitez prédire
image_path = 'test_images/chien.jpg'
predicted_class = predict_animal(image_path, model)

if predicted_class is not None:
    # Mapper les indices de classes aux noms des animaux
    class_indices = {'bear': 0, 'beaver': 1, 'cat': 2, 'chien': 3, 'coyote': 4,
                     'ecureuil': 5, 'lapin': 6, 'loup': 7, 'raccoon': 8, 'rat': 9}
    class_names = list(class_indices.keys())

    print(f'Predicted animal: {class_names[predicted_class]}')
