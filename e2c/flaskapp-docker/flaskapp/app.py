"""

IN ORDER TO RUN SERVER, WRITE THESE TWO COMMANDS

export FLASK_APP=app.py
flask run

"""

from flask import Flask, jsonify, request
from backend import communicate
from model import predict
from batch import *
from PIL import Image

import logging
import copy

app = Flask(__name__)
communicate = Communicate()
model = predict.Prediction()
LOG_FILENAME = 'requests.log'



@app.route("/upload", methods=["POST"])
def upload():
    image = request.files.get('image', '')
    crop = request.args["crop"]
    uid = request.args['uid']
    ref = communicate.upload(image, uid)
    disease = model.predict(image, crop)
    communicate.add_image_disease(uid, ref, disease)
    return disease


@app.route("/daily", methods=["POST"])
def daily():
    batch_process(communicate)
    return "true"

@app.route("/link", methods=["POST"])
def send():
    link = request.args['link']
    tokens = {
        'en': [],
        'hi': []
    }
    users = communicate.get_users()
    for user in users:
        # print(user.to_dict())
        try:
            usr = user.to_dict()
            lang = usr['lang']
            token = usr['token']
            tokens[lang].append(token)
            data = {
                "Link" : link
            }
            # communicate.add_daily_disease(user.id, data, 3) 
        except Exception as e:
            pass
    
    english = communicate.send_notifications(tokens["en"], "Please Watch Video", "* It is highly recommended you watch the video we have sent. You will find it in the notification section. ")
      
    hindi = communicate.send_notifications(tokens["hi"], "वीडियो जरूर देखें", "* यह अत्यधिक अनुशंसा है कि आप हमारे द्वारा भेजे गए वीडियो को देखें। यह आपको नोटिफिकेशन सेक्शन में मिलेगा।")

    if english == 0: 
        print("worked")
    else:
        print(len(tokens["en"]))
        print(english)

    if hindi == 0: 
        print("worked")
    else:
        print(len(tokens["hi"]))
        print(hindi)

    return "true"
       
