import streamlit as st
import requests

options = ['RAG', 'EPRAG', 'Candidate Match', 'Atlas', '売上分析', 'ニュース要約']

# Streamlit UI
st.title("RYH CrewAI")

# Select Target
target = = st.selectbox(
    'CrewAI ファンクションを選んでください:',
    options,
    index=0,  # デフォルトで最初の選択肢が選ばれる
    key='CrewAI ファンクション'
)

# Input for prompt
prompt = st.text_input("プロンプトを入力してください:")

# Button to get response
if st.button("生成"):
    try:
      # GETリクエストを送信
      if (target == 'RAG'):
        response = requests.get('https://www.ryhintl.com/crewai/cohere?prompt='+prompt)
        st.write(response)
      elif (target == 'EPRAG'):
        response = requests.get('https://www.ryhintl.com/crewai/eprag?prompt='+prompt)
        st.write(response)
      elif (target == 'Candidate Match'):
        response = requests.get('https://www.ryhintl.com/crewai/match/?job='+prompt)
        st.write(response)
      elif (target == 'Atlas'):
        response = requests.get('https://www.ryhintl.com/crewai/regionsum/')
        st.write(response)
      elif (target == '売上分析'):
        response = requests.get('https://www.ryhintl.com/crewai/sumgen/')
        st.write(response)
      elif (target == 'ニュース要約'):
        response = requests.get('https://www.ryhintl.com/crewai/summary_news/?parm='+prompt)
        st.write(response)
    except:
      print("HTTPエラー:")
      st.write("HTTPエラー:")
