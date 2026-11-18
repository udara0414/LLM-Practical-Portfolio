
# Activity Outcomes – Sipwise

## 1. Project Overview

**Product Name:** Sipwise  
**Group:** Group 4 – The Dehydrated Student  
**Module:** PUSL 3205 – Large Language Models and Generative AI  

**Tagline:**  
"Drink water on your class schedule, not when you're already thirsty."

Sipwise is an AI-assisted hydration support product concept designed to help university students maintain better hydration habits while managing busy academic schedules.

The proposed solution combines a timetable-aware mobile application, Large Language Model (LLM) capabilities, and an ESP32-powered smart bottle cap. Instead of relying on fixed hourly reminders, Sipwise considers a student's academic timetable and hydration progress to suggest suitable drinking times.

## 2. Problem Identification

University students often spend extended periods attending lectures, participating in laboratory sessions, completing assignments, and studying. During these activities, they may forget to drink water regularly.

Although traditional hydration reminder applications provide notifications at fixed time intervals, these reminders may arrive during lectures or other academic activities. As a result, students may ignore, mute, or disable the notifications.

The main challenge is therefore not simply reminding students to drink water. It is identifying appropriate moments when they can conveniently respond to those reminders without interrupting their academic activities.

### Identified Challenges

- Students may forget to drink water during long lectures and laboratory sessions.
- Fixed-interval notifications may interrupt academic activities.
- Students may not have an easy way to monitor their daily hydration progress.
- Traditional reminder applications may not consider individual class schedules.
- Students may forget to carry their water bottles when moving between locations.

## 3. Proposed Product Solution

Sipwise addresses these challenges through a smart hydration-support concept that connects a mobile application with a smart bottle cap.

The mobile application uses timetable information and hydration progress to develop a personalized drinking schedule. The proposed smart cap provides visual feedback based on hydration progress, while the application delivers notifications during suitable breaks.

The concept aims to make hydration reminders more context-aware, convenient, and less disruptive to students' daily academic routines.

## 4. Target Audience

The primary target audience is university students who have busy academic schedules.

The proposed product is particularly suitable for:

- Students attending consecutive lectures.
- Students participating in long laboratory sessions.
- Students who frequently forget to drink water while studying.
- Students who carry reusable water bottles to university.
- Students who prefer personalized reminders rather than fixed-time notifications.

## 5. Main Product Features

### 5.1 Timetable-Aware Hydration Planning

Students can provide their academic timetable through an image or PDF. The proposed AI functionality extracts timetable information and uses it to prepare a suitable hydration plan.

The plan considers lecture periods and available breaks to identify convenient times for drinking water.

Students can also update timetable information using natural-language instructions, such as changing the time of a laboratory session.

### 5.2 Daily Hydration Tracking

The mobile application includes a daily progress dashboard that allows students to monitor their hydration progress.

The proposed interface includes:

- A daily hydration progress indicator.
- A personalized daily hydration goal.
- Manual drink logging options.
- Quick logging amounts such as 150 ml, 250 ml, and 500 ml.
- Adjustments to the suggested goal based on contextual factors, such as hot weather.

### 5.3 ESP32-Powered Smart Bottle Cap

Sipwise proposes a smart cap that can be attached to a regular water bottle.

The cap is designed around an ESP32 microcontroller and a sensor-based sip-counting mechanism. It communicates with the mobile application through Bluetooth Low Energy (BLE).

The proposed visual feedback system includes:

- **Blue LED:** Indicates that the student is on track with the hydration plan.
- **Amber LED:** Indicates that the student may be falling behind the planned hydration progress.

This provides a simple visual reminder without requiring students to check their phones during lectures.

### 5.4 Context-Aware Notifications

Unlike traditional reminder applications, Sipwise is designed to consider the student's timetable and current hydration progress before sending notifications.

For example, if a student is falling behind during a lecture, the smart cap can provide a visual indication. When the next suitable break arrives, the mobile application can display a personalized reminder.

This approach aims to reduce unnecessary interruptions during academic activities.

### 5.5 Left-Behind Bottle Alert

The proposed application uses Bluetooth signal strength to help identify when a student may have moved away from their connected water bottle.

If the connection indicates that the bottle may have been left behind, the application can provide an alert to remind the student to collect it.

### 5.6 Campus Refill Points and Social Features

The proposed application also includes additional features to support hydration habits within the university environment.

These include:

- A campus map showing nearby water refill points.
- Friends' hydration streaks.
- Progress-based engagement features that encourage consistent habits.

## 6. Application of Large Language Models (LLMs)

LLMs are an important part of the Sipwise product concept. They are proposed as a way to understand natural-language information and generate personalized interactions.

Three main LLM-based functions were identified during the product development activity.

### 6.1 Timetable Information Extraction

The proposed system allows students to upload a timetable as an image or PDF.

An LLM-based processing workflow can interpret the timetable information and help convert it into structured schedule details. These details can then be used to generate a personalized hydration plan.

### 6.2 Personalized Notification Generation

The system can use contextual information such as:

- The student's next class.
- Current hydration progress.
- Available break periods.
- Friends' hydration streaks.

Based on this information, an LLM can generate short, personalized hydration notifications that are more relevant to the student's current situation.

### 6.3 Natural-Language Drink Logging

Students can record drinks using ordinary language rather than selecting every detail manually.

For example:

"I had a Milo at the canteen."

The proposed LLM functionality can interpret the entry and estimate the drink amount for the hydration log. The estimated amount would need to be reviewed or confirmed by the user when necessary.

## 7. Proposed Technologies and Components

The product concept combines AI-based software functionality with connected hardware components.

| Component | Purpose |
|---|---|
| Large Language Models | Timetable interpretation, notification generation, and natural-language drink logging |
| Mobile Application | Hydration tracking, timetable management, and notifications |
| ESP32 | Microcontroller for the proposed smart bottle cap |
| Sensors | Support the proposed sip-counting mechanism |
| Bluetooth Low Energy | Communication between the smart cap and mobile application |
| LED Indicators | Visual hydration progress feedback |
| Rechargeable Battery | Power supply for the proposed smart cap |

## 8. Expected Product Outcome

The expected outcome of the activity is a product concept demonstrating how Large Language Models, mobile application functionality, and IoT-based hardware can be combined to address an everyday student challenge.

Sipwise aims to demonstrate a more context-aware approach to hydration reminders by considering academic schedules instead of depending entirely on fixed notification intervals.

The proposed solution also highlights how LLMs can support natural-language interaction and personalized user experiences in an everyday application.

## 9. Product Development Deliverables

The main outcomes of the group activity include:

- Identification and analysis of an everyday student hydration problem.
- Development of the Sipwise product concept.
- Identification of the target user group.
- Design of the main mobile application features.
- Proposed ESP32 smart bottle cap functionality.
- Identification of three potential LLM use cases.
- Development of a visual mobile application mock-up using Figma.
- Preparation of the product proposal and group presentation.

## 10. Conclusion

The Sipwise concept demonstrates how generative AI can be explored as a product-development partner when addressing practical everyday challenges.

By combining timetable-aware planning, personalized LLM-generated interactions, and proposed smart hardware functionality, Sipwise presents an alternative approach to supporting students' hydration habits.

The activity provided an opportunity to identify a real-world problem, develop an AI-assisted product concept, explore possible LLM applications, and communicate the proposed solution through a visual prototype.

 
