# SSO Authentication

## LDAP

If LDAP is enabled and [configured properly](../installation/backend-config.md), users will be able to log in with their LDAP credentials. If the user does not already have an account in Mealie, then one will be created.

If the user already has an account in Mealie and wants to use their LDAP credentials instead, then you can go to the **User Management** page in the admin panel and change the "Authentication Backend" from `Mealie` to `LDAP`. If for whatever reason, the user no longer wants to use LDAP authentication, then you can switch this back to `Mealie`.

!!! warning "Head's Up"
    If you switch a user from `LDAP` to `Mealie` who was initially created by LDAP, then the user will have to reset their password through the password reset flow.

## JWT Authentication

You can configure Grafana to accept a JWT token provided in the HTTP header. The token is verified using a JSON Web Key Set provided by the configured JWKS endpoint.

This method of authentication is useful for integrating with identity-aware proxies, in order to enable and configure JWT Authentication you need to [set the appropriate configuration parameters](../installation/backend-config.md).
