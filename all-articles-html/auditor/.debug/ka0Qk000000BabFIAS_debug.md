# Article Processing Debug: ka0Qk000000BabFIAS

**Generated:** 2025-06-03 12:22:25

## Article Content

```
How to Read Netwrix Auditor Logs What to expect from Netwrix Auditor logs Logs can reveal many aspects of operations for all Netwrix Auditor Collectors and Services. Not all log information is related to errors, in fact most of the text will walk you through the collection process. Where are the logs? The Netwrix Auditor Logs can be found by default at "C:ProgramDataNetwrix AuditorLogs" on the Netwrix Auditor Server. There is certainly an overwhelming amount of logs to choose from. To efficiently view logs, first choose which collector you would like to troubleshoot or investigate. Most log folders display the name of the related collector. Some logs are nested and may take longer to find unless you build familiarity with the file structure. Data Collection CoreThis is an example of a less obvious log location. This directory has logs for collectors like File Server Auditing and Logon Activity. Audit CoreThis directory will include logs for Netwrix Auditor Core Services. For example, Technical Support will visit these logs in instances where data may not be getting stored in SQL. In this example, we would look at the NwArchiveSVC because the Netwrix Auditor Archive Service is responsible for storing data in SQL. How to read the logs Due to variance between logs, the general rule of thumb when viewing logs is to start with the largest sized log. Alternatively, you can choose to start with log files with names that match the collector in question. In this example, they are one in the same: Once you open a log, you will want to either scroll to the bottom or use the handy keystroke CONTROL + ENDLog data is formatted in columns. From left to right, data is presented as: Date/Time, Message Type, Process Code, Process Name, Process description/Error Description Unless you are viewing logs to better understand collector processes, you will want to filter through the log using a find function. Here are useful ways to find errors and warnings Control + F warn err error failed tracing (This may not be present in every log, but if it is, you can see when a collection begins, follow it through, and watch for signs of root cause) names of servers and domain controllers (If you suspect issues with collections from identified machines, you may find clues by searching their names in the logs) Ultimately, learning logs requires the ability to watch for patterns. While extremely useful, logs will not always lead to a direct resolution. They tend to act as a stepping stone along the path to resolution. Sending logs to Technical Support In most cases, Technical Support will request logs for tickets not resolved on initial contact. If you would like to anticipate this and possibly expedite resolution, you can prepare the logs using the steps seenhere.
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.80
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide relevant information about Netwrix Auditor logs and their management, which complements the article. However, there are minor updates needed to ensure consistency with the latest version and practices mentioned in the references.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.7229)

```
v10.7 Review Past Event Log Entries Netwrix Auditor Event Log Manager collects event log entries and stores them to the Audit Archive. Follow the steps to review past events. Step 1 – On the main Netwrix Auditor Event Log Manager page, click View next to View collected events. Step 2 – In the Netwrix Auditor Event Viewer window, complete the following to narrow results: Option Description Select the monitoring plan that audits desired event Monitoring plan log entries.
```

### Chunk 2 (Score: 0.7136)

```
CAUTION: Folder associated with NETWRIX AUDITOR must be excluded from antivirus scanning. See the Antivirus Exclusions for Netwrix Auditor knowledge base article for additional information. You can configure your IT Infrastructure for monitoring in one of the following ways: Table 1: Parameter Description • Log Level • Alert Level • Syslog Level Set to "Info". • Enable Audit Log Send to Syslog Server in Audit Log Settings Send to Syslog Server in Access Log Settings Select these checkboxes.
```

### Chunk 3 (Score: 0.7131)

```
Audit data is stored to the Audit databases and the repository (Long-Term Archive) and preserved there according to the corresponding retention settings. Netwrix Auditor analyzes the incoming audit data and alerts appropriate staff about critical changes, according to the built-in alerts you choose to use and any custom alerts you have created. v10.7 Authorized users use the Netwrix Auditor Client to view pre-built dashboards, run predefined reports, conduct investigations, and create custom reports based on their searches. Other users obtain the data they need via email or third-party tools.
```

### Chunk 4 (Score: 0.7047)

```
The current version of Netwrix Auditor contains the following diagrams: Enterprise (aggregates data on all audited systems listed below) Active Directory Exchange File Servers SharePoint SQL Server VMware Windows Server If you are sure that some audit data is missing (e.g., you do not see information on your fi le servers in reports and search results), verify that the Audit Database settings are configure d and that data is written to databases that reside on the default SQL Server instance. By default, Auditor allows generating reports and running interactive searches on data collected in the last 180 days. If you want to investigate incidents that occurred more than 180 days ago, ask your Auditor Global administrator to import that data from the Long-Term Archive. All diagrams provide the drill-down functionality, which means that by clicking on a segment, you will be redirected to a report with the corresponding filtering and grouping of data that renders the next level of detail.
```

### Chunk 5 (Score: 0.6964)

```
EventStorePath — Select where to store temporary files of syslog messages before the add-on sends them to Auditor Server. Netwrix recommends to store these files in the same directory with the add-on (SyslogService.exe). LogLevel warning Specify logging level: • none • info • warning (used by default) • error • debug v10.7 Parameter Default value Description case, data will be written to a database linked to this plan. If you select a plan name in the addon, make sure a dedicated plan is created in Auditor, the Netwrix API data source is added to the plan and enabled for monitoring.
```

