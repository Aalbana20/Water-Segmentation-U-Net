import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard
from tensorflow.keras.optimizers import Adam
from unet_model import unet_model
from process_dat import load_images_from_folders

# Define your folders and parameters
train_images_dirs = ['C:/your/path/to/data1', 'C:/your/path/to/data2']
img_height, img_width = 128, 128
batch_size = 16
epochs = 10

# Load data
images, masks = load_images_from_folders(train_images_dirs, img_height, img_width)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(images, masks, test_size=0.2, random_state=42)

# Build and compile the model
model = unet_model(input_shape=(img_height, img_width, 3))
model.compile(optimizer=Adam(learning_rate=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

# Define callbacks
checkpoint = ModelCheckpoint('model_checkpoint.keras', save_best_only=True, monitor='val_loss', mode='min')
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
tensorboard = TensorBoard(log_dir='./logs')

# Train the model
history = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,
                   callbacks=[early_stopping, checkpoint, tensorboard])

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test loss: {loss}')
print(f'Test accuracy: {accuracy}')

# Save the model
model.save('water_segmentation_model.keras')
