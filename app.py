import datetime
import math

class Memory:
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content,
            "time": datetime.datetime.now()
        })

    def get_history(self):
        return self.history

    def show(self):
        for item in self.history:
            print(f"[{item['role']}] {item['content']}")

class Tools:
    def calculator(self, expression):
        try:
            result = eval(expression)
            return f"Hasil: {result}"
        except:
            return "Perhitungan tidak valid"

    def current_time(self):
        return str(datetime.datetime.now())

    def knowledge_base(self, query):
        data = {
            "python": "Python adalah bahasa pemrograman populer untuk AI dan data science.",
            "ai": "AI adalah teknologi yang memungkinkan mesin meniru kecerdasan manusia.",
            "agent": "AI Agent adalah sistem yang dapat mengambil keputusan dan bertindak secara otomatis."
        }

        for key in data:
            if key in query.lower():
                return data[key]

        return "Informasi tidak ditemukan di knowledge base."

class ReasoningEngine:
    def __init__(self, tools):
        self.tools = tools

    def decide(self, user_input):

        if user_input.startswith("calc"):
            expression = user_input.replace("calc", "").strip()
            return self.tools.calculator(expression)

        elif "time" in user_input.lower():
            return self.tools.current_time()

        elif "what is" in user_input.lower() or "apa itu" in user_input.lower():
            return self.tools.knowledge_base(user_input)

        else:
            return self.general_response(user_input)

    def general_response(self, text):

        responses = [
            "Menarik, ceritakan lebih lanjut.",
            "Saya mengerti.",
            "Bisa jelaskan lebih detail?",
            "Itu terdengar penting.",
            "Saya sedang memproses informasi."
        ]

        index = len(text) % len(responses)
        return responses[index]

class AIAgent:

    def __init__(self, name="AgentX"):
        self.name = name
        self.memory = Memory()
        self.tools = Tools()
        self.reasoner = ReasoningEngine(self.tools)

    def process(self, user_input):

        self.memory.add("user", user_input)

        decision = self.reasoner.decide(user_input)

        self.memory.add("agent", decision)

        return decision

    def run(self):

        print(f"{self.name} aktif. Ketik 'exit' untuk keluar.\n")

        while True:

            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Agent dimatikan.")
                break

            response = self.process(user_input)

            print(f"{self.name}: {response}")

def main():

    agent = AIAgent("AI-Agent")

    agent.run()

if __name__ == "__main__":
    main()
