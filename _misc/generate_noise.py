from PIL import Image
import numpy as np

def generate_noise(dimensions, colors, probabilities ):
    """ Generate noise based on given colors and probabilities """
    width, height = dimensions
    
    img = Image.new('RGB', dimensions)
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            i = np.random.choice(len(colors), p=probabilities )
            pixels[x, y] = colors[i]    
    return img


dimensions = (100, 100)
# # ISR tiles
# colors = [
#     (82, 80, 82),
#     (98, 101, 98),
#     (65, 64, 65),
#     (60, 88, 48),
#     (48, 96, 4),
#     (32, 80, 4),
#     (44, 68, 32),
#     (64, 112, 12),
#     (32, 72, 44),
#     (16, 64, 0),
#     (80, 104, 60),
# ]
# probabilities  = [
#     0.3232421875,
#     0.26953125,
#     0.166015625,
#     0.07421875,
#     0.0556640625,
#     0.0439453125,
#     0.037109375,
#     0.0185546875,
#     0.005859375,
#     0.0048828125,
#     0.0009765625,
# ]

colors = [
    (65, 64, 65),
    (82, 80, 82),
    (115, 117, 115),
    (48, 48, 48),
    (168, 168, 168),
    (98, 101, 98),
    (32, 32, 32),
    (148, 149, 148),
    (131, 133, 131),
    (156, 160, 172),
]

probabilities  = [
    0.20214123432199432,
    0.19065699791478635,
    0.13065264075192182,
    0.13664747440166817,
    0.13316174411004948,
    0.06896766362702686,
    0.019630886060191096,
    0.05340636768230058,
    0.05228595437428029,
    0.012449036755781021,
]


image = generate_noise(dimensions, colors, probabilities)
image.show()
