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

   **Lili** - As a team, at the beginning of the project, we brainstormed and discussed ideas of the project. Two favored project ideas was AI-powered stock-picking service, and college admission couching service to preper high school students to successfully enroll their dream collegies/universities. Although there're many existing AI-powered financial services, our team decided to work on it as a great learning experience.

    **Ben** - Trello was a soild tool to learn about and use. We were able to keep track of everything we wanted to add into Hinton.io, and we knew who was focusing on what specific user story.

3. **Challenges and Overcoming Them:**

   *Recall a specific challenge, like debugging a code issue together. Explain how you collaborated to identify the bug's source and successfully resolved it. This experience showcases your problem-solving and teamwork skills.*

   **Dany** - We all encountered challenges while running Django on our local machines due to compatibility issues with certain Python or Django versions and incompatible packages. Our troubleshooting documentation played a crucial role in overcoming these challenges. An instance involved a teammate facing a unique error. We collaborated for approximately an hour, before we decided to troubleshoot together through TeamViewer(something new I got to experience). I went through our troubleshooting document and retraced the steps to run Django and successfully configured it to run on their local machine.

   **Jason** - Initially, we encountered issues setting up github and cloning the repository. Then it turned into implementing ideas into code. After troubleshooting with each other, we overcame any technical issue that came throughout the project's cycle. As Dany mentioned, TeamViewer was useful. Especially when all of us weren't on campus. Overall, **Communication** and **Research** helped problem solve.

    **Lili** - At the beginning of the sememster, none of the teammember had experience on full-stack development project. Therefore, we didn't know how to integrate database, data, website, API, AI and other componnents together. The team researched on front-end & back-end framework, and decided on Django. I had prior experience on how to build database on MySQL, learned JavaScript and Django on the fly. My main controbution to the project was database, which itself was a challenge. For example, how to store historic stock data, pull & update daily stock data, and call stock information from the back-end as well as how to present this data in the front-end. Thanks to researches and team communication, we finalized on calling stock data via Yahoo Finance and using Streamlit to present to users in charts, and ingerated AI-powered chatbox to help new investors to understand these stock data in textual format.

   **Ben** - Creating a QA AI System was confusing, as every different tutorial I saw online had a different way of explaining the concept of the system, without explaining how to code the system. The AI Chatbot was also similarly difficult, as every tutorial had a different way to code. Additionally, my computer was having trouble running Python. Eventually, I found Botpress, a website that allowed me to build a chatbot in a visual manner.

4. **Accomplishments and Pride:**

   *Highlight a feature you contributed to, such as creating a login system. Discuss how your combined skills enabled the team to deliver a functional feature that enhances user experience.*

   **Dany** - I played a role in building a login system for our project using Django and some frontend work for both the login system and our dashboard. This included creating a user-friendly UI and making sure users were smoothly being redirected to our main dashboard, where we used Streamlit for our core functionality.  

   Integrating Streamlit with Django posed a challenge since Streamlit usually runs independently, often opening in a new tab each time a user logs in. To solve this, I embedded the Streamlit application within an iframe. This way, users could seamlessly move from the login page to the dashboard without disruptions.

   **Jason** - I played a role in creating the Streamlit application. I chose Streamlit because it was designed for data-centric applications. There is a massive community that provides resources which helped me in the delopment process. I have always had an interest in machine learning, and Streamlit provides many libraries that help showcase models and visualize data. This program was intended to run independently, but I shared with the group that it may be a fun experience to integrate with Django. Additionally, Streamlit applications offer customization options for both beginners and advanced users.

   **Lili** - As a team, we all contributed to this project. My main contributions are, brainstorming & finalizing project ideas; stock data management and presentation (database), recording & finalizing meeting notes, and communicating & updating project progresses with the team.

     **Ben** - My main role was building a QA System. Through research I found that the scope of it would have far exceeded the scope of the project, so instead I found that building a chatbot would fulfill the user story for a Question and Answering system, while being easy to build and maintain. I was also the team scribe, keeping notes for both the meetings and the class, keeping us on track.

6. **Learning and Growth:**

   *Provide an example of how you applied a concept learned in class to a practical scenario. Describe how you used version control (like Git) to collaborate on a coding assignment, improving code organization and collaboration.*

   **Dany** - When I first started work, I was taught to use cherry-pick in Git which often led to conflicts where I started to update the code manually. Before I started this course, I researched a ton on best ways to merge without facing this issue. About 2 weeks into the course, our professor talked about facing similar situations and that manually updating Git would be easier. I took this with a bit more confidence and I am sticking to manually updating all my changes without feeling doubtful of how I am merging codes. 

   **Jason** - Before this course, I had minimal experience with team-based software development. I was introduced to great tools such as Git and Trello, which were used through the whole development process. I enjoyed using Teams to communicate as well. I used to always code on my own and not work with people. Overall, this course made me comfortable with collaboration!

   **Lili** - It was a great learning experience to work on a full-stack project. Learning various frameworks for both front-end and back-end development. Lots to do in the near future to have myself comfortable in building full-stack products. For example, JavaScript has many cool features such as Node.js and Machine Learning on JavaScript. It's really cool to discover and learn development tools.

    **Ben** - Using and learning Trello was very helpful. Before, I would try to keep track of projects and task mentally, without help by writing it down. With Trello, we were able to keep track of what needed to get done, and who was doing it. I'll be looking foward to using Trello for future project.


