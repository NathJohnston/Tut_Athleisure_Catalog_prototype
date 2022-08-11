import streamlit
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')

my_cnn = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnn.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
