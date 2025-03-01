Add 
PostHog (Learning analytics tracks user behavior and application performance)
fal.ai API calls for video ,  image , audio generation , video processing
Mistral AI calls using langchain js generates text-based tutorial scripts


Have landing page with demo videos , sign up page , login page 
Content Generation page for parents
Parent Input: Parents provide a one liner description of the topic they want their child to learn. Selects the target age of the child. Selects from a drop down of audio accents of five voices. The app transforms the parent's input into a comprehensive 3-minute audio-visual tutorial by following below steps
1)  Call Mistral to create an age appropriate tutorial with text of 250 to 300 words.The steps should create metadata of five labels that captures the topic.  Generate three multiple choice questions related to the topic so as to reinforce learning and assess understanding. 
2) The text is converted into audio for voiceover narration by calling fal.ai api call.Text-to-speech technology converts the script into clear, natural-sounding narration.
Background music or sound effects may be added to increase appeal. 
3) The text is passed to fal.api text to image model of fal-ai/recraft-20b to create a set of 10 images 
4) The text is passed to fal.ai text to video model of fal-ai/kling-video/v1/standard/text-to-video to create a video clip of 5 seconds 
5) The audio , images and video are combined into a single video clip of 2 to 3 minutes using fal-ai/ffmpeg-api/compose. The content is timed to sync with the narration, enhancing understanding and engagement
In all steps info is stored in back end supabase database 

A page for view of pre-generated content from the community library
View content from the available media
Have a search to search the metadata labels associated with content 

Child interface - view the content allocated by parent
The child views the content set for them by parents. The quiz functionality is appended to the end of the tutorial.By scoring more than 2 of 3 right will give a kudos animation display on screen. 
Parent-Child Chat Bridge to send message to parent about content

Parent dashboard page accessible only by parent 
Progress syncs between parent/child accounts to let parents see content usage of child 
Progress tracking wall
Parent-Child Chat Bridge to send and receive message from and to child about content
  


Layered Logging: Implement layered logging (debug/info/error) with correlation IDs and environment toggle

Use a logging framework that supports different log levels
Include correlation IDs for request tracing
Allow toggling of log levels based on the environment


Documentation: Write JSDoc comments for all complex functions including params, returns, and error cases

Health Checks: Add healthcheck endpoints (/_health) with DB connection tests

Error Handling: Implement proper error handling with contextual messages

Create custom error classes for different types of errors
Use try-catch blocks with async/await for asynchronous operations
Avoid using console.error for raw error logging
Environment Variables: Use environment variables for secrets with validation on app startup

Store sensitive information like API keys and database credentials as environment variables
Validate the presence and format of required environment variables when the application starts


Performance Metrics: Add performance metrics (response times, memory usage)

Use monitoring tools to track application performance
Implement custom metrics for critical operations
RESTful Practices: Follow RESTful practices for APIs: proper status codes, versioning, and pagination

Use appropriate HTTP status codes for different scenarios
Implement API versioning to manage changes
Add pagination for endpoints that return large datasets
Code Review: Include // TODO-AI comments where human review is critical

Implement proper security measures, including input validation and protection against common vulnerabilities

Implement proper separation of concerns by layering components (web, logic, data access)

Wrap common utilities as npm packages to reduce code duplication and improve manageability


