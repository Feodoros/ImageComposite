from PIL import Image
import random
import os


# Make random size of our png image
def resizer(arrow_path, img_path):
    arrow = Image.open(arrow_path)
    img = Image.open(img_path)
    r = random.uniform(0.1, 0.5)
    width_img, height_img = img.size
    if (int(width_img * r) < width_img) and (int(height_img * r) < height_img):
        new_size = (int(width_img * r), int(height_img * r))
        return arrow.resize(new_size)
    else:
        resizer(arrow_path, img_path)


# Make random angle, random location of our png and
# impose onto our jpg image
def image_maker(arrow_path, img_path):
    img = Image.open(img_path)
    resized_arrow = resizer(arrow_path, img_path)
    width_img, height_img = img.size

    rangle = random.randint(0, 360)
    new_arrow = resized_arrow.rotate(rangle, expand=True)
    width_new_arrow, height_new_arrow = new_arrow.size
    rx = random.randint(0, height_img - height_new_arrow)
    ry = random.randint(0, width_img - width_new_arrow)

    area = (ry, rx)
    img.paste(new_arrow, area, new_arrow)
    try:
        img.paste(new_arrow, area, new_arrow)
    except Exception:
        print("Not Today: ", arrow_path, img_path)

    return img


def main():

    #                 Path of directory with jpg images
    path_to_images = "C:\\Users\\fzhil\\Desktop\\dataSet_Good\\image_data1\\forest"

    #                 Path of directory with png images
    path_to_arrows = "C:\\Users\\fzhil\\Desktop\\Arrows"

    image_names = os.listdir(path_to_images)
    arrow_names = os.listdir(path_to_arrows)

    i = 0
    counter = 0

    for image_name in image_names:
        full_path_to_img = path_to_images + "\\" + image_name
        full_path_to_arrow = path_to_arrows + "\\" + arrow_names[i]

        if i < len(arrow_names) - 1:
            i += 1
        else:
            i = 0

        img = image_maker(full_path_to_arrow, full_path_to_img)

        #        Path to save
        img.save("C:\\Users\\fzhil\\Desktop\\with_handmade_arrows\\zakl_forest1_" + str(counter) + ".jpg")
        counter += 1


if __name__ == "__main__":
    main()