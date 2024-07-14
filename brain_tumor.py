import streamlit as st
import os
import pandas as pd
from PIL import Image

def count_images_in_classes(directory):
    classes = os.listdir(directory)
    class_image_counts = {}
    for cls in classes:
        class_path = os.path.join(directory, cls)
        if os.path.isdir(class_path):
            images = os.listdir(class_path)
            class_image_counts[cls] = len(images)
    return class_image_counts

def load_data(training_dir, testing_dir):
    training_counts = count_images_in_classes(training_dir)
    testing_counts = count_images_in_classes(testing_dir)
    
    return training_counts, testing_counts

# Set the directory paths
training_dir = '/content/Training'
testing_dir = '/content/Testing'

# Load the data
training_counts, testing_counts = load_data(training_dir, testing_dir)

# Streamlit app layout
st.title("Brain Tumor MRI Dataset Analysis")

st.header("Training Dataset")
st.write(f'Total Images: {sum(training_counts.values())} images in {len(training_counts)} classes')
for cls, count in training_counts.items():
    st.write(f'Class {cls}: {count} images')

st.header("Testing Dataset")
st.write(f'Total Images: {sum(testing_counts.values())} images in {len(testing_counts)} classes')
for cls, count in testing_counts.items():
    st.write(f'Class {cls}: {count} images')

# Display an example image from each class
st.header("Sample Images")
for cls in training_counts.keys():
    class_path = os.path.join(training_dir, cls)
    images = os.listdir(class_path)
    if images:  # Check if the directory is not empty
        img_path = os.path.join(class_path, images[0])
        image = Image.open(img_path)
        st.image(image, caption=cls)

# Optionally, add more Streamlit components for interactivity or additional analysis
