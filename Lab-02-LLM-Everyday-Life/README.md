
# Lab 02 – AI in Everyday Challenges

## Project: Sipwise – Smart Hydration Support for University Students

**Module:** PUSL 3205 – Large Language Models and Generative AI  
**Group:** Group 4 – The Dehydrated Student  
**Product Name:** Sipwise  

> "Drink water on your class schedule, not when you're already thirsty."

## 1. Overview

This practical activity explores how Large Language Models (LLMs) can be used as product-development partners to identify everyday challenges and develop AI-assisted product concepts.

Our group selected student dehydration as the main problem, focusing on university students who often forget to drink water because of busy academic schedules.

To address this challenge, we developed **Sipwise**, a proposed AI-assisted hydration support product that combines a timetable-aware mobile application with an ESP32-powered smart bottle cap.

The concept aims to make hydration reminders more personalized and convenient by considering students' academic schedules and hydration progress.

## 2. Problem Statement

University students often attend consecutive lectures, laboratory sessions, and study for extended periods without drinking enough water.

Traditional hydration reminder applications usually send notifications at fixed time intervals. These reminders may interrupt lectures or other academic activities, causing students to ignore or disable them.

Therefore, there is a need for a more context-aware hydration support solution that considers when students are actually available to drink water.

## 3. Proposed Solution – Sipwise

Sipwise is designed around three main components:

### 3.1 AI-Powered Mobile Application

The proposed mobile application provides:

- Timetable-based hydration planning.
- Daily hydration progress tracking.
- Personalized hydration goals.
- Manual drink logging.
- AI-generated notifications.
- Campus water refill point discovery.
- Friends' hydration streaks.

### 3.2 ESP32 Smart Bottle Cap

The proposed smart cap is designed to attach to a regular water bottle.

Its planned capabilities include:

- Sensor-based sip counting.
- ESP32-based hardware control.
- Bluetooth Low Energy (BLE) communication.
- Blue and amber LED indicators.
- Left-behind bottle alerts.

### 3.3 LLM Integration

LLMs are proposed for three main functionalities:

1. **Timetable Interpretation:** Extracting timetable information from images or PDFs to help generate a personalized hydration plan.
2. **Personalized Notifications:** Generating contextual reminders using timetable information and hydration progress.
3. **Natural-Language Drink Logging:** Interpreting natural-language drink entries and estimating drink quantities for the hydration log.

## 4. How We Used LLMs

During the product-development activity, our group explored how an LLM could support the development of Sipwise.

The LLM was considered for:

- Brainstorming potential solutions to the identified problem.
- Generating and refining product feature ideas.
- Exploring practical applications of generative AI.
- Designing a product concept around user requirements.
- Identifying possible LLM-based functionalities.
- Improving the organization and presentation of the product idea.

The final concept was developed through group discussion and consideration of the ideas generated with LLM assistance.

## 5. Target Users

The primary target users are university students who:

- Have busy academic timetables.
- Attend long lectures and laboratory sessions.
- Frequently forget to drink water while studying.
- Carry reusable water bottles.
- Prefer reminders that do not interrupt their academic activities.

## 6. Product Design and Prototype

A visual mobile application mock-up was created using Figma to communicate the proposed Sipwise user experience.

The design illustrates the main application screens and product features, including hydration tracking, timetable-aware planning, and personalized reminders.

**Figma Prototype:** [Sipwise – Hydration Mockup](ADD_FIGMA_LINK_HERE)

## 7. Repository Structure

```text
Lab-02-LLM-Everyday-Life/
│
├── README.md
│
├── group-activity/
│   ├── README.md
│   ├── group-members.md
│   ├── activity-outcomes.md
│   ├── discussion-summary.md
│   └── Group4_Product_Proposal.pdf
│
└── screenshots/
    └── README.md
```

## 8. Documentation

The following files provide further information about the group activity:

| File | Description |
|---|---|
| [Group Activity](group-activity/README.md) | Introduction to the group activity |
| [Group Members](group-activity/group-members.md) | Group member information |
| [Activity Outcomes](group-activity/activity-outcomes.md) | Product concept, features, and expected outcomes |
| [Discussion Summary](group-activity/discussion-summary.md) | Group discussions and LLM-assisted development |
| [Product Proposal](group-activity/Group4_Product_Proposal.pdf) | Group product proposal |
| [Screenshots](screenshots/README.md) | Visual evidence and prototype references |

## 9. Learning Outcomes

Through this activity, we explored how LLMs can support product development beyond simple question answering.

The activity provided an opportunity to:

- Identify an everyday problem and define its requirements.
- Explore AI-assisted solution development.
- Apply LLM concepts to a practical product scenario.
- Evaluate and refine AI-generated ideas through group discussion.
- Design a product concept and communicate it through a visual prototype.
- Understand how AI and IoT technologies can be combined in an application.

## 10. Conclusion

Sipwise demonstrates how generative AI can be explored as part of an everyday problem-solving process.

By combining timetable-aware hydration planning, personalized LLM interactions, and proposed smart hardware functionality, the product concept aims to support students in developing more convenient hydration habits.

This activity strengthened our understanding of the potential role of LLMs in brainstorming, product design, and practical AI-assisted innovation.
