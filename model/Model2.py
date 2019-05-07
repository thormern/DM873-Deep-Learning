from keras.models import load_model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')

# Freeze the layers except the last 4 layers
for layer in model.layers[:-4]:
    layer.trainable = False

# Check the trainable status of the individual layers
for layer in model.layers:
    print(layer, layer.trainable)

