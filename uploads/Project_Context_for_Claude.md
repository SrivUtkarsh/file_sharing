PROJECT CONTEXT — FACULTY WORK MANAGEMENT & AI-ASSISTED STUDENT BOOK REVIEW

PROJECT TITLE
Web-Based Platform for Faculty Work Management and AI-Assisted Student Book Review

OVERVIEW
The project is a web-based platform with two independent user-facing portals:
1. Admin portal — for reviewing and approving daily work submitted by faculty and providing feedback.
2. Faculty portal — for reviewing handwritten summaries prepared by students for books they read in the library, with assistance from a locally deployed AI system.

The system should be modular and should avoid locking the project into a specific AI model, OCR model, or interaction method too early.

ADMIN PORTAL
The admin portal is intended to allow authorized administrators to:
- View daily work/activity submissions made by faculty.
- Review submitted work.
- Approve work.
- Reject/request changes where required.
- Provide feedback or comments related to the submitted work.
- Maintain a history of submissions, decisions, and feedback.
- Potentially filter or view records by faculty member, date, or status.

FACULTY PORTAL
The faculty portal is intended to allow faculty to:
- Manage/select books for student reading activities.
- Receive student handwritten book-summary submissions.
- Create a grading/evaluation standard for a particular book or reading activity.
- Review AI-assisted evaluations of student submissions.
- Confirm or modify the suggested assessment.
- View previous submissions and evaluations.

FLEXIBLE BOOK-SPECIFIC GRADING STANDARD
The grading standard belongs to the book/reading activity, NOT to an individual student.

A faculty member can define a standard once for a book and reuse it for multiple student submissions.

For example:

Book: The Alchemist
Total Marks: 20

Criteria:
- Characters — 4 marks
  Identify and describe important characters.
- Plot — 5 marks
  Demonstrate understanding of major events.
- Themes — 5 marks
  Explain the central themes.
- Personal Reflection — 3 marks
  Explain what the student learned.
- Accuracy — 3 marks
  Avoid major factual errors.

The important requirement is that the standard is flexible. Different books can have different criteria, descriptions, weights, and total marks.

The system should not hardcode what constitutes a good summary. Instead, the teacher-defined standard should be provided to the AI evaluation component.

STANDARD VERSIONING
A grading standard may change over time. Previous evaluations should remain associated with the version/standard that was used when they were evaluated.

This prevents changing a new rubric from unintentionally changing the interpretation of old student submissions.

AI-ASSISTED BOOK REVIEW PIPELINE
The intended high-level pipeline is:

Student handwritten image
        ↓
Handwriting / document text extraction
        ↓
Extracted student text
        ↓
Teacher-defined grading standard
        ↓
Local AI/LLM evaluation
        ↓
Structured evaluation
        ↓
Faculty verification

The system should ideally separate text extraction from evaluation:
- One local AI/document-processing component determines what the student wrote.
- A local language model evaluates the extracted text against the teacher-defined standard.

The exact models can remain flexible.

AI OUTPUT
The AI should preferably return structured information rather than only free-form text.

Example:

{
  "total_marks": 20,
  "score": 16,
  "criteria": [
    {
      "criterion": "Characters",
      "max_marks": 4,
      "score": 4,
      "evidence": "..."
    },
    {
      "criterion": "Plot",
      "max_marks": 5,
      "score": 4,
      "evidence": "..."
    }
  ],
  "feedback": "..."
}

The faculty member should be able to:
- Accept the suggested grade.
- Modify/override the grade.
- Review the reasoning/evidence.
- Provide or modify final feedback.

The AI should assist the faculty rather than completely replace faculty judgment.

LOCAL AI / RESOURCE CONSTRAINT
A major requirement is that the AI system should be free/local and capable of operating under relatively tight hardware constraints.

Possible implementation direction discussed:
- Local handwriting/document extraction model.
- Lightweight/quantized local LLM.
- Local inference runtime such as Ollama or llama.cpp.

These are implementation candidates rather than fixed requirements. The final AI model should be selected based on actual handwriting quality, accuracy, and available hardware.

