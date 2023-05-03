import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot")
        self.window.geometry("500x600")
        self.window.configure(bg='white')

        self.chat_log = tk.Text(self.window, state=tk.DISABLED, bg='lightgray', font=("Arial", 12), wrap=tk.WORD)
        self.chat_log.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10, expand=True)

        input_frame = tk.Frame(self.window, bg='purple')
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        # Set the color of the text to red
        print("\033[33mHello, world!\033[33m")


        self.input_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
        self.input_entry.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

        self.submit_button = tk.Button(input_frame, text="Send", command=self.submit_message, bg='green', fg='white', font=("Arial", 12))
        self.submit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(input_frame, text="Clear", command=self.clear_chat_log, bg='red', fg='white', font=("Arial", 12))
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.window, text="Save conversation to PDF", command=self.save_to_pdf, bg='orange', fg='white', font=("Arial", 12))
        self.save_button.pack(side=tk.BOTTOM, padx=10, pady=10)

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
        elif "How old are you?" in user_message.lower():
            return "I am a computer program, so I don't have an age."
        elif "what can you do" in user_message.lower():
            return "I can answer your questions,provide information,or just have a conversation with you."
        elif "what is the meaning of life" in user_message.lower():
            return "That is a difficult question to answer.it depends on who you ask."
        elif "what is your favorite color" in user_message.lower():
            return "I don't have a favorite color because I'am machine."
        elif "How do i change my password?" in user_message.lower():
            return "To change your password, go to your account settings and look for the option to change your password."
        elif "How do i contact customer support?" in user_message.lower():
            return "You can contact customer support by phone, email or through our website live chat feature."
        elif "What is the capital of france?" in user_message.lower():
            return "The capital of france is Paris."
        elif "what is python" in user_message.lower():
            return "python is programming languages."
        elif "what is java" in user_message.lower():
            return "java is programming languages."
        elif "what is laptop" in user_message.lower():
            return "laptop is device"
        elif "what is the typical listing price on airbnb in the uk?" in user_message.lower():
            return "According to data from inside Airbnb, the typical listing price on airbnb in the uk is around $100-120 per night."
        elif "How many Airbnb listing does the typical uk host have" in user_message.lower():
            return "The typical uk host has 1 or 2 listing on airbnb, although there are hosts with many more listing."
        elif "what kind of home is most frequently posted on airbnb in the uk?" in user_message.lower():
            return "According to data from inside aribnb, the most frequently posted type of home on airbnb in the uk is the entire apartment or house,followed by private rooms."
        elif "How many bedrooms do the majority of listing on airbnb in the uk have?" in user_message.lower():
            return "according to the same data, the majority of listing on airbnb in the uk have 1 or 2 bedrooms."
        elif "what is the typical review rating for listings on airbnb in the uk?" in user_message.lower():
            return "The typical review rating for listings on airbnb in the uk is 4.7 out of 5 stars, based on data from airbnb website."
        elif "what is the breakdown of airbnb host response times in the uk?" in user_message.lower():
            return "According to airbnb, the breakdown of host response times in the uk is as follow: 61% respond within an hour."
        elif "what are the most popular means of verification used by host on airbnb in the uk?" in user_message.lower():
            return "the most popular means of vericatiopn used by hosts on airbnb in the uk include phone number, email address, government-issued id, and social media account verification."
        elif "what percentage of booking requests on airbnb in the uk are accepted by hosts on average?" in user_message.lower():
            return "according to airbnb . the average accceptance rate or booking requests on the platformn in the uk is around 50%."
        elif "what types of rooms are available on airbnb in the uk?" in user_message.lower():
            return "the types of rooms available on airbnb in the uk include entire homes/apartments, private rooms,shared rooms, and unique accomodation such as castles ,yurts, and treehouses."
        elif "can guests easily reserve properties on airbnb in the uk without host consent?" in user_message.lower():
            return "guests cannot resesrve properties on airbnb in the uk without host consent. hosts must acccept a booking request before a resevation is confirmed."
        elif "how many listings on airbnb in the uk have never received any feedback?" in user_message.lower():
            return "it is not possible to determine the exact number of listings on airbnb in the uk thet have never received any feedback, as this information is not publicly available."
        elif "how many bathrooms are there on average in uk rentals on airbnb?" in user_message.lower():
            return "the number of bathrooms in uk rentalls on airbnb can vary widely depending on the type of accomodation. however, on average, most entire homes/apartments listed on airbnb in the uk have two or more bathrooms."        
        elif "who is the prime minister of uk?" in user_message.lower():
            return "In 2019, the office of Minister for the Union was established; Boris Johnson became the first prime minister to hold this title. The prime minister's official residence and office is 10 Downing Street in London. Rishi Sunak has been the prime minister since 25 October 2022."    
        elif "what rae the main criteria that uk visitors to airbnb often rate in their reviews?" in user_message.lower():
            return "Cleanliness and overall condition of the property Location and accessibility to nearby attractions or amenities Accuracy of the listing description and photos Communication and helpfulness of the host Value for money and overall experience"  
        elif "what are the most popular means of verification used by hosts on airbnb in the uk?" in user_message.lower():
            return "Airbnb hosts in the UK can use various means of verification to establish their identity and build trust with guests. Some of the most popular means of verification used by hosts on Airbnb in the UK include:Providing a government-issued ID: Hosts can provide Airbnb with a copy of their passport, driver's license or national ID card.Connecting social media accounts: Hosts can connect their Airbnb account to their social media accounts to show that they have a real online presence.Confirming email and phone number: Airbnb verifies the email and phone number provided by hosts to ensure that they are valid and operational."
        elif "what percentage of booking requests on airbnb in the uk are acceptecd by hosts on average?" in user_message.lower():
            return "The acceptance rate of booking requests on Airbnb in the UK can vary depending on different factors such as location, time of year, and the quality of the guest's profile. However, according to Airbnb's data, the average acceptance rate for booking requests in the UK is around 60-70%. It's worth noting that some hosts may have stricter acceptance policies, while others may be more flexible."        
        elif "in the uk airbnb data, what is the distribution of treview scores for location for listings with a specific number of bedrooms?" in user_message.lower():
            return "In the UK Airbnb data, the distribution of review scores for location for listings with a specific number of bedrooms can vary depending on several factors, such as the location, amenities, and other features of the property. Therefore, it is not possible to provide a general answer without specific information about the listings in question."
        elif "how many listings in the uk's airbnb data have a 'flexible' or moderate cancellation policy that are free?" in user_message.lower():
            return "It is unclear from the question whether  means that the cancellation policy is free or that the listing is free of charge. Assuming you mean listings that offer a free cancellation policy, I cannot provide an exact number without the latest data. However, it is possible to filter Airbnb listings by cancellation policy and availability, which could help narrow down the search."
        elif " in the uk airbnb statistics, wehat is the average price per night for listings with a specific number of maximum nights allowed, such as 1 night or 7 nights?" in user_message.lower():
            return "The average price per night for listings with a specific number of maximum nights allowed can vary widely depending on several factors, such as location, property type, and amenities. Therefore, it is not possible to provide a general answer without specific information about the listings in question."
        elif " how many listings from the uk's airbnb database were examinated in the past 30 days?" in user_message.lower():
            return "The number of listings from the UK's Airbnb database that were examined in the past 30 days is not available to me as my knowledge cutoff date is 2021-09."
        elif "what is the breakdown of property types in the uk airbnb data for listyings with  a specific number of bathrooms sucha sa 1 bathtroom or 2 bathrooms?" in user_message.lower():
            return "The breakdown of property types in the UK Airbnb data for listings with a specific number of bathrooms can also vary depending on several factors, such as location, property type, and amenities. Therefore, it is not possible to provide a general answer without specific information about the listings in question."
        elif "how many listings in the uk's data on airbnb have hosts who have undergone various levels of verification?" in user_message.lower():
            return "The number of listings in the UK's data on Airbnb that have hosts who have undergone various levels of verification is not available to me as my knowledge cutoff date is 2021-09."
        elif " what is the typical check in review ratings for listings in a particular neighbourhood according to the uk airbnb data?" in user_message.lower():
            return "The typical check-in review rating for listings in a particular neighbourhood according to the UK Airbnb data can vary depending on several factors, such as the quality of the property and the host's communication skills. Therefore, it is not possible to provide a general answer without specific information about the neighbourhood and listings in question."
        elif "how many listings in the uk's airbnb database have a host who can be instantly booked and has their identity verified?" in user_message.lower():
            return "The number of listings in the UK's Airbnb database that have a host who can be instantly booked and has their identity verified is not available to me as my knowledge cutoff date is 2021-09."
        elif "what types of rooms are available on airbnb in the uk?" in user_message.lower():
            return "The types of rooms available on Airbnb in the UK can vary widely, from private rooms in shared homes to entire apartments, houses, villas, and unique accommodations such as boats, treehouses, and yurts."
        elif "can guests easily reseve properties on airbnb in the uk without host consent?" in user_message.lower():
            return "Guests cannot reserve properties on Airbnb in the UK without host consent. Guests can only request to book a property, and hosts have 24 hours to accept or decline the request. Some hosts may also have instant booking enabled, which means that guests can book the property without prior host approval."
        elif "how many listings on airbnb in the uk have never received any feedback?" in user_message.lower():
            return "The number of listings on Airbnb in the UK that have never received any feedback is not available to me as my knowledge cutoff date is 2021-09."
        elif "how many bathrooms are there on average in uk rentals on airbnb?" in user_message.lower():
            return "The average number of bathrooms in UK rentals on Airbnb can vary depending on several factors, such as the size and type of property. Some properties may have shared bathrooms, while others may have multiple en-suite bathrooms."
        elif "what are the main criteria the uk visitors to airbnb often rate in their reviews?" in user_message.lower():
            return "The main criteria that UK visitors to Airbnb often rate in their reviews include the location, cleanliness, accuracy of the listing description, communication with the host, and value for money."  
        elif "which five types of properties are most frequently listed on airbnb in the uk?" in user_message.lower():
            return "The five types of properties most frequently listed on Airbnb in the UK are entire apartments, private rooms, entire houses, shared rooms, and bed and breakfasts."
        elif "can you give any instances of amenties that hosts frequently offer on airbnb in the uk?" in user_message.lower():
            return "Some amenities that hosts frequently offer on Airbnb in the UK include Wi-Fi, kitchen facilities, washing machines, free parking, and TV."
        elif "how does the average listing price on airbnbb differ based on the kind of home in the uk?" in user_message.lower():
            return "The average listing price on Airbnb in the UK can differ based on the kind of home. For example, entire apartments and houses tend to be more expensive than private rooms or shared rooms."
        elif "how many beds are typically listed on airbnb in the uk?" in user_message.lower():
            return "The number of beds listed on Airbnb in the UK can vary widely, depending on the size and type of property. Some listings may have only one bed, while others may have multiple beds in different rooms."
        elif "where is solent university?" in user_message.lower():
            return "Solent University is located in Southampton, a port city on the south coast of England, UK."
        elif " how many courses are available in solent university?" in user_message.lower():
            return "As of my knowledge cutoff in September 2021 Solent University offered over 200 undergraduate and postgraduate courses across a range of subjects including art, design and fashion, business and law, communication and media, computing and technology, engineering, maritime, psychology, sport and exercise, and tourism and hospitality However, the number of courses offered may have changed since then It is best to check Solent University's website for the most up-to-date information."
        elif "how to get addmission in solent university?" in user_message.lower():
            return "To apply for admission to Solent University, you can follow these general steps:1. Choose a course: Visit the Solent University website to browse through the available courses and choose the one that best suits your interests and career goals.2. Check the entry requirements: Make sure you meet the minimum academic and English language requirements for your chosen course. This information is usually available on the course page.3. Apply online: Complete the online application form on the Solent University website. You will need to provide your personal details, academic qualifications, and a personal statement.4. Submit supporting documents: You may be required to submit supporting documents, such as academic transcripts, a CV, or a portfolio of work. Make sure to check the specific requirements for your course.5. Receive an offer: If your application is successful, you will receive an offer from Solent University. The offer may be unconditional, meaning you have met all the entry requirements, or conditional, meaning you still need to meet certain conditions, such as obtaining a specific grade in your exams 6. Accept the offer: If you are happy with the offer, you can accept it and pay any required deposit to secure your place at the university.7. Apply for a visa (if applicable): If you are an international student, you will need to apply for a student visa to study at Solent University.It is important to note that the application process may vary depending on your nationality, chosen course"        
        elif "capital of uk?" in user_message.lower():
            return "The capital of the UK is London."
        elif "what is solent university?" in user_message.lower():
            return "Solent University is a public university located in Southampton, UK. It offers a range of undergraduate and postgraduate courses across various subjects."        
        elif "when was solent university was founded?" in user_message.lower():
            return "Solent University was founded in 2004, although it traces its roots back to the Southampton Technical College, which was established in 1894."
        elif "what is the typical monthly review count for listing on airbnb in the uk?" in user_message.lower():
            return "Host response times on Airbnb in the UK and their associated percentages:According to Airbnb's website, hosts are expected to respond to inquiries within 24 hours. In general, hosts who respond quickly tend to have a higher booking rate than those who do not. However, the exact response times and associated percentages may vary depending on the host and the property."
        elif "what relationship is there netween the review score rating and the review scores for cleanliness, check-in, communications, and location on airbnb in the uk?" in user_message.lower():
            return "Typical monthly review count for listings on Airbnb in the UK:The monthly review count for listings on Airbnb in the UK can vary widely depending on factors such as location, property type, and seasonality. However, hosts who receive more reviews tend to have higher occupancy rates and earn more revenue."
        elif "what is the average cost of listing on airbnb in the uk that offer fast booking compared to those that do not?" in user_message.lower():
            return "Relationship between review score rating and review scores for cleanliness, check-in, communication, and location on Airbnb in the UK: The review score rating on Airbnb is an overall rating that reflects guests' overall satisfaction with their stay. However, guests are also asked to rate specific aspects of their stay, including cleanliness, check-in, communication, and location. In general, a higher overall review score rating is associated with higher ratings for these specific aspects of the stay."
        elif "can you give some examples of the most popular type of verifiaction utilised by hosts on airbnb in the uk?" in user_message.lower():
            return "Average cost of listings on Airbnb in the UK that offer fast booking compared to those that do not: The average cost of listings on Airbnb in the UK that offer fast booking compared to those that do not may vary depending on the property and the location. However, listings that offer fast booking tend to be more popular with guests and may command higher prices."
        elif "how many bedrooms are on average in the listing?" in user_messages.lower() :
            return "Average number of bedrooms in listings The average number of bedrooms in listings on Airbnb in the UK can vary widely depending on factors such as location, property type, and size. However, the most common types of listings tend to have 1-2 bedrooms."
        elif "what is your name?" in user_messages.lower():
            return "my name is chatbot."
        elif "what can you do?" in user_messages.lower():
            return " I am designed to help you with specific purpose of the chatbot You can ask me questions or give me commands related to specific area."
        elif "can you help me."  in user_message.lower():
            return ": Yes, I can help you with specific task Please provide me with more information about what you need."   
        elif "how do i contact customer support?" in user_message.lower():
            return "You can contact customer support by [specific instructions or contact information], or I can assist you in submitting a support request."
        elif "what are some popular tourist attractions in the uk?" in user_message.lower():
            return "Some popular tourist attractions in the UK include the Tower of London, Buckingham Palace, Stonehenge, the Scottish Highlands, and the Lake District."
        elif "what is the currency used in the uk?" in user_message.lower():
            return " The currency used in the UK is the pound sterling GBP."
        elif "what is the official language of the uk?" in user_message.lower():
            return " The official language of the UK is English."
        
        
        else:
            return "I'm sorry, I didn't understand your message."

    def append_message(self, message, alignment):
        self.chat_log.configure(state=tk.NORMAL)
        self.chat_log.tag_config(alignment, justify=alignment)
        self.chat_log.insert(tk.END, message + "\n\n", alignment)
        self.chat_log.configure(state=tk.DISABLED)
        self.chat_log.see(tk.END)

    def clear_chat_log(self):
        self.chat_log.configure(state=tk.NORMAL)
        self.chat_log.delete("1.0", tk.END)
        self.chat_log.configure(state=tk.DISABLED)

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
    def __del__(self):
        if self.conversation:
            self.save_to_pdf()

