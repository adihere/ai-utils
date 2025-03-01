## Production-Grade Implementation Requirements for Node.js Projects
(A Few points are opinionated)

### Key Requirements

- **Monorepo Structure**: Use Turborepo monorepo structure with separate `apps` (Next.js/NestJS) and shared `packages` (UI/utils)
- **Node.js Version**: Enforce Node.js LTS version
  - Use the latest stable LTS version (even-numbered) for production environments

- **Layered Logging**: Implement layered logging (debug/info/error) with correlation IDs and environment toggle
  - Use a logging framework that supports different log levels
  - Include correlation IDs for request tracing
  - Allow toggling of log levels based on the environment

- **Documentation**: Write JSDoc comments for all complex functions including params, returns, and error cases

- **Health Checks**: Add healthcheck endpoints (`/_health`) with DB connection tests

- **Error Handling**: Implement proper error handling with contextual messages
  - Create custom error classes for different types of errors
  - Use try-catch blocks with async/await for asynchronous operations
  - Avoid using `console.error` for raw error logging

- **Environment Variables**: Use environment variables for secrets with validation on app startup
  - Store sensitive information like API keys and database credentials as environment variables
  - Validate the presence and format of required environment variables when the application starts

- **Performance Metrics**: Add performance metrics (response times, memory usage)
  - Use monitoring tools to track application performance
  - Implement custom metrics for critical operations

- **RESTful Practices**: Follow RESTful practices for APIs: proper status codes, versioning, and pagination
  - Use appropriate HTTP status codes for different scenarios
  - Implement API versioning to manage changes
  - Add pagination for endpoints that return large datasets

- **Code Review**: Include `// TODO-AI` comments where human review is critical

- Implement proper security measures, including input validation and protection against common vulnerabilities
- Implement proper separation of concerns by layering components (web, logic, data access)
- Wrap common utilities as npm packages to reduce code duplication and improve manageability
