# Importing the necessary libraries
import gradio as gr
import numpy as np
import pandas as pd
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
import os  # To extract the filename from the path

# Load the pretrained model and processor from Hugging Face
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def caption_images(input_files: list):
    """
    Generates captions for multiple uploaded images using the BLIP model.

    Args:
        input_files (list): A list of file paths for the input images.

    Returns:
        str: A string representation of the DataFrame containing filenames and their generated captions.
        str: The path to the CSV file containing the filenames and captions.
    """
    captions = []
    filenames = []

    for input_file in input_files:
        # Extract just the filename (not the full path)
        filename = os.path.basename(input_file)  # Extracts the file name from the full path
        
        # Open the image file using its path
        raw_image = Image.open(input_file).convert('RGB')

        # Process the image
        inputs = processor(images=raw_image, return_tensors="pt")

        # Generate a caption for the image
        outputs = model.generate(**inputs, max_length=50)

        # Decode the generated tokens to text and store it into `caption`
        caption = processor.decode(outputs[0], skip_special_tokens=True)

        # Append the filename and caption to the list
        filenames.append(filename)  # Store just the filename
        captions.append(caption)

    # Create a pandas DataFrame to store filenames and captions
    df = pd.DataFrame({"Filename": filenames, "Caption": captions})
    
    # Save the captions to a CSV file
    csv_file = "captions.csv"
    df.to_csv(csv_file, index=False)

    return df.to_string(index=False), csv_file


# Create the Gradio interface
iface = gr.Interface(
    fn=caption_images, 
    inputs=gr.Files(label="Upload One or More Images", type="filepath", interactive=True),  # Accept multiple image files (filepath type)
    outputs=[
        gr.Textbox(label="Generated Captions", interactive=True, lines=10, placeholder="Captions will appear here..."),
        gr.File(label="Download Captions as CSV")  # Output captions and CSV file
    ],
    title="Multi-Upload Image Captioning App by Karan Heera",
    description=(
        "This app is a multi-upload image captioning tool powered by the BLIP model from Hugging Face's Transformers. "
        "Simply upload one or more images, and the app will generate a caption for each, showing the image's filename. "
        "You can also download the captions in CSV format."
    ),
)

# Launch the Web App
iface.launch()
