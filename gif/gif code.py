import imageio
images = []
filenames = ["k1.png","k2.png"]
for filename in filenames:
    images. append(imageio.imread(filename))
imageio.mimsave('animate.gif', images, duration=0.5)