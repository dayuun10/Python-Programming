
import streamlit as st
import requests
import pandas as pd
from io import StringIO

API_URL = "https://omori.fandom.com/api.php"

st.title("OMORI BATTLE GUIDE")

boss = st.selectbox(
    "보스 선택",
    ["SWEETHEART", "PLUTO", "SPACE EX-BOYFRIEND"]
)

if st.button("보스 능력치 가져오기"):
    try:
        # 1. 위키 문서 전체 요청
        response = requests.get(
            API_URL,
            params={
                "action": "parse",
                "page": boss,
                "prop": "text",
                "format": "json"
            },
            headers={
                "User-Agent": "OMORIBattleGuide/0.1 (school project)"
            },
            timeout=15
        )
        response.raise_for_status()

        # 2. JSON 변환
        data = response.json()

        if "error" in data:
            st.error(data["error"].get("info", "API 오류"))
            st.stop()

        # 3. JSON 안의 HTML 추출
        html = data["parse"]["text"]["*"]

        # 4. HTML 표들을 DataFrame으로 변환
        tables = pd.read_html(StringIO(html))

        found = False

        for table in tables:
            # 표에 포함된 모든 문자열 검사
            table_text = (
                table.to_string(index=False)
                .upper()
            )

            # 전투 능력치 표인지 확인
            if (
                "HEART" in table_text
                and "ATTACK" in table_text
                and "DEFENSE" in table_text
            ):
                st.subheader("전투 능력치")
                st.dataframe(
                    table,
                    hide_index=True
                )
                found = True

        if not found:
            st.warning("능력치 표를 찾지 못했습니다.")

    except requests.RequestException as e:
        st.error(f"API 요청 실패: {e}")

    except (KeyError, ValueError, ImportError) as e:
        st.error(f"데이터 분석 실패: {e}")
