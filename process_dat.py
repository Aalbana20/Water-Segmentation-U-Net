import os
import numpy as np
from PIL import Image

def process_dat_file(dat_file_path, output_folder, width=3300, height=19105, num_channels=3):
    print(f"Processing: {dat_file_path}")
    header_size = 33000 * 3  # Assuming 3 header records of 33000 bytes each
    expected_data_length = width * height * num_channels
    with open(dat_file_path, 'rb') as dat_file:
        header = dat_file.read(header_size)  # Skip the header records
        print(f"Header of {dat_file_path}: {header[:100]}...")  # Print only the first 100 bytes for brevity
        data = dat_file.read()  # Read the rest of the file
        if len(data) == expected_data_length:
            print(f"Matched dimensions: {width}x{height}x{num_channels}")
            # Convert the data to a numpy array and reshape
            image_data = np.frombuffer(data, dtype=np.uint8).reshape((height, width, num_channels))
            # Save the full image
            image = Image.fromarray(image_data)
            image_name = os.path.basename(dat_file_path).replace('.dat', '_image.png')
            image.save(os.path.join(output_folder, image_name))
            # Save each channel separately
            for i in range(num_channels):
                channel_data = image_data[:, :, i]
                channel_image = Image.fromarray(channel_data)
                channel_name = os.path.basename(dat_file_path).replace('.dat', f'_channel_{i}.png')
                channel_image.save(os.path.join(output_folder, channel_name))
        else:
            print(f"Unexpected data length for {dat_file_path}: {len(data)}")

def process_dat_files(folder_path):
    output_folder = os.path.join(folder_path, 'output')
    os.makedirs(output_folder, exist_ok=True)
    for dat_file_name in os.listdir(folder_path):
        if dat_file_name.endswith('.dat'):
            dat_file_path = os.path.join(folder_path, dat_file_name)
            process_dat_file(dat_file_path, output_folder)

# Folder containing the .dat files
folder_path = r"your\path\to\dat\files"
process_dat_files(folder_path)
