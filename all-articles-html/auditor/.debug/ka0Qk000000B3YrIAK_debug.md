# Article Processing Debug: ka0Qk000000B3YrIAK

**Generated:** 2025-06-02 13:04:34

## Article Content

```
Netwrix Auditor Health Log Contains EventID 3230 Symptom Netwrix Auditor (NA) System Health Log contains EventID 3230 for a SharePoint Online monitoring plan: Cause The lock status for a site collection means that this is a personal site collection that has been locked. Personal site collections are not intended to be collected, and the error withNo accesslock status can be fixed by unlocking the site. NA for SharePoint is intended as an enterprise solution and would be best to be configured for public documents only. IMPORTANT:Please consider that this event does not affect data collection. Resolution As a workaround, you can exclude personal site collections from being audited by editing theOmitSitScStoreList.txtfile located in the following default path: NOTE:To determine your Working Folder location, you can run the following PowerShell command. If this script does not return a value, then your Working Folder is our default location of�C:\ProgramData\Netwrix Auditor\. For additional information on how to configure your SharePoint Online monitoring scope, refer to the following article:SharePoint Online Monitoring Plans � Monitoring Scope � v10.6. Related Articles SharePoint Online Monitoring Plans � Monitoring Scope � v10.6.
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.70
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide additional context and procedural steps related to Netwrix Auditor, which are relevant to the article. However, the article may need minor updates for clarity and to correct any potential typos or formatting issues.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.6737)

```
Step 3 – Navigate to the Monitored computers list and add a server where the Netwrix Auditor Server resides. Step 4 – Navigate to the Audit Database tab and select Write event descriptions to Audit Database if you want to see the exact error or warning text. Make sure that Audit Database settings are configured properly, follow the Audit Database Step 5 – Click Configure next to Audit archiving filters and select the Netwrix Auditor System Health Log filter in the Inclusive Filters list. This procedure describes the basic steps, required for creation of the monitoring plan that will be used to collect data on Netwrix Auditor health status events.
```

### Chunk 2 (Score: 0.6510)

```
CAUTION: Folder associated with NETWRIX AUDITOR must be excluded from antivirus scanning. See the Antivirus Exclusions for Netwrix Auditor knowledge base article for additional information. You can configure your IT Infrastructure for monitoring in one of the following ways: Table 1: Parameter Description • Log Level • Alert Level • Syslog Level Set to "Info". • Enable Audit Log Send to Syslog Server in Audit Log Settings Send to Syslog Server in Access Log Settings Select these checkboxes.
```

### Chunk 3 (Score: 0.6472)

```
https:// Corp.sharepoint.com/* Contains a list of event IDs to be event ID omiteventloglist.txt excluded from the Netwrix Auditor System Health event log. For example: Table 1: File Description Syntax 1001 Only add known error or warning events, otherwise you may lose important data. omitreadstorelist.txt Contains the SharePoint Online lists, documents, etc., to be excluded from being monitored for read access. https://URL For example: https:// Corp.sharepoint.com/* *list/document.docx omituserreadstorelist.txt Contains a list of user accounts to be excluded from read access monitoring.
```

### Chunk 4 (Score: 0.6420)

```
Step 2 – Make sure that the Enable event log collection checkbox is selected. Specify the name for the new plan, for example, "Netwrix Auditor Health Status". Step 3 – Navigate to the Monitored computers list and add a server where the Auditor server resides. Step 4 – On the General tab, click Configure next to Alerts.
```

### Chunk 5 (Score: 0.6400)

```
Step 1 – Start Netwrix Auditor Event Log Manager and create the new monitoring plan. Step 2 – Make sure that the Enable event log collection checkbox is selected. Specify the name for the new monitoring plan, for example, "Netwrix Auditor Health Status". Step 3 – Navigate to the Monitored computers list and add a server where the Netwrix Auditor Server resides.
```

