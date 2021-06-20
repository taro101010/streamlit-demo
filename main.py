import streamlit as st
import time

st.title('streamlit entry')
st.write('Progress bar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)



left_column, right_column = st.beta_columns(2)
button = left_column.button('Display text on right column')
if button:
    right_column.write('Here is right column')

expander1 = st.beta_expander('Contact 1')
expander1.write('Write quetion')
expander2 = st.beta_expander('Contact 2')
expander2.write('Write quetion')
expander3 = st.beta_expander('Contact 3')
expander3.write('Write quetion')

option = st.text_input('What is your hobby?')
condition = st.slider('How is your condition?', 0, 100, 50)

# 'Your hobby is', option
# 'Condition:', condition

# if st.checkbox('Show Image'):
#     img = Image.open('kuro.jpg')
#     st.image(img, caption='kurochan', use_column_width=True)
