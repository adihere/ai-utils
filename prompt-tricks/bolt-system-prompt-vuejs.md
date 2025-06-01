Create a full-stack Vue.js application with Node.js backend following enterprise-grade best practices:

## Frontend (Vue.js)
- Build a Vue 3 application using Composition API
- Implement proper component structure with separation of concerns
- Use Pinia for state management
- Add Vue Router for navigation
- Include Tailwind CSS for styling
- Create reusable components following DRY principles
- Implement proper error boundaries and loading states

## Backend (Node.js/Express)
- Use Node.js LTS version (enforce in package.json engines field)
- Implement layered architecture: routes → controllers → services → data access

## Node.js Version Enforcement

## Layered Logging System
- Implement Winston logger with multiple levels (debug, info, warn, error)
- Create custom Logger class with service-specific instances
- Add request logging middleware
- Include stack trace logging for debugging
- Configure different log outputs for development/production

## Documentation Standards
- Add comprehensive JSDoc comments for all functions
- Document parameters with types and descriptions
- Include @returns documentation with type information
- Document @throws for error cases

## Health Check Implementation
- Create /_health endpoint returning JSON status
- Test database connection in health check
- Include system information (uptime, memory usage)
- Return proper HTTP status codes (200 for healthy, 503 for unhealthy)
- Add dependency checks (Redis, external APIs if applicable)

## Error Handling Architecture
- Create BaseError class extending Error with statusCode and isOperational properties
- Implement specific error classes: Api404Error, ValidationError, DatabaseError
- Add centralized error handling middleware
- Use async/await with try-catch blocks throughout
- Include contextual error messages with request IDs
- Implement proper error logging and user-friendly responses

## Environment Variables Management
- Create .env.example file with all required variables
- Implement startup validation for required environment variables
- Use dotenv for environment variable loading
- Create config module that validates and exports typed configuration

## RESTful API Design
- Implement proper HTTP methods (GET, POST, PUT, DELETE)
- Use appropriate status codes (200, 201, 400, 404, 500)
- Add API versioning (/api/v1/)
- Implement pagination with limit/offset or cursor-based
- Include proper response formatting with data/error/meta structure
- Add request/response validation with Joi or similar

## Security Implementation
- Add helmet.js for security headers
- Implement rate limiting with express-rate-limit
- Add input validation and sanitization
- Use bcrypt for password hashing
- Add CORS configuration
- Validate and sanitize all user inputs
- Implement SQL injection prevention

## Architecture & Code Organization

## Database Integration
- Use Prisma ORM for type-safe database operations
- Implement proper connection pooling
- Add database migrations
- Include seed data for development
- Implement proper transaction handling

## Additional Requirements
- Add comprehensive error logging with context
- Implement request correlation IDs
- Create middleware for authentication and authorization
- Add input validation schemas
- Include API documentation with Swagger/OpenAPI
- Implement graceful shutdown handling
- Add unit and integration tests setup
- Configure ESLint and Prettier for code quality

Generate a complete application structure with all these practices implemented, including example endpoints, proper error handling, logging, and security measures.
