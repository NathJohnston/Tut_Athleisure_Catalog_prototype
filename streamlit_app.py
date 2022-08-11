import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# Connect to Snowflake
my_cnn = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnn.cursor()

# run a Snowflake query and put it all in a variable called my_catalog
my_cur.execute("SELECT color_or_style FROM catalog_for_website")
my_catalog = my_cur.fetchall()

# put the data into a dataframe
df=pandas.DataFrame(my_catalog)

# temp write the dataframe to the page so I can see what I am workimg with 
#streamlit.write(df)

# put the first column into a list
color_list = df[0].values.tolist()
#print(color_list)

# Le's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

#We'ii build the image cation now, since we can
product_cation = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# Use the option selected to go back and get all the info from the database
my_cur.execute("SELECT direct_url, price, size_list, upsell_product_desc FROM catalog_for_website WHERE color_or_style ='" + option + "';")
df2 = my_cur.fetchone()

streamlit.image(
df2[0],
width=400,
caption= product_caption
)

streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])
                             
