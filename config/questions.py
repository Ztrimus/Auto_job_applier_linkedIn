"""
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
"""

###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "templates/Resume_Saurabh_Zinjad.pdf"  # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience?
years_of_experience = "6"  # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"  # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/Ztrimus"  # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/saurabhzinjad"  # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"


## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 150000  # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
"""
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
"""

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = (
    106000  # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
)
"""
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
"""

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg:
# currency = "USD"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 14  # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
"""
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
"""

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "AI/ML Research Engineer at UOPX | Masters in Computer Science(Thesis) | 6 Years of Experience"  # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Versatile engineer with 6 years of experience developing production-ready ML solutions and full stack applications. Managing end-
to-end pipelines, from design to deployment and optimization in cloud environments. Passionate about advancing AI infrastructure,
fine-tuning foundation models, and delivering scalable, cost-effective solutions globally.
"""

"""
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
"""

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Saurabh Zinjad
github.com/Ztrimus; linkedin.com/in/saurabhzinjad; saurabhzinjad@gmail.com; 480-913-5544

Dear Hiring Team,

I build AI systems end-to-end—training and post-training models, shipping reliable services, and closing the loop with evaluations, monitoring, and fast iteration—across Machine Learning Engineering and AI Research Engineering.

### What I bring

1. Production impact: Drove ~6× capacity by shipping GenAI + explainability flows (LangGraph + LLMs); delivered an LLM summary dashboard (Kafka → Salesforce) and a Text-to-Visual API used in Slack/Teams—turning research into daily tools.
2. Safety & evaluations: First-author study on perturbation risk (*Can Typos Cause Harm?*) introducing a safety flip-rate metric; released a perturbation-aware eval pipeline to harden models pre-launch.
3. Observability at scale: Rolled out a multi-cloud model-monitoring platform (lifecycle tracking, alerting) adopted by 10+ clients; previously owned PySpark/Databricks data/ML pipelines with measurable lift.
4. Inference optimization / edge: Cut mobile compute cost ~30\% and reduced survey error ~22% with a lightweight SSD/MobileNetV2 engine; optimized API/DB paths to meet strict latency targets.
5. MLOps & feedback loops: AWS (Lambda, API Gateway, CloudWatch), Kafka, Docker/Kubernetes, CI/CD, experiment tracking; telemetry-driven A/Bs and post-training loops so models improve with real user signals.

### How I’ll add value—either track

1. ML Engineering: Harden training→serving paths, add evals/monitoring, and optimize throughput/$ while protecting quality.
2. AI Research: Implement/extend papers, run clean ablations and robustness tests, and land results in user-visible agents/APIs.

Happy to walk through these systems and discuss where I can accelerate safe, scalable model deployment and convert research into measurable impact. I’m available this week.

Respectfully,
Saurabh Zinjad
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc.
user_information_all = """
{
    "name": "SAURABH BHAUSAHEB ZINJAD",
    "title": "I build AI systems that solve real-world problems.",
    "summary": "Versatile engineer with 6 years of experience developing production-ready ML solutions and full stack applications. Managing end-to-end pipelines, from design to deployment and optimization in cloud environments. Passionate about advancing AI infrastructure, fine-tuning foundation models, and delivering scalable, cost-effective solutions globally.",
    "phone": "480-913-5544",
    "email": "saurabhzinjad@gmail.com",
    "media": {
        "linkedin": "https://linkedin.com/in/saurabhzinjad",
        "github": "https://github.com/Ztrimus",
        "medium": "https://ztrimus.medium.com",
        "devpost": "https://devpost.com/Ztrimus"
    },
    "work_experience": [
        {
            "role": "AI/ML Engineer II",
            "company": "University of Phoenix",
            "location": "AZ, USA",
            "from_date": "Feb 2025",
            "to_date": "Present",
            "description": [
                "Built GenAI + explainability tools (LangGraph + OpenAI) to process unstructured data and auto-explain complex academic/financial calcs, enhance advisor support capacity by 6x",
                "Integrated organizational knowledge base with LLMs, building pipelines to extract code logic into step-by-step explanations, accelerating onboarding and improving developer productivity",
                "Improved advisor support capacity by 6x by building GenAI + explainability tools using LangGraph and OpenAI to process unstructured data and auto-explain complex academic/financial calculations."
            ]
        },
        {
            "role": "AI Research Intern",
            "company": "University of Phoenix",
            "location": "AZ, USA",
            "from_date": "May 2024",
            "to_date": "Aug 2024",
            "description": [
                "Developed an LLM summary dashboard with chain-of-thought reasoning, integrated with Salesforce via Kafka, resulting in a 40% increase in advisor efficiency",
                "Created a Text-to-Visual API service that converts text to interactive diagrams and integrated it with Slack/Teams/CRMs, significantly improving documentation speed",
                "Increased advisor efficiency by 40% by developing an LLM summary dashboard with chain-of-thought reasoning and integrating it with Salesforce via Kafka.",
                "Led development of an AI-powered student note summarization tool in a winning hackathon, significantly improving advisor efficiency and enhancing student experience.",
                "Developed an innovative AI-based complex calculation explanation system, integrating multiple data sources (like log files and code repositories) and APIs to improve student support resolution speed by 6x. (Innovative Approach)",
                "Implemented critical Salesforce backend logic for tracking future out-of-pocket payments in excess funds cases, streamlining financial processes and improving data accuracy.",
                "Key Technologies: Python, Salesforce, Amazon Bedrock, LangChain, GPT4o, Claude Sonnet, Llama 3"
            ]
        },
        {
            "role": "Data Analyst",
            "company": "Decision Theater at Arizona State University, Tempe, USA",
            "from": "Jan 2024",
            "to": "Present",
            "description": [
                "Developed and implemented advanced data downscaling techniques, increasing resolution from PUMS to block level, and utilized clustering algorithms (k-means, DBSCAN, hierarchical) to analyze high-resolution patterns, enhancing granularity of policy insights by 40%.",
                "Engineered custom Python libraries for synthetic data generation and analysis, integrating machine learning models for data block property prediction and classification, resulting in a 30% improvement in data processing efficiency.",
                "Conducted comprehensive statistical analyses, including correlation studies (Pearson, cosine similarity) and property extraction, creating impactful visualizations and reports that directly informed policymaker decisions and stakeholder communications."
            ]
        },
        {
            "role": "Senior Machine Learning Engineer",
            "company": "Tiger Analytics",
            "location": "Bangalore, India",
            "from_date": "June 2022",
            "to_date": "July 2023",
            "description": [
                "Trained and tuned predictive ML models and scalable Data pipelines (Python, PySpark, Databricks), achieving an 18% increase in client revenue",
                "Architected a multi-cloud model monitoring platform for lifecycle tracking/alerts, supporting 10+ client adoptions",
                "Improved client revenue by 18% by training and tuning predictive ML models and building scalable data pipelines using Python, PySpark, and Databricks.",
                "Spearheaded development of Data & CI/CD pipelines, Interactive Dashboards, Constraint-based ML Models, Web App, and Comprehensive Documentation for MSP Value Optimization in Petcare sector with a team of 8 analysts. (Team Leadership)",
                "Developed MLCORE product (end-to-end MLOps platform) by implementing research ideas, organizing through prototyping, and Integrating it with numerous cloud services, attracting an additional four significant clients. (Interpersonal Skills)"
            ]
        },
        {
            "role": "Software Engineer",
            "company": "Winjit Technologies",
            "location": "Nashik, India",
            "from_date": "January 2020",
            "to_date": "June 2022",
            "description": [
                "Engineered 10+ RESTful APIs for real-time AI data processing and built 30+ low latency responsive UI React features",
                "Optimized large-scale MySQL, PostgreSQL databases, accelerating data access for AI model training and real-time inference",
                "Improved development efficiency by 8x by innovating a data-driven UI framework with dynamic form reconfiguration and customizable CSS.",
                "Engineered 10+ RESTful APIs Architecture and Distributed services; Designed 30+ low-latency responsive UI/UX application features with high-quality web architecture; Managed and optimized large-scale Databases. (Systems Design)",
                "Initiated and Designed a standardized solution for dynamic forms generation, with customizable CSS capabilities feature, which reduces development time by 8x; Led and collaborated with a 12 member cross-functional team. (Idea Generation)"
            ]
        },
        {
            "role": "Deep Learning Engineer",
            "company": "Automation Teknix",
            "location": "Pune, India",
            "from_date": "September 2019",
            "to_date": "January 2020",
            "description": [
                "Developed a lightweight object recognition engine with SSD & MobileNetV2, reducing computational cost by 30% for mobile use",
                "Streamlined CNN model using TensorFlow, OpenCV to improve image processing, reducing survey error in production by 22%",
                "Reduced survey error in production by 22% by streamlining a CNN model using TensorFlow and OpenCV to improve image processing.",
                "Devised a Lightweight Object Recognition Engine with a low computational cost by leveraging an SSD algorithm with MobilenetV2 architecture, which decreased survey error by 22%. (Problem Identification)",
                "Conducted thorough Initial research; prototyped neural network flow; conceptualized POC, training, and monitoring of models. This resulted in a 7% increase in accuracy and reduced inference time by 2x. (Experiment Design)"
            ]
        },
        {
            "role": "Research Intern",
            "company": "IMATMI, Robbinsville, New Jersey (Remote)",
            "from": "Mar 2019",
            "to": "Aug 2019",
            "description": [
                "Conducted research and developed a range of ML and statistical models to design analytical tools and streamline HR processes, optimizing talent management systems for increased efficiency.",
                "Created 'goals and action plan generation' tool for employees, considering their weaknesses to facilitate professional growth.",
                "Implemented an automated system to identify 'best-fit employees' for upcoming projects, improving project outcomes and resource allocation for managers."
            ]
        }
    ],
    "education": [
        {
            "degree": "Masters of Science in Computer Science - Thesis",
            "university": "Arizona State University, Tempe, USA",
            "from_date": "August 2023",
            "to_date": "May 2025",
            "courses": [
                "Statistical Machine Learning",
                "Operational Deep Learning",
                "Software verification, Validation and Testing",
                "AI Safety and Assessment",
                "Social Media Mining",
                "Knowledge Representation and Reasoning Algorithms",
                "Software Security"
            ]
        },
        {
            "degree": "Bachelor of Engineering in Electronics and Telecommunications",
            "university": "Pune Institute of Computer Technology, Pune, India",
            "from_date": "July 2015",
            "to_date": "June 2019",
            "courses": [
                "Data Structures and Algorithms",
                "Object Oriented Programming",
                "Operating Systems",
                "System Programming",
                "Computer Networks",
                "Artificial Intelligence",
                "Machine Learning",
                "Digital Video & Image Processing"
            ]
        }
    ],
    "skill_section": [
        {
            "name": "Languages",
            "skills": [
                "Python",
                "JavaScript/TypeScript",
                "C#",
                "C++",
                "SQL",
                "Java",
                "Bash",
                "HTML",
                "CSS"
            ]
        },
        {
            "name": "ML/AI",
            "skills": [
                "PyTorch",
                "TensorFlow",
                "scikit-learn",
                "LangChain",
                "LangGraph",
                "OpenCV",
                "Pandas",
                "MLflow",
                "Databricks"
            ]
        },
        {
            "name": "GenAI & Systems",
            "skills": [
                "RAG",
                "LLM evaluation",
                "fine-tuning",
                "prompt engineering",
                "agentic AI design",
                "MLOps",
                "observability",
                "Kafka"
            ]
        },
        {
            "name": "Cloud/DevOps",
            "skills": [
                "AWS (Bedrock, Lambda, S3, CloudWatch API Gateway, Cognito)",
                "GCP",
                "Azure",
                "Docker",
                "Kubernetes",
                "Git"
            ]
        },
        {
            "name": "Full-Stack",
            "skills": [
                "React",
                "Node.js",
                "Flask",
                "FastAPI",
                ".NET",
                "PostgreSQL",
                "MySQL",
                "MongoDB",
                "Terraform"
            ]
        }
    ],
    "publications": [
        {
            "title": "Can Typos Cause Harm? The Impact of Imperfect Input on LLM Safety",
            "venue": "SBP-BRiMS 2025",
            "from_date": "Sep 2024",
            "to_date": "Aug 2025",
            "link": null,
            "description": [
                "Systematic study of LLM safety under prompt perturbations; introduced safety flip rate and evaluated 5 models across 14 perturbation types & 11 harm categories—minor typos/paraphrases flip safety in 30% of cases",
                "Released open-source framework & augmentation pipeline for perturbation-aware safety evaluation and robust alignment tools"
            ]
        },
        {
            "title": "LLM-facilitated Pipeline for Personalized Resume Generation",
            "venue": "ACM SIGIR 2024",
            "from_date": "Aug 2023",
            "to_date": "Jul 2024",
            "link": "https://dl.acm.org/doi/10.1145/3626772.3657680",
            "description": [
                "Authored and published research on an ML pipeline optimized for user personalization using LLMs.",
                "Formulated novel user personalization metrics, setting benchmarks for AI-enhanced resume evaluation.",
                "Released an open-source Python library integrating information retrieval and web scraping; used by 1000+ users."
            ]
        }
    ],
    "projects": [
        {
            "name": "Multimodal AI System for Media Search",
            "type": "Hackathon",
            "link": "https://devpost.com/software/team-soul-1fjgwo",
            "resources": [],
            "from_date": "October 2024",
            "to_date": "October 2024",
            "description": [
                "Won Big Data Prize for content-based search across video/audio/images; stored in Postgres delivered 92% faster media search",
                "Implemented a content-based search system across video/audio/images, using Postgres database, resulting in a 92% faster media search",
                "Developed a multimodal AI system for media search that uses AWS, CLIP, and a vector database to achieve a 92% increase in search speed.",
                "Big Data Awards in Python FAST API and angular development, providing efficient data access and retrieval.",
                "Converted and stored every file type data as vector embeddings, ensuring low-latency search capabilities.",
                "Used Machine Learning techniques such as BERT, OCR, ResNet50, and Image Captioning to parse Image features.",
                "Contributed to Elasticsearch implementation for blazing-fast search responses, with millisecond response times."
            ]
        },
        {
            "name": "Forest fire Detection using IoT Sensor Data",
            "type": "Industrial Project",
            "link": "https://github.com/OmdenaAI/Dryad",
            "resources": [],
            "from_date": "September 2021",
            "to_date": "January 2022",
            "description": [
                "Implemented a TabNet classifier model with 98.7% accuracy on edge devices using AWS, TinyML, Docker, Redis, and Celery",
                "Utilized SMOTE and hyperparameter tuning to balance data and optimize recall, reducing errors detecting fire in 7 mins",
                "Reduced errors in detecting forest fires by 7 minutes using SMOTE and hyperparameter tuning to balance data and optimize recall.",
                "Devised a TabNet Classifier Model having 98.7% accuracy in detecting forest fire through IoT sensor data, deployed on AWS and edge devices 'Silvanet Wildfire Sensors' using technologies TinyML, Docker, Redis, and celery.",
                "Examine and utilize many performance metrics (Recall, F2 score, sensitivity, specificity. etc.) to reduce high type II error.",
                "Performed Model Exploration, Analysis, and Optimization."
            ]
        },
        {
            "name": "GenAI’s Capabilities and Boundaries Exploration - Prompt Engineering Hackathon for Humanities",
            "type": "Hackathon",
            "link": "https://www.linkedin.com/pulse/exploring-depths-ai-story-writing-prompt-engineering-hackathon-wbqwc",
            "from": "Oct 2023",
            "to": "Oct 2023",
            "description": [
                "1st runner up prize in crafted AI persona, to explore LLM's subtle contextual understanding and create innovative collaborations between humans and machines.",
                "Addressed limitations in narrative flow, simplicity, emotional depth, and hallucinations through innovative approaches.",
                "Demonstrated creative mindset and ability to navigate complex tasks and adapt to evolving requirements during hackathon."
            ]
        },
        {
            "name": "Stock Market Analysis",
            "type": "Intern Project",
            "link": "https://github.com/Ztrimus/Stock-Market-Analysis",
            "from": "Dec 2018",
            "to": "Feb 2019",
            "description": [
                "Conducted in-depth Exploratory Data Analysis (EDA) and utilized data visualization techniques for comprehensive stock market analysis. Implemented a range of statistical and ML models on diverse time-series stocks to extract insights and predictions. Improved performance by 27% on the “clustering and diversification analysis”."
            ]
        },
        {
            "name": "Autonomous Surveillance Monitoring System",
            "type": "Project",
            "link": "",
            "from": "Feb 2019",
            "to": "Jun 2019",
            "description": [
                "At a college-sponsored project, I Built a surveillance engine to detect and alert about suspicious behaviors on campus by constructing a computer vision pipeline of CCTV footage data processing, face detection, poses & action recognition using OpenCV, MediaPipe, Tensorflow, MLFlow, and Flask. Finally, We deployed it on college premises."
            ]
        },
        {
            "name": "Speech Emotion Recognition",
            "type": "Project",
            "link": "https://github.com/Ztrimus/speech-emotion-recognition",
            "from": "Nov 2018",
            "to": "Feb 2019",
            "description": [
                "Researched and optimized existing emotion detection approaches by combining CNN and LSTM networks. Discovered emotion-affecting attributes in voice by analyzing audio signal features-MFCC, ZCR, Pitch, and Chroma.",
                "Compressed audio data using an Autoencoder technique to avoid data loss. Due to this, we were able to boost the accuracy of the speech model by 31%. Used tools like PyTorch, Librosa, puAudioAnalysis, and Tensorboard."
            ]
        },
        {
            "name": "Homecoming: Animal Habitat Organization",
            "type": "Project",
            "link": "",
            "from": "Aug 2018",
            "to": "Jan 2019",
            "description": [
                "Developed a Custom Animal Identification and Classification model using Faster R-CNN architecture to identify animals and their habitats in a simulated environment, which Integrated it into the Firebird V ATMEGA2560 Robot (we tailored it to put animals into a habitat). Optimized the \"Region Proposal Network\" component resulting in 35% decrease in processing time."
            ]
        }
    ],
    "certifications": [
        {
            "name": "Deep Learning Specialization",
            "by": "DeepLearning.AI, Coursera Inc.",
            "link": "https://www.coursera.org/account/accomplishments/specialization/G3WPNWRYX628"
        },
        {
            "name": "MLOps for AI Engineers and Data Scientists",
            "by": "Omdena Inc.",
            "link": "https://drive.google.com/file/d/1fh4AEscb0P82nfoaA-muWMzmFngzyk2g/view"
        },
        {
            "name": "Microsoft Azure Fundamentals",
            "by": "Udemy.",
            "link": "https://www.udemy.com/certificate/UC-37e943d1-e7f7-4d27-a1e4-e799aef7013b/"
        },
        {
            "name": "Server-side Backend Development",
            "by": "The Hong Kong University of Science and Technology.",
            "link": "https://www.coursera.org/account/accomplishments/verify/TYMQX23D4HRQ"
        },
        {
            "name": "Front-End Web UI Frameworks and Tools",
            "by": "The Hong Kong University of Science and Technology.",
            "link": "https://www.coursera.org/account/accomplishments/verify/TW8MA6MEXSCZ"
        }
    ],
    "achievements": [
        "Won 10+ Hackathons and coding competitions at university and professional levels.",
        "1st runner-up in “Prompt Engineering Hackathon 2023 for Humanities”",
        "Received the 'Extra Miller - 2021' award at Winjit Technologies for outstanding performance. ",
        "President of Machine Learning Club: Led a team of 20 people in a project and was awarded \"Best Project of the Year.\"",
        "Finalist in E-yantra Robotics Competition 2018 - IITB.",
        "Dance Section's Head of PICT Art Circle: Best dance choreography for Winning \"Firodiya theater competition 2019.\"",
        "Performed in multiple award-winning state-level drama competitions and received the best-organized team prize thrice.",
        "An active member of the NSS (National Community Service Group in PICT) in 2016."
    ]
}
"""
##<
"""
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
"""

# Name of your most recent employer
recent_employer = (
    "Not Applicable"  # "", "Lala Company", "Google", "Snowflake", "Databricks"
)

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = (
    "9"  # Any number between "1" to "10" including 1 and 10, put it in quotes ""
)
##


# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False  # True or False, Note: True or False are case-sensitive
"""
Note: Will be treated as False if `run_in_background = True`
"""

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True  # True or False, Note: True or False are case-sensitive
"""
Note: Will be treated as False if `run_in_background = True`
"""
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = (
    False  # True or False, Note: True or False are case-sensitive
)


############################################################################################################
"""
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
"""
############################################################################################################
