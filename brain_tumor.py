import streamlit as st
import os
import pandas as pd
from PIL import Image

def count_images_in_classes(directory):
    class_image_counts = {}
    if os.path.exists(directory):
        for class_name in os.listdir(directory):
            class_path = os.path.join(directory, class_name)
            if os.path.isdir(class_path):
                images = os.listdir(class_path)
                class_image_counts[class_name] = len(images)
    else:
        raise FileNotFoundError(f"Directory '{directory}' not found.")

    return class_image_counts


def load_data(training_dir, testing_dir):
    training_counts = count_images_in_classes(training_dir)
    testing_counts = count_images_in_classes(testing_dir)
    return training_counts, testing_counts


def show_sample_images(training_dir, testing_dir, training_counts, testing_counts):
    st.header("Sample Images")
    
    st.subheader("Training Dataset")
    for cls, count in training_counts.items():
        class_path = os.path.join(training_dir, cls)
        if os.path.exists(class_path) and count > 0:
            images = os.listdir(class_path)
            img_path = os.path.join(class_path, images[0])
            image = Image.open(img_path)
            st.image(image, caption=f"Class: {cls}")

    st.subheader("Testing Dataset")
    for cls, count in testing_counts.items():
        class_path = os.path.join(testing_dir, cls)
        if os.path.exists(class_path) and count > 0:
            images = os.listdir(class_path)
            img_path = os.path.join(class_path, images[0])
            image = Image.open(img_path)
            st.image(image, caption=f"Class: {cls}")


# Set the directory paths
training_dir = '/content/Training'
testing_dir = '/content/Testing'

# Load the data
try:
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

    # Display sample images
    show_sample_images(training_dir, testing_dir, training_counts, testing_counts)

except FileNotFoundError as e:
    st.error(str(e))
