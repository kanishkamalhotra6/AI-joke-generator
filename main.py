from google import genai
client = genai.Client(api_key = "  ") // enter your api key
 
def save_joke(joke):
    with open ("jokes.txt", "a") as file:
        file.write(joke+"\n\n")

while True:
    topic = input("\nEnter a topic (or type quit): ")

    if topic.lower() == "quit":
        print("Goodbye")
        break
    prompt = f"tell me a funny joke about {topic}"
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    joke = response.text
    print ("\nJoke:")
    print(joke)
    print("-" * 30)
    save_joke(joke)
 


