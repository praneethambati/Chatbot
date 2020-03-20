from nltk.chat.util import Chat, reflections

conversations= [
    [
        r"hi|hey|hello",
        ["Hello!, I am LPU chatbot","This is LPU chat bot, How can I help you"]

    ],
    [
        r"(.*) college accredited|college accredited(.*)|college accredited",
        ["Yes this is an accredited college"]

    ],

    [
        r"(.*) college fees|college fees|college fees(.*)",
        ["It is 90000 per semester but we provide scholarship ","Per semester it costs around 90000 but you can get scholarship by writing LPUNEST"]

    ],
    [
        r"(.*) scholarship|scholarship|scholarship (.*)",
        ["It depends on the marks obtained in LPUNEST or Jeemains score or board exams ","Scholarship can be availed through LPUNEST or board exam marks"]

    ],
    [
        r"(.*) lpunest|lpunest (.*)|lpunest",
        ["It is an entrance exam exam conducted by LPU","Every year LPU conducts an enrance exam called LPUNEST"]

    ],
    [
        r"(.*) pay college fee| (.*) installments",
        ["yes,but permission of HOD is required","This require permissions from higher authorities","You need to state the purpose for paying the fees in installments"]

    ],
    [
        r"(.*) college hours|college hours|college hours (.*)",
        ["We are open 9 am - 5 pm Monday-saturday!","Monday - Saturday from 9 - 5 and sunday is a holiday"]

    ],
    [
        r"(.*) subjects in 5th sem computer science|subjects in 5th sem computer science",
        ["subjects in 5th sem are:\nTheory of computation\nMicroprocessor and Interface\nprograming in java\nAnalysis and Design of Algorithm\nDatabase management system\nUnix and Shell Programing'"]

    ],
    [
        r"(.*) paymentmode (.*)|paymentmode|payment mode (.*)|(.*) how the payment will be done",
        ["cheque,debit card,netbanking,credit card and cash are acceptable","we accept cheque,credit card, netbanking or cash"]

    ],
    [
        r"(.*) hostel (.*) available (.*)|(.*) hostel (.*) available |(.*) hostel available|hostel available|(.*) hostel available (.*)",
        ["yes, hostel facility is available ","Students can avail the hostel facility within the campus"]

    ],
    [
        r"(.*) facilities available in hostel| facilities available in hostel",
        ["Telephone\nInternet access\nIndoor games\nFirst– Aid.\nReading materials\nTelevision\nDining Hall\nVehicle parking\nRound the-clock security, etc "]

    ],
    [
        r"(.*) hostel fees (.*)|(.*) hostel fees| hostel fees (.*)|hostel fees",
        ["It might be an average of Rs 57500/-","This depend on the type of room you choose"]

    ],
    [
        r"(.*) placements (.*)|(.*) placements|placements (.*)|placements",
        ["Here at LPU we provide 100 percent placement assistance","Every year LPU students get placed at top MNC's"]

    ],
    [
         r"(.*)Thankyou(.*)|(.*)thank you|thankyou(.*)|thankyou",
         ["Have a nice day","We are always to serve you,Thank you!!","Thank you"]
    ],

    ]
def chatbot():
        print("Hi, I'm LOVELY Professionl University CHATBOT ")
        chat = Chat(conversations, reflections)
        chat.converse()
if __name__ == "__main__":
    chatbot()

