import pickle,os,sys
import numpy as np
import PIL.Image
# print(sys.argv)
options={'cat':'karras2018iclr-lsun-cat-256x256.pkl',
			'cow':'karras2018iclr-lsun-cow-256x256.pkl',
			'airplane':'karras2018iclr-lsun-airplane-256x256.pkl',
			'bird':'karras2018iclr-lsun-bird-256x256.pkl',
			'sofa':'karras2018iclr-lsun-sofa-256x256.pkl',
			'pottedplant':'karras2018iclr-lsun-pottedplant-256x256.pkl',
			'train':'karras2018iclr-lsun-train-256x256.pkl',
			'sheep':'karras2018iclr-lsun-sheep-256x256.pkl',
			'bottle':'karras2018iclr-lsun-bottle-256x256.pkl'
		}

def show_categories():
	for k,v in options.items():
		print(k)

if sys.argv[1] == 'help':
	os.system('clear')
	print("Usage : python import_example.py <category> <csv of latents>")
	print("Single category : import_example.py cow 1,2,3,4")
	print("Example to do all categories : for i in `p import_example.py categories`; do echo $i;p import_example.py $i 1,2,3,4; done")
	print("Latents list can have items from 1 to 500")
	print("Available categories :")
	show_categories()
	sys.exit()

if sys.argv[1] == 'categories':
	show_categories()
	sys.exit()

strofnrs=sys.argv[2]
latents_list= [int(x) for x in strofnrs.split(',')]
print('Chosen latents of 1000')
print(latents_list)

# set default pkl
CAT='cat'
PKL='karras2018iclr-lsun-cat-256x256.pkl'
# change it if chosen exists in dict
if sys.argv[1] in options.keys():
	
	CAT== sys.argv[1]
	PKL=options[sys.argv[1]]

# Output chosen category pkl file
print(CAT)
print(PKL)


# Initialize TensorFlow session.
import tensorflow as tf
tf.InteractiveSession()
# Import pretrained pkl network.
with open(PKL, 'rb') as file:
    G, D, Gs = pickle.load(file)

# Generate latent vectors.
latents = np.random.RandomState(100).randn(100, *Gs.input_shapes[0][1:]) # 100 random latents
latents = latents[[477, 56, 83, 887, 583, 391, 86, 340, 341, 415]] # hand-picked top-10
# latents = latents[[477, 56, 83, 887]] # hand-picked top-10
# latents = latents[latents_list] # input from cmd line second argument

# Generate dummy labels (not used by the official networks).
labels = np.zeros([latents.shape[0]] + Gs.input_shapes[1][1:])

# Run the generator to produce a set of images.
images = Gs.run(latents, labels)

# Convert images to PIL-compatible format.
images = np.clip(np.rint((images + 1.0) / 2.0 * 255.0), 0.0, 255.0).astype(np.uint8) # [-1,1] => [0,255]
images = images.transpose(0, 2, 3, 1) # NCHW => NHWC

# Save images as PNG.
for idx in range(images.shape[0]):
	if not os.path.exists('output/'+sys.argv[1]):
		os.mkdir('output/'+sys.argv[1],755)
	PIL.Image.fromarray(images[idx], 'RGB').save('output/'+sys.argv[1]+'/img%d.png' % idx)




# with open('karras2018iclr-lsun-cat-256x256.pkl', 'rb') as file:
# with open('karras2018iclr-lsun-cow-256x256.pkl', 'rb') as file:
# with open('karras2018iclr-lsun-bird-256x256.pkl', 'rb') as file:
# with open('karras2018iclr-lsun-airplane-256x256.pkl', 'rb') as file:
