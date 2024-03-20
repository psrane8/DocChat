import streamlit as st
import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
import tempfile
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings

load_dotenv()

#retrieve the user defined OpenAI api key 
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
os.environ['OPENAI_API_KEY']=openai_api_key
st.sidebar.write("Create a new OpenAI API Key  \nhttps://platform.openai.com/api-keys")

#setting default llm as GPT 3.5 turbo 
Settings.llm=OpenAI(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the retrieving information and your job is to answer document related questions. Assume that all questions are related to the given document. Keep your answers accurate and based on facts and do not hallucinate information."))

#readFile reads the uploaded file and store it in a temporary directory 
def read_file(uploaded_file):
    temp_dir=tempfile.mkdtemp()
    path=os.path.join(temp_dir,uploaded_file.name )
    with open(path,"wb") as file:
        file.write(uploaded_file.getvalue())
    return temp_dir


#createIndex is used to create a index which can be further used as chat_engine
@st.cache_resource(show_spinner=False)
def create_index(temp_dir):
       document=SimpleDirectoryReader(temp_dir,recursive=True).load_data()
       #converting the documents to index
       index=VectorStoreIndex.from_documents(document, show_progress=True)
       print("index is created")
       return index


#generates response using query_engine and prompt
def generate_response(chat_engine,prompt):
    chatbot_response=chat_engine.chat(prompt).response
    return chatbot_response


#UserInterface of the Application 

st.title("Doc-Chat📄")

#opens the file selection window
with st.sidebar:
    uploaded_file=st.file_uploader(label="Please select a file ",type="pdf",accept_multiple_files=False)
          
#verify if the api key is valid or not
valid_key=openai_api_key.startswith("sk")

#read the uploaded file
if uploaded_file:
       dir=read_file(uploaded_file)


#Conditions to make sure that api key & document are correctly defined
if uploaded_file is None and valid_key is False:
       st.error("Please upload the document and enter the OpenAI key to continue",icon="🚨" )
elif uploaded_file  and valid_key==False:
       st.error("Please add a valid OpenAI api key",icon="⚠️")
elif uploaded_file is None and valid_key :
       st.error("Please upload your document", icon="⚠️")
else :
       #create index based on the uploaded files
       index=create_index(dir)
       #initializing chat engine, chat mode set to condense_question, to retrieve factually correct answers
       chat_engine=index.as_chat_engine(chat_mode="condense_question",llm=Settings.llm)



#Initialize the chat message history
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question!"}
    ]



# Prompt for user input and save to chat history
if prompt := st.chat_input("Please enter your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the prior chat messages
for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])


# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Retrieving information.Please Wait."):
            #retrieve the response based on chat_engine and user prompt
            response = generate_response(chat_engine,prompt)
            st.write(response)
            message = {"role": "assistant", "content": response}
            # Add response to message history
            st.session_state.messages.append(message) 


       


      
        
        
       
                
            


    
     










    

    





    








    
    

