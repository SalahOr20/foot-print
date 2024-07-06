import os
import csv

root_path = r'C:\Users\oulis\Documents\mspr-ia\projet MSPR\Mammiferes'

csv_folder_path = os.path.join(r'C:\Users\oulis\Documents\mspr-ia\projet MSPR', 'CSVs')
if not os.path.exists(csv_folder_path):
    os.makedirs(csv_folder_path)

for species_folder in os.listdir(root_path):
    species_path = os.path.join(root_path, species_folder)
    
    if os.path.isdir(species_path):
        csv_filename = f'{csv_folder_path}\\{species_folder}_data.csv'
    
        with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Espèce', 'Chemin d\'accès'])
        
            for img_filename in os.listdir(species_path):
                img_path = os.path.join(species_path, img_filename)
                img_id = img_filename.split('.')[0]
                writer.writerow([img_id, species_folder, img_path])
                
            print(f'Fichier CSV créé pour {species_folder}: {csv_filename}')
