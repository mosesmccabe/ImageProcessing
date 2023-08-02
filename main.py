from PIL import Image, ImageFilter

img = Image.open('bulbasaur.jpg')

# filter the image
filter_img = img.filter(filter=ImageFilter.BLUR)
filter_img.save(fp='blur.png', format='png')

# convert the image
convert_img = img.convert(mode='L')  # RGB format
convert_img.save(fp='blur2.png', format='png') # save image

# convert_img.show() # show image

# Rotate Image
rotate_img = convert_img.rotate(angle=180)
# rotate_img.show()  # show image

# Resize Image
resize_img = img.resize(size=(300,300))
resize_img.save(fp='resize_img.png', format='png')
#resize_img.show()

# crop image
box = (100, 100, 300, 300)
crop_img = img.crop(box=box)
crop_img.show()