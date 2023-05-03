# chatBoba
A simple python api to use openai's gpt-3.5 and gpt-4 to generate text.

# Usage
```python
cb = ChatBoba(system_prompt="You are a helpful chatbot that helps people with their problems.")

while True:
    inp = str(input("> "))
    c = cb.chat(inp)
    for i in c:
        d = i[0]["delta"]
        if "content" in d:
            sys.stdout.write(d["content"])
        sys.stdout.flush()
    sys.stdout.write("\n")
```