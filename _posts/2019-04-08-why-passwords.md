---
title: "Why do we still use passwords?"
layout: post
...

Almost all websites let you reset your password via email. This means that
access to your email account is already going to imply access to almost all
websites you have an account with. Instead of authenticating people with
passwords, why don’t we authenticate them via email?

If you had to do this on every visit it'd be terrible. But most websites let
you stay logged in for a while (or indefinitely) if you don't log out.
Logging in periodically by clicking a link in an email feels acceptable.

This is basically just using email as a kind of SSO protocol. Actual
SSO via Google or some provider might be a better flow in certain cases. But
the point is if you allow password resets via email, you're already using
email as a kind of SSO.

You can already approximate this flow with a lot of sites by just choosing an
ephermeral random password that you immediately forget, and using password
reset links every time you need to "login".
