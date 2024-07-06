from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Définir les générateurs de données
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

# Générateur de données d'entraînement
train_generator = datagen.flow_from_directory(
    'C:\\Users\\user\\OneDrive\\Documents\\GitHub\\mspr-ia\\projet MSPR\\output',
    target_size=(128, 128),
    batch_size=32,
    class_mode='sparse',
    subset='training')

# Générateur de données de validation
validation_generator = datagen.flow_from_directory(
    'C:\\Users\\user\\OneDrive\\Documents\\GitHub\\mspr-ia\\projet MSPR\\output',
    target_size=(128, 128),
    batch_size=32,
    class_mode='sparse',
    subset='validation')

# Initialiser le modèle
model = Sequential()

# Ajouter des couches convolutionnelles et de pooling
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(12, activation='softmax'))  # 12 classes pour les 12 animaux

# Compiler le modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=10)

# Sauvegarder le modèle
model.save('animal_footprint_classifier.h5')

# Évaluation du modèle
test_loss, test_acc = model.evaluate(validation_generator)
print(f'Test accuracy: {test_acc}')
