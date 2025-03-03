import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLlamaresponse(input_text,no_words,blog_style):
    # Llama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config={'max_tokens':256, 'temperature':0.01})
    # Prompt Template
    template="""
        Write a blog for {blog_style} on the topic "{input_text}"
        within {no_words} words.
    """
    # generate the response from the Llama2 model
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],template=template)
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs", page_icon="camera", layout="centered", initial_sidebar_state="expanded")
st.header("Generate Blogs")
input_text=st.text_input("Enter the topic for the blog")
# create more columns for additional 2 fields
col1, col2 = st.columns([5,5])
with col1:
    no_words=st.number_input("Enter the number of words for the blog",min_value=100,max_value=1000)
with col2:
    blog_style=st.selectbox("Select the blog style",['Photographers','Graphic Designers','Businesses','Common People','Creative Individuals','Schools'], index=0)

submit=st.button('Generate Blog')

# final response
if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))
