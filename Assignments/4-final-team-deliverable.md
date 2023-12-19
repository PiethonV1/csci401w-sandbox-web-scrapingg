# Software Engineering Class Final Reflection

## Table of Contents

- [Product Vision](#product-vision)
- [Learning and Growth Journey](#learning-and-growth-journey)
  - [Reflection](#reflection)
- [Product Showcase](#product-showcase)
  - [Elevator Pitch](#elevator-pitch)
  - [Product Demo](#product-demo)
  - [Technical Architecture Overview](#technical-architecture-overview)
  - [Codebase Exploration](#codebase-exploration)
  - [Access Your Work](#access-your-work)
- [Final Reflection Presentation](#final-reflection-presentation)
- [Career Readiness Assessment](#career-readiness-assessment)

## Product Vision

- **Product Vision Statement:** 

FOR investors WHO strive for a competitive advantage, **Hinton.io** is a web-based application THAT offers accurate financial forecasts utilizing machine learning. UNLIKE other financial tools, **Hinton.io** provides a user-friendly experience to streamline complex data analysis and decision-making processes. Our platform stands out with an intuitive interface, ensuring accessibility for both seasoned investors and newcomers to the financial landscape. **Hinton.io** is committed to democratizing the power of accurate financial predictions, offering a seamless and approachable solution that empowers investors to navigate the markets with confidence and make informed, strategic investment choices.

## Learning and Growth Journey

### Reflection

Reflect on your journey in learning software engineering through concrete scenarios:

1. **Team Collaboration Approach:**

   *Describe how your team used tools like Slack and Trello to coordinate tasks. Share an example of how assigning tasks in Trello helped streamline your group projects and fostered effective communication.*

   **Jason** - Starting this project, I was familiar with Slack and ClickUp for coordinating tasks. Trello is very similar to those, and the group enjoyed its' simplicity. The use of Teams provided effective communication for the group as well if we weren't together on campus.

2. **Challenges and Overcoming Them:**

   *Recall a specific challenge, like debugging a code issue together. Explain how you collaborated to identify the bug's source and successfully resolved it. This experience showcases your problem-solving and teamwork skills.*

   **Dany** - We all encountered challenges while running Django on our local machines due to compatibility issues with certain Python or Django versions and incompatible packages. Our troubleshooting documentation played a crucial role in overcoming these challenges. An instance involved a teammate facing a unique error. We collaborated for approximately an hour, before we decided to troubleshoot together through TeamViewer(something new I got to experience). I went through our troubleshooting document and retraced the steps to run Django and successfully configured it to run on their local machine.

   **Jason** - Initially, we encountered issues setting up github and cloning the repository. Then it turned into implementing ideas into code. After troubleshooting with each other, we overcame any technical issue that came throughout the project's cycle. As Dany mentioned, TeamViewer was useful. Especially when all of us weren't on campus. Overall, **Communication** and **Research** helped problem solve.

3. **Accomplishments and Pride:**

   *Highlight a feature you contributed to, such as creating a login system. Discuss how your combined skills enabled the team to deliver a functional feature that enhances user experience.*

   **Dany** - I played a role in building a login system for our project using Django and some frontend work for both the login system and our dashboard. This included creating a user-friendly UI and making sure users were smoothly being redirected to our main dashboard, where we used Streamlit for our core functionality.  

   Integrating Streamlit with Django posed a challenge since Streamlit usually runs independently, often opening in a new tab each time a user logs in. To solve this, I embedded the Streamlit application within an iframe. This way, users could seamlessly move from the login page to the dashboard without disruptions.

   **Jason** - I played a role in creating the Streamlit application. I chose Streamlit because it was designed for data-centric applications. There is a massive community that provides resources which helped me in the delopment process. I have always had an interest in machine learning, and Streamlit provides many libraries that help showcase models and visualize data. This program was intended to run independently, but I shared with the group that it may be a fun experience to integrate with Django. Additionally, Streamlit applications offer customization options for both beginners and advanced users.

4. **Learning and Growth:**

   *Provide an example of how you applied a concept learned in class to a practical scenario. Describe how you used version control (like Git) to collaborate on a coding assignment, improving code organization and collaboration.*

   **Dany** - When I first started work, I was taught to use cherry-pick in Git which often led to conflicts where I started to update the code manually. Before I started this course, I researched a ton on best ways to merge without facing this issue. About 2 weeks into the course, our professor talked about facing similar situations and that manually updating Git would be easier. I took this with a bit more confidence and I am sticking to manually updating all my changes without feeling doubtful of how I am merging codes. 

   **Jason** - Before this course, I had minimal experience with team-based software development. I was introduced to great tools such as Git and Trello, which were used through the whole development process. I enjoyed using Teams to communicate as well. I used to always code on my own and not work with people. Overall, this course made me comfortable with collaboration!

## Product Showcase

### Elevator Pitch

Hinton.io revolutionizes stock prediction with a seamless blend of sophisticated analysis and user-friendly interface. Imagine navigating the complex world of stock market insights as effortlessly as flipping through your favorite magazine. Our app, with its intuitive design (akin to a user-friendly magazine layout), empowers both novice and experienced investors to effortlessly access and comprehend stock predictions. Just like a well-organized magazine makes content discovery a breeze, Hinton.io's streamlined interface enhances user navigation, ensuring a smooth journey through the intricacies of stock data. Elevate your investment experience with Hinton.io, where insightful predictions meet a user-friendly design for a market exploration like never before.

### Product Demo

**[Presentation & Demo](https://youtu.be/o46YeIrEnf0):** Click to view our presentation & demo video!

### Technical Architecture Overview

Simplify a technical concept with an example:

Imagine Hinton.io as a live TV show about stock predictions. In this setup:

Django as the TV Studio (Frontend):

**Analogous Element:** The TV studio where the show is broadcasted.
**Explanation:** Django on Hinton.io is the frontend, serving as the TV studio that viewers (users) see. It manages the overall presentation, layout, and user interface, much like a TV studio sets the stage for the show. It's the interface that users interact with directly.

Streamlit as the Expert Analyst (Backend):

**Analogous Element:** The expert analyst providing insights behind the scenes.
**Explanation:** Streamlit on Hinton.io is the expert analyst working behind the scenes, analyzing data and generating insights. It's not directly visible to the viewers (users) but contributes to the content presented on the Hinton.io TV show. Streamlit, in this case, is responsible for the stock prediction analysis and processing.

Stock Prediction Insights as the On-Air Presentation:

**Analogous Element:** The on-air presentation of stock predictions.
**Explanation:** The stock prediction insights, generated by Streamlit on Hinton.io, are like the on-air presentation during the TV show. These insights are seamlessly integrated into Django's frontend (TV studio), creating a cohesive and engaging user experience.

In summary, Hinton.io is like a live TV show where Django serves as the frontend TV studio, Streamlit operates as the expert analyst behind the scenes, and the stock prediction insights are presented on-air through Hinton.io's interface. Together, they create a dynamic and interactive stock prediction experience for users.

### Codebase Exploration

Illustrate a coding concept with a relatable analogy:

Coding is like building a sandwich. Imagine you're the chef, and your code is the ultimate sandwich creation. Your variables are the ingredients - the lettuce, tomatoes, and bacon. The functions are the special sauces that add flavor and bring everything together.

Now, debugging is like being a detective in a food mystery. You take a bite and realize something's off – maybe the lettuce is acting weird or the bacon is misbehaving. You put on your detective hat, inspect each layer, and figure out where the flavor went wrong.

Pair programming is like having a sous-chef in the kitchen. You and your coding buddy work together, one chopping the onions while the other grills the chicken. It's a dance of collaboration, ensuring that your sandwich – I mean, code – turns out delicious and bug-free.

But beware of spaghetti code! That's when your sandwich ingredients get tangled up like a messy plate of spaghetti. Nobody wants to eat that, and nobody wants to debug that either. Keep your codebase neat and organized, like a well-arranged sandwich on a plate.

In the end, a successful code project is like serving a perfect sandwich to your customers. It's satisfying, it meets expectations, and it leaves everyone with a smile – unless, of course, someone forgot to handle the crusts. Nobody likes unhandled crusts!

### Access Your Work

- **[Presentation Slides](https://emailric-my.sharepoint.com/:p:/g/personal/jcain_7978_email_ric_edu/EXPWB_dhcO1PrltWA_Ct-vsBwUqOWzuGdiY6woqBDh18iw?e=BvT5LS):** Click to view our powerpoint presentation!
- **[Source Code Repository](https://github.com/PiethonV1/csci401w-sandbox-web-scrapingg/tree/main/Source%20Code):** Click to be directed to the github repository!
- **[Presentation & Demo](https://youtu.be/o46YeIrEnf0):** Click to view our presentation & demo video!
- **Other Materials:** Include links to diagrams or documents you created for your project.

## Final Reflection Presentation

- **Duration:** 25-minute minimum, 40-minute maximum

## Career Readiness Assessment

Answer the following questions with practical examples:

1. **Team Collaboration Skills:** Reflect on a time when coordinating with team members improved a project's outcome or efficiency.
2. **Problem-Solving Abilities:** Share a situation where you had to troubleshoot a technical issue and how you approached the problem-solving process.
3. **Contributions to the Project:** Discuss a specific task you contributed to and how your involvement positively impacted the project's development.
4. **Applied Knowledge:** Describe a technical concept learned in class that you've used in your project, highlighting its practical relevance.
5. **Adaptability and Learning:** Provide an example of a challenge you faced that required learning a new skill or concept, and how you adapted to overcome it.