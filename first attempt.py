from PIL import Image
import urllib.request
from io import BytesIO

# function to position images
def position_images(urls):
    # create a new blank image
    #new_image = Image.new('RGB', (1000, 1000), color = (255, 255, 255))
    new_image = Image.new('RGBA', (1000, 1000), color = (255, 255, 255, 0))
    images = []
    # open and resize images
    for url in urls:
        image_bytes = urllib.request.urlopen(url).read()
        image = Image.open(BytesIO(image_bytes))
        image = image.resize((500, 500))
        images.append(image)

    if len(images) == 1:
        # paste the image in the middle of the new image
        new_image.paste(images[0], (250, 250))
    elif len(images) == 2:
        # paste the first image on the left side
        new_image.paste(images[0], (0, 250))
        # paste the second image on the right side
        new_image.paste(images[1], (500, 250))
    elif len(images) == 3:
        # paste the first image on the top
        new_image.paste(images[0], (0, 0))
        # paste the second image on the top right
        new_image.paste(images[1], (500, 0))
        # paste the third image on the bottom
        new_image.paste(images[2], (250, 500))
    elif len(images) == 4:
        # paste the first image on the top left
        new_image.paste(images[0], (0, 0))
        # paste the second image on the top right
        new_image.paste(images[1], (500, 0))
        # paste the third image on the bottom left
        new_image.paste(images[2], (0, 500))
        # paste the fourth image on the bottom right
        new_image.paste(images[3], (500, 500))
    else:
        print("Error: Only 1-4 images can be positioned")
        return

    # save the new image as a png
    new_image.save('new_image.png')
    # save the new image as a jpg
    #new_image.save('new_image.jpg')

# example usage
position_images(['https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x6b175474e89094c44da98b954eedeac495271d0f.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xdac17f958d2ee523a2206206994597c13d831ec7.png'])#,'https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x0000000000085d4780b73119b644ae5ecd22b376.png'])

