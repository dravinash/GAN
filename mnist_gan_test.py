# example of loading the generator model and generating images
from tensorflow.keras.models import load_model
from numpy.random import randn
from matplotlib import pyplot

# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
	# generate points in the latent space
	x_input = randn(latent_dim * n_samples)
	# reshape into a batch of inputs for the network
	x_input = x_input.reshape(n_samples, latent_dim)
	return x_input

# create and save a plot of generated images (reversed grayscale)
def save_plot(examples, n):
	# plot images
	for i in range(n * n):
		# define subplot
		pyplot.subplot(n, n, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(examples[i, :, :, 0], cmap='gray_r')
	# pyplot.show()
	# save plot to file
	filename = 'plots/generated_plot_%03d.png' % (n)
	pyplot.savefig(filename)

# load model
model = load_model('models/generator_model_500.h5')
# generate images
latent_points = generate_latent_points(100, 1) # 1 for single image
print("Latent points:",latent_points.shape)
# generate images
X = model.predict(latent_points)
print(X.shape)
# plot the result
save_plot(X, 1)

