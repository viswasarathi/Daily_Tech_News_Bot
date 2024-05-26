from credentials import Twilio_SID,Twilio_Auth_Token,Twilio_Phone_Number,Client_Number
from flask import Flask,request
from scraping import news_obtained
# import requests
# from twilio.twiml.messaging_response import MessagingResponse
# import openai

app = Flask(__name__)


#function to get daily news
def get_tech_news():
    return news_obtained

#text to ask chatgpt
# def ask_gpt3(prompt):
#     openai.api_key = Gpt_Api_key
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return send_reply(response.choices[0].text.strip())

# # Function to handle incoming SMS messages
# def handle_incoming_message(message_body):
#     # Custom logic for handling user messages
#     # For simplicity, just return a response from GPT-3
#     return ask_gpt3(message_body)

#Function to send sms
def send_sms(message, to):
    from twilio.rest import Client
    client = Client(Twilio_SID, Twilio_Auth_Token)
    msg='\n\n'.join([str(i+1)+". "+ m[0] for i,m in enumerate(message)])
    message = client.messages.create(
        body=msg,
        from_=Twilio_Phone_Number,
        to=Client_Number
    )
# def send_reply(message, to):
#     from twilio.rest import Client
#     client = Client(Twilio_SID, Twilio_Auth_Token)
#     message = client.messages.create(
#         body=message,
#         from_=Twilio_Phone_Number,
#         to=Client_Number
#     )

def send_daily_news():
    articles = get_tech_news()
    # summarized_news = summarize_news(articles)
    send_sms(articles, Client_Number)

# # Handle incoming SMS replies using Flask
# @app.route('/sms', methods=['POST'])
# def sms():
#     incoming_message = request.form['Body']
    
#     # Process the incoming message
#     response_message = handle_incoming_message(incoming_message)

#     # Send the response back to the user
#     resp = MessagingResponse()
#     resp.message(response_message)
#     return str(resp)

if __name__ == '__main__':
    # Schedule to send daily news (you can use a task scheduler for this)
    send_daily_news()

    # Run Flask app to handle incoming SMS replies
    app.run(debug=True)

