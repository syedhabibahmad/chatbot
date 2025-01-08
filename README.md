# Customer Support Chatbot with PDF Upload and Question Answering

This repository contains a Flask-based web application for customer support that allows users to upload PDF documents, process them into embeddings, and then ask questions based on the content of those PDFs. The application utilizes powerful language models such as Groq and Google Generative AI for generating responses, and integrates voice recognition to convert spoken questions into text.

## Features

- **PDF Upload and Processing**: Upload a PDF document, and the app processes it by extracting text and converting it into embeddings for later question answering.
- **Question Answering**: Ask questions related to the content of the uploaded PDF, and the chatbot will generate answers based on the document's content.
- **Voice Input**: Ask questions by using voice recognition. Just click the microphone icon to start speaking.
- **Live Feedback**: Receive real-time answers, with an option to hear the response via text-to-speech.

## Technologies Used

- **Flask**: A lightweight web framework for building the application.
- **Langchain**: A framework for processing documents, creating embeddings, and generating answers.
- **Groq API**: For leveraging the LLM model to generate answers based on the PDF content.
- **Google API**: For generating embeddings for documents.
- **FAISS**: A library for fast similarity search in high-dimensional spaces, used for storing and retrieving document embeddings.
- **Web Speech API**: For converting speech into text, enabling voice input.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/syedhabibahmad/chatbot.git


2. Navigate to the project directory:
   ```bash
   cd chatbot
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API keys by adding them to your environment variables or a `.env` file:
   - `GROQ_API_KEY`: Your Groq API key.
   - `GOOGLE_API_KEY`: Your Google API key.

5. Start the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/` to access the app.

## Usage

1. **Upload a PDF**: Click on the "Upload PDF" button to upload a PDF document.
2. **Ask a Question**: After uploading the PDF, you can ask questions related to its content. Type your question or use the microphone to speak your question.
3. **View Response**: The chatbot will generate a response based on the content of the uploaded PDF. You can click the "Listen" button to hear the response.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, feel free to contact me at [your-email@example.com](hafizsyedhabibahmadg@gmail.com).

---

## Project Structure

### `app.py`
The main Flask application file that handles routing, PDF processing, and question answering.

### `index.html`
The frontend HTML file that provides the user interface, including the chat interface, PDF upload form, and voice recognition features.

### `requirements.txt`
Contains the list of Python dependencies required to run the project.

---

## Topics

- **Flask Web Application**  
  Web framework used to create the app.

- **PDF Document Processing**  
  How PDFs are uploaded and processed into embeddings for question answering.

- **Question Answering**  
  Using document embeddings to answer questions related to the PDF content.

- **Voice Recognition**  
  Integration of the Web Speech API for converting speech into text.

- **Groq API & Google Generative AI**  
  APIs used for generating answers from the content of the PDFs.

- **FAISS Vector Store**  
  Storing and retrieving document embeddings for fast search.

---

Thank you for checking out this project! Happy coding! 🚀
```

This README includes the updated repository link and other relevant details. You can customize the contact email as needed.
