import imageio
images = []
# filenames = ["k1.png","k2.png"]
filenames = ["gif/wave1.jpg","gif/wave3.jpg","gif/wave2.jpg","gif/wave5.jpg","gif/wave6.jpg","gif/wave7.jpg","gif/wave8.jpg"]
for filename in filenames:
    images. append(imageio.imread(filename))
imageio.mimsave('animate.gif', images, duration=0.5)