# Vibe Quiz Generation App Prompts

## Project Architecture & Setup

```
Design the architecture for a quiz generation app with:
- Next.js frontend hosted on Vercel
- Serverless backend functions
- AI-powered quiz generation using Mistral AI via LangChain.js
- User authentication for saving quizzes
- Database for storing generated quizzes and user progress

Include component diagrams and data flow between systems.
```

## AI Integration Prompt

```
Implement a LangChain.js integration with Mistral AI that:
- Takes user-provided text content and desired number of questions
- Analyzes the text to extract key concepts and information
- Generates engaging multiple-choice questions with 4 options per question
- Ensures one correct answer per question with clear explanations
- Returns structured JSON with questions, options, correct answers, and explanations
- Implements proper error handling and retry logic

The output should follow this format:
{
  "questions": [
    {
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correctIndex": 0,
      "explanation": "Explanation of why this answer is correct"
    }
  ]
}
```

## Frontend User Interface

```
Create a vibrant, engaging React component for the quiz generation interface with:
- Text input area for pasting content or entering a topic
- Number selector for choosing question count (3-10)
- Quiz theme/style selector with visual previews
- Generate button with animated loading state
- Preview panel showing generated questions
- Error handling with user-friendly messages
- Mobile-responsive design with smooth animations

Include the necessary state management and API integration code.
```

## Quiz Presentation Interface

```
Design an interactive quiz presentation component that:
- Displays one question at a time with a progress indicator
- Shows multiple-choice options with hover/selection effects
- Implements a countdown timer for each question (configurable)
- Provides immediate feedback on answer selection
- Shows explanation after answering
- Tracks and displays running score
- Includes confetti animation for correct answers
- Shows final score with share options at completion

Include animations, transitions, and sound effects to create an engaging experience.
```

## Backend Quiz Generation

```
Implement a serverless function that:
- Receives text content and number of questions as input
- Sanitizes and processes the input text
- Calls Mistral AI through LangChain.js to generate quiz questions
- Validates the AI response for proper format and content
- Randomizes question order and option order for variety
- Returns a structured JSON response with quiz data
- Implements caching for similar requests to improve performance
- Handles errors gracefully with informative messages

Include rate limiting, error handling, and performance optimization.
```

## Quiz Data Management

```
Create a data management system that:
- Stores generated quizzes in vercel postgres database
- Associates quizzes with user accounts (if authenticated)
- Implements a public/private sharing model for quizzes
- Tracks quiz play statistics (completion rate, average score)
- Allows users to favorite or bookmark quizzes
- Implements tagging for categorization and search
- Provides an API for retrieving user's quiz history

Include database schema and API endpoint specifications.
```

## Quiz Customization Options

```
Implement quiz customization features that allow users to:
- Adjust time limits per question (5-60 seconds)
- Choose visual themes/skins for the quiz interface
- Toggle sound effects and animations
- Select difficulty levels that affect question complexity
- Enable/disable explanations after questions
- Choose between strict mode (one attempt) or practice mode (multiple attempts)
- Customize the quiz completion screen with personalized messages

Include UI components and settings management code.
```

## Social Sharing Integration

```
Create social sharing functionality that:
- Generates shareable links to quizzes
- Creates preview cards for social media sharing
- Allows embedding quizzes in other websites
- Implements challenge features to invite friends
- Tracks and displays leaderboards for competitive quizzes
- Provides options to share results on social platforms
- Generates achievement badges for quiz completion

Include API integrations with popular social platforms.
```

## Analytics Dashboard

```
Design an analytics dashboard for quiz creators that shows:
- Number of times each quiz has been played
- Average scores and completion rates
- Question-level analytics (which questions are missed most often)
- User engagement metrics (time spent, return rate)
- Geographic distribution of players
- Device and browser statistics
- Conversion rates for call-to-action elements

Include data visualization components and filtering options.
```

## Deployment & Performance

```
Implement deployment and performance optimization:
- Configure Vercel deployment with environment variables
- Set up CI/CD pipeline for automated testing and deployment
- Implement edge caching for faster global performance
- Optimize assets for fast loading on mobile devices
- Configure monitoring and alerting for system health
- Implement progressive loading for better perceived performance
- Add offline support with service workers

Include configuration files and performance testing scripts.


Apply good NFR practice as below

Documentation: Write JSDoc comments for all complex functions including params, returns, and error cases

Error Handling: Implement proper error handling with contextual messages

Create custom error classes for different types of errors
Use try-catch blocks with async/await for asynchronous operations

Environment Variables: Use environment variables for secrets with validation on app startup

Store sensitive information like API keys and database credentials as environment variables
Validate the presence and format of required environment variables when the application starts

Implement proper security measures, including input validation and protection against common vulnerabilities

Wrap common utilities as npm packages to reduce code duplication and improve manageability

Implement proper separation of concerns by layering components (web, logic, data access)

Layered Logging: Implement layered logging (debug/info/error) with correlation IDs and environment toggle
-Allow toggling of log levels based on the environment
