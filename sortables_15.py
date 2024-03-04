import streamlit as st
from streamlit_sortables import sort_items
from st_draggable_list import DraggableList

tab_1, tab_2, tab_3, tab_4=st.tabs(["ひらがな ならびかえ ゲーム", "漢字 ならびかえ ゲーム", "県名 ならびかえ ゲーム",
                                   "文章 さくせい ゲーム"])

with tab_1:

  st.title("ひらがな ならびかえ ゲーム")
  st.markdown("選択肢欄のひらがなを並びかえてことばを作ってください")
  st.markdown("")

  original_items = [
    {'header': '選択肢欄',  'items': ['き', 'く', 'ち', 'じ', 'ま', 'ん', 'た', 'ふ', 'け', 'し', 'あ']},
    {'header': '回答欄１', 'items': [ ]},
    {'header': '回答欄２', 'items': [ ]}
  ]

  sorted_items = sort_items(original_items, multi_containers=True)

with tab_2:

  st.title("漢字 ならびかえ ゲーム")
  st.markdown("選択肢欄の漢字を使ってことばを2つ作ってください")
  st.markdown("")

  original_items = [
    {'header': '選択肢欄',  'items': ['都', '田', '学', '京', '庁', '秋', '大', '県']},
    {'header': '回答欄１', 'items': [ ]},
    {'header': '回答欄２', 'items': [ ]}
  ]

  sorted_items = sort_items(original_items, multi_containers=True)


with tab_3:

  st.title("県名 ならびか えゲーム")
  st.markdown("北から順に県名を並べてください")
  st.markdown("")

  data = [
    {"id": "chiba", "order": 5, "name": "千葉県"},
    {"id": "tokyo", "order": 6, "name": "東京都"},
    {"id": "ehime", "order": 8, "name": "愛媛県"},
    {"id": "kanagawa", "order": 1, "name": "神奈川県"},
    {"id": "gunma", "order": 4, "name": "群馬県"},
    {"id": "shizuoka", "order": 7, "name": "静岡県"},
    {"id": "kochi", "order": 10, "name": "高知県"},
    {"id": "saga", "order": 11, "name": "佐賀県"},
    {"id": "miyagi", "order": 1, "name": "宮城県"},
    {"id": "shimane", "order": 9, "name": "島根県"},
    {"id": "akita", "order": 2, "name": "秋田県"},
    {"id": "ishikawa", "order": 3, "name": "石川県"},
  ]

  slist = DraggableList(data, width="50%")


with tab_4:

  st.title("文章 さくせい ゲーム")
  st.markdown("この問題は少し難しいかもしれません")
  st.markdown("選択肢欄にあることばを並びかえて回答欄１に文章を作ってください")
  st.markdown("文章に足りない文字を回答欄２から選んで回答欄３に入れてください")
  st.markdown("")

  original_items = [
    {'header': '選択肢欄',  'items': ['外', 'し', 'わたし', 'で', 'な', 'ら', 'に', 'った', 'は', '人', 'い']},
    {'header': '回答欄１', 'items': [ ]},
    {'header': '回答欄２', 'items': [ '家', 'ゆ', 'あ', '車', 'と', 'あなた', ]},
    {'header': '回答欄３', 'items': [ ]}
  ]

  sorted_items = sort_items(original_items, multi_containers=True)


