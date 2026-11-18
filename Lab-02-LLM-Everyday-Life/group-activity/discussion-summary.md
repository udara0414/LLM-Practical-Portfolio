# Group Discussion Summary – Sipwise

## 1. Introduction

As part of Lab Sheet 2 – AI in Everyday Challenges, Group 4 explored how Large Language Models (LLMs) could be used as product-development partners to address an everyday problem.

Our group was assigned the challenge of "The Dehydrated Student". The group focused on university students who often forget to drink water because of their busy academic schedules.

Through group discussions and the use of an LLM, we developed a product concept called **Sipwise**.

## 2. Problem Exploration

Initially, the group discussed common situations where university students may forget to drink water.

We identified that students frequently spend several hours attending lectures, laboratory sessions, and studying. During these activities, they may not remember to drink water regularly.

We also discussed the limitations of traditional hydration reminder applications. Although these applications send reminders at fixed intervals, notifications may arrive during lectures or other activities where students cannot respond immediately.

Based on this discussion, we identified that a more suitable solution should consider students' academic schedules and provide reminders at convenient times.

## 3. Product Idea Development

After identifying the problem, the group explored possible product solutions with the assistance of an LLM.

Several important ideas were considered:

- A mobile application for tracking daily water consumption.
- A personalized drinking schedule based on lecture times.
- A smart bottle cap that provides visual feedback.
- AI-generated notifications based on individual progress.
- A bottle alert feature to help students avoid leaving their bottles behind.

The group combined these ideas into one product concept rather than developing separate solutions.

The selected product was named **Sipwise**, with the tagline:

"Drink water on your class schedule, not when you're already thirsty."

## 4. Discussion on Product Features

The group discussed how the proposed product could work in a university environment.

### 4.1 Timetable Integration

We discussed allowing students to upload their academic timetables as images or PDFs. This information could be interpreted using an LLM to create a hydration plan that considers lecture periods and available breaks.

### 4.2 Smart Bottle Cap

The group explored the possibility of using an ESP32 microcontroller, an open sensor, Bluetooth Low Energy (BLE), and LED indicators to support hydration tracking.

The proposed open sensor detects each time the bottle is opened, with each opening counted as a sip in the concept.

The smart cap uses Bluetooth Low Energy as its primary connection to communicate sip counts and proximity information to the mobile application. Wi-Fi is considered a backup option for synchronising data when the student's phone is not nearby.

The proposed blue and amber LED indicators provide visual feedback about the student's hydration progress. This allows the smart cap to display alerts without interrupting students during lectures.

The sensor detects bottle openings rather than measuring the exact volume of water consumed.

### 4.3 Personalized Notifications

We discussed generating notifications based on timetable information and hydration progress instead of sending reminders at fixed intervals.

For example, if a student is falling behind during a lecture, the smart cap could provide a visual indication. A mobile notification could then be sent during the next suitable break.

### 4.4 Additional Features

The group also considered features such as:

- Manual drink logging.
- Daily hydration progress tracking.
- Left-behind bottle alerts.
- Campus water refill point mapping.
- Friends' hydration streaks.

These features were included to make the proposed solution more useful within a university environment.

## 5. How the Group Used the LLM

The LLM was used as a product-development partner during the brainstorming and concept-development process.

The group explored how an LLM could assist with:

1. **Idea Generation:** Exploring possible AI-based solutions to the identified hydration problem.
2. **Feature Development:** Identifying useful product features and improving the initial product concept.
3. **Product Design:** Exploring how the mobile application, smart bottle cap, and AI functionality could work together.
4. **LLM Integration:** Identifying practical situations where natural-language processing and personalized text generation could be used.
5. **Concept Refinement:** Improving the overall product idea and organizing the proposed features into a clear solution.

The LLM supported the development process, while the group considered and selected the ideas relevant to the identified problem.

The group also identified three main LLM-based functions for the proposed product:

- **Timetable Interpretation:** Understanding timetable information uploaded as images or PDFs and identifying class sessions and breaks.
- **Personalized Notification Generation:** Generating reminders using information such as the next class, hydration progress, and friends' streaks.
- **Natural-Language Drink Logging:** Interpreting ordinary text entries, such as "I had a Milo at the canteen", and estimating the drink amount for the hydration log.

These functions were identified as proposed applications of LLM technology rather than implemented features.

## 6. Key Decisions Made by the Group

Following the discussions, the group agreed on the following decisions:

- **Product Name:** Sipwise.
- **Primary Target Audience:** University students with busy academic schedules.
- **Main Problem:** Forgetting to drink water during lectures and other academic activities.
- **Main Solution:** A timetable-aware hydration support application connected to a proposed smart bottle cap.
- **Main AI Component:** LLM-based timetable interpretation and personalized notification generation.
- **Hardware Concept:** ESP32-powered smart bottle cap with sensor-based sip tracking and LED feedback.
- **Visual Prototype:** A mobile application mock-up designed using Figma.

## 7. Final Product Concept

The final concept combines three main components:

| Component | Main Purpose |
|---|---|
| AI-powered mobile application | Timetable interpretation, hydration planning, and personalized notifications |
| Smart bottle cap | Proposed sip tracking and visual progress feedback |
| Campus support features | Refill point discovery and social engagement |

These components work together to provide a more context-aware hydration support experience.

## 8. Conclusion

The group discussion helped transform a common student problem into a structured AI-assisted product concept.

By using an LLM during brainstorming and product development, the group explored different solution ideas, identified suitable features, and considered practical applications of generative AI.

The final outcome was Sipwise, a proposed hydration-support solution that combines timetable-aware planning, personalized AI interactions, and smart hardware functionality.

