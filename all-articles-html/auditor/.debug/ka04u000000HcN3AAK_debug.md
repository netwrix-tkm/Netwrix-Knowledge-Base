# Article Processing Debug: ka04u000000HcN3AAK

**Generated:** 2025-06-02 17:29:45

## Article Content

```
Exporting information on account lockout events
```

## Assessment Results

- **Update Level**: major
- **Relevance Score**: 0.80
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide detailed information on auditing and monitoring account lockout events, which is directly relevant to the article's topic. However, the article lacks specific procedures and tools mentioned in the references, indicating a need for significant content updates to align with current practices.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.5660)

```
◦ To export filtered data to PDF or CSV, click Export data. You can also configure and receive alerts on the events you are interested in. See the following topics for additional information: Alerts View and Search Collected Data Subscriptions Monitored Events The Add-On supports monitoring of the following syslog events from CyberArk PAS: Event ID Description Password verification by Central Policy Manager (success) Password stored in EPV changed by Central Policy Manager (success) Password reconciliation by Central Policy Manager (success) Password verification by Central Policy Manager (failure) Table 1: Event ID Description 57 Password stored in Enterprise Password Vault changed by Central Policy Manager (failure) 60 Password reconciliation by Central Policy Manager (failure) 130 Password stored in Enterprise Password Vault disabled by Central Policy Manager 295 User retrieved a password stored in Enterprise Password Vault 300 User session started in Privileged Session Manager 302 User session ended in Privileged Session Manager 308 User used a password stored in Enterprise Password Vault 411 A window was activated by user in Privileged Session Manager v10.7 Event ID Description Password stored in Enterprise Password Vault changed by Central Policy Manager (failure) Password reconciliation by Central Policy Manager (failure) Password stored in Enterprise Password Vault disabled by Central Policy Manager User retrieved a password stored in Enterprise Password Vault 300 User session started in Privileged Session Manager 302 User session ended in Privileged Session Manager User used a password stored in Enterprise Password Vault A window was activated by user in Privileged Session Manager Maintenance and Troubleshooting The Add-On operations are logged into the SyslogService.txt file. This file is located in the same folder as SyslogService.exe.
```

### Chunk 2 (Score: 0.5217)

```
Scenario A: Advanced audit policies Enable the following Advanced audit policies for the target machines: Audit entry Event ID Success/Failure Account Logon Audit Credential Validation 4776 Failure Audit Kerberos Authentic ation 4771 Failure Service Audit Other Account Logon Events 4776 Failure Account Management Audit User Account Management 4740 Success Logon/Logoff Audit Logon 4625 Failure Audit Account Lockout 4625 Failure Scenario B: Basic audit policies Enable the following basic audit policies for the target machines: Audit entry Event ID Success/Failure Audit logon events 4625 Failure Audit account logon events 4776, 4771 Failure Audit account management 4740 Success v10.7 Examining Lockouts To start using Netwrix Account Lockout Examiner, download it from Netwrix web site. Once the download completes, run the executable from your browser menu or from your Downloads folder. To find out why an Active Directory account was locked out, perform the following steps: 1. Set up the auditing as described in Planning and Preparation section.
```

### Chunk 3 (Score: 0.4926)

```
Enabled Examine all domain controllers Select this option if you want to examine all domain controllers to detect potential lockout reason. Disabled v10.7 Once the examination completes, you will be presented with a list of reasons why the account you supplied is being locked out. Modifying product settings After you click Settings in the main window, you can apply the following options: Option Description Default Examining For safety reasons, Netwrix Account Lockout Examiner by default does not connect to the unknown and Skip unresolved IP addresses Enabled potentially dangerous IP addresses. See this Knowledge Base article for more information.
```

### Chunk 4 (Score: 0.4898)

```
Set up the auditing as described in Planning and Preparation section. Download the application onto a computer within the domain where lockouts happen. Run the application. When prompted, accept the end-user license agreement.
```

### Chunk 5 (Score: 0.4856)

```
When the add-on operates normally there should be no errors and the following types of events should appear regularly: Regular events from *splunk\ta-netwrix-auditor-add-on-forsplunk_netwrix_auditor_api_input_* source with POST requests to the Netwrix Auditor API. Regular events from *splunk\ta-netwrix-auditor-add-on-forsplunk_netwrix_auditor_api_input_* source with checkpoint update with new ContinuationMarks received from Netwrix Auditor API. Events from *\splunk\metrics.log source with information about indexed volumes. v10.7 Account Lockout Examiner Overview Netwrix Account Lockout Examiner helps IT administrators to discover why an Active Directory account keeps locking out, so they can quickly identify the lockout reason and restore normal operations.
```

