# Doc-Chat

## Description

The goal of this application is to help the user chat with their document and retrieve information more efficiently, thereby enhancing the user's productivity. To provide better data security for the uploaded documents, tempfile library is used to create a temporary directory to deal with the user documents. Being a RAG (Retrieval Augmented Generation) application, this chatbot tends to provide factual information to user queries based on the user-defined data.
This project utilizes Llama-index, OpenAI Embeddings, Streamlit, GPT 3.5 turbo LLM, and Python.

## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/psrane8/DocChat.git
   ```

2. Navigate to the project directory.
   ```bash
   cd DocChat
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have installed all dependencies as instructed above.

2. Run the Streamlit app.
   ```bash
   streamlit run application.py
   ```

3. Access the app through your browser at http://localhost:8501

4. Enter your OpenAI API key or create one and then upload your document from the file selector
   
5. Follow the instructions provided in the app to chat with your document and retrieve information efficiently.

## Deployment
Doc-Chat has been deployed at https://doc-chat-app.streamlit.app/

## Credits

- [Llama-index](https://www.llamaindex.ai/)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- [Streamlit](https://streamlit.io/)
- [GPT 3.5 Turbo LLM](https://platform.openai.com/docs/models)
- [Python](https://www.python.org/)

## License

This project is licensed under the [MIT License](LICENSE).
```
