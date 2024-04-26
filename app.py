from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

new_list = {
    "hi":["Hii,how can i help you?"],
    "greeting": ["Hello!", "Hey!", "hey hii"],
    "how are you": ["I am fine, thanks for asking."],
    "what is your name": ["I am a chat bot."],
    "bye": ["Goodbye!", "Bye!"],
    "thanks": ["You're welcome!"],
    "unknown": ["I'm sorry, I didn't understand that."],
    "weather": ["The weather today is sunny with a high of 75°F."],
    "time": ["The current time is 3:00 PM."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!"],
    "quote": ["The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"],
    "fact": ["The Earth's circumference is about 40,075 kilometers."],
    "compliment": ["You're doing great!"],
    "insult": ["I'm sorry, I can't do that."],
    "advice": ["Always remember to stay hydrated!"],
    "question": ["What's your favorite color?"],
    "answer": ["My favorite color is blue."],
    "news": ["In today's news, scientists have discovered a new species of butterfly."],
    "help": ["I'm here to assist you with any questions or concerns you have."],
    "music": ["I'm sorry, I can't play music."],
    "recipe": ["How about trying a delicious pasta carbonara?"],
    "reminder": ["Don't forget to call your mom tomorrow!"],
    "exercise": ["Remember to stretch before exercising to prevent injury."],
    "motivation": ["You've got this! Keep pushing forward!"]
}



def respond(text):
    for key in new_list:
        if text in key:
            return random.choice(new_list[key])
    return "I'm sorry, i don't understand."

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/res", methods=["POST"])
def res():
    data = request.get_json()
    text = data.get("message")
    response = respond(text)
    message = {"ans": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
