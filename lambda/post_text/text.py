import json

def lambda_handler(event, context):
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
                "14": "उपयोगकर्ता नाम दर्ज करें",
		"15": "भाषा"
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
                "14": "और देखें",
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
                "14": "Enter Username", 
		"15": "Language"
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