from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded college information with 50 key components
college_info = {
    # Greetings
    "hii": "Hello! How can I assist you today?",
    "hello": "Hi there! What would you like to know?",
    "how are you": "I'm just a chatbot, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! If you have more questions, feel free to ask.",
    "help": "Sure! You can ask about admission, courses, campus facilities, scholarships, and student life.",
    
    # Academic Information
    "degree programs": "We offer various degree programs including Bachelor's, Master's, and Doctorates in multiple fields.",
    "online courses": "Yes, we provide several online courses for remote learning.",
    "course duration": "Most undergraduate programs take about four years to complete, while postgraduate programs typically take two years.",
    "class size": "Our average class size is about 30 students, allowing for personalized attention.",
    "faculty qualifications": "Our faculty members hold advanced degrees and have extensive industry experience.",
    "research opportunities": "We offer numerous research opportunities across various disciplines.",
    "academic calendar": "Our academic year starts in August and ends in May, with breaks in between.",
    "exchange programs": "We have partnerships with universities worldwide for student exchange programs.",
    "internships": "Internship opportunities are available through our career services office.",
    "grading system": "We follow a standard grading system from A to F, with GPA calculated on a 4.0 scale.",
    
    # Admission and Application
    "application deadlines": "Our application deadlines are usually in January for the fall semester.",
    "application fee": "There is a non-refundable application fee of $50.",
    "requirements for international students": "International students need to submit additional documents like TOEFL/IELTS scores.",
    "scholarship application": "Scholarship applications are typically due at the same time as the admissions application.",
    "interview process": "Some programs may require an interview as part of the admissions process.",
    "acceptance rate": "Our acceptance rate is approximately 30%.",
    "transfer students": "We welcome transfer students from other institutions. Please check the transfer policy.",
    "early decision": "We offer an early decision option for students who are certain about their choice.",
    "letters of recommendation": "Two letters of recommendation are required for the application.",
    "personal statement": "A personal statement outlining your goals and motivations is part of the application.",
    
    # Financial Information
    "tuition fees": "Tuition fees for undergraduate programs are around $20,000 per year.",
    "financial aid": "Financial aid is available based on need. Please fill out the FAFSA.",
    "payment plans": "We offer flexible payment plans for tuition fees.",
    "work-study programs": "Yes, we have work-study programs available for eligible students.",
    "cost of living": "The estimated cost of living in the area is about $15,000 per year.",
    "scholarship opportunities": "Various scholarships are available based on merit and need.",
    "grants": "We provide several grants for students from low-income families.",
    "student loans": "We have partnerships with financial institutions for student loans.",
    "tuition waivers": "Certain tuition waivers are available for veterans and active military personnel.",
    "emergency funds": "We offer emergency funds for students facing unforeseen financial challenges.",
    
    # Campus Life
    "housing options": "We provide on-campus housing as well as off-campus housing assistance.",
    "food services": "Multiple dining options are available, including vegetarian and vegan choices.",
    "clubs and organizations": "There are over 50 student clubs and organizations to join.",
    "sports facilities": "Our campus has a gym, swimming pool, and several sports fields.",
    "student health services": "We offer comprehensive health services for all students.",
    "transportation": "There are shuttle services and public transportation options near campus.",
    "student events": "Regular events and activities are organized to foster community engagement.",
    "mental health support": "Counseling services are available for students who need mental health support.",
    "study abroad programs": "We offer study abroad programs in various countries.",
    "community service": "Many opportunities for community service and volunteering are available.",
    
    # Career Services
    "career counseling": "We provide career counseling services to help you plan your career path.",
    "job placement services": "Our job placement services assist graduates in finding employment.",
    "resume workshops": "We conduct resume and interview workshops regularly.",
    "career fairs": "Career fairs are held twice a year to connect students with employers.",
    "alumni network": "Our strong alumni network provides valuable connections for students.",
    "internship programs": "We help students secure internships in their field of study.",
    "mentorship programs": "Mentorship programs connect students with professionals in their field.",
    "skills development": "Workshops for skills development are regularly offered to students.",
    "networking events": "Networking events are organized to connect students with industry leaders.",
    "job search resources": "We provide various resources to assist students in their job search.",
    
    "what is the tuition fee?": "Tuition fees for undergraduate programs are around $20,000 per year.",
   "what programs do you offer?": "We offer a variety of undergraduate and postgraduate programs including Computer Science, Business Administration, and more.",
   "what are the admission requirements?": "To apply for admission, you need to submit an application form along with your transcripts and test scores.",
   "when is the application deadline?": "Our application deadlines are usually in January for the fall semester.",
   "what is the acceptance rate?": "Our acceptance rate is approximately 30%.",
   "do you offer scholarships?": "Yes, we offer several scholarships based on merit and need. Please check our website for more details.",
   "how can I apply for financial aid?": "Financial aid is available based on need. Please fill out the FAFSA to apply.",
   "what is the cost of living on campus?": "The estimated cost of living in the area is about $15,000 per year.",
   "what are the housing options available?": "We provide on-campus housing as well as off-campus housing assistance.",
   "are there online courses available?": "Yes, we provide several online courses for remote learning.",
   "what is the average class size?": "Our average class size is about 30 students, allowing for personalized attention.",
   "what extracurricular activities are offered?": "There are over 50 student clubs and organizations to join.",
   "is there a campus health center?": "Yes, we offer comprehensive health services for all students.",
   "what support services are available for students?": "We provide various support services including academic advising and mental health support.",
   "what are the faculty qualifications?": "Our faculty members hold advanced degrees and have extensive industry experience.",
   "is there a study abroad program?": "We offer study abroad programs in various countries.",
   "what is the process for transferring credits?": "Transfer credits are evaluated on a case-by-case basis. Please check our transfer policy.",
   "how do I contact admissions for more information?": "You can contact our admissions office via email or phone. Details are on our website.",
   "what types of internships are available?": "Internship opportunities are available through our career services office.",
   "are there work-study programs?": "Yes, we have work-study programs available for eligible students.",
   "what is the campus culture like?": "Our campus culture is vibrant with a diverse student body and many events.",
   "are there any clubs or organizations I can join?": "Yes, there are various clubs and organizations catering to different interests.",
   "what are the library facilities like?": "Our library is well-equipped with study areas, computer labs, and extensive resources.",
   "is there a transportation service on campus?": "Yes, there are shuttle services and public transportation options available.",
   "how does the grading system work?": "We follow a standard grading system from A to F, with GPA calculated on a 4.0 scale.",
   "what is the process for changing majors?": "Students can change majors by meeting with their academic advisor and filling out the required forms.",
   "how can I get involved in research opportunities?": "Many research opportunities are available through various departments. Speak with your faculty advisor.",
   "what kind of career services do you offer?": "We provide career counseling, resume workshops, and job placement services.",
   "are there any orientation programs for new students?": "Yes, we offer orientation programs for new students before the semester begins.",
   "what is the academic calendar?": "Our academic year starts in August and ends in May, with breaks in between.",
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def ask():
    user_input = request.json.get('queryResult', {}).get('action', '').lower()

    # Default response
    response = "I'm sorry, I don't have information about that. Please ask another question!"

    # Generate response based on user input
    for key in college_info:
        if key in user_input:
            response = college_info[key]
            break

    return jsonify({"fulfillmentText": response})

#if __name__ == '__main__':
 #   app.run(debug=True)
