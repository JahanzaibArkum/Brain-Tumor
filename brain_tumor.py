import streamlit as st
import os
from PIL import Image
import kaggle

# Function to download the Kaggle dataset
def download_dataset():
    # Adjust this command to match the Kaggle dataset you want to download
    kaggle.api.dataset_download_files('masoudnickparvar/brain-tumor-mri-dataset', path='./', unzip=True)

def count_images_in_classes(directory):
    class_image_counts = {}
    if os.path.exists(directory):
        for class_name in os.listdir(directory):
            class_path = os.path.join(directory, class_name)
            if os.path.isdir(class_path):
                images = os.listdir(class_path)
                class_image_counts[class_name] = len(images)
    else:
        raise FileNotFoundError(f"Directory '{directory}' not found or empty.")

    return class_image_counts

def load_data(training_dir, testing_dir):
    try:
        print(f"Loading data from Training directory: {training_dir}")
        training_counts = count_images_in_classes(training_dir)
        print(f"Loading data from Testing directory: {testing_dir}")
        testing_counts = count_images_in_classes(testing_dir)
        return training_counts, testing_counts
    except FileNotFoundError:
        return None, None

def show_sample_images(training_dir, testing_dir, training_counts, testing_counts):
    st.header("Sample Images")
    
    if training_counts:
        st.subheader("Training Dataset")
        for cls, count in training_counts.items():
            class_path = os.path.join(training_dir, cls)
            if os.path.exists(class_path) and count > 0:
                images = os.listdir(class_path)
                img_path = os.path.join(class_path, images[0])
                image = Image.open(img_path)
                st.image(image, caption=f"Class: {cls}")

    if testing_counts:
        st.subheader("Testing Dataset")
        for cls, count in testing_counts.items():
            class_path = os.path.join(testing_dir, cls)
            if os.path.exists(class_path) and count > 0:
                images = os.listdir(class_path)
                img_path = os.path.join(class_path, images[0])
                image = Image.open(img_path)
                st.image(image, caption=f"Class: {cls}")

# Download the Kaggle dataset (you can call this manually or integrate it in your app)
download_dataset()

# Set the directory paths after downloading the dataset
base_dir = './'  # Assuming the dataset was downloaded to the current directory
training_dir = os.path.join(base_dir, 'Training')
testing_dir = os.path.join(base_dir, 'Testing')

# Print out the paths for verification
print(f"Base directory: {base_dir}")
print(f"Training directory: {training_dir}")
print(f"Testing directory: {testing_dir}")

# Load the data
training_counts, testing_counts = load_data(training_dir, testing_dir)

# Streamlit app layout
st.title("Brain Tumor MRI Dataset Analysis")

if training_counts is not None and testing_counts is not None:
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

else:
    st.error(f"Directory '{training_dir}' or '{testing_dir}' not found or empty.")
