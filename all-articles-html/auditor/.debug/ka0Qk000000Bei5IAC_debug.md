# Article Processing Debug: ka0Qk000000Bei5IAC

**Generated:** 2025-06-03 12:25:59

## Article Content

```
How to Send Netwrix Auditor Logs Question What logs might be requested by Netwrix Technical Support? What logs might be requested by Netwrix Technical Support? How can you upload Netwrix Auditor logs to a support ticket? How can you upload Netwrix Auditor logs to a support ticket? Answer Technical Support checklist Netwrix Technical Support might request a collection of your Netwrix Auditor logs for troubleshooting purposes. Make sure you gather the following items to help your Technical Support Engineer resolve your issue. Netwrix Auditor System Health event log.�Refer to the following article for additional information on exporting the System Health event log:How to Save and Zip Netwrix Auditor System Health Event Log. Netwrix Auditor System Health event log.�Refer to the following article for additional information on exporting the System Health event log:How to Save and Zip Netwrix Auditor System Health Event Log. Netwrix Auditor configuration files. Navigate to%Working Folder%\AuditCore\ConfigServerand copy theConfigServerfolder. The default location of theConfigServerfolder isC:\ProgramData\Netwrix Auditor\AuditCore\ConfigServer. Netwrix Auditor configuration files. Navigate to%Working Folder%\AuditCore\ConfigServerand copy theConfigServerfolder. The default location of theConfigServerfolder isC:\ProgramData\Netwrix Auditor\AuditCore\ConfigServer. Trace logs. If requested, navigate to%Working Folder%\Netwrix Auditor\Logs, and copy the required folder(s).NOTE:Your Technical Support Engineer will request a specific subdirectory of theLogsfolder. Please do not send the entireLogsfolder unless requested. Trace logs. If requested, navigate to%Working Folder%\Netwrix Auditor\Logs, and copy the required folder(s). NOTE:Your Technical Support Engineer will request a specific subdirectory of theLogsfolder. Please do not send the entireLogsfolder unless requested. NOTE:If you are unable to locate Working Folder, refer to the following options to perform in your Auditor server to establish the folder location: Run the following line in Command Prompt in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Auditor server:reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride" Run the following line in Command Prompt in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Auditor server: Run the following line in PowerShell in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Netwrix Auditor server:Get-ItemPropertyValue -Path "HKLM:\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride" -Name "(Default)" Run the following line in PowerShell in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Netwrix Auditor server: Review the string entry under the following registry subnode in your Netwrix Auditor server. TheValue Datafield contains the location of Working Folder:Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride Review the string entry under the following registry subnode in your Netwrix Auditor server. TheValue Datafield contains the location of Working Folder: Uploading the logs Once you have located all the required logs, copy them to a single folder and compress it by right-clicking the folder and selectingSend to>Compressed (zipped) folder. Once you have located all the required logs, copy them to a single folder and compress it by right-clicking the folder and selectingSend to>Compressed (zipped) folder. Log in to the Customer Portal�and attach the archived logs to the opened ticket. Use the following link to open theOpen ticketspage:My Tickets � Open Tickets. Log in to the Customer Portal�and attach the archived logs to the opened ticket. Use the following link to open theOpen ticketspage:My Tickets � Open Tickets. NOTE:Once you have opened theOpen Ticketspage and identified the corresponding ticket (with a matching ticket #), you can attach the logs via one of the following ways: Click theAdd attachmentsbutton located under theActionscolumn of the ticket.� Click theAdd attachmentsbutton located under theActionscolumn of the ticket.� Expand the ticket details by clicking thedown carat (?)button and click theplus (+)button next toAttachments.� Expand the ticket details by clicking thedown carat (?)button and click theplus (+)button next toAttachments.� Related links How to Save and Zip Netwrix Auditor System Health Event Log How to Save and Zip Netwrix Auditor System Health Event Log My Tickets � Open Tickets My Tickets � Open Tickets
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.70
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide relevant information about monitoring plans and event log management in Netwrix Auditor, which is related to the article's content on log collection for technical support. However, the article may need minor updates for clarity and to ensure consistency with the latest procedures mentioned in the references.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.7491)

```
Step 3 – Navigate to the Monitored computers list and add a server where the Netwrix Auditor Server resides. Step 4 – Navigate to the Audit Database tab and select Write event descriptions to Audit Database if you want to see the exact error or warning text. Make sure that Audit Database settings are configured properly, follow the Audit Database Step 5 – Click Configure next to Audit archiving filters and select the Netwrix Auditor System Health Log filter in the Inclusive Filters list. This procedure describes the basic steps, required for creation of the monitoring plan that will be used to collect data on Netwrix Auditor health status events.
```

### Chunk 2 (Score: 0.7471)

```
Step 1 – Start Netwrix Auditor Event Log Manager and create the new monitoring plan. Step 2 – Make sure that the Enable event log collection checkbox is selected. Specify the name for the new monitoring plan, for example, "Netwrix Auditor Health Status". Step 3 – Navigate to the Monitored computers list and add a server where the Netwrix Auditor Server resides.
```

### Chunk 3 (Score: 0.7402)

```
Step 1 – Navigate to Start > Netwrix Auditor > Netwrix Auditor Event Log Manager. Step 2 – On the main page, you will be prompted to select a monitoring plan. Click Add to add new plan. Step 3 – Configure basic parameters as follows: Enable event log collection — Select the checkbox to start monitoring event logs.
```

### Chunk 4 (Score: 0.7389)

```
Create Monitoring Plan for System Health Log If you want to generate reports on health state and to be alerted on important Netwrix Auditor health events, you need to create a dedicated monitoring plan for this log with Netwrix Auditor Event Log Manager standalone tool. You can also review and filter Netwrix Auditor health events right in the product. See Netwrix Auditor Health Log for addditional information Follow the steps to configure the Netwrix Auditor System Health log monitoring. Step 1 – Start Netwrix Auditor Event Log Manager and create the new monitoring plan.
```

### Chunk 5 (Score: 0.7302)

```
EventStorePath — Select where to store temporary files of syslog messages before the add-on sends them to Auditor Server. Netwrix recommends to store these files in the same directory with the add-on (SyslogService.exe). LogLevel warning Specify logging level: • none • info • warning (used by default) • error • debug v10.7 Parameter Default value Description case, data will be written to a database linked to this plan. If you select a plan name in the addon, make sure a dedicated plan is created in Auditor, the Netwrix API data source is added to the plan and enabled for monitoring.
```

