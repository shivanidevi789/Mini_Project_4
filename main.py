from gtts import gTTS
import random
import pygame
from io import BytesIO

# Initialize pygame mixer
pygame.mixer.init()

# Jokes dictionary
jokes_dict = {
    1: "Teacher: Tum itne marks kaise laaye? \nStudent: Exam ke pehle light chali gayi thi, mai andhere me hi likh aaya.",
    2: "Pappu: Doctor sahab, jab mai chai peeta hoon to dard hota hai. \nDoctor: Cup se chammach nikaal lo!",
    3: "Santa: Agar koi insaan tumhe do baar bevakoof banaye to? \nBanta: Tisri baar uski shaadi attend mat karna.",
    4: "Boy: Tum itni khubsurat ho, tumse shaadi kaise karu? \nGirl: Pehle bank balance dikhao, fir baat karenge.",
    5: "Ek aadmi doctor ke paas gaya, or bola: Doctor sahab, mujhe bhoolne ki bimari ho gayi hai. \nDoctor: Kab se? \nAadmi: Kab se kya?",
    6: "Boss: Tum late kyu aaye? \nEmployee: Sir alarm nahi baja... Boss: Mobile me tha ya ghante me? Employee: Neend me tha.",
    7: "Teacher: Pappu, tum class me so rahe ho! \nPappu: Sir, aankh band kar ke soch raha hoon.",
    8: "Raju: Main itna handsome hoon ki mirror bhi mujhe dekhta reh jata hai!",
    9: "Patient: Mujhe bhoolne ki bimari ho gayi hai. \nDoctor: Kab se? Patient: Kab se kya?",
    10: "Golu: Pata hai meri girlfriend ka naam kya hai? \nMotu: Nahi, kya? Golu: Tumhari kalpana.",
    11: "Boy: Aapka naam kya hai? \nGirl: Tumhe kya karna hai? \nBoy: Resume me likhna hai Dream Job ke niche.",
    12: "Teacher: Homework kyun nahi kiya? \nStudent: Sir kal light chali gayi thi. \nTeacher: Din me? Student: Sir solar light thi.",
    13: "Wife: Sunte ho, aap mujhe kuch surprise doge? \nHusband: Haan, main gas ka bill bhar aaya.",
    14: "Bhai: Mujhe bhagwan dikhte hain! \nDost: Kya leke aaya re tu?",
    15: "Doctor: Tumhare pair me fracture hai. \nPatient: Sir, dard to dil me hai.",
    16: "Pappu: Mere pass ek aisi chappal hai jo udti hai. \nBantu: Fir? \nPappu: Ud ke direct teacher ke muh pe lagti hai.",
    17: "Santa: Agar main marr gaya to? \nBanta: Bhai party deni padegi!",
    18: "Mom: Beta result kya aaya? \nBeta: Darr mat maa, fail to tere laal ne bhi kiya tha.",
    19: "Pappu: Sir, bathroom me signal nahi aa raha. \nTeacher: Waha kya WhatsApp chalana hai?",
    20: "Boy: Mere paas car hai, bangla hai. \nGirl: Tumhare paas kya hai? \nBoy: Mere paas tum ho!",
    21: "Teacher: Ye equation ka answer kya hai? \nStudent: Sir Google bhi confuse ho gaya.",
    22: "Patient: Doctor sahab, jab mai baat karta hoon to awaz nahi nikalti. \nDoctor: To fir yeh kya tha?",
    23: "Santa: Main toh sochta hoon Himalaya par chadh jaun. Banta: Chadh ja, lekin Himalaya cream mat le jana!",
    24: "Boy: Tumhara favourite fruit kya hai? \nGirl: Mango. \nBoy: Toh meri zindagi me aa ja meri aam-zindagi.",
    25: "Teacher: Neend me kyun ho? \nStudent: Sir sapne me padh raha tha.",
    26: "Girl: Aaj mere pair dukh rahe hain. \nBoy: Kyun? \nGirl: Tumhare khwab me chal chal ke thak gayi hoon.",
    27: "Baccha: Mumma aap kya kar rahi ho? \nMumma: Makeup. Baccha: Pehle kyun nahi kiya?",
    28: "Wife: Aaj kal tum mujhe dekhtay nahi! \nHusband: Kyunki tumhara mobile mere se zyada beautiful hai.",
    29: "Friend: Tera phone gira kya? Screen to phat gayi. \nBoy: Nahi bhai, maa dekh li status.",
    30: "Santa: Mujhe hawa me chalte dekhna hai. \nBanta: Plane me chadh ja!",
    31: "Student: Agar paper easy aaya to fail nahi hote. \nTeacher: Paper likhna bhi to padhta hai.",
    32: "Patient: Mujhe toh kuch yaad hi nahi rehta. \nDoctor: Kab se? Patient: Kab se kya?",
    33: "Raju: Agar girlfriend naraz ho jaye to kya karte ho? \nShyam: Recharge karwa deta hoon.",
    34: "Boy: Aap coffee piyengi? \nGirl: Nahi. \nBoy: To fir chai hi le lo meri zindagi me.",
    35: "Doctor: Aapko kis cheez se allergy hai? \nPatient: Homework se!",
    36: "Boy: Tumhara naam kya hai? \nGirl: Guess karo. \nBoy: Password to nahi hoga?",
    37: "Wife: Mere liye kya laaye? \nHusband: Online shopping ka password.",
    38: "Santa: WhatsApp band ho gaya to kya hoga? \nBanta: Log sach bolne lag jayenge!",
    39: "Boy: Tum khush ho? \nGirl: Haan. \nBoy: To fir mera WiFi chhodo!",
    40: "Teacher: Definition of success? \nStudent: Jab result aaye aur mummy smile kare.",
    41: "Friend: Kaisa lag raha hai exam ke baad? \nBoy: Jaise shadi ke baad dulha.",
    42: "Teacher: Mobile kyun use kar rahe ho? \nStudent: Sir alarm band kar raha hoon.",
    43: "Boy: Mere sapne me tu aayi thi. \nGirl: Sapne me bhi jhoot?",
    44: "Boy: Aaj kuch toofani karte hain. \nFriend: Jaake notes pad le!",
    45: "Wife: Mai maa banne wali hoon. \nHusband: WhatsApp pe daal diya kya?",
    46: "Student: Exam me time nahi mila. \nTeacher: Kya kar rahe the? \nStudent: Zindagi ke baare me soch raha tha.",
    47: "Pappu: Mere dad teacher ko google bulate hain. \nGappu: Kyun? \nPappu: Har sawal ka jawab dete hain!",
    48: "Girl: Tum har jagah dikhte ho. \nBoy: Kyunki tumhara wallpaper hoon.",
    49: "Boy: Ghar chalo. \nFriend: Kyu? \nBoy: WiFi weak ho gaya hai.",
    50: "Pappu: Mobile me space nahi hai. \nBantu: To bhabhi ke photo hata de!",
    51: "GF: Aaj kal tum mujhe ignore karte ho \nBF: Arre nahi baby, main toh bas tumhara data save kar raha hoon ",
    52: "Interviewer: Where do you see yourself in 5 years? \nCandidate: In mirror sir, looking older but still jobless",
    53: "Life after engineering: \nResume mein likhte hain “Team Player”… \nReality: PUBG Squad chhod deta hai!",
    54: "Boy: Aunty, Neha ghar pe hai? \nAunty: Haan beta, par online hai. WhatsApp pe mil lo.",
    55: "Pappu: Aaj main apne kaam mein focus karunga. \n5 mins later… Insta, YouTube, fridge, repeat",
    56: "Boss: You're late again! \nEmployee: Sir, neend aur traffic mein se ek toh jhoot hota… maine neend choose ki.",
    57: "Girl: Tum mujhe kab tak yaad rakhoge? \nBoy: Jab tak Google “Did you mean…” dikhana bandh nahi karta! ",          
    58: "Teacher: Tum itne marks kaise laaye? \nStudent: Exam ke pehle light chali gayi thi, mai andhere me hi likh aaya.",
    59: "Pappu: Doctor sahab, jab mai chai peeta hoon to dard hota hai. \nDoctor: Cup se chammach nikaal lo!",
    60: "Santa: Agar koi insaan tumhe do baar bevakoof banaye to? \nBanta: Tisri baar uski shaadi attend mat karna.",
    62: "Boy: Tum itni khubsurat ho, tumse shaadi kaise karu? \nGirl: Pehle bank balance dikhao, fir baat karenge.",
    61: "Doctor: Tumhare pair me fracture hai. \nPatient: Sir, dard to dil me hai."
   
}

def speak_hindi(text):
    
    print(text)
    try:
        # Create Hindi speech 
        tts = gTTS(text=text, lang='hi', slow=False)
        
        # Save to memory instead of file
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Play the audio
        pygame.mixer.music.load(audio_bytes)
        pygame.mixer.music.play()
        
        # Wait until playback finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print("Error in voice generation:", e)

def tell_joke():
    # Tell a random Hindi joke
    joke = jokes_dict[random.randint(1, len(jokes_dict))]
    print("\nJoke:")
    speak_hindi(joke)
    print("-"*20,"😂😂😂","-"*20)

if __name__ == "__main__":
    
    speak_hindi("Ye Raha ek chutakula, dekhte hai aapko hasi aati hai ya nahi!")
    
    # Tell a joke
    tell_joke()
    
    # Ask if user wants another joke
    while True:
        speak_hindi("Kya Aap ek aur chutakula sunna chahoge?")
        user_input = input("Kya Aap ek aur chutakula sunna chahoge? (ha/na): ").lower()
        
        if user_input in ['हाँ', 'yes', 'y', 'haan', 'हां', 'ha']:
            speak_hindi("Theek hai, ek or chutakula hazir hai ")
            tell_joke()
        else:
            speak_hindi("Theek hai, phir milte hain! Hashte rahiye!")
            break

 
 