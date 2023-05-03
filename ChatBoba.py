import sys
from json import loads
from requests import post

class ChatBoba:
    def __init__(self, system_prompt: str = None, data_sources: list[str] = None, model: str = "gpt-3.5-turbo") -> None:
        self.model = model
        self.data_sources = data_sources if data_sources else []
        self.messages = self.__init_messages(system_prompt)

    def __init_messages(self, system_prompt: str) -> list:
        return [{"role": "system", "content": system_prompt}]
    
    def add_data(self, data: str) -> None:
        self.data_sources.append(data)

    def chat(self, message: str) -> str:
        self.messages.append({"role": "user", "content": message})

        response = post(
            url="https://chatboba.com/api/stream",
            json={
                "messages": self.messages,
                "dataSources": self.data_sources,
                "model": self.model
            },
            stream=True
        )


        assert response.status_code == 200, f"ChatBoba returned status code {response.status_code}."

        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                yield loads(chunk.decode("utf-8").split("data: ")[1])["choices"]
