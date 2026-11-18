
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

### 5.3 Smart Bottle Cap

Sipwise includes a proposed smart bottle cap designed to support hydration tracking.

The smart cap uses the following components:

- **Open Sensor:** Detects each time the bottle is opened. Each opening is counted as a sip in the prototype concept.
- **ESP32:** Processes the sensor information and communicates with the mobile application.
- **LED Ring:** Provides visual feedback to the student.
- **Rechargeable Battery:** Supplies power to the smart cap.

**Connectivity:**

- Bluetooth Low Energy (BLE) is the primary connection used to send sip counts and proximity information to the mobile application.
- Wi-Fi is considered a backup option for synchronising data when the student's phone is not nearby.

**Visual Feedback:**

- A blue light pulse indicates that the student is on track with the hydration plan.
- An amber light indicates that the student is falling behind the planned hydration target.
- If the student is in a lecture, the smart cap provides a visual alert instead of sending a phone notification.

The sensor detects bottle openings rather than directly measuring the exact volume of water consumed. Therefore, the sip count is an estimated tracking method.

### 5.4 How the Sipwise System Works

Sipwise combines the student's class timetable, smart bottle cap data, and daily weather conditions to provide personalised hydration support.

The proposed system follows this process:

1. **Timetable Input:** The student uploads a timetable as an image or PDF. The LLM identifies class sessions and available breaks.
2. **Hydration Planning:** The application creates a hydration schedule based on the student's timetable.
3. **Sip Tracking:** The smart cap detects bottle openings and sends the sip count to the mobile application through Bluetooth Low Energy.
4. **Progress Monitoring:** The application compares the recorded sip count with the planned hydration schedule.
5. **Context-Aware Notifications:**
   - If the student is behind the hydration plan during a lecture, the smart cap displays an amber light.
   - If the student is behind the plan but not attending a lecture, the application can generate an AI-assisted reminder for the next suitable break.
   - If the student is on track, the system remains quiet.
6. **Progress Updates:** When a drink is logged, the application updates the student's progress and streak.

The system aims to provide reminders at appropriate times without unnecessarily interrupting lectures.

### 5.5 Context-Aware Notifications

Unlike traditional reminder applications, Sipwise is designed to consider the student's timetable and current hydration progress before sending notifications.

For example, if a student is falling behind during a lecture, the smart cap can provide a visual indication. When the next suitable break arrives, the mobile application can display a personalized reminder.

This approach aims to reduce unnecessary interruptions during academic activities.

### 5.6 Left-Behind Bottle Alert

The proposed application uses Bluetooth signal strength to help identify when a student may have moved away from their connected water bottle.

If the connection indicates that the bottle may have been left behind, the application can provide an alert to remind the student to collect it.

### 5.7 Campus Refill Points and Social Features

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

 
