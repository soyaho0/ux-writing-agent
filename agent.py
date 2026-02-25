import google.generativeai as genai

# 1. 여기에 발급받은 API 키를 따옴표 안에 넣어주세요
MY_API_KEY = "AIzaSyAn1qNZA5FaF08QPQC_D437bnZ35U17qs0"

# 2. 안전하게 연결 설정
genai.configure(api_key=MY_API_KEY)

# 3. 모델 설정 (가장 호환성 높은 이름 사용)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def check_ux_writing(text):
    print(f"\n입력하신 문구: {text}")
    print("에이전트가 검토 중입니다...\n")
    
    # 에이전트에게 줄 구체적인 역할(논리)
    prompt = f"""
너는 '기억생생' 앱의 UX 라이터야. 
사용자는 60대 이상의 어르신들이니 아래 원칙을 반드시 지켜줘:

1. 어려운 외래어는 쉬운 우리말로 바꾼다 (예: 클릭 -> 누르기, 팝업 -> 안내창)
2. '하세요' 같은 명령조보다는 '~해볼까요?'처럼 친절한 권유형을 사용한다.
3. 한 문장에는 하나의 정보만 담는다.

수정할 문구: {text}
"""
    
    try:
        response = model.generate_content(prompt)
        print("-" * 30)
        print("✨ UX 라이팅 제안:")
        print(response.text)
        print("-" * 30)
    except Exception as e:
        print(f"앗, 에러가 발생했어요: {e}")

# 4. 테스트 실행
check_ux_writing("여기를 클릭해서 다음 단계로 넘어가세요.")