TELEGRAM
Telegram was discussed as a possible future interface in which a Telegram bot could support both admin and faculty workflows, potentially combined with a Telegram Mini App.

However, Telegram should NOT be included as a requirement in the current project report. Keep the interface abstract so another interaction method can be used later.

PROPOSED ARCHITECTURE

                         ADMIN PORTAL
                              │
                              │
                              ▼
                        Backend API
                              ▲
                              │
                         FACULTY PORTAL
                              │
                              ▼
                    Student Submissions
                              │
                              ▼
                   Local AI / OCR Pipeline
                              │
                              ▼
                       Local LLM
                              │
                              ▼
                   Structured Evaluation
                              │
                              ▼
                    Faculty Verification

Both portals can share the same backend, authentication system, database, and processing services while remaining separate user interfaces.

PROPOSED TECH STACK
- Frontend: React.js with Vite
- Styling: Tailwind CSS
- Backend: Node.js with Express.js
- API: RESTful API
- Authentication: JWT-based authentication with role-based access control
- Database: PostgreSQL
- AI / OCR: Local AI pipeline for handwriting/text extraction and rubric-based evaluation, using a lightweight LLM and suitable local inference runtime such as Ollama or llama.cpp
- Deployment: Vercel for now

The AI/OCR implementation is intentionally kept somewhat flexible so the specific model/runtime can be changed after testing.

DATABASE CONCEPTS
Potential core entities:

User
- Admin
- Faculty

FacultyWork
- faculty_id
- date
- description
- status
- admin_feedback
- reviewed_at

Book
- title
- author
- metadata

Student
- name
- class
- section

GradingStandard
- book_id
- created_by
- name
- description
- total_marks
- version
- criteria

GradingCriterion
- grading_standard_id
- name
- description
- max_marks
- weight/order

Submission
- student_id
- book_id
- grading_standard_id
- image/submission reference
- extracted_text
- AI score
- faculty/final score
- status

Evaluation
- submission_id
- criterion
- max_marks
- AI marks
- evidence
- faculty override

IMPORTANT DESIGN PRINCIPLES
1. The grading standard is defined by faculty for a book/reading activity and reused across students.
2. The grading standard should be flexible rather than hardcoded.
3. Previous evaluations should retain the standard/version used at the time.
4. AI-generated grades are suggestions and should be verifiable/overridable by faculty.
5. AI/OCR components should be modular and replaceable.
6. The local AI solution should prioritize reasonable resource usage.
7. Avoid committing the project report to Telegram or a specific AI model unless necessary.
8. The admin and faculty interfaces are separate portals but can share a common backend.
9. The system should return structured AI evaluation results so they can be stored and displayed reliably.

REPORT STRUCTURE
The problem statement report follows this general structure:

1. INTRODUCTION
2. PROBLEM STATEMENT
3. OBJECTIVE
4. REQUIREMENTS
5. TECH STACK
6. SUMMARY

PROBLEM STATEMENT CONTENT
The key problems identified are:
- Manual faculty work review.
- Time-consuming review of handwritten student summaries.
- Potentially inconsistent evaluation across submissions.
- Need for flexible, book-specific assessment criteria.
- Difficulty of extracting information from handwritten work.
- Need for local AI processing that can operate with limited computational resources.

OBJECTIVE
The main goal is to develop a lightweight web-based platform that streamlines faculty work review and assists educators in evaluating handwritten student book summaries using locally deployed AI.

Specific objectives:
- Provide an administrative interface for reviewing, approving/rejecting, and commenting on faculty work.
- Provide a faculty interface for managing and reviewing student book summaries.
- Extract handwritten content using an appropriate local text/document processing component.
- Allow faculty to define reusable, flexible grading standards for books.
- Compare student content against the selected standard using a local AI/LLM.
- Generate structured suggested scores and feedback.
- Allow faculty to verify or modify AI-generated assessments.
- Keep the architecture modular enough to change AI models, processing components, or interfaces later.
