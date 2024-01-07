import streamlit as st
import google.generativeai as genai


GOOGLE_API_KEY = "USE YOUR API KEY"

genai.configure(api_key = GOOGLE_API_KEY)

# Use for textual not for image or video for for 60 query / minute
model = genai.GenerativeModel('gemini-pro')


# Title of the webpage
#st.title('Simple Streamlit Webpage')
st.set_page_config(page_title="SQL Query Generator💥", page_icon=":robot:")
st.markdown(
    """
        <div style="text-align: center;">
             <h1>SQL Query Generator🔥</h1>
             <h3> Provide your prompts to generate SQL Query </h3>
             <h4> My backend is Google's GemeiniPro 💪</h2>
        </div>
    """,
    # Below line is mandatory to show above markdown on html as html style
    unsafe_allow_html=True,
    
    )


# A simple text input 
#text_input = st.text_input("Enter your query in simple English:")

# A simple text input area
user_input = st.text_area("Enter your query in simple English:")

#Submit button
submit_button = st.button("Generate SQL Query")


############################### Use below code only if you want to test whether the code is running

#If submit button is pressed the 'user_input' is sent to GeminiPro and the response is saved into 
# 'response'. The 'response.text' field is used to show on the streamlit web page.
# if submit_button:
    
#     response = model.generate_content(user_input)
    
#     print(response.text)
    
#     st.write(response.text)
######################################


if submit_button:
    
    # generate a message fpinner while the GeminiPro is busy to respond back to user's query
    with st.spinner("Qenerating SQL Query..."):
        
        #Create a streamlit template that resembles to users prompt
        template = """
        Create a SQL Query snippet using the below text:
            
            ```
            {user_input}
            
            ```
        Provide the SQL query without explanataions.
        
        
        """
    
    
########################## The below code snippet sends prompt template 'template' from user to geminiPro and gtes the SQL query back on Streamlit
    
    # Formatted template for feding to Streamlit
    formatted_template = template.format(user_input = user_input)
   
    # Uncomment below, if you want to debug 
    #st.write(formatted_template)
    
    # Response from GeminiPro based on the user prompt in the format of formatted template
    response = model.generate_content(formatted_template)
    
    #Save the response text part from the response ofr GeminiPro
    sql_query = response.text
    
    #Show the the same on Streamlit
    #st.write(sql_query)
    
    
###########Stripping the SQL Query Style [OPTIONAL STEP]
###
# ```sql
# SELECT DISTINCT salary
# FROM salary;
# ```

    sql_query = sql_query.strip().lstrip("```sql").rstrip("```")


##################################

########################## If you want expected outcome fpr the SQL Query
#The below code snippet sends prompt from user to geminiPro and gtes the SQL query back on Streamlit

    #Create a streamlit template that resembles to users prompt
    expected_output_template = """
    Provide the expected output of this SQL query snippet:
            
        ```
        {sql_query}
            
        ```
    Provide sample tabular representations without explanataions.
        
        
    """
        
    # Formatted template for feding to Streamlit for 'expected_output_template'
    expected_output_formatted_template = expected_output_template.format(sql_query = sql_query)
        
       
    # Uncomment below, if you want to debug 
    #st.write(expected_output_formatted_template)
        
        
    # Response from GeminiPro based on the user prompt in the format of formatted template
    expected_output_response = model.generate_content(expected_output_formatted_template)
        
        
    #Save the response text part from the response ofr GeminiPro
    expected_response_from_sql_query = expected_output_response.text
        
    #Show the the same on Streamlit
    #st.write(expected_response_from_sql_query)





########################## If you want explanation for expected outcome fpr the SQL Query
#The below code snippet sends prompt from user to geminiPro and gtes the SQL query back on Streamlit

    #Create a streamlit template that resembles to users prompt
    explanation_template = """
    Explain this SQL Query:
            
        ```
        {sql_query}
            
        ```
    Provide with simple explanataions.
        
        
    """
        
    # Formatted template for feding to Streamlit for 'expected_output_template'
    explanation_formatted_template = explanation_template.format(sql_query = sql_query)
        
       
    # Uncomment below, if you want to debug 
    #st.write(expected_output_formatted_template)
        
        
    # Response from GeminiPro based on the user prompt in the format of formatted template
    explanation_response = model.generate_content(explanation_formatted_template)
        
        
    #Save the response text part from the response ofr GeminiPro
    explanation_response_from_sql_query = explanation_response.text
        
    #Show the the same on Streamlit
    #st.write(explanation_response_from_sql_query)





#########SQL Query formatting
    
    with st.container():
        
        st.success("SQL Query Generated Successfully. Here is the Query below:")
        st.code(sql_query, language="sql")

        st.success("Expected ouput of the SQL Query:")
        st.markdown(expected_response_from_sql_query)
        
        st.success("Explanation of this SQL Query is below:")
        st.markdown(explanation_response_from_sql_query)









# Use below for running the code on Visual Studio Code
#main()



