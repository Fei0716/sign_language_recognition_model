# data for fine-tuning: to improve the performance of the model for specific tasks
# List of actions detected by the sign language model
sign_language_actions = [
    'Hi', 'Saya Sayang Awak', 'Makan', 'Selamat Malam', 'Terima Kasih', 'Apa Khabar',
    'Awak', 'Saya', 'Minum', 'Salah', 'Betul', 'Minta Maaf', 'Tolong', 'Hijau',
    'Kita', 'Mereka', 'Ini', 'Itu', 'Apa', 'Siapa', 'Ini Di Luar Pengetahuan Saya'
]

diverse_training_data = [
    {
        "text_input": "What is EchoSign?", 
        "output": "EchoSign is an AI-driven online meeting platform that translates Malaysian Sign Language (BIM) in real-time, enabling seamless communication for the deaf and hard-of-hearing community."
    },
    {
        "text_input": "Can you explain what EchoSign is?", 
        "output": "EchoSign is an AI-driven online meeting platform that translates Malaysian Sign Language (BIM) in real-time, enabling seamless communication for the deaf and hard-of-hearing community."
    },
    {
        "text_input": "Tell me about EchoSign.", 
        "output": "EchoSign is an AI-driven online meeting platform that translates Malaysian Sign Language (BIM) in real-time, enabling seamless communication for the deaf and hard-of-hearing community."
    },
    {
        "text_input": "What does BIM mean?", 
        "output": "BIM stands for Bahasa Isyarat Malaysia, which is Malaysian Sign Language."
    },
    {
        "text_input": "What is the meaning of BIM?",
        "output": "BIM stands for Bahasa Isyarat Malaysia, which is Malaysian Sign Language."
    },
    {
        "text_input": "Can you define BIM?", 
        "output": "BIM stands for Bahasa Isyarat Malaysia, which is Malaysian Sign Language."
    },
    {
        "text_input": "What is the purpose of EchoSign?", 
        "output": "The purpose of EchoSign is to bridge communication barriers by recognizing Malaysian Sign Language (BIM) gestures and displaying the detected actions as text in real-time."
    },
    {
        "text_input": "Why was EchoSign created?", 
        "output": "The purpose of EchoSign is to bridge communication barriers by recognizing Malaysian Sign Language (BIM) gestures and displaying the detected actions as text in real-time."
    },
    {
        "text_input": "What is EchoSign’s goal?", 
        "output": "The purpose of EchoSign is to bridge communication barriers by recognizing Malaysian Sign Language (BIM) gestures and displaying the detected actions as text in real-time."
    },
    {
        "text_input": "How does the sign language recognition model work?", 
        "output": "The platform uses Temporal Convolutional Network (TCN) to recognize Malaysian Sign Language (BIM) gestures in real-time."
    },
    {
        "text_input": "Can you describe how sign language recognition functions?", 
        "output": "The platform uses Temporal Convolutional Network (TCN) to recognize Malaysian Sign Language (BIM) gestures in real-time."
    },
    {
        "text_input": "What powers the sign language detection?", 
        "output": "The platform uses Temporal Convolutional Network (TCN) to recognize Malaysian Sign Language (BIM) gestures in real-time."
    },
    {
        "text_input": "What are the features of the admin portal?", 
        "output": "The admin portal allows tracking analytics such as user engagement and key metrics."
    },
    {
        "text_input": "What does the admin portal do?", 
        "output": "The admin portal allows tracking analytics such as user engagement and key metrics."
    },
    {
        "text_input": "Can you explain the admin portal functionality?", 
        "output": "The admin portal allows tracking analytics such as user engagement and key metrics."
    },
    {
        "text_input": "What are some of the recognized sign language actions?", 
        "output": "Currently, the model can recognize 21 actions such as 'Hi', 'Saya Sayang Awak', 'Makan', 'Selamat Malam', and 'Terima Kasih'."
    },
    {
        "text_input": "Which sign language gestures can EchoSign detect?", 
        "output": "Currently, the model can recognize 21 actions such as 'Hi', 'Saya Sayang Awak', 'Makan', 'Selamat Malam', and 'Terima Kasih'."
    },
    {
        "text_input": "What actions are recognized by the sign language model?", 
        "output": "Currently, the model can recognize 21 actions such as 'Hi', 'Saya Sayang Awak', 'Makan', 'Selamat Malam', and 'Terima Kasih'."
    },
    {
        "text_input": "What is the meeting interface like?", 
        "output": "The meeting interface includes sections for video, recognized gestures displayed as text, and intuitive controls for users."
    },
    {
        "text_input": "Describe the interface of EchoSign.", 
        "output": "The meeting interface includes sections for video, recognized gestures displayed as text, and intuitive controls for users."
    },
    {
        "text_input": "How does the meeting interface look?", 
        "output": "The meeting interface includes sections for video, recognized gestures displayed as text, and intuitive controls for users."
    },
    {
        "text_input": "What are all the actions the sign language model can detect?", 
        "output": f"The model can detect the following actions: {', '.join(sign_language_actions)}."
    },
    {
        "text_input": "List the actions recognized by the sign language model.", 
        "output": f"The model can detect the following actions: {', '.join(sign_language_actions)}."
    },
    {
        "text_input": "Can you provide the full list of recognized sign language gestures?", 
        "output": f"The model can detect the following actions: {', '.join(sign_language_actions)}."
    },
    {
        "text_input": "Which gestures does the platform support?", 
        "output": f"The model can detect the following actions: {', '.join(sign_language_actions)}."
    },
    {
        "text_input": "What signs are identified by the recognition model?", 
        "output": f"The model can detect the following actions: {', '.join(sign_language_actions)}."
    },
    {
        "text_input": "How do I enable the sign language recognition model?",
        "output": "The feature can be toggled on by clicking on the button with the sign language icon, located below the toggle mic button and the end meeting button."
    },
    {
        "text_input": "Where is the option to turn on the sign language recognition?",
        "output": "The feature can be toggled on by clicking on the button with the sign language icon, located below the toggle mic button and the end meeting button."
    },
    {
        "text_input": "How can I activate the sign language recognition feature?",
        "output": "The feature can be toggled on by clicking on the button with the sign language icon, located below the toggle mic button and the end meeting button."
    },
    {
        "text_input": "Is there a way to enable the sign language function?",
        "output": "The feature can be toggled on by clicking on the button with the sign language icon, located below the toggle mic button and the end meeting button."
    },
    {
        "text_input": "How can I turn on the BIM recognition mode?",
        "output": "The feature can be toggled on by clicking on the button with the sign language icon, located below the toggle mic button and the end meeting button."
    },
        {
        "text_input": "What are the features of EchoSign?",
        "output": "EchoSign includes features such as real-time Malaysian Sign Language (BIM) recognition, an AI chatbot for assistance, an admin portal for analytics, and a user-friendly video meeting interface."
    },
    {
        "text_input": "Can you list the features available on the platform?",
        "output": "The platform offers real-time Malaysian Sign Language recognition, AI chatbot support, an admin portal for user analytics, and an intuitive video meeting interface."
    },
    {
        "text_input": "What functionalities are included in EchoSign?",
        "output": "EchoSign provides real-time BIM recognition, an AI chatbot for user support, an admin portal for tracking engagement and metrics, and a seamless video meeting platform."
    },
    {
        "text_input": "What makes EchoSign unique?",
        "output": "EchoSign bridges communication barriers with real-time Malaysian Sign Language recognition, an AI-powered chatbot for assistance, and a user-friendly meeting interface."
    },
    {
        "text_input": "What tools does EchoSign offer for communication?",
        "output": "EchoSign offers real-time sign language recognition, a chatbot for support, and a robust admin portal for analytics."
    },
    {
        "text_input": "What are the key features of EchoSign?",
        "output": "Key features include Malaysian Sign Language recognition, AI chatbot support, an analytics admin portal, and an intuitive video meeting interface."
    },
    {
        "text_input": "Can you explain the main functionalities of the platform?",
        "output": "EchoSign supports real-time BIM recognition, an AI chatbot, a meeting interface for seamless communication, and an admin portal for monitoring engagement."
    },
    {
        "text_input": "What are the highlights of EchoSign’s features?",
        "output": "Highlights include real-time Malaysian Sign Language recognition, AI chatbot assistance, and tools for user analytics."
    },
    {
        "text_input": "What does the EchoSign platform include?",
        "output": "EchoSign includes sign language recognition, AI chatbot support, an admin portal, and a meeting interface designed for all users."
    },
    {
        "text_input": "How does EchoSign support communication?",
        "output": "EchoSign supports communication through its Malaysian Sign Language recognition model, AI chatbot, and a user-friendly video meeting interface."
    },
        {
        "text_input": "Who developed EchoSign?",
        "output": "EchoSign was developed by Members of Group 7 for Workshop 2: Fei, Nik Faruq, Thavaness, and Fazreen."
    },
    {
        "text_input": "Who created this platform?",
        "output": "EchoSign was developed by Members of Group 7 for Workshop 2: Fei, Nik Faruq, Thavaness, and Fazreen."
    },
    {
        "text_input": "Why is TCN used in this system?",
        "output": "TCN (Temporal Convolutional Network) is used because it offers faster inference and training speed, and achieves higher accuracy scores compared to other deep learning methods for sign language recognition."
    },
    {
        "text_input": "What are the advantages of using TCN?",
        "output": "TCN provides faster inference and training speed, and achieves higher accuracy scores for sign language recognition compared to other deep learning methods."
    },
    {
        "text_input": "How can I contact support?",
        "output": "For inquiries or complaints about the system, you can contact B032320066@student.utem.edu.my"
    },
    {
        "text_input": "Where can I report issues?",
        "output": "For inquiries or complaints about the system, you can contact B032320066@student.utem.edu.my"
    },
    {
        "text_input": "How do I change my input settings?",
        "output": "You can change input settings like microphone or webcam by clicking the settings button (nut icon) at the bottom left of the page."
    },
    {
        "text_input": "Where are the input settings?",
        "output": "You can change input settings like microphone or webcam by clicking the settings button (nut icon) at the bottom left of the page."
    },
    {
        "text_input": "How do I turn off my camera?",
        "output": "You can toggle your webcam on/off using the webcam button located above the microphone toggle button."
    },
    {
        "text_input": "How do I disable my camera?",
        "output": "You can toggle your webcam on/off using the webcam button located above the microphone toggle button."
    },
    {
        "text_input": "How do I mute myself?",
        "output": "You can toggle your microphone on/off using the microphone button located below the webcam toggle button."
    },
    {
        "text_input": "How do I turn off my mic?",
        "output": "You can toggle your microphone on/off using the microphone button located below the webcam toggle button."
    },
    {
        "text_input": "How do I exit the meeting?",
        "output": "You can leave the meeting by pressing the end call button located below the toggle sign language recognition button."
    },
    {
        "text_input": "How do I end the call?",
        "output": "You can leave the meeting by pressing the end call button located below the toggle sign language recognition button."
    },
    {
        "text_input": "Where can I see the predicted signs?",
        "output": "Click the arrow button at the top right of the user using sign language recognition to see the five most recent predicted sign language actions."
    },
    {
        "text_input": "How do I view recent predictions?",
        "output": "Click the arrow button at the top right of the user using sign language recognition to see the five most recent predicted sign language actions."
    },
    {
        "text_input": "How can I add participants?",
        "output": "Participants can join using a shared meeting link (click the share button to copy) or by entering the room ID on the home page's join meeting button."
    },
    {
        "text_input": "How do I invite others?",
        "output": "Participants can join using a shared meeting link (click the share button to copy) or by entering the room ID on the home page's join meeting button."
    },
    {
        "text_input": "What makes TCN better for sign language recognition?",
        "output": "TCN is optimal for sign language recognition because it processes temporal sequences efficiently, handles variable-length inputs well, and maintains stable gradients during training compared to other deep learning methods."
    },
    {
        "text_input": "What are the technical benefits of TCN?",
        "output": "TCN provides parallel processing capabilities, stable gradient flow, and efficient temporal dependency learning, making it ideal for real-time sign language recognition."
    },
    {
        "text_input": "How does TCN improve the system?",
        "output": "TCN enhances the system through faster processing speeds, better temporal feature extraction, and improved accuracy in real-time sign language recognition."
    },
    {
        "text_input": "What should I do if sign language recognition isn't working?",
        "output": "Ensure you're well-lit and centered in the frame, check if the feature is toggled on, and try refreshing the page if issues persist."
    },
    {
        "text_input": "How can I improve sign language detection accuracy?",
        "output": "Ensure good lighting, face the camera directly, make clear gestures, and maintain a steady position within the frame for better recognition."
    },
    {
        "text_input": "What's the best way to use sign language recognition?",
        "output": "Position yourself in good lighting, face the camera directly, make clear gestures, and ensure the sign language recognition feature is toggled on."
    },
    {
        "text_input": "How do I share my screen?",
        "output": "Click the screen share icon in the bottom toolbar, then select which window or application you want to share with other participants."
    },
    {
        "text_input": "Can I present my screen?",
        "output": "Yes, use the screen share feature by clicking the screen share icon in the bottom toolbar and selecting your desired window or application."
    },
    {
        "text_input": "How do I stop sharing my screen?",
        "output": "Click the 'Stop Sharing' button that appears at the top of your screen when you're actively sharing, or click the screen share icon again."
    },
    {
        "text_input": "What if my microphone isn't working?",
        "output": "Check if your microphone is properly connected, selected in the audio settings menu, and not muted in your system settings or the meeting interface."
    },
    {
        "text_input": "How do I fix audio issues?",
        "output": "Check your audio settings in the settings menu, ensure the correct microphone is selected, and verify it's not muted in system settings."
    },
    {
        "text_input": "What browsers support EchoSign?",
        "output": "EchoSign works best on Chrome, Firefox, and Edge browsers with the latest updates installed for optimal performance."
    },
    {
        "text_input": "Is EchoSign compatible with my browser?",
        "output": "EchoSign is compatible with Chrome, Firefox, and Edge browsers. Please ensure your browser is updated to the latest version."
    },
        {
        "text_input": "How should I position my camera for sign language detection?",
        "output": "Position your webcam to fully capture your upper body, including your complete arms and hands, for accurate sign language recognition."
    },
    {
        "text_input": "Why isn't the model detecting my signs correctly?",
        "output": "Ensure your webcam captures your entire upper body, including full arms and hands. Incomplete visibility of these areas will reduce recognition accuracy."
    },
    {
        "text_input": "What's the correct camera position for sign language?",
        "output": "Position yourself so your upper body, including complete arms and hands, is fully visible in the webcam frame for accurate sign detection."
    },
    {
        "text_input": "How do I improve sign language detection?",
        "output": "Ensure your webcam fully captures your upper body, including complete arms and hands. Maintain good lighting and make clear gestures."
    },
    {
        "text_input": "What's the proper framing for sign language recognition?",
        "output": "Your webcam should capture your entire upper body, with full visibility of arms and hands for optimal sign language recognition."
    },
    {
        "text_input": "Can I use EchoSign on mobile?",
        "output": "Currently, EchoSign is optimized for desktop/laptop use to ensure accurate sign language recognition and best video quality."
    },
    {
        "text_input": "Does EchoSign work on tablets?",
        "output": "EchoSign is designed for desktop/laptop use. Mobile devices may not provide optimal performance for sign language recognition."
    },
    {
        "text_input": "What lighting is best for sign language recognition?",
        "output": "Use even, front-facing lighting that clearly illuminates your upper body, arms, and hands without creating shadows."
    },
    {
        "text_input": "How do I get better lighting?",
        "output": "Position yourself facing a light source and avoid backlighting. Natural daylight or a desk lamp in front of you works well."
    },
    {
        "text_input": "What's the correct webcam position?",
        "output": "Place your webcam slightly elevated and position yourself 50-60cm away to ensure full visibility of your upper body."
    },
    {
        "text_input": "How should I set up my camera?",
        "output": "Set your webcam at a slightly elevated position and sit 50-60cm away for optimal sign language recognition."
    },
       {
        "text_input": "What should I do if the model isn't detecting my signs?",
        "output": "Check that you're 50-60cm from the webcam, ensure full visibility of upper body and hands, maintain good lighting, and make clear gestures."
    },
    {
        "text_input": "When does sign language detection work best?",
        "output": "Sign language detection works best with proper distance (50-60cm from webcam), good lighting, clear background, and when your upper body and hands are fully visible."
    },
    {
        "text_input": "Do I need special equipment?",
        "output": "No special equipment needed, just a standard webcam positioned slightly elevated and 50-60cm away from you with good lighting."
    },
    {
        "text_input": "What are common recognition errors?",
        "output": "Common errors occur from incorrect distance (should be 50-60cm), poor lighting, partially visible hands/arms, or rapid movements."
    },
    {
        "text_input": "How to improve recognition accuracy?",
        "output": "Maintain 50-60cm distance, ensure good lighting, make deliberate gestures, and keep your upper body fully visible in the frame."
    },
    {
        "text_input": "Does webcam quality matter?",
        "output": "A standard 720p webcam is sufficient. More important is proper positioning (slightly elevated, 50-60cm distance) and good lighting."
    },
    {
        "text_input": "What's the best way to test recognition?",
        "output": "Position yourself 50-60cm from the webcam, ensure good lighting, toggle on recognition, and try basic signs like 'Hi' or 'Thank you'."
    },
    {
        "text_input": "Can multiple people use sign language recognition?",
        "output": "Yes, but each person should be 50-60cm from their webcam with their upper body fully visible for accurate recognition."
    },
    {
        "text_input": "What if my signs aren't being recognized?",
        "output": "Verify your distance (50-60cm from webcam), lighting, and ensure your complete upper body and hands are visible in frame."
    },
    {
        "text_input": "How do I set up my workspace?",
        "output": "Place your webcam slightly elevated, position yourself 50-60cm away, ensure good lighting, and clear background for optimal recognition."
    },
        {
        "text_input": "Can multiple people use sign language recognition?",
        "output": "Yes, multiple users can enable the sign language recognition feature, but each webcam should only capture one person for accurate recognition."
    },
    {
        "text_input": "Is it possible for many users to use the sign language model at the same time?",
        "output": "Yes, the platform supports multiple users enabling the sign language recognition feature, but each user's webcam should focus on only one person."
    },
    {
        "text_input": "Can the system handle multiple people using the sign language feature?",
        "output": "Yes, the system can handle multiple users toggling on the feature simultaneously, but each webcam should capture just one person."
    },
    {
        "text_input": "Can I use sign language recognition if there are several people in the meeting?",
        "output": "Yes, several people in the meeting can use the feature, but each user's webcam should show only one person to ensure accurate detection."
    },
    {
        "text_input": "Can multiple participants activate the sign language recognition feature?",
        "output": "Yes, multiple participants can activate it, but every webcam should display only one person to maintain accurate recognition."
    },
    {
        "text_input": "Does the sign language recognition model support group use?",
        "output": "Yes, it supports group use where multiple users can activate it, but each webcam should focus on one individual for proper detection."
    },
    {
        "text_input": "Can more than one user toggle on the sign language feature in a meeting?",
        "output": "Yes, more than one user can toggle it on, but each webcam should only have one person in the frame."
    },
    {
        "text_input": "Can two people share the same webcam while using the sign language recognition feature?",
        "output": "No, the system requires only one person to be visible in each webcam for accurate sign language recognition."
    },
    {
        "text_input": "If several users want to use the recognition model, is that allowed?",
        "output": "Yes, several users can use the model simultaneously, but each user's webcam should focus on a single individual."
    },
    {
        "text_input": "Can I share my webcam with another person while using the sign language feature?",
        "output": "No, for the feature to work correctly, your webcam should only show one person at a time."
    }
]


print(len(diverse_training_data))