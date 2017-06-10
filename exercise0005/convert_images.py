import glob, os
from PIL import Image

def convert_images(input_folder, output_folder, size):
    url = os.path.join(input_folder+"/*.jpg")
    images = glob.glob(str(url))
    for image in images:
        file_name, ext_name = os.path.splitext(image)
        file_name2 = os.path.split(file_name)
        im = Image.open(image)
        im.thumbnail(size)
        if not os.path.isdir(output_folder):
            os.mkdir(output_folder)
        im.save(output_folder+r"/"+file_name2[1]+ext_name)
            
print("Jobs Finished")
if __name__ == '__main__':
    image_size=[100, 300]
#     convert_images(image_size)
    convert_images("input", "output", image_size)