## Product Showcase

### Elevator Pitch

Hinton.io revolutionizes stock prediction with a seamless blend of sophisticated analysis and user-friendly interface. Imagine navigating the complex world of stock market insights as effortlessly as flipping through your favorite magazine. Our app, with its intuitive design (akin to a user-friendly magazine layout), empowers both novice and experienced investors to effortlessly access and comprehend stock predictions. Just like a well-organized magazine makes content discovery a breeze, Hinton.io's streamlined interface enhances user navigation, ensuring a smooth journey through the intricacies of stock data. Elevate your investment experience with Hinton.io, where insightful predictions meet a user-friendly design for a market exploration like never before.

Overall, **Hinton.io is an AI-powered tool to help all investors to pick best performing stock.**

### Product Demo

**[Presentation & Demo](https://youtu.be/o46YeIrEnf0):** Click to view our presentation & demo video!

### Technical Architecture Overview

Simplify a technical concept with an example...

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

Selecting the project idea was a team effort. Each of us had many great ideas and chose to work on Hinton.io was a team effort. We all found it would a cool project to work on and each of us can learn from workin on the project.

**Jason** - We enjoyed the use of Trello to track our tasks. We also greatly enjoyed the use of Teams to share thoughts virtually whenever we had to. Overall, we had great communication and I will continue to use these methods throughout my journey as a dev. 

2. **Problem-Solving Abilities:** Share a situation where you had to troubleshoot a technical issue and how you approached the problem-solving process.

For example, in the Database element, which could include multiple tables and represent various attributions of stock. How could the stock data presented to users in a straight-forward and easy to digest manner was our main concern. In the end, our team chose to use Yahoo Finance and Streamlit.

**Jason** - In general, whenever someone had an issue, it was properly communicated via Teams or verbally in class. From there, we figured out who else had a similar issue and came up with a solution for it. A lot of debugging took place. Finding errors became second nature... If noone in the group knew, research was our friend. That is why we chose popular tools to work with so we were able to find solutions to our problems.

 **Ben** - When researching and developing the Chatbot, my computer refused to run Python code, preventing me from testing the code I was working on. This lead to me finding a workaround via Botpress, which allowed me to build my Chatbot without needing to struggle with my computer.

3. **Contributions to the Project:** Discuss a specific task you contributed to and how your involvement positively impacted the project's development.

**Lili** - Selecting the project idea was quick fun as every teammember had many cool ideas. We researched on these project ideas and analyzed the feasibility of working on these project in a time frame of one sememster. We decided on the AI-powered stock picking service.

**Jason** - I introduced the team to Streamlit web applications. I was able to present how user friendly the library is and how we can utilize the built-in features to make a core program. It has plenty of resources to assist with development. Overall, it is a fantastic platform for data apps that utilize machine learning and to generate visualizations. I created the stock prediction program, and with that, we tied in the many plug and play aspects to it to really show off that application. 

 **Ben** - As the team scribe, I was taking notes of both the in class lectures, as well as our meeting notes, allowing us to see how far we had come with our project and keeping track of what we had to do next.


4. **Applied Knowledge:** Describe a technical concept learned in class that you've used in your project, highlighting its practical relevance.

**Lili** - For me, it's good to know the various development style: waterfall v. Agile; various frameworks in front-end v. back-end development. things to consider in architecture and software development: not only building a product, but how to effeciently & effectively build a projet in a secure manner.

**Jason** - I found that the Agile methodology was useful for our project. Before this course, I have only seen that term while looking through job descriptions. I was excited to learn about the concept in class and how we would apply that into our project. I found the sprints to be useful because we were able to break down our project into managable pieces and complete them as a team. 

5. **Adaptability and Learning:** Provide an example of a challenge you faced that required learning a new skill or concept, and how you adapted to overcome it.

**Lili** - As the team made progress on the project, at each small step, we learn new things. For example, which development framework do we adopt in front-end and back-end. I researched Django and other frameworks, and learned Django has cybersecurity built in and support of many other software components. Another good skill that I learned during this semest is how to use Github and push & pull code on Visual Studio Code. Additionally. how to host Hinton.io and present to users in static mode: one solution is to link our Github repository to [Netlify](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Introducing_complete_toolchain), another is to use VSC extention, or run it in local host. Also, I did spend great many time in learning JavaScript, how to create an interactive website (Hinton.io) using JavaScript (although our team decidec on another solution.).

**Jason** - I found Django to be a challenge because I haven't used that framework before. It was exciting that we selected that framework because I enjoy learning new tools... Specifically, I didn't understand how to connect the Streamlit application to Django. As a team, we researched how to do that and we compared with other examples and then tried to replicate the process. I am glad there were many resources on that framework because we definitely needed them to get through.
