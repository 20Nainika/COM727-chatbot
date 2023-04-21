import openai
import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# with open ('hidden.txt') as file:
# openai.api_key = file.read()
openai.api_key = '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'

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("OpenAI Chatbot")
        self.window.configure(bg='cyan')

        self.chat_log = tk.Text(self.window, state=tk.DISABLED, bg='yellow')
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_label = tk.Label(self.window, text="User Input:", bg='cyan')
        self.input_label.grid(row=1, column=0, padx=5, pady=5)

        self.input_entry = tk.Entry(self.window, width=50)
        self.input_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_message, bg='green')
        self.submit_button.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self.window, text="Save", command=self.save_to_pdf, bg='orange')
        self.save_button.grid(row=2, column=0, padx=5, pady=5)

        self.conversation = []

        self.window.mainloop()

    def submit_message(self):
        user_message = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.append_message("You: " + user_message, 'right')

        bot_message = self.get_bot_response(user_message)
        self.append_message("Bot: " + bot_message, 'left')

        self.conversation.append(("You", user_message))
        self.conversation.append(("Bot", bot_message))

    def get_bot_response(self, user_message):
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "what are you doing now" in user_message.lower():
            return "Nothing much just talk with you"
        elif "bye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "who is owner of this project" in user_message.lower():
            return "MS.NAINIKA"
        elif "" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "goodbye" in user_message.lower():
            return "Goodbye! Have a nice day."
        
        else:
            prompt = f"Conversation with chatbot:\nUser: {user_message}\nBot:"
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                temperature=0.5,
                max_tokens=60,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            return response.choices[0].text.strip()

    def append_message(self, message, alignment):
        self.chat_log.configure(state=tk.NORMAL)
        self.chat_log.tag_config(alignment, justify=alignment)
        self.chat_log.insert(tk.END, message + "\n", alignment)
        self.chat_log.configure(state=tk.DISABLED)
        self.chat_log.see(tk.END)
    
    def save_to_pdf(self):
        filename = ("conversation.pdf")
        if not filename:
            return

        c = canvas.Canvas(filename, pagesize=letter)
        textobject = c.beginText()
        textobject.setTextOrigin(50, 750)

        for speaker, message in self.conversation:
            textobject.textLine(f"{speaker}: {message}")

        c.drawText(textobject)
        c.showPage()
        c.save()

    def __del__(self):
        if self.conversation:
            self.save_to_pdf()

if __name__ == "__main__":
    ChatbotGUI()
