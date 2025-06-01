# Article Processing Debug: ka0Qk000000BmvlIAC

**Generated:** 2025-06-01 00:18:26

## Article Content

```
System Cannot Find the Path Specified in Logon Activity Monitoring Plan Symptoms The following error is prompted in Health Log for the Logon Activity monitoring plan:Source: Active Directory Logon Activity Audit Service Event ID: 5004 Monitoring plan: %monitoring_plan_name% Data collection has failed. Error: The system cannot find the path specified The following error is prompted in Health Log for the Logon Activity monitoring plan: No data is collected in your affected monitoring plan. No data is collected in your affected monitoring plan. Causes Netwrix Auditor Logon Activity Audit Service is corrupted or cannot be found. Resolutions Upgrade your Netwrix Auditor instance to the latest version to repair the corrupted service. Refer to the following article for additional information:Installation � Upgrade to the Latest Version ? v10.6. Upgrade your Netwrix Auditor instance to the latest version to repair the corrupted service. Refer to the following article for additional information:Installation � Upgrade to the Latest Version ? v10.6. If the latest Netwrix Auditor version is installed in your environment, you can repair your Netwrix Auditor instance. Refer to the following article for additional information:How to Repair Netwrix Auditor Installation. If the latest Netwrix Auditor version is installed in your environment, you can repair your Netwrix Auditor instance. Refer to the following article for additional information:How to Repair Netwrix Auditor Installation. Related articles Installation � Upgrade to the Latest Version ? v10.6 How to Repair Netwrix Auditor Installation
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.80
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide relevant troubleshooting and configuration information for Netwrix Auditor, which is pertinent to the article's focus on logon activity monitoring issues. However, the article may need minor updates to reflect the latest version (v10.7) and ensure consistency in terminology and procedures.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.6827)

```
v10.7 Logon Activity Netwrix Auditor relies on native logs for collecting audit data. Therefore, successful change and access auditing requires a certain configuration of native audit settings in the audited environment and on the Auditor console computer. Configuring your IT infrastructure may also include enabling certain built-in Windows services, etc. Proper audit configuration is required to ensure audit data integrity, otherwise your change reports may contain warnings, errors or incomplete audit data.
```

### Chunk 2 (Score: 0.6678)

```
Data collection for this monitoring plan might not have been launched two times yet or there was no data collection after this change; therefore, audit data has not been written to the Audit Database yet. Some settings in Auditor are configure d incorrectly. Contact your Auditor administrator to make sure that: v10.7 Troubleshooting This section provides instructions on how to troubleshoot issues that you may encounter while using Netwrix Auditor. If your issue is not listed in the table below, try searching Netwrix Knowledge Base.
```

### Chunk 3 (Score: 0.6567)

```
Step 1 – Start Netwrix Auditor Event Log Manager and create the new monitoring plan. Step 2 – Make sure that the Enable event log collection checkbox is selected. Specify the name for the new monitoring plan, for example, "Netwrix Auditor Health Status". Step 3 – Navigate to the Monitored computers list and add a server where the Netwrix Auditor Server resides.
```

### Chunk 4 (Score: 0.6499)

```
Netwrix recommends to store all audit data on the same default SQL Server instance. "No plans found" text in the Monitoring plan field. Contact your Auditor Global administrator or Configurator to make sure that the monitoring plans exist and are properly configured. I see a blank window instead of a report.
```

### Chunk 5 (Score: 0.6423)

```
Step 2 – Make sure that the Enable event log collection checkbox is selected. Specify the name for the new plan, for example, "Netwrix Auditor Health Status". Step 3 – Navigate to the Monitored computers list and add a server where the Auditor server resides. Step 4 – On the General tab, click Configure next to Alerts.
```

