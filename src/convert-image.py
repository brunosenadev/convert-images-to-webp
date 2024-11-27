from os import listdir, path, mkdir
from PIL import Image
from time import sleep

def convert_all_images_in_directory():
    directory = 'C:\\Users\\User\\Documents\\EmpresasImagens'
    directory_webp = 'C:\\Users\\User\\Documents\\EmpresasImagensWebp'
    folders = [folder for folder in listdir(directory) if path.isdir(path.join(directory, folder))]

    if not path.isdir(directory_webp):
        mkdir(directory_webp)

    for folder in folders: 
        c = 0
        if not path.isdir(path.join(directory_webp, folder)):
            mkdir(path.join(directory_webp, folder))

        for img in listdir(path.join(directory, folder)):
            c += 1
            if img.endswith(('.png', '.jpg', '.jpeg')):
                input_path = path.join(directory, folder, img)
                output_path = path.join(directory_webp, folder, f'{folder}-{c}.webp')
                convert_image_to_webp(input_path, output_path)
            
def convert_image_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'WEBP', quality=80)

convert_all_images_in_directory()

print('Todas as imagens foram convertidas com sucesso.')

sleep(3)