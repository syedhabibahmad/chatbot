from flask import Flask, request, jsonify, render_template
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import time

app = Flask(__name__)

# Initialize API keys
os.environ["GROQ_API_KEY"] = "your-groq-api-key"
os.environ["GOOGLE_API_KEY"] = "your-google-api-key"

# Global variables for embeddings and chatbot
vectors = None
llm = ChatGroq(groq_api_key=os.environ["GROQ_API_KEY"], model_name="mixtral-8x7b-32768")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_pdf():
    global vectors
    try:
        pdf = request.files['pdf']
        if pdf:
            # Save the uploaded PDF
            pdf_path = os.path.join("uploads", pdf.filename)
            pdf.save(pdf_path)

            # Process the PDF and create embeddings
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
            final_documents = text_splitter.split_documents(documents)
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            vectors = FAISS.from_documents(final_documents, embeddings)

            return jsonify({'status': 'success', 'message': 'PDF processed successfully.'})
        else:
            return jsonify({'status': 'error', 'message': 'No file uploaded.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        global vectors
        if not vectors:
            return jsonify({'status': 'error', 'message': 'Embeddings not loaded yet.'})

        question = request.json.get('question')
        if question:
            # Create the retrieval chain
            prompt = ChatPromptTemplate.from_template("""
            Answer the user's question using the provided context ONLY.
            Keep the tone conversational, professional, and concise.

            <context>
            {context}
            <context>
            Question: {input}
            """)
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            # Get the response
            start = time.process_time()
            response_with_docs = retrieval_chain.invoke({'input': question})
            elapsed_time = time.process_time() - start

            response = response_with_docs.get('answer', 'No answer found.')
            return jsonify({'status': 'success', 'answer': response, 'time': elapsed_time})
        else:
            return jsonify({'status': 'error', 'message': 'No question provided.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
