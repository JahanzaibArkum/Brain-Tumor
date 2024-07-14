import streamlit as st
import os
from PIL import Image

def count_images_in_classes(directory):
    class_image_counts = {}
    try:
        classes = os.listdir(directory)
        for cls in classes:
            class_path = os.path.join(directory, cls)
            if os.path.isdir(class_path):
                images = os.listdir(class_path)
                class_image_counts[cls] = len(images)
    except FileNotFoundError:
        st.error(f"Directory '{directory}' not found.")
    except PermissionError:
        st.error(f"Permission denied for directory '{directory}'.")
    
    return class_image_counts

def load_data(dataset_dir):
    dataset_counts = count_images_in_classes(dataset_dir)
    return dataset_counts

# Set the directory path for your extracted dataset
dataset_dir = '/path/to/your/extracted/dataset'

# Load the data
dataset_counts = load_data(dataset_dir)

# Streamlit app layout
st.title("Brain Tumor MRI Dataset Analysis")

st.header("Dataset Overview")
st.write(f'Total Images: {sum(dataset_counts.values())} images in {len(dataset_counts)} classes')
for cls, count in dataset_counts.items():
    st.write(f'Class {cls}: {count} images')

# Display an example image from each class
st.header("Sample Images")
for cls in dataset_counts.keys():
    class_path = os.path.join(dataset_dir, cls)
    images = os.listdir(class_path)
    if images:  # Check if the directory is not empty
        img_path = os.path.join(class_path, images[0])
        image = Image.open(img_path)
        st.image(image, caption=cls)


# Optionally, add more Streamlit components for interactivity or additional analysis
