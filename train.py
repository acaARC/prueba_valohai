import os
import tensorflow as tf
import numpy as np

# Get the output path from the Valohai machines environment variables
output_path = os.getenv('VH_OUTPUTS_DIR', './outputs/')  # Default to './outputs/' if not found

# Sample data: let's use random data for training instead of loading MNIST
x_train = np.random.rand(100, 28, 28)  # 100 samples of 28x28 images
y_train = np.random.randint(0, 10, 100)  # 100 labels (10 classes)

# Simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model for 5 epochs
model.fit(x_train, y_train, epochs=5)

# Save the trained model to the output path
model_save_path = os.path.join(output_path, 'model.h5')
model.save(model_save_path)

print(f"Model saved to {model_save_path}")
