# Key Architectural Decisions

## Table of Contents

- [Directions](#directions)
- [1. Introduction](#1-introduction)
  - [1.1. Purpose](#11-purpose)
- [2. System Overview](#2-system-overview)
- [3. Technical Choices](#3-technical-choices)
  - [3.1. Frontend Framework](#31-frontend-framework)
  - [3.2. Backend Framework](#32-backend-framework)
  - [3.3. Database System](#33-database-system)
- [4. Other Considerations](#4-other-considerations)
  - [4.1. Team Skills and Learning](#41-team-skills-and-learning)
  - [4.2. Community and Support](#42-community-and-support)
  - [4.3. Future Adaptability](#43-future-adaptability)
- [5. Decision Log](#5-decision-log)

## Directions:

This assignment is designed to guide you in understanding the foundational aspects of your project. Remember, in software engineering, understanding the "why" behind decisions is often as important as the decisions themselves. As you navigate these early stages of your coding journey, focus on grasping the core reasons behind each choice, and use this document to record and reflect on those reasons.

---

## 1. Introduction

### 1.1. Purpose

A brief overview of what this document entails.

1) This document is to note what/which tools we will be using in developing our AI-Driven Stock/Financial App.

---

## 2. System Overview

Provide a simple diagram or description of the high-level system.

1) This AI-powered app will learn from and read stock market information, presenting it in a clear, easy to understand way.

---

## 3. Technical Choices

### 3.1. Frontend Framework

We chose **Django** as our frontend framework because it provides a secure and reliable environment for handling multiple users simultaneously. Django follows best practices in web development, including built-in security features, an ORM for database interactions, and a robust authentication system. These qualities make it an excellent choice for projects where security and scalability are crucial.

### 3.2. Backend Framework

1) **Django** is our chosen backend framework due to its seamless integration with the frontend (Django itself) and its proven track record for building robust web applications. The ability to handle many users concurrently is crucial for our project, and Django's built-in features, such as the ORM, authentication system, and support for handling multiple requests, make it a secure and reliable choice. The Python ecosystem, extensive documentation, and an active community further contribute to our decision to use Django as our backend framework.

2) We have integrated **Streamlit** into our Django project because it complements Django's capabilities by providing a simple and effective way to create interactive data-driven web applications using Python. Streamlit allows us to build rich, responsive user interfaces with minimal effort, leveraging the power of Python libraries for data analysis and visualization. This integration enhances the user experience by seamlessly combining the robust backend capabilities of Django with the interactive and dynamic frontend features offered by Streamlit.

### 3.3. Database System

**MySQL** has been around for a long time and has a reputation for stability and reliability. This can be crucial for projects that prioritize a mature and proven technology stack.

---

## 4. Other Considerations

### 4.1. Team Skills and Learning

Are there particular strengths within your team that influenced your decisions? Is there a particular technology someone is excited to learn more about?

1) Several of us know the Python language.

2) We are eager to learn about and use AI Driven Software.

### 4.2. Community and Support

Did the availability of tutorials, community support, or other resources influence your choice?

1) Python is a very well supported, and easy to learn language, making it our main choice.

2) Django is a well supported framework with plenty of assistance online.

3) Streamlit is widely used for making interactive data-driven web applications. It is user friendly and easily deployable. 

### 4.3. Future Adaptability

How easy do you believe it will be to adapt or extend the technology choices you’ve made in the future based on your current knowledge?

1) With AI technology still being developed, the app could easily grow to include even more information to read and explain in the future. The algorithms are always being improved, so the predicitions will become more accurate as well.

---

## 5. Decision Log

| Date       | Decision                             | Reasoning               |
|------------|--------------------------------------|-------------------------|
| 09/18/2023 | Chose React as our frontend framework.   | Our team found an abundance of beginner-friendly tutorials for React. Additionally, two members have some prior exposure to it, making it a logical starting point for our project. |
| 10/09/2023 | Chose Django As Frontend Frame work  | Security and reliablity. We also found that it looked nicer and the built in tools sparked our interest. Through small experiments, we found that it is greatly customizable, and we can connect web apps such as our Streamlit program.  |
| 10/16/2023 | Chose Streamlit for our main web-app | It is used in many data web apps. It is easy to work with and it runs relatively smooth.                   |
| 10/23/2023 | Chose SQLite as Database              | Well Supported by Django and easy to connect (no password required). We spent most of our time working with our frontend and middleware. Now that we have a solid application, we can implement the DB. |
| 10/30/2023 | News Updates | We wanted to add more "life" to our front page. This plugin adds real time news updates about the stocks                  |
| 11/30/2023 | Implement BotPress as our chatbot   | We were looking to add some finishing touches to our app. Essentially, it is plug and play. Can connect it to the app and we are able to manipulate the prompts on the fly            |





Note: As you progress, keep adding to this log. It will not only help you track your decisions but also offer insights into your evolving