@app.route("/text", methods=["POST"])
def text():
    # with open('./text.json') as f: 
    #     data = json.load(f)
    #     return jsonify(data)
    return {
        "hi" :{
            "DiseaseDetection": {
                "1": "रोग पहचाने",
                "2": "निर्देश",
                "3": "कृपया आप मोबाइल फोन या गैलरी से पौधों के रोगग्रस्त भाग का क्लोज़-अप फोटो लें",
                "4": "इसे रोग की पहचान के लिए अपलोड करें",
                "5": "एक उदाहरण फोटो",
                "6": "कैमरा",
                "7": "गैलरी",
                "8": "रोग पहचाने",
                "9": "इस फसल में। अब इस लिंक पर शामिल हों: ",
                "10": "साझा करें",
                "11": "फसल चुनें",
                "12": "आपके विकल्प हैं"
            },
            "FirstPage": {
                "1": "मौसम की स्थिति: ",
                "2": "आर्द्रता: ",
                "3": "धान",
                "4": "प्रजाति: ",
                "5": "बुवाई की तिथि: ",
                "6": "रोपाई की तिथि: ",
                "7": "स्थान:",
                "8": "स्थान डेटा के बिना, मौसम डेटा उपलब्ध नहीं है",
                "9": "इस लिंक पर अब जयकृषि से जुड़ें: https://play.google.com/store/apps/details?id=com.jaikrishi.appjaikrishi",
                "10": "फसल वर्णन",
                "11": "कम",
                "12": "मध्यम",
                "13": "लंबा",
                "14": "उपयोगकर्ता नाम दर्ज करें"
            },
            "DetectRice": {
                "1": "पता लगाएँ",
                "2": "फोटो से हमने जो  फसल रोग का पता लगाया वह था: ",
                "3": "रोग की रोक-थाम"
            },
            "DetectRandomPicture": {
                "1": "पता लगाएँ",
                "2": "कृपया धान की फोटो भेजें!"
            },
            "CropStatus": {
                "1": "फसल की स्थिति",
                "2": "रोग की चेतावनी",
                "3": "हमारा परामर्श है कि आप अपनी स्वस्थ फसल के लिये, निम्नलिखित उपाय करें",
                "4": "सूखे नर्सरी के लिए, प्रति किलोग्राम बीज में  तीन ग्राम  (3 gm) कार्बेन्डाजिम के साथ बीज का उपचार करें",
                "5": "1 ग्राम कार्बेन्डाजिम प्रति लीटर पानी प्रति किलो बीज में बीज को सोखें ",
                "6": "5 सेन्ट आकार की नर्सरी के लिए, जुताई के दौरान नाइट्रोजेन, फॉस्फोरस, पोटाश प्रत्येक उर्वरक 1 किलोग्राम की दर से डालें",
                "7": "और देखें",
                "8": "पिछला रोग विवरण",
                "9": "आपकी फसल में भूरे रंग के धब्बे का पता चला",
                "10": "और जानें",
                "11": "क्या उपचार कार्य सफल था?",
                "12": "हाँ",
                "13": "नहीं",
                "14": "और देखें"
            },
            "PastDiseaseDetection": {
                "1": "आपकी फसल में भूरे रंग के धब्बे का पता चला",
                "2": "और जानें",
                "3": "क्या उपचार कार्य सफल था?",
                "4": "हाँ",
                "5": "नहीं",
                "6": "आपकी फसल में स्वस्थ धान के पौधे का पता चला!",
                "7": "और जानें!",
                "8": "क्या उपचार कार्य सफल था?",
                "9": "हाँ",
                "10": "नहीं",
                "11": "आपकी फसल में पाया जाने वाला बैक्टीरियल लीफ ब्लाइट",
                "12": "और जानें!",
                "13": "क्या उपचार कार्य सफल था?",
                "14": "हाँ",
                "15": "नहीं"
            },
            "WelcometoJaikrishi": {
                "1": " जयकृषि में आपका स्वागत है",
                "2": "फसल रोग चेतावनी, रोग की खोज और नियंत्रण के लिए आपका मित्र",
                "3": "फसल का चयन करें",
                "4": "छोड़ें",
                "5": "अगला",
                "6": "फसल  चुनें",
                "7": "आपके विकल्प हैं",
                "8": "धान"
            },
            "SeedingLocation": {
                "1": " बुवाई और स्थान",
                "2": "अपनी फसल की बुवाई और रोपाई की तारीखें आपको समय पर फसल रोग की चेतावनी देती रहेगी।",
                "3": "बीज बोने की तिथि  बतायॆ",
                "4": "रोपाई की तिथि बतायॆ",
                "5": " अभी छोड़ें",
                "6": "अगला",
                "7": "आपके विकल्प हैं",
                "8": "धान"
            },
            "VarietyLocation": {
                "1": " प्रजाति और स्थान",
                "2": "बीमारी की चेतावनी प्राप्त करने के लिए अपनी फसल की प्रजाति और अपनी फसल का स्थान बतायॆ।",
                "3": "धान की प्रजाति का चयन करें",
                "4": "फसल का स्थान का चयन करॆ",
                "5": "हो गया",
                "6": "मार्कर को अपनी फसल के स्थान पर खींचें",
                "7": "वर्तमान स्थान आपकी फसल का स्थान है।",
                "8": "त्रुटि:",
                "9": "एक या अधिक क्षेत्र खाली थे। कृपया उन्हें भरें।",
                "10": "धान की प्रजाति चुनें",
                "11": "आपके विकल्प हैं",
                "12": "लघु अवधि",
                "13": "मध्यम अवधि",
                "14": "लम्बा अवधि",
                "15": "फसल का स्थान",
                "16": "आगे बढ़ने के लिए खींचें"
            },
            "SignUp": {
                "1": "आरंभ करें",
                "2": "फोन नंबर",
                "3": "लॉग इन",
                "4": "त्रुटि:",
                "5": "फोन नंबर खाली नहीं हो सकता।",
                "6": "उपयोगकर्ता नाम पहले से ही उपयोग में है।",
                "7": "देश कोड पहले से ही निर्दिष्ट है।",
                "8": "लॉग इन करने में असमर्थ।"
            },
            "edit" : {
                "question" : "अाप क्या बदलना चाहते हैं।",
                "select": "बदलने के लिये इनमॆ से चुनॆ।",
                "loc": "फसल स्थान",
                "variety": "प्रजात", 
                "trans": "रोपाई की तिथि",
                "seed": "बोवाई की तिथि",
                "crop" : "फसल"
            },
            "error": {
                "Address": "पता उपलब्ध नहीं है",
                "loc": "कृपया स्थान जानने की अनुमति दॆ"
            },
            "Crops": {
                "1": "धान"
            },
            "Instructions": {
                "1": "वीडियो निर्देश",
                "2": "और जानें",
                "3": "चरण"
            },
            "History": {
                "based": "चूंकि बुआई से ",
                "days": "  दिन हो चुके हैं, ",  
                "recomend": "हमारा परामर्श है कि आप अपनी स्वस्थ फसल के लिये, निम्नलिखित उपाय करें ",
                "glad": "सुनकर बहुत अच्छा लगा!",
                "unfortunate": "दुर्भाग्यपूर्ण, लेकिन हम अभी भी काम कर रहे हैं",
                "thankyou": "आपके उत्तर के लिए धन्यवाद, हम सुधार करेंगे",
                "noNotifications": "कोइ नया परामर्श नही है !",
                "seeMore": "और देखें",
                "highChance": "एक उच्च संभावना है कि",
                "present": "आपकी फसल में मौजूद है। जितनी जल्दी हो सके अपनी फसल की जांच करें।",
                "detected": "फसल रोग: ",
                "yourCrop": "आपकी फसल में!",
                "work": "क्या उपचार कार्य किया था?",
                "noDetect": "पिछली बीमारियों का पता नहीं चला",
                "warning": "रोग चेतावनी",
                "haventDetect": "अभी तक किसी भी बीमारी का पता नहीं चला है! :)",
                "ok": "ठीक है",
                "warningNotif": " चेतावनी देते हैं कि आपको अपनी फसल को स्वस्थ रखने के लिए निम्नलिखित कदम उठाने की आवश्यकता है: ",
                "warningDisease": " आपकी फसल में मौजूद हो सकता है। कृपया जाँचने के लिए हमारी पहचान सुविधा का उपयोग करें।",
                "warns": " चेतावनी दी है कि ",
                "suggestLink": "हमारा सूझाव है कि आप यह वीडियो देखॆ” वीडियो देखने के लिये कृपया दबायॆ \"और देखॆ\"", 
                "suggestLinkOnPrev": "हमारा सूझाव है कि आप यह वीडियो देखॆ"
            },
            "prevNotifications": {
                "warning": "विगत रोग चेतावनी",
                "noNotifications": "कोइ नया परामर्श नही है!"
            },
            "prevDetections": {
                "noDetected": "अब तक फसल मॆ कोइ रोग नही ",
                "detected": "आपकी फसल के अब तक के सारे रोग",
                "yes": "हाँ",
                "no": "नहीं",
                "thankyou": "आपके उत्तर के लिए धन्यवाद, हम सुधार करेंगे",
                "great": "सुनकर बहुत अच्छा लगा!",
                "unfortunate": "दुर्भाग्यपूर्ण, लेकिन हम अभी भी काम कर रहे हैं"
            }
        }, 
        "en": {
            "DiseaseDetection": {
                "1": "Disease Detection",
                "2": "Instructions",
                "3": "Please take a close-up photo of the diseased part of the plant from you mobile phone or gallery",
                "4": "Upload it for disease detection",
                "5": "An example photo",
                "6": "Camera",
                "7": "Gallery",
                "8": "detected: ",
                "9": " in this crop. Join now at this link: ",
                "10": "Share",
                "11": "Choose Crop",
                "12": "Your Options are "
            },
            "FirstPage": {
                "1": "Weather Condition: ",
                "2": "Humditity: ",
                "3": "Rice",
                "4": "Variety: ",
                "5": "Date of Seeding: ",
                "6": "Date of Transplanting: ",
                "7": "Location: ",
                "8": "Without Location data, weather data is not available",
                "9": "Join JaiKrishi now at this link: https://play.google.com/store/apps/details?id=com.jaikrishi.appjaikrishi",
                "10": "Crop Profile",
                "11": "Short",
                "12": "Medium",
                "13": "Long",
                "14": "Enter Username"
            },
            "DetectRice": {
                "1": "Detect",
                "2": "Detected: ",
                "3": "Disease Treatment"
            },
            "DetectRandomPicture": {
                "1": "Detect",
                "2": "Please send an image of Rice!"
            },
            "CropStatus": {
                "1": "Crop Status",
                "2": "Disease Predictions",
                "3": "Based on the days from seeding, we highly recommend that you do the following steps to make sure that your crop is healthy",
                "4": "Treat Seeds with 3 gm Carbendazim per kg seed for dry Nursery",
                "5": "Soak seed in 1 gm Carbendazim per litre water per kg seed",
                "6": "For 5 cents of Nursery size, apply 1 kg each of Nitrozen, Phosphorous, Potash fertilizer during ploughing",
                "7": "See More",
                "8": "Previous Disease Detections",
                "9": "Disease: Brown Spot in your crop",
                "10": "Learn More",
                "11": "Did the treatment work?",
                "12": "Yes",
                "13": "No",
                "14": "See More"
            },
            "PastDiseaseDetection": {
                "1": "Disease: Brown Spot in your crop",
                "2": "Learn More",
                "3": "Did the treatment work?",
                "4": "Yes",
                "5": "No",
                "6": "Disease: Healthy Rice Plant in your crop!",
                "7": "Learn More!",
                "8": "Did the treatment work?",
                "9": "Yes",
                "10": "No",
                "11": "Disease: Bacterial Leaf Blight in your crop",
                "12": "Learn More!",
                "13": "Did the treatment work?",
                "14": "Yes",
                "15": "No"
            },
            "WelcometoJaikrishi": {
                "1": "Welcome to JaiKrishi",
                "2": "Your friend for  crop disease warning, detection and control.",
                "3": "Select Crop",
                "4": "Skip",
                "5": "Next",
                "6": "Choose Crop",
                "7": "Your options are",
                "8": "Rice"
            },
            "SeedingLocation": {
                "1": "Seeding & Location",
                "2": "Seeding and transplantation dates of your crop would give you timely crop disease alerts.",
                "3": "Enter the date of seeding",
                "4": "Enter the date of transplanting",
                "5": "Skip",
                "6": "Next"
            },
            "VarietyLocation": {
                "1": "Variety & Location",
                "2": "Enter your crop variety and  the location of your crop to get disease alerts.",
                "3": "Select Rice Variety",
                "4": "Edit the crop's location",
                "5": "Done",
                "6": "Drag the Marker to your crop's location",
                "7": "The default location is your crop's device.",
                "8": "Error:",
                "9": "One or more fields were empty. Please fill them out.",
                "10": "Choose Rice Variety",
                "11": "Your options are",
                "12": "Short Duration",
                "13": "Medium Duration",
                "14": "Long Duration",
                "15": "Crop Location",
                "16": "Drag to Move"
            },
            "SignUp": {
                "1": "Get Started",
                "2": "Phone Number",
                "3": "Log In",
                "4": "Error:",
                "5": "Phone Number can not be empty.",
                "6": "Username already in use.",
                "7": "Country Code already specified.",
                "8": "Unable to log in."
            },
            "Crops": {
                "1": "Rice"
            },
            "edit" : {
                "question" : "What would you like to edit?",
                "select": "Select something to edit",
                "loc": "Crop Location", 
                "variety": "Variety", 
                "trans": "Date of Transplanting",
                "seed": "Date of Seeding",
                "crop" :"Crop"
            },
            "error": {
                "Address": "Address is not currently available",
                "loc": "Enable Location Permissions: "
            },
            "Instructions": {
                "1": "Video Instructions",
                "2": "Learn More",
                "3": "Step"
            },
            "History": {
                "based": "Since it has been ",
                "days": " days from sowing, ", 
                "recomend": "we highly recommend that you do the following steps to make sure that your crop is healthy",
                "glad": "Great to hear!",
                "unfortunate": "Unfortunate, but we are still working",
                "thankyou": "Thank you for your input, we will improve",
                "noNotifications": "No notifications to display!",
                "seeMore": "See More",
                "highChance": "There is a high chance that ",
                "present": " is present in your crop. Please check your crop as soon as possible. ",
                "detected": "Crop Disease: ",
                "yourCrop": " in your crop!",
                "work": "Did the treatment work? ",
                "noDetect": "No previous diseases detected",
                "warning": " Disease Warnings",
                "haventDetect": "Haven't detected any diseases yet! :)",
                "ok": "Okay",
                "warningNotif": " warns that you need to do the following steps to keep your crop healthy: ",
                "warningDisease": " might be present in your crop. Please use our detection feature to check.",
                "warns": " warns that ",
                "suggestLink": "We highly recommend that you watch the following video. To view the video in app please click \"See More\"", 
                "suggestLinkOnPrev": "We highly recommend that you watch the following video"
            },
            "prevNotifications": {
                "warning": "Past Disease Warning",
                "noNotifications": "No notifications to display!"
            },
            "prevDetections": {
                "noDetected": "No previous diseases detected",
                "detected": "Past Diseases Detected",
                "yes": "Yes",
                "no": "No",
                "thankyou": "Thank you for your input, we will improve",
                "great": "Great to hear!",
                "unfortunate": "Unfortunate, but we are still working"
            }
        }
    }

