# Applier - Personalized Job Application Generator

Applier is a web application designed to help users create personalized job application emails and LinkedIn messages. It uses advanced AI (Google Gemini API) to generate tailored content based on user inputs, such as their name, profession, and the recruiter's details. The application also saves recruiter information to a PostgreSQL database for future reference.

## How It Works

### 1. User Input
The user provides the following details through a web form:

**Personal Information:**
- Full Name
- Gender
- Profession

**Recruiter Information:**
- Recruiter's Full Name
- Company Name
- Recruiter's Email (optional)

**Platform:**
- Choose between Email or LinkedIn.

**Language:**
- Select the language for the generated content (e.g., English, Spanish, French).

### 2. Content Generation
Once the user submits the form, the application uses the Google Gemini API to generate personalized content. Here's how it works:

#### a. Personal Description
The application generates a short personal description based on the user's name, gender, profession, and selected language. For example:
> "I am John Doe, a passionate Software Engineer with experience in building scalable web applications. I enjoy solving complex problems and working in collaborative environments."

#### b. Email or LinkedIn Message
Based on the selected platform, the application generates either:

**A job application email:**
- Includes a polite and professional message tailored to the recruiter and company.
- Mentions the user's interest in opportunities related to their profession.

**A LinkedIn message:**
- A concise and professional message to contact the recruiter on LinkedIn.
- Highlights the user's interest in opportunities at the company.

### 3. Database Integration
The application saves the recruiter's details (name and company) to a PostgreSQL database. This allows users to keep track of recruiters they've contacted and reuse their information in the future.

### 4. Output
The generated content is displayed to the user in the web interface. The user can:
- Copy the email or LinkedIn message.
- Use it to contact the recruiter directly.

## Example Workflow

**Input**

_User Details:_
- Full Name: John Doe
- Gender: Male
- Profession: Software Engineer

_Recruiter Details:_
- Full Name: Jane Smith
- Company: Tech Corp
- Email: jane.smith@techcorp.com

_Platform:_ Email  
_Language:_ English  

**Output (Generated Email)**

```plaintext
Subject: Job Application for Software Engineer Position

Dear Jane Smith,

I hope this message finds you well. My name is John Doe, and I am a Software Engineer with a passion for building scalable and efficient systems. I came across Tech Corp and was impressed by your innovative projects and company culture.

I am reaching out to express my interest in any opportunities for Software Engineers at Tech Corp. I believe my skills and experience align well with your team's needs, and I would love to contribute to your ongoing success.

Please let me know if there are any open positions or if I can provide additional information. I look forward to the possibility of working together.

Best regards,  
John Doe
