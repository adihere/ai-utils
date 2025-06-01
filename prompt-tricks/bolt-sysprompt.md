Create a full-stack web application with modern frontend and Node.js backend following enterprise-grade best practices:

## Frontend Architecture
- Build a modern single-page application using component-based architecture
- Implement proper component structure with separation of concerns
- Use state management solution for application state
- Add client-side routing for navigation
- Include modern CSS framework for styling
- Create reusable components following DRY principles
- Implement proper error boundaries and loading states
- Support responsive design and accessibility standards

## Backend
- Use Node.js LTS version (enforce in package.json engines field)
- Implement layered architecture: routes → controllers → services → data access


## Layered Logging System
- Implement structured logging with multiple levels (debug, info, warn, error)
- Create custom Logger class with service-specific instances
- Add request logging middleware with correlation IDs
- Include stack trace logging for debugging environments
- Configure different log outputs for development/production
- Use JSON format for production logs to enable log aggregation

## Documentation Standards
- Add comprehensive JSDoc comments for all functions
- Document parameters with types and descriptions
- Include @returns documentation with type information
- Document @throws for error cases
- Example format:
```
/**
 * Retrieves user by ID with comprehensive error handling
 * @param {string} userId - The unique identifier for the user
 * @param {Object} options - Configuration options
 * @param {boolean} options.includeProfile - Whether to include user profile
 * @returns {Promise} User object with profile data
 * @throws {Api404Error} When user is not found
 * @throws {ValidationError} When userId format is invalid
 */
```

## Health Check Implementation
- Create /_health endpoint returning JSON status
- Test database connection and critical dependencies in health check
- Include system information (uptime, memory usage, Node.js version)
- Return proper HTTP status codes (200 for healthy, 503 for unhealthy)
- Add dependency checks for external services (Redis,supabase, google api,  third-party APIs)
- Keep health checks lightweight and fast to avoid system strain
- Differentiate between critical and non-critical dependencies

## Error Handling Architecture
- Create BaseError class extending Error with statusCode and isOperational properties
- Implement specific error classes: Api404Error, ValidationError, DatabaseError
- Add centralized error handling middleware
- Use async/await with try-catch blocks throughout asynchronous operations
- Include contextual error messages with request correlation IDs
- Implement proper error logging and user-friendly responses
- Handle uncaught exceptions and unhandled promise rejections

## Environment Variables Management
- Create .env.example file with all required variables
- Implement startup validation for required environment variables
- Use dotenv for environment variable loading
- Create config module that validates and exports typed configuration
- Store sensitive information like API keys and database credentials securely

## RESTful API Design
- Implement proper HTTP methods (GET, POST, PUT, DELETE)
- Use appropriate status codes (200, 201, 400, 404, 500)
- Add API versioning (/api/v1/)
- Implement pagination with limit/offset or cursor-based approaches
- Include proper response formatting with data/error/meta structure
- Add comprehensive request/response validation
- Follow REST conventions for resource naming and operations

## Security Implementation
- Add security headers middleware for protection
- Implement rate limiting to prevent abuse
- Add comprehensive input validation and sanitization
- Use secure password hashing algorithms
- Implement proper authentication and session management
- Add CORS configuration for cross-origin requests
- Validate and sanitize all user inputs to prevent injection attacks
- Implement protection against common vulnerabilities (XSS, CSRF, SQL injection)

## Architecture & Code Organization
/src
  /components (Frontend components)
  /views (Frontend pages/views)
  /stores (State management)
  /services (API communication layer)
  /utils (Frontend utilities)
/server
  /routes (Express route definitions)
  /controllers (Request handlers and response formatting)
  /services (Business logic layer)
  /models (Data access layer)
  /middleware (Custom middleware functions)
  /utils (Server utilities and helpers)
  /config (Configuration management)
```

## Database Integration
- Use modern ORM for type-safe database operations
- Implement proper connection pooling and management
- Add database migrations for schema versioning
- Include seed data for development environment
- Implement proper transaction handling for data consistency
- Add database health monitoring

## Dependency Management
- Ensure all dependencies are up to date and vulnerability-free
- Use npm audit for security scanning
- Regularly clean node_modules cache to avoid stale dependencies
- Monitor and update dependencies to mitigate security risks


##Supabase Setup and Configuration
- Create a new Supabase project and configure environment variables in Bolt.new
- Set up database connection using Supabase client with proper authentication
- Configure Row-Level Security (RLS) policies for data protection and user-specific access
- Enable real-time subscriptions for live data synchronization across devices
- Implement Supabase Auth integration for seamless user authentication


Generate a complete application structure with all these practices implemented, including example endpoints, comprehensive error handling, structured logging, security measures, and production-ready configurations.

