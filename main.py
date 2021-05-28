import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit 超入門')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)



# st.write('DataFrame')

# df = pd.DataFrame(
    # np.random.randn(100,2)/[50,50] + [35.69, 139.70],
    # columns=['lat', 'lon']
# ) 

#st.table(df.style.highlight_max(axis=0))
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
# st.map(df)


# if st.checkbox('Show Image'):
    # img = Image.open('pexels-photo-1108099.jpeg')
    # st.image(img, caption='Two Dogs', use_column_width=True)

left_columns, right_column = st.beta_columns(2)
button = left_columns.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('Q1')
expander1.write('Q1 Answer')
# option = st.text_input(
#     'あなたの趣味はなんですか？',
# )

# 'あなたの趣味:',option

# condition = st.slider('あなたの調子は？',0,100,50)

# 'コンディション:',condition