@app.route("/reminder", methods=["POST"])
def reminder():
    tokens = {
        'en': [],
        'hi': []
    }
    users = communicate.get_users()
    for user in users:
        try:
            user = user.to_dict()
            lang = user['lang']
            token = user['token']
            tokens[lang].append(token)
        except Exception as e:
            pass
    for key, value in tokens.items():
        if key == 'en':
            english = communicate.send_notifications(tokens[key], 'Reminder', '*Please upload photo if you think your crop has some disease')
            print(english/len(tokens[key]))
        elif key =='hi':
            hindi = communicate.send_notifications(tokens[key], 'अनुस्मारक', '* कृपया फोटो अपलोड करें यदि आपको लगता है कि आपकी फसल में कोई बीमारी है')
            print(hindi/len(tokens[key]))

    return 'true'

@app.route("/newDiseases", methods=["POST"])
def newDiseases():
    return {"hi" : 
            {
            "Leaf Blast": {
                "Disease": "लीफ ब्लास्ट (झौंका)",
                "Step 1": " ट्राईसाइक्लाज़ोल @ 6ग्राम / 10 ली0  पानी की दर से छिड़काव करे।",
                "Step 2": "यूरिया का प्रयोग बिलकुल न करें, यूरिया तभी डालॆ जब लीफ कलर कार्ड सुझाव दे  वह भी दवा डालने के 7 दिनों के बाद। ",
                "Step 3": "फसल अवशेष नष्ट करें",
                "Link": "https://youtu.be/QSSAr56AdD8",
                "Image": "https://i1.wp.com/agfax.com/wp-content/uploads/rice-blast-leaf-lesions-lsu.jpg?fit=600%2C400&ssl=1"

            },
            "BLB": {
                "Disease": "बैक्टीरियल लीफ ब्लाइट",
                "Step 1": "स्ट्रेप्टोमाइसिन सल्फेट एवं टेट्रासाइक्लिन को (साथ मिलाकर) 300 ग्राम + कॉपर ऑक्सीक्लोराइड 1.25 किग्रा / हेक्टेयर की दर से छिड़काव करें। यदि आवश्यक हो तो 15 दिन बाद फिर दवा छिङकॆ।",
                "Step 2": "गब्भा अवस्था के पहले यदि रोग हो, तो खेत से पानी निकाल दें",
                "Step 3": "3-4 दिनों के लिए खेत को सूखने दें",
                "Link": "https://youtu.be/C44FxCu7ubo",
		"Image": "https://m.farms.com/Portals/0/bacterial-leaf-blight-300-1_1.png"
            },
            "False Smut": {
                "Disease": " आभाषी कंड (कंडवा या हरदी)",
                "Step 1": "7 दिनों के अंतराल पर हेक्साकोनाज़ोल @ 1.0 मिली / लीटर पानी का 2 बार छिङकाव करें",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/zxbcXWJ6cTA",
		"Image": "https://www.lsuagcenter.com/~/media/system/9/4/a/e/94ae4909bab82f9b5def7eabc3bb6983/falsesmut4.jpg"
            },
            "Brown Spot": {
                "Disease": " भूरा धब्बा ",
                "Step 1": "पोटाश का छिङकाव  करॆ और  प्रोपिकोनाज़ोल @ 1.0 ग्राम या क्लोरोथालोनिल@2.0 ग्राम प्रति लीटर पानी में डालें या  ट्राइसाइक्लाजोल 18% + मानोकोजेब 62% WP 1.0 कि ग्रा  प्रति हेक्टेयर डालॆ,  और 10-12 दिनों के बाद दोहराएं यदि लक्षण बने रहें",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/AxFCqZFwDQo",
		"Image": "https://www.indogulfbioag.com/Rice-Protect-Kits/images/brown-spot-big.jpg"

            },
            "Sheath Blight": {
                "Disease": "शीथ ब्लाइट या पर्ण अंगमारी",
                "Step 1": "यूरिया का प्रयोग बिलकुल न करें, यूरिया तभी डालॆ जब लीफ कलर कार्ड सुझाव दे  वह भी दवा डालने के 7 दिनों के बाद",
                "Step 2": "कार्बेन्डाजिम @ 1.0 ग्राम या प्रोपिकोनाजोल @ 1.0 मिली या हेक्साकोनाजोल @ 1.0 मिली प्रति लीटर पर्ण स्प्रे के रूप में। अगर लक्षण बने रहें तो 10-15 दिन बाद दोहराएं",
                "Step 3": "",
                "Link": "https://youtu.be/gLPX_2QcdqM",
		"Image": "https://www.apsnet.org/edcenter/disandpath/fungalasco/pdlessons/Article%20Images/RiceSheathFig5.jpg"
            },
            "ZnDf": {
                "Disease": "खैरा",
                "Step 1": "0.5% जिंक सल्फेट का छिङकाव (10 लीटर पानी में 25 ग्राम जिंक सल्फेट)। जिंक सल्फेट हेक्टाहाइड्रेट के 25 किग्रा / हेक्टेयर या 16 किलोग्राम / हेक्टेयर जिंक सल्फेट मोनोहाइड्रेट का प्रयोग करें।",
                "Step 2": "0.5% जिंक सल्फेट का छिङकाव (10 लीटर पानी में 25 ग्राम जिंक सल्फेट)",
                "Step 3": "",
                "Link": "https://youtu.be/tbsOs9POhVk",
		"Image": "https://lariceman.files.wordpress.com/2010/06/bronzing-6-10-2.jpg"
            },

            "Sheath Rot": {
                "Disease": "शीथ रोट",
                "Step 1": "कार्बेन्डाजिम @ 250 ग्राम या प्रोपिकोनाजोल @ 2.0 मिली या क्लोरोथैलोनिल @ 1.0 किलोग्राम या इडिफेनफोस प्रति लीटर  प्रति हेक्टेयर का छिङकाव करॆ। अगर लक्षण बने रहें तो 10-15 दिन बाद दोहराएं",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://www.youtube.com/watch?v=Dqv1jAGLViU",
                "Image": "https://www.gardeningknowhow.com/wp-content/uploads/2019/07/sheath-rot.jpg"
            },
	   "PaddyField": {
		"Disease" : "कृपया रोगी पौधे की पास से फोटो लॆ।",
		"Step 1" : "", 
		"Step 2": "", 
		"Step 3": "",
		"Link" : "",
		"Image": "",
	   },
            "This is not rice": {
                "Disease": "कृपया धान की एक फोटो भेजें!",
                "Step 1": "",
                "Step 2": "",
                "Step 3": "",
                "Link": ""
            },
            "Image is unclear. Please try again": {
                "Disease": "छवि अस्पष्ट है। कृपया पुनः प्रयास करें"
            },
            "Healthy": {
                "Disease": "स्वस्थ धान का पौधा!"
            }
        },
    
        "en": {
            "Leaf Blast": {
                "Disease": "Leaf Blast",
                "Step 1": "Apply Tricyclazole @ 6gm/10L water",
                "Step 2": "Do not apply urea. Apply after 7 days of blast treatment, only if LCC recommends",
                "Step 3": "Destroy debris post harvest",
                "Link": "https://youtu.be/QSSAr56AdD8",
                "Image": "https://i1.wp.com/agfax.com/wp-content/uploads/rice-blast-leaf-lesions-lsu.jpg?fit=600%2C400&ssl=1"
            },
            "BLB": {
                "Disease": "Bacterial Leaf Blight",
                "Step 1": "Spray Streptomycin sulphate + Tetracycline combination 300 g + Copper oxychloride 1.25kg/ha. If necessary repeat 15 days later.",
                "Step 2": "Drain the field if in vegetative stage",
                "Step 3": "Leave the field dry for 3-4 days",
                "Link": "https://youtu.be/C44FxCu7ubo",
		"Image": "https://m.farms.com/Portals/0/bacterial-leaf-blight-300-1_1.png"
            },
            "False Smut": {
                "Disease": "FalseSmut",
                "Step 1": "2 times spray of hexaconazole @ 1.0ml/ litre water at 7 days interval",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/zxbcXWJ6cTA",
		"Image": "https://www.lsuagcenter.com/~/media/system/9/4/a/e/94ae4909bab82f9b5def7eabc3bb6983/falsesmut4.jpg"
            },
            "Brown Spot": {
                "Disease": "Brown Spot",
                "Step 1": "Apply PotashSpray Propiconazole@1.0 gm or Chlorothalonil@2.0 gm per litre of water or Tricyclazole 18% + Manocozeb 62% WP 1000- 1250 gm per Hectare and repeat after 10-12 days if symptoms persist",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/AxFCqZFwDQo",
		"Image": "https://www.indogulfbioag.com/Rice-Protect-Kits/images/brown-spot-big.jpg"
            },
            "Sheath Blight": {
                "Disease": "Sheath Blight",
                "Step 1": "Do not apply urea after detection till recommended by LCC",
                "Step 2": "Carbendazim @ 1.0 gm or Propiconazole @ 1.0 ml or Hexaconazole @ 1.0 ml per itre as foliar spray. Repeat after 15 days",
                "Step 3": "",
                "Link": "https://youtu.be/gLPX_2QcdqM",
		"Image": "https://www.apsnet.org/edcenter/disandpath/fungalasco/pdlessons/Article%20Images/RiceSheathFig5.jpg"
            },
            "ZnDf": {
                "Disease": "Khaira",
                "Step 1": "25 kg/Hectare of Zinc Sulphate HectaHydrate or 16 Kg/ Hectare Zinc Sulphate Monohydrate.",
                "Step 2": "Spray of 0.5% Zinc Sulphate (25 gm Zinc Sulphate in 10 lit of water)",
                "Step 3": "",
                "Link": "https://youtu.be/tbsOs9POhVk",
		"Image":"https://lariceman.files.wordpress.com/2010/06/bronzing-6-10-2.jpg"
            },

            "Sheath Rot": {
                "Disease": "Sheath Rot",
                "Step 1": "Sprinkle carbendazim @ 250 g or propiconazole @ 2.0 ml or chlorothalonil @ 1.0 kg or idiphenphos   per liter per hectare. Repeat after 10-15 days if symptoms persist.",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://www.youtube.com/watch?v=Dqv1jAGLViU",
                "Image": "https://www.gardeningknowhow.com/wp-content/uploads/2019/07/sheath-rot.jpg"   
            },
	"PaddyField": {
                "Disease" : "Please take a close-up photo of the affected plant part",
                "Step 1" : "", 
                "Step 2": "", 
                "Step 3": "",
                "Link" : "",
                "Image": "",
           },
            "This is not rice": {
                "Disease": "Please send an image of Rice!",
                "Step 1": "",
                "Step 2": "",
                "Step 3": "",
                "Link": ""
            },
            "Image is unclear. Please try again": {
                "Disease": "Image is unclear. Please try again"
            },
            "Healthy": {
                "Disease": "Healthy Rice Plant!"
            }
        }
    }


