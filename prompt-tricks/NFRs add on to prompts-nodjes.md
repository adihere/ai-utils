## Production-Grade Implementation Requirements for Node.js Projects
(A Few points are opinionated)

1. Use Turborepo monorepo structure with separate `apps` (Next.js/NestJS) and shared `packages` (UI/utils)

2. Enforce Node.js LTS version with `.nvmrc` + `engine-strict` in `.npmrc`

3. Implement layered logging (debug/info/error) with correlation IDs and environment toggle

4. Write JSDoc comments for all complex functions including params, returns, and error cases

5. Achieve 80%+ test coverage with Jest/Testing Library, including edge cases

6. Validate all user inputs and API responses with Zod schemas

7. Use exact package versions (`package-lock.json`) and audit dependencies weekly

8. Add healthcheck endpoints (`/_health`) with DB connection tests

9. Document key architectural decisions in ADRs (Architecture Decision Records)

10. Configure CI/CD pipeline with lint-test-build-deploy stages

11. Implement proper error handling with contextual messages (no `console.error` raw)

12. Use environment variables for secrets with validation on app startup

13. Add performance metrics (response times, memory usage)

14. Follow RESTful practices for APIs: proper status codes, versioning, and pagination

15. Include `// TODO-AI` comments where human review is critical
