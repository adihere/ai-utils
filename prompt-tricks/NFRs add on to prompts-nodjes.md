## Production-Grade Implementation Requirements for Node.js Projects
(A Few points are opinionated)

Use Turborepo monorepo structure with separate `apps` (Next.js/NestJS) and shared `packages` (UI/utils)
Enforce Node.js LTS version 
Implement layered logging (debug/info/error) with correlation IDs and environment toggle
Write JSDoc comments for all complex functions including params, returns, and error cases
Add healthcheck endpoints (`/_health`) with DB connection tests
Implement proper error handling with contextual messages (no `console.error` raw)
Use environment variables for secrets with validation on app startup
Add performance metrics (response times, memory usage)
Follow RESTful practices for APIs: proper status codes, versioning, and pagination
Include `// TODO-AI` comments where human review is critical
