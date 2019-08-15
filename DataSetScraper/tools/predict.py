import os,sys
import time
import numpy as np
import tensorflow as tf
import pickle
import config
import tfutil
import dataset
import misc
import PIL


predict_folder=sys.argv[2]

snap_id=sys.argv[1]

get_id=misc.list_network_pkls(snap_id)
# print(misc.list_network_pkls('001'))
reloaded_pkl=get_id[len(get_id)-2]

print(reloaded_pkl)

tf.InteractiveSession(config=tf.ConfigProto( intra_op_parallelism_threads=1, inter_op_parallelism_threads=1))
with open(reloaded_pkl, 'rb') as file:
	G, D, Gs = pickle.load(file)
	# G = Instantaneous snapshot of the generator, mainly useful for resuming a previous training run.
	# D = Instantaneous snapshot of the discriminator, mainly useful for resuming a previous training run.
	# Gs = Long-term average of the generator, yielding higher-quality results than the instantaneous snapshot.

# Generate latent vectors.
latents = np.random.RandomState(1000).randn(1000, *Gs.input_shapes[0][1:]) # 1001 random latents
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
	if not os.path.exists('output/'+sys.argv[2]):
		os.mkdir('output/'+sys.argv[2],755)
	PIL.Image.fromarray(images[idx], 'RGB').save('output/'+sys.argv[2]+'/img%d.png' % idx)


# Gs.run()