@app.route("/diseases", methods=["POST"])
def diseases():
    lang = request.args["loc"]
    uid = request.args['uid']
    if uid != "":
        user = communicate.get_user(uid)
        communicate.update_document(user, {
            "lang": lang
        })
    if lang == "hi":
        return {
            "Leaf Blast": {
                "Disease": "लीफ ब्लास्ट (झौंका)",
                "Step 1": " ट्राईसाइक्लाज़ोल @ 6ग्राम / 10 ली0  पानी की दर से छिड़काव करे।",
                "Step 2": "यूरिया का प्रयोग बिलकुल न करें, यूरिया तभी डालॆ जब लीफ कलर कार्ड सुझाव दे  वह भी दवा डालने के 7 दिनों के बाद। ",
                "Step 3": "फसल अवशेष नष्ट करें",
                "Link": "https://youtu.be/QSSAr56AdD8",
                "Image": "https://i1.wp.com/agfax.com/wp-content/uploads/rice-blast-leaf-lesions-lsu.jpg?fit=600%2C400&ssl=1"

            },
            "BLB": {
                "Disease": "बैक्टीरियल लीफ ब्लाइट",
                "Step 1": "स्ट्रेप्टोमाइसिन सल्फेट एवं टेट्रासाइक्लिन को (साथ मिलाकर) 300 ग्राम + कॉपर ऑक्सीक्लोराइड 1.25 किग्रा / हेक्टेयर की दर से छिड़काव करें। यदि आवश्यक हो तो 15 दिन बाद फिर दवा छिङकॆ।",
                "Step 2": "गब्भा अवस्था के पहले यदि रोग हो, तो खेत से पानी निकाल दें",
                "Step 3": "3-4 दिनों के लिए खेत को सूखने दें",
                "Link": "https://youtu.be/C44FxCu7ubo",
                "Image": "data:image/jpeg;base64,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"
            },
            "False Smut": {
                "Disease": " आभाषी कंड (कंडवा या हरदी)",
                "Step 1": "7 दिनों के अंतराल पर हेक्साकोनाज़ोल @ 1.0 मिली / लीटर पानी का 2 बार छिङकाव करें",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/zxbcXWJ6cTA",
                "Image": "data:image/jpeg;base64,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"

            },
            "Brown Spot": {
                "Disease": " भूरा धब्बा ",
                "Step 1": "पोटाश का छिङकाव  करॆ और  प्रोपिकोनाज़ोल @ 1.0 ग्राम या क्लोरोथालोनिल@2.0 ग्राम प्रति लीटर पानी में डालें या  ट्राइसाइक्लाजोल 18% + मानोकोजेब 62% WP 1.0 कि ग्रा  प्रति हेक्टेयर डालॆ,  और 10-12 दिनों के बाद दोहराएं यदि लक्षण बने रहें",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/AxFCqZFwDQo",
                "Image": "data:image/jpeg;base64,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"

            },
            "Sheath Blight": {
                "Disease": "शीथ ब्लाइट या पर्ण अंगमारी",
                "Step 1": "यूरिया का प्रयोग बिलकुल न करें, यूरिया तभी डालॆ जब लीफ कलर कार्ड सुझाव दे  वह भी दवा डालने के 7 दिनों के बाद",
                "Step 2": "कार्बेन्डाजिम @ 1.0 ग्राम या प्रोपिकोनाजोल @ 1.0 मिली या हेक्साकोनाजोल @ 1.0 मिली प्रति लीटर पर्ण स्प्रे के रूप में। अगर लक्षण बने रहें तो 10-15 दिन बाद दोहराएं",
                "Step 3": "",
                "Link": "https://youtu.be/gLPX_2QcdqM",
                "Image": "data:image/jpeg;base64,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"

            },
            "ZnDf": {
                "Disease": "खैरा",
                "Step 1": "0.5% जिंक सल्फेट का छिङकाव (10 लीटर पानी में 25 ग्राम जिंक सल्फेट)। जिंक सल्फेट हेक्टाहाइड्रेट के 25 किग्रा / हेक्टेयर या 16 किलोग्राम / हेक्टेयर जिंक सल्फेट मोनोहाइड्रेट का प्रयोग करें।",
                "Step 2": "0.5% जिंक सल्फेट का छिङकाव (10 लीटर पानी में 25 ग्राम जिंक सल्फेट)",
                "Step 3": "",
                "Link": "https://youtu.be/tbsOs9POhVk",
                "Image": "data:image/jpeg;base64,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"
            },

            "Sheath Rot": {
                "Disease": "शीथ रोट",
                "Step 1": "कार्बेन्डाजिम @ 250 ग्राम या प्रोपिकोनाजोल @ 2.0 मिली या क्लोरोथैलोनिल @ 1.0 किलोग्राम या इडिफेनफोस प्रति लीटर  प्रति हेक्टेयर का छिङकाव करॆ। अगर लक्षण बने रहें तो 10-15 दिन बाद दोहराएं",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://www.youtube.com/watch?v=Dqv1jAGLViU",
                "Image": "https://www.gardeningknowhow.com/wp-content/uploads/2019/07/sheath-rot.jpg"
            },
"PaddyField": {
                "Disease" : "कृपया रोगी पौधे की पास से फोटो लॆ।",
                "Step 1" : "", 
                "Step 2": "", 
                "Step 3": "",
                "Link" : "",
                "Image": "",
           },
            "This is not rice": {
                "Disease": "कृपया धान की एक फोटो भेजें!",
                "Step 1": "",
                "Step 2": "",
                "Step 3": "",
                "Link": ""
            },
            "Image is unclear. Please try again": {
                "Disease": "छवि अस्पष्ट है। कृपया पुनः प्रयास करें"
            },
            "Healthy": {
                "Disease": "स्वस्थ धान का पौधा!"
            }
        }
    elif lang == "en":
        return {
            "Leaf Blast": {
                "Disease": "Leaf Blast",
                "Step 1": "Apply Tricyclazole @ 6gm/10L water",
                "Step 2": "Do not apply urea. Apply after 7 days of blast treatment, only if LCC recommends",
                "Step 3": "Destroy debris post harvest",
                "Link": "https://youtu.be/QSSAr56AdD8",
                "Image": "https://i1.wp.com/agfax.com/wp-content/uploads/rice-blast-leaf-lesions-lsu.jpg?fit=600%2C400&ssl=1"
            },
            "BLB": {
                "Disease": "Bacterial Leaf Blight",
                "Step 1": "Spray Streptomycin sulphate + Tetracycline combination 300 g + Copper oxychloride 1.25kg/ha. If necessary repeat 15 days later.",
                "Step 2": "Drain the field if in vegetative stage",
                "Step 3": "Leave the field dry for 3-4 days",
                "Link": "https://youtu.be/C44FxCu7ubo",
                "Image": "data:image/jpeg;base64,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"
            },
            "False Smut": {
                "Disease": "FalseSmut",
                "Step 1": "2 times spray of hexaconazole @ 1.0ml/ litre water at 7 days interval",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/zxbcXWJ6cTA",
                "Image": "data:image/jpeg;base64,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"
            },
            "Brown Spot": {
                "Disease": "Brown Spot",
                "Step 1": "Apply PotashSpray Propiconazole@1.0 gm or Chlorothalonil@2.0 gm per litre of water or Tricyclazole 18% + Manocozeb 62% WP 1000- 1250 gm per Hectare and repeat after 10-12 days if symptoms persist",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://youtu.be/AxFCqZFwDQo",
                "Image": "data:image/jpeg;base64,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"
            },
            "Sheath Blight": {
                "Disease": "Sheath Blight",
                "Step 1": "Do not apply urea after detection till recommended by LCC",
                "Step 2": "Carbendazim @ 1.0 gm or Propiconazole @ 1.0 ml or Hexaconazole @ 1.0 ml per itre as foliar spray. Repeat after 15 days",
                "Step 3": "",
                "Link": "https://youtu.be/gLPX_2QcdqM",
                "Image": "data:image/jpeg;base64,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"
            },
            "ZnDf": {
                "Disease": "Khaira",
                "Step 1": "25 kg/Hectare of Zinc Sulphate HectaHydrate or 16 Kg/ Hectare Zinc Sulphate Monohydrate.",
                "Step 2": "Spray of 0.5% Zinc Sulphate (25 gm Zinc Sulphate in 10 lit of water)",
                "Step 3": "",
                "Link": "https://youtu.be/tbsOs9POhVk",
                "Image": "data:image/jpeg;base64,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"
            },

            "Sheath Rot": {
                "Disease": "Sheath Rot",
                "Step 1": "Sprinkle carbendazim @ 250 g or propiconazole @ 2.0 ml or chlorothalonil @ 1.0 kg or idiphenphos   per liter per hectare. Repeat after 10-15 days if symptoms persist.",
                "Step 2": "",
                "Step 3": "",
                "Link": "https://www.youtube.com/watch?v=Dqv1jAGLViU",
                "Image": "https://www.gardeningknowhow.com/wp-content/uploads/2019/07/sheath-rot.jpg"
            },
	"PaddyField": {
                "Disease" : "Please take a close-up photo of the affected plant part",
                "Step 1" : "", 
                "Step 2": "", 
                "Step 3": "",
                "Link" : "",
                "Image": "",
           },
            "This is not rice": {
                "Disease": "Please send an image of Rice!",
                "Step 1": "",
                "Step 2": "",
                "Step 3": "",
                "Link": ""
            },
            "Image is unclear. Please try again": {
                "Disease": "Image is unclear. Please try again"
            },
            "Healthy": {
                "Disease": "Healthy Rice Plant!"
            }
        }


if __name__ == "__main__":
    app.run()
