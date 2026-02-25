import google.generativeai as genai

# 1. 여기에 발급받은 API 키를 따옴표 안에 넣어주세요
MY_API_KEY = "AIzaSyAn1qNZA5FaF08QPQC_D437bnZ35U17qs0"

# 2. 안전하게 연결 설정
genai.configure(api_key=MY_API_KEY)

# 3. 모델 설정 (가장 호환성 높은 이름 사용)
model = genai.GenerativeModel('gemini-pro')

def check_ux_writing(text):
    print(f"\n입력하신 문구: {text}")
    print("에이전트가 검토 중입니다...\n")
    
    # 에이전트에게 줄 구체적인 역할(논리)
    prompt = f"너는 10년 차 UX 라이터야. 다음 문구를 사용자가 이해하기 쉽게 고쳐줘: {text}"
    
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