import numpy as np
from PIL import Image

img = np.array(Image.open("rena.png"))
print(type(img))
print(img.shape)

img_90 = np.rot90(img)
rena_90 = Image.fromarray(img_90)
rena_90.save("rena_90.png")

img_ud = np.flipud(img)
rena_ud = Image.fromarray(img_ud)
rena_ud.save("rena_ud.png")

img_lr = np.fliplr(img)
rena_lr = Image.fromarray(img_lr)
rena_lr.save("rena_lr.png")

