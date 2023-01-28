from PIL import Image
import urllib.request
from io import BytesIO

# function to position images
def position_images(urls):
    # create a new blank image
    new_image = Image.new('RGBA', (1000, 1000), color = (0, 0, 0, 0))
    images = []
    # open and resize images
    for url in urls:
        image = Image.open(BytesIO(urllib.request.urlopen(url).read()))

        image = image.convert('RGBA').resize((500, 500))
        images.append(image)

    if len(images) == 1:
        # paste the image in the middle of the new image
        images = []
        image = image.convert('RGBA').resize((1000, 1000))
        images.append(image)
        new_image.paste(images[0], (0, 0))
    elif len(images) == 2:
        # bottom right
        new_image.alpha_composite(images[0], (350, 350))
        # bottom left
        new_image.alpha_composite(images[1], (0, 350))
    elif len(images) == 3:
        # bottom right
        new_image.alpha_composite(images[0], (350, 350))
        # bottom left
        new_image.alpha_composite(images[1], (0, 350))
        # top middle
        new_image.alpha_composite(images[2], (175, 0))
    elif len(images) == 4:
        # bottom right
        new_image.alpha_composite(images[0], (350, 350))
        # bottom left
        new_image.alpha_composite(images[1], (0, 350))
        # bottom right
        new_image.alpha_composite(images[2], (350, 0))
        # bottom left
        new_image.alpha_composite(images[3], (0, 0))
    else:
        print("Error: Only 1-4 images can be positioned")
        return

    # save the new image as a png
    new_image.save('new_image.png')
    # save the new image as a jpg
    #new_image.save('new_image.jpg')

#input = ['https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x6b175474e89094c44da98b954eedeac495271d0f.png']
input = ['https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x6b175474e89094c44da98b954eedeac495271d0f.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png']
#input = ['https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x6b175474e89094c44da98b954eedeac495271d0f.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xdac17f958d2ee523a2206206994597c13d831ec7.png']
#input = ['https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0x6b175474e89094c44da98b954eedeac495271d0f.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png','https://cdn.jsdelivr.net/gh/curvefi/curve-assets/images/assets/0xdac17f958d2ee523a2206206994597c13d831ec7.png','https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png']

input.reverse()

# example usage
position_images(input)
