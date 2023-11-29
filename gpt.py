import openai

openai.api_key = "key"


# 챗봇 생성
class chatbot:
    chat_log_size = 2  # 채팅을 기억할 수 있는 크기
    gpt_standard_messages = [
        {
            "role": "system",
            "content": "I want you to act as a Web Developer expert in web development and programming, specializing in HTML/CSS/JavaScript. Base CSS is Bootstrap CSS. When I ask you a question, you must answer with web code. Don't explain, Just Code.",
        }
    ]  # Web Developer 역할 수행 및 Bootstrap CSS 기본 지정, 코드만 반환하도록 prompt, 목적에 맞게 변환 가능

    def set_log_size(self, chat_log_size):
        self.chat_log_size = chat_log_size

    def gpt_send_message(self, question: str):  # 질문 및 답변
        self.gpt_standard_messages.append({"role": "user", "content": question})

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.gpt_standard_messages, temperature=0.8
        )  # 모델 선택 및 질의응답

        answer = res["choices"][0]["message"]["content"]
        self.gpt_standard_messages.append({"role": "assistant", "content": answer})
        if self.chat_log_size * 2 < len(self.gpt_standard_messages):
            self.gpt_standard_messages.pop(1)
            self.gpt_standard_messages.pop(1)

        return answer
