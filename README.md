# Auto Image Captions via Upload-GenAI App : <br> (Using Hugging Face's BLIP Transformers and Gradio)

## Description

This Generative AI app generates captions for multiple uploaded images using the **BLIP** model from Hugging Face's **Transformers** library. Users can upload one or more images, and the app will process them to generate captions. The app also provides the option to download the captions along with the filenames in a CSV format for further analysis or reporting.

### Key Features:
- **Image Captioning**: Automatically generates captions for uploaded images using the BLIP model.
- **Multiple Image Upload**: Allows users to upload and process multiple images at once.
- **CSV Export**: The generated captions and filenames can be downloaded in CSV format.
- **Interactive Interface**: Built using Gradio for easy interaction.

## Demo

You can try the app by uploading your images, and the app will generate captions for each image, showing the filenames alongside the captions. You can also download the generated captions in CSV format.

## Technologies Used

- **Gradio**: For building the interactive web interface.
- **Hugging Face Transformers**: For using the BLIP model to generate captions.
- **Pandas**: For organizing and saving the captions data in CSV format.
- **Pillow**: For image opening and processing.
- **Python**: The primary programming language used to build the app.

## Installation

### Prerequisites

To run this project locally, you need to have Python installed. You also need to install the required Python packages listed in `requirements.txt`.

1. Clone the repository:
   ```bash
   git clone https://github.com/karanheera/Auto-Image-Captions-via-Upload-GenAI-App.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Auto-Image-Captions-via-Upload-GenAI-App
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
python app.py
```
The app will start running on your local server, usually at [http://127.0.0.1:7860](http://127.0.0.1:7860/).

## File Structure

```plaintext
/multi-upload-image-captioning-app-using-blip-gradio
│
├── app.py              # The main app file
├── CODE_OF_CONDUCT.md  # Code of conduct file
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # MIT License file
├── README.md           # This file
├── requirements.txt    # List of required Python libraries
```

## Usage

### Upload Images
Click the "Upload One or More Images" button to upload images from your device. The app supports multiple image file uploads. 

### View Generated Captions
After the images are uploaded, the app will display the generated captions for each image along with their filenames.

### Download Captions as CSV
The generated captions and filenames can be downloaded as a CSV file for reporting or further analysis.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project was developed with the following libraries and technologies:

- **[BLIP (Bootstrapping Language-Image Pretraining)](https://huggingface.co/Salesforce/blip-image-captioning-base)** from Hugging Face’s **Transformers** library. The model is used to generate captions for the uploaded images.
- **[Gradio](https://gradio.app/)**: A Python library for building machine learning demos with an easy-to-use interface.
- **[Pillow](https://python-pillow.org/)**: Python Imaging Library (PIL) Fork, used to handle image opening and processing.
- **[Pandas](https://pandas.pydata.org/)**: A library used for handling and storing data in tabular form (CSV in this case).
- **[NumPy](https://numpy.org/)**: A fundamental package for scientific computing with Python.

Special thanks to **IBM Skills Network Labs** for their course on Building Generative AI-Powered Applications with Python and educational resources that inspired this project.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your forked repository.
4. Create a pull request with a clear explanation of your changes.

## Contact

For any questions or inquiries, please contact the project maintainer:

**Karan Heera**  
- LinkedIn: [https://www.linkedin.com/in/karanheera/](https://www.linkedin.com/in/karanheera/)  
- GitHub: [https://github.com/karanheera](https://github.com/karanheera)
