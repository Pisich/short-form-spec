# SFS: Email and Password Login

**ID:** SFS-001
**Status:** Implemented
**Date:** 2026-09-28
**Version / PR:** v1.4.0 / #212

## Summary
Users can sign in with an email and password and receive a session that lasts 7 days. This replaces anonymous access to the dashboard.

## Behavior
- Valid credentials create a session and redirect to `/dashboard`.
- Invalid credentials show a generic "Incorrect email or password" message.
- After 5 failed attempts in 10 minutes, the account is locked for 15 minutes.
- Sessions expire after 7 days of inactivity.
- Logging out invalidates the session immediately.

## Interfaces and data
```
POST /api/login
Body:    { "email": string, "password": string }
200:     { "sessionToken": string, "expiresAt": ISO8601 }
401:     { "error": "invalid_credentials" }
429:     { "error": "account_locked", "retryAfterSeconds": number }
```
Passwords are stored as bcrypt hashes in `users.password_hash`.

## Key decisions
- Session tokens are stored in an HttpOnly cookie.
- Error messages never reveal whether the email exists.
- Lockout is per account, not per IP.

## Limitations and out of scope
- No password reset (tracked separately).
- No social login or multi-factor authentication.

## Verification
- `npm test auth` runs the login and lockout tests.
- Manual: 5 wrong passwords in a row should return 429 on the 6th attempt.

## References
- Working spec: docs/specs/login-working-spec.md
- PR: #212