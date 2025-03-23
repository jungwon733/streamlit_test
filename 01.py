import pandas as pd
import streamlit as st

df = pd.read_csv('../repo/output/2025_daegu_apt_total.csv', encoding='utf-8')
# print(df.head())


gu_list = df['구'].sort_values().unique()

with st.sidebar:
    gu_selected = st.selectbox(label='구를 선택해주세요!',
                 options=gu_list,
                 index=None,
                 placeholder='==선택==')
    if gu_selected:
        df1 = df.query(f'구=="{gu_selected}"').reset_index(drop=True)

        dong_list= df1['동'].sort_values().unique()
        dong_selected = st.selectbox(label='동을 선택해주세요!',
                                   options=dong_list,
                                   index=None,
                                   placeholder='==선택==')
        if dong_selected:
            df1 = df1.query(f'동 == "{dong_selected}"').reset_index(drop=True)
st.title('2025년 대구 아파트 매매 내역')
if gu_selected:
    st.write(df1)

