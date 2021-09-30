import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import time

st.title('Streamlit')
st.write('Dataframe')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40],
})

st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
st.table(df.style.highlight_max(axis=0))

# import pandas as pd
# import numpy as np
# import altair as alt
#
# df = pd.DataFrame(
# np.random.randn(200, 3),
# columns=['a', 'b', 'c'])
#
# c = alt.Chart(df).mark_circle().encode(
# x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
#
# st.write(c)
"""
# 章
## 章
### 章


"""

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)
# st.line_chart(df)
# st.line_chart(df)
# #

st.write('Display Image')
if st.checkbox('show Image'):
    img=Image.open('../../ginko-3510673_1920.jpg')
    st.image(img, caption='tasaki', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたが好きな数字は', option, 'です。'

st.write('Interactive widgets')
hobby = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味は',hobby,'です'

condition = st.sidebar.slider('あなたの調子は？', 0,100, 50)
'コンディション：', condition

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここにカラムを表示')

expander = st.beta_expander('お問い合わせ1')
expander.write('お問い合わせ1の回答')
expander = st.beta_expander('お問い合わせ2')
expander.write('お問い合わせ2の回答')
expander = st.beta_expander('お問い合わせ3')
expander.write('お問い合わせ3の回答')

st.write('プログレスバーの表示')
'START!!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'DONE!!!'