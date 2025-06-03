# Article Processing Debug: ka04u000000HdEsAAK

**Generated:** 2025-06-03 12:48:04

## Article Content

```
Disable MFA for Users or Groups Summary This article outlines how to disable Multi-factor Authentication (MFA) for individual users or groups of users in SbPAM. IMPORTANT:Disabling MFA is not recommended per security best practices. Instructions Log-in to SbPAM as an Administrator, then navigate to Users & Groups in the sidebar navigation. Click on a user or a group, then navigate to that principal's�Authentication Connector�tab. Click�Not Required, which will immediately disable the MFA requirement for the user or all users that are a member of the group. �
```

## Assessment Results

- **Update Level**: major
- **Relevance Score**: 0.70
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references discuss modern authentication and MFA, which are relevant to the article's topic of disabling MFA. However, the article does not mention the implications of disabling MFA or the recommended practices, which are critical for security. Therefore, significant updates are needed to align the article with current best practices and provide comprehensive guidance.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.4899)

```
Support for modern authentication will allow you to audit the organizations where MFA is enabled for all users, including service accounts. Required configuration procedure includes several manual steps, as described in the corresponding section: Configuring Microsoft Entra ID App for Auditing SharePoint Online To collect data with modern authentication, you should do the following: Step 1 – Create an Microsoft Entra ID app that will be used for modern authentication. See the Creating and registering a new app in Microsoft Entra ID topic for additional information. Step 2 – Grant required permissions to that application using Microsoft Entra ID app manifest.
```

### Chunk 2 (Score: 0.4874)

```
Change password on next sign in with MFA passwordProfile Yes/No Specifies the password profile for the user. The password in the pr ofile must satisfy the minimum requirements as s pecified by the passwordPolicies property. By default, a strong password is required. City city Example: "London" The city where a user is located.
```

### Chunk 3 (Score: 0.4770)

```
Change password on next sign in passwordProfile Yes/No Specifies the password profile for a user. The password in the pr ofile must satisfy the minimum requirements as s pecified by the passwordPolicies property. By default, a strong password is required. Change password on next sign in with MFA passwordProfile Yes/No Specifies the password profile for the user.
```

### Chunk 4 (Score: 0.4369)

```
Unchecking this option allows you to configure access to be granted at a future time. v10.7 Step 4 – The new user displays in the list on the Console Access page. Repeat these steps for each trustee to be granted console access. Once the first user with the role of Administrator has been added, the Builtin Administrator account can be disabled by that user.
```

### Chunk 5 (Score: 0.4251)

```
Using Modern Authentication with SharePoint Online This option is recommended for organizations that use modern authentication as the identity management approach, having multi-factor authentication (MFA) enabled for their user accounts. In this scenario,Netwrix Auditor will access the cloud-based infrastructure via v10.7 Microsoft Graph and other modern APIs, being authenticated through a pre-configure d Microsoft Entra ID application with appropriate access permissions. If you plan to implement such scenario, you should register an Microsoft Entra ID app manually and provide its settings to Auditor when configuring a monitored item. Support for modern authentication will allow you to audit the organizations where MFA is enabled for all users, including service accounts.
```

