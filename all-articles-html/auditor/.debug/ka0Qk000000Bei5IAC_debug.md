# Article Processing Debug: ka0Qk000000Bei5IAC

**Generated:** 2025-06-01 00:12:09

## Article Content

```
How to Send Netwrix Auditor Logs Question What logs might be requested by Netwrix Technical Support? What logs might be requested by Netwrix Technical Support? How can you upload Netwrix Auditor logs to a support ticket? How can you upload Netwrix Auditor logs to a support ticket? Answer Technical Support checklist Netwrix Technical Support might request a collection of your Netwrix Auditor logs for troubleshooting purposes. Make sure you gather the following items to help your Technical Support Engineer resolve your issue. Netwrix Auditor System Health event log.�Refer to the following article for additional information on exporting the System Health event log:How to Save and Zip Netwrix Auditor System Health Event Log. Netwrix Auditor System Health event log.�Refer to the following article for additional information on exporting the System Health event log:How to Save and Zip Netwrix Auditor System Health Event Log. Netwrix Auditor configuration files. Navigate to%Working Folder%\AuditCore\ConfigServerand copy theConfigServerfolder. The default location of theConfigServerfolder isC:\ProgramData\Netwrix Auditor\AuditCore\ConfigServer. Netwrix Auditor configuration files. Navigate to%Working Folder%\AuditCore\ConfigServerand copy theConfigServerfolder. The default location of theConfigServerfolder isC:\ProgramData\Netwrix Auditor\AuditCore\ConfigServer. Trace logs. If requested, navigate to%Working Folder%\Netwrix Auditor\Logs, and copy the required folder(s).NOTE:Your Technical Support Engineer will request a specific subdirectory of theLogsfolder. Please do not send the entireLogsfolder unless requested. Trace logs. If requested, navigate to%Working Folder%\Netwrix Auditor\Logs, and copy the required folder(s). NOTE:Your Technical Support Engineer will request a specific subdirectory of theLogsfolder. Please do not send the entireLogsfolder unless requested. NOTE:If you are unable to locate Working Folder, refer to the following options to perform in your Auditor server to establish the folder location: Run the following line in Command Prompt in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Auditor server:reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride" Run the following line in Command Prompt in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Auditor server: Run the following line in PowerShell in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Netwrix Auditor server:Get-ItemPropertyValue -Path "HKLM:\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride" -Name "(Default)" Run the following line in PowerShell in your Auditor server to get the value of theDataPathOverridesubkey entry. The output will contain the location of Working Folder in your Netwrix Auditor server: Review the string entry under the following registry subnode in your Netwrix Auditor server. TheValue Datafield contains the location of Working Folder:Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Auditor\DataPathOverride Review the string entry under the following registry subnode in your Netwrix Auditor server. TheValue Datafield contains the location of Working Folder: Uploading the logs Once you have located all the required logs, copy them to a single folder and compress it by right-clicking the folder and selectingSend to>Compressed (zipped) folder. Once you have located all the required logs, copy them to a single folder and compress it by right-clicking the folder and selectingSend to>Compressed (zipped) folder. Log in to the Customer Portal�and attach the archived logs to the opened ticket. Use the following link to open theOpen ticketspage:My Tickets � Open Tickets. Log in to the Customer Portal�and attach the archived logs to the opened ticket. Use the following link to open theOpen ticketspage:My Tickets � Open Tickets. NOTE:Once you have opened theOpen Ticketspage and identified the corresponding ticket (with a matching ticket #), you can attach the logs via one of the following ways: Click theAdd attachmentsbutton located under theActionscolumn of the ticket.� Click theAdd attachmentsbutton located under theActionscolumn of the ticket.� Expand the ticket details by clicking thedown carat (?)button and click theplus (+)button next toAttachments.� Expand the ticket details by clicking thedown carat (?)button and click theplus (+)button next toAttachments.� Related links How to Save and Zip Netwrix Auditor System Health Event Log How to Save and Zip Netwrix Auditor System Health Event Log My Tickets � Open Tickets My Tickets � Open Tickets
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.70
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide relevant information about monitoring plans and event log management in Netwrix Auditor, which is related to the article's focus on log collection for technical support. However, the article may need minor updates to ensure consistency and clarity, as it repeats some information and could benefit from improved organization.

## Document Chunks Analysis

Total chunks analyzed: 6108
<details>
<summary>Full Similarity Score Distribution</summary>

| # | Score | Text Preview |
|---|-------|-------------|
| 1 | 0.7491 | Step 3 – Navigate to the Monitored computers list ... |
| 2 | 0.7471 | Step 1 – Start Netwrix Auditor Event Log Manager a... |
| 3 | 0.7402 | Step 1 – Navigate to Start > Netwrix Auditor > Net... |
| 4 | 0.7389 | Create Monitoring Plan for System Health Log If yo... |
| 5 | 0.7302 | EventStorePath — Select where to store temporary f... |
| 6 | 0.7291 | See the Appendix. Netwrix Auditor Integration Even... |
| 7 | 0.7242 | v10.7 Review Past Event Log Entries Netwrix Audito... |
| 8 | 0.7230 | Select where to store temporary files of syslog me... |
| 9 | 0.7217 | Follow the basic steps, required for creation of t... |
| 10 | 0.7205 | v10.7 Netwrix Auditor System Health Log When an er... |
| 11 | 0.7184 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 12 | 0.7110 | This procedure describes the basic steps, required... |
| 13 | 0.7092 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 14 | 0.7008 | Download free add-ons from Netwrix Auditor Add-on ... |
| 15 | 0.7003 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 16 | 0.6990 | To do this, right-click a task and click Run. Work... |
| 17 | 0.6988 | To do this, right-click a task and click Run. Work... |
| 18 | 0.6981 | Specify an item name. Make sure to create a dedica... |
| 19 | 0.6944 | Step 4 – Hit Enter. Depending on the number of Act... |
| 20 | 0.6905 | Compatibility Notice Make sure to check your produ... |
| 21 | 0.6879 | Specify IP address of the computer that hosts your... |
| 22 | 0.6875 | Event Log You can fine-tune Netwrix Auditor by spe... |
| 23 | 0.6864 | For example, warnings on failed data collection or... |
| 24 | 0.6854 | Work with Collected Data Step 1 – On the computer ... |
| 25 | 0.6838 | Work with Collected Data Follow the steps to work ... |
| 26 | 0.6831 | Netwrix Auditor Event Log Manager synchronizes Aud... |
| 27 | 0.6825 | v10.7 33.. The add-on creates a special Windows ev... |
| 28 | 0.6820 | The Netwrix Auditor Integration event log will be ... |
| 29 | 0.6820 | In the Web Interface, navigate Log → Settings and ... |
| 30 | 0.6819 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 31 | 0.6782 | Step 8 – Complete the Event Filter dialog. In the ... |
| 32 | 0.6748 | Navigate to C:\ProgramData\Netwrix Auditor\Windows... |
| 33 | 0.6746 | See the Integration Event Log Fields topic for add... |
| 34 | 0.6740 | Step 2 – Make sure that the Enable event log colle... |
| 35 | 0.6737 | Step 2 – In the Netwrix Auditor Event Viewer windo... |
| 36 | 0.6723 | Netwrix recommends not to store these files out of... |
| 37 | 0.6717 | Syslog Level Enable Audit Log Send to Syslog Serve... |
| 38 | 0.6715 | NetwrixAuditorPlanItem — Specify an item name here... |
| 39 | 0.6706 | v10.7 Create Your First Monitoring Plan To start c... |
| 40 | 0.6689 | v10.7 When requested by Netwrix Support, click Dow... |
| 41 | 0.6683 | For more information on the Activity Record struct... |
| 42 | 0.6678 | Event Log Manager Netwrix Auditor Event Log Manage... |
| 43 | 0.6664 | See the Configure a Response Action for Alert topi... |
| 44 | 0.6664 | • Enable Audit Log Send to Syslog Server in Audit ... |
| 45 | 0.6635 | The product does not log any errors on these event... |
| 46 | 0.6634 | EventStorePath — Netwrix recommends to store these... |
| 47 | 0.6634 | Accept List Address Specify a list of IP addresses... |
| 48 | 0.6633 | Step 3 – Review events. Table 1: Event log field n... |
| 49 | 0.6632 | Step 9 – Click OK to save the changes and close th... |
| 50 | 0.6622 | Ensure the script execution completed successfully... |
| 51 | 0.6621 | Ensure the script execution completed successfully... |
| 52 | 0.6615 | Review the table below for more information. To...... |
| 53 | 0.6547 | 1144.. Locate the Syslog parameter and set it to I... |
| 54 | 0.6543 | The add-on processes these Syslog messages into Au... |
| 55 | 0.6533 | Step 1 – In Auditor, navigate to Reports > Organiz... |
| 56 | 0.6527 | Step 2 – Out of the box, messages from Red Hat Ent... |
| 57 | 0.6520 | To review Event Trace Session objects' configurati... |
| 58 | 0.6515 | By default, the Netwrix Auditor Integration event ... |
| 59 | 0.6515 | By default, the Netwrix Auditor Integration event ... |
| 60 | 0.6510 | The add-on connects to the Netwrix Auditor server ... |
| 61 | 0.6510 | The add-on connects to the Netwrix Auditor server ... |
| 62 | 0.6509 | Netwrix Auditor Event Log Manager does not collect... |
| 63 | 0.6504 | • Enable Audit Log Send to Syslog Server in Audit ... |
| 64 | 0.6493 | Step 3 – On the syslog panel, click Add and select... |
| 65 | 0.6477 | ◦◦ Enable SharePoint Administration Service on the... |
| 66 | 0.6472 | You can also configure and receive alerts on the e... |
| 67 | 0.6466 | The downloaded logs have the debug logging informa... |
| 68 | 0.6451 | You can choose whether to import the list once, or... |
| 69 | 0.6450 | Step 3 – The add-on processes these events into Ne... |
| 70 | 0.6437 | Specify the time range for which you want to retri... |
| 71 | 0.6437 | For more information on the structure of the Activ... |
| 72 | 0.6437 | Go to the Audit Database section and make sure tha... |
| 73 | 0.6436 | Prerequisites Before running the add-on, ensure th... |
| 74 | 0.6434 | If you want to investigate incidents that occurred... |
| 75 | 0.6426 | For example, in the Apply Filters dialog you can s... |
| 76 | 0.6415 | By default, the Netwrix Auditor Integration event ... |
| 77 | 0.6401 | Complete the following fields: Table 1: Option Des... |
| 78 | 0.6397 | Depending on the number of Activity Records stored... |
| 79 | 0.6397 | Depending on the number of Activity Records stored... |
| 80 | 0.6397 | Depending on the number of Activity Records stored... |
| 81 | 0.6395 | The add-on connects to the Auditor server and retr... |
| 82 | 0.6394 | Table 1: Option Description To find out a log’s na... |
| 83 | 0.6387 | Expand the Options section and complete the follow... |
| 84 | 0.6385 | For example: Add arguments (optional) file "C:\Add... |
| 85 | 0.6355 | Option to save and send a report at the same time.... |
| 86 | 0.6334 | Work with Collected Data Follow the steps to work ... |
| 87 | 0.6329 | Specify a name of associated monitoring plan in Au... |
| 88 | 0.6329 | Specify a name of associated monitoring plan in Au... |
| 89 | 0.6325 | Specify a name of associated monitoring plan in Au... |
| 90 | 0.6325 | Specify a name of associated monitoring plan in Au... |
| 91 | 0.6325 | 44.. After that, you will be able to attach the fi... |
| 92 | 0.6321 | Step 2 – Click Save. Step 3 – Reproduce the issue ... |
| 93 | 0.6321 | Step 2 – Select Audit module and select 5 - Notice... |
| 94 | 0.6320 | Log File: By default the Access Reviews applicatio... |
| 95 | 0.6313 | Using the Integration API, the add-on sends the ac... |
| 96 | 0.6313 | Event log Select event log that contains desired e... |
| 97 | 0.6307 | Configure alerts triggered by specific events in t... |
| 98 | 0.6306 | See the Monitoring Overview topic for additional i... |
| 99 | 0.6298 | Select monitoring plans whose audit data you want ... |
| 100 | 0.6297 | Schedule email delivery of a variety of reports or... |
| 101 | 0.6296 | Default is Medium. v10.7 Parameter Description [Ne... |
| 102 | 0.6290 | Specify a name of associated monitoring plan in Au... |
| 103 | 0.6288 | If the Event Level check box is cleared, all event... |
| 104 | 0.6285 | Monitoring plans Select monitoring plans whose aud... |
| 105 | 0.6276 | Step 3 – Add script parameters. The console will l... |
| 106 | 0.6265 | When an update is available, a user is immediately... |
| 107 | 0.6262 | 22.. Navigate to HKEY_LOCAL_MACHINE → SOFTWARE → W... |
| 108 | 0.6261 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 109 | 0.6251 | Click Browse to select from the list of containers... |
| 110 | 0.6247 | Audit data is stored to the Audit databases and th... |
| 111 | 0.6237 | Collect data for state-in-time reports Configure N... |
| 112 | 0.6236 | Step 1 – Stop the old version of Netwrix Auditor a... |
| 113 | 0.6236 | Monitored Computers For a newly created monitoring... |
| 114 | 0.6225 | To reduce the volume of the stored logs and the co... |
| 115 | 0.6225 | Step 2 – Select the Netwrix Auditor User Activity ... |
| 116 | 0.6224 | Define what events will be saved to the Long-Term ... |
| 117 | 0.6223 | Event parameter descriptions can also be added. In... |
| 118 | 0.6222 | See theNetwork Devices topic for additional inform... |
| 119 | 0.6216 | Certain applications can also be added to Exceptio... |
| 120 | 0.6207 | The add-on listens to the specified UDP ports and ... |
| 121 | 0.6207 | The add-on listens to the specified UDP ports and ... |
| 122 | 0.6206 | set csv disable Table 1: Option Description Name/I... |
| 123 | 0.6192 | Step 1 – Create a monitoring plan in Netwrix Audit... |
| 124 | 0.6186 | Step 2 – Click Manage. v10.7 Step 3 – Select the d... |
| 125 | 0.6174 | Integration Event Log Fields This section describe... |
| 126 | 0.6173 | Using the Integration API, the add-on sends the ac... |
| 127 | 0.6160 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 128 | 0.6160 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 129 | 0.6160 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 130 | 0.6160 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 131 | 0.6160 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 132 | 0.6147 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 133 | 0.6146 | Subscriptions can be uploaded either to a file sha... |
| 134 | 0.6145 | Step 1 – An IT administrator configures Netwrix Au... |
| 135 | 0.6142 | Refer to Create Alerts for Event Log for Table 1: ... |
| 136 | 0.6140 | For this data to be provided to Splunk, it adds a ... |
| 137 | 0.6140 | See the Integration API topic for additional infor... |
| 138 | 0.6140 | See the Integration API topic for additional infor... |
| 139 | 0.6139 | This option controls how often audit data is expor... |
| 140 | 0.6139 | The service will collect and process events from t... |
| 141 | 0.6139 | The service will collect and process events from t... |
| 142 | 0.6139 | The Services Control Manager opens. Step 2 – Right... |
| 143 | 0.6138 | Store that file content to a safe location. Step 3... |
| 144 | 0.6133 | Depending on the number of Activity Records stored... |
| 145 | 0.6131 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 146 | 0.6131 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 147 | 0.6131 | Process computer accounts Select this checkbox to ... |
| 148 | 0.6128 | Shows all activity records imported with Netwrix A... |
| 149 | 0.6127 | The option is not available for auditing User Acti... |
| 150 | 0.6126 | If the event source for p articular DataSource doe... |
| 151 | 0.6126 | Specify a name of associated monitoring plan in Au... |
| 152 | 0.6124 | To reduce the volume of the stored logs and the co... |
| 153 | 0.6116 | Subscribe to the Health Summary Email The Health S... |
| 154 | 0.6115 | RECOMMENDED: click Send Test Email. The system wil... |
| 155 | 0.6114 | After creating a task, wait for the next scheduled... |
| 156 | 0.6114 | After creating a task, wait for the next scheduled... |
| 157 | 0.6100 | Locate the NetwrixAuditorForWindowsServer object, ... |
| 158 | 0.6098 | See the Integration API topic for additional infor... |
| 159 | 0.6097 | Step 2 – Select Netwrix Auditor Event Log Compress... |
| 160 | 0.6095 | Specify notification delivery time Modify the Even... |
| 161 | 0.6091 | See the Supported Data Sources configuration topic... |
| 162 | 0.6087 | Netwrix Auditor Server — the central component tha... |
| 163 | 0.6082 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 164 | 0.6080 | The add-on processes Netwrix Auditor-compatible da... |
| 165 | 0.6080 | The add-on processes Netwrix Auditor-compatible da... |
| 166 | 0.6078 | This method is recommended for evaluation purposes... |
| 167 | 0.6074 | <NetwrixAuditorPassword>NetwrixIsCoo l </NetwrixAu... |
| 168 | 0.6074 | * @name:514;RSYSLOG_SyslogProt ocol23Format where ... |
| 169 | 0.6068 | The current version of Netwrix Auditor contains th... |
| 170 | 0.6065 | ImportAllEvents — By deafult, only events with pro... |
| 171 | 0.6065 | Make sure to provide correct path to the script fi... |
| 172 | 0.6056 | Manually – Native audit settings must be adjusted ... |
| 173 | 0.6048 | Netwrix recommends to store all audit data on the ... |
| 174 | 0.6041 | For both new and existing monitoring plans, you ca... |
| 175 | 0.6033 | On a high level, the add-on works as follows: 11..... |
| 176 | 0.6033 | On a high level, the add-on works as follows: 11..... |
| 177 | 0.6033 | On a high level, the add-on works as follows: 11..... |
| 178 | 0.6027 | Its key capabilities are as follows: Allows Audito... |
| 179 | 0.6026 | On a high level, the add-on works as follows: 11..... |
| 180 | 0.6024 | Stores data collected by Netwrix Auditor self-audi... |
| 181 | 0.6021 | Event Log Review the basic registry keys that you ... |
| 182 | 0.6017 | Tip for reading the table: For example, on the com... |
| 183 | 0.6010 | Integration Event Log Fields This section describe... |
| 184 | 0.6005 | Unless specified, data is not associated with a sp... |
| 185 | 0.6004 | The TCP 9699 port (default Auditor Integr ation AP... |
| 186 | 0.5998 | It should be a running Netwrix Syslog service or a... |
| 187 | 0.5995 | v10.7 Netwrix Auditor Integration API operates wit... |
| 188 | 0.5987 | Step 2 – Add the following line: auth.*;authpriv. ... |
| 189 | 0.5984 | v10.7 Step 2 – Review the results. Successfully ap... |
| 190 | 0.5983 | v10.7 Configure Audit Database Settings When you f... |
| 191 | 0.5980 | Data collection for this monitoring plan might not... |
| 192 | 0.5978 | * @name:514;RSYSLOG_SyslogProtocol23Fo rmat where ... |
| 193 | 0.5977 | Follow the steps to troubleshoot data input from N... |
| 194 | 0.5973 | Database Settings At this step, you need to specif... |
| 195 | 0.5972 | Netwrix Auditor ConnectWise Manage Integration Ser... |
| 196 | 0.5972 | SIEM Generic Integration for Event Log Export Netw... |
| 197 | 0.5972 | v10.7 Option Description Unless specified, data is... |
| 198 | 0.5971 | Netwrix Auditor Alerts to Event Log Add-on On... E... |
| 199 | 0.5970 | For example: Router# configure terminal 33.. Enabl... |
| 200 | 0.5965 | Proper audit configuration is required to ensure a... |
| 201 | 0.5965 | Proper audit configuration is required to ensure a... |
| 202 | 0.5965 | Proper audit configuration is required to ensure a... |
| 203 | 0.5965 | Proper audit configuration is required to ensure a... |
| 204 | 0.5965 | Proper audit configuration is required to ensure a... |
| 205 | 0.5965 | Proper audit configuration is required to ensure a... |
| 206 | 0.5965 | Proper audit configuration is required to ensure a... |
| 207 | 0.5958 | Only the latest snapshot is available for reportin... |
| 208 | 0.5957 | Make sure there is enough disk space allocated for... |
| 209 | 0.5955 | Each event contains the user account, action, time... |
| 210 | 0.5955 | In the Event Fields tab, select event levels that ... |
| 211 | 0.5939 | Table 1: To monitor... Execute the command... Conf... |
| 212 | 0.5936 | v10.7 Logon Activity Netwrix Auditor relies on nat... |
| 213 | 0.5936 | Each event contains the user account, action, time... |
| 214 | 0.5935 | To detect actual change initiator, Netwrix Auditor... |
| 215 | 0.5927 | For example: #*,server,MicrosoftDNS_S #*,*,StdServ... |
| 216 | 0.5924 | Currently, Netwrix Auditor processes details for t... |
| 217 | 0.5922 | This option controls how often audit data is expor... |
| 218 | 0.5917 | See the Adjust Security Event Log Size and Retenti... |
| 219 | 0.5917 | For example: hostname(config)# logging enable 44..... |
| 220 | 0.5914 | For other dist ributions, deployment of rsyslog pa... |
| 221 | 0.5911 | * @name:514;RSYSLOG_SyslogProtocol23Fo rmat where ... |
| 222 | 0.5906 | The add-on creates a special Windows event log nam... |
| 223 | 0.5905 | See the Health Status Dashboard topic for addition... |
| 224 | 0.5897 | Proper audit configuration is required to ensure a... |
| 225 | 0.5895 | Audit Configuration Assistant is a part of Netwrix... |
| 226 | 0.5894 | Netwrix_Auditor_API Stores activity records collec... |
| 227 | 0.5893 | Table 2: On... Ensure that... The Auditor Server s... |
| 228 | 0.5893 | All Integration API Activity Shows all activity re... |
| 229 | 0.5892 | General On the General tab you can configure globa... |
| 230 | 0.5890 | You can copy and archive this folder manually, or ... |
| 231 | 0.5889 | If you are using SharePoint 2019 or SharePoint Sub... |
| 232 | 0.5889 | OutputFolder — This is a mandatory parameter. Choo... |
| 233 | 0.5887 | By deafult, only events with processed details wil... |
| 234 | 0.5885 | The email looks like shown below: v10.7 v10.7 The ... |
| 235 | 0.5883 | The add-on connects to the Netwrix Auditor Server ... |
| 236 | 0.5883 | v10.7 Clicking the Go to Notifications button open... |
| 237 | 0.5875 | The add-on creates a special Windows event log nam... |
| 238 | 0.5873 | Auditor Monitoring Plan settings Auditor Plan Unle... |
| 239 | 0.5873 | Auditor Monitoring Plan settings Auditor Plan Unle... |
| 240 | 0.5869 | Data out: Further automate your business processes... |
| 241 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 242 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 243 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 244 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 245 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 246 | 0.5857 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 247 | 0.5851 | The installation wizard placed a Netwrix Auditor A... |
| 248 | 0.5851 | Title Default: [Netwrix Auditor] %AlertName% That ... |
| 249 | 0.5849 | Execute the following commands: # configure Table ... |
| 250 | 0.5848 | Each event contains the user account, action, time... |
| 251 | 0.5848 | Each event contains the user account, action, time... |
| 252 | 0.5846 | The body is empty. The posted file exceeds support... |
| 253 | 0.5843 | Once troubleshooting has finished, it is recommend... |
| 254 | 0.5842 | Step 2 – Download the add-on package and copy it t... |
| 255 | 0.5841 | Complete the following fields: Option Description ... |
| 256 | 0.5841 | File Share UNC path to audit logs Path to the file... |
| 257 | 0.5840 | The add-ons comes with a special set of alerts dev... |
| 258 | 0.5838 | In this case audit data is For example: still bein... |
| 259 | 0.5838 | In the Web Interface, navigate to Manage → Log Set... |
| 260 | 0.5836 | Netwrix has built a ready-to-use add-on that autom... |
| 261 | 0.5834 | NetwrixAuditorPlanItem — Unless specified, data is... |
| 262 | 0.5834 | It is recommended to create a dedicated monitoring... |
| 263 | 0.5830 | Behavior Anomalies Schedule email delivery of a va... |
| 264 | 0.5822 | On a high level, the add-on works as follows: 11..... |
| 265 | 0.5821 | The add-on creates a special Windows event log nam... |
| 266 | 0.5813 | Role-Based Access and Delegation Configure general... |
| 267 | 0.5809 | Step 3 – On the Triggers tab, click New and define... |
| 268 | 0.5808 | Before you start monitoring your Oracle Database w... |
| 269 | 0.5808 | Netwrix Auditor Access Reviews is now configured a... |
| 270 | 0.5808 | Implemented as a service, this add-on facilitates ... |
| 271 | 0.5805 | Auditor settings • The Audit Database settings sho... |
| 272 | 0.5804 | Execute... Upload alert set shipped with the addon... |
| 273 | 0.5802 | Object type Action What Details Successful Logon N... |
| 274 | 0.5802 | Fine-tune logon activity monitoring Specify interv... |
| 275 | 0.5801 | Specify a name of associated monitoring plan in Au... |
| 276 | 0.5798 | NOTE: Right after setting up the integration the d... |
| 277 | 0.5794 | Table 1: Event log field name Filled in with value... |
| 278 | 0.5794 | Table 1: Event log field name Filled in with value... |
| 279 | 0.5790 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 280 | 0.5788 | Table 1: To.. Do.. See how data collection goes on... |
| 281 | 0.5787 | This value is filled in automatically. time zone w... |
| 282 | 0.5787 | If you want to change root directory, do the follo... |
| 283 | 0.5785 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432NODE\Netwrix Au... |
| 284 | 0.5785 | For a full list of audit settings required for Net... |
| 285 | 0.5784 | After you click Connect, the connection with Netwr... |
| 286 | 0.5782 | Health Status Dashboard Schedule Health Summary em... |
| 287 | 0.5780 | Netwrix Auditor Integration API is enabled by defa... |
| 288 | 0.5779 | Step 3 – In the Remote Registry Properties dialog ... |
| 289 | 0.5772 | Each Activity Record contains the user account, lo... |
| 290 | 0.5772 | Self-Audit Built-in Netwrix Auditor self-audit all... |
| 291 | 0.5769 | Step 4 – Navigate to the Send data for Access Revi... |
| 292 | 0.5769 | Protocols and Ports Required v10.7 Detect insider ... |
| 293 | 0.5767 | Data source: %DataSource% Step 2 – Then open Conne... |
| 294 | 0.5765 | To retrieve activity logs on Copilot interactions,... |
| 295 | 0.5764 | Add the following line: auth.*;authpriv. * @name:5... |
| 296 | 0.5762 | 1166.. Start Netwrix Auditor. 1177.. Navigate to y... |
| 297 | 0.5761 | The chart shows how many events with different sev... |
| 298 | 0.5760 | By default, the Netwrix Auditor Integration event ... |
| 299 | 0.5758 | Step 2 – Download the Add-On. Step 3 – Configure P... |
| 300 | 0.5757 | For your change management workflow, Netwrix Audit... |
| 301 | 0.5755 | See the Prerequisites topic for additional informa... |
| 302 | 0.5755 | See the Prerequisites topic for additional informa... |
| 303 | 0.5755 | See the Prerequisites topic for additional informa... |
| 304 | 0.5751 | Ensure that... Step 5 – Open the / etc/ rsyslog.co... |
| 305 | 0.5747 | Step 3 – On the Triggers tab, click New and define... |
| 306 | 0.5747 | Step 3 – On the Triggers tab, click New and define... |
| 307 | 0.5747 | Step 3 – On the Triggers tab, click New and define... |
| 308 | 0.5746 | You will be alerted on events from this event log.... |
| 309 | 0.5746 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 310 | 0.5745 | Netwrix Auditor supports integration with Netwrix ... |
| 311 | 0.5740 | For a full list of the rights and permissions, and... |
| 312 | 0.5740 | Configure Netwrix Auditor to store daily snapshots... |
| 313 | 0.5736 | v10.7 Exchange Netwrix Auditor relies on native lo... |
| 314 | 0.5735 | Each Activity Record contains the user account, ac... |
| 315 | 0.5731 | Please contact Netwrix Technical Support team to m... |
| 316 | 0.5730 | App — points where the index configuration is stor... |
| 317 | 0.5730 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 318 | 0.5724 | See File-Based Repository for Long-Term Archive fo... |
| 319 | 0.5716 | These events are structured and ready for integrat... |
| 320 | 0.5715 | Manage auditing and security log. See the Configur... |
| 321 | 0.5713 | See the Integrations topic for additional informat... |
| 322 | 0.5713 | EventID {Calculated by add-on} -ORDepending on Gen... |
| 323 | 0.5711 | • The alert response action settings in Auditor Se... |
| 324 | 0.5710 | v10.7 After that it is strongly recommended to re-... |
| 325 | 0.5709 | Once the required steps are done, the recommendati... |
| 326 | 0.5708 | *) To configure the audit settings manually, refer... |
| 327 | 0.5708 | These events are structured and ready for integrat... |
| 328 | 0.5703 | Netwrix Auditor allows importing data from the Lon... |
| 329 | 0.5703 | This file is shipped separately. Table 1: Where Pr... |
| 330 | 0.5698 | Netwrix.Nutanix.IntegrationService.exe Main add-on... |
| 331 | 0.5698 | Table 1: Option Description Monitor this data sour... |
| 332 | 0.5692 | To review data sources and items included in each ... |
| 333 | 0.5691 | In Netwrix Auditor settings, go to the Integration... |
| 334 | 0.5688 | Activity Records are -NetwrixAuditorUserName expor... |
| 335 | 0.5685 | 22.. Access the global configuration mode. For exa... |
| 336 | 0.5685 | For a Windows File Server, the service is the Netw... |
| 337 | 0.5685 | Netwrix Auditor Access Reviews is configured and r... |
| 338 | 0.5685 | And make sure that the UDP port is used for sendin... |
| 339 | 0.5685 | Only the latest snapshot is available for reportin... |
| 340 | 0.5683 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 341 | 0.5681 | Create Alerts for Non-Owner Mailbox Access Events ... |
| 342 | 0.5679 | Work with Collected Data Follow the steps to work ... |
| 343 | 0.5677 | Alert Handler: Receives the IDs of the alert and a... |
| 344 | 0.5674 | Use the Database statistics widget to examine data... |
| 345 | 0.5674 | This data is not associated with any monitoring pl... |
| 346 | 0.5670 | View Reports Create alerts to be notified about su... |
| 347 | 0.5669 | v10.7 To instruct Netwrix Auditor to collect data ... |
| 348 | 0.5667 | Otherwise, Netwrix Auditor may not operate properl... |
| 349 | 0.5665 | Follow the steps to install Netwrix Auditor agent ... |
| 350 | 0.5664 | Start Abandoned Data Source Auditing If you have a... |
| 351 | 0.5662 | Opens the list of the configuration reco mmendatio... |
| 352 | 0.5654 | ◦◦ To provide a coherent picture of changes that o... |
| 353 | 0.5653 | Table 1: On... Ensure that... The Netwrix Auditor ... |
| 354 | 0.5652 | See the Group Policy configuration topic for a ddi... |
| 355 | 0.5651 | Execute the command... AUDIT POLICY nwx_actions_po... |
| 356 | 0.5649 | <NetwrixAuditorEndpoint>https:// 172.28.6.19:9699/... |
| 357 | 0.5649 | RECOMMENDED: The notification should include: Why ... |
| 358 | 0.5648 | ◦◦ The following inbound Firewall rules must be en... |
| 359 | 0.5646 | For a full list of the rights and permissions, and... |
| 360 | 0.5645 | Navigate to this directory and locate Netwrix_Audi... |
| 361 | 0.5645 | See the Configure Removable Storage Media for Moni... |
| 362 | 0.5644 | Main add-on component, responsible for audit data ... |
| 363 | 0.5643 | Click View to generate the selected report. Moreov... |
| 364 | 0.5641 | v10.7 Prepare for Using Netwrix Auditor Integratio... |
| 365 | 0.5638 | Netwrix provides a command-line tool for enabling ... |
| 366 | 0.5636 | After you click View details, the following inform... |
| 367 | 0.5636 | format=json} {&count=Number} — POST https://{host:... |
| 368 | 0.5635 | Configure audit settings Do not select the checkbo... |
| 369 | 0.5633 | If you want to clear Netwrix Auditor Health Log, s... |
| 370 | 0.5631 | monitoring. For example: SQLPlan,Ent-SQL,Table,gue... |
| 371 | 0.5629 | You can also launch data collection and Activity S... |
| 372 | 0.5628 | Activity Records are exported to a local event log... |
| 373 | 0.5628 | Click Run to start collecting data with the Add-On... |
| 374 | 0.5625 | All you have to do is provide connection details a... |
| 375 | 0.5625 | All you have to do is provide connection details a... |
| 376 | 0.5624 | Format Select IETF. Facility Netwrix recommends us... |
| 377 | 0.5623 | Table 1: Parameter Default value Description Gener... |
| 378 | 0.5621 | Ensure your computer is listed as Receiver (e.g., ... |
| 379 | 0.5620 | Other users obtain the data they need via email or... |
| 380 | 0.5620 | Auditor settings The Audit Database settings shoul... |
| 381 | 0.5616 | If you want to reopen closed tickets, you must be ... |
| 382 | 0.5614 | Refer to the following sections for detailed infor... |
| 383 | 0.5614 | Step 2 – Run the installation package. Step 3 – Fo... |
| 384 | 0.5613 | By default, Netwrix Auditor only tracks changes to... |
| 385 | 0.5613 | NOTE: Stop and then restart the service every time... |
| 386 | 0.5610 | See Permissions for SharePoint Auditing topic for ... |
| 387 | 0.5606 | To check or configure these settings, navigate to ... |
| 388 | 0.5604 | When prompted to configure the Audit database sett... |
| 389 | 0.5597 | Its data is also stored in the Long-Term Archive. ... |
| 390 | 0.5597 | Its data is also stored in the Long-Term Archive. ... |
| 391 | 0.5595 | If you provide a monitoring plan name for input Ac... |
| 392 | 0.5591 | Compatibility Notice Make sure to check your produ... |
| 393 | 0.5586 | It is recommended to create a dedicated monitoring... |
| 394 | 0.5586 | Alternatively, you can grant it the Global adminis... |
| 395 | 0.5583 | The status is 200 OK and the body is empty. HTTP/1... |
| 396 | 0.5583 | Netwrix Auditor Serverthen writes the Activity Rec... |
| 397 | 0.5583 | v10.7 Option Description To import snapshots, you ... |
| 398 | 0.5582 | Do not select the checkbox if you want to configur... |
| 399 | 0.5577 | Step 5 – Open the / etc/ rsyslog.conf file. Step 6... |
| 400 | 0.5574 | v10.7 Configuration parameters to specify in setti... |
| 401 | 0.5573 | Therefore, successful change and access auditing r... |
| 402 | 0.5572 | This option controls how often audit data is expor... |
| 403 | 0.5571 | Netwrix recommends you to create a dedicated folde... |
| 404 | 0.5571 | If AD FS Admin logging is disabled, you should ena... |
| 405 | 0.5570 | v10.7 How It Works Netwrix Auditor add-on for Splu... |
| 406 | 0.5569 | Write Activity Records Schema The Activity Records... |
| 407 | 0.5568 | Default prefix is NA, for example:NA Windows Serve... |
| 408 | 0.5568 | You can enable Auditor to continually enforce the ... |
| 409 | 0.5567 | v10.7 Notify owners of their responsibilities. See... |
| 410 | 0.5565 | Click Import, select object type (Web applica tion... |
| 411 | 0.5564 | Table 2: Registry key (REG_DWORD type) Description... |
| 412 | 0.5562 | Configure a Response Action for Alert Upon the ale... |
| 413 | 0.5562 | ◦◦ To get ‘Who’ (initiator) and ‘When’ (date and t... |
| 414 | 0.5561 | In Object Explorer, right-click each Netwrix datab... |
| 415 | 0.5557 | Filter data by the time interval when the change o... |
| 416 | 0.5556 | The Working Folder widget—Helps you to estimate th... |
| 417 | 0.5556 | ◦◦ Remember to set the filter to “Data Sourceequal... |
| 418 | 0.5556 | From the Logon Activity source properties. Start A... |
| 419 | 0.5555 | Parameter Default value Description General parame... |
| 420 | 0.5551 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 421 | 0.5549 | v10.7 Using historical data For many data sources,... |
| 422 | 0.5547 | These settings must be configured for Everyone sec... |
| 423 | 0.5544 | See the Audit Database topic for additional inform... |
| 424 | 0.5542 | Synology Netwrix Auditor relies on native logs for... |
| 425 | 0.5536 | For example: APIAdminTool.exe api https certificat... |
| 426 | 0.5535 | Make sure the account that runs the task has all n... |
| 427 | 0.5535 | Make sure the account that runs the task has all n... |
| 428 | 0.5535 | Make sure the account that runs the task has all n... |
| 429 | 0.5531 | Controls ticket resolution and corrective measures... |
| 430 | 0.5529 | WriteAgentsToApplicationLog Defines whether to wri... |
| 431 | 0.5527 | It means you retrieved all Activity Records matchi... |
| 432 | 0.5527 | On the computer where Auditor Server resides, you ... |
| 433 | 0.5524 | Activity Records are exported to a local event log... |
| 434 | 0.5523 | At least the first script run should be performed ... |
| 435 | 0.5522 | For more information on audit configuration, refer... |
| 436 | 0.5518 | C:\Addons\Netwrix_Auditor_Activity_Records_ to_Eve... |
| 437 | 0.5518 | For example: Add arguments (optional) file "C:\Add... |
| 438 | 0.5518 | Audit Database settings are properly configured fo... |
| 439 | 0.5518 | NetwrixAuditorPlan – Unless specified, data is wri... |
| 440 | 0.5514 | Table 1: Database name Description Netwrix_AlertsD... |
| 441 | 0.5514 | Do not change this setting unless advised accordin... |
| 442 | 0.5514 | Remember, the Access Reviews version must align to... |
| 443 | 0.5514 | To do that, copy and edit the file with processing... |
| 444 | 0.5509 | EventID {Calculated by add-on} -OR0 Depending on G... |
| 445 | 0.5508 | The product updates the latest snapshot on the reg... |
| 446 | 0.5506 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 447 | 0.5506 | Monitoring plan for File Server data source with '... |
| 448 | 0.5504 | Select the index that will be used to store the co... |
| 449 | 0.5503 | Table 2: Entry in EventData Activity Record field ... |
| 450 | 0.5500 | This may happen due to Secondary Logon Service Whe... |
| 451 | 0.5498 | Auditor informs you if you are running out of spac... |
| 452 | 0.5498 | Users open Auditor Client to work with collected d... |
| 453 | 0.5497 | It will deploy and enable the Netwrix Auditor Conn... |
| 454 | 0.5496 | Step 6 – Run the following command to update group... |
| 455 | 0.5494 | If you are going to configure Fine Grained Auditin... |
| 456 | 0.5490 | For that purpose, special Netwrix utilities should... |
| 457 | 0.5490 | Review Auditor Self-Audit Report Also, there is a ... |
| 458 | 0.5483 | Implemented as a PowerShell script, this add-on fa... |
| 459 | 0.5483 | Implemented as a PowerShell script, this add-on fa... |
| 460 | 0.5482 | Here you can review a brief description of each co... |
| 461 | 0.5479 | Each Activity Record contains the user account, ac... |
| 462 | 0.5479 | Shows all changes across your IT infrastructure, A... |
| 463 | 0.5478 | Netwrix suggests the following execution scenarios... |
| 464 | 0.5477 | Mixed Mode—Default auditing in a newly installed d... |
| 465 | 0.5475 | Therefore, successful change and access auditing r... |
| 466 | 0.5475 | Therefore, successful change and access auditing r... |
| 467 | 0.5475 | Therefore, successful change and access auditing r... |
| 468 | 0.5475 | Therefore, successful change and access auditing r... |
| 469 | 0.5475 | Therefore, successful change and access auditing r... |
| 470 | 0.5475 | Therefore, successful change and access auditing r... |
| 471 | 0.5475 | Therefore, successful change and access auditing r... |
| 472 | 0.5475 | Therefore, successful change and access auditing r... |
| 473 | 0.5475 | Therefore, successful change and access auditing r... |
| 474 | 0.5475 | Therefore, successful change and access auditing r... |
| 475 | 0.5471 | Perform the following steps to integrate alerts wi... |
| 476 | 0.5468 | Reason: unexpected shutdown or system failure Comp... |
| 477 | 0.5468 | To... Execute... Netwrix.ITSM.AlertsUploaderTool.e... |
| 478 | 0.5466 | The default path is "C:\Program Files (x86)\Netwri... |
| 479 | 0.5460 | To review Event Trace Session objects' configurati... |
| 480 | 0.5460 | Activity Records are exported to -NetwrixAuditorUs... |
| 481 | 0.5457 | Aggregating data into a single audit trail simplif... |
| 482 | 0.5456 | If you select a plan name in the addon, make sure ... |
| 483 | 0.5456 | Then click OK to confirm. The Database service acc... |
| 484 | 0.5446 | Start Assessment 3. View Results 4. Complete the p... |
| 485 | 0.5446 | Write audit data to Subscriptions created in the A... |
| 486 | 0.5445 | Follow the steps to change trace log location. Ste... |
| 487 | 0.5444 | Activity Records are exported to -NetwrixAuditorUs... |
| 488 | 0.5444 | Unpack the ZIP archive to a folder of your choice;... |
| 489 | 0.5443 | In the Manage historical snapshots section, click ... |
| 490 | 0.5443 | Older tickets requests are cleared. Step 3 – Resta... |
| 491 | 0.5442 | The tool is located in the Netwrix Auditor install... |
| 492 | 0.5442 | Netwrix Auditor allows auditing the entire SharePo... |
| 493 | 0.5440 | In this case, data will be written to a database l... |
| 494 | 0.5440 | In this case, data will be written to a database l... |
| 495 | 0.5440 | In this case, data will be written to a database l... |
| 496 | 0.5439 | See the Normal and Enterprise Modes for Clusters t... |
| 497 | 0.5439 | Netwrix.ITSM.AlertsUploaderTool.exe / List Review ... |
| 498 | 0.5439 | To specify a nondefault port, provide a new port n... |
| 499 | 0.5438 | If you select a plan name in the addon, make sure ... |
| 500 | 0.5438 | View Reports Create alerts to be notified about su... |
| 501 | 0.5437 | When the add-on operates normally there should be ... |
| 502 | 0.5436 | Step 3 – On the General tab, specify a task name, ... |
| 503 | 0.5434 | Make sure that you have the Access Reviews license... |
| 504 | 0.5434 | Step 1 – On the computer where Auditor Server resi... |
| 505 | 0.5432 | Step 1 – Turn the switch to On if you want a respo... |
| 506 | 0.5431 | Each Activity Record contains the user information... |
| 507 | 0.5431 | Netwrix Auditor Settings In the Settings section, ... |
| 508 | 0.5429 | This command is required to create a shared folder... |
| 509 | 0.5428 | History Allows for on-demand subscription delivery... |
| 510 | 0.5426 | Refer to the Netwrix Privilege Secure documentatio... |
| 511 | 0.5424 | The Netwrix Auditor One or more A ctivity 500 Inte... |
| 512 | 0.5422 | Name of the event log where the events will be Fil... |
| 513 | 0.5421 | Assessment results are reported on the screen and ... |
| 514 | 0.5418 | See the View Reports topic for additional informat... |
| 515 | 0.5417 | Netwrix Auditor will inform you if you are running... |
| 516 | 0.5416 | Data is sent in the request body and must be forma... |
| 517 | 0.5415 | computer that hosts Internal error Netwrix Auditor... |
| 518 | 0.5412 | It will be also selected by default if you are upg... |
| 519 | 0.5411 | Table 1: Option Description Long-Term Archive sett... |
| 520 | 0.5409 | v10.7 Time zone — time zone where Netwrix Auditor ... |
| 521 | 0.5406 | See the Monitoring Planstopic for additional infor... |
| 522 | 0.5405 | C:\Add-ons\Netwrix_Auditor_Event_Log_ Export_Add-o... |
| 523 | 0.5405 | Syntax: server\instance name Each entry must be a ... |
| 524 | 0.5402 | Step 3 – Add script parameters. The console will l... |
| 525 | 0.5399 | Configuring your IT infrastructure may also includ... |
| 526 | 0.5398 | Monitoring plan name,server name,error text For ex... |
| 527 | 0.5398 | With Netwrix Auditor, AWS audit data is kept for m... |
| 528 | 0.5392 | Step 4 – Splunk starts pulling activity records vi... |
| 529 | 0.5392 | For that, start Netwrix Auditor client and navigat... |
| 530 | 0.5391 | Step 1 – Navigate to the Search page of the add-on... |
| 531 | 0.5388 | In this case, data will be written to a database l... |
| 532 | 0.5387 | Unless specified, the service runs under the accou... |
| 533 | 0.5385 | See the Permissions for Oracle Database Auditing t... |
| 534 | 0.5383 | Table 1: Setting Value Max event log size 4 GB Ret... |
| 535 | 0.5381 | Self-audit allows tracking every change to monitor... |
| 536 | 0.5381 | v10.7 Prepare Netwrix Auditor for Data Processing ... |
| 537 | 0.5377 | 503 Service Unavailable Error The Netwrix Auditor ... |
| 538 | 0.5375 | Refer to the Netwrix Privilege Secure documentatio... |
| 539 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 540 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 541 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 542 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 543 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 544 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 545 | 0.5375 | Configuring your IT infrastructure may also includ... |
| 546 | 0.5375 | Step 13 – Ensure that new GPO settings were applie... |
| 547 | 0.5373 | To open User Activity report for the selected user... |
| 548 | 0.5371 | Install for User Activity Core Service By default,... |
| 549 | 0.5368 | Monitoring plan name,server name, resource path Wi... |
| 550 | 0.5368 | The Insertion Strings tab Specify this parameter i... |
| 551 | 0.5366 | v10.7 Access Reviews Netwrix Auditor supports inte... |
| 552 | 0.5362 | Click Accept. Navigate to Log → Categories. Select... |
| 553 | 0.5361 | Splunk Enterprise Splunk Administrator or any othe... |
| 554 | 0.5360 | The Netwrix Auditor Integration API provides acces... |
| 555 | 0.5359 | v10.7 After environment variable substitution, the... |
| 556 | 0.5358 | Unless specified, the service runs under the accou... |
| 557 | 0.5356 | On Ubuntu 16: Navigate to the /etc/rsyslog.d/50def... |
| 558 | 0.5356 | On Ubuntu 16: Navigate to the /etc/rsyslog.d/50def... |
| 559 | 0.5355 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 560 | 0.5355 | Auditor Server • Integration API and Audit Databas... |
| 561 | 0.5352 | If the monitoring plan name in the <NetwrixAuditor... |
| 562 | 0.5351 | Netwrix Auditor allows you to assign differen t ac... |
| 563 | 0.5350 | To check it, navigate to Settings → Integrations t... |
| 564 | 0.5349 | Activity Records are exported to a local event log... |
| 565 | 0.5346 | Navigate to Start → Netwrix Auditor. 22.. Log into... |
| 566 | 0.5345 | See the State–In–Time Reports topic for a dditiona... |
| 567 | 0.5345 | Step 4 – On the Select Installation Type step, you... |
| 568 | 0.5345 | NOTE: Event records with more than 30,000 characte... |
| 569 | 0.5344 | • For monitoring Windows Server and User Activity,... |
| 570 | 0.5340 | If you plan to collect state-in-time data from a S... |
| 571 | 0.5337 | If you select a plan name in the addon, make sure ... |
| 572 | 0.5337 | If you select a plan name in the addon, make sure ... |
| 573 | 0.5334 | Remember to set the filter to “Data Sourceequals O... |
| 574 | 0.5332 | For ONTAP 8.3, just check file-ops. To configure l... |
| 575 | 0.5331 | It is installed together with Netwrix Auditor clie... |
| 576 | 0.5330 | Implemented as a service, this add-on facilitates ... |
| 577 | 0.5330 | See the following Netwrix knowledge base article f... |
| 578 | 0.5329 | For that, start Auditor client and navigate to Sea... |
| 579 | 0.5324 | Activity Records are exported to a local event log... |
| 580 | 0.5323 | Implemented as a service, this add-on facilitates ... |
| 581 | 0.5322 | Internet Information Services (IIS) Auditor suppor... |
| 582 | 0.5320 | Unless specified, data is written to the Netwrix_ ... |
| 583 | 0.5318 | Password Provide the password for the selected acc... |
| 584 | 0.5318 | For example: -file "C:\Addons\Netwrix_Auditor_Add-... |
| 585 | 0.5317 | v10.7 In this case, you need to provide the userna... |
| 586 | 0.5316 | The console will look similar to the following: Wi... |
| 587 | 0.5315 | Step 10 – Assign a less-privileged role to this ac... |
| 588 | 0.5314 | Configuring your IT infrastructure may also includ... |
| 589 | 0.5314 | Configuring your IT infrastructure may also includ... |
| 590 | 0.5311 | v10.7 Parameter Default value Description Instruct... |
| 591 | 0.5310 | You can delegate control over a monitoring plan to... |
| 592 | 0.5306 | These operations can be performed in any of the fo... |
| 593 | 0.5306 | If a domain account is used, make sure to use the ... |
| 594 | 0.5304 | Role-Based Access and Delegation Configure general... |
| 595 | 0.5304 | For that, start Auditor client and navigate to Sea... |
| 596 | 0.5302 | C:\Add-ons\Netwrix_Auditor_Addon_for_Intel_Securit... |
| 597 | 0.5302 | If you select a plan name in the addon, make sure ... |
| 598 | 0.5301 | Activity Records are exported to NetwrixAuditorUse... |
| 599 | 0.5298 | See the Configure Integration API SettingsAudit Da... |
| 600 | 0.5298 | Activity Records are exported to a local event log... |
| 601 | 0.5297 | NOTE: Make sure that your Netwrix Auditor Integrat... |
| 602 | 0.5296 | Other users can obtain audit data by email or with... |
| 603 | 0.5296 | Notification — Configure the Notification settings... |
| 604 | 0.5295 | Install the Add-on Follow the steps to install the... |
| 605 | 0.5294 | The MonitoringPlan element contains sub-elements s... |
| 606 | 0.5293 | You can configure Netwrix Auditor Access Reviews i... |
| 607 | 0.5293 | Parameter Default value Description General parame... |
| 608 | 0.5290 | Sub-elements: Name and ID. If you provide a monito... |
| 609 | 0.5289 | https:// Corp.sharepoint.com/* Contains a list of ... |
| 610 | 0.5286 | Follow the steps to use Netwrix Auditor Access Rev... |
| 611 | 0.5284 | To configure Core Audit for Qumulo file servers 11... |
| 612 | 0.5283 | Unless specified, data is written to Netwrix_Audit... |
| 613 | 0.5281 | If, for some reason, installation has failed, you ... |
| 614 | 0.5281 | See the How to Migrate Netwrix Auditor Working Fol... |
| 615 | 0.5279 | How the Copilot Add-on Works On a high level, the ... |
| 616 | 0.5278 | %ProgramData%\Netwrix Auditor\AuditCore\AuditA v10... |
| 617 | 0.5278 | Review a full list of object types Netwrix Auditor... |
| 618 | 0.5277 | Download the Add-On 1. Download the distribution p... |
| 619 | 0.5275 | Monitoring plan for File Server data source with '... |
| 620 | 0.5275 | If you select to automatically configure audit in ... |
| 621 | 0.5274 | The account must be assigned the Global reviewer r... |
| 622 | 0.5274 | The account must be assigned the Global reviewer r... |
| 623 | 0.5273 | This email lists VMware infrastructure changes and... |
| 624 | 0.5269 | Use this report to investigate how permissions are... |
| 625 | 0.5269 | See the View Reports topic for additional informat... |
| 626 | 0.5268 | See the Monitoring Planstopic for additional infor... |
| 627 | 0.5268 | By default, set to zero offset. MonitoringPlan — U... |
| 628 | 0.5267 | .Net Framework 4.7.2 and above is installed. The c... |
| 629 | 0.5267 | When prompted, accept the license agreement and sp... |
| 630 | 0.5266 | Attachments larger than 50MB will be uploaded to \... |
| 631 | 0.5265 | Specify an item name. Auditor Plan Item Make sure ... |
| 632 | 0.5263 | Table 1: Object type Actions Event ID Cisco ASA de... |
| 633 | 0.5261 | ◦◦ The following Windows Firewall inbound rules mu... |
| 634 | 0.5260 | .NET 4.8 must be installed. See the following topi... |
| 635 | 0.5259 | With enabled HTTPS, provide the computer name as i... |
| 636 | 0.5255 | Activity Records are exported to NetwrixAuditorUse... |
| 637 | 0.5254 | Step 9 – Ensure that new GPO settings applied on a... |
| 638 | 0.5254 | Activity Records are retrieved according to the ac... |
| 639 | 0.5253 | Domain Audit Policy Settings Effective domain cont... |
| 640 | 0.5253 | If you need to be alerted on specific events in yo... |
| 641 | 0.5252 | 135 Retrieve Exchange Netwrix Auditor and dynamic ... |
| 642 | 0.5251 | Make sure to select this parameter if you plan to ... |
| 643 | 0.5248 | • Netwrix Auditor license has expired. • Internal ... |
| 644 | 0.5248 | When Filter data by the time interval when the cha... |
| 645 | 0.5245 | • .NET 4.5 or later must be installed. Execution p... |
| 646 | 0.5245 | Failed Enabling this option on public shares will ... |
| 647 | 0.5244 | Specifies the length of ti meout before events fro... |
| 648 | 0.5244 | File Description Syntax Contains a list of data c ... |
| 649 | 0.5244 | Credential-based is the default option. Refer to t... |
| 650 | 0.5244 | Credential-based is the default option. Refer to t... |
| 651 | 0.5244 | Credential-based is the default option. Refer to t... |
| 652 | 0.5241 | At least the first script run should be performed ... |
| 653 | 0.5240 | A custom account must be granted the same permissi... |
| 654 | 0.5239 | Then, do one of the following: Audit SharePoint re... |
| 655 | 0.5238 | The Audit Database settings are configured in Audi... |
| 656 | 0.5237 | See the Adjust DHCP Server Operational Log Setting... |
| 657 | 0.5237 | See the State–In–Time Reports topic for additional... |
| 658 | 0.5235 | Netwrix_ImportDB Stores data imported from Long-Te... |
| 659 | 0.5235 | Task read attempt No — Message located in \Tasks T... |
| 660 | 0.5235 | See the Predefi ned Reports topic for additional i... |
| 661 | 0.5231 | In this case, you need to provide the username of ... |
| 662 | 0.5230 | Activity Records are exported to a local event log... |
| 663 | 0.5230 | The alert response action settings in Auditor Serv... |
| 664 | 0.5225 | Review the following for additional information: N... |
| 665 | 0.5224 | Activity Records are exported to a local event log... |
| 666 | 0.5224 | Splunk is a log management solution that enables s... |
| 667 | 0.5221 | Optionally, you can click the Create Test Ticket b... |
| 668 | 0.5219 | Recommendations This section covers the Recommenda... |
| 669 | 0.5218 | You can configure your IT Infrastructure for monit... |
| 670 | 0.5218 | See the About Netwrix Auditor topic for additional... |
| 671 | 0.5216 | In this case, data will be written to a database A... |
| 672 | 0.5216 | In this case, data will be written to a database A... |
| 673 | 0.5216 | CIM might not have data models for some of the act... |
| 674 | 0.5212 | In the Performance Monitor snap-in, navigate to Pe... |
| 675 | 0.5212 | Step 2 – Unpack the installation package. The foll... |
| 676 | 0.5211 | See the Custom Search-Based Reports topic for addi... |
| 677 | 0.5210 | Step 3 – In the General tab, set the Startup type ... |
| 678 | 0.5208 | v10.7 Endpoint Use to export data from the Audit D... |
| 679 | 0.5208 | Enable integration Netwrix.ITSM.AlertsUploaderTool... |
| 680 | 0.5208 | For that, start Auditor client and navigate to Sea... |
| 681 | 0.5207 | For example: https://siteColl* v10.7 File Descript... |
| 682 | 0.5207 | In Netwrix Auditor 9.0, Netwrix has updated API sc... |
| 683 | 0.5207 | To report on other snapshots, make sure they are a... |
| 684 | 0.5206 | -NetwrixAuditorUserName enterprise\NAuser NetwrixA... |
| 685 | 0.5206 | You may need to limit their scope to a specific mo... |
| 686 | 0.5205 | Step 1 – Upgrade Netwrix Auditor Server OS to the ... |
| 687 | 0.5204 | Activity Records are exported to -NetwrixAuditorUs... |
| 688 | 0.5203 | You will get a list of activity records with detai... |
| 689 | 0.5203 | Alternatively, a fter NetwrixAuditorUserName Curre... |
| 690 | 0.5202 | Run Windows PowerShell as administrator and execut... |
| 691 | 0.5202 | 88.. Switch to the Admin Access tab. Under the Sel... |
| 692 | 0.5201 | Ensure that... Set-ExecutionPolicy Unrestricted Th... |
| 693 | 0.5201 | For example, if you are using the add-on that impo... |
| 694 | 0.5201 | Step 4 – Save the dbparam.ini file. Download the A... |
| 695 | 0.5200 | Visit Netwrix Corporation Software License Agreeme... |
| 696 | 0.5199 | v10.7 CAUTION: Folder associated with NETWRIX AUDI... |
| 697 | 0.5198 | Clicking the Add plan button opens the New Monitor... |
| 698 | 0.5195 | C:\Add-ons\Netwrix_Auditor_Addon_for_ LogRhythm.ps... |
| 699 | 0.5195 | v10.7 Option Description Password Provide the pass... |
| 700 | 0.5192 | Manually – Native audit settings must be adjusted ... |
| 701 | 0.5192 | In addition to the restrictions for a monitoring p... |
| 702 | 0.5192 | Step 3 – Create a shared folder named netwrix_audi... |
| 703 | 0.5192 | See the Netwrix Privilege Secure topic for additio... |
| 704 | 0.5190 | All Changes by Data Source Shows all changes acros... |
| 705 | 0.5190 | empty string. For example: ,,\\\\*\\System Volume ... |
| 706 | 0.5189 | • The Audit Database settings are configured in Au... |
| 707 | 0.5188 | the fi le path. Alternatively, the command line wi... |
| 708 | 0.5185 | NetwrixAuditorUserPassword Current user credential... |
| 709 | 0.5185 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 710 | 0.5184 | Add an Exchange Online Monitoring Plan Follow the ... |
| 711 | 0.5183 | Specify an object name (e.g., Policy) to find all ... |
| 712 | 0.5183 | See the Netwrix Privilege Secure topic for additio... |
| 713 | 0.5183 | Set the Max Size of Entire Index to match the expe... |
| 714 | 0.5182 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Solarwinds_L... |
| 715 | 0.5181 | Configure Auditor to monitor SharePoint Online rea... |
| 716 | 0.5180 | You can use the Search field, or apply a filter to... |
| 717 | 0.5179 | For that, click Notification settings, then follow... |
| 718 | 0.5176 | The designated service team performs data analysis... |
| 719 | 0.5175 | Do one of the following, depending on your Oracle ... |
| 720 | 0.5173 | Time zone — time zone where Netwrix Auditor server... |
| 721 | 0.5171 | Execute... Store audit records to XML audit trail ... |
| 722 | 0.5170 | Set the value to "730" (which equals 2 years). Act... |
| 723 | 0.5170 | Oracle Database has the following options: Databas... |
| 724 | 0.5167 | In this Table 1: Parameter Default value Descripti... |
| 725 | 0.5167 | v10.7 Step 6 – Click Configure. Next, for the most... |
| 726 | 0.5167 | Provide the new data input parameters: Name of the... |
| 727 | 0.5166 | If you have configured alerting in Netwrix Auditor... |
| 728 | 0.5166 | Click Add Recipient and provide email summaries ad... |
| 729 | 0.5166 | Integration API and Audit Database settings are co... |
| 730 | 0.5165 | Add this parameter to write data in JSON format. O... |
| 731 | 0.5164 | Please note that all audit types should be enabled... |
| 732 | 0.5163 | v10.7 Add MS Teams monitoring plan Follow the step... |
| 733 | 0.5161 | For details, see Manage historical snapshots optio... |
| 734 | 0.5161 | In addition to the restrictions for a monitoring p... |
| 735 | 0.5159 | This refers, for example, to Netwrix Auditor for N... |
| 736 | 0.5150 | Step 1 – In Netwrix Auditor, find your Exchange On... |
| 737 | 0.5149 | NOTE: Netwrix recommends using different credentia... |
| 738 | 0.5146 | Step 1 – Get your certificate or generate a self-s... |
| 739 | 0.5145 | Step 1 – In main Netwrix Auditor menu, select Moni... |
| 740 | 0.5144 | The account must be assigned the Global reviewer r... |
| 741 | 0.5143 | Review the event IDs available in the Netwrix Non-... |
| 742 | 0.5143 | Reports with Video Netwrix Auditor can be configur... |
| 743 | 0.5143 | In the Event Log field enter "Netwrix Non-Owner Ma... |
| 744 | 0.5138 | If you cannot log into Netwrix Auditor with your W... |
| 745 | 0.5138 | If you select a plan name in the addon, make sure ... |
| 746 | 0.5137 | Password Provide the password for the selected acc... |
| 747 | 0.5136 | v10.7 Follow the steps to review the recommendatio... |
| 748 | 0.5135 | Available for report and search subscriptions only... |
| 749 | 0.5135 | MonitoringPlan — Unless specified, data is written... |
| 750 | 0.5135 | Configure Video Recordings Playback Settings Video... |
| 751 | 0.5135 | See Configure Integration API and Audit Database. ... |
| 752 | 0.5134 | For example, if you are going to audit Internet In... |
| 753 | 0.5134 | This includes all Audit databases, Integration API... |
| 754 | 0.5133 | Step 1 – Log in to the Nasuni Management Console a... |
| 755 | 0.5133 | Although you can always use the add-on as is, but ... |
| 756 | 0.5131 | Specify path to the short-term archive (Netwrix Au... |
| 757 | 0.5131 | NOTE: If you select a plan name in the add-on, mak... |
| 758 | 0.5130 | Add-on running on the same machine as Auditor Serv... |
| 759 | 0.5129 | In this case, a single alert will be sent instead ... |
| 760 | 0.5129 | Step 6 – (optional) To adjust the add-on operation... |
| 761 | 0.5124 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 762 | 0.5120 | See Configure Integration API and Audit Database. ... |
| 763 | 0.5120 | Core Service Deploy Netwrix Auditor for SharePoint... |
| 764 | 0.5117 | Error message will not appear on the screen; inste... |
| 765 | 0.5117 | v10.7 Requirements This topic provides the require... |
| 766 | 0.5117 | Password Provide the password for the selected acc... |
| 767 | 0.5115 | Once the script execution completed, you can start... |
| 768 | 0.5114 | See the Navigation and Customize Home Screen topic... |
| 769 | 0.5114 | v10.7 Review the following for additional informat... |
| 770 | 0.5113 | Step 1 – Check prerequisites. Since the add-ons wo... |
| 771 | 0.5113 | Table 1: XML curl -H "Content-Type:application/xml... |
| 772 | 0.5112 | <Address>172.28.3.18</Address> The add-on runs on ... |
| 773 | 0.5110 | *) Services HKEY_LOCAL_MACHINE\SYSTEM\ControlSet00... |
| 774 | 0.5110 | Review and Manage Subscriptions On the main Netwri... |
| 775 | 0.5108 | For that, a unified audit trail is required, suppo... |
| 776 | 0.5108 | For your convenience, the product provides predefi... |
| 777 | 0.5108 | Use this path—UNC path to the file share located o... |
| 778 | 0.5105 | Also, remember to perform the following steps for ... |
| 779 | 0.5100 | The body is empty. The posted Error Large file exc... |
| 780 | 0.5100 | Follow the steps to add an account to the Netwrix ... |
| 781 | 0.5098 | For more information on additional deployment opti... |
| 782 | 0.5097 | Provide the IP address of the interface you specif... |
| 783 | 0.5096 | Add more ticket parameters or update values if nec... |
| 784 | 0.5096 | Auditor Plan Item Make sure to create a dedicated ... |
| 785 | 0.5096 | Auditor Plan Item Make sure to create a dedicated ... |
| 786 | 0.5095 | See the Netwrix Auditor Health Log topic for addit... |
| 787 | 0.5094 | If so, consider that current user account (logged ... |
| 788 | 0.5091 | Installation Overview The Netwrix Auditor Access R... |
| 789 | 0.5088 | The Audit Database settings are configured in Audi... |
| 790 | 0.5086 | The Netwrix Auditor Archive Service is busy or unr... |
| 791 | 0.5084 | During the Netwrix Auditor for SharePoint Core Ser... |
| 792 | 0.5083 | On a high level, the add-on works as follows: 11..... |
| 793 | 0.5083 | Netwrix suggests the following execution scenarios... |
| 794 | 0.5081 | Delete Netwrix Auditor for Active Directory Compre... |
| 795 | 0.5080 | Netwrix Auditor is a visibility platform for user ... |
| 796 | 0.5079 | See the Integration API topic for additional infor... |
| 797 | 0.5079 | 33.. Right-click the Operational log and select Pr... |
| 798 | 0.5077 | For example: Add arguments (optional) file "C:\Add... |
| 799 | 0.5075 | Overexposed Files and Folders Monitoring plan for ... |
| 800 | 0.5073 | Data is ArcSightHost 172.28.6.24 - retrieved from ... |
| 801 | 0.5073 | Step 2 – Click Search. NOTE: You might want to app... |
| 802 | 0.5073 | NetwrixAuditorPassword Current user credentials Pr... |
| 803 | 0.5071 | Tip for reading the table: For example, on the com... |
| 804 | 0.5071 | Password Enter a password for SMTP authentication.... |
| 805 | 0.5069 | See the Deploy the Service topic for additional in... |
| 806 | 0.5069 | Step 1 – Install the Netwrix Auditor Access Review... |
| 807 | 0.5069 | The console will look similar to the following: Wi... |
| 808 | 0.5067 | Netwrix suggests the following execution scenarios... |
| 809 | 0.5067 | Then, do one of the following: • Click Add and pro... |
| 810 | 0.5066 | v10.7 Add Microsoft Entra ID monitoring plan Follo... |
| 811 | 0.5064 | The add-on uploads audit trails to ArcSight Logger... |
| 812 | 0.5064 | In the Add Syslog Server dialog, find the IP addre... |
| 813 | 0.5062 | Follow the steps to exclude data from the Active D... |
| 814 | 0.5062 | Logon Activity Monitoring Scope You can fine-tune ... |
| 815 | 0.5061 | Table 1: Scenario Example The add-on runs on the A... |
| 816 | 0.5055 | They will help to ensure imported data consistency... |
| 817 | 0.5055 | It should be a third-party Syslog forward service ... |
| 818 | 0.5054 | For that purpose, you can use a specially designed... |
| 819 | 0.5053 | The output Activity Records may contain the follow... |
| 820 | 0.5053 | The list of available add-ons keeps growing becaus... |
| 821 | 0.5052 | To store data to the database, leave this check bo... |
| 822 | 0.5050 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 823 | 0.5050 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 824 | 0.5050 | The add-on will match the application name and the... |
| 825 | 0.5049 | Launch an Internet browser and enter the following... |
| 826 | 0.5047 | Policy Subnode Policy Name Audit Events Audit Secu... |
| 827 | 0.5046 | Step 2 – Select a monitoring plan and the time ran... |
| 828 | 0.5045 | See the Access Reviews topic for a dditional infor... |
| 829 | 0.5044 | Default is Priority 3 — Priority Normal Response. ... |
| 830 | 0.5043 | The account must be assigned the Global reviewer r... |
| 831 | 0.5043 | A service ticket is then created manually or autom... |
| 832 | 0.5043 | EventData is filled in with data from the Activity... |
| 833 | 0.5042 | This file is located in the same folder as SyslogS... |
| 834 | 0.5041 | Creating a ticket with Customer portal 11.. Sign i... |
| 835 | 0.5040 | Note that the new monitoring scope restrictions ap... |
| 836 | 0.5037 | Auditor time format. By default, set NetwrixAudito... |
| 837 | 0.5035 | The User Activity Core Service is installed on the... |
| 838 | 0.5034 | The service automatically creates incident tickets... |
| 839 | 0.5033 | Besides notifying you on who changed what, when an... |
| 840 | 0.5031 | For example, you may need to change logging and re... |
| 841 | 0.5029 | Append help to any command to see available parame... |
| 842 | 0.5027 | You can enable Auditor to continually enforce the ... |
| 843 | 0.5023 | See the Netwrix Privilege Secure topic for additio... |
| 844 | 0.5023 | The account must be assigned the Contributor role ... |
| 845 | 0.5022 | monitoring plan name,server name,class name,proper... |
| 846 | 0.5019 | Open Administrative Tools > Services, right-click ... |
| 847 | 0.5018 | Step 4 – The selected account is displayed in the ... |
| 848 | 0.5018 | General Considerations and Known Issues During the... |
| 849 | 0.5017 | XML: <Item> <Name>Item name</Name> — </Item> JSON:... |
| 850 | 0.5016 | Monitor SQL Server configuration changes Always en... |
| 851 | 0.5012 | NOTE: Netwrix recommends using different credentia... |
| 852 | 0.5012 | NOTE: Netwrix recommends using different credentia... |
| 853 | 0.5011 | Netwrix suggests the following execution scenarios... |
| 854 | 0.5011 | Required role Retrieve all activity records and wr... |
| 855 | 0.5009 | Splunk Enterprise Splunk version is 8.0.6 or highe... |
| 856 | 0.5009 | Manually – Native audit settings must be adjusted ... |
| 857 | 0.5008 | v10.7 Report Requirement Netwrix Data Classificati... |
| 858 | 0.5008 | v10.7 Step 6 – Click Next. Step 7 – You need to ma... |
| 859 | 0.5000 | Netwrix Auditor shows only the top 2,000 anomalies... |
| 860 | 0.4998 | Place the Netwrix.xsl file there, too, so that def... |
| 861 | 0.4998 | If both components are installed on the same machi... |
| 862 | 0.4995 | User account under which data will be w ritten to ... |
| 863 | 0.4993 | For your convenience, the account specified will b... |
| 864 | 0.4993 | Ensure that... ◦ Command line preview looks like t... |
| 865 | 0.4992 | Alternatively, you can grant the Global administra... |
| 866 | 0.4991 | • Location • Name • Ownership Permissions: ◦ Group... |
| 867 | 0.4989 | Program/script Input "Powershell.exe". Add argumen... |
| 868 | 0.4988 | If you want to use another account, make sure it h... |
| 869 | 0.4987 | To review collected data, you must be assigned the... |
| 870 | 0.4985 | Seamless upgrade to Netwrix Auditor 10.7 is suppor... |
| 871 | 0.4984 | For that, start Auditor client and navigate to Sea... |
| 872 | 0.4980 | Review the following for additional information: E... |
| 873 | 0.4979 | Navigate to Start → Run and type "regedit". Regist... |
| 874 | 0.4976 | The system will send a test message to the s pecif... |
| 875 | 0.4976 | Step 1 – In the Auditor main screen, select Settin... |
| 876 | 0.4976 | See the Data C ollecting Account topic for additio... |
| 877 | 0.4973 | You can configure Netwrix Auditor to use an existi... |
| 878 | 0.4972 | Step 1 – Click Update. Step 2 – In the dialog that... |
| 879 | 0.4972 | At least the first script run should be performed ... |
| 880 | 0.4970 | On the computer where Auditor Server resides, you ... |
| 881 | 0.4968 | Step 5 – Configure and run reviews. The Entitlemen... |
| 882 | 0.4968 | See the Audit Configuration Assistant topic for a ... |
| 883 | 0.4968 | If you select a plan name in the add-on, make sure... |
| 884 | 0.4966 | Make sure to select this parameter if you plan to ... |
| 885 | 0.4965 | Otherwise — if you change the storage location whi... |
| 886 | 0.4964 | For a full list of audit s ettings required to col... |
| 887 | 0.4964 | Table 1: Option Setting Log Format "XML" or "EVTX"... |
| 888 | 0.4963 | • The Netwrix Auditor Archive Service is unreachab... |
| 889 | 0.4962 | Deploy the required number of Netwrix Auditor clie... |
| 890 | 0.4960 | SharePoint Monitoring Scope You can fine-tune Netw... |
| 891 | 0.4959 | NOTE: Before installing Netwrix Auditor, make sure... |
| 892 | 0.4959 | Do one of the following: To configure Fortinet For... |
| 893 | 0.4959 | The user retrieving data from the Audit Database i... |
| 894 | 0.4959 | Otherwise, the program will automatically search f... |
| 895 | 0.4957 | For the newly created app, you should use the Appl... |
| 896 | 0.4956 | Step 3 – Configure basic parameters as follows: En... |
| 897 | 0.4956 | To learn more about Netwrix Auditor Core Services,... |
| 898 | 0.4956 | Example 4 SCVMM and/or Auditor run on the machines... |
| 899 | 0.4955 | NOTE: Perform this procedure only if you enabled t... |
| 900 | 0.4951 | and dynamic range: TCP Domain controllers Server g... |
| 901 | 0.4950 | The alerts have preset filters and can be easily u... |
| 902 | 0.4948 | To report on other snapshots, make sure they are a... |
| 903 | 0.4948 | Table 1: Parameter Default value Description The a... |
| 904 | 0.4946 | Use Netwrix Privilege Secure as a Data Collecting ... |
| 905 | 0.4946 | The dashboard includes the following widgets: The ... |
| 906 | 0.4946 | See the Configure Scope topic for a dditional info... |
| 907 | 0.4944 | To apply tags to an alert, navigate to alert setti... |
| 908 | 0.4944 | Prior to the Netwrix Auditor for SharePoint Core S... |
| 909 | 0.4943 | Microsoft Exchange Server 2010 is no longer suppor... |
| 910 | 0.4942 | Depending on the execution scenario you choose, yo... |
| 911 | 0.4941 | IP Address — server IP address. Port— port for inc... |
| 912 | 0.4940 | Added and Moved v10.7 After configuring all filter... |
| 913 | 0.4939 | If you want Netwrix Auditor to audit custom regist... |
| 914 | 0.4937 | Step 4 – Click Save. Optionally, you can select Do... |
| 915 | 0.4937 | Most parameters are optional, the service uses the... |
| 916 | 0.4936 | The Audit Database settings are configured in the ... |
| 917 | 0.4935 | You will get a list of activity records with detai... |
| 918 | 0.4932 | To grant required permissions, assign granular App... |
| 919 | 0.4932 | To grant required permissions, assign granular App... |
| 920 | 0.4932 | Databases To store data from the data sources incl... |
| 921 | 0.4931 | An IT administrator configures the Integration API... |
| 922 | 0.4931 | Review the following for additional information: O... |
| 923 | 0.4930 | Possible values: • Empty—Check Netwrix Auditor cer... |
| 924 | 0.4927 | Disable integration NOTE: You can disable integrat... |
| 925 | 0.4926 | v10.7 If an event occurs that triggers an alert, a... |
| 926 | 0.4925 | Consider the following: Step 1 – Configure Securit... |
| 927 | 0.4923 | POST Activity Records activity_records/ Write Acti... |
| 928 | 0.4921 | Also notice that the response action will be launc... |
| 929 | 0.4921 | Download the product installation package. Open th... |
| 930 | 0.4918 | The TCP 9699 port (default Auditor Integr ation AP... |
| 931 | 0.4913 | See the Microsoft Turn auditing on or off article ... |
| 932 | 0.4913 | For detailed information, refer to the Microsoft a... |
| 933 | 0.4913 | Port Protocol Source Target Purpose Monitored netw... |
| 934 | 0.4912 | Also, Netwrix prepares add-ons—sample scripts—to h... |
| 935 | 0.4912 | You can configure these settings automatically usi... |
| 936 | 0.4910 | v10.7 Attribute 1: Member of - equals \| Value: Dom... |
| 937 | 0.4910 | To collect event data from the domain, this servic... |
| 938 | 0.4910 | v10.7 6. Using the Integration API, the add-on sen... |
| 939 | 0.4910 | Registry key (REG_DWORD type) Description / Value ... |
| 940 | 0.4903 | See the User Management topic in the Netwrix Data ... |
| 941 | 0.4903 | Supported versions are SQL Server 2012 and later (... |
| 942 | 0.4902 | Method Endpoint POST Data https://{host:port}/ net... |
| 943 | 0.4902 | Netwrix Auditor 53 UDP DNS Server DNS Client Serve... |
| 944 | 0.4902 | Step 4 – Click New Rule. In the New Inbound Rule w... |
| 945 | 0.4902 | Follow the steps to configure Event Log Size and R... |
| 946 | 0.4901 | Monitored Objects Netwrix Auditor tracks changes m... |
| 947 | 0.4901 | To feed data, send a POST request containing Activ... |
| 948 | 0.4901 | If any conflicts are detected with your current au... |
| 949 | 0.4899 | ◦◦ On the Netwrix Auditor host system/server: The ... |
| 950 | 0.4897 | To create the Event Trace Session object: logman i... |
| 951 | 0.4897 | The helpdesk supervisor has access to both folders... |
| 952 | 0.4896 | Provide the name of the UDP port used to listen to... |
| 953 | 0.4895 | Table 1: Scenario Example The add-on runs on theAu... |
| 954 | 0.4895 | search results. For example to exclude the adminCo... |
| 955 | 0.4894 | Note that a CSV file will exist only while the exe... |
| 956 | 0.4893 | Step 3 – Configure the following audit policies. T... |
| 957 | 0.4892 | By default, Netwrix Auditor will monitor all share... |
| 958 | 0.4892 | Step 1 – On the computer where Auditor Server resi... |
| 959 | 0.4890 | For that, in the dashboard window click Subscribe ... |
| 960 | 0.4889 | Password Enter a password for SMTP authentication.... |
| 961 | 0.4889 | Recipients will be notified by email, and response... |
| 962 | 0.4889 | At least the first script run should be performed ... |
| 963 | 0.4888 | The account must be assigned the Global reviewer r... |
| 964 | 0.4887 | Configure Logging for CTERA Edge Filer Prior to st... |
| 965 | 0.4885 | Make sure to create a dedicated item inAuditor in ... |
| 966 | 0.4885 | Consider the following: To store data from the dat... |
| 967 | 0.4885 | Add the following parameters to the end: /s:server... |
| 968 | 0.4885 | Mark all as reviewed – Click to mark all alerts in... |
| 969 | 0.4883 | v10.7 Review the following for additional informat... |
| 970 | 0.4882 | See the Use Group Managed Service Account (gMSA) t... |
| 971 | 0.4879 | VMware Monitoring Scope You can fine-tune Netwrix ... |
| 972 | 0.4879 | Table 1: Option Description You can review a sampl... |
| 973 | 0.4878 | Capacity To examine the repository capacity and da... |
| 974 | 0.4878 | Before installing Auditor, make sure that the Wind... |
| 975 | 0.4876 | Make sure to create a dedicated item in Auditor in... |
| 976 | 0.4873 | Step 5 – You can specify any other user group, but... |
| 977 | 0.4873 | Major benefits: Gain a high-level view of the data... |
| 978 | 0.4873 | If you plan to have more than one Netwrix Auditor ... |
| 979 | 0.4872 | To monitor the mount points targeted at the subfol... |
| 980 | 0.4871 | You can configure your IT Infrastructure for monit... |
| 981 | 0.4870 | Execute... ALTER SYSTEM SET audit_trail=XML SCOPE=... |
| 982 | 0.4870 | Each data source has a dedicated item type. Netwri... |
| 983 | 0.4867 | C:\Addons\Netwrix_Auditor_CEF_Export_Addon. ps1 -O... |
| 984 | 0.4866 | See the Audit Database topic for additional inform... |
| 985 | 0.4866 | Step 2 – Open a port for inbound connections. See ... |
| 986 | 0.4865 | If Auditor Server becomes unavailable for some tim... |
| 987 | 0.4865 | All Netwrix product announcements have moved to th... |
| 988 | 0.4864 | Allow outbound connections to remote ports on the ... |
| 989 | 0.4864 | Make sure that the folder is accessible from compu... |
| 990 | 0.4862 | Location (optional) Provides a link to a corrupted... |
| 991 | 0.4859 | The anomalies list displays details for each anoma... |
| 992 | 0.4859 | The TCP 9699 port must be open on firew alls betwe... |
| 993 | 0.4858 | Service which helps Netwrix Auditor SQL Server Bro... |
| 994 | 0.4858 | Step 9 – Ensure that new GPO settings applied on a... |
| 995 | 0.4856 | At the end of each run, the script creates the Net... |
| 996 | 0.4856 | At the end of each run, the script creates the Net... |
| 997 | 0.4855 | The add-on exports Activity Records from a remote ... |
| 998 | 0.4851 | Alternatively, you can grant the Global administra... |
| 999 | 0.4850 | Table 1: Description Enabling this option on publi... |
| 1000 | 0.4847 | The tool transfers information on service accounts... |
| 1001 | 0.4847 | At the end of each run, the script creates the Net... |
| 1002 | 0.4847 | You will get a list of activity records with detai... |
| 1003 | 0.4846 | See the Use Filters in Advanced Mode topic for add... |
| 1004 | 0.4846 | By default, Netwrix Auditor Integration API works ... |
| 1005 | 0.4845 | When prompted, accept the license agreement and sp... |
| 1006 | 0.4844 | Specify the account that you want to define this p... |
| 1007 | 0.4844 | Set the Network Security: Restrict NTLM: Outgoing ... |
| 1008 | 0.4844 | Always enabled, as SQL Server configuration change... |
| 1009 | 0.4843 | At the end of each run, the script creates the Net... |
| 1010 | 0.4843 | ServiceNow Incident Management The add-on works in... |
| 1011 | 0.4842 | You will need to create this fi le manually and co... |
| 1012 | 0.4842 | See the Use Netwrix Privilege Secure as a Data Col... |
| 1013 | 0.4841 | Step 2 – Navigate to Network wide > Configure > Ge... |
| 1014 | 0.4841 | How It Works On a high level, the add-on works as ... |
| 1015 | 0.4840 | v10.7 Parameter Default value Description The add-... |
| 1016 | 0.4840 | The Auditor Server side User account under which d... |
| 1017 | 0.4839 | Standard Auditing (trail a uditing Oracle Database... |
| 1018 | 0.4839 | Table 1: File Description Syntax OmitErrorsList.tx... |
| 1019 | 0.4839 | See the Audit Database topic for additional inform... |
| 1020 | 0.4839 | NOTE: The account must be assigned the Global revi... |
| 1021 | 0.4838 | If your issue is not listed in the table below, tr... |
| 1022 | 0.4838 | Step 4 – Run the shell script by executing the fol... |
| 1023 | 0.4838 | Out of the box, messages from Red Hat Enterprise L... |
| 1024 | 0.4837 | Step 7 – Navigate to Event Filters and click Add t... |
| 1025 | 0.4836 | Make sure Do not overwrite events (Clear logs manu... |
| 1026 | 0.4836 | You can click Browse to select a computer from the... |
| 1027 | 0.4835 | You will get a list of activity records with detai... |
| 1028 | 0.4835 | Step 1 – On Netwrix Auditor server, go to the %Net... |
| 1029 | 0.4834 | So, when planning your Netwrix Auditor deployment,... |
| 1030 | 0.4833 | Step 1 – On the computer where SharePoint Central ... |
| 1031 | 0.4832 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 1032 | 0.4830 | v10.7 Option Description Accept List Specify a lis... |
| 1033 | 0.4830 | See the Data C ollecting Account topic for additio... |
| 1034 | 0.4829 | Later, you can always create custom report from in... |
| 1035 | 0.4826 | However, if you want to use specific settings for ... |
| 1036 | 0.4825 | Step 4 – Configure audit manually. For 8.3, review... |
| 1037 | 0.4825 | Click OK to save the settings and close the dialog... |
| 1038 | 0.4825 | Step 2 – Navigate to Event Viewer tree > Windows L... |
| 1039 | 0.4823 | It is recommended to create a dedicated monitoring... |
| 1040 | 0.4823 | Select the Informational value for the following p... |
| 1041 | 0.4821 | To find out a log’s name, navigate to Start > Wind... |
| 1042 | 0.4819 | Logon Activity Ports Review a full list of protoco... |
| 1043 | 0.4818 | Application permissions are consented by an admini... |
| 1044 | 0.4813 | If you want to restart monitoring these objects, r... |
| 1045 | 0.4813 | On the computer where Netwrix Auditor Server resid... |
| 1046 | 0.4812 | The Microsoft-IIS-Configuration/Operational log mu... |
| 1047 | 0.4812 | Step 1 – Download the product installation package... |
| 1048 | 0.4812 | Step 3 – In the Settings list, locate Downloads > ... |
| 1049 | 0.4812 | Manually, as described in the corresponding topics... |
| 1050 | 0.4811 | These steps must be taken each time a new audit da... |
| 1051 | 0.4811 | Table 1: File name Description ta-netwrix-auditor-... |
| 1052 | 0.4810 | Allow outbound connections from the dynamic (1024 ... |
| 1053 | 0.4809 | On a high level, the add-on works as follows: The ... |
| 1054 | 0.4808 | By default, you can log in with your Windows crede... |
| 1055 | 0.4808 | To find out a log’s name, navigate to Start > Wind... |
| 1056 | 0.4808 | See the Netwrix Privilege Secure and How to Add Mi... |
| 1057 | 0.4807 | Netwrix Auditor helps you gain complete visibility... |
| 1058 | 0.4807 | Add arguments (optional) Add a path to the add-on ... |
| 1059 | 0.4806 | v10.7 You might want to apply a filter to narrow d... |
| 1060 | 0.4804 | Lines that start with the # sign are treated as co... |
| 1061 | 0.4804 | NetwrixAuditorDateTimeFormat yyyy-MM-ddTHH:mm:ssZ ... |
| 1062 | 0.4801 | See the Create a New Plan topic for additional inf... |
| 1063 | 0.4801 | Then you will provide this account in the monitori... |
| 1064 | 0.4800 | The user retrieving data from the Audit Database i... |
| 1065 | 0.4796 | In particular, the script deploys and starts Netwr... |
| 1066 | 0.4795 | Method Endpoint POST Data https://{host:port}/ net... |
| 1067 | 0.4795 | Use this report to identify data at high risk and ... |
| 1068 | 0.4794 | Security Event Log Settings Security event log set... |
| 1069 | 0.4794 | See Data Collecting Account for a dditional inform... |
| 1070 | 0.4793 | Local Admin on the Netwrix Auditor server. The com... |
| 1071 | 0.4792 | The account must be assigned the Global reviewer r... |
| 1072 | 0.4790 | Starting with version 10.7, you can implement the ... |
| 1073 | 0.4789 | Some settings in Auditor are configure d incorrect... |
| 1074 | 0.4787 | Monitoring plan for File Server data source with '... |
| 1075 | 0.4786 | Step 1 – Start the Auditor client and navigate to ... |
| 1076 | 0.4786 | To be able to watch video files captured by Netwri... |
| 1077 | 0.4785 | PaloAlto Devices Review a full list of object type... |
| 1078 | 0.4785 | NetwrixAuditorDateTimeFormat yyyy-MM-ddTHH:mm:ssZ ... |
| 1079 | 0.4784 | Netwrix Auditor ignores changes to system data (e.... |
| 1080 | 0.4784 | To process all anomalies In the Actions section, s... |
| 1081 | 0.4784 | Configure ConnectWise This section describes how t... |
| 1082 | 0.4784 | Netwrix_CommonDB Stores views to provide cross-dat... |
| 1083 | 0.4783 | v10.7 You might want to apply a filter to narrow d... |
| 1084 | 0.4782 | Troubleshooting Log files of Netwrix Account Locko... |
| 1085 | 0.4780 | Possible values: NetwrixAuditorCertificateThumbpr ... |
| 1086 | 0.4779 | Manually – Native audit settings must be adjusted ... |
| 1087 | 0.4778 | Log in to HPE Aruba web interface. Navigate to Mob... |
| 1088 | 0.4776 | NetwrixAuditorPassword Current user credentials Un... |
| 1089 | 0.4776 | Step 1 – Select an alert from the list and enable ... |
| 1090 | 0.4776 | v10.7 set facility <facility_name> set port 514 se... |
| 1091 | 0.4773 | Automate Add-On Execution To ensure you feed the m... |
| 1092 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1093 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1094 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1095 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1096 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1097 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1098 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1099 | 0.4773 | The Audit Database settings are configured in Audi... |
| 1100 | 0.4771 | See the Objects topic for additional information. ... |
| 1101 | 0.4771 | v10.7 Option Description available for 7 days. Che... |
| 1102 | 0.4769 | In this case, data will be written to a database l... |
| 1103 | 0.4769 | To receive an invitation to the Partner Portal, pl... |
| 1104 | 0.4768 | Select this checkbox if you want to verify securit... |
| 1105 | 0.4766 | v10.7 Option Description By default, Netwrix Audit... |
| 1106 | 0.4763 | The account must be assigned the Contributor role ... |
| 1107 | 0.4762 | Step 3 – Add script parameters. The console will l... |
| 1108 | 0.4762 | User account under which data will be w ritten Aud... |
| 1109 | 0.4759 | Every time you run the script, Auditor makes a tim... |
| 1110 | 0.4759 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 1111 | 0.4759 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 1112 | 0.4758 | v10.7 Export Activity Records in Bulk As said, Net... |
| 1113 | 0.4757 | You might want to apply a filter to narrow down yo... |
| 1114 | 0.4757 | Step 8 – Apply the following settings to your Perm... |
| 1115 | 0.4757 | These Email Templates (multiple files) Located in ... |
| 1116 | 0.4756 | Activity Records are on_for_Intel_Security.ps1 exp... |
| 1117 | 0.4754 | When finished, click OK. Table 1: File Description... |
| 1118 | 0.4753 | For Microsoft Entra ID Auditing To collect audit d... |
| 1119 | 0.4753 | The user retrieving data from the Audit Database i... |
| 1120 | 0.4753 | The user account for running the service and conne... |
| 1121 | 0.4752 | See the User Activity topic for additional informa... |
| 1122 | 0.4751 | Data is retrieved via Oracle Instant Client applic... |
| 1123 | 0.4750 | Make sure to grant sufficient permissions on folde... |
| 1124 | 0.4750 | This information will help you to take corrective ... |
| 1125 | 0.4749 | Upgrade Procedure You can upgrade Netwrix Auditor ... |
| 1126 | 0.4749 | If your deployment planning reveals that SQL Serve... |
| 1127 | 0.4748 | Scenario A: Advanced audit policies Enable the fol... |
| 1128 | 0.4748 | Step 10 – Type repadmin /syncall command and press... |
| 1129 | 0.4744 | Data is activity_records</ written to a remote Net... |
| 1130 | 0.4743 | DataCollectionPassword Specify user account passwo... |
| 1131 | 0.4742 | This topic focuses on the CEF Export SIEM solution... |
| 1132 | 0.4740 | Error details: 0x80040204 Cannot convert the attri... |
| 1133 | 0.4738 | Considerations for Netwrix Privilege Secure Integr... |
| 1134 | 0.4738 | To reduce the impact on the system drive in large ... |
| 1135 | 0.4737 | While you can send Netwrix Auditor data to one of ... |
| 1136 | 0.4736 | By default, it will contain the following detailed... |
| 1137 | 0.4735 | Possible parameter values: • True — fill in the Ev... |
| 1138 | 0.4735 | Possible parameter values: • True — fill in the Ev... |
| 1139 | 0.4733 | The data collected by Auditor is updated at least ... |
| 1140 | 0.4732 | Under the Root directory option, click Browse and ... |
| 1141 | 0.4732 | Parameter Default value Description Connection to ... |
| 1142 | 0.4732 | The wizard will start and ask the additional param... |
| 1143 | 0.4731 | Oracle administrator prepares a dedicated service ... |
| 1144 | 0.4730 | Please refer to the Managing Indexers and Clusters... |
| 1145 | 0.4730 | The Audit Database settings are configured in Audi... |
| 1146 | 0.4730 | The Audit Database settings are configured in Audi... |
| 1147 | 0.4729 | For example: #*,server,MicrosoftDNS_Server #*,*,St... |
| 1148 | 0.4728 | Perform the procedure below, prior to the Core Ser... |
| 1149 | 0.4728 | Specifies the length of ti meout before events fro... |
| 1150 | 0.4728 | The details for each role include its name, type, ... |
| 1151 | 0.4726 | Subscriptions can be uploaded either to a file sha... |
| 1152 | 0.4724 | See the Netwrix Privilege Secure topic for additio... |
| 1153 | 0.4723 | Specify the account for collecting data Select the... |
| 1154 | 0.4722 | For the account, worksta tion, application name fi... |
| 1155 | 0.4722 | NOTE: The account must be assigned the Contributor... |
| 1156 | 0.4722 | Step 1 – On the computer where AuditorServer resid... |
| 1157 | 0.4720 | This functionality is currently available for the ... |
| 1158 | 0.4720 | v10.7 Parameter Default value Description is not a... |
| 1159 | 0.4718 | You cannot select event categories if you use Clus... |
| 1160 | 0.4716 | SQL Server Express Edition with Advanced Services ... |
| 1161 | 0.4716 | v10.7 To manage API security settings with APIAdmi... |
| 1162 | 0.4715 | See the Use Netwrix Privilege Secure as a Data Col... |
| 1163 | 0.4713 | Pay attention to the "Data categories" column in s... |
| 1164 | 0.4712 | To learn more about modern authentication, refer t... |
| 1165 | 0.4711 | Deployment Scenarios The Add-On can run on any com... |
| 1166 | 0.4710 | Depending on Error the error code, the response bo... |
| 1167 | 0.4710 | Step 5 – Specify the application name and Netwrix ... |
| 1168 | 0.4707 | Review a full list of object types and attributes ... |
| 1169 | 0.4705 | Object path —path to the monitored object, as form... |
| 1170 | 0.4705 | See the Netwrix Privilege Secure topic for additio... |
| 1171 | 0.4704 | You can write RESTful requests using any tool or a... |
| 1172 | 0.4703 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 1173 | 0.4703 | Step 1 – Log in to your CyberArk system. Step 2 – ... |
| 1174 | 0.4702 | Aggregating data into a single audit trail simplif... |
| 1175 | 0.4701 | v10.7 Delete Netwrix Auditor Mailbox Access Core S... |
| 1176 | 0.4701 | This option controls how often audit data is expor... |
| 1177 | 0.4700 | Location XML is considered a default format for Ne... |
| 1178 | 0.4700 | Name of the event log where the events will be Fil... |
| 1179 | 0.4700 | Click Manage to review the full list of accounts a... |
| 1180 | 0.4697 | Netwrix Auditor periodically checks for updates so... |
| 1181 | 0.4697 | ObjectType Yes nvarchar 255 An type of affected ob... |
| 1182 | 0.4697 | The section below explains how to create, disable ... |
| 1183 | 0.4696 | NOTE: You can disable integration with one alert a... |
| 1184 | 0.4696 | Table 1: Service account Description Account for d... |
| 1185 | 0.4696 | Owner Performs Review — Owners process the review,... |
| 1186 | 0.4694 | Allow outbound connections from the dynamic (1024 ... |
| 1187 | 0.4693 | Required permissions • Unless specified, the Netwr... |
| 1188 | 0.4690 | Default is 514. Note that if you are using Netwrix... |
| 1189 | 0.4689 | Create a shortcut for this executable file. Right-... |
| 1190 | 0.4688 | Now you can augment SIEM with data collected by Au... |
| 1191 | 0.4683 | Do one of the following: To configure HPE Aruba de... |
| 1192 | 0.4679 | Otherwise, the add-on will not be able to write da... |
| 1193 | 0.4678 | See Permissions for Table 1: Option Description Sh... |
| 1194 | 0.4678 | In workgroups The computer where Auditor Server is... |
| 1195 | 0.4678 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1196 | 0.4677 | The syntax greatly depends on the tool you use. Sc... |
| 1197 | 0.4675 | Follow the steps to configure settings for other l... |
| 1198 | 0.4674 | You can skip some parameters—the script uses a def... |
| 1199 | 0.4674 | v10.7 Option Description Refer to Configure Scope ... |
| 1200 | 0.4674 | Follow the steps to exclude data from the Active D... |
| 1201 | 0.4673 | In this case, the credentials will not be stored b... |
| 1202 | 0.4673 | In this case, the credentials will not be stored b... |
| 1203 | 0.4672 | v10.7 Step 3 – In the Windows Firewall with Advanc... |
| 1204 | 0.4672 | To use this option, you need to provide the Activi... |
| 1205 | 0.4672 | To use this option, you need to provide the Activi... |
| 1206 | 0.4671 | Alternatively, you can limit the auditing scope to... |
| 1207 | 0.4671 | See the COMPLIANCE MAPPING Compliance Mappings top... |
| 1208 | 0.4671 | At least the first script run should be performed ... |
| 1209 | 0.4671 | At least the first script run should be performed ... |
| 1210 | 0.4668 | For that, you should estimate the required capacit... |
| 1211 | 0.4668 | Follow the steps to exclude data from the Group Po... |
| 1212 | 0.4667 | You can perform this procedure on any of the Excha... |
| 1213 | 0.4665 | Alert Details: Instructs the system to fill in the... |
| 1214 | 0.4664 | The product has the following limitations dependin... |
| 1215 | 0.4659 | You can specify any other user group, but in this ... |
| 1216 | 0.4656 | For each item, you can: Specify a custom account f... |
| 1217 | 0.4656 | Run a search request to /netwrix/api/v1/activity_r... |
| 1218 | 0.4656 | See the Prerequisites and Audit Database topics fo... |
| 1219 | 0.4655 | If you plan, however, not to use Netwrix Auditor b... |
| 1220 | 0.4655 | ): No special configuration required to audit RMAN... |
| 1221 | 0.4654 | Step 3 – In the Advanced Security Settings for <Sh... |
| 1222 | 0.4653 | Aggregating data into a single audit trail simplif... |
| 1223 | 0.4653 | Selected mailbox 11.. On the computer where the mo... |
| 1224 | 0.4653 | In this case, the credentials will not be stored b... |
| 1225 | 0.4652 | Download and install Netwrix Auditor on that machi... |
| 1226 | 0.4647 | On the computer where Netwrix Auditor Server resid... |
| 1227 | 0.4647 | NetwrixAuditorPlan — When specified, overrides the... |
| 1228 | 0.4645 | NetwrixAuditorPassword Current user credentials Un... |
| 1229 | 0.4645 | You can also configure and receive alerts on the e... |
| 1230 | 0.4645 | Configure the Event Log Size Using Group Policy Pe... |
| 1231 | 0.4644 | Specify a list of IP addresses of syslog events so... |
| 1232 | 0.4644 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 1233 | 0.4643 | Step 3 – Locate the InitialDescription parameter a... |
| 1234 | 0.4642 | Ensure that... The user retrieving data from the A... |
| 1235 | 0.4641 | Parameter Default value Description NetwrixIntegra... |
| 1236 | 0.4641 | Microsoft 365 Microsoft 365 audit configuration wi... |
| 1237 | 0.4640 | Remember, for Exchange auditing, do the following:... |
| 1238 | 0.4639 | Make sure to specify a unique name. To modify a cu... |
| 1239 | 0.4639 | The TCP 9699 port (default Integration API port) i... |
| 1240 | 0.4639 | Review the following Microsoft technical a rticle ... |
| 1241 | 0.4638 | v10.7 44.. Click Search next to Login Name and spe... |
| 1242 | 0.4638 | Step 1 – Navigate to Start > Netwrix Auditor > Net... |
| 1243 | 0.4637 | • The TCP 9699 port must be open on Windows firewa... |
| 1244 | 0.4636 | See the Netwrix Privilege Secure topic for v10.7 a... |
| 1245 | 0.4636 | Netwrix Privilege Secure is ready to use as an acc... |
| 1246 | 0.4635 | Step 5 – Double-click the newly created rule and o... |
| 1247 | 0.4634 | NETWRIX AUDITOR is unable to work in a workgroup. ... |
| 1248 | 0.4633 | Required permissions Unless specified, the Netwrix... |
| 1249 | 0.4633 | • NOCHECK—Do not check Netwrix Auditor certificat ... |
| 1250 | 0.4632 | v10.7 You can apply a filter to narrow down your s... |
| 1251 | 0.4630 | NetwrixAuditorEndpoint https://localhost:9699/netw... |
| 1252 | 0.4630 | v10.7 Windows Server 2012 R2 Windows Server 2012 C... |
| 1253 | 0.4630 | Allowed-addresses are: 192.168.1.0/24. Check the c... |
| 1254 | 0.4624 | v10.7 Option Description Read Access Configure Net... |
| 1255 | 0.4622 | Licenses The Licenses tab allows you to review the... |
| 1256 | 0.4622 | In the Netwrix Auditor API location field provide ... |
| 1257 | 0.4621 | Step 1 – Select the AD FS data source in this moni... |
| 1258 | 0.4620 | You will only have to enter password. v10.7 To cre... |
| 1259 | 0.4619 | See State–In–Time Reports for more information. CA... |
| 1260 | 0.4618 | Password – Provide password for this account. Summ... |
| 1261 | 0.4616 | Follow the steps to configure syslog forwarding. S... |
| 1262 | 0.4615 | NOTE: Access Reviews is a separately licensed prod... |
| 1263 | 0.4615 | You can also copy event details. Select the event ... |
| 1264 | 0.4615 | Aggregating data into a single audit trail simplif... |
| 1265 | 0.4615 | Aggregating data into a single audit trail simplif... |
| 1266 | 0.4615 | Aggregating data into a single audit trail simplif... |
| 1267 | 0.4612 | Step 2 – On the General tab, specify a task name. ... |
| 1268 | 0.4612 | Step 2 – On the General tab, specify a task name. ... |
| 1269 | 0.4610 | When enabled, Netwrix users can also browse sensit... |
| 1270 | 0.4609 | For input Activity Records, the data source is aut... |
| 1271 | 0.4609 | Audit Database service account An account used by ... |
| 1272 | 0.4609 | The System account is used to launch the add-on vi... |
| 1273 | 0.4608 | Aggregating data into a single audit trail simplif... |
| 1274 | 0.4607 | Step 3 – Add script parameters. The console will l... |
| 1275 | 0.4607 | The second option is Resource-based. To use this o... |
| 1276 | 0.4605 | Step 3 – Click Modify under the API settings secti... |
| 1277 | 0.4604 | Step 2 – Configure Syslog message forwarding in Cy... |
| 1278 | 0.4604 | If the configuration is correct, you will see the ... |
| 1279 | 0.4602 | Provide a different password if necessary. Table 2... |
| 1280 | 0.4602 | Provide a different password if necessary. Table 2... |
| 1281 | 0.4602 | Click Add to add a new principal. You can also sel... |
| 1282 | 0.4602 | Step 2 – Select Netwrix Privilege Secure. Step 3 –... |
| 1283 | 0.4601 | Table 2: Configure custom location of session reco... |
| 1284 | 0.4601 | For a full list of audit settings and instructions... |
| 1285 | 0.4601 | Run the following command in nlci: v10.7 ncli> rsy... |
| 1286 | 0.4600 | Overexposed Sensitive Data Objects Monitoring plan... |
| 1287 | 0.4598 | v10.7 Investigations By default, the Audit Databas... |
| 1288 | 0.4598 | For example: hostname(config)# logging trap 5 77..... |
| 1289 | 0.4597 | It is recommended to select Adjust audit settings ... |
| 1290 | 0.4597 | Migrate to Unified Audit Starting with 10.5 versio... |
| 1291 | 0.4597 | If you want to run the add-on on another machine, ... |
| 1292 | 0.4597 | Data is C:\Add-ons\Netwrix_Auditor_Addwritten to a... |
| 1293 | 0.4595 | Specify the account for collecting data Scope Tabl... |
| 1294 | 0.4593 | See the Choose Appropriate Execution Scenario topi... |
| 1295 | 0.4593 | See the Choose Appropriate Execution Scenario topi... |
| 1296 | 0.4592 | Each Activity Record contains initiator’s account,... |
| 1297 | 0.4591 | Table 1: Option Description Read Access Audit Shar... |
| 1298 | 0.4591 | StartsWith EndsWith Table 1: Filter Description Su... |
| 1299 | 0.4591 | Provide a different password if necessary. v10.7 P... |
| 1300 | 0.4590 | Step 1 – To create or modify an audit archiving fi... |
| 1301 | 0.4589 | Step 6 – Specify a plan name. Settings for Data Co... |
| 1302 | 0.4588 | Your current audit settings will be checked on eac... |
| 1303 | 0.4587 | See the Permissions for Oracle Database Auditing t... |
| 1304 | 0.4586 | See the Prerequisites and Audit Database topics fo... |
| 1305 | 0.4586 | See the Prerequisites and Audit Database topics fo... |
| 1306 | 0.4586 | In the Add New Syslog Servers dialog, complete the... |
| 1307 | 0.4584 | SQL Server Reporting Services Netwrix Auditor util... |
| 1308 | 0.4584 | Step 2 – Complete the following fields: Option Des... |
| 1309 | 0.4583 | Or simply drag and drop the add-on file in the con... |
| 1310 | 0.4580 | Sensitive Files and Folders by Source Monitoring p... |
| 1311 | 0.4580 | For monitoring Active Directory, File Servers, Sha... |
| 1312 | 0.4580 | Registry key (REG_DWORD type) Description / Value ... |
| 1313 | 0.4579 | Audit logon events policy must be set to "Success.... |
| 1314 | 0.4578 | If you have not already started using Netwrix Audi... |
| 1315 | 0.4578 | Before running or scheduling the add-on, you shoul... |
| 1316 | 0.4577 | Once all the Activity Records are retrieved, you w... |
| 1317 | 0.4576 | To exclude computers from within the s pecified ra... |
| 1318 | 0.4576 | See State–In–Time Reports for more information. CA... |
| 1319 | 0.4576 | Starting with version 10.7, you can implement the ... |
| 1320 | 0.4575 | See the State–In–Time Reports topic for additional... |
| 1321 | 0.4575 | As the interactive search in the Netwrix Auditor c... |
| 1322 | 0.4574 | The issues occur because the product applies data ... |
| 1323 | 0.4574 | For example: *,server,MicrosoftDNS_Se rver *,*,Std... |
| 1324 | 0.4571 | For that: On the computer where Netwrix Auditor is... |
| 1325 | 0.4568 | The tool will be launched in a new window. See the... |
| 1326 | 0.4567 | NOTE: For the Netwrix Auditor Access Reviews appli... |
| 1327 | 0.4567 | Specify a resource name (e.g., Enterprise) to find... |
| 1328 | 0.4567 | The user account for running the service and conne... |
| 1329 | 0.4565 | Note that events exceeding 4000 symbols are trimme... |
| 1330 | 0.4561 | To do it, click Configure next to Audit archiving ... |
| 1331 | 0.4560 | The wizard will start and ask the additional param... |
| 1332 | 0.4557 | v10.7 Configure Audit Settings for CIFS File Share... |
| 1333 | 0.4557 | Auditor add-on for SIEMNetwrixAuditorUserName Tabl... |
| 1334 | 0.4555 | Allow outbound connections from the dynamic (1024 ... |
| 1335 | 0.4555 | This significant ly improves data transfer and min... |
| 1336 | 0.4554 | v10.7 Prerequisites Netwrix Auditor Integration AP... |
| 1337 | 0.4554 | Later, you can always run it from the Start menu o... |
| 1338 | 0.4553 | The account used to run Netwrix Account Lockout Ex... |
| 1339 | 0.4552 | Program/script Input "Powershell.exe". Add argumen... |
| 1340 | 0.4549 | Step 3 – In the Netwrix Auditor Client Users Prope... |
| 1341 | 0.4549 | Step 3 – Make sure Enable logging is selected. Ste... |
| 1342 | 0.4549 | Creating, sending, or Admin receiving a message is... |
| 1343 | 0.4548 | Netwrix Privilege Secure. Starting with version 10... |
| 1344 | 0.4547 | Provide alert names as they appear in Auditor. NOT... |
| 1345 | 0.4547 | v10.7 The second option is Resource-based. To use ... |
| 1346 | 0.4546 | AD FS Servers Data Collection For Active Directory... |
| 1347 | 0.4546 | To get the add-on up and running, refer the follow... |
| 1348 | 0.4545 | When prompted to configure the Audit database sett... |
| 1349 | 0.4544 | The Security event log maximum size must be set to... |
| 1350 | 0.4544 | User/password – Provide a username and password fo... |
| 1351 | 0.4543 | Step 2 – In the right pane, select the Items tab. ... |
| 1352 | 0.4542 | Specify an item name. Make sure to create a dedica... |
| 1353 | 0.4542 | Specify an item name. Make sure to create a dedica... |
| 1354 | 0.4541 | To audit successful changes on NetApp 8.x or earli... |
| 1355 | 0.4541 | For monitoring Windows Server and User Activity, e... |
| 1356 | 0.4540 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 1357 | 0.4540 | Considerations for Oracle Database 11g Starting wi... |
| 1358 | 0.4539 | The account must belong to the same domain where N... |
| 1359 | 0.4538 | ArcSight Netwrix Auditor helps you extend auditing... |
| 1360 | 0.4538 | Otherwise, the add-on will not be able to write da... |
| 1361 | 0.4537 | Click Apply. Fortinet FortiGate Devices Review a f... |
| 1362 | 0.4536 | All filters are applied using AND logic. By defaul... |
| 1363 | 0.4534 | Access key is used to run requests to AWS SDK, CLI... |
| 1364 | 0.4533 | NetwrixAuditorUserName Current user credentials Un... |
| 1365 | 0.4533 | Provide alert names as they appear in Auditor. NOT... |
| 1366 | 0.4532 | cmdlet.param=friendlyna me For example: RoleGroupM... |
| 1367 | 0.4532 | For that, run the following command: ncli> rsyslog... |
| 1368 | 0.4532 | omitreporterrors.txt Contains a list of errors to ... |
| 1369 | 0.4530 | Review the following for additional information: C... |
| 1370 | 0.4530 | You can get add-ons within the product. To do so, ... |
| 1371 | 0.4530 | On the target server: The account requires Read sh... |
| 1372 | 0.4528 | Step 3 – If you have a client-server deployment, t... |
| 1373 | 0.4527 | Events collected from any other source will be ign... |
| 1374 | 0.4526 | The Audit Database settings are configured in Audi... |
| 1375 | 0.4526 | See the following topics for additional informatio... |
| 1376 | 0.4525 | Make sure this account has sufficient rights to co... |
| 1377 | 0.4525 | Select an event log from the drop-down list. You w... |
| 1378 | 0.4524 | Possible values: Empty—Check Netwrix Auditor certi... |
| 1379 | 0.4524 | See the Check the Windows Services Status topic fo... |
| 1380 | 0.4523 | Method Endpoint POST Data https://{host:port}/ net... |
| 1381 | 0.4523 | Example: SQLSRV01\MSSQL2016\|C:\Logs\NA trace logs\... |
| 1382 | 0.4521 | You must define connection details: Auditor Server... |
| 1383 | 0.4520 | Step 3 – Configure the following audit policies. P... |
| 1384 | 0.4519 | Enter local user account name and password, then c... |
| 1385 | 0.4519 | Please consider the following: For the data collec... |
| 1386 | 0.4518 | Step 3 – Select the type of the Access Policy you ... |
| 1387 | 0.4517 | You can apply a filter to narrow down your search ... |
| 1388 | 0.4516 | Step 4 – In a separate Advanced Security Settings ... |
| 1389 | 0.4516 | Specify the account for collecting data Starting w... |
| 1390 | 0.4516 | The Activity Record structure is described in the ... |
| 1391 | 0.4516 | The Activity Record structure is described in the ... |
| 1392 | 0.4514 | See the Monitoring Scope topic for additional info... |
| 1393 | 0.4509 | v10.7 44.. Make sure the Enable logging option is ... |
| 1394 | 0.4508 | Implemented as a PowerShell script, this add-on au... |
| 1395 | 0.4508 | • For monitoring Windows Server and User Activity,... |
| 1396 | 0.4508 | The add-on works in collaboration with Netwrix Aud... |
| 1397 | 0.4508 | The add-on works in collaboration with Netwrix Aud... |
| 1398 | 0.4507 | Step 1 – On the audited server, open the Local Sec... |
| 1399 | 0.4506 | You can also configure and receive alerts on the e... |
| 1400 | 0.4506 | Registry key (REG_DWORD type) Description / Value ... |
| 1401 | 0.4506 | Starting with version 10.7, you can implement the ... |
| 1402 | 0.4505 | Users open Auditor Client to work with collected d... |
| 1403 | 0.4501 | Manually – Native audit settings must be adjusted ... |
| 1404 | 0.4500 | If you want to run searches and generate reports, ... |
| 1405 | 0.4499 | Netwrix Privilege Secure Starting with version 10.... |
| 1406 | 0.4498 | The add-on will operate as a Syslog listener for N... |
| 1407 | 0.4496 | For example: -file "C:\Addons\Netwrix_Auditor_Addv... |
| 1408 | 0.4496 | For exclusive: all Windows logs events will be exc... |
| 1409 | 0.4494 | Deploy the required number of Netwrix Auditor clie... |
| 1410 | 0.4494 | Table 1: Parameter Default value Description Conne... |
| 1411 | 0.4494 | Table 1: Parameter Default value Description Conne... |
| 1412 | 0.4491 | Issues encountered during examination section is s... |
| 1413 | 0.4490 | This folder points to / ifs: isi smb shares create... |
| 1414 | 0.4489 | • NOCHECK—Do not check Netwrix Auditor certificate... |
| 1415 | 0.4489 | You can configure your IT Infrastructure for monit... |
| 1416 | 0.4488 | Default prefix is NA, for example:NA Windows Serve... |
| 1417 | 0.4487 | Audit SharePoint Online configuration and content ... |
| 1418 | 0.4485 | Change Log Level The AccessInformationCenter.Servi... |
| 1419 | 0.4484 | The procedure below provides a possible way to spe... |
| 1420 | 0.4484 | Enterprise Overview Dashboard Enterprise Overview ... |
| 1421 | 0.4484 | See the File Servers topic for additional informat... |
| 1422 | 0.4483 | If the utility is installed on the remote machine ... |
| 1423 | 0.4481 | Second monitoring plan for collecting data from Or... |
| 1424 | 0.4481 | When specified, overrides the NetwrixAuditorPlanIt... |
| 1425 | 0.4479 | Refer to the following documentation to learn more... |
| 1426 | 0.4479 | Tip for reading the table: For example, on the com... |
| 1427 | 0.4477 | If the monitoring plan name in the <NetwrixAuditor... |
| 1428 | 0.4472 | Step 1 – Navigate to Start > Windows Administrativ... |
| 1429 | 0.4471 | Required role The user must be assigned the Global... |
| 1430 | 0.4470 | Auditor skips all automated deactivation actions f... |
| 1431 | 0.4469 | Also, several dedicated databases are created auto... |
| 1432 | 0.4469 | On Red Hat Enterprise Linux 7, perform the followi... |
| 1433 | 0.4469 | Step 3 – Select the type of the Access Policy you ... |
| 1434 | 0.4466 | See the Network Traffic Compression topic for addi... |
| 1435 | 0.4465 | Device class: ◦◦ CD and DVD ◦◦ Floppy Drives Remov... |
| 1436 | 0.4464 | Provide the port configured in your monitoring pla... |
| 1437 | 0.4459 | You can skip or define parameters depending on you... |
| 1438 | 0.4459 | You can skip or define parameters depending on you... |
| 1439 | 0.4459 | To get the add-on up and running, please read the ... |
| 1440 | 0.4459 | The log is available on Windows Server 2012 R2 and... |
| 1441 | 0.4457 | You can use a single account to collect audit data... |
| 1442 | 0.4457 | Starting with version 10.7, you can implement the ... |
| 1443 | 0.4456 | For v10.7 Windows Server NOTE: Prior to configurin... |
| 1444 | 0.4455 | The account must be a member of the local Administ... |
| 1445 | 0.4453 | For ONTAP 8.3, just check file-ops. v10.7 33.. Cre... |
| 1446 | 0.4453 | Step 5 – Review sensitive data. Netwrix suggests t... |
| 1447 | 0.4452 | If you want to run the add-on on another machine, ... |
| 1448 | 0.4452 | You can skip or define parameters depending on you... |
| 1449 | 0.4450 | Ensure that... .NET Framework 4.5 or later is inst... |
| 1450 | 0.4447 | Step 2 – Depending on the user's delegated scope, ... |
| 1451 | 0.4446 | Accept List Specify a list of IP addresses of sysl... |
| 1452 | 0.4444 | Step 5 – Complete the Event Filters wizard. Comple... |
| 1453 | 0.4444 | v10.7 Issue Reason and solution Monitoring Plan: <... |
| 1454 | 0.4444 | Each activity record contains the Who-What-When-Wh... |
| 1455 | 0.4444 | You can configure your IT Infrastructure for monit... |
| 1456 | 0.4443 | Configure Syslog Message Forwarding in CyberArk On... |
| 1457 | 0.4443 | Step 5 – In the Manage Snapshots window, select th... |
| 1458 | 0.4442 | OutputFolder C:\CEF_Export C:\Addons\Netwrix_Audit... |
| 1459 | 0.4442 | Other Activity Summaries generated and delivered b... |
| 1460 | 0.4441 | In busy environments and during activity peaks, wo... |
| 1461 | 0.4441 | For all Windows server versions Run the auditpol u... |
| 1462 | 0.4441 | See next: Navigation Automate Sign-in to the Clien... |
| 1463 | 0.4440 | See the Role-Based Access and Delegation topic for... |
| 1464 | 0.4439 | If you want to use modern authentication and the N... |
| 1465 | 0.4439 | If not set, <not set> is reported. Object path —pa... |
| 1466 | 0.4439 | Use the omitreadaccess.txt to exclude MYSERVER\* S... |
| 1467 | 0.4437 | Contains a list of AD paths to be For example, you... |
| 1468 | 0.4436 | Auditor will automatically configure audit setting... |
| 1469 | 0.4435 | SQL Server Objects Review a full list of all objec... |
| 1470 | 0.4434 | <domain\user> The file contains a list of user For... |
| 1471 | 0.4433 | Follow the steps to exclude data from the Windows ... |
| 1472 | 0.4433 | Table 2: Parameter Default value Description Event... |
| 1473 | 0.4432 | It means you reached the end of the Audit Database... |
| 1474 | 0.4431 | If you want to run the add-on on another machine, ... |
| 1475 | 0.4430 | v10.7 On... Ensure that... Role-Based Access and D... |
| 1476 | 0.4430 | To configure removable storage media monitoring re... |
| 1477 | 0.4429 | Scope Specify restriction filters to narrow your m... |
| 1478 | 0.4429 | Default prefix is NA, for example:NA Windows Serve... |
| 1479 | 0.4429 | Step 3 – After configuring all filters, click Add ... |
| 1480 | 0.4422 | Prior to the Netwrix Auditor for SharePoint Core S... |
| 1481 | 0.4422 | Active Directory State-In-Time Reports Examine the... |
| 1482 | 0.4422 | So, you should register an Microsoft Entra ID app ... |
| 1483 | 0.4421 | For auditing cloud-based applications (Microsoft E... |
| 1484 | 0.4421 | For example, if you grant the data collecting acco... |
| 1485 | 0.4420 | Step 2 – By default, the security log is set to ov... |
| 1486 | 0.4420 | Changes Audit SharePoint farm configuration change... |
| 1487 | 0.4418 | Sufficient access rights in Netwrix Auditor, which... |
| 1488 | 0.4416 | Configuration objects store the information on sit... |
| 1489 | 0.4416 | For that purpose, you can use a specially designed... |
| 1490 | 0.4415 | The name cannot be changed. ◦ <path to the EventTr... |
| 1491 | 0.4415 | Specify a name of associated monitoring plan in Au... |
| 1492 | 0.4414 | Please be aware that monitoring of actions perform... |
| 1493 | 0.4414 | Click Browse to select a folder on the computer th... |
| 1494 | 0.4413 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 1495 | 0.4413 | Specify Active Directory credentials Provide the n... |
| 1496 | 0.4413 | Specify Active Directory credentials Provide the n... |
| 1497 | 0.4413 | * v10.7 A wildcard (*) is supported. You can use *... |
| 1498 | 0.4411 | Its convenient interactive search interface enable... |
| 1499 | 0.4411 | v10.7 Automatically through a monitoring plan – Th... |
| 1500 | 0.4411 | Event log field name Filled in with value Details ... |
| 1501 | 0.4410 | MonitoringPlanItem — Specify an item name. Make su... |
| 1502 | 0.4409 | DataCollection UDP port for receiving incoming Sys... |
| 1503 | 0.4409 | If a user is removed from this list, agentomituser... |
| 1504 | 0.4408 | Step 3 – Run the NetwrixOktaAddon.exe and follow t... |
| 1505 | 0.4407 | An event that indicates a significant problem such... |
| 1506 | 0.4405 | It also generates summary reports that can be deli... |
| 1507 | 0.4405 | v10.7 The add-on operates as a syslog listener for... |
| 1508 | 0.4403 | When prompted to configure the Audit database sett... |
| 1509 | 0.4402 | Review a full list of object types Netwrix Auditor... |
| 1510 | 0.4402 | You can configure a single Netwrix Auditor client ... |
| 1511 | 0.4401 | You can add any elements (a dashboard, report, ale... |
| 1512 | 0.4401 | Step 1 – Configure Data Collecting Account, as des... |
| 1513 | 0.4401 | Step 5 – On the Destination Folder step, specify t... |
| 1514 | 0.4399 | You can configure your IT Infrastructure for monit... |
| 1515 | 0.4398 | NetwrixAuditorUserName Current user credentials Un... |
| 1516 | 0.4398 | Activity Records are exported to a local folder. C... |
| 1517 | 0.4397 | The service will connect to Auditor Server using t... |
| 1518 | 0.4397 | You can configure your IT Infrastructure for monit... |
| 1519 | 0.4396 | Table 1: To... Execute... Disable API APIAdminTool... |
| 1520 | 0.4396 | On the add-on installation server, the administrat... |
| 1521 | 0.4395 | If you want to run the add-on on another machine, ... |
| 1522 | 0.4395 | If you want to run the add-on on another machine, ... |
| 1523 | 0.4394 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1524 | 0.4394 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1525 | 0.4394 | To do this, right-click a task and click Run. Work... |
| 1526 | 0.4394 | Major benefits: Gain a high-level view of the data... |
| 1527 | 0.4393 | Configure Integration API Settings Follow the step... |
| 1528 | 0.4393 | See the Compliance Reports topic for additional in... |
| 1529 | 0.4391 | For example: -file "C:\Addons\Netwrix_Auditor_Addo... |
| 1530 | 0.4390 | The retention method of the log must be set to “Ov... |
| 1531 | 0.4386 | Table 1: On... Ensure that... The Auditor Server s... |
| 1532 | 0.4386 | For a full list of the rights and permissions requ... |
| 1533 | 0.4385 | If you accept, Netwrix collects statistical inform... |
| 1534 | 0.4384 | In the Specify a name for your custom report dialo... |
| 1535 | 0.4384 | The maximum size of the attachment file is 50 MB. ... |
| 1536 | 0.4383 | Check that you have configured the audit s ettings... |
| 1537 | 0.4381 | Change and Activity Reports Change and activity re... |
| 1538 | 0.4381 | v10.7 Step 12 – After the validation, click Finish... |
| 1539 | 0.4381 | The changes include creation, modifica tion, delet... |
| 1540 | 0.4378 | v10.7 Object type Details Description Administrato... |
| 1541 | 0.4378 | Table 1: Platform API (ISI_PRIV_LOGIN_PAPI) readon... |
| 1542 | 0.4375 | Such instances may have a lot of maintenance plans... |
| 1543 | 0.4375 | Step 2 – Mount this file system on a mount point, ... |
| 1544 | 0.4375 | You have already identified the intruder and now y... |
| 1545 | 0.4375 | Netwrix Auditor 53 UDP DNS Server DNS Client Serve... |
| 1546 | 0.4375 | The summary section shows: Role name Role type — F... |
| 1547 | 0.4374 | See the Table 1: On... Ensure that... Role-Based A... |
| 1548 | 0.4374 | Configuration Tile This tile helps you set up and ... |
| 1549 | 0.4374 | The product will be automatically installed on com... |
| 1550 | 0.4374 | Step 2 – Complete the fields. Review the following... |
| 1551 | 0.4373 | Step 3 – Click the Add button. You can use a singl... |
| 1552 | 0.4373 | For example, the product failed to process a domai... |
| 1553 | 0.4373 | To delete a custom report Navigate to Reports → Cu... |
| 1554 | 0.4372 | If not selected, then your current Windows cr eden... |
| 1555 | 0.4372 | Customers who are logged in to the Netwrix Custome... |
| 1556 | 0.4371 | v10.7 Create a Group Policy to Deploy Netwrix Audi... |
| 1557 | 0.4370 | v10.7 Export SSRS-based reports To export SSRS-bas... |
| 1558 | 0.4367 | NetwrixAuditorHost localhost:9699 Assumes that the... |
| 1559 | 0.4365 | See the First Launch topic for additional informat... |
| 1560 | 0.4364 | 11.. On the DHCP server, navigate to Event Viewer.... |
| 1561 | 0.4363 | To review data sources and items included in each ... |
| 1562 | 0.4363 | Statement ID — This attribute appears if an object... |
| 1563 | 0.4362 | Step 3 – Right-click the newly created GPO and sel... |
| 1564 | 0.4361 | For input Activity Records, the data source is aut... |
| 1565 | 0.4360 | Major benefits: Table 1: Pre-installation procedur... |
| 1566 | 0.4359 | By default, it is set to "C:\ProgramData\Netwrix A... |
| 1567 | 0.4359 | Enable / disable an existing alert Step 1 – Select... |
| 1568 | 0.4358 | Oracle Database Monitoring Scope You can fine-tune... |
| 1569 | 0.4358 | COMPLIANCE MAPPING Enables you to review how Audit... |
| 1570 | 0.4358 | NOTE: This is applicable for NetApp and Dell Data ... |
| 1571 | 0.4357 | In the Services snap-in, locate the Microsoft Exch... |
| 1572 | 0.4355 | If you want to run the add-on on another machine, ... |
| 1573 | 0.4355 | v10.7 NOTE: Netwrix Data Classification and Netwri... |
| 1574 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1575 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1576 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1577 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1578 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1579 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1580 | 0.4354 | The user retrieving data from the Audit Database i... |
| 1581 | 0.4354 | The user writing data to the Audit Database is gra... |
| 1582 | 0.4353 | See Import Audit Data with the Database Importer f... |
| 1583 | 0.4353 | If you want to run the add-on on another machine, ... |
| 1584 | 0.4353 | NetwrixAuditorUserName Current user credentials If... |
| 1585 | 0.4353 | NetwrixAuditorUserName Current user credentials If... |
| 1586 | 0.4352 | Set Applies to to "This folder, subfolders and fil... |
| 1587 | 0.4352 | According to the RESTful model, each operation is ... |
| 1588 | 0.4351 | Netwrix Auditor Certificat e Thumbprint Property. ... |
| 1589 | 0.4351 | v10.7 Duplicates, if any, are written to the Netwr... |
| 1590 | 0.4351 | v10.7 Duplicates, if any, are written to the Netwr... |
| 1591 | 0.4350 | The Audit object access policy must be set to "Suc... |
| 1592 | 0.4349 | -NetwrixAuditorHost 172.28.6.15 -NetwrixAuditorUse... |
| 1593 | 0.4349 | You can add it in NDC console > Settings > Users. ... |
| 1594 | 0.4348 | Follow the steps to delete the Netwrix Auditor for... |
| 1595 | 0.4348 | See the Netwrix Privilege Secure topic for additio... |
| 1596 | 0.4348 | Netwrix Privilege Secure. Starting with version 10... |
| 1597 | 0.4347 | Using the Integration API, the add-on sends the ac... |
| 1598 | 0.4347 | settings.xml Contains parameters for the add-on se... |
| 1599 | 0.4344 | Step 1 – Download the distribution package Netwrix... |
| 1600 | 0.4344 | Assign the Observers role to the user using Cluste... |
| 1601 | 0.4344 | You can enable Auditor to continually enforce the ... |
| 1602 | 0.4343 | Registry key (REG_DWORD type) Description / Value ... |
| 1603 | 0.4343 | It is located in the installation directory: ...\N... |
| 1604 | 0.4342 | Program/script Input "Powershell.exe". Add a path ... |
| 1605 | 0.4342 | ps1 -OutputFolder C:\CEF_Export - NetwrixAuditorHo... |
| 1606 | 0.4341 | The CEF log file will be created in the destinatio... |
| 1607 | 0.4340 | v10.7 Parameter Default value Description Specifie... |
| 1608 | 0.4339 | monitoring plan name,who,where,object type,what,pr... |
| 1609 | 0.4339 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1610 | 0.4339 | Ensure that... Role-Based Access and Delegation to... |
| 1611 | 0.4339 | v10.7 Option Description Events collected from any... |
| 1612 | 0.4338 | All filters are applied using AND logic. See the C... |
| 1613 | 0.4338 | This is optional unless you plan to create index c... |
| 1614 | 0.4338 | Another example: a user creates a new document con... |
| 1615 | 0.4337 | The add-on processes these events into Auditor-com... |
| 1616 | 0.4337 | To learn more about modern authentication, refer t... |
| 1617 | 0.4336 | The user retrieving data from the Audit The Audito... |
| 1618 | 0.4336 | The user retrieving data from the Audit The Audito... |
| 1619 | 0.4335 | Step 5 – Continue retrieving Activity Records. Sen... |
| 1620 | 0.4335 | Ensure that... • The user running the script must ... |
| 1621 | 0.4333 | Tip for reading the table: For example, on the com... |
| 1622 | 0.4331 | Similarly, the add-on also creates the Netwrix_Aud... |
| 1623 | 0.4331 | v10.7 Before you start creating a monitoring plan ... |
| 1624 | 0.4330 | • NOCHECK—Do not check the certificate. Make sure ... |
| 1625 | 0.4330 | You may also want to apply audit settings via GPO ... |
| 1626 | 0.4329 | See the following topics for additional informatio... |
| 1627 | 0.4329 | Group UMHuntGroup = U nified Messaging Hunt Group ... |
| 1628 | 0.4328 | File Description Syntax Name This file defines a l... |
| 1629 | 0.4328 | The add-on and Auditor must be installed on the sa... |
| 1630 | 0.4328 | You can configure your IT Infrastructure for monit... |
| 1631 | 0.4327 | The following step-bystep instructions are for mod... |
| 1632 | 0.4327 | Remember to do the following: v10.7 Prepare a Data... |
| 1633 | 0.4327 | Table 1: Option Description Event Log Select an ev... |
| 1634 | 0.4326 | Table 1: Event log field name Filled in with value... |
| 1635 | 0.4325 | Advanced permissions: ◦ Create files / write data ... |
| 1636 | 0.4325 | NOTE: If you previously used a non-privileged acco... |
| 1637 | 0.4324 | See the Configure Basic Domain Audit Policies or C... |
| 1638 | 0.4323 | By default, the remote Syslog listening server is ... |
| 1639 | 0.4323 | See the File-Based Repository for LongTerm Archive... |
| 1640 | 0.4321 | Starting with version 10.5, Netwrix Auditor provid... |
| 1641 | 0.4319 | The CIM contains a number of standard data models ... |
| 1642 | 0.4318 | timeout Defines the Audit Database connection time... |
| 1643 | 0.4318 | The following inbound Firewall rules must be enabl... |
| 1644 | 0.4317 | For example, if you grant the data collecting acco... |
| 1645 | 0.4314 | If enabled, a Compression Service will be automati... |
| 1646 | 0.4312 | Configuring mailbox access tracking for Exchange 2... |
| 1647 | 0.4311 | OR In the main screen, in the Configuration sectio... |
| 1648 | 0.4310 | The service will collect and process events from t... |
| 1649 | 0.4305 | Starting with version 10.7, you can implement the ... |
| 1650 | 0.4305 | Starting with version 10.7, you can implement the ... |
| 1651 | 0.4305 | If you need to modify them later, run the Netwrix.... |
| 1652 | 0.4304 | Make sure the data source you are going to audit i... |
| 1653 | 0.4304 | Data Collecting Account This is a service account ... |
| 1654 | 0.4303 | following line: .adminDesciption=Admin Screen Desc... |
| 1655 | 0.4302 | Select the event types that you want to be save. I... |
| 1656 | 0.4302 | For Managed Service Providers: 443 TCP Netwrix Aud... |
| 1657 | 0.4301 | In this case, Netwrix Auditor Server will retrieve... |
| 1658 | 0.4300 | If you select to automatically configure audit in ... |
| 1659 | 0.4300 | The custom Long-Term Archive service account can b... |
| 1660 | 0.4299 | v10.7 Step 2 – The level value is set in the LogLe... |
| 1661 | 0.4298 | • The user running the script must be a member of ... |
| 1662 | 0.4297 | The best practice is to review user profile after ... |
| 1663 | 0.4297 | See the Notifications Page topic for additional in... |
| 1664 | 0.4297 | Step 4 – Hit Enter. Depending on the number of Act... |
| 1665 | 0.4296 | See the Role-Based Access and Delegation topic for... |
| 1666 | 0.4296 | The addon must always run locally, on the computer... |
| 1667 | 0.4294 | To store data from the data sources included in th... |
| 1668 | 0.4294 | Optionally, you can select Download to edit the ma... |
| 1669 | 0.4293 | Alternatively, you can grant the Global administra... |
| 1670 | 0.4293 | Step 5 – Navigate to File → Connect Network Regist... |
| 1671 | 0.4291 | And UDP port (for, example 514) is used for sendin... |
| 1672 | 0.4291 | timeout Defines the Audit Database connection time... |
| 1673 | 0.4291 | Object Access Audit Detailed File Share "Failure" ... |
| 1674 | 0.4290 | For example: -file "C:\Addons\Netwrix_Auditor_Audi... |
| 1675 | 0.4289 | Manually – Native audit settings must be adjusted ... |
| 1676 | 0.4287 | HEALTH STATUS Opens the Health Status dashboard, w... |
| 1677 | 0.4287 | Continuation Mark POST /netwrix/api/v1/ activity_r... |
| 1678 | 0.4286 | You can use this file to track possible duplicates... |
| 1679 | 0.4286 | SMB Azure file shares are accessible from Windows,... |
| 1680 | 0.4285 | Alternatively, you can install Auditor client usin... |
| 1681 | 0.4284 | v10.7 You can use a single account to collect audi... |
| 1682 | 0.4284 | Example: For: PROD-SQL-01-AG1 SQL Server Monitorin... |
| 1683 | 0.4283 | v10.7 The user writing data to the Audit Database ... |
| 1684 | 0.4282 | The product has the following limitations dependin... |
| 1685 | 0.4282 | Run the Command Prompt as Administrator. Execute t... |
| 1686 | 0.4282 | Auditor can monitor for operations with MS Teams e... |
| 1687 | 0.4281 | The account must be a member of the BUILTIN\Admini... |
| 1688 | 0.4281 | The add-on works in collaboration with Netwrix Aud... |
| 1689 | 0.4280 | If you want the add-on to use another account to c... |
| 1690 | 0.4277 | Table 1: Option Description Accept List Address Sp... |
| 1691 | 0.4276 | For example: Create ONTAPI role: security login ro... |
| 1692 | 0.4275 | Failed change attempts The Auditing Entry below sh... |
| 1693 | 0.4275 | You can select Everyone (or another u ser-defined ... |
| 1694 | 0.4274 | Duplicates, if any, are written to the Netwrix_Aud... |
| 1695 | 0.4273 | Using the Integration API, the add-on sends the ac... |
| 1696 | 0.4272 | To use the account currently logged in, leave this... |
| 1697 | 0.4271 | user activity or state-in-time data. Table 1: Opti... |
| 1698 | 0.4271 | Duplicates, if any, are written to the Netwrix_Aud... |
| 1699 | 0.4271 | As a next step, click Add item to specify an objec... |
| 1700 | 0.4270 | Working Folder The working folder is a file-based ... |
| 1701 | 0.4270 | C:\Add-ons\Netwrix_Auditor_Addon_for_HPE_ ArcSight... |
| 1702 | 0.4268 | In this case, the product still collects stat-in-t... |
| 1703 | 0.4267 | Your current audit settings will be checked on eac... |
| 1704 | 0.4266 | See the Role-Based Access and Delegation topic for... |
| 1705 | 0.4266 | NetwrixAuditorUserName Current user credentials Un... |
| 1706 | 0.4262 | If you want to audit Dell VNX/VNXe, select Adjust ... |
| 1707 | 0.4261 | You will also need to configure Exchange Administr... |
| 1708 | 0.4260 | v10.7 Step 1 – Go to Configuration > Monitoring pl... |
| 1709 | 0.4259 | v10.7 Then follow the steps in the Monitoring Plan... |
| 1710 | 0.4259 | See the Role-Based Access and Delegation topic for... |
| 1711 | 0.4258 | You can add several IDs separated by comma. Event ... |
| 1712 | 0.4257 | You can add several IDs separated by comma. Select... |
| 1713 | 0.4257 | list/ document.docx. SQL Server NOTE: Prior to con... |
| 1714 | 0.4255 | To change the add-on logging level, use the LogLev... |
| 1715 | 0.4255 | At least the first script run should be performed ... |
| 1716 | 0.4251 | Add a path to the add-on in double quotes and spec... |
| 1717 | 0.4250 | 1=yes 0=no (default) Parameters within SourceList ... |
| 1718 | 0.4250 | Depending on the network traffic compression setti... |
| 1719 | 0.4250 | Step 5 – Click on the arrow button next to any of ... |
| 1720 | 0.4250 | The credentials are case sensitive. A custom accou... |
| 1721 | 0.4249 | NOTE: On the Netwrix Auditor Server, the gMSA acco... |
| 1722 | 0.4247 | Synology Auditor supports monitoring the following... |
| 1723 | 0.4244 | When the port is set as desired, click Next. NOTE:... |
| 1724 | 0.4243 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 1725 | 0.4241 | See the Role-Based Access and Delegation topic for... |
| 1726 | 0.4241 | See the Role-Based Access and Delegation topic for... |
| 1727 | 0.4241 | As soon as the item is added, to the monitoring pl... |
| 1728 | 0.4240 | Windows File Server. Table 1: Component Version Ne... |
| 1729 | 0.4239 | ◦◦ Upload to a file share—Select this option to sa... |
| 1730 | 0.4239 | Applicable for: File Servers SharePoint SharePoint... |
| 1731 | 0.4239 | For more information on this deployment option, re... |
| 1732 | 0.4239 | Step 3 – Move the selected snapshots to the Snapsh... |
| 1733 | 0.4237 | Maximum number of Audit Records ARsNumberAtTime th... |
| 1734 | 0.4237 | If you plan to enable this option, make sure the a... |
| 1735 | 0.4235 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 1736 | 0.4234 | For bigger SharePoint farms, consider up to 10 min... |
| 1737 | 0.4233 | Table 1: Element Mandatory Datatype Description Da... |
| 1738 | 0.4232 | Click Next. Step 3 – Click Run and close the windo... |
| 1739 | 0.4232 | See the Integration API topic for additional infor... |
| 1740 | 0.4232 | Netwrix Privilege Secure is ready to use as an acc... |
| 1741 | 0.4232 | The add-on enriches your SIEM data with actionable... |
| 1742 | 0.4230 | NOTE: Make sure that the AD Computer account for t... |
| 1743 | 0.4229 | Netwrix Privilege Secure is ready to use as an acc... |
| 1744 | 0.4226 | Specify actions for monitoring Specify actions you... |
| 1745 | 0.4222 | Specify port and protocol for incoming connections... |
| 1746 | 0.4222 | Step 2 – In the Tenant information locate the Prim... |
| 1747 | 0.4222 | Step 2 – In the Tenant information locate the Prim... |
| 1748 | 0.4222 | If you need a data source that is not listed on th... |
| 1749 | 0.4221 | v10.7 Step 1 – On the computer where Netwrix Audit... |
| 1750 | 0.4220 | Recipients RECOMMENDED: click Send Test Email. The... |
| 1751 | 0.4217 | Format Select None. Click Submit. The new server i... |
| 1752 | 0.4217 | If not yet existing on the specified SQL server in... |
| 1753 | 0.4216 | Collect data for state-in-time reports Configure A... |
| 1754 | 0.4215 | Facility Select desired facility. v10.7 55.. Under... |
| 1755 | 0.4213 | For example: Table 1: Event ID Description 22 Pass... |
| 1756 | 0.4211 | This database is always created but is involved in... |
| 1757 | 0.4210 | Table 1: Issue Reason and solution Monitoring Plan... |
| 1758 | 0.4210 | In the same domain No restrictions In two-way trus... |
| 1759 | 0.4209 | It instructs Netwrix Auditor to Not in group Domai... |
| 1760 | 0.4209 | You can use a single account to collect audit data... |
| 1761 | 0.4208 | In a separate Advanced Security Settings for <Shar... |
| 1762 | 0.4208 | It might cause performance issues on the medium an... |
| 1763 | 0.4208 | OR ◦◦ Modern authentication has ever been selected... |
| 1764 | 0.4203 | See the Monitoring Planstopic for additional infor... |
| 1765 | 0.4203 | Alternatively, you can grant the Global administra... |
| 1766 | 0.4201 | Careful review of successful and failed logons fro... |
| 1767 | 0.4201 | Get the most from your SIEM investment — To maximi... |
| 1768 | 0.4201 | For example: http:// sharepointsrv:3333/ omitscsto... |
| 1769 | 0.4198 | When finished, run the gpupdate /force command to ... |
| 1770 | 0.4197 | See the Microsoft Turn auditing on or off article ... |
| 1771 | 0.4196 | Password field can be empty. Starting with version... |
| 1772 | 0.4196 | Step 5 – In case some computers are still present ... |
| 1773 | 0.4195 | Step 2 – Select the log you need. Step 3 – Edit Sp... |
| 1774 | 0.4195 | Alternatively, you can grant the Global administra... |
| 1775 | 0.4195 | The filters may vary slightly depending on the aud... |
| 1776 | 0.4192 | The DetailList element is Table 1: Format Schema d... |
| 1777 | 0.4192 | The appearance of the license will be reflected in... |
| 1778 | 0.4191 | State — as set in the database properties at snaps... |
| 1779 | 0.4191 | In the next menu, select Paste all certificates in... |
| 1780 | 0.4190 | For Managed Service Providers: Netwrix Auditor Net... |
| 1781 | 0.4189 | Configure ONTAPI\RESTAPI Web Access Netwrix Audito... |
| 1782 | 0.4189 | Currently, not every detail about permission and a... |
| 1783 | 0.4187 | The Detail field may contain sub-fields with value... |
| 1784 | 0.4186 | Step 2 – Navigate to the Groups node and locate th... |
| 1785 | 0.4186 | Unless specified, the script runs with the current... |
| 1786 | 0.4186 | Step 2 – Fine-tune data source settings, if necess... |
| 1787 | 0.4185 | <domain\user> For example, to exclude changes made... |
| 1788 | 0.4184 | Success HTTP/1.1 200 OK Server: Microsoft-HTTPAPI/... |
| 1789 | 0.4184 | Actions reported by Auditor vary depending on the ... |
| 1790 | 0.4182 | See the Configure SMTP Server Settings topic for i... |
| 1791 | 0.4182 | Password Enter a password. NOTE: If you want to us... |
| 1792 | 0.4181 | Currently, you cannot assign or create tags on thi... |
| 1793 | 0.4180 | These requirements will add up to the requirements... |
| 1794 | 0.4176 | For example, you can run the add-on on the compute... |
| 1795 | 0.4176 | Besides, Netwrix Auditor Password Expiration Notif... |
| 1796 | 0.4174 | Make sure the volume you specified is mounted on S... |
| 1797 | 0.4173 | This account requires administrative rights. Then ... |
| 1798 | 0.4173 | * — these actions are reported for SharePoint Onli... |
| 1799 | 0.4171 | See the Integration API topic for additional infor... |
| 1800 | 0.4169 | See the Network Traffic Compression topic for addi... |
| 1801 | 0.4167 | • Group Policy On the computer where Auditor Serve... |
| 1802 | 0.4166 | The dashboard comprises a set of widgets that disp... |
| 1803 | 0.4165 | • The servers within the farm are located in diffe... |
| 1804 | 0.4165 | This is a mandatory parameter. v10.7 Parameter Def... |
| 1805 | 0.4162 | You can also create a subscription to any report y... |
| 1806 | 0.4161 | Name For example: *OU=C,OU=B,OU=A* v10.7 NOTE: Tip... |
| 1807 | 0.4160 | v10.7 Option Description Select this checkbox if y... |
| 1808 | 0.4159 | -ArcSightHost 172.28.6.18 C:\Add-ons\Netwrix_Audit... |
| 1809 | 0.4159 | The newly created data source will appear in the D... |
| 1810 | 0.4159 | Allow outbound connections to the remote ports on ... |
| 1811 | 0.4158 | See RoleBased Access and Delegation. Alternatively... |
| 1812 | 0.4158 | Data is retrieved from a remote Auditor repository... |
| 1813 | 0.4158 | Complete the process After you click Apply require... |
| 1814 | 0.4156 | • 1—Full installation v10.7 where %Temp% can be re... |
| 1815 | 0.4154 | v10.7 Step 7 – Click Run and close the window. The... |
| 1816 | 0.4153 | on the fi rst server you have set up in the farm: ... |
| 1817 | 0.4150 | See the Requirements for SQL Server to Store Audit... |
| 1818 | 0.4149 | Currently, auditing is available for SMB shares on... |
| 1819 | 0.4148 | Effective grant —the effective set of permissions ... |
| 1820 | 0.4148 | Review your data source settings and click Add to ... |
| 1821 | 0.4148 | Review your data source settings and click Add to ... |
| 1822 | 0.4148 | Review your data source settings and click Add to ... |
| 1823 | 0.4147 | NetwrixAuditorCertificateThumbpr int NOCHECK Audit... |
| 1824 | 0.4147 | Automate Add-On Execution To ensure you feed the m... |
| 1825 | 0.4147 | Active Directory Ports Review a full list of proto... |
| 1826 | 0.4146 | If an ESXi host was specified as a monitored item ... |
| 1827 | 0.4144 | JSON: [0x00007FFDCC06BBC8,0x00007FFDB99EF4BA; 0x00... |
| 1828 | 0.4144 | Then s/he adds items to the monitoring plan – thes... |
| 1829 | 0.4143 | The credentials are case sensitive. A custom accou... |
| 1830 | 0.4142 | Since Netwrix Auditor shows only the top 2,000 ano... |
| 1831 | 0.4141 | Move the selected snapshots to the Snapshots avail... |
| 1832 | 0.4141 | The Syslog daemon must be configured to redirect e... |
| 1833 | 0.4141 | C:\Add-ons\Netwrix_Auditor_Addon_for_ AlienVault_U... |
| 1834 | 0.4140 | Step 1 – In the audited SharePoint farm, navigate ... |
| 1835 | 0.4138 | The user writing data to the Audit Database is gra... |
| 1836 | 0.4138 | The user writing data to the Audit Database is gra... |
| 1837 | 0.4137 | Table 1: Policy Subnode Policy Name Audit Events A... |
| 1838 | 0.4136 | ◦◦ The Advanced audit policy settings can be confi... |
| 1839 | 0.4136 | NOTE: If you want to get only state-in-time snapsh... |
| 1840 | 0.4134 | To modify conditions for the selected filters, mak... |
| 1841 | 0.4134 | Refer to the Netwrix Privilege Secure documentatio... |
| 1842 | 0.4133 | Unless specified, the script runs with the current... |
| 1843 | 0.4132 | or generating reports, or I am sure that some data... |
| 1844 | 0.4130 | Step 4 – Configure Audit Settings for CIFS File Sh... |
| 1845 | 0.4129 | The URL for the Access Reviews Console is now acce... |
| 1846 | 0.4129 | Step 5 – On the Destination Folder step, specify t... |
| 1847 | 0.4127 | See the Configure Security Event Log Maximum Size ... |
| 1848 | 0.4126 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1849 | 0.4126 | • Services—Enables auditing of started/stopped ser... |
| 1850 | 0.4125 | Event level Select level of the events that you wa... |
| 1851 | 0.4124 | v10.7 Reported data The report has a summary secti... |
| 1852 | 0.4124 | A Security Officer wants to monitor a file share, ... |
| 1853 | 0.4121 | NetwrixAuditorUserName Current user credentials Un... |
| 1854 | 0.4121 | Right-click it and select Properties from the pop-... |
| 1855 | 0.4121 | Step 8 – Complete the following fields: Option Des... |
| 1856 | 0.4120 | To disable Activity Summary Emails, you need to di... |
| 1857 | 0.4120 | Step 2 – Delete the HKEY_LOCAL_MACHINE\SYSTEM\Curr... |
| 1858 | 0.4120 | EventData is filled in with data from the Activity... |
| 1859 | 0.4118 | This option is recommended for organizations that ... |
| 1860 | 0.4116 | See the Considerations for Oracle Database 11g top... |
| 1861 | 0.4115 | The credentials are case sensitive. If using a gro... |
| 1862 | 0.4115 | What column. For example, if you only want to moni... |
| 1863 | 0.4114 | See RoleBased Access and Delegation. Alternatively... |
| 1864 | 0.4112 | State-in-time configuration snapshots are also use... |
| 1865 | 0.4110 | It may include the data source type (e.g. Exchange... |
| 1866 | 0.4110 | Step 4 – Provide retention settings and access cre... |
| 1867 | 0.4109 | ): No special configuration required to audit RMAN... |
| 1868 | 0.4108 | Starting with version 10.7, you can implement the ... |
| 1869 | 0.4107 | Special Considerations The originally released Net... |
| 1870 | 0.4107 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1871 | 0.4105 | To collect data from Windows Failover Cluster, net... |
| 1872 | 0.4105 | 44.. Configure the following audit policies. Table... |
| 1873 | 0.4100 | Auditor Administrators Global administrator Audito... |
| 1874 | 0.4099 | See Add Items for Monitoringfor more information. ... |
| 1875 | 0.4098 | As a next step, click Add item to specify an objec... |
| 1876 | 0.4098 | Partners and MSPs who are logged into the Netwrix ... |
| 1877 | 0.4094 | References details. Detail sub-elements (provided ... |
| 1878 | 0.4093 | To specify a non-default port, provide a server na... |
| 1879 | 0.4093 | To specify a non-default port, provide a server na... |
| 1880 | 0.4092 | Depending on Error the error code, the response bo... |
| 1881 | 0.4090 | Automate Add-On Execution To ensure you feed the m... |
| 1882 | 0.4090 | Automate Add-On Execution To ensure you feed the m... |
| 1883 | 0.4090 | Adding the widlcard (*) to omitpathlist.txt will n... |
| 1884 | 0.4089 | For example, -76. v10.7 Option Description Select ... |
| 1885 | 0.4088 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 1886 | 0.4088 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 1887 | 0.4088 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 1888 | 0.4087 | This will facilitate operations tracking and possi... |
| 1889 | 0.4085 | User name This account must be granted the databas... |
| 1890 | 0.4084 | Starting with version 10.7, you can implement the ... |
| 1891 | 0.4082 | At the end of the first run, the timestamp will be... |
| 1892 | 0.4082 | Collected via MS Graph on endpoint /devices All se... |
| 1893 | 0.4082 | If you want to generate reports based on differen ... |
| 1894 | 0.4081 | Otherwise, specify custom path to logo file. Defau... |
| 1895 | 0.4080 | The Activity Records have the format similar to th... |
| 1896 | 0.4079 | Enter: Application ID; Application secret. ◦◦ See ... |
| 1897 | 0.4079 | Enter: Application ID; Application secret. ◦◦ See ... |
| 1898 | 0.4078 | RuleFileList cyberark-v2.xml You can specify sever... |
| 1899 | 0.4077 | Step 2 – Navigate to Security Settings > Local Pol... |
| 1900 | 0.4076 | v10.7 Parameter Default value Description Unless s... |
| 1901 | 0.4075 | -NetwrixAuditorHost 172.28.6.15 C:\Add-ons\Netwrix... |
| 1902 | 0.4075 | v10.7 Step 6 – In the dialog that opens, locate Ne... |
| 1903 | 0.4074 | .Net Framework 4.7.2 and above is installed. Revie... |
| 1904 | 0.4074 | Configuration parameters to specify in settings.xm... |
| 1905 | 0.4074 | To use the account currently logged in, leave this... |
| 1906 | 0.4073 | After creating a task, wait for the next scheduled... |
| 1907 | 0.4072 | Collect activity data only 1. For initial connecti... |
| 1908 | 0.4070 | If you want the add-on to use another account to c... |
| 1909 | 0.4068 | How to Include/Exclude Applications To create a li... |
| 1910 | 0.4065 | C:\Add-ons\Netwrix_Auditor_Addon_for_HPE_ ArcSight... |
| 1911 | 0.4065 | The credentials are case sensitive. A custom accou... |
| 1912 | 0.4064 | For the User Password Changes report to function p... |
| 1913 | 0.4064 | It may include the data source type (e.g. Exchange... |
| 1914 | 0.4062 | Possible parameter values: True — fill in the Even... |
| 1915 | 0.4061 | Refer to the following sections below for manual i... |
| 1916 | 0.4055 | With that automated flow, you can use Splunk Enter... |
| 1917 | 0.4055 | See the following topics for additional informatio... |
| 1918 | 0.4054 | You may keep the existing audit log retention prov... |
| 1919 | 0.4054 | Review the table below for more information. Step ... |
| 1920 | 0.4054 | Configurator to make sure that the monitoring plan... |
| 1921 | 0.4053 | Table 1: File name Description HVARunner.exe Main ... |
| 1922 | 0.4053 | <Address>172.28.4.15</Address> <Address>172.28.3.1... |
| 1923 | 0.4053 | If you want to generate a report to assess your sy... |
| 1924 | 0.4053 | Step 4 – Click Apply. Table 1: Port Protocol Sourc... |
| 1925 | 0.4052 | Table 2: Parameter Default value Description Event... |
| 1926 | 0.4052 | See the Audit Configuration Assistant topic for ad... |
| 1927 | 0.4051 | Group Policy. See the Use Netwrix Privilege Secure... |
| 1928 | 0.4051 | Whenever the alert is triggered, the add-on uses t... |
| 1929 | 0.4050 | XML: XML: <ActivityRecord><Action>Successful L ogo... |
| 1930 | 0.4049 | You can use * for cmdlets and their parameters. Li... |
| 1931 | 0.4047 | See the Manage Data Sources topic for additional i... |
| 1932 | 0.4047 | Navigate to Reports and select one of the followin... |
| 1933 | 0.4046 | You can put a wildcard (*) in the omitpathlist.txt... |
| 1934 | 0.4046 | Open a web browser and type the Report Manager URL... |
| 1935 | 0.4046 | Netwrix recommends assigning a unique identificato... |
| 1936 | 0.4045 | Table 1: Option Description Do not select the chec... |
| 1937 | 0.4045 | For other dist ributions, deployment of the rsyslo... |
| 1938 | 0.4043 | Step 3 – Specify a data source. Step 4 – Configure... |
| 1939 | 0.4043 | Allow outbound connections from the dynamic (1024 ... |
| 1940 | 0.4042 | Table 2: Format Example XML <?xml version="1.0" en... |
| 1941 | 0.4040 | • .NET Framework 4.5 or later must be installed. Q... |
| 1942 | 0.4039 | If an object has been moved between file shares, t... |
| 1943 | 0.4039 | v10.7 For example, if you selected the 'Enable Sta... |
| 1944 | 0.4037 | Rolebased access system ensures that only relevant... |
| 1945 | 0.4036 | (Unlike that, without network traffic compression ... |
| 1946 | 0.4035 | NetwrixAuditorPassword Current user credentials Un... |
| 1947 | 0.4034 | .Net Framework 4.7.2 and above is installed. The c... |
| 1948 | 0.4034 | Maintenance and Troubleshooting If you cannot see ... |
| 1949 | 0.4033 | MS Teams monitoring plan has been added to Auditor... |
| 1950 | 0.4031 | It also illustrates the customization process with... |
| 1951 | 0.4028 | For detailed information, review the Planning the ... |
| 1952 | 0.4028 | C:\Add-ons\Netwrix_Auditor_Addon_for_IBM_ QRadar.p... |
| 1953 | 0.4028 | Wait until the tool has finished restoring the sel... |
| 1954 | 0.4028 | Auditor Plan Item Unless specified, data is not as... |
| 1955 | 0.4027 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1956 | 0.4027 | Default prefix is NA, for example:NA Windows Serve... |
| 1957 | 0.4025 | Table 1: Successful changes 1 Failed change attemp... |
| 1958 | 0.4024 | For that, follow the procedure below. If you enabl... |
| 1959 | 0.4024 | Then specify how you want the report to be deliver... |
| 1960 | 0.4024 | Then specify how you want the report to be deliver... |
| 1961 | 0.4024 | Then specify how you want the report to be deliver... |
| 1962 | 0.4024 | Then specify how you want the report to be deliver... |
| 1963 | 0.4024 | Then specify how you want the report to be deliver... |
| 1964 | 0.4024 | Then specify how you want the report to be deliver... |
| 1965 | 0.4024 | Monitored Object Types, Actions, and Attributes Ne... |
| 1966 | 0.4023 | These features allow enabling Windows Media Player... |
| 1967 | 0.4021 | monitoring plan name,server name,error text For ex... |
| 1968 | 0.4020 | It defines mapping between the Activity Records an... |
| 1969 | 0.4020 | Adding the widlcard (*) to omitpathlist.txt will n... |
| 1970 | 0.4019 | RECOMMENDED: Netwrix recommends reviewing your cur... |
| 1971 | 0.4019 | This ensures that dedicated specialists have acces... |
| 1972 | 0.4019 | Alternatively, you can grant the Global administra... |
| 1973 | 0.4019 | Alternatively, you can grant the Global administra... |
| 1974 | 0.4018 | ◦◦ Target Nutanix File Server must be located in t... |
| 1975 | 0.4017 | Note that these actions are system, not user-effec... |
| 1976 | 0.4016 | Usage example Database administrators in the Corp ... |
| 1977 | 0.4015 | NetwrixAuditorCertificateThumbpr int NOCHECK Netwr... |
| 1978 | 0.4015 | Step 4 – Enable auditing: 11.. On the Volumes tab,... |
| 1979 | 0.4013 | In Auditor settings, go to the Integrations sectio... |
| 1980 | 0.4013 | Table 1: Version Edition SQl Server 2022 • Standar... |
| 1981 | 0.4012 | { "resourceAppId": "00000003-0000-0000-c000-000000... |
| 1982 | 0.4012 | Configuration Activity Records to Event Log Add-on... |
| 1983 | 0.4012 | For example: mydomain\user1. Consider the followin... |
| 1984 | 0.4010 | ◦ Download the appropriate package from Oracle web... |
| 1985 | 0.4010 | For removable storages, the When value reports act... |
| 1986 | 0.4008 | Activity Records are exported to a local folder. C... |
| 1987 | 0.4006 | You can configure your IT Infrastructure for monit... |
| 1988 | 0.4006 | Refer to the Netwrix Privilege Secure documentatio... |
| 1989 | 0.4006 | The machine where the Add-On will be installed The... |
| 1990 | 0.4005 | Uninstall Compression and Core Services Perform th... |
| 1991 | 0.4005 | Possible parameter values: True — fill in the Even... |
| 1992 | 0.4005 | Possible parameter values: True — fill in the Even... |
| 1993 | 0.4005 | Refer to the Permissions for Active Directory A ud... |
| 1994 | 0.4004 | If you want the add-on to use another account to c... |
| 1995 | 0.4000 | Step 2 – Start Windows PowerShell and specify a pa... |
| 1996 | 0.4000 | In addition to the restrictions for a monitoring p... |
| 1997 | 0.3997 | In this case, Netwrix Auditor Server will retrieve... |
| 1998 | 0.3997 | The user who runs the script is granted the db_own... |
| 1999 | 0.3996 | When the free disk space is less than 3 GB, the Ne... |
| 2000 | 0.3995 | See the Configure Dell Isilon/PowerScale Cluster i... |
| 2001 | 0.3995 | Local TCP Port 9004 is opened for inbound connecti... |
| 2002 | 0.3993 | Time zone — time zone where Netwrix Auditor server... |
| 2003 | 0.3993 | When you add the first item (Nutanix SMB shares) t... |
| 2004 | 0.3991 | ShortTermFolder ShortTerm Specify path to the shor... |
| 2005 | 0.3991 | Only the latest snapshot is available for reportin... |
| 2006 | 0.3991 | All fi lters required to store events for all avai... |
| 2007 | 0.3990 | v10.7 New Features Integration with Netwrix Privil... |
| 2008 | 0.3989 | Password – Provide a password for that account Ena... |
| 2009 | 0.3989 | For NetApp Clustered Data ONTAP 8 and ONTAP 9, onl... |
| 2010 | 0.3989 | Leave blank if you use Windows Authentication. SQL... |
| 2011 | 0.3988 | RECOMMENDED: click Send Test Email. The system wil... |
| 2012 | 0.3986 | Step 6 – Choose modern authentication. Step 7 – En... |
| 2013 | 0.3983 | See the Configure Dell Isilon/PowerScale Cluster i... |
| 2014 | 0.3982 | ◦◦ To use this option for NetApp Clustered Data ON... |
| 2015 | 0.3982 | Windows Server Ports Review a full list of protoco... |
| 2016 | 0.3981 | Write to/Don't write to Select the location to wri... |
| 2017 | 0.3981 | /netwrix/api/v1/ GET — activity_records/enum Retri... |
| 2018 | 0.3979 | To audit users and groups, vCenter 6.5 and above r... |
| 2019 | 0.3979 | The changes include creation, modifica tion, delet... |
| 2020 | 0.3976 | VMware Servers Auditor supports monitoring the fol... |
| 2021 | 0.3976 | The credentials are case sensitive. If using a gro... |
| 2022 | 0.3976 | v10.7 File Description Syntax For example, if you ... |
| 2023 | 0.3975 | Within timeframe: • Today • Yesterday • LastSevenD... |
| 2024 | 0.3975 | Most parameters are optional, the script uses the ... |
| 2025 | 0.3974 | Typically, data collected from the certain data so... |
| 2026 | 0.3973 | Troubleshooting The following are several troubles... |
| 2027 | 0.3972 | Add a path to the add-on in double quotes and spec... |
| 2028 | 0.3969 | v10.7 Option Description Do not select the checkbo... |
| 2029 | 0.3967 | On the computer where Auditor Server is installed:... |
| 2030 | 0.3966 | Enter: Application ID; Application secret. ◦◦ See ... |
| 2031 | 0.3966 | Or simply drag and drop the add-on file in the con... |
| 2032 | 0.3966 | If you want to run the add-on on another machine, ... |
| 2033 | 0.3965 | See the Fine-tune Monitoring Scope for a dditional... |
| 2034 | 0.3965 | v10.7 To... Follow the steps... Use the Filter by ... |
| 2035 | 0.3964 | If you select to automatically configure audit in ... |
| 2036 | 0.3964 | These group Managed Service Accounts should meet t... |
| 2037 | 0.3964 | Default is Priority 3 — Normal Response. Table 2: ... |
| 2038 | 0.3963 | Create a special user account with permissions to ... |
| 2039 | 0.3963 | Step 1 – On the computer where Auditor is installe... |
| 2040 | 0.3962 | Step 2 – Select Settings > Email and Alerts > Sysl... |
| 2041 | 0.3962 | Consider the following: • Use NetBIOS format for d... |
| 2042 | 0.3959 | Adjust Security Event Log Size and Retention Defin... |
| 2043 | 0.3959 | 44.. Configure the following audit policies. Polic... |
| 2044 | 0.3959 | For example: mydomain\user1. Consider the followin... |
| 2045 | 0.3958 | If you select to automatically configure audit in ... |
| 2046 | 0.3958 | Otherwise, the add-on will not be v10.7 Parameter ... |
| 2047 | 0.3956 | This capability is supported for the following rep... |
| 2048 | 0.3956 | Manually – Native audit settings must be adjusted ... |
| 2049 | 0.3955 | You can create as many shortcuts with different pa... |
| 2050 | 0.3955 | See the Adjust Security Event Log Size and Retenti... |
| 2051 | 0.3955 | Name and Location Select a name for the new virtua... |
| 2052 | 0.3953 | You can enable Auditor to continually enforce the ... |
| 2053 | 0.3953 | This policy should be configured manually since Au... |
| 2054 | 0.3952 | Step 5 – Make sure the Do not overwrite events (Cl... |
| 2055 | 0.3951 | In addition to the restrictions for a monitoring p... |
| 2056 | 0.3951 | v10.7 The "Create a monitoring plan" link prompts ... |
| 2057 | 0.3950 | If the same account is being used for multiple pur... |
| 2058 | 0.3949 | NOTE: The new destination folder will be ...\Netwr... |
| 2059 | 0.3947 | Step 5 – Review the account configuration scope an... |
| 2060 | 0.3947 | Step 6 – Choose modern authentication. Step 7 – En... |
| 2061 | 0.3947 | Unless specified, data is not associated with a s ... |
| 2062 | 0.3945 | NOTE: You might want to apply a filter to narrow d... |
| 2063 | 0.3941 | Depending on your auditing requirements, you may n... |
| 2064 | 0.3940 | QueueSizeLimit 100 Specifies the maximum number of... |
| 2065 | 0.3939 | Any additional role assignments will not be necess... |
| 2066 | 0.3939 | Any additional role assignments will not be necess... |
| 2067 | 0.3939 | In the Maximum security log size Properties dialog... |
| 2068 | 0.3934 | fs_create_hard_link A new hard link was created. f... |
| 2069 | 0.3934 | To add users to the list, click Add and provide us... |
| 2070 | 0.3932 | Troubleshoot SharePoint Auditing Problem Descripti... |
| 2071 | 0.3931 | v10.7 You can configure your IT Infrastructure for... |
| 2072 | 0.3930 | The output Activity Records may contain the follow... |
| 2073 | 0.3930 | Auditor Endpoint Assumes that the add-on runs on t... |
| 2074 | 0.3930 | What Specify an object name (e.g., Policy) to find... |
| 2075 | 0.3929 | Step 3 – Configure Audit Object Access Policy. Set... |
| 2076 | 0.3928 | For example: http:// webApplication1:3333/ SharePo... |
| 2077 | 0.3927 | The response body should contain the list of serve... |
| 2078 | 0.3926 | The Auditor server side • Auditor version is 10.0 ... |
| 2079 | 0.3925 | First, you should decide on the objects and action... |
| 2080 | 0.3924 | Step 4 – The new secret will be displayed in the l... |
| 2081 | 0.3923 | The status is 200 OK. For XML, a response body con... |
| 2082 | 0.3920 | See the Health Status Dashboard topic for addition... |
| 2083 | 0.3918 | Configure Dell Isilon/PowerScale Cluster in Normal... |
| 2084 | 0.3916 | See the Add Account to the Organization Management... |
| 2085 | 0.3916 | Take action Click the Details link to examine the ... |
| 2086 | 0.3916 | If you select to automatically configure audit in ... |
| 2087 | 0.3915 | For example, you can run the add-on on the compute... |
| 2088 | 0.3915 | For example, you can run the add-on on the compute... |
| 2089 | 0.3915 | This topic focuses on the AlienVault USM SIEM solu... |
| 2090 | 0.3915 | This topic focuses on the AlienVault USM SIEM solu... |
| 2091 | 0.3914 | Step 4 – In the CN=Configuration, DC=<name>, DC=<n... |
| 2092 | 0.3913 | See the topics on the monitored items for details.... |
| 2093 | 0.3913 | Currently, auditing is available for SMB shares on... |
| 2094 | 0.3912 | Step 2 – Select the snapshots that you want to imp... |
| 2095 | 0.3912 | In addition to the restrictions for a monitoring p... |
| 2096 | 0.3911 | Netwrix recommends installing the latest available... |
| 2097 | 0.3908 | 66.. Run the following command to update group pol... |
| 2098 | 0.3908 | Installation of Netwrix Auditor and SQL Server on ... |
| 2099 | 0.3907 | Step 4 – Specify syslog server parameters: Paramet... |
| 2100 | 0.3907 | If any conflicts are detected with your current se... |
| 2101 | 0.3907 | This account must have at least Read Only role on ... |
| 2102 | 0.3905 | Where Specify a resource name (e.g., Enterprise) t... |
| 2103 | 0.3904 | Companies leverage these policies to empower users... |
| 2104 | 0.3903 | Select this option if you want to use other creden... |
| 2105 | 0.3901 | As a next step, click Add item to specify an objec... |
| 2106 | 0.3900 | Create a special user account with permissions to ... |
| 2107 | 0.3899 | Windows PowerShell ISE will start. Step 3 – Run th... |
| 2108 | 0.3899 | The retention method must be set to “Overwrite eve... |
| 2109 | 0.3899 | When configuring audit manually, you see the follo... |
| 2110 | 0.3898 | I want to suppress errors from this server by excl... |
| 2111 | 0.3897 | If not set, <not set> is reported. Total objects c... |
| 2112 | 0.3897 | Write event descriptions to Audit Database Select ... |
| 2113 | 0.3896 | To ensure proper operation, the VM template must b... |
| 2114 | 0.3896 | Make sure that you specified the same names as in ... |
| 2115 | 0.3896 | Make sure that you specified the same names as in ... |
| 2116 | 0.3896 | Make sure that you specified the same names as in ... |
| 2117 | 0.3896 | See the Use Group Managed Service Account (gMSA) t... |
| 2118 | 0.3896 | See the Use Group Managed Service Account (gMSA) t... |
| 2119 | 0.3896 | See the Use Group Managed Service Account (gMSA) t... |
| 2120 | 0.3896 | See the Use Group Managed Service Account (gMSA) t... |
| 2121 | 0.3896 | See the Use Group Managed Service Account (gMSA) t... |
| 2122 | 0.3895 | Unless specified, the add-on runs with the current... |
| 2123 | 0.3894 | To exclude a change from reports, search results a... |
| 2124 | 0.3894 | For initial connection to SharePoint Online, initi... |
| 2125 | 0.3894 | In addition to the restrictions for a monitoring p... |
| 2126 | 0.3892 | If you want the add-on to use another account to c... |
| 2127 | 0.3892 | Step 4 – The new secret will be displayed in the l... |
| 2128 | 0.3892 | See the File Servers topic for additional informat... |
| 2129 | 0.3892 | EventData is filled in with data from the Activity... |
| 2130 | 0.3891 | This URL is used to get OneFS web administration i... |
| 2131 | 0.3891 | Table 1: Netwrix Auditor Per 1 Million Files Per 5... |
| 2132 | 0.3891 | Any of them are required if you want to get the "W... |
| 2133 | 0.3889 | NetwrixAuditorPassword – Provide a password for th... |
| 2134 | 0.3888 | Step 5 – Run the installation package. Step 6 – Ac... |
| 2135 | 0.3887 | Table 1: Port Protocol Source Target Purpose 9004 ... |
| 2136 | 0.3887 | XML <?xml version="1.0" encoding="UTF-8" ?> <Activ... |
| 2137 | 0.3887 | Step 1 – After the installation, the add-on config... |
| 2138 | 0.3887 | VMware groups. The product collects data from vCen... |
| 2139 | 0.3886 | Step 9 – In the Advanced Deployment Options dialog... |
| 2140 | 0.3885 | In the report filters, select a monitoring plan yo... |
| 2141 | 0.3883 | v10.7 Step 2 – Unzip the package to any folder on ... |
| 2142 | 0.3882 | Unless specified, data is not associated with a s ... |
| 2143 | 0.3882 | NOTE: This step is only required when changing the... |
| 2144 | 0.3880 | Specify a name of associated monitoring plan in Au... |
| 2145 | 0.3880 | 55.. Go to Certificates (Local Computer) > Persona... |
| 2146 | 0.3880 | In the same domain No restrictions In two-way trus... |
| 2147 | 0.3880 | Once the product is configured to collect data fro... |
| 2148 | 0.3880 | Provide the name of the UDP port used to listen to... |
| 2149 | 0.3879 | Step 7 – In Auditor, create a monitoring plan for ... |
| 2150 | 0.3879 | ◦ Additional configuration if auto-backup is enabl... |
| 2151 | 0.3879 | v10.7 Step 6 – Click OK. Step 7 – In Auditor, crea... |
| 2152 | 0.3879 | Clicking the second link opens a dashboard that li... |
| 2153 | 0.3876 | to the Auditor Home screen to access them instantl... |
| 2154 | 0.3875 | Step 7 – In Auditor, create a monitoring plan for ... |
| 2155 | 0.3875 | The credentials are case sensitive. If using a gro... |
| 2156 | 0.3875 | The credentials are case sensitive. If using a gro... |
| 2157 | 0.3875 | The credentials are case sensitive. If using a gro... |
| 2158 | 0.3874 | Table 2: Opens the Alerts Overview dashboard, whic... |
| 2159 | 0.3873 | • HTTP HTTPS v10.7 Option Description General Prov... |
| 2160 | 0.3873 | ◦◦ See the Configure AD FS farm manually topic for... |
| 2161 | 0.3872 | For example, the Windows Firewall service stopped.... |
| 2162 | 0.3872 | Click Search. Navigate to Tools and select Subscri... |
| 2163 | 0.3871 | Monitoring Plan Summary At this step of the wizard... |
| 2164 | 0.3871 | Use the following format: <parameter>value</parame... |
| 2165 | 0.3871 | To import snapshots, you must be assigned the Glob... |
| 2166 | 0.3869 | v10.7 Assign Permission Via the Registry Editor Sn... |
| 2167 | 0.3867 | In the latter case, make sure the directory exists... |
| 2168 | 0.3864 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 2169 | 0.3863 | NetwrixAuditorUserName Current user credentials Un... |
| 2170 | 0.3862 | Step 3 – In the Allow an app or feature through Wi... |
| 2171 | 0.3862 | Thus, it is recommended that instead of retrievein... |
| 2172 | 0.3861 | Add a path to the add-on in double quotes and spec... |
| 2173 | 0.3858 | Table 1: Option Description General Monitor this d... |
| 2174 | 0.3858 | Otherwise, your audit scope may contain warnings, ... |
| 2175 | 0.3857 | The events will be saved into the local repository... |
| 2176 | 0.3856 | Step 1 – In Auditor client, click Settings > Long-... |
| 2177 | 0.3854 | Step 3 – Run the installation package. Step 4 – Ac... |
| 2178 | 0.3854 | Step 3 – Run the installation package. Step 4 – Ac... |
| 2179 | 0.3853 | Allow outbound connections from the dynamic (1024 ... |
| 2180 | 0.3853 | To specify a non-default port, provide a server na... |
| 2181 | 0.3852 | To specify a non-default port, provide a server na... |
| 2182 | 0.3851 | v10.7 Option Description Do not select the checkbo... |
| 2183 | 0.3851 | By default, SQL Server trace logs will be stored i... |
| 2184 | 0.3851 | See the State–In–Time Reports topic for additional... |
| 2185 | 0.3849 | Unless you are going to audit logon events, the ci... |
| 2186 | 0.3847 | If you upgraded Netwrix Auditor from the version 1... |
| 2187 | 0.3847 | Failed Use this option to detect suspicious activi... |
| 2188 | 0.3847 | Defines a SQL Server instance where your Audit SQL... |
| 2189 | 0.3846 | Starting with version 10.7, you can implement the ... |
| 2190 | 0.3844 | Compatibility Notice The file must be formatted in... |
| 2191 | 0.3844 | Select import database name. By default, data is i... |
| 2192 | 0.3844 | See the Integration API topic for additional infor... |
| 2193 | 0.3843 | SyslogServerProtocol – communication protocol for ... |
| 2194 | 0.3842 | A custom account must be granted the same permissi... |
| 2195 | 0.3842 | Follow the steps to define the Log On As a Service... |
| 2196 | 0.3841 | Work with Collected Data Review the examples below... |
| 2197 | 0.3841 | They list all activity that occurred across the au... |
| 2198 | 0.3840 | During the Netwrix Auditor for SharePoint Core Ser... |
| 2199 | 0.3839 | Select which of your Active Directory environment ... |
| 2200 | 0.3839 | Use semicolon to separate several addresses. Monit... |
| 2201 | 0.3837 | Examples: *admin*@corp.com */Drafts - exclude Draf... |
| 2202 | 0.3835 | • Workstation where activity was initiated — enter... |
| 2203 | 0.3835 | NOTE: The template remains the same for all alerts... |
| 2204 | 0.3835 | To specify a non-default port, provide a server na... |
| 2205 | 0.3835 | To specify a non-default port, provide a server na... |
| 2206 | 0.3832 | Create login for ONTAPI role: security login creat... |
| 2207 | 0.3832 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} (DN... |
| 2208 | 0.3832 | See for API Endpoints more information. 404 Not Fo... |
| 2209 | 0.3831 | Ensure that your account meets the requirements an... |
| 2210 | 0.3831 | Item—name of the SQL Server instance monitored wit... |
| 2211 | 0.3831 | Item—name of the SQL Server instance monitored wit... |
| 2212 | 0.3831 | Step 2 – In the item configuration menu, select Ne... |
| 2213 | 0.3830 | Enable automatic audit configuration— If any confl... |
| 2214 | 0.3830 | SQL Server Ports Review a full list of protocols a... |
| 2215 | 0.3830 | See the State–In–Time Reports topic for additional... |
| 2216 | 0.3829 | Click Configure to specify the import scope. Optio... |
| 2217 | 0.3829 | Syslog Server Provide a server name by entering it... |
| 2218 | 0.3828 | Logon Activity Auditor supports monitoring the fol... |
| 2219 | 0.3826 | Execute... https certificate subject= "Netwrix Int... |
| 2220 | 0.3824 | Table 1: Option Description The Event tab Name Spe... |
| 2221 | 0.3824 | Table 2: Option Description From... To... Specify ... |
| 2222 | 0.3822 | Cisco FTD Auditor supports monitoring the followin... |
| 2223 | 0.3822 | In the search box, type Mail.ReadWrite and Mail.Se... |
| 2224 | 0.3822 | Unless specified, the add-on runs with the current... |
| 2225 | 0.3822 | Do not select the checkbox if you want to configur... |
| 2226 | 0.3821 | The 'When' column shows the time when the syslog m... |
| 2227 | 0.3821 | If you want to run the add-on on another machine, ... |
| 2228 | 0.3820 | — Address The Address parameter may be followed by... |
| 2229 | 0.3819 | v10.7 Configure Advanced Audit Policies Configure ... |
| 2230 | 0.3818 | Parameter Default value Description Assumes that t... |
| 2231 | 0.3818 | Step 3 – Right-click the service and on the Genera... |
| 2232 | 0.3817 | To specify a non-default port, provide a server na... |
| 2233 | 0.3817 | (514 by default). v10.7 Click Proceed and complete... |
| 2234 | 0.3815 | Navigate to Manage → Log Settings → Syslog. 77.. S... |
| 2235 | 0.3815 | Assumes that the add-on runs on the computer hosti... |
| 2236 | 0.3815 | Assumes that the add-on runs on the computer hosti... |
| 2237 | 0.3813 | To specify a non-default port, provide a server na... |
| 2238 | 0.3812 | You are looking for changes that occurred more tha... |
| 2239 | 0.3812 | If you later clear this option to start saving dat... |
| 2240 | 0.3811 | For example, "MyOracle". Wallet alias Alias name i... |
| 2241 | 0.3810 | Step 3 – Provide Auditor Server IP address and por... |
| 2242 | 0.3809 | To restore original look and feel, run the script ... |
| 2243 | 0.3809 | Personalize the home page of the product depending... |
| 2244 | 0.3808 | See the Choose Appropriate Execution Scenario topi... |
| 2245 | 0.3808 | Table 1: Option Description Do not select the chec... |
| 2246 | 0.3805 | See the Create a New Monitoring Plan topic for add... |
| 2247 | 0.3804 | collection at least twice. For example: #*,server,... |
| 2248 | 0.3804 | Step 1 – Create organizational units within audite... |
| 2249 | 0.3804 | v10.7 Parameter Default value Description Connecti... |
| 2250 | 0.3803 | Review Event Description Review the example of the... |
| 2251 | 0.3802 | Enabling this option on public shares will result ... |
| 2252 | 0.3802 | ◦ DNSHostName — FQDN of the new gMSA account, here... |
| 2253 | 0.3801 | The newly created data source will appear in the D... |
| 2254 | 0.3799 | See File-Based Repository for Long-Term Archive fo... |
| 2255 | 0.3798 | Otherwise, enabling this option may lead to issues... |
| 2256 | 0.3797 | AWS CloudTrail is an internal tracking service tha... |
| 2257 | 0.3797 | Allow outbound connections to the remote ports on ... |
| 2258 | 0.3796 | Microsoft Entra ID applications can be assigned De... |
| 2259 | 0.3796 | Microsoft Entra ID applications can be assigned De... |
| 2260 | 0.3795 | The next time you run the script, it will start re... |
| 2261 | 0.3794 | Follow the step to configure integration service s... |
| 2262 | 0.3794 | ◦◦ Create a shared directory /ifs/.ifsvar/audit/ o... |
| 2263 | 0.3794 | * @172.28.18.25:514;RSYSLOG_SyslogProt ocol23Forma... |
| 2264 | 0.3793 | Subscriptions Opens the Subscriptions wizard, whic... |
| 2265 | 0.3793 | Specify actions you want to track and auditing mod... |
| 2266 | 0.3791 | For example: list/document.docx http(s)://URL Ente... |
| 2267 | 0.3791 | Step 1 – Select the desired item. Step 2 – In the ... |
| 2268 | 0.3791 | Step 1 – Select the desired item. Step 2 – In the ... |
| 2269 | 0.3787 | If you plan to use modern authentication, see the ... |
| 2270 | 0.3787 | Ensure that... The Audit Database settings are con... |
| 2271 | 0.3785 | Step 1 – On the computer where Auditor Server resi... |
| 2272 | 0.3784 | See the Manage Sources and Control Data Processing... |
| 2273 | 0.3784 | See the Role-Based Access and Delegation topic for... |
| 2274 | 0.3784 | Use the account with a privileged role on a regula... |
| 2275 | 0.3783 | parameter, it cannot be replaced omitcollectlist.t... |
| 2276 | 0.3782 | The sysadmin server role on SQL Server instance is... |
| 2277 | 0.3782 | Table 1: Option Description Okta Connection Settin... |
| 2278 | 0.3781 | Audit data will still be collected. Monitoring pla... |
| 2279 | 0.3780 | You can enable Auditor to continually enforce the ... |
| 2280 | 0.3778 | v10.7 Step 4 – Click Save. Optionally, you can sel... |
| 2281 | 0.3776 | To specify a non-default port, provide a server na... |
| 2282 | 0.3775 | Step 2 – On the Summary page, select the Event Sum... |
| 2283 | 0.3774 | Failed change attempts The Auditing Entry below sh... |
| 2284 | 0.3774 | Table 1: Feature Version 4.1 Version 5.x Network/d... |
| 2285 | 0.3770 | To specify a non-default port, provide a server na... |
| 2286 | 0.3770 | To specify a non-default port, provide a server na... |
| 2287 | 0.3770 | Step 2 – In the item configuration menu, select Ne... |
| 2288 | 0.3769 | The UDP 514 port is open for inbound connections. ... |
| 2289 | 0.3769 | See the Assign Permission To Read the Registry Key... |
| 2290 | 0.3768 | Instead, they will be managed by Netwrix Privilege... |
| 2291 | 0.3768 | In addition to the restrictions for a monitoring p... |
| 2292 | 0.3766 | Enabling TLS 1.2 Usage The add-on supports Transpo... |
| 2293 | 0.3766 | See the Launch Audit Configuration Assistant secti... |
| 2294 | 0.3765 | property name and property value are optional, but... |
| 2295 | 0.3765 | Ongoing audit data collection will leverage Micros... |
| 2296 | 0.3765 | Unless specified, the add-on runs with the current... |
| 2297 | 0.3765 | Unless specified, the add-on runs with the current... |
| 2298 | 0.3764 | Step 1 – Open Nutanix Prism web portal. Step 2 – S... |
| 2299 | 0.3764 | ALTER SYSTEM SET audit_trail=XML SCOPE=SPFILE; If ... |
| 2300 | 0.3761 | For example: -file "C:\Addons\Netwrix_Auditor_Addo... |
| 2301 | 0.3760 | You can set them to audit the following: Configura... |
| 2302 | 0.3760 | Password – Provide password for this account. Summ... |
| 2303 | 0.3760 | After deploying and configuring the add-on as desc... |
| 2304 | 0.3760 | v10.7 Step 4 – In the Maximum security log size Pr... |
| 2305 | 0.3759 | In this case, Auditor will Table 1: Option Descrip... |
| 2306 | 0.3758 | v10.7 Option Description switch to turn the featur... |
| 2307 | 0.3757 | ◦ Continue video recording regardless of the user ... |
| 2308 | 0.3757 | Step 2 – In the upper-left of your site collection... |
| 2309 | 0.3757 | Click the Details link to examine the product log.... |
| 2310 | 0.3755 | Then you will provide this account in the monitori... |
| 2311 | 0.3755 | See this Knowledge Base article for more inf ormat... |
| 2312 | 0.3754 | Step 3 – After configuring all filters, click Add ... |
| 2313 | 0.3753 | Table 1: To... Execute the command... Apply audit ... |
| 2314 | 0.3753 | Step 4 – Accept the license agreement and follow t... |
| 2315 | 0.3753 | Monitoring Overview Aggregated statistics on the m... |
| 2316 | 0.3752 | Instead, they will be managed by Netwrix Privilege... |
| 2317 | 0.3752 | Depending on the execution scenario you choose, yo... |
| 2318 | 0.3751 | Client Users group. See the Role-Based Access and ... |
| 2319 | 0.3751 | Table 1: Object Type Reported Action Reported Prop... |
| 2320 | 0.3750 | Export data When exporting large amount of data (e... |
| 2321 | 0.3750 | Data is collected from a NetwrixAuditorHost remote... |
| 2322 | 0.3749 | The body is empty. The 404 Not Found Error request... |
| 2323 | 0.3748 | Working with Mount Points You can specify a mount ... |
| 2324 | 0.3747 | If you are running the add-on for the first time (... |
| 2325 | 0.3743 | SonicWall Devices Review a full list of object typ... |
| 2326 | 0.3743 | NetwrixAuditorHost localhost:9699 If you want to r... |
| 2327 | 0.3743 | 53 UDP Netwrix Auditor Server DNS Server DNS Clien... |
| 2328 | 0.3743 | Service Team Service team that will be responsible... |
| 2329 | 0.3742 | v10.7 Required Roles and Permissions To... Require... |
| 2330 | 0.3742 | /q Specify the user interface (UI) that displays d... |
| 2331 | 0.3741 | See the Permissions for SharePoint Online Auditing... |
| 2332 | 0.3740 | Auditor provides out-of-box reports that allow val... |
| 2333 | 0.3740 | See the Netwrix Privilege Secure topic for additio... |
| 2334 | 0.3739 | Settings for a certain event source (within the So... |
| 2335 | 0.3738 | Also, this folder includes a report on Auditor sel... |
| 2336 | 0.3737 | Table 1: Port Protocol Source Target Purpose 443 T... |
| 2337 | 0.3735 | Execute the following command: Add-SPShellAdmin –U... |
| 2338 | 0.3735 | The Read share permission on the audited shared fo... |
| 2339 | 0.3733 | This status applies to the monitoring plans target... |
| 2340 | 0.3733 | Step 6 – Register the Add-On Prepare Auditor for D... |
| 2341 | 0.3731 | You can use a wildcard (*). In this case you will ... |
| 2342 | 0.3730 | File Servers Dell Data Storage Auditor supports mo... |
| 2343 | 0.3730 | In addition to the restrictions for a monitoring p... |
| 2344 | 0.3730 | To specify a non-default port, provide a server na... |
| 2345 | 0.3730 | The Resource name in this case is where the activi... |
| 2346 | 0.3730 | Step 1 – On the main Auditor page, navigate to the... |
| 2347 | 0.3729 | If not, the service will proceed to the next rule ... |
| 2348 | 0.3728 | To connect to NetApp Clustered Data ONTAP 8 or ONT... |
| 2349 | 0.3728 | When specified, overrides the NetwrixAuditorPlan —... |
| 2350 | 0.3728 | Step 2 – Within the monitoring plan window, highli... |
| 2351 | 0.3728 | Table 1: Data source Components • Microsoft Entra ... |
| 2352 | 0.3727 | Step 1 – Select the desired item. Step 2 – In the ... |
| 2353 | 0.3727 | Active Directory Auditor supports monitoring the f... |
| 2354 | 0.3726 | After you click View details, the Monitoring Overv... |
| 2355 | 0.3724 | If you configured a dedicated monitoring plan, mak... |
| 2356 | 0.3723 | Data is written a remote on_for_HPE_ ArcSight.ps1 ... |
| 2357 | 0.3723 | (514 by default). Auditor Endpoint Auditor Server ... |
| 2358 | 0.3722 | Make sure to create a dedicated item in Auditor in... |
| 2359 | 0.3722 | Microsoft Entra ID (formerly Azure AD) Auditor sup... |
| 2360 | 0.3721 | This permission should be assigned on each domain ... |
| 2361 | 0.3721 | Send a POST request containing your search paramet... |
| 2362 | 0.3719 | v10.7 Each report has a set of filters which help ... |
| 2363 | 0.3718 | Table 1: on... Ensure that... The Auditor Server s... |
| 2364 | 0.3718 | v10.7 Step 7 – When done, click Finish. Define Par... |
| 2365 | 0.3715 | Netwrix recommends limiting the input Activity Rec... |
| 2366 | 0.3715 | For example, clicking Go to Original Go to Origina... |
| 2367 | 0.3714 | Step 2 – Locate the ConnectWiseSettings.xml file a... |
| 2368 | 0.3713 | If you plan to use modern authentication, see the ... |
| 2369 | 0.3713 | If you plan to use modern authentication, see the ... |
| 2370 | 0.3713 | See the Choose Appropriate Execution Scenario topi... |
| 2371 | 0.3710 | v10.7 Parameter Default value Description The numb... |
| 2372 | 0.3709 | Access MS Teams Using Modern Authentication This o... |
| 2373 | 0.3709 | For that, use the Monitoring Plan wizard or naviga... |
| 2374 | 0.3709 | You can also: Select a particular computer type to... |
| 2375 | 0.3706 | Ensure that... The Auditor server side • Auditor v... |
| 2376 | 0.3705 | Allow outbound connections from the dynamic (1024 ... |
| 2377 | 0.3703 | Step 3 – Specify default SQL Server instance and c... |
| 2378 | 0.3703 | When using this mode, consider that the "What" fi ... |
| 2379 | 0.3703 | Depending on the execution scenario you choose, yo... |
| 2380 | 0.3701 | Subscription to Risk Assessment Overview This subs... |
| 2381 | 0.3701 | The non-replicated attributes pertain to a particu... |
| 2382 | 0.3700 | Network Devices Cisco ASA Devices Auditor supports... |
| 2383 | 0.3699 | You can click Browse to select a array computer fr... |
| 2384 | 0.3697 | Events collected from any other source will be ign... |
| 2385 | 0.3695 | The retention method of the Security event log mus... |
| 2386 | 0.3693 | v10.7 Click Proceed and complete the following fie... |
| 2387 | 0.3691 | To be able to audit and report who made those chan... |
| 2388 | 0.3690 | Windows File Share Nutanix SMB Shares File Servers... |
| 2389 | 0.3689 | Configure Default SQL Server Settings On the Setti... |
| 2390 | 0.3689 | v10.7 44.. Double-click CleanAutoBackupLogs. The E... |
| 2391 | 0.3688 | Please note the following rebranding limitations a... |
| 2392 | 0.3688 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 2393 | 0.3688 | Check that your data collecting account has all re... |
| 2394 | 0.3686 | When prompted, accept the end-user license agreeme... |
| 2395 | 0.3686 | To verify the necessary settings of the existing p... |
| 2396 | 0.3685 | When running Free Community Edition, at any time y... |
| 2397 | 0.3685 | Software Compatibility & Versions For proper funct... |
| 2398 | 0.3684 | By default, set to zero offse t (UTC). Define a cu... |
| 2399 | 0.3684 | To specify a non-default port, provide a server na... |
| 2400 | 0.3683 | Prerequisites Before running the add-on, ensure th... |
| 2401 | 0.3683 | Sub-element: Name. The item type is added inside t... |
| 2402 | 0.3682 | Dell Isilon Dell VNX VNXe NetApp Windows File Shar... |
| 2403 | 0.3681 | Run the fs list command in ncli to get the list of... |
| 2404 | 0.3681 | You can use a wildcard (*). In this case you will ... |
| 2405 | 0.3678 | The following considerations and limitations refer... |
| 2406 | 0.3678 | Same logic applies to the inclusion rules. Example... |
| 2407 | 0.3678 | Some network compression services must be removed ... |
| 2408 | 0.3677 | For more information on the structure of the Activ... |
| 2409 | 0.3677 | Subscribe to a report On the main Auditor page, na... |
| 2410 | 0.3675 | • .NET Framework versions 4.5 or later Nutanix Pri... |
| 2411 | 0.3675 | If you plan to monitor Dell Isilon, clear the chec... |
| 2412 | 0.3673 | Table 1: Location Prerequisites Auditor Server • T... |
| 2413 | 0.3673 | Settings for a certain event source (within the So... |
| 2414 | 0.3672 | If you want to generate reports based on differen ... |
| 2415 | 0.3672 | If you want to generate reports based on differen ... |
| 2416 | 0.3672 | If you want to generate reports based on differen ... |
| 2417 | 0.3671 | Assumes that the add-on runs on the computer hosti... |
| 2418 | 0.3670 | will not be monitored. See the topics on the monit... |
| 2419 | 0.3669 | NOTE: If you want to reopen closed tickets, you mu... |
| 2420 | 0.3669 | To specify a non-default port, provide a server na... |
| 2421 | 0.3667 | Step 4 – Select Content Manager. Grant Additional ... |
| 2422 | 0.3667 | Table 1: Parameter Default value Description Provi... |
| 2423 | 0.3666 | Table 1: Port Protocol Source Target Purpose 137 1... |
| 2424 | 0.3664 | For that, review the following procedures: Configu... |
| 2425 | 0.3662 | See the Dell Upsilon CLI Administration Guide for ... |
| 2426 | 0.3662 | The Resource name in this case is where the activi... |
| 2427 | 0.3662 | Under the Syslog Servers, complete the following f... |
| 2428 | 0.3661 | Contact your Auditor Global administrator to make ... |
| 2429 | 0.3660 | will not be monitored. See the topics on the monit... |
| 2430 | 0.3660 | Overview diagrams—System-specific diagram reports ... |
| 2431 | 0.3658 | To specify a non-default port, provide a server na... |
| 2432 | 0.3658 | Symbol XML entity & &amp; e.g., Ally & Sons e.g., ... |
| 2433 | 0.3658 | Review your configuration and click Save. Review R... |
| 2434 | 0.3656 | C:\Add-ons\Netwrix_Auditor_Addon_for_RADIUS_Server... |
| 2435 | 0.3656 | Add / Remove Programs Installed For** Add or Remov... |
| 2436 | 0.3655 | Add the requirements for 5 million files which are... |
| 2437 | 0.3655 | v10.7 Prerequisites Before running the add-on, ens... |
| 2438 | 0.3655 | Retention period for the video files can be adjust... |
| 2439 | 0.3654 | Step 3 – Adjust the security event log size and re... |
| 2440 | 0.3653 | You can append other options, such as n to hide th... |
| 2441 | 0.3652 | See the Role-Based Access and Delegation topic for... |
| 2442 | 0.3650 | Then, s/he does not want the product to NetApp mon... |
| 2443 | 0.3650 | Copy it to a safe location. See the following Micr... |
| 2444 | 0.3648 | See the Health Status Dashboard topic for addition... |
| 2445 | 0.3648 | The Auditor Server side • Auditor version is 9.8 o... |
| 2446 | 0.3647 | object_type.property_nam e If there is no separato... |
| 2447 | 0.3647 | 55.. Run the following command to update group pol... |
| 2448 | 0.3646 | Also, consider that all risk metrics and related r... |
| 2449 | 0.3644 | Click Search. Navigate to Tools and select Subscri... |
| 2450 | 0.3644 | Synology Ports Review a full list of protocols and... |
| 2451 | 0.3643 | An account used by Netwrix Auditor to upload data ... |
| 2452 | 0.3643 | v10.7 7. The add-on starts collecting and forwardi... |
| 2453 | 0.3642 | For example: ◦◦ If you want to periodically receiv... |
| 2454 | 0.3641 | gpupdate / force 445 TCP Netwrix Auditor Server Do... |
| 2455 | 0.3641 | If selected, change the retention method to Overwr... |
| 2456 | 0.3640 | Sub-element: Name. The item type is added inside t... |
| 2457 | 0.3640 | Attach Activity Summary as a CSV file — You can co... |
| 2458 | 0.3639 | Configure Local Audit Policies You can choose to c... |
| 2459 | 0.3638 | ◦◦ The logging trap option is selected from 1 to 6... |
| 2460 | 0.3637 | See the Create a New Monitoring Plan topic for add... |
| 2461 | 0.3635 | Pager is the default property. If the Pager proper... |
| 2462 | 0.3632 | If selected, this option instructs Auditor to depl... |
| 2463 | 0.3631 | The credentials are case sensitive. A custom accou... |
| 2464 | 0.3630 | Step 4 – Hit Enter. Depending on the number of eve... |
| 2465 | 0.3630 | Feature comparison is provided in the table below.... |
| 2466 | 0.3629 | State-in-time configuration snapshots are also use... |
| 2467 | 0.3628 | Snapshot date —select the date of state-in-time sn... |
| 2468 | 0.3628 | Snapshot date —select the date of state-in-time sn... |
| 2469 | 0.3628 | Windows Installer 3.1 and Windows Installer 3.1 an... |
| 2470 | 0.3628 | Copy it to a safe location. See the following Micr... |
| 2471 | 0.3627 | Step 2 – Unzip the Add-On to a desired folder. Ste... |
| 2472 | 0.3627 | The default values is 900 seconds, i.e., 15 minute... |
| 2473 | 0.3625 | To specify a non-default port, provide a new port ... |
| 2474 | 0.3624 | See the Role-Based Access and Delegation topic for... |
| 2475 | 0.3623 | DBName By default, the database responsible for Ne... |
| 2476 | 0.3623 | SQL Server Instance As a Auditor administrator I w... |
| 2477 | 0.3622 | Ensure that... Auditor version is 10.0 or later. T... |
| 2478 | 0.3621 | On successful subscription generation you will rec... |
| 2479 | 0.3621 | Configure the Microsoft Entra ID App for Auditing ... |
| 2480 | 0.3621 | File Servers (including Windows file server, Dell,... |
| 2481 | 0.3620 | This account must be included in the following gro... |
| 2482 | 0.3616 | v10.7 This feature is supported only for SQL Serve... |
| 2483 | 0.3616 | Grant —the set of permissions granted to this acco... |
| 2484 | 0.3616 | Step 1 – On your target server, open Registry Edit... |
| 2485 | 0.3615 | After specifying the criteria you need, click Sear... |
| 2486 | 0.3615 | ◦ Continue video recording regardless of the user ... |
| 2487 | 0.3614 | It is shipped with the add-on and creates the RADI... |
| 2488 | 0.3614 | Netwrix gathers the following information about MS... |
| 2489 | 0.3614 | 50-100 concurrent sessions per terminal server. Ne... |
| 2490 | 0.3613 | NOTE: In some cases, Who will be the system and Wh... |
| 2491 | 0.3612 | C:\Add-ons\Netwrix_Auditor_Addon_for_ RADIUS_Serve... |
| 2492 | 0.3612 | Unless an account is specified, the NetwrixAuditor... |
| 2493 | 0.3611 | AccessInformationCenter.Service.e xe Located in th... |
| 2494 | 0.3611 | Step 2 – Type a path to the add-on. Or simply drag... |
| 2495 | 0.3611 | If a specific account is designated to run the add... |
| 2496 | 0.3610 | Step 4 – The new secret will be displayed in the l... |
| 2497 | 0.3610 | Auditor Server side • Auditor version is 9.8 or la... |
| 2498 | 0.3609 | Follow the steps to use Netwrix Privilege Secure a... |
| 2499 | 0.3609 | Follow the steps to use Netwrix Privilege Secure a... |
| 2500 | 0.3608 | v10.7 Option Description they will not be collecte... |
| 2501 | 0.3607 | To import Active Directory data from the removed m... |
| 2502 | 0.3606 | For example, you can run the add-on on the compute... |
| 2503 | 0.3605 | Path The path must be provided in the same format ... |
| 2504 | 0.3605 | To be able to audit and report who made those chan... |
| 2505 | 0.3605 | Consider the following: Specify monitoring restric... |
| 2506 | 0.3604 | See the Prerequisites and Audit Database topics fo... |
| 2507 | 0.3604 | You can enable Auditor to continually enforce the ... |
| 2508 | 0.3602 | OR Table 1: To... Requirement Comment Cloud Applic... |
| 2509 | 0.3602 | For example to switch to the SVM called svm1: clus... |
| 2510 | 0.3601 | Manually – Native audit settings must be adjusted ... |
| 2511 | 0.3601 | If not, the service will proceed to the next rule ... |
| 2512 | 0.3601 | If not, the service will proceed to the next rule ... |
| 2513 | 0.3599 | All audit data from your search query results will... |
| 2514 | 0.3597 | type,what,property name Table 1: File Description ... |
| 2515 | 0.3597 | Step 5 – Click on the arrow button next to any of ... |
| 2516 | 0.3597 | In this case audit data is still being collected. ... |
| 2517 | 0.3596 | Table 1: Option Description You must be assigned t... |
| 2518 | 0.3596 | In the Group Policy Management Editor dialog, expa... |
| 2519 | 0.3596 | Notifications Notification settings are configured... |
| 2520 | 0.3593 | See the Netwrix Privilege Secure topic for additio... |
| 2521 | 0.3592 | v10.7 Parameter Default value Description Server r... |
| 2522 | 0.3591 | Customize Branding Netwrix Auditor allows customiz... |
| 2523 | 0.3590 | Monitoring plan configuration List folders + + + +... |
| 2524 | 0.3590 | Users can also configure Only the latest snapshot ... |
| 2525 | 0.3590 | Users can also configure Only the latest snapshot ... |
| 2526 | 0.3590 | Step 3 – In the Group Policy Management Editor dia... |
| 2527 | 0.3590 | See the Audit Configuration Assistant topic for ad... |
| 2528 | 0.3589 | The logging trap option is selected from 1 to 6 in... |
| 2529 | 0.3588 | Table 1: Registry key (REG_DWORD type) Description... |
| 2530 | 0.3588 | To collect data from 32-bit operating systems, net... |
| 2531 | 0.3588 | The newly created data source will appear in the D... |
| 2532 | 0.3587 | v10.7 Work with Collected Data To leverage data co... |
| 2533 | 0.3587 | Send a POST request containing this Continuation m... |
| 2534 | 0.3586 | Database service account – This is the same accoun... |
| 2535 | 0.3584 | Specify Nutanix File Server If you need to audit a... |
| 2536 | 0.3582 | DefaultTsTimezone — Define the time zone of syslog... |
| 2537 | 0.3582 | Click Modify and select day(s) of week you want yo... |
| 2538 | 0.3582 | Click Modify and select day(s) of week you want yo... |
| 2539 | 0.3582 | Specify monitoring restrictions Remember that admi... |
| 2540 | 0.3581 | NOTE: Make sure that the Send alert when the actio... |
| 2541 | 0.3579 | Log format – Set to "IETF (RFC 5424)". Enable secu... |
| 2542 | 0.3578 | This codec is installed automatically on the compu... |
| 2543 | 0.3578 | Prerequisites Before running the add-on, ensure th... |
| 2544 | 0.3576 | The Auditor server side • Auditor version is 10.0 ... |
| 2545 | 0.3574 | : Dell Data Storage Dell Isilon/PowerScale NetApp ... |
| 2546 | 0.3573 | See the NetApp Data ONTAP topic for additional inf... |
| 2547 | 0.3573 | Move the selected snapshots to the Snapshots avail... |
| 2548 | 0.3572 | Then you will provide this account in the monitori... |
| 2549 | 0.3572 | Step 2 – Enable audit in the Azure Files settings.... |
| 2550 | 0.3572 | (not displayed) The data source status is unknown.... |
| 2551 | 0.3571 | Default value is -1 (switch off concurrent forward... |
| 2552 | 0.3571 | Data is written a remote ArcSight through UDP prot... |
| 2553 | 0.3571 | Permissions Permissions are needed to the Netwrix ... |
| 2554 | 0.3570 | Current data should be stored in other access zone... |
| 2555 | 0.3569 | For that, run the following command in ncli : fs a... |
| 2556 | 0.3569 | Equals (default) Netwrix Auditor supports the 2. N... |
| 2557 | 0.3569 | See the Assign Permission To Read the Registry Key... |
| 2558 | 0.3568 | You should specify only the account name in the do... |
| 2559 | 0.3568 | Microsoft Entra ID monitoring plan has been added ... |
| 2560 | 0.3567 | SharePoint NOTE: Prior to configuring your monitor... |
| 2561 | 0.3567 | Step 1 – On the computer where Microsoft Exchange ... |
| 2562 | 0.3566 | Inner_type is optional. Table 1: File Description ... |
| 2563 | 0.3566 | omitlogonlist.txt to exclude logon activity from m... |
| 2564 | 0.3565 | See the View Reports topic for additional informat... |
| 2565 | 0.3564 | The checklist will be replaced by statistics acros... |
| 2566 | 0.3563 | To upgrade the Access Reviews application to a new... |
| 2567 | 0.3563 | You can click Browse to select a computer from the... |
| 2568 | 0.3563 | Palo Alto Pulse Secure Provide this account in the... |
| 2569 | 0.3561 | Enforce certificate validation to ensure security ... |
| 2570 | 0.3561 | Click Add Recipient and provide email address. REC... |
| 2571 | 0.3560 | The servers within the farm are located in differe... |
| 2572 | 0.3559 | Prerequisites Before running the add-on, ensure th... |
| 2573 | 0.3559 | Follow the steps to configure local audit policies... |
| 2574 | 0.3559 | See the Add Items for Monitoring topic for additio... |
| 2575 | 0.3558 | Make sure this account is granted the Content Mana... |
| 2576 | 0.3557 | For Dell Isilon/PowerScale storage 8.2 and above, ... |
| 2577 | 0.3555 | Credentials for connection to Nutanix Prism server... |
| 2578 | 0.3554 | ExcludedCmdlets *-InboxRule, *-MailboxAutoReplyCon... |
| 2579 | 0.3553 | logons), use the omitlogonlist.txt. Use the omitre... |
| 2580 | 0.3553 | For example, you can run the add-on on the compute... |
| 2581 | 0.3552 | For some antiviruses (for example, Trend Micro) yo... |
| 2582 | 0.3551 | However, consider the following: If a mount point ... |
| 2583 | 0.3551 | In addition to the restrictions for a monitoring p... |
| 2584 | 0.3550 | The product updates the latest snapshot on the reg... |
| 2585 | 0.3549 | Auditor version is 9.8 or later. The Audit Databas... |
| 2586 | 0.3548 | Path *OU=OUNAME* For example: If the OU is "sample... |
| 2587 | 0.3547 | Complete the following fields: Option Description ... |
| 2588 | 0.3545 | To exclude events containing “System” instead of i... |
| 2589 | 0.3543 | Successful changes The Auditing Entry below shows ... |
| 2590 | 0.3543 | In this case audit data is still being collected. ... |
| 2591 | 0.3543 | Unless an account is specified, the NetwrixAuditor... |
| 2592 | 0.3543 | Locate the POST request for partner_servers endpoi... |
| 2593 | 0.3543 | See the Isilon OneFS 8.2.1 CLI Administration Guid... |
| 2594 | 0.3541 | Regular Environment Recommendations below refer to... |
| 2595 | 0.3541 | Define Parameters The configuration wizard opens i... |
| 2596 | 0.3540 | v10.7 IBM QRadar Netwrix Auditor Add-on for SIEM h... |
| 2597 | 0.3540 | See the Configuring Your Dell Isilon/PowerScale Cl... |
| 2598 | 0.3539 | For example: Word\x0020 where \x0020 (with space a... |
| 2599 | 0.3538 | A custom account must be granted the same permissi... |
| 2600 | 0.3538 | If you are using Netwrix Auditor for Network Devic... |
| 2601 | 0.3538 | Active Directory service account – The Access Revi... |
| 2602 | 0.3537 | Step 3 – Use the Access reviews configuration tool... |
| 2603 | 0.3537 | Max length: 255. • Contains (default) • DoesNotCon... |
| 2604 | 0.3537 | Step 1 – Make sure you have completed the preparat... |
| 2605 | 0.3537 | v10.7 Error in PowerShell Resolution Select the ac... |
| 2606 | 0.3536 | Review the following for additional information: O... |
| 2607 | 0.3535 | See the State–In–Time Reports topic for additional... |
| 2608 | 0.3535 | Auditor version is 9.8 or later. The Audit Databas... |
| 2609 | 0.3534 | See the State–In–Time Reports topic for a dditiona... |
| 2610 | 0.3534 | See the State–In–Time Reports topic for a dditiona... |
| 2611 | 0.3533 | This method is recommended for evaluation purposes... |
| 2612 | 0.3533 | Alerts Configure alerts that will be triggered by ... |
| 2613 | 0.3532 | You should specify only the account name in the do... |
| 2614 | 0.3531 | Table 1: Option Description Events collected from ... |
| 2615 | 0.3531 | Table 1: Option Description Events collected from ... |
| 2616 | 0.3531 | • Windows Server (with enabled network tra ffic co... |
| 2617 | 0.3531 | This method is recommended for evaluation purposes... |
| 2618 | 0.3530 | The Audit Database settings are configured in Audi... |
| 2619 | 0.3530 | In the page that opens, navigate to the report you... |
| 2620 | 0.3529 | See the SQL Server Reporting Services topic for ad... |
| 2621 | 0.3529 | For example, "MyOracle". Alias name in Netwrix Aud... |
| 2622 | 0.3527 | Execute the following command: Get-MailboxDatabase... |
| 2623 | 0.3526 | Otherwise, reports will contain limited data and w... |
| 2624 | 0.3525 | I see a blank window instead of a report. Contact ... |
| 2625 | 0.3524 | Depending on your Oracle Database version, the SEL... |
| 2626 | 0.3524 | For example: Format Request curl https://WKSWin201... |
| 2627 | 0.3524 | snapshot_modify_snapshot A snapshot was modified. ... |
| 2628 | 0.3524 | VMware Ports Review a full list of protocols and p... |
| 2629 | 0.3523 | Server and Client It is recommended to deploy Audi... |
| 2630 | 0.3522 | See the following Microsoft article for additional... |
| 2631 | 0.3521 | Assumes that the add-on runs on the computer hosti... |
| 2632 | 0.3519 | The product updates the latest snapshot on the reg... |
| 2633 | 0.3519 | When configuring, mind that your data will be dele... |
| 2634 | 0.3519 | If you select to automatically configure audit in ... |
| 2635 | 0.3519 | In this case audit data is ,*,*,Scheduled still be... |
| 2636 | 0.3518 | See the Fine-tune Monitoring ScopeFine-tune Monito... |
| 2637 | 0.3518 | Microsoft System Center Virtual Machine Manager SC... |
| 2638 | 0.3517 | Updates to this partition are replicated to all do... |
| 2639 | 0.3517 | To check that a new policy was included in the lis... |
| 2640 | 0.3516 | Changes to Domain local groups of a different doma... |
| 2641 | 0.3516 | There you can use the UI controls to run the varie... |
| 2642 | 0.3516 | Step 1 – Create a monitoring plan with the wizard.... |
| 2643 | 0.3516 | Virtual Deployment Overview In addition to on-prem... |
| 2644 | 0.3515 | See the MS Teams topic for additional information.... |
| 2645 | 0.3515 | Also, creating a mailbox folder isn't audited. Tab... |
| 2646 | 0.3515 | Tip for reading the table: For example, on the com... |
| 2647 | 0.3514 | Subscription options - delivery by email or upload... |
| 2648 | 0.3514 | For example: v10.7 ◦◦ If you want to periodically ... |
| 2649 | 0.3514 | For example: v10.7 ◦◦ If you want to periodically ... |
| 2650 | 0.3513 | Effective grant —the effective set of permissions ... |
| 2651 | 0.3513 | Specify data collection method You can enable netw... |
| 2652 | 0.3513 | Specify data collection method You can enable netw... |
| 2653 | 0.3513 | Recent alerts – Shows all the triggered alerts in ... |
| 2654 | 0.3512 | v10.7 Step 5 – Configure Add-on parameters Prepare... |
| 2655 | 0.3512 | Configuration parameters to specify in settings.xm... |
| 2656 | 0.3510 | Auditor Server IP address and port number followed... |
| 2657 | 0.3510 | Data will be collected using a set of triggers. Fo... |
| 2658 | 0.3509 | Table 1: On... Ensure that... The Auditor Server s... |
| 2659 | 0.3505 | If you want to run the add-on on another machine, ... |
| 2660 | 0.3503 | Compliance Mappings This tile contains links to th... |
| 2661 | 0.3503 | Auditor Server host by its DNS or NetBIOS name. Th... |
| 2662 | 0.3502 | Then s/he adds items to the monitoring plan – thes... |
| 2663 | 0.3500 | Table 1: Option Description Use implicit SSL Selec... |
| 2664 | 0.3500 | See the following Microsoft article for additional... |
| 2665 | 0.3498 | Using Modern Authentication with SharePoint Online... |
| 2666 | 0.3498 | Remember, deploy the add-on on the same machine wi... |
| 2667 | 0.3496 | Enable Secondary Logon Service Follow the steps to... |
| 2668 | 0.3496 | Collect data for state-in-time reports is switched... |
| 2669 | 0.3495 | See the Role-Based Access and Delegation topic for... |
| 2670 | 0.3495 | RECOMMENDED: For security reasons, enable only SSL... |
| 2671 | 0.3494 | Specify an item name. Make sure to create a dedica... |
| 2672 | 0.3491 | SharePoint Farm As a Auditor Administrator I want ... |
| 2673 | 0.3491 | Alternatively, you can grant the Global administra... |
| 2674 | 0.3489 | NOTE: In some scenarios multi-factor authenticatio... |
| 2675 | 0.3489 | The procedure below describes how to apply Advance... |
| 2676 | 0.3489 | Unless specified, the script runs with the current... |
| 2677 | 0.3487 | Select Monitor userdefined hidden shares if necess... |
| 2678 | 0.3487 | You can also review the <TicketParameterRefs> sect... |
| 2679 | 0.3487 | See the Customizing Favorite Reports topic for add... |
| 2680 | 0.3486 | CAUTION: UPD 514 port can only be used by one serv... |
| 2681 | 0.3481 | You can deploy Auditor on a virtual machine runnin... |
| 2682 | 0.3478 | Collect activity data Any of the following roles: ... |
| 2683 | 0.3478 | Unless specified, the service runs under the accou... |
| 2684 | 0.3478 | Unless specified, the service runs under the accou... |
| 2685 | 0.3476 | v10.7 After creating a task, wait for the next sch... |
| 2686 | 0.3476 | See the Behavior Anomalies topic for additional in... |
| 2687 | 0.3476 | Step 2 – On the Home page, navigate to Folder Sett... |
| 2688 | 0.3476 | Data is collected from a remote RADIUS server with... |
| 2689 | 0.3475 | cluster1::> vserver services web access show -name... |
| 2690 | 0.3475 | Use this option to track suspicious Failed activit... |
| 2691 | 0.3474 | See the Exchange Administrator Audit Logging Setti... |
| 2692 | 0.3474 | Table 1: On... Ensure that... The Audit Database s... |
| 2693 | 0.3474 | v10.7 Step 4 – In the Services window, ensure that... |
| 2694 | 0.3474 | Path The path must be provided in the same format ... |
| 2695 | 0.3473 | The instructions below apply only if you are going... |
| 2696 | 0.3472 | v10.7 Option Description monitoring plan you are g... |
| 2697 | 0.3471 | See the Role-Based Access and Delegation topic for... |
| 2698 | 0.3471 | v10.7 On... Ensure that... The Audit Database sett... |
| 2699 | 0.3471 | v10.7 On... Ensure that... The Audit Database sett... |
| 2700 | 0.3470 | You can also configure and receive alerts on the e... |
| 2701 | 0.3470 | You can specify custom delivery time and frequency... |
| 2702 | 0.3470 | Successful changes The Auditing Entry below shows ... |
| 2703 | 0.3470 | Configurator Access to monitoring plan configurati... |
| 2704 | 0.3470 | v10.7 Complete the following fields: Option Descri... |
| 2705 | 0.3469 | The newly created data source will appear in the D... |
| 2706 | 0.3469 | As a next step, click Add item to specify an objec... |
| 2707 | 0.3468 | Make sure the Windows File Servers you want to mon... |
| 2708 | 0.3466 | Account Lockout Examiner machine and the domain co... |
| 2709 | 0.3466 | Step 2 – Type a path to the add-on. Or simply drag... |
| 2710 | 0.3466 | Select a plan and click Edit. In the monitoring pl... |
| 2711 | 0.3465 | See Assign Roles topic for more information. Navig... |
| 2712 | 0.3465 | v10.7 To.. Do.. 1. Select a plan and click Edit. I... |
| 2713 | 0.3465 | You must be assigned the Global administrator or t... |
| 2714 | 0.3465 | You must be assigned the Global administrator or t... |
| 2715 | 0.3465 | You must be assigned the Global administrator or t... |
| 2716 | 0.3465 | System-specific dashboards reflect all changes acr... |
| 2717 | 0.3465 | The newly created data source will appear in the D... |
| 2718 | 0.3463 | Table 1: Port Protocol Source Target Purpose 9898 ... |
| 2719 | 0.3461 | Use other options (Computer, IP range to specify t... |
| 2720 | 0.3461 | Use other options (Computer, IP range to specify t... |
| 2721 | 0.3461 | Use other options (Computer, IP range to specify t... |
| 2722 | 0.3460 | cluster1::>network interface modify -vserver svm -... |
| 2723 | 0.3460 | Table 1: Step Description Locate Folder Browse for... |
| 2724 | 0.3459 | Successful changes The Auditing Entry below shows ... |
| 2725 | 0.3457 | In the Schedule state-in-time data collection sect... |
| 2726 | 0.3457 | Specify monitoring restrictions Add Computer – Pro... |
| 2727 | 0.3455 | Active Directory Ports AD FS Ports Microsoft Entra... |
| 2728 | 0.3455 | For example, an IT manager can easily provide audi... |
| 2729 | 0.3455 | If you want to run the add-on on another machine, ... |
| 2730 | 0.3455 | If you want to run the add-on on another machine, ... |
| 2731 | 0.3455 | State-in-Time reports to monitor data source state... |
| 2732 | 0.3455 | See Configure Fine Grained A uditing topic for mor... |
| 2733 | 0.3451 | Step 1 – On the audited server, open the Local Sec... |
| 2734 | 0.3451 | Step 3 – Download the Add-On. Step 4 – Configure A... |
| 2735 | 0.3451 | You can enable Auditor to continually enforce the ... |
| 2736 | 0.3450 | Execute... APIAdminTool.exe api disable Disable AP... |
| 2737 | 0.3449 | • Contains subscription generation details (interv... |
| 2738 | 0.3449 | You should specify only the account name in the do... |
| 2739 | 0.3449 | You should specify only the account name in the do... |
| 2740 | 0.3448 | Verify the parameters you provided in Settings.xml... |
| 2741 | 0.3447 | You can also configure and receive alerts on the e... |
| 2742 | 0.3446 | Create Role on NetApp Clustered Data ONTAP 8 or ON... |
| 2743 | 0.3446 | v10.7 Audit SELECT Use the settings in this sectio... |
| 2744 | 0.3445 | The Auditor Server side The Audit Database setting... |
| 2745 | 0.3445 | The Auditor Server side The Audit Database setting... |
| 2746 | 0.3445 | Make sure you have at least one monitored item in ... |
| 2747 | 0.3444 | I want to suppress errors from this server by excl... |
| 2748 | 0.3443 | By default, Auditor allows generating reports and ... |
| 2749 | 0.3443 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 2750 | 0.3442 | Pay attention to the "Data categories" column in s... |
| 2751 | 0.3441 | It is not recommended to store your Long-Term Arch... |
| 2752 | 0.3441 | Unless specified, the script runs with the current... |
| 2753 | 0.3440 | Step 2 – In the Help Protect your computer with Wi... |
| 2754 | 0.3437 | For detailed information about Qumulo Web UI. refe... |
| 2755 | 0.3437 | To collect data from Windows Failover Cluster, net... |
| 2756 | 0.3437 | Collect data on non-owner access to mailboxes Revi... |
| 2757 | 0.3436 | For more information on this deployment option, re... |
| 2758 | 0.3436 | This helps to optimize solution performance during... |
| 2759 | 0.3436 | This helps to optimize solution performance during... |
| 2760 | 0.3436 | Review details and play a video by clicking the Sh... |
| 2761 | 0.3436 | If you select to automatically configure audit in ... |
| 2762 | 0.3435 | For Dell VNX: server_security <NAS Server Name> -u... |
| 2763 | 0.3435 | and modifying attributes of these objects (listed ... |
| 2764 | 0.3435 | See the Deployment Proceduretopic for more informa... |
| 2765 | 0.3434 | See the Fine-tune Monitoring ScopeFine-tune Monito... |
| 2766 | 0.3433 | If you want to audit all actions (successful reads... |
| 2767 | 0.3429 | Only the lowest 9 bits of the calculation result a... |
| 2768 | 0.3429 | Step 4 – Obtain the tenant ID. You will need it wh... |
| 2769 | 0.3428 | Step 2 – Double-click SQL Server monitoring plan. ... |
| 2770 | 0.3428 | Table 1: File name Description install.ps1 PowerSh... |
| 2771 | 0.3428 | Prerequisites Before running the add-on, ensure th... |
| 2772 | 0.3428 | A monitoring plan defines data collection, notific... |
| 2773 | 0.3427 | If you want to generate reports based on differen ... |
| 2774 | 0.3427 | Step 3 – Specify SQL Server instance that you need... |
| 2775 | 0.3426 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 2776 | 0.3426 | This script creates a Windows scheduled task that ... |
| 2777 | 0.3425 | Click Finish to Summary exit the wizard. The newly... |
| 2778 | 0.3425 | Work with Collected Data To leverage data collecte... |
| 2779 | 0.3425 | Work with Collected Data To leverage data collecte... |
| 2780 | 0.3425 | Work with Collected Data To leverage data collecte... |
| 2781 | 0.3424 | ONTAPI/ONTAP REST API Select one of the following:... |
| 2782 | 0.3424 | Add Computer – Provide the name of the Specify mon... |
| 2783 | 0.3423 | Tip for reading the table: For example, on any mon... |
| 2784 | 0.3422 | To specify a non-default port, provide a server na... |
| 2785 | 0.3422 | See the Assign Permission to Read the Registry Key... |
| 2786 | 0.3421 | (not displayed) The data source status is unknown.... |
| 2787 | 0.3421 | The Syslog service – main add-on component, Syslog... |
| 2788 | 0.3420 | Table 1: Object Action Property Virtual Machine1 C... |
| 2789 | 0.3420 | Follow the steps to install Oracle Instant Client ... |
| 2790 | 0.3419 | No manual configurations are required. Review a fu... |
| 2791 | 0.3418 | Setting Recording Settings Configure custom locati... |
| 2792 | 0.3418 | This action is also logged when the admin or deleg... |
| 2793 | 0.3418 | Enable State-in-Time Data Collection If you want t... |
| 2794 | 0.3417 | CAUTION: Once you click UNINSTALL you cannot cance... |
| 2795 | 0.3417 | See the Assign Permission to Read the Registry Key... |
| 2796 | 0.3416 | The status is 200 OK. For XML, a response body con... |
| 2797 | 0.3414 | If you select to automatically configure audit in ... |
| 2798 | 0.3413 | v10.7 If you are using Netwrix Auditor for Network... |
| 2799 | 0.3413 | Users can also configure Only the latest snapshot ... |
| 2800 | 0.3412 | If an alerts is triggered a fter the UpdateInterva... |
| 2801 | 0.3411 | See this Knowledge Base article for more informati... |
| 2802 | 0.3410 | To specify a non-default port, provide a server na... |
| 2803 | 0.3410 | To specify a non-default port, provide a server na... |
| 2804 | 0.3409 | ◦ Provide this user name and password in the monit... |
| 2805 | 0.3409 | In the Schedule state-in-time data collection sect... |
| 2806 | 0.3409 | CertificateThumbprint NOCHECK Auditor Certificate ... |
| 2807 | 0.3408 | By default, it is set to "0" (decimal). Modify thi... |
| 2808 | 0.3407 | attempt) RacNumber=12&Arg1= Received AV Alert The ... |
| 2809 | 0.3407 | Step 7 – Enter Application ID and Application secr... |
| 2810 | 0.3406 | • To exclude the certain user's mailbox, enter use... |
| 2811 | 0.3405 | RECOMMENDED: Adjust retention period for the backu... |
| 2812 | 0.3404 | Table 1: Option Setting Rule Type Program Program ... |
| 2813 | 0.3404 | To Summary emails. In this case audit disable filt... |
| 2814 | 0.3403 | For SSRS-based reports - verify that SSRS (SQL Ser... |
| 2815 | 0.3402 | To obtain them, you will need an API Member accoun... |
| 2816 | 0.3401 | Max length: 21 HeaderText characters. Defines URL ... |
| 2817 | 0.3400 | Table 1: Data source Required rights and permissio... |
| 2818 | 0.3396 | v10.7 Option Description Auditor Server IP address... |
| 2819 | 0.3394 | Configure audit settings Do not select the checkbo... |
| 2820 | 0.3394 | v10.7 You can also create lists of specific file s... |
| 2821 | 0.3393 | Step 6 – Click OK to save the changes and close th... |
| 2822 | 0.3391 | By default, the Collect data for self-audit checkb... |
| 2823 | 0.3391 | Table 1: CorrelationTicketFormat Description Previ... |
| 2824 | 0.3390 | Use this report to see who has permissions to what... |
| 2825 | 0.3390 | Edit the template by deleting or inserting informa... |
| 2826 | 0.3389 | Allow outbound connections from the dynamic (1024 ... |
| 2827 | 0.3389 | Make sure to install the latest version. Step 2 – ... |
| 2828 | 0.3387 | v10.7 Parameter Default value Description naplanit... |
| 2829 | 0.3381 | Tip for reading the table: For example, on the com... |
| 2830 | 0.3381 | In the Schedule state-in-time data collection sect... |
| 2831 | 0.3381 | In the Schedule state-in-time data collection sect... |
| 2832 | 0.3381 | object=friendlyname Contains a list of human-reada... |
| 2833 | 0.3381 | Table 1: On... Ensure that... The Auditor server s... |
| 2834 | 0.3379 | Your notification policy can include any of them. ... |
| 2835 | 0.3379 | Configure Scope how to narrow your monitoring scop... |
| 2836 | 0.3378 | Another o ption is to install the add-on and Audit... |
| 2837 | 0.3377 | You can use a wildcard (*). For inclusive filters:... |
| 2838 | 0.3375 | Specify a file server Do not specify a default fil... |
| 2839 | 0.3375 | Supported editions are Enterprise, Standard and Ex... |
| 2840 | 0.3375 | See the Subscriptions topic for additional informa... |
| 2841 | 0.3375 | For example, backupsrv01.mydomain.local. Wildcards... |
| 2842 | 0.3375 | For example, backupsrv01.mydomain.local. Wildcards... |
| 2843 | 0.3375 | Specify the account for collecting data Group Mana... |
| 2844 | 0.3373 | Subscribe Subscription to the search results is no... |
| 2845 | 0.3373 | Reports are sent according to a specified schedule... |
| 2846 | 0.3373 | Review the following for a dditional information: ... |
| 2847 | 0.3372 | The body empty. contains Activity Records. 200 OK ... |
| 2848 | 0.3371 | Table 1: On... Ensure that... The Auditor side • A... |
| 2849 | 0.3370 | v10.7 Prerequisites Before running the add-on, ens... |
| 2850 | 0.3370 | For example, account.corp.lab Access Zone Enter th... |
| 2851 | 0.3369 | Do one of the following, depending on your Dell Is... |
| 2852 | 0.3366 | If enabled, a Compression Service will be automati... |
| 2853 | 0.3366 | If enabled, a Compression Service will be automati... |
| 2854 | 0.3366 | AlienVault USM 53 UDP/TCP Script host DNS Server D... |
| 2855 | 0.3365 | To add items right after finishing the monitoring ... |
| 2856 | 0.3364 | 44.. Hit the Save Auditing Settings button. Accoun... |
| 2857 | 0.3363 | Step 2 – If you are running VMware 6.0, connect to... |
| 2858 | 0.3363 | Unless specified, the add-on runs with the current... |
| 2859 | 0.3363 | ◦◦ The following advanced audit policy settings mu... |
| 2860 | 0.3363 | Follow the steps to define log on as a service pol... |
| 2861 | 0.3362 | object_type_name.propert y_name.attribute_name Con... |
| 2862 | 0.3362 | Only the lowest 9 bits of the calculation result a... |
| 2863 | 0.3359 | You can click Browse Specify syslog host or networ... |
| 2864 | 0.3359 | NetwrixAuditorPassword Current user credentials Un... |
| 2865 | 0.3356 | To review currently applied capabilities, you can ... |
| 2866 | 0.3355 | Requirements Installation If you are using previou... |
| 2867 | 0.3354 | If you select to automatically configure audit in ... |
| 2868 | 0.3352 | If a credential password for one of these accounts... |
| 2869 | 0.3351 | Allow outbound connections from the dynamic (1024 ... |
| 2870 | 0.3350 | • XML: <ActivityRecord><Action>Added</Action ><Mon... |
| 2871 | 0.3349 | Plan for the file servers and shares you want to a... |
| 2872 | 0.3348 | Apply a new service-policy to the SVM LIFs. Run th... |
| 2873 | 0.3347 | The following table lists actions that can be perf... |
| 2874 | 0.3346 | If a change seems unauthorized, or requires furthe... |
| 2875 | 0.3345 | See the Add Items for Monitoring topic for additio... |
| 2876 | 0.3342 | Program/script Input "Powershell.exe". Add a path ... |
| 2877 | 0.3341 | Prerequisites Before running the add-on, ensure th... |
| 2878 | 0.3340 | RacNumber=25&Arg1= • Rename / Renamed (Failed atte... |
| 2879 | 0.3340 | Step 2 – In the left pane, navigate to HKEY_LOCAL_... |
| 2880 | 0.3339 | See the Database SQL Language Reference for additi... |
| 2881 | 0.3339 | Table 1: Vserver Type Service Name Description Ena... |
| 2882 | 0.3339 | Permissions for Windows File Server Auditing Befor... |
| 2883 | 0.3338 | SharePoint Farm Complete the following fields: Opt... |
| 2884 | 0.3337 | Auditing of System zone is not supported. As state... |
| 2885 | 0.3336 | You can enable Auditor to continually enforce the ... |
| 2886 | 0.3336 | To adjust your Security event log size and retenti... |
| 2887 | 0.3335 | PauseWhenSendingFailed Pause after a failed attemp... |
| 2888 | 0.3332 | Alternatively, you can instruct Auditor not to sto... |
| 2889 | 0.3332 | If you have more than one Auditor Server running S... |
| 2890 | 0.3329 | In the list of servers, select the server you want... |
| 2891 | 0.3328 | In this case audit data is still being collected. ... |
| 2892 | 0.3327 | Requirements Installation If you are using previou... |
| 2893 | 0.3326 | Use other options (Computer, IP range to specify t... |
| 2894 | 0.3326 | Use other options (Computer, IP range to specify t... |
| 2895 | 0.3326 | Use other options (Computer, IP range to specify t... |
| 2896 | 0.3326 | Use other options (Computer, IP range to specify t... |
| 2897 | 0.3325 | Add Items for Monitoring Once you completed monito... |
| 2898 | 0.3324 | If an alerts is triggered a fter the UpdateInterva... |
| 2899 | 0.3323 | Do one of the following, depending on your Dell Is... |
| 2900 | 0.3323 | Select the account that will be used to collect da... |
| 2901 | 0.3323 | Select the account that will be used to collect da... |
| 2902 | 0.3322 | Select one of the following options: Table 1: Opti... |
| 2903 | 0.3322 | If you have an on-premises Exchange server 2019, 2... |
| 2904 | 0.3322 | Check the password for this account. v10.7 NOTE: Y... |
| 2905 | 0.3321 | You are trying to connect to a remote Auditor spec... |
| 2906 | 0.3321 | Table 2: Option Description General Specify ShareP... |
| 2907 | 0.3321 | Table 1: Option Description Auditor Endpoint Audit... |
| 2908 | 0.3321 | Table 1: Option Description Auditor Endpoint Audit... |
| 2909 | 0.3321 | See the Prerequisites and Audit Database topics fo... |
| 2910 | 0.3320 | Later, you can always create custom report from in... |
| 2911 | 0.3319 | At least the first script run should be performed ... |
| 2912 | 0.3319 | At least the first script run should be performed ... |
| 2913 | 0.3319 | At least the first script run should be performed ... |
| 2914 | 0.3319 | Port Protocol Source Target Purpose For a full lis... |
| 2915 | 0.3319 | Step 1 – On the main Auditor page, click the Alert... |
| 2916 | 0.3319 | This role is also granted to service accounts or a... |
| 2917 | 0.3318 | On the ServiceNow side ServiceNow version should b... |
| 2918 | 0.3318 | Defines the Audit Database connection timeout (in ... |
| 2919 | 0.3317 | Click Examine. Table 1: Option Description Default... |
| 2920 | 0.3316 | By default, each v10.7 monitoring plan will use a ... |
| 2921 | 0.3316 | v10.7 Account Lockout Examiner Overview Netwrix Ac... |
| 2922 | 0.3315 | Otherwise, reports will contain limited data and w... |
| 2923 | 0.3315 | See the Prerequisites and Audit Database topics fo... |
| 2924 | 0.3315 | Unless specified, the script runs with the current... |
| 2925 | 0.3314 | Send a POST request containing Continuation mark t... |
| 2926 | 0.3313 | Prerequisites Before running the add-on, ensure th... |
| 2927 | 0.3312 | Change and activity reports—System-specific report... |
| 2928 | 0.3312 | Select the account that will be used to collect da... |
| 2929 | 0.3311 | During the initial data collection, the product au... |
| 2930 | 0.3310 | All Internet Explorer-related settings are relevan... |
| 2931 | 0.3310 | Modify plan settings, add or delete data sources, ... |
| 2932 | 0.3309 | Add a Data Source to an Existing Plan Follow the s... |
| 2933 | 0.3307 | Other federation servers you add to the farm will ... |
| 2934 | 0.3307 | Step 4 – In the left pane, select Containers and C... |
| 2935 | 0.3306 | To enable the policy 1. On the audited server, ope... |
| 2936 | 0.3304 | You can automate this process, as described in the... |
| 2937 | 0.3304 | The latter ones are listed in the table below. Fil... |
| 2938 | 0.3303 | v10.7 Step 4 – Double-click the searchFlags attrib... |
| 2939 | 0.3302 | Also, it lists requirements for the accounts used ... |
| 2940 | 0.3301 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 2941 | 0.3301 | The changes include creation, modifica tion, delet... |
| 2942 | 0.3301 | Additional Configuration to Review Changes Made vi... |
| 2943 | 0.3301 | Detect additional details Specify additional infor... |
| 2944 | 0.3300 | An originating worksta tion from which the change ... |
| 2945 | 0.3300 | Subscribe Create subscription for periodic deliver... |
| 2946 | 0.3299 | For example, to exclude inf ormation about databas... |
| 2947 | 0.3298 | The list of Exchange object classes is version-dep... |
| 2948 | 0.3297 | Specify Windows file share Do not specify a defaul... |
| 2949 | 0.3297 | Then you will provide this account in the monitori... |
| 2950 | 0.3294 | Monitoring plan configuration List folders + + + +... |
| 2951 | 0.3294 | To collect activity data, the account must have at... |
| 2952 | 0.3292 | v10.7 Database name Description Intended for integ... |
| 2953 | 0.3292 | By default, add-ons are configured to accept all c... |
| 2954 | 0.3290 | When configuring the IncludeDataSourceToMakeEventI... |
| 2955 | 0.3290 | Audited domain Specify domain name in the FQDN for... |
| 2956 | 0.3289 | See the View Reports topic for additional informat... |
| 2957 | 0.3288 | Alternatively, you can grant the Global administra... |
| 2958 | 0.3288 | Alternatively, you can grant the Global administra... |
| 2959 | 0.3287 | RacNumber=31&Arg1= Request='GET /cgi-bin/ Read / R... |
| 2960 | 0.3285 | Execute the command... TRIGGER,DROP TRIGGER,CREATE... |
| 2961 | 0.3285 | For example, if you selected Services, the program... |
| 2962 | 0.3284 | See the Prerequisites and Audit Database topics fo... |
| 2963 | 0.3284 | See the Add Items for Monitoring topic for additio... |
| 2964 | 0.3283 | Only the lowest 9 bits of the calculation result a... |
| 2965 | 0.3283 | The machine where the add-on will be installed .NE... |
| 2966 | 0.3283 | Step 5 – Review the <CorrelationTicketFormat> sect... |
| 2967 | 0.3282 | See the Subscriptions topic for additional informa... |
| 2968 | 0.3282 | This app will allow you to collect both activity a... |
| 2969 | 0.3276 | I do not receive any results while searching audit... |
| 2970 | 0.3275 | For details, see Manage historical snapshots optio... |
| 2971 | 0.3274 | Table 1: Action Object Type Attributes Interactive... |
| 2972 | 0.3273 | VMware vCenter or ESX(i) host ◦◦ VMware events tha... |
| 2973 | 0.3271 | File Servers State-In-Time Reports This section co... |
| 2974 | 0.3270 | Object type:property: When a new object is added, ... |
| 2975 | 0.3269 | *) v10.7 This refers to the following keys: HKEY_L... |
| 2976 | 0.3269 | Table 1: Option Value Action Set to "Start a progr... |
| 2977 | 0.3269 | Version Related documentation Clustered Data ONTAP... |
| 2978 | 0.3267 | Otherwise, reports will contain limited data and w... |
| 2979 | 0.3267 | This can be helpful when Auditor detects many acti... |
| 2980 | 0.3266 | BatchTimeOut Defines batch writing timeout (in sec... |
| 2981 | 0.3266 | If the Pager property of an AD User contains a ful... |
| 2982 | 0.3266 | To set up a response action, this account must als... |
| 2983 | 0.3265 | Select a plan and click Edit. On the page that ope... |
| 2984 | 0.3265 | Monitoring plan Select to display events from one ... |
| 2985 | 0.3264 | For example: OracleUser as sysdba Step 3 – Enter y... |
| 2986 | 0.3264 | Find the Group Policy Object (GPO) that is applied... |
| 2987 | 0.3263 | Enable network traffic compression If selected, th... |
| 2988 | 0.3263 | Table 1: Port Protocol Source Target Purpose 8080 ... |
| 2989 | 0.3262 | The image is also configured to use Microsoft Edge... |
| 2990 | 0.3262 | Success. The body contains Activity Records. Activ... |
| 2991 | 0.3262 | autoDetect Set to False. Step 5 – Start the Audito... |
| 2992 | 0.3260 | See the Create a New Monitoring Plan topic for add... |
| 2993 | 0.3259 | If you audit multiple servers, you may want to cre... |
| 2994 | 0.3258 | Option Setting Rule Type Program Specify the path ... |
| 2995 | 0.3257 | to the Auditor Home screen to access them instantl... |
| 2996 | 0.3257 | The requested endpoint does not exist (e.g., / net... |
| 2997 | 0.3256 | These settings cannot be modified for a certain pl... |
| 2998 | 0.3256 | So, you should register an Microsoft Entra ID app ... |
| 2999 | 0.3256 | v10.7 Favorites Sub-Folder Options Favorites > [Re... |
| 3000 | 0.3255 | You can select both Active Directory and Logon Act... |
| 3001 | 0.3255 | Move the selected snapshots to the Snapshots avail... |
| 3002 | 0.3254 | 126"} Retrieves all activity records where adminis... |
| 3003 | 0.3254 | * .msExchEdgeSyncCredent ial .msExchMailboxMoveTar... |
| 3004 | 0.3252 | Exchange_Server.Adminis trativeGroup Exchange_Serv... |
| 3005 | 0.3252 | See the Notifications topic for additional informa... |
| 3006 | 0.3251 | The Auditor Server side The TCP 9699 port (default... |
| 3007 | 0.3250 | • XML: <ActivityRecord><Action>Modified</Acti on><... |
| 3008 | 0.3249 | The entry may also include a modifier—a match type... |
| 3009 | 0.3247 | In the dialog that opens, specify the groups that ... |
| 3010 | 0.3247 | Configure audit settings You can adjust audit sett... |
| 3011 | 0.3247 | Configure audit settings You can adjust audit sett... |
| 3012 | 0.3247 | Configure audit settings You can adjust audit sett... |
| 3013 | 0.3247 | Configure audit settings You can adjust audit sett... |
| 3014 | 0.3246 | Only the lowest 9 bits of the calculation result a... |
| 3015 | 0.3246 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Amazon_Web_S... |
| 3016 | 0.3245 | v10.7 Option Description Enabling this option on p... |
| 3017 | 0.3245 | AB:BB:CC—Check Auditor Server certificat e thumbpr... |
| 3018 | 0.3245 | AB:BB:CC—Check Auditor Server certificat e thumbpr... |
| 3019 | 0.3243 | Then you will provide this account in the monitori... |
| 3020 | 0.3243 | Select the Security tab and click Advanced. In the... |
| 3021 | 0.3242 | Connect to your SonicWall device. Launch an Intern... |
| 3022 | 0.3242 | By default, the report includes data obtained duri... |
| 3023 | 0.3242 | By default, the report includes data obtained duri... |
| 3024 | 0.3242 | fields. The DetailList field is not mandatory, it ... |
| 3025 | 0.3241 | Unless specified, the script runs with the current... |
| 3026 | 0.3240 | Action Type – select what types of a ctions perfor... |
| 3027 | 0.3240 | In the response, locate the uuids of the target fo... |
| 3028 | 0.3239 | REPORTS Access the predefined reports for each dat... |
| 3029 | 0.3239 | In the dialog appears, select Create new address o... |
| 3030 | 0.3238 | Table 1: Parameter Description Company Organizatio... |
| 3031 | 0.3237 | Application that initiated the activity — enter th... |
| 3032 | 0.3236 | You can delegate control over a monitoring plan to... |
| 3033 | 0.3235 | Select the account that will be used to collect da... |
| 3034 | 0.3235 | You may have insufficient permissions. Contact you... |
| 3035 | 0.3234 | Step 1 – Connect to your PaloAlto device: launch a... |
| 3036 | 0.3233 | DOMAIN\username agentomitusers.txt This file conta... |
| 3037 | 0.3232 | See the Configure Local Audit Policies topic and t... |
| 3038 | 0.3232 | To do so, perform the following steps: Step 1 – Go... |
| 3039 | 0.3232 | By default, data is imported to a specially create... |
| 3040 | 0.3231 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 3041 | 0.3231 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 3042 | 0.3230 | Also view historical reviews. My Reviews tab Direc... |
| 3043 | 0.3230 | Add a path to the add-on in double quotes and spec... |
| 3044 | 0.3228 | By default, the report includes data obtained duri... |
| 3045 | 0.3228 | Configure audit settings You can adjust audit sett... |
| 3046 | 0.3225 | See the Microsoft Entra ID topic for additional in... |
| 3047 | 0.3225 | v10.7 Option Setting Rule Type Program Specify the... |
| 3048 | 0.3223 | When auditing file servers, changes to both access... |
| 3049 | 0.3223 | To modify the timeframe, use the drop-down list in... |
| 3050 | 0.3222 | In the Auditing Entry dialog, click the Select a p... |
| 3051 | 0.3222 | In the Auditing Entry dialog, click the Select a p... |
| 3052 | 0.3222 | See the Prerequisites and Audit Database topics fo... |
| 3053 | 0.3221 | Availability group name Enter a name of your SQL S... |
| 3054 | 0.3221 | Step 2 – Type a path to the add-on. Or simply drag... |
| 3055 | 0.3219 | ◦◦ On the Auditor console computer: If you have en... |
| 3056 | 0.3219 | ◦◦ On the Auditor console computer: If you have en... |
| 3057 | 0.3219 | Possible parameter values: • True — generate uniqu... |
| 3058 | 0.3218 | Follow the steps to enable object-level auditing f... |
| 3059 | 0.3218 | Investigate incidents by running interactive searc... |
| 3060 | 0.3217 | Select this checkbox if the implicit SSL mode is u... |
| 3061 | 0.3216 | Allow outbound connections to remote ports on the ... |
| 3062 | 0.3216 | Set up the auditing as described in Planning and P... |
| 3063 | 0.3216 | Endure that image file is located in the default d... |
| 3064 | 0.3215 | If you have not specified the default settings bef... |
| 3065 | 0.3215 | Server instance, use * for all servers Audit data,... |
| 3066 | 0.3214 | Are there any files likely to contain credentials,... |
| 3067 | 0.3214 | OneDrive for Business changes are reported as Shar... |
| 3068 | 0.3212 | When configuring the IncludeDataSourceToMakeEventI... |
| 3069 | 0.3210 | It instructs Netwrix Auditor to In group Domain\Ad... |
| 3070 | 0.3210 | Collect data for state-in-time reports Configure A... |
| 3071 | 0.3209 | Step 3 – In the With parameters field, enter the p... |
| 3072 | 0.3209 | v10.7 String Description String5 The GUID of the m... |
| 3073 | 0.3209 | Create and Register a New App in Microsoft Entra I... |
| 3074 | 0.3209 | Create and Register a New App in Microsoft Entra I... |
| 3075 | 0.3209 | Create and Register a New App in Microsoft Entra I... |
| 3076 | 0.3207 | Reason: Computer Reason type System state changed ... |
| 3077 | 0.3206 | Subscription emails may vary slightly depending on... |
| 3078 | 0.3205 | Specify the recipients who will receive daily a ct... |
| 3079 | 0.3204 | Each parameter is preceded with a dash; a space se... |
| 3080 | 0.3203 | On the Name step, specify the rule's name, for exa... |
| 3081 | 0.3202 | By default, the LongTerm Archive (repository) and ... |
| 3082 | 0.3201 | Data communication is performed using TCP protocol... |
| 3083 | 0.3200 | By default, this email is generated daily at 7:00 ... |
| 3084 | 0.3200 | The state-in-time reports are available under the ... |
| 3085 | 0.3200 | For example: ,,CORP\\jsmith,*,*, Monitoring plan n... |
| 3086 | 0.3200 | Port Protocol Source Target Purpose Exchange Onlin... |
| 3087 | 0.3199 | Example: winsrv2016-01.mydomain.local. • Setting c... |
| 3088 | 0.3199 | However, you can adjust them manually, using the i... |
| 3089 | 0.3199 | If you also want to audit changes to AD configurat... |
| 3090 | 0.3199 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3091 | 0.3198 | Table 1: Option Description Applications Specify a... |
| 3092 | 0.3197 | Configure Windows Registry Audit Settings Windows ... |
| 3093 | 0.3197 | To check this, start the Group Policy Management c... |
| 3094 | 0.3195 | The list contains computer name, its current statu... |
| 3095 | 0.3195 | Table 1: Object type Action What Description User ... |
| 3096 | 0.3194 | Contact your virtual infrastructure administrator ... |
| 3097 | 0.3194 | For production deployment planning in bigger envir... |
| 3098 | 0.3194 | If you set the In group condition for Who filter t... |
| 3099 | 0.3194 | Step 2 – Navigate to Security Settings > Local Pol... |
| 3100 | 0.3193 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 3101 | 0.3193 | See also: Enterprise Overview Dashboard All Activi... |
| 3102 | 0.3193 | Note that the new monitoring scope restrictions ap... |
| 3103 | 0.3193 | Some data sources require additional system compon... |
| 3104 | 0.3192 | RacNumber=16&Arg1= • Remove / Removed (Failed atte... |
| 3105 | 0.3192 | v10.7 Domain Complete the following fields: Option... |
| 3106 | 0.3191 | How Risk Levels Are Estimated As mentioned, dashbo... |
| 3107 | 0.3191 | Possible deployment options are as follows (here i... |
| 3108 | 0.3191 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 3109 | 0.3190 | If enabled, a Compression Service will be automati... |
| 3110 | 0.3187 | Prepare a machine for Microsoft SQL Server meeting... |
| 3111 | 0.3187 | You can enable network traffic compression. If Spe... |
| 3112 | 0.3186 | It displays currently triggered alerts with detail... |
| 3113 | 0.3185 | • For subscription to risk assessment overview —Se... |
| 3114 | 0.3185 | v10.7 Option Description audit data. Note that the... |
| 3115 | 0.3183 | • Advanced permissions: ◦ Create files / write dat... |
| 3116 | 0.3183 | Table 2: Windows File Server Dell Data storage Net... |
| 3117 | 0.3182 | If any conflicts are detected with your current au... |
| 3118 | 0.3182 | See the s ection below for special considerations.... |
| 3119 | 0.3181 | 44.. Configure the following audit policies. Polic... |
| 3120 | 0.3180 | v10.7 Notes for Managed Service Providers Being a ... |
| 3121 | 0.3178 | The string descriptions for 10 actFolderMoveCopy S... |
| 3122 | 0.3178 | For that, the user account will need an administra... |
| 3123 | 0.3177 | Step 3 – Click Edit data source on the right. Step... |
| 3124 | 0.3176 | Table 1: On... Ensure that... The Auditor server s... |
| 3125 | 0.3176 | For the purpose of the Access Reviewsapplication, ... |
| 3126 | 0.3175 | v10.7 Configuring Microsoft Entra ID App for Audit... |
| 3127 | 0.3175 | If enabled, a Compression Service will be automati... |
| 3128 | 0.3173 | The IT risks are grouped into the following catego... |
| 3129 | 0.3172 | See the Configure Advanced Audit Policies topic fo... |
| 3130 | 0.3170 | Remember that replication of namespace roots is no... |
| 3131 | 0.3169 | On the computer where your database is deployed, r... |
| 3132 | 0.3168 | 22.. Connect to your Oracle Database—use Oracle ac... |
| 3133 | 0.3168 | Under Permissions, select all checkboxes except th... |
| 3134 | 0.3167 | Step 8 – Review sample tnsnames.ora file where myO... |
| 3135 | 0.3167 | Specify what types of logon events you want to mon... |
| 3136 | 0.3165 | Group Managed Service Account (gMSA). You should s... |
| 3137 | 0.3164 | Step 2 – If some issues occurred due to the lack o... |
| 3138 | 0.3164 | Mailboxes: UserMailbox SharedMailbox EquipmentMail... |
| 3139 | 0.3161 | You can specify a custom account only for the Long... |
| 3140 | 0.3160 | v10.7 Apply a gMSA as a Data Collecting Account Ap... |
| 3141 | 0.3160 | Your current audit settings will be checked on eac... |
| 3142 | 0.3159 | On domain controllers in your domain (target), all... |
| 3143 | 0.3159 | Failed change attempts The Auditing Entry below sh... |
| 3144 | 0.3158 | If any conflicts are detected with your current au... |
| 3145 | 0.3158 | Trailing comma is not supported. Table 1: Method E... |
| 3146 | 0.3156 | See the Audit Configuration Assistant topic for in... |
| 3147 | 0.3156 | To execute commands in the context of Cluster, add... |
| 3148 | 0.3156 | See the Permissions for Microsoft Entra ID Auditin... |
| 3149 | 0.3155 | Step 2 – Go to Manage > API permissions and click ... |
| 3150 | 0.3154 | Source Specify this parameter if you want to save ... |
| 3151 | 0.3154 | Users not included in this list will not be notifi... |
| 3152 | 0.3154 | The following operations will be audited: "FILE_RE... |
| 3153 | 0.3153 | See the Reported Attributes topic for more informa... |
| 3154 | 0.3151 | Under Permissions, select all checkboxes except th... |
| 3155 | 0.3151 | To be able to audit and report v10.7 who made thos... |
| 3156 | 0.3150 | Table 1: Auditing Entry Successful reads The Audit... |
| 3157 | 0.3150 | Logons Cause (for failed attempts) Successful logo... |
| 3158 | 0.3150 | You can, for example, open any SSRS-based report u... |
| 3159 | 0.3149 | If you want to use a specific account (other than ... |
| 3160 | 0.3148 | When you restore deleted accounts with the Netwrix... |
| 3161 | 0.3147 | Authentication Select the authentication type you ... |
| 3162 | 0.3147 | As a next step, click Add item to specify an objec... |
| 3163 | 0.3147 | See the Compliance Reports topic for additional in... |
| 3164 | 0.3145 | Step 3 – In the Windows Firewall with Advanced Sec... |
| 3165 | 0.3144 | Configuring Windows registry audit settings on Win... |
| 3166 | 0.3141 | If you want to generate reports based on differen ... |
| 3167 | 0.3139 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 3168 | 0.3137 | Table 1: Option Description General Specify Dell V... |
| 3169 | 0.3136 | See the Audit Database topic for additional inform... |
| 3170 | 0.3135 | Use them to create the lists of specific objects t... |
| 3171 | 0.3134 | A Security Officer wants to monitor a file share, ... |
| 3172 | 0.3134 | For XML audit trail: Only ALTER actions will be re... |
| 3173 | 0.3133 | ◦◦ If your file shares are stored within one folde... |
| 3174 | 0.3132 | If you have an on-premises Exchange server in your... |
| 3175 | 0.3132 | If enabled, a Compression Service will be automati... |
| 3176 | 0.3132 | If enabled, a Compression Service will be automati... |
| 3177 | 0.3132 | Step 2 – Define operational parameters such as Aud... |
| 3178 | 0.3132 | For example, your network adapter configuration ch... |
| 3179 | 0.3131 | Every time you run a script, Auditor makes a check... |
| 3180 | 0.3130 | If you want to monitor userv10.7 Data Source Item ... |
| 3181 | 0.3129 | Select the data source you need (for example, Acti... |
| 3182 | 0.3128 | Add-On Parameters To configure the add-on paramete... |
| 3183 | 0.3128 | Check the required audit settings in your monitore... |
| 3184 | 0.3128 | The message indicates to the recipient who the Tab... |
| 3185 | 0.3126 | Specify additional information to include in repor... |
| 3186 | 0.3126 | Specify additional information to include in repor... |
| 3187 | 0.3125 | Clicking a Role link opens the detailed report on ... |
| 3188 | 0.3125 | *) HKEY_LOCAL_MACHINE\SYSTEM\CurrentContro lSet\Se... |
| 3189 | 0.3124 | Under Log/Monitoring, expand the User Access link.... |
| 3190 | 0.3123 | Step 4 – Depending on your monitoring requirements... |
| 3191 | 0.3122 | Domain Complete the following fields: Option Descr... |
| 3192 | 0.3120 | The add-on will only collect and process events yo... |
| 3193 | 0.3120 | • Starting with add-on build 1.0.12.0, TLS 1.2 pro... |
| 3194 | 0.3119 | Creating and registering a new app in Microsoft En... |
| 3195 | 0.3119 | AD Container I want to exclude specific computers ... |
| 3196 | 0.3119 | Enter the account's password in both the Password ... |
| 3197 | 0.3116 | See the Configure the Back up Files and Directorie... |
| 3198 | 0.3116 | If you use the following combination of the audit ... |
| 3199 | 0.3115 | Supported Browsers Supported browsers for the Acce... |
| 3200 | 0.3114 | The Event Fields tab Event ID Enter the identifier... |
| 3201 | 0.3113 | It has dbo access to the configuration database. F... |
| 3202 | 0.3111 | See the RoleBased Access and Delegation topic for ... |
| 3203 | 0.3111 | Table 1: Option Description Consider the following... |
| 3204 | 0.3110 | See the Configure Client Secret topic for addition... |
| 3205 | 0.3109 | v10.7 For evaluation and PoC projects you can depl... |
| 3206 | 0.3108 | In group This operator relates to the Who filter. ... |
| 3207 | 0.3107 | Make sure to copy and save the API key in a secure... |
| 3208 | 0.3105 | You can also create lists of specific file shares ... |
| 3209 | 0.3104 | Request Error details returned 400 Bad Request Inv... |
| 3210 | 0.3104 | Your current audit settings will be checked on eac... |
| 3211 | 0.3104 | Your current audit settings will be checked on eac... |
| 3212 | 0.3104 | Remember, a “resource” refers to the file system s... |
| 3213 | 0.3103 | Configure Scope You can narrow your monitoring sco... |
| 3214 | 0.3103 | The score, that is between 1 and 100 points, refle... |
| 3215 | 0.3103 | Use an existing SQL Server instance — select this ... |
| 3216 | 0.3103 | Advanced filters to make your results context matc... |
| 3217 | 0.3103 | ), shares Table 1: Option Description used by prin... |
| 3218 | 0.3103 | See Assigning 'System Administrator' Role section ... |
| 3219 | 0.3102 | Table 1: Add-on Port Protocol Source Target Purpos... |
| 3220 | 0.3102 | Configure Message Forwarding for Nutanix Prism To ... |
| 3221 | 0.3101 | Step 3 – In the Remote Registry Properties dialog ... |
| 3222 | 0.3101 | Table 2: Port Protocol Source Target Purpose 389 T... |
| 3223 | 0.3101 | Step 1 – Open the monitored item properties for ed... |
| 3224 | 0.3100 | The procedure below explains how to configure redi... |
| 3225 | 0.3100 | See the Integration API topic for additional infor... |
| 3226 | 0.3100 | Use the server_name\instance_name format, for exam... |
| 3227 | 0.3099 | Then click OK to confirm. Assigned resource owners... |
| 3228 | 0.3099 | Configure Scope You can narrow your monitoring sco... |
| 3229 | 0.3097 | NOTE: This covers all the required permissions bel... |
| 3230 | 0.3096 | If you set the In group condition for This operato... |
| 3231 | 0.3096 | Table 1: Option Value Add arguments (optional) Add... |
| 3232 | 0.3095 | ForNDC Endpoint Provider: Browse your data with Ne... |
| 3233 | 0.3095 | Event Collection Provide UNC path to a file server... |
| 3234 | 0.3094 | Assign Permission Via the Registry Editor Snap-in ... |
| 3235 | 0.3094 | Step 7 – Click Show advanced permissions and selec... |
| 3236 | 0.3093 | See the Create and Register a New App in Microsoft... |
| 3237 | 0.3093 | The option is Enforce certificate validation to en... |
| 3238 | 0.3092 | Make sure the account has sufficient permissions t... |
| 3239 | 0.3092 | Step 2 – In the upper-left of your site collection... |
| 3240 | 0.3091 | Step 4 – On the General tab, click Configure next ... |
| 3241 | 0.3091 | Set the TNS_ADMIN environment variable to the dire... |
| 3242 | 0.3091 | Deployment Scenarios The add-on can be deployed on... |
| 3243 | 0.3090 | All reviews will be visible on the Entitlement Rev... |
| 3244 | 0.3089 | If you have multiple Auditor servers, you can spec... |
| 3245 | 0.3089 | Account for Accessing REST API You will also need ... |
| 3246 | 0.3089 | v10.7 Assign Permission via the Registry Editor Sn... |
| 3247 | 0.3089 | Specify the account for collecting data Select the... |
| 3248 | 0.3089 | Specify the account for collecting data Select the... |
| 3249 | 0.3089 | Note that the new monitoring scope restrictions ap... |
| 3250 | 0.3088 | Step 6 – For auditing Logon Activity, you also nee... |
| 3251 | 0.3088 | NOTE: For Microsoft Entra ID, only the current dat... |
| 3252 | 0.3087 | The user must have sufficient v10.7 Step 2 – Defin... |
| 3253 | 0.3086 | On the main Auditor page, navigate to Behavior Sub... |
| 3254 | 0.3086 | See the Monitoring Planstopic for additional infor... |
| 3255 | 0.3085 | See the SQL Server Reporting Services topic for ad... |
| 3256 | 0.3085 | • Check "Successful" and "Failed" next to List fol... |
| 3257 | 0.3084 | You can enable network traffic compression. If ena... |
| 3258 | 0.3084 | You can enable network traffic compression. If ena... |
| 3259 | 0.3084 | The account used for data collection must meet the... |
| 3260 | 0.3083 | Review the following for additional information: T... |
| 3261 | 0.3083 | Complete the following fields: Option Description ... |
| 3262 | 0.3082 | • Advanced permissions—SelectList folder / read da... |
| 3263 | 0.3082 | description %AlertDescription% %PreviousTicketRefe... |
| 3264 | 0.3078 | • Applies to—Set to"Files only". • Advanced permis... |
| 3265 | 0.3078 | Step 4 – Hit Enter. Depending on the number of Act... |
| 3266 | 0.3077 | ALTER SYSTEM SET audit_trail=DB SCOPE=SPFILE; Stor... |
| 3267 | 0.3077 | Table 2: XML <?xml version="1.0" encoding="utf-8"?... |
| 3268 | 0.3076 | For example, you had a monitoring plan corp.local ... |
| 3269 | 0.3076 | By default, new. To specify another status, provid... |
| 3270 | 0.3075 | Network Devices NOTE: Prior to configuring your mo... |
| 3271 | 0.3074 | For details about metrics calculation, see How Ris... |
| 3272 | 0.3072 | Thus, only the latest snapshot is available for on... |
| 3273 | 0.3072 | How owners should log into the application console... |
| 3274 | 0.3071 | For example, you had a monitoring plan corp.local ... |
| 3275 | 0.3070 | Step 10 – Assign a less-privileged role to this ac... |
| 3276 | 0.3069 | See the Reports topic for additional information. ... |
| 3277 | 0.3069 | Make sure that theOnly apply these auditing settin... |
| 3278 | 0.3067 | Only one usage of each socket address (protocol/ne... |
| 3279 | 0.3066 | Thus, the account should be a member of the follow... |
| 3280 | 0.3065 | Failed read attempts Table 1: Auditing Entry The A... |
| 3281 | 0.3064 | audit_sys_operations=TRUE SCOPE=SPFILE; Table 1: S... |
| 3282 | 0.3062 | By the way of example, this section provides instr... |
| 3283 | 0.3061 | Step 9 – Repeat the steps 4-8 for keys below: HKEY... |
| 3284 | 0.3061 | Table 2: Option Description v10.7 Options Descript... |
| 3285 | 0.3061 | See the Data Collecting Account topic for User/Pas... |
| 3286 | 0.3061 | Optionally, you can select Download to edit the ma... |
| 3287 | 0.3060 | See the Change and Activity Reports topic for addi... |
| 3288 | 0.3059 | For more details about gMSA usage, see the Use Gro... |
| 3289 | 0.3059 | For more details about gMSA usage, see the Use Gro... |
| 3290 | 0.3058 | Table 1: Option Value Action Set to "Start a progr... |
| 3291 | 0.3058 | See the Configuring client secret topic for additi... |
| 3292 | 0.3058 | Step 5 – Expand Directory role and select the role... |
| 3293 | 0.3058 | Step 5 – Expand Directory role and select the role... |
| 3294 | 0.3058 | Ensure that... The Auditor server side • Auditor v... |
| 3295 | 0.3057 | Configure a threshold-based alert, email recipient... |
| 3296 | 0.3057 | For example: *,,CORP\\jsmith,*,*, omitstorelist.tx... |
| 3297 | 0.3057 | Table 1: Audit subcategory Command Security Group ... |
| 3298 | 0.3056 | This account should have sufficient REST API privi... |
| 3299 | 0.3055 | Step 4 – Right-click the newly created GPO and sel... |
| 3300 | 0.3053 | Table 1: Auditing Entry Failed change attempts The... |
| 3301 | 0.3053 | severity 1 Sets Severity to "1 – High". v10.7 <Con... |
| 3302 | 0.3052 | -InboxRule, -MailboxAutoReplyConfiguration, SetMai... |
| 3303 | 0.3052 | After No ntext The new value of the modified prope... |
| 3304 | 0.3051 | Exclude—Add users to be excluded from the auditing... |
| 3305 | 0.3051 | Example: System Properties*. You can use a wildcar... |
| 3306 | 0.3051 | Example: System Properties*. You can use a wildcar... |
| 3307 | 0.3051 | v10.7 Option Description Create rules for objects ... |
| 3308 | 0.3050 | This significantly improves data transfer and mini... |
| 3309 | 0.3050 | This significantly improves data transfer and mini... |
| 3310 | 0.3049 | Table 1: Hardware component Requirement Processor ... |
| 3311 | 0.3048 | Unless specified, the add-on runs with the current... |
| 3312 | 0.3048 | Perform the following procedures to configure obje... |
| 3313 | 0.3047 | On the computer where Auditor Server is installed:... |
| 3314 | 0.3046 | Logging facility Leave empty. v10.7 # logging secu... |
| 3315 | 0.3045 | • PowerShell connections: ◦ 5985 - for HTTP ◦ 5986... |
| 3316 | 0.3044 | It is recommended to assign the API Member Connect... |
| 3317 | 0.3044 | Step 2 – On the Alert Properties step, specify the... |
| 3318 | 0.3043 | Do not specify a default file share mapped to a lo... |
| 3319 | 0.3043 | Failed change attempts The Auditing Entry below sh... |
| 3320 | 0.3043 | To create a filter for user activity monitoring, s... |
| 3321 | 0.3043 | See the Create Alerts topic for additional informa... |
| 3322 | 0.3043 | Server — Enter the database server hostname (NetBI... |
| 3323 | 0.3042 | (See the Microsoft Placing fi les directly in the ... |
| 3324 | 0.3041 | For that, in the Manage historical snapshots secti... |
| 3325 | 0.3040 | See the Data Collecting Account topic for addition... |
| 3326 | 0.3039 | Collect data for state-in-time reports When auditi... |
| 3327 | 0.3038 | Major benefit of the integrated solution implement... |
| 3328 | 0.3038 | Click Change to browse for a different location. W... |
| 3329 | 0.3036 | PaloAlto Devices Auditor supports monitoring the f... |
| 3330 | 0.3036 | This file contains a list of users who must be exc... |
| 3331 | 0.3036 | Multiple occurrences of a ction sets may indicate ... |
| 3332 | 0.3034 | Netwrix encrypts data with a self-signed automatic... |
| 3333 | 0.3033 | Otherwise, the addon will not be able to write dat... |
| 3334 | 0.3033 | Otherwise, the addon will not be able to write dat... |
| 3335 | 0.3033 | For that, you need to set the Network Security: Re... |
| 3336 | 0.3032 | The Browser role is required to generate reports. ... |
| 3337 | 0.3032 | To control who does what in the IT infrastructure ... |
| 3338 | 0.3032 | If you set the Not in group Not in group This oper... |
| 3339 | 0.3031 | Configure console access, Active Directory service... |
| 3340 | 0.3031 | Execute... Database audit trail (default setting) ... |
| 3341 | 0.3028 | Step 1 – In Auditor, navigate to Search. Step 2 – ... |
| 3342 | 0.3027 | By default, Personal. ◦ thumbprint—Mandatory, defi... |
| 3343 | 0.3024 | Starting with add-on build 1.0.12.0, TLS 1.2 proto... |
| 3344 | 0.3024 | initiato r's account) as System. Network Protocol*... |
| 3345 | 0.3023 | property name Contains a list of objects to be and... |
| 3346 | 0.3023 | Configure Data Collecting Account, as described in... |
| 3347 | 0.3023 | Move the selected snapshots to the Snapshots avail... |
| 3348 | 0.3023 | Move the selected snapshots to the Snapshots avail... |
| 3349 | 0.3023 | Move the selected snapshots to the Snapshots avail... |
| 3350 | 0.3022 | Review the following Microsoft technical a rticle ... |
| 3351 | 0.3022 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3352 | 0.3021 | Select this checkbox to write data to a SQL Server... |
| 3353 | 0.3020 | See the Reported Attributes topic below for more i... |
| 3354 | 0.3019 | You can also create a subscription to any report y... |
| 3355 | 0.3018 | Step 2 – Log in to your cluster as a root user. Ta... |
| 3356 | 0.3018 | Specify the account for collecting data Select the... |
| 3357 | 0.3018 | Specify the account for collecting data Select the... |
| 3358 | 0.3018 | Specify the account for collecting data Select the... |
| 3359 | 0.3018 | Specify the account for collecting data Select the... |
| 3360 | 0.3017 | • Applies to—Set to "Files only". • Advanced permi... |
| 3361 | 0.3017 | Each data collecting accounts should meet the requ... |
| 3362 | 0.3016 | 14 actFolderCreated String9 The new folder URL v10... |
| 3363 | 0.3016 | To track the copy action, enable successful read a... |
| 3364 | 0.3014 | Try modifying your search. You are looking for cha... |
| 3365 | 0.3014 | Currently, not every detail about permission and a... |
| 3366 | 0.3014 | Make sure that the Only apply these auditing setti... |
| 3367 | 0.3013 | • File server helpdesk personnel have access to a ... |
| 3368 | 0.3012 | SharePoint I want to exclude the domain\nwxservice... |
| 3369 | 0.3012 | This account should be assigned the following role... |
| 3370 | 0.3011 | Computer Select the account that will be used to c... |
| 3371 | 0.3010 | If you want to audit all access types (successful ... |
| 3372 | 0.3010 | Failed change attempts The Auditing Entry below sh... |
| 3373 | 0.3008 | Note that the new monitoring scope restrictions ap... |
| 3374 | 0.3007 | Failed Use this option to track suspicious activit... |
| 3375 | 0.3006 | Specifies number of threads and TaskLimit 8 queues... |
| 3376 | 0.3005 | If any conflicts are detected with your current au... |
| 3377 | 0.3004 | Step 5 – Click Upload. v10.7 The Upload button tex... |
| 3378 | 0.3004 | Scheduled Tasks Account Name Application Comment S... |
| 3379 | 0.3004 | Computer Specify a computer. You will only be aler... |
| 3380 | 0.3004 | Database retention Configure retention if you want... |
| 3381 | 0.3002 | • Make sure that the Only apply these auditing set... |
| 3382 | 0.2997 | Tip for reading the table: For example, on the com... |
| 3383 | 0.2996 | Configure Audit Object Access Policy Netwrixrecomm... |
| 3384 | 0.2995 | Specify the account for collecting data A custom a... |
| 3385 | 0.2994 | The role should be assigned to a very limited numb... |
| 3386 | 0.2994 | Specify restriction filters to narrow your monitor... |
| 3387 | 0.2993 | To disable outgoing NTLM authentication traffic vi... |
| 3388 | 0.2992 | Procedure for Nutanix Command-Line Interface Alter... |
| 3389 | 0.2991 | For outbound rules, create or enable predefined Wi... |
| 3390 | 0.2991 | • Advanced permissions: ◦ Create files / write dat... |
| 3391 | 0.2991 | Allow the following process to use the port: %syst... |
| 3392 | 0.2991 | SHOW PARAMETERS audit%r; If you want to clean your... |
| 3393 | 0.2990 | For example: ◦ "\\domain\dfsnamespace\" (domain-ba... |
| 3394 | 0.2990 | For these users, the product collects data from ES... |
| 3395 | 0.2988 | Verify the parameters you provided in settings.xml... |
| 3396 | 0.2986 | All filters are applied using AND logic. See the F... |
| 3397 | 0.2985 | The group policy will be updated. Step 12 – Type r... |
| 3398 | 0.2985 | See this Microsoft article for details. Last full ... |
| 3399 | 0.2985 | Table 1: To monitor for... Execute... Successful d... |
| 3400 | 0.2984 | Step 2 – Enable auditing of Oracle Database change... |
| 3401 | 0.2984 | The alerts contain pre-configured filters and in m... |
| 3402 | 0.2983 | To import snapshots, you must be assigned the Glob... |
| 3403 | 0.2983 | Nutanix AHV is a fully integrated component of the... |
| 3404 | 0.2982 | For that, execute: GRANT DBA TO <account_name>; Fo... |
| 3405 | 0.2981 | Events collected from any other source will be ign... |
| 3406 | 0.2980 | Step 3 – Add script parameters. The console will l... |
| 3407 | 0.2980 | v10.7 Step 2 – Configure Access Reviews. The Confi... |
| 3408 | 0.2980 | Run the setup and select the Data Provider for .NE... |
| 3409 | 0.2980 | Troubleshooting If no data is displayed in the rep... |
| 3410 | 0.2979 | You can use server name or IP address, for example... |
| 3411 | 0.2979 | Audit successful SELECT statements Auditing SELECT... |
| 3412 | 0.2977 | d625dccec0a8016700a22a0 assignment_ group NOTE: Yo... |
| 3413 | 0.2977 | Supported object types and attributes are listed i... |
| 3414 | 0.2977 | Supported object types and attributes are listed i... |
| 3415 | 0.2977 | The same SQL Server instance cannot be used to sto... |
| 3416 | 0.2976 | v10.7 2. Click View button in the right pane. To l... |
| 3417 | 0.2975 | If you also want to audit changes to the Schema pa... |
| 3418 | 0.2974 | Oracle Auditor supports monitoring the following v... |
| 3419 | 0.2973 | Unless an account is specified, the service runs u... |
| 3420 | 0.2973 | Download the latest add-on version in the Add-on S... |
| 3421 | 0.2973 | Download the latest add-on version in the Add-on S... |
| 3422 | 0.2973 | Download the latest add-on version in the Add-on S... |
| 3423 | 0.2970 | To audit users and groups, vCenter 6.5 and above r... |
| 3424 | 0.2969 | Right-click the effective domain controllers polic... |
| 3425 | 0.2969 | For example, you want to receive an alert on suspi... |
| 3426 | 0.2967 | Permission assignment will depend on the data you ... |
| 3427 | 0.2967 | Table 1: Location Prerequisites ConnectWise Manage... |
| 3428 | 0.2964 | By default, Auditor uses the LocalSystem account t... |
| 3429 | 0.2964 | Changes could only occur between September 16, 201... |
| 3430 | 0.2963 | For search subscription, you can also select a par... |
| 3431 | 0.2962 | AppNameRegExp — If you provide a pattern for appli... |
| 3432 | 0.2962 | Access to global environment. settings, monitoring... |
| 3433 | 0.2961 | will not be monitored. See the topics on the monit... |
| 3434 | 0.2961 | View and Search Collected Data how to apply filter... |
| 3435 | 0.2960 | Once have created a monitoring plan and verified t... |
| 3436 | 0.2959 | As a next step, click Add item to specify an objec... |
| 3437 | 0.2959 | DNS AAAA • Container name • IPv6 Address • Owner n... |
| 3438 | 0.2957 | This role is granted to specialists who use the In... |
| 3439 | 0.2955 | Ensure that... Set-ExecutionPolicy Unrestricted • ... |
| 3440 | 0.2954 | In-Script Parameters You may also need to modify t... |
| 3441 | 0.2954 | In-Script Parameters You may also need to modify t... |
| 3442 | 0.2954 | In-Script Parameters You may also need to modify t... |
| 3443 | 0.2952 | In this case, you will only be able to receive act... |
| 3444 | 0.2951 | Configure required protocols and ports, as describ... |
| 3445 | 0.2950 | For example: *,sqlserver1.corp.local, *Access is d... |
| 3446 | 0.2949 | ◦◦ User name – Provide the name of account that wi... |
| 3447 | 0.2948 | AD Container Complete the following fields: Option... |
| 3448 | 0.2947 | Update the template if necessary. CorrelationTicke... |
| 3449 | 0.2946 | Object type Actions Event ID LOGIN_INFORMATION Acc... |
| 3450 | 0.2946 | Using Basic Authentication with Microsoft Entra ID... |
| 3451 | 0.2943 | Report Summary with Star icon unchecked Other Acti... |
| 3452 | 0.2943 | When a new object is added, Auditor does not show ... |
| 3453 | 0.2941 | The user writing data to the Audit Database is gra... |
| 3454 | 0.2940 | Table 1: Option Description General Specify a comp... |
| 3455 | 0.2939 | This can be helpful, for example, if you want to e... |
| 3456 | 0.2939 | Applies to—Set to "Files only". Advanced permissio... |
| 3457 | 0.2939 | NOTE: In this case,Auditor does not adjust audit s... |
| 3458 | 0.2939 | NOTE: In this case,Auditor does not adjust audit s... |
| 3459 | 0.2939 | NOTE: In this case,Auditor does not adjust audit s... |
| 3460 | 0.2938 | Otherwise, the addon will not be able to write dat... |
| 3461 | 0.2938 | Otherwise, the addon will not be able to write dat... |
| 3462 | 0.2936 | v10.7 Step 5 – On the Select a creation type step,... |
| 3463 | 0.2935 | Failed read attempts v10.7 Auditing Entry Type—Set... |
| 3464 | 0.2934 | Helps find out who was trying to access your priva... |
| 3465 | 0.2934 | Run Windows PowerShell as administrator and execut... |
| 3466 | 0.2933 | Opens the listed Auditor report. See the Custom Se... |
| 3467 | 0.2932 | Delegate FolderBind NOTE: Audit records for folder... |
| 3468 | 0.2932 | Users can also configure Only the latest snapshot ... |
| 3469 | 0.2932 | Item is added and SQL Server monitoring plan is re... |
| 3470 | 0.2932 | See the Export A ctivity Records topic for a dditi... |
| 3471 | 0.2931 | If you want to audit all access types (successful ... |
| 3472 | 0.2931 | Perform this action with other computers. Step 4 –... |
| 3473 | 0.2930 | See the To Enable JavaScript topic for additional ... |
| 3474 | 0.2930 | The add-on will operate as a Syslog listener for t... |
| 3475 | 0.2930 | Step 5 – In the Alert Properties wizard, specify t... |
| 3476 | 0.2928 | v10.7 The timeout parameter is configured within t... |
| 3477 | 0.2928 | Usage example Database administrators need to disc... |
| 3478 | 0.2927 | v10.7 Option Description your current audit settin... |
| 3479 | 0.2927 | This account should meet the requirements listed b... |
| 3480 | 0.2927 | You can also configure and receive alerts on the e... |
| 3481 | 0.2926 | Facility Netwrix recommends using default values. ... |
| 3482 | 0.2925 | This role is also granted Audit Database. to servi... |
| 3483 | 0.2925 | Use the omitreadaccess.txt to exclude SELECT state... |
| 3484 | 0.2925 | Register the Add-On Run the install.ps1 PowerShell... |
| 3485 | 0.2925 | View and Search Collected Data how to apply filter... |
| 3486 | 0.2924 | You can also create lists of specific file shares ... |
| 3487 | 0.2923 | Or simply drag and drop the add-on file in the con... |
| 3488 | 0.2922 | Your current audit settings will be checked on eac... |
| 3489 | 0.2922 | Specify monitoring restrictions Specify restrictio... |
| 3490 | 0.2921 | Program/script Input "Powershell.exe". Add a path ... |
| 3491 | 0.2921 | To import Active Directory data from the removed m... |
| 3492 | 0.2920 | See the Amazon Web Services topic for additional i... |
| 3493 | 0.2916 | See the Reports with Video topic for additional in... |
| 3494 | 0.2916 | In most cases the default values should be used. P... |
| 3495 | 0.2915 | In this case the "Who", "Workstation" and "When" v... |
| 3496 | 0.2913 | Data Discovery and Classification Reports Follow t... |
| 3497 | 0.2913 | If any conflicts are detected with Table 1: Option... |
| 3498 | 0.2913 | Each Activity Record contains the user account, ac... |
| 3499 | 0.2910 | Step 3 – Navigate to the Monitored computers list ... |
| 3500 | 0.2908 | • Advanced permissions—Select List folder / read d... |
| 3501 | 0.2908 | This functionality is currently available for the ... |
| 3502 | 0.2908 | 55.. Run the following command to update group pol... |
| 3503 | 0.2907 | Note that the new monitoring scope restrictions ap... |
| 3504 | 0.2907 | The Auditor server side Auditor version is 10.0 or... |
| 3505 | 0.2907 | The Auditor server side Auditor version is 10.0 or... |
| 3506 | 0.2907 | The Auditor server side Auditor version is 10.0 or... |
| 3507 | 0.2906 | Currently, the Windows Server State-in-Time report... |
| 3508 | 0.2906 | Option Description Specify the name of the SQL Ser... |
| 3509 | 0.2906 | Free Community Edition helps you maintain visibili... |
| 3510 | 0.2904 | Step 2 – On the main page, you will be prompted to... |
| 3511 | 0.2904 | See the Monitoring Planstopic for additional infor... |
| 3512 | 0.2903 | Applies to—Set to"This folder, subfolders and file... |
| 3513 | 0.2903 | v10.7 Do.. Recommended use This is helpful when yo... |
| 3514 | 0.2900 | Upon s electing Combination of file and share perm... |
| 3515 | 0.2900 | Table 1: Criteria Data model Description DataSourc... |
| 3516 | 0.2899 | C:\Add-ons\Netwrix_Auditor_Addon_for_RADIUS_Server... |
| 3517 | 0.2899 | For example: Table 1: Symbol XML entity & e.g., Al... |
| 3518 | 0.2897 | See the Fine-Tune Your Plan and Edit Settings topi... |
| 3519 | 0.2897 | In the Filter by organizational unit dialog that o... |
| 3520 | 0.2896 | If false, a corresponding error message will be di... |
| 3521 | 0.2895 | By default, the LocalSystem account is used for th... |
| 3522 | 0.2894 | Step 4 – Review the <TicketParameters> section. Th... |
| 3523 | 0.2893 | Make Reports Handy In addition to reviewing report... |
| 3524 | 0.2893 | Specify the account for collecting data Select the... |
| 3525 | 0.2893 | Service Board Service tickets created by the add-o... |
| 3526 | 0.2893 | Your current audit settings will be checked on eac... |
| 3527 | 0.2893 | Your current audit settings will be checked on eac... |
| 3528 | 0.2891 | If you want to run the addon on another machine, p... |
| 3529 | 0.2891 | The procedure below explains how to configure redi... |
| 3530 | 0.2891 | For example, "company.local". Specify the account ... |
| 3531 | 0.2891 | You can also use group Managed Service Accounts (g... |
| 3532 | 0.2889 | • Advanced permissions—Select List folder / read d... |
| 3533 | 0.2888 | AD Container Complete the following fields: Option... |
| 3534 | 0.2887 | v10.7 In the Insertion Strings tab: Option Descrip... |
| 3535 | 0.2887 | More informative subject lines in email notificati... |
| 3536 | 0.2887 | See the Data Collection from VMware Servers topic ... |
| 3537 | 0.2886 | Table 1: Option Description Specify the account fo... |
| 3538 | 0.2885 | These settings cannot be modified for a certain pl... |
| 3539 | 0.2885 | Set up protocols and ports. See the Dell Data Stor... |
| 3540 | 0.2885 | Table 1: This tile shows the current number of use... |
| 3541 | 0.2884 | Upgrade in progress Database is being upgraded. Al... |
| 3542 | 0.2883 | By default, it is set to 120 months. Use custom cr... |
| 3543 | 0.2883 | To report on copy actions on remote file shares, m... |
| 3544 | 0.2881 | See the Define Parameters topic for additional inf... |
| 3545 | 0.2881 | To read more about activity records, see the Refer... |
| 3546 | 0.2880 | Unless specified, RFC 3164/5424 format is used. If... |
| 3547 | 0.2878 | If you set the Who filter to does not contain John... |
| 3548 | 0.2876 | For example, if you have advanced omitreporterrors... |
| 3549 | 0.2876 | - SSD Table 1: Hardware component Requirement Proc... |
| 3550 | 0.2876 | property name Contains a list of objects to be and... |
| 3551 | 0.2876 | The changes include creation, modification, deleti... |
| 3552 | 0.2874 | Monitor SSO users/groups on vCenter and Local user... |
| 3553 | 0.2874 | v10.7 on... Ensure that... The UDP Receiver is ena... |
| 3554 | 0.2873 | See the Placing files directly in the namespace sh... |
| 3555 | 0.2873 | Step 2 – Edit the following parameters of the cust... |
| 3556 | 0.2873 | String9 The internal message URL 5 actMessageDelet... |
| 3557 | 0.2870 | Table 1: Option Description General Specify Nutani... |
| 3558 | 0.2870 | If you want to use a specific account (other than ... |
| 3559 | 0.2870 | If you want to use a specific account (other than ... |
| 3560 | 0.2870 | If you want to use a specific account (other than ... |
| 3561 | 0.2870 | If you want to use a specific account (other than ... |
| 3562 | 0.2870 | If you want to use a specific account (other than ... |
| 3563 | 0.2870 | If you want to use a specific account (other than ... |
| 3564 | 0.2870 | To make Windows operating system use more secure p... |
| 3565 | 0.2869 | Review Behavior Anomalies Dashboard To review the ... |
| 3566 | 0.2868 | See the Export A ctivity Records topic for a dditi... |
| 3567 | 0.2867 | This value is set to 1 by default, which means tha... |
| 3568 | 0.2867 | You can adjust audit settings automatically. Your ... |
| 3569 | 0.2867 | StateUpdatingPeriodicity Periodic time interval fo... |
| 3570 | 0.2866 | See the Data C ollecting Account topic for additio... |
| 3571 | 0.2864 | • Make sure that the Apply these auditing entries ... |
| 3572 | 0.2863 | See the Configuration topic for additional informa... |
| 3573 | 0.2862 | Tip for reading the table: For example, on the com... |
| 3574 | 0.2862 | Specify delivery options • File format—Configure r... |
| 3575 | 0.2861 | Right-click the effective domain controllers polic... |
| 3576 | 0.2861 | NotEqualTo Max length: 255. StartsWith EndsWith Li... |
| 3577 | 0.2860 | Reviewer Access to data collected by Auditor and i... |
| 3578 | 0.2859 | AD Container Complete the following fields: Option... |
| 3579 | 0.2858 | The custom account must be granted the following r... |
| 3580 | 0.2856 | For example, a new file share was created on the a... |
| 3581 | 0.2856 | Enabled Examine all domain controllers Select this... |
| 3582 | 0.2856 | Click Explore. In the File Server REST API Explore... |
| 3583 | 0.2853 | For example: ONTAPI cluster1::> vserver services w... |
| 3584 | 0.2853 | Table 1: CorrelationTicketFormat Description Previ... |
| 3585 | 0.2853 | Monitor Oracle Database logon activity Specify wha... |
| 3586 | 0.2852 | Item— name of the SQL Server instance monitored wi... |
| 3587 | 0.2851 | Step 2 – When adding a cluster file server for aud... |
| 3588 | 0.2851 | v10.7 Configure the following: Setting Description... |
| 3589 | 0.2851 | Ensure that... auth.*;authpriv. * @172.28.18.25:51... |
| 3590 | 0.2851 | Ensure that... auth.*;authpriv. * @172.28.18.25:51... |
| 3591 | 0.2851 | Configure Parameters for Data Collection In the ad... |
| 3592 | 0.2848 | • Make sure that the Apply these auditing entries ... |
| 3593 | 0.2848 | The user running the script must have sufficient p... |
| 3594 | 0.2848 | Step 2 – Run the install.cmd file. The file deploy... |
| 3595 | 0.2846 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} • (... |
| 3596 | 0.2846 | Step 3 – On the Select Rollback Source step, speci... |
| 3597 | 0.2845 | To open a new ticket for every alert, set the para... |
| 3598 | 0.2845 | Advanced permissions: ◦ Create files / write data ... |
| 3599 | 0.2845 | • Run the setup and select the Data Provider for .... |
| 3600 | 0.2842 | This data can help you to assess the activity reco... |
| 3601 | 0.2842 | Your current audit settings will be checked on eac... |
| 3602 | 0.2841 | will not be monitored. Step 3 – Review considerati... |
| 3603 | 0.2840 | Applies to—Set to "This folder, subfolders and fil... |
| 3604 | 0.2839 | Windows File Server NOTE: Prior to configuring you... |
| 3605 | 0.2839 | For example, 1, 3, 5-99. You can also exclude unwa... |
| 3606 | 0.2838 | Use this option to track suspicious activity. Help... |
| 3607 | 0.2838 | object type:property: When an object is deleted, A... |
| 3608 | 0.2837 | NOTE: This covers all the required permissions bel... |
| 3609 | 0.2837 | Step 3 – Assign the required permissions. Permissi... |
| 3610 | 0.2835 | Add arguments (optional) Add a path to the add-on ... |
| 3611 | 0.2835 | Table 2: XML Retrieve Activity Records <?xml versi... |
| 3612 | 0.2835 | This is the initial product installation. Requirem... |
| 3613 | 0.2834 | Specify custom connection parameters Make sure thi... |
| 3614 | 0.2834 | Step 4 – In the Advanced Security Settings for SOF... |
| 3615 | 0.2833 | Step 2 – Disable the Object Access, Account Manage... |
| 3616 | 0.2833 | Successful SELECT statement execution will be repo... |
| 3617 | 0.2833 | Use this report to discover user accounts with set... |
| 3618 | 0.2833 | The same SQL Server instance cannot be used to sto... |
| 3619 | 0.2831 | For most data sources, if an Activity Summaries co... |
| 3620 | 0.2831 | For more information on the attributes marked with... |
| 3621 | 0.2830 | In addition to the restrictions for a monitoring p... |
| 3622 | 0.2828 | v10.7 Type—Set to "Fail". Applies to—Set to "This ... |
| 3623 | 0.2827 | Select Add User. v10.7 Scope Roles Global administ... |
| 3624 | 0.2825 | Using Modern Authentication with Microsoft Entra I... |
| 3625 | 0.2825 | In the Maximum Password Age Setting dialog that op... |
| 3626 | 0.2824 | If you want to use a specific account (other than ... |
| 3627 | 0.2824 | If you want to use a specific account (other than ... |
| 3628 | 0.2824 | If you want to use a specific account (other than ... |
| 3629 | 0.2823 | Defines destination IP address. In case of multipl... |
| 3630 | 0.2822 | Select this option to receive reports attached to ... |
| 3631 | 0.2822 | Step 2 – Run data collection. Step 3 – Consider th... |
| 3632 | 0.2822 | Accepted changes must be implemented outside of th... |
| 3633 | 0.2819 | Remember, when auditing SQL Server availability on... |
| 3634 | 0.2817 | If you want to use a specific account (other than ... |
| 3635 | 0.2817 | If you want to use a specific account (other than ... |
| 3636 | 0.2816 | For example: v1.0\powershell.exe v10.7 In the With... |
| 3637 | 0.2816 | All diagrams provide the drill-down functionality,... |
| 3638 | 0.2816 | Extra-Large Environment Recommendations below refe... |
| 3639 | 0.2816 | This helps you keep track of all changes in your I... |
| 3640 | 0.2815 | For example: cluster1::> system services web show ... |
| 3641 | 0.2815 | See the Other Components topic for a dditional inf... |
| 3642 | 0.2814 | Download the latest add-on version in the Add-on S... |
| 3643 | 0.2813 | Devices 514 UDP Service host devices However, you ... |
| 3644 | 0.2813 | While inputting text inline is easy, your baseline... |
| 3645 | 0.2812 | Specify UNC path to the shared folder where user s... |
| 3646 | 0.2812 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3647 | 0.2811 | • Check that network connectivity between the Acco... |
| 3648 | 0.2811 | Below is the default hardware configuration for th... |
| 3649 | 0.2808 | Enterprise Overview See also: Enterprise Overview ... |
| 3650 | 0.2807 | Depending on the type of the object you want to ex... |
| 3651 | 0.2806 | See the Dell Data Storage topic for additional inf... |
| 3652 | 0.2806 | The default value is 86400 seconds, i.e., 24 hours... |
| 3653 | 0.2805 | This helps to optimize solution performance during... |
| 3654 | 0.2801 | To force basic audit policies to be ignored and pr... |
| 3655 | 0.2796 | You have already identified the intruder (e.g., Ba... |
| 3656 | 0.2793 | Check the Database, Active Directory, and Notifica... |
| 3657 | 0.2793 | See the Monitoring Planstopic for additional infor... |
| 3658 | 0.2793 | A Security Officer wants to monitor a file share, ... |
| 3659 | 0.2792 | v10.7 File Description Syntax Use the omitlogonlis... |
| 3660 | 0.2791 | See the Obtain the Tenant Name topic for additiona... |
| 3661 | 0.2791 | Step 5 – Check Allow next to the Read permission. ... |
| 3662 | 0.2790 | Several examples are provided below. v10.7 In the ... |
| 3663 | 0.2790 | This value is filled in automatically. Snapshot da... |
| 3664 | 0.2790 | Step 5 – Remediation of the accepted changes must ... |
| 3665 | 0.2790 | v10.7 Parameter Default value Description Instead ... |
| 3666 | 0.2789 | Membership in one of the following groups: Adminis... |
| 3667 | 0.2788 | Table 1: Name Description IgnoreUploadAttachmentEr... |
| 3668 | 0.2787 | The spaces are trimmed. If they are required, use ... |
| 3669 | 0.2786 | For more information about authentication, refer t... |
| 3670 | 0.2785 | See the Review User Profiles and Process Anomalies... |
| 3671 | 0.2785 | If you want to use a specific account (other than ... |
| 3672 | 0.2785 | Wildcards (*) are not supported. In addition to th... |
| 3673 | 0.2784 | In sqlplus tool, execute the following command: sq... |
| 3674 | 0.2784 | v10.7 Option Description General Specify an IP ran... |
| 3675 | 0.2783 | Step 5 – Navigate to the Actions tab and complete ... |
| 3676 | 0.2782 | Make sure that the Apply these auditing entries to... |
| 3677 | 0.2782 | When an object is deleted, Auditor does not show a... |
| 3678 | 0.2782 | Send the request, clicking Try it out. Get the res... |
| 3679 | 0.2781 | In the Specific local ports field specify the port... |
| 3680 | 0.2780 | Step 1 – Sign in to Microsoft Entra ID portal usin... |
| 3681 | 0.2777 | Table 1: Item Action Audited How this change is re... |
| 3682 | 0.2775 | Reports with review status to track team workflow.... |
| 3683 | 0.2775 | Be sure to use a different installation folder. St... |
| 3684 | 0.2773 | In the right pane, go to the Intelligence s ection... |
| 3685 | 0.2773 | For example: ,sqlserver1.corp.local, Access is den... |
| 3686 | 0.2771 | You can select to collect event data from the same... |
| 3687 | 0.2770 | To check receiver settings or add a new receiver, ... |
| 3688 | 0.2769 | If any conflicts are detected with Configure audit... |
| 3689 | 0.2769 | See the Interactive Reports for Change Management ... |
| 3690 | 0.2769 | Use the omitlogonlist.txt to exclude SQL logons fr... |
| 3691 | 0.2768 | Applies to—Set to "This folder, subfolders and fil... |
| 3692 | 0.2767 | All devices Collected via MS Graph on endpoint /de... |
| 3693 | 0.2767 | v10.7 Follow the steps to restore original look. S... |
| 3694 | 0.2767 | Advanced permissions—Select List folder / read dat... |
| 3695 | 0.2765 | CAUTION: Monitoring of non-default hidden shares i... |
| 3696 | 0.2762 | The default name for the original database was Net... |
| 3697 | 0.2762 | Step 12 – Type repadmin/syncall command and press ... |
| 3698 | 0.2762 | This account should have the following minimal rig... |
| 3699 | 0.2761 | ◦◦ By default, Auditor will monitor all shares sto... |
| 3700 | 0.2760 | To configure them manually, refer to the Configure... |
| 3701 | 0.2760 | Description Network Protocol** Status Configuratio... |
| 3702 | 0.2759 | If a different log level is needed or desired, the... |
| 3703 | 0.2759 | Failed read attempts The Auditing Entry below show... |
| 3704 | 0.2759 | Failed read attempts The Auditing Entry below show... |
| 3705 | 0.2759 | The credentials are case sensitive. Take into cons... |
| 3706 | 0.2758 | Customizing Metrics for Your Organization Default ... |
| 3707 | 0.2755 | The subscription (email attachment or file uploade... |
| 3708 | 0.2754 | Enterprise Overview—A dashboard with a set of widg... |
| 3709 | 0.2752 | Click the Details link to examine the product log.... |
| 3710 | 0.2751 | See the procedure below for details. NOTE: In this... |
| 3711 | 0.2751 | See the procedure below for details. NOTE: In this... |
| 3712 | 0.2750 | See Response Status Codes for more information. v1... |
| 3713 | 0.2750 | Advanced permissions: ◦ Create files / write data ... |
| 3714 | 0.2750 | A listener allows you to connect to a replica with... |
| 3715 | 0.2749 | Table 1: Description Changes Successful Use this o... |
| 3716 | 0.2749 | Port 1433 is the default connections port, however... |
| 3717 | 0.2748 | Wildcards (*) are not supported. In addition to th... |
| 3718 | 0.2747 | The Remove changes window closes. Owners & Access ... |
| 3719 | 0.2745 | Select this checkbox if your SMTP server requires ... |
| 3720 | 0.2745 | Upon login, you will be directed to the My Reviews... |
| 3721 | 0.2744 | Follow the steps to import snapshots. Step 1 – In ... |
| 3722 | 0.2744 | To do it, click Configure next to Alerts. Follow t... |
| 3723 | 0.2743 | ADPermission #RBAC: -MailboxAuditLogSearch -AdminA... |
| 3724 | 0.2742 | • Applies to—Set to "This folder, subfolders and f... |
| 3725 | 0.2742 | If you configured a dedicated monitoring plan, mak... |
| 3726 | 0.2741 | Date Created Date Modified Disabled ID Instead of ... |
| 3727 | 0.2740 | .NET 4.5 or later must be installed. The computer ... |
| 3728 | 0.2740 | For example, "Successful read attempts on importan... |
| 3729 | 0.2740 | Failed read attempts The Auditing Entry below show... |
| 3730 | 0.2739 | Configure Audit Database Account This is the accou... |
| 3731 | 0.2738 | v10.7 Step 5 – Configure Data Collecting Account. ... |
| 3732 | 0.2738 | If necessary, modify the parameters as required. P... |
| 3733 | 0.2737 | Clicking the link opens the corresponding report: ... |
| 3734 | 0.2737 | To find out what is included in the alert details,... |
| 3735 | 0.2736 | Step 7 – Select Server roles on the left and assig... |
| 3736 | 0.2735 | Instead of updating the ticket every time, the ser... |
| 3737 | 0.2734 | Execute the following command: Table 1: Track... S... |
| 3738 | 0.2734 | accounts (disable, move, delete) Table 1: File Des... |
| 3739 | 0.2732 | The risk score assigned to a user does not qualify... |
| 3740 | 0.2731 | To specify another status, provide its ID in the <... |
| 3741 | 0.2730 | Table 1: Event Type Description Information An eve... |
| 3742 | 0.2728 | Message No string Object-specific details about th... |
| 3743 | 0.2728 | Administrator & Privileged Role Administrator & Te... |
| 3744 | 0.2727 | IsArchiveOnly No — IsArchiveOnly allows to save Ac... |
| 3745 | 0.2727 | You can also change these settings later. See the ... |
| 3746 | 0.2727 | You cannot disable auditing the Domain partition f... |
| 3747 | 0.2726 | Normally contains information specific to your dat... |
| 3748 | 0.2725 | If you want to use a specific account (other Table... |
| 3749 | 0.2725 | Failed change attempts The Auditing Entry below sh... |
| 3750 | 0.2723 | So you can easily discover what is going on in you... |
| 3751 | 0.2722 | Exports the selected review instance information t... |
| 3752 | 0.2721 | CAUTION: This field should never be empty. Checkpo... |
| 3753 | 0.2721 | Make sure that the Apply these auditing entries to... |
| 3754 | 0.2721 | Make sure that the Apply these auditing entries to... |
| 3755 | 0.2721 | Select Group membershipif you want to include Grou... |
| 3756 | 0.2721 | Tickets for new alert types are created immediatel... |
| 3757 | 0.2718 | v10.7 Manage Data Sources You can fine-tune data c... |
| 3758 | 0.2718 | Follow the steps to assign the role you need: Step... |
| 3759 | 0.2717 | On your Oracle Database Server (target), allow inb... |
| 3760 | 0.2715 | For example, dsacls "CN=Deleted Objects,DC=Corp,DC... |
| 3761 | 0.2713 | Make sure Virtual Directory is set correctly, and ... |
| 3762 | 0.2712 | Assigned owners can log in to complete reviews. Th... |
| 3763 | 0.2712 | To migrate to Unified Auditing for Oracle Database... |
| 3764 | 0.2710 | The product will not collect any user activity or ... |
| 3765 | 0.2710 | "sampledomain.sample/sampling", the syntax should ... |
| 3766 | 0.2710 | Step 5 – Finally, at the Summary step, review the ... |
| 3767 | 0.2708 | Step 8 – Provide the object name and configure ite... |
| 3768 | 0.2708 | Starting with version 10.5, Auditor provides limit... |
| 3769 | 0.2707 | AD Container Complete the following fields: Option... |
| 3770 | 0.2707 | The product will audit only user accounts that bel... |
| 3771 | 0.2705 | If network traffic compression will be disabled, a... |
| 3772 | 0.2705 | Parameter or switch Default value Description By d... |
| 3773 | 0.2705 | Thus, s/he configures the product not to monitor t... |
| 3774 | 0.2705 | Thus, s/he configures the product not to monitor t... |
| 3775 | 0.2705 | Thus, s/he configures the product not to monitor t... |
| 3776 | 0.2704 | NOTE: If you are going to configure monitoring rul... |
| 3777 | 0.2702 | See the corresponding Oracle documentation article... |
| 3778 | 0.2701 | Ensure that... On the ArcSight side The UDP Receiv... |
| 3779 | 0.2699 | At least the first script run should be performed ... |
| 3780 | 0.2698 | v10.7 Option Description your current audit settin... |
| 3781 | 0.2695 | Table 1: To... Follow the steps... Find an alert U... |
| 3782 | 0.2694 | Scale-Out File Server (SOFS) cluster is not suppor... |
| 3783 | 0.2694 | Send empty subscriptions when no a ctivity occurre... |
| 3784 | 0.2692 | You can configure advanced audit policies for the ... |
| 3785 | 0.2690 | Health Status Dashboard Schedule Health Summary em... |
| 3786 | 0.2689 | Note that the new monitoring scope restrictions ap... |
| 3787 | 0.2688 | User SID For example: <v v="*S-1-5-21-11806992 -87... |
| 3788 | 0.2688 | Time zone — is set automatically. Snapshot date —s... |
| 3789 | 0.2688 | For example, the product Information successfully ... |
| 3790 | 0.2686 | Select Monitor userdefined hidden shares if necess... |
| 3791 | 0.2686 | This significantly improves data transfer and mini... |
| 3792 | 0.2685 | Specify the name from the Value list or type it yo... |
| 3793 | 0.2684 | Possible values: Empty—Check Auditor certificate v... |
| 3794 | 0.2684 | Possible values: Empty—Check Auditor certificate v... |
| 3795 | 0.2683 | Each <TicketParameter> includes the <Name></Name> ... |
| 3796 | 0.2682 | Add-on installation server, i.e. the machine where... |
| 3797 | 0.2682 | Click Add to add a new monitoring plan. Step 3 – C... |
| 3798 | 0.2681 | This option works only when ReopenTicketOnRepetiti... |
| 3799 | 0.2681 | v10.7 Review the following for additional informat... |
| 3800 | 0.2679 | Non-owner Mailbox Access Audit: Manual Configurati... |
| 3801 | 0.2677 | See the Fine-Tune Your Plan and Edit Settings topi... |
| 3802 | 0.2676 | Older tickets requests are cleared. Table 2: <Conn... |
| 3803 | 0.2676 | Use... To... Save as report Save your search resul... |
| 3804 | 0.2676 | Enable this option and specify one or several emai... |
| 3805 | 0.2676 | exomiteventuserlist.txt user@tenant.com will be re... |
| 3806 | 0.2676 | Monitor VMware configuration changes Configuration... |
| 3807 | 0.2675 | If you select to automatically configure audit in ... |
| 3808 | 0.2674 | By default, you will receive data on all risk cate... |
| 3809 | 0.2674 | Example As a database administrator, you can have ... |
| 3810 | 0.2672 | Applying Filters Every time you run the script, Au... |
| 3811 | 0.2671 | If you have alternate access mapping configured in... |
| 3812 | 0.2670 | Do not select the checkbox if you want to configur... |
| 3813 | 0.2670 | Select this checkbox if the implicit SSL mode is u... |
| 3814 | 0.2669 | If you have alternate access mapping configured in... |
| 3815 | 0.2668 | This option works in co mbination with UpdateTicke... |
| 3816 | 0.2668 | For that, you will need an executable file stored ... |
| 3817 | 0.2668 | In the left pane, navigate to Forest: <forest_name... |
| 3818 | 0.2668 | In the left pane, navigate to Forest: <forest_name... |
| 3819 | 0.2667 | See SQL Server Reporting Services for a dditional ... |
| 3820 | 0.2667 | Specify data collection method You can enable netw... |
| 3821 | 0.2666 | If it is not, double-click the service. In the Rem... |
| 3822 | 0.2665 | Step 4 – Run the shell script by executing the fol... |
| 3823 | 0.2664 | This does require the Access Reviews application t... |
| 3824 | 0.2664 | <v v= "*ROOTDC1*"/> <n n="localhost"> <a n="DCWith... |
| 3825 | 0.2662 | Step 3 – Assign the required permissions. Permissi... |
| 3826 | 0.2659 | Step 2 – Select Microsoft Entra ID on the left. St... |
| 3827 | 0.2659 | Step 2 – Select Microsoft Entra ID on the left. St... |
| 3828 | 0.2658 | As a Auditor administrator I want to exclude the d... |
| 3829 | 0.2658 | Step 3 – Right-click the Security node and select ... |
| 3830 | 0.2657 | Name and Location Select a name for the new virtua... |
| 3831 | 0.2657 | Check "Successful" next to the following permissio... |
| 3832 | 0.2656 | Helps find out who was trying to access your priva... |
| 3833 | 0.2656 | Grouped alerts for different computers will be del... |
| 3834 | 0.2655 | Table 2: Option Description Specify Active Directo... |
| 3835 | 0.2655 | Table 2: Option Description Specify Active Directo... |
| 3836 | 0.2655 | In addition, you can exclude data from non-owner a... |
| 3837 | 0.2654 | Step 7 – Click Save. Then click OK to confirm. The... |
| 3838 | 0.2654 | Thus, you will need to prepare an Microsoft 365 us... |
| 3839 | 0.2653 | 55.. Run the following command to update group pol... |
| 3840 | 0.2653 | v10.7 Web Application Firewall Geo IP & Botnet Fil... |
| 3841 | 0.2653 | For example, your DNS security parameters' changes... |
| 3842 | 0.2651 | Until then, data collection will not be performed.... |
| 3843 | 0.2651 | Until then, data collection will not be performed.... |
| 3844 | 0.2648 | Follow the steps to assign the dbcreator and db_ow... |
| 3845 | 0.2648 | See the Data C ollecting Account topic for additio... |
| 3846 | 0.2647 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 3847 | 0.2647 | This permission should be assigned on each domain ... |
| 3848 | 0.2647 | See the Use Filters in Advanced Mode topic for a d... |
| 3849 | 0.2646 | Syslog Device Network Devices Cisco Meraki Dashboa... |
| 3850 | 0.2644 | At least the first script run should be performed ... |
| 3851 | 0.2642 | Send report to administrators Enable this option a... |
| 3852 | 0.2642 | You can also refresh the alerts information by cli... |
| 3853 | 0.2642 | The report is added to the Favorite reports sectio... |
| 3854 | 0.2640 | share. Thus, s/he configures the product not to mo... |
| 3855 | 0.2640 | share. Thus, s/he configures the product not to mo... |
| 3856 | 0.2639 | You can configure advanced audit policies for the ... |
| 3857 | 0.2639 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Amazon_Web_S... |
| 3858 | 0.2639 | See the Integration API topic for additional infor... |
| 3859 | 0.2638 | Depending on the error code, the response body may... |
| 3860 | 0.2638 | Table 1: Sign-In types Action Types Description De... |
| 3861 | 0.2637 | Use a standard account for that. See the SQL Serve... |
| 3862 | 0.2636 | The resource name can Where Yes nvarchar 255 be a ... |
| 3863 | 0.2636 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 3864 | 0.2636 | See the Create a New Monitoring Plan topic for add... |
| 3865 | 0.2636 | Notify users about activity monitoring You can ena... |
| 3866 | 0.2635 | To specify another status, provide its ID in the <... |
| 3867 | 0.2635 | Oracle recommends using Unified Auditing, which en... |
| 3868 | 0.2634 | Also, remember to do the following: Configure Data... |
| 3869 | 0.2633 | Example: mydomain\user1. Object URL – provide URL ... |
| 3870 | 0.2633 | Table 2: Option Description General Specify AD con... |
| 3871 | 0.2633 | Users Select the users whose activity should be re... |
| 3872 | 0.2632 | A management IP is an IP address that is used for ... |
| 3873 | 0.2630 | This permission should be assigned on each domain ... |
| 3874 | 0.2630 | Alerts are helpful if you want to be notified abou... |
| 3875 | 0.2629 | Make sure that your carrier supports sms to email ... |
| 3876 | 0.2629 | Pay attention to the "Data categories" column in s... |
| 3877 | 0.2629 | Table 1: Button Description Export CSV Exports the... |
| 3878 | 0.2626 | This helps to optimize solution performance during... |
| 3879 | 0.2626 | For example: Set-Item wsman:\localhost\Client\ Tru... |
| 3880 | 0.2625 | All filters are applied using AND logic. Configure... |
| 3881 | 0.2624 | Below is an example of a mask: ◦ * - any machine ◦... |
| 3882 | 0.2622 | Specify the switch during the addon execution if y... |
| 3883 | 0.2622 | Specify users to track their activity Exclude—Add ... |
| 3884 | 0.2622 | Successful Enabling this option on public shares w... |
| 3885 | 0.2622 | Step 2 – In the Help Protect your computer with Wi... |
| 3886 | 0.2621 | Event Description fs_create_directory A new direct... |
| 3887 | 0.2621 | Associate a risk score with the alert — Assign a r... |
| 3888 | 0.2620 | You can create a custom file or use rules provided... |
| 3889 | 0.2620 | SqlLogon — Successful logon attempt made through S... |
| 3890 | 0.2620 | Item — name of the item within your monitoring pla... |
| 3891 | 0.2619 | Step 2 – Configure System Access Control List (SAC... |
| 3892 | 0.2617 | This account requires at least Read permission for... |
| 3893 | 0.2616 | If you need to change user name or password for ac... |
| 3894 | 0.2613 | Follow the steps to perform distributed deployment... |
| 3895 | 0.2612 | User name and password for connection to Nutanix P... |
| 3896 | 0.2608 | See the View Reports topic for additional informat... |
| 3897 | 0.2607 | Specify Active Directory domain For example, "comp... |
| 3898 | 0.2606 | Apply gMSA to Access Long-Term Archive To write da... |
| 3899 | 0.2606 | ConsolidationInterval 900 Specify the time period,... |
| 3900 | 0.2605 | File Description Syntax Contains a list of account... |
| 3901 | 0.2605 | Table 2: Option Description Specify account which ... |
| 3902 | 0.2605 | Data Collecting Account Start data collection. Con... |
| 3903 | 0.2605 | Data Collecting Account Start data collection. Con... |
| 3904 | 0.2604 | For example, you can run the add-on on the compute... |
| 3905 | 0.2602 | NotEqualTo Max length: 536870911. StartsWith EndsW... |
| 3906 | 0.2599 | Error message text v10.7 File Description Syntax C... |
| 3907 | 0.2599 | Table 2: Option Description Send report to the use... |
| 3908 | 0.2599 | You can adjust audit settings automatically. Your ... |
| 3909 | 0.2597 | • .NET 4.5 or later must be installed. Execution p... |
| 3910 | 0.2597 | Remove subscriptions Click icon next to the select... |
| 3911 | 0.2597 | Step 1 – On the main Auditor page, click the Repor... |
| 3912 | 0.2595 | The moment when the change occurred. When When Yes... |
| 3913 | 0.2595 | Your monitoring plan is configure d to track domai... |
| 3914 | 0.2595 | See the Monitoring Planstopic for additional infor... |
| 3915 | 0.2594 | To be able to perform the test run, current user a... |
| 3916 | 0.2593 | Table 1: Auditing type Oracle version Details Unif... |
| 3917 | 0.2591 | RID is included in output A ctivity Records only. ... |
| 3918 | 0.2591 | Specify how long data will be stored. By default, ... |
| 3919 | 0.2591 | Follow the steps to review and update global Audit... |
| 3920 | 0.2590 | If you want to use a specific account (other than ... |
| 3921 | 0.2590 | SQL Server Auditor supports monitoring the followi... |
| 3922 | 0.2590 | NOTE: You can specify any other user group, but in... |
| 3923 | 0.2589 | In large environments, it is required to wait 10 h... |
| 3924 | 0.2589 | Filters You can narrow your reporting scope using ... |
| 3925 | 0.2589 | Filters You can narrow your reporting scope using ... |
| 3926 | 0.2589 | See the Monitoring Overview topic for additional i... |
| 3927 | 0.2587 | Click Add Rule and configure the following: Table ... |
| 3928 | 0.2586 | Monitor SSO users/groups on vCenter and Local user... |
| 3929 | 0.2585 | Step 3 – Navigate to Users tab and click Add next ... |
| 3930 | 0.2585 | Make sure this account has Log on as batch job pri... |
| 3931 | 0.2583 | SqlLogon — Successful logon attempt made through S... |
| 3932 | 0.2582 | Step 2 – Edit the *.txt files, based on the follow... |
| 3933 | 0.2582 | Step 4 – Modify the default scheduled task name: $... |
| 3934 | 0.2581 | contain John, you will exclude the Does not contai... |
| 3935 | 0.2580 | Netwrix recommends setting it to 2 years (730 days... |
| 3936 | 0.2580 | You can add any elements (a dashboard, report, ale... |
| 3937 | 0.2579 | server\instance name In this case the "Who", "Work... |
| 3938 | 0.2579 | StartsWith EndsWith Contains (default) DoesNotCont... |
| 3939 | 0.2578 | ◦◦ *TestVM* — exclude VMs with names containing Te... |
| 3940 | 0.2576 | Opens the Send Send Reminders Reminders window, wh... |
| 3941 | 0.2575 | When prompted to c onfirm granting, click Yes. Ste... |
| 3942 | 0.2574 | Click Add and complete the following fields: User ... |
| 3943 | 0.2574 | Thus, s/he configures the product not to monitor t... |
| 3944 | 0.2573 | Option Description General Name Update a plan name... |
| 3945 | 0.2572 | Table 1: Option Description Logging level Select I... |
| 3946 | 0.2572 | The default value is 3600 seconds, i.e., 1 hour. C... |
| 3947 | 0.2570 | Lines that start with the # sign are treated as co... |
| 3948 | 0.2569 | Enter the IP subrange you want to exclude, and cli... |
| 3949 | 0.2567 | Information on alerts that are older than 1 month ... |
| 3950 | 0.2567 | The following audit permissions must be set to "Su... |
| 3951 | 0.2567 | RID is included in output A ctivity Records only. ... |
| 3952 | 0.2565 | However, if you have specified a time period for A... |
| 3953 | 0.2565 | Successful Enabling this option on public shares w... |
| 3954 | 0.2564 | To find out a field name in ServiceNow, switch to ... |
| 3955 | 0.2564 | Failed read attempts The Auditing Entry below show... |
| 3956 | 0.2564 | Failed read attempts The Auditing Entry below show... |
| 3957 | 0.2564 | Older tickets requests are cleared. NOTE: Stop and... |
| 3958 | 0.2563 | In the left pane, navigate to Forest: <forest_name... |
| 3959 | 0.2563 | Helps find out who was trying to access your priva... |
| 3960 | 0.2561 | <Who>Administrator</Who><DataSource>S harePoint</D... |
| 3961 | 0.2560 | Each guide contains detailed instructions for depl... |
| 3962 | 0.2560 | Unavailable Failed to connect to the database. Upg... |
| 3963 | 0.2560 | Licenses – Example: Microsoft 365 E1 – The user or... |
| 3964 | 0.2560 | v10.7 For example, you can create a gMSA using the... |
| 3965 | 0.2557 | omitarlist.txt SELECT statements auditing and SQL ... |
| 3966 | 0.2555 | These settings are global, that is, they will be a... |
| 3967 | 0.2555 | In the dialog that opens, specify the OUs that you... |
| 3968 | 0.2555 | This configuration procedure involves creation of ... |
| 3969 | 0.2555 | Enter the IP subrange you want to exclude, and cli... |
| 3970 | 0.2555 | Enter the IP subrange you want to exclude, and cli... |
| 3971 | 0.2554 | This SQL Server will be used as default host for A... |
| 3972 | 0.2554 | See the State–In–Time Reports topic for additional... |
| 3973 | 0.2554 | See the State–In–Time Reports topic for additional... |
| 3974 | 0.2554 | See the State–In–Time Reports topic for additional... |
| 3975 | 0.2553 | • DHCP configuration—Enables auditing of DHCP conf... |
| 3976 | 0.2552 | For that, under Specify monitoring restrictions, s... |
| 3977 | 0.2550 | Step 2 – In the Help Protect your computer with Wi... |
| 3978 | 0.2550 | Use this option to supervise access to files conta... |
| 3979 | 0.2550 | Do not specify a default file share mapped to a lo... |
| 3980 | 0.2549 | To modify most plan settings, you must be assigned... |
| 3981 | 0.2548 | With enabled HTTPS, provide the computer name as i... |
| 3982 | 0.2547 | Successful changes v10.7 Configure Object-level ac... |
| 3983 | 0.2547 | See the Monitoring Planstopic for additional infor... |
| 3984 | 0.2546 | Table 1: File Description Syntax adomiteventuserli... |
| 3985 | 0.2546 | * - any machine with a 3-character name or longer ... |
| 3986 | 0.2544 | You can configur e Auditor to publish reports to f... |
| 3987 | 0.2543 | For example, you can run the add-on on the compute... |
| 3988 | 0.2543 | You can Specify a host or network resource select ... |
| 3989 | 0.2542 | Modify the timeframe to narrow down the results. T... |
| 3990 | 0.2542 | The subscription (email attachment or file uploade... |
| 3991 | 0.2542 | Step 2 – Right-click Registry and select New > Reg... |
| 3992 | 0.2541 | Once you completed all filters, click Preview on t... |
| 3993 | 0.2540 | Click Add to create an alert for non-owner mailbox... |
| 3994 | 0.2540 | cmdlet.attrname For example: Set-User Set-ContactS... |
| 3995 | 0.2540 | Note that the new monitoring scope restrictions ap... |
| 3996 | 0.2540 | If Modern Authentication is used: ◦ Microsoft Entr... |
| 3997 | 0.2539 | Please note that modern authentication must alread... |
| 3998 | 0.2539 | Click the Details link to examine the product log.... |
| 3999 | 0.2538 | v10.7 How this change is Item Action Audited repor... |
| 4000 | 0.2538 | JSON may contain a ContinuationMark object. Each F... |
| 4001 | 0.2537 | See the following Microsoft article for more infor... |
| 4002 | 0.2537 | If you want to use a specific account (other than ... |
| 4003 | 0.2536 | SenderSleepTime 30 Specifies retry interval in sec... |
| 4004 | 0.2534 | What Shows the path to the modified AD object. Tab... |
| 4005 | 0.2533 | Upon s electing Combination of file and share perm... |
| 4006 | 0.2533 | Upon s electing Combination of file and share perm... |
| 4007 | 0.2533 | Upon s electing Combination of file and share perm... |
| 4008 | 0.2533 | Window Application Run As: <account_name> Standard... |
| 4009 | 0.2531 | Specify a user account. Make sure the user has suf... |
| 4010 | 0.2531 | Information specific to the data source, e.g., ass... |
| 4011 | 0.2531 | Supported Data Sources Configure Auditor service a... |
| 4012 | 0.2530 | This filter can be helpful when you are looking fo... |
| 4013 | 0.2530 | SQL Server When planning for SQL Server that will ... |
| 4014 | 0.2528 | v10.7 Step 1 – Navigate to the Access Reviews inst... |
| 4015 | 0.2528 | Click Finish to restart the add-on service so that... |
| 4016 | 0.2527 | Details Shows the before and after values of the m... |
| 4017 | 0.2524 | You can use a wildcard (*) to replace any number o... |
| 4018 | 0.2522 | The Long-Term Archive widget—Helps you to estimate... |
| 4019 | 0.2522 | If you are going to use a gMSA to access Audit Dat... |
| 4020 | 0.2522 | Step 7 – When done, click Finish. Define Parameter... |
| 4021 | 0.2522 | Access is denied.” error. member of the local Admi... |
| 4022 | 0.2522 | v10.7 Adjust Active Directory Tombstone Lifetime (... |
| 4023 | 0.2520 | All members of the local Administrators group are ... |
| 4024 | 0.2519 | Select one of the custom reports in the list and r... |
| 4025 | 0.2517 | Auditor supports automated size calculation for al... |
| 4026 | 0.2517 | ◦◦ If you plan to process Active Directory Deleted... |
| 4027 | 0.2515 | Step 2 – Select the required data source and click... |
| 4028 | 0.2515 | When a successful status is indicated, assigned ow... |
| 4029 | 0.2514 | For JSON, a response body contains the ActivityRec... |
| 4030 | 0.2514 | v10.7 The dashboards includes the following sectio... |
| 4031 | 0.2513 | Helps find out who was trying to access your priva... |
| 4032 | 0.2513 | Thus, s/he configures the product not to monitor t... |
| 4033 | 0.2512 | Use other options (Computer name, IP address range... |
| 4034 | 0.2512 | To view all groups the account is member of, expor... |
| 4035 | 0.2512 | The credentials are case sensitive. Specify the ac... |
| 4036 | 0.2512 | If necessary, enable threshold to trigger the new ... |
| 4037 | 0.2511 | Define the Log On As a Service Policy On the Logon... |
| 4038 | 0.2510 | Make Search Results Actionnable You can export you... |
| 4039 | 0.2510 | Provide this account in the monitoring plan wizard... |
| 4040 | 0.2509 | The hyperlink will open the Entitlement Reviews in... |
| 4041 | 0.2508 | To configure audit settings for the CIFS fi le sha... |
| 4042 | 0.2508 | Template Name Message Type Description Reminds own... |
| 4043 | 0.2507 | In such cases, contact your network administrator ... |
| 4044 | 0.2507 | Adjust the audit policy settings using the Active ... |
| 4045 | 0.2506 | DNS resource records—Enables auditing of all types... |
| 4046 | 0.2506 | Depending on the selected virtual appliance config... |
| 4047 | 0.2505 | See Configure Oracle Database for Auditing topic f... |
| 4048 | 0.2505 | Fine Grained Auditing Oracle Database 23c, 21c, 19... |
| 4049 | 0.2504 | Do not specify a default file share mapped to a lo... |
| 4050 | 0.2503 | Alerts use the same interface and logic as search.... |
| 4051 | 0.2503 | Execute... cluster1::> system services firewall po... |
| 4052 | 0.2501 | Open the File Server REST API Explorer client usin... |
| 4053 | 0.2500 | See the Data C ollecting Account topic for additio... |
| 4054 | 0.2500 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 4055 | 0.2498 | Otherwise, XMLTable 1: Parameter Mandatory Descrip... |
| 4056 | 0.2498 | No items have been added to this Empty data source... |
| 4057 | 0.2496 | Activity record stands for one operable chunk of i... |
| 4058 | 0.2496 | Allow outbound connections to remote ports on the ... |
| 4059 | 0.2496 | Switch to HTTP APIAdminTool.exe api http Netwrix r... |
| 4060 | 0.2494 | Term Archive. Error validating request parameters ... |
| 4061 | 0.2494 | Table 1: Report Description File Servers Activity ... |
| 4062 | 0.2491 | Review the following for additional information: R... |
| 4063 | 0.2489 | Activity Record for groups membership $deltaToken=... |
| 4064 | 0.2487 | If you want to reopen closed ticke ts, you must be... |
| 4065 | 0.2487 | v10.7 Add Exclusion Follow the steps to add exclus... |
| 4066 | 0.2487 | Allows specifying report delivery schedule (daily,... |
| 4067 | 0.2484 | v10.7 Option Description To specify what data chan... |
| 4068 | 0.2483 | The default values is 900 seconds, i.e., 15 minute... |
| 4069 | 0.2483 | In the right pane, click Configure, next to Advanc... |
| 4070 | 0.2482 | In the right pane, go to the Intelligence s ection... |
| 4071 | 0.2482 | Table 1: Option Description Example All Data Selec... |
| 4072 | 0.2482 | Table 1: Option Description Example All Data Selec... |
| 4073 | 0.2481 | However, to ensure that Reporting Services is prop... |
| 4074 | 0.2481 | A custom account must be granted the same permissi... |
| 4075 | 0.2479 | As you inspect anomalies and respond to threats, u... |
| 4076 | 0.2479 | State description ORCapacity error Size limit for ... |
| 4077 | 0.2478 | For example, an unknown user was added to the Admi... |
| 4078 | 0.2477 | RADIUSPassword Current user credentials Provide a ... |
| 4079 | 0.2476 | You should also provide links to the appropriate t... |
| 4080 | 0.2476 | with a huge amount of objects, so s/he does not wa... |
| 4081 | 0.2476 | You will also need to configure Exchange Administr... |
| 4082 | 0.2475 | Step 9 – Open Microsoft Entra ID portal and remove... |
| 4083 | 0.2472 | will be reported, but the Who value will be "syste... |
| 4084 | 0.2472 | Step 4 – Click Add and enter the name of the user ... |
| 4085 | 0.2471 | Service accounts (svc_%) must be skipped in the re... |
| 4086 | 0.2470 | Click Customize to edit the notification template,... |
| 4087 | 0.2469 | Review and Pin Risks Follow the steps to review ri... |
| 4088 | 0.2469 | If you have several monitoring plans for monitorin... |
| 4089 | 0.2469 | The add-on was renamed due to HPE acquisition by M... |
| 4090 | 0.2468 | Check and process the alert queue every N seconds;... |
| 4091 | 0.2468 | APIAdminTool.exe api https Switch to HTTPS Run thi... |
| 4092 | 0.2467 | Shows the name of the account under which the Who ... |
| 4093 | 0.2467 | • It is recommended to assign the API Member accou... |
| 4094 | 0.2467 | You can use HTML tags when editing a template. Att... |
| 4095 | 0.2467 | Step 9 – To create a self-signed certificate to be... |
| 4096 | 0.2467 | The RADIUS server The account collecting RADIUS lo... |
| 4097 | 0.2466 | or moved, and emails sent. Since you are intereste... |
| 4098 | 0.2466 | The View Responses window closes. Step 5 – Repeat ... |
| 4099 | 0.2465 | See the Notification to Owners topic for additiona... |
| 4100 | 0.2464 | IncludeDataSourceToMakeEventId * True Defines whet... |
| 4101 | 0.2463 | Specify the time period, in seconds. During this t... |
| 4102 | 0.2461 | Internal parameter. Check and CheckAlertQueueInter... |
| 4103 | 0.2459 | The account collecting RADIUS logon events is memb... |
| 4104 | 0.2456 | SetDataSourceAsEventSource False Defines whether t... |
| 4105 | 0.2456 | • File shares—Enables auditing of created / remove... |
| 4106 | 0.2452 | Changes (per transaction) to collect and report: I... |
| 4107 | 0.2452 | File Servers Dell Isilon Dell VNX VNXe NetApp Wind... |
| 4108 | 0.2451 | The OU itself, however, will not be monitored, mea... |
| 4109 | 0.2450 | Adds the full alert text to Work notes, including ... |
| 4110 | 0.2450 | It means that data collection from at least one en... |
| 4111 | 0.2450 | It means that data collection from at least one en... |
| 4112 | 0.2449 | The syntax greatly depends on the tool you use. St... |
| 4113 | 0.2449 | The first thing that should be done is to configur... |
| 4114 | 0.2447 | See SharePoint for more information. ◦ The user th... |
| 4115 | 0.2446 | Use U nified and Standard audit policies to keep t... |
| 4116 | 0.2446 | For example: OracleUser as sysdba Table 1: To moni... |
| 4117 | 0.2446 | Add-on Internal Parameters Internal parameters lis... |
| 4118 | 0.2444 | For that, set up the TrustedHosts list: ◦ to inclu... |
| 4119 | 0.2442 | Delete event Yes Message with subject <...> was mo... |
| 4120 | 0.2442 | Table 1: Name Value Description assignment_ group ... |
| 4121 | 0.2441 | Specify the time period, in seconds. UpdateInterva... |
| 4122 | 0.2439 | Unless specified, the add-on runs with the current... |
| 4123 | 0.2439 | Step 3 – Double-click the Log on as a service poli... |
| 4124 | 0.2438 | Users with the Configurator role can create plans ... |
| 4125 | 0.2438 | Note that the new monitoring scope restrictions ap... |
| 4126 | 0.2434 | Not in group This operator relates to the Who filt... |
| 4127 | 0.2433 | For this report to function properly, you must ena... |
| 4128 | 0.2433 | Step 6 – Select what type of data you want to excl... |
| 4129 | 0.2433 | Step 6 – Select what type of data you want to excl... |
| 4130 | 0.2432 | Expand the Recipients list and click Add to add mo... |
| 4131 | 0.2432 | Table 1: Parameter Description proxyaddress Specif... |
| 4132 | 0.2432 | Follow the steps to configure Audit Object Access ... |
| 4133 | 0.2429 | In this case, this user will have the most extende... |
| 4134 | 0.2429 | Filters You can narrow your reporting scope using ... |
| 4135 | 0.2429 | Add/Remove programs—Enables auditing of installed ... |
| 4136 | 0.2428 | File Description Syntax monitoring plan name,serve... |
| 4137 | 0.2428 | See the Resource Owners Overview topic for additio... |
| 4138 | 0.2427 | that are less important. See Configure Fine Graine... |
| 4139 | 0.2427 | Table 1: Option Description When auditing file ser... |
| 4140 | 0.2425 | For example, to report on the database hosted on s... |
| 4141 | 0.2424 | NOTE: If you are going to configure monitoring rul... |
| 4142 | 0.2420 | Select the necessary actions (successful or failed... |
| 4143 | 0.2420 | Applicable packages for each Oracle Database versi... |
| 4144 | 0.2419 | The resource is returned to a ‘Waiting’ status, re... |
| 4145 | 0.2419 | All Users Used for previous values in users Activi... |
| 4146 | 0.2419 | fields. The MonitoringPlan element contains sub-el... |
| 4147 | 0.2417 | Default value is -1 (switch off concurrent forward... |
| 4148 | 0.2416 | Add-on running on the same machine as SCVMM Manage... |
| 4149 | 0.2415 | For that, the user account will need an administra... |
| 4150 | 0.2415 | Assign Permission To Read the Registry Key NOTE: T... |
| 4151 | 0.2412 | v10.7 Define Parameters Before running or scheduli... |
| 4152 | 0.2412 | v10.7 Parameter Mandatory Description Add this par... |
| 4153 | 0.2412 | Execute... AUDIT SELECT,INSERT,DELETE,UPDATE,RENAM... |
| 4154 | 0.2411 | object type:property: When a new object is created... |
| 4155 | 0.2409 | Delete folder Yes Folder <...> was moved from fold... |
| 4156 | 0.2409 | JSON-formatted Continuation mark includes the fi e... |
| 4157 | 0.2408 | A backslash (\) must be put in front of (*), (? ),... |
| 4158 | 0.2408 | When a new object is created, Auditor does not sho... |
| 4159 | 0.2408 | See the Create Alertstopic for additional informat... |
| 4160 | 0.2407 | Configure Exchange Online State-in-Time Modern Aut... |
| 4161 | 0.2407 | See the following Microsoft article for more infor... |
| 4162 | 0.2407 | Remember that administrative hidden shares like de... |
| 4163 | 0.2407 | Message No string Message is included in output Ac... |
| 4164 | 0.2405 | See Download Client Credentials (Wallets) for more... |
| 4165 | 0.2404 | Follow the steps to configure Microsoft 365 tenant... |
| 4166 | 0.2404 | Check "Failed" next to the following permissions: ... |
| 4167 | 0.2404 | managers, chief info rmation security officer, and... |
| 4168 | 0.2403 | Resources — Select resources to be included in the... |
| 4169 | 0.2402 | You can use group Managed Service Accounts (gMSA) ... |
| 4170 | 0.2400 | Shows the before and after values of the modified ... |
| 4171 | 0.2399 | Only alerts grouped by the Who parameter can be in... |
| 4172 | 0.2398 | For example, a new alert is triggered —the service... |
| 4173 | 0.2396 | Table 1: Interface Purpose Opened By Accessible To... |
| 4174 | 0.2396 | v10.7 You can also use the Search window to examin... |
| 4175 | 0.2396 | This is determined by the following formula: (Lice... |
| 4176 | 0.2395 | In the Change Status dialog, set the status to "re... |
| 4177 | 0.2395 | For example, computer name or workgroup changes. H... |
| 4178 | 0.2394 | Risk Assessment, Compliance Mapping, Live News, an... |
| 4179 | 0.2393 | Opens the Send Reminders window, which indicates a... |
| 4180 | 0.2392 | v10.7 Configuration of government Microsoft 365 te... |
| 4181 | 0.2391 | In this scenario, you only deploy Auditor Server a... |
| 4182 | 0.2391 | Table 1: Option Description Example All Data Selec... |
| 4183 | 0.2391 | Modify the AccessInformationCenter.Service.exe.Con... |
| 4184 | 0.2390 | Table 1: Requirement Comment Microsoft Entra ID ap... |
| 4185 | 0.2390 | You can click Browse to select a computer from the... |
| 4186 | 0.2389 | We welcome any feedback and ideas you might have. ... |
| 4187 | 0.2389 | v10.7 Option Description When the retention period... |
| 4188 | 0.2387 | See the Delete Review Window topic for additional ... |
| 4189 | 0.2387 | Lines that start with the # sign are treated as co... |
| 4190 | 0.2387 | Step 12 – Click Save to save your changes. v10.7 T... |
| 4191 | 0.2387 | ◦ .Net Framework 3.5 SP1 is installed on the compu... |
| 4192 | 0.2385 | Clicking the tile opens the Behavior Anomalies das... |
| 4193 | 0.2384 | Table 1: Port Protocol Source Target Purpose 389 T... |
| 4194 | 0.2384 | Port Protocol Source Target Purpose LDAP Netwrix A... |
| 4195 | 0.2384 | Specify the account for collecting data A custom a... |
| 4196 | 0.2383 | Table 1: Option Description Slide the switch under... |
| 4197 | 0.2382 | You should specify only the account name in the do... |
| 4198 | 0.2380 | Source Specify this parameter if you want to be al... |
| 4199 | 0.2379 | Follow the steps of the wizard to configure connec... |
| 4200 | 0.2378 | Step 6 – If the SMTP settings are configured corre... |
| 4201 | 0.2376 | It can be any custom name, for example a server na... |
| 4202 | 0.2376 | See the Alertstopic for a dditional information. T... |
| 4203 | 0.2375 | Specify custom connection parameters Make sure to ... |
| 4204 | 0.2373 | Click Show user activity below the total risk scor... |
| 4205 | 0.2373 | This automatically downloads the file. See the Dat... |
| 4206 | 0.2373 | In group/Not in group filters don’t not process gr... |
| 4207 | 0.2372 | The default value is 3600 seconds, i.e., 1 hour. S... |
| 4208 | 0.2372 | Check and process the alert queue every N seconds;... |
| 4209 | 0.2372 | count=Number No Add this parameter to define the n... |
| 4210 | 0.2371 | User name Enter a user name for the SMTP authentic... |
| 4211 | 0.2370 | Specify the Audit Database retention period. This ... |
| 4212 | 0.2370 | Step 1 – Navigate to the target file share, right-... |
| 4213 | 0.2369 | Wrong HTTP request was sent (any request was sent ... |
| 4214 | 0.2368 | For example, it helps monitor the usage of SUDO as... |
| 4215 | 0.2368 | The maximum number of ticket requests the service ... |
| 4216 | 0.2367 | Define Parameters Before running or scheduling the... |
| 4217 | 0.2367 | Define Parameters Before running or scheduling the... |
| 4218 | 0.2366 | Have there been any unusual spikes in failed activ... |
| 4219 | 0.2365 | v10.7 Local TCP Port 9003 is opened for inbound co... |
| 4220 | 0.2365 | Infrastructure Table 1: Risk Assessment formula De... |
| 4221 | 0.2364 | User name Table 1: Option Description • Password S... |
| 4222 | 0.2364 | Table 1: Hardware component Evaluation, PoC or sta... |
| 4223 | 0.2364 | ◦ If necessary, add the IP addresses of required A... |
| 4224 | 0.2364 | See the Selected Resources Window topic for additi... |
| 4225 | 0.2364 | v10.7 Track... Steps... Set-Mailbox -Identity {0} ... |
| 4226 | 0.2363 | Example: Shows the path to Parent OU/container acc... |
| 4227 | 0.2361 | In this case, Auditor will v10.7 Option Descriptio... |
| 4228 | 0.2360 | Step 6 – Click Install. Table 1: Option Descriptio... |
| 4229 | 0.2358 | In case all required components have been already ... |
| 4230 | 0.2357 | Example: WALLET_LOCATION = (SOURCE = (METHOD = fil... |
| 4231 | 0.2357 | Helps find out who made changes to your fi les, in... |
| 4232 | 0.2356 | You can use full or relative path. v10.7 Parameter... |
| 4233 | 0.2356 | v10.7 Option Description Ensure that the requireme... |
| 4234 | 0.2356 | v10.7 It has the following pages: Console Access P... |
| 4235 | 0.2355 | Source If you need to specify several sources, you... |
| 4236 | 0.2354 | Process user accounts Select this checkbox to audi... |
| 4237 | 0.2354 | See SharePoint for more information. v10.7 The use... |
| 4238 | 0.2353 | Table 1: Item Action Audited How this change is re... |
| 4239 | 0.2353 | The Action filt er in the Advanced mode contains a... |
| 4240 | 0.2353 | Soft-deleted items are Admin moved to the Recovera... |
| 4241 | 0.2353 | Follow the steps to edit your plan settings: Step ... |
| 4242 | 0.2352 | The default period is set to 30 days. Select the r... |
| 4243 | 0.2351 | Microsoft System Center Virtual Machine Manager (S... |
| 4244 | 0.2351 | Assume, each department has its own field of respo... |
| 4245 | 0.2350 | * Inactive User Tracker Auditor Inactive User Trac... |
| 4246 | 0.2350 | Configuration If you are using Oracle Wallet to co... |
| 4247 | 0.2349 | Thus, changes made to your Active Directory domain... |
| 4248 | 0.2349 | When configuring the IncludeDataSourceToMakeEventI... |
| 4249 | 0.2346 | State-in-Time Select to configure Auditor to exclu... |
| 4250 | 0.2346 | State-in-Time Select to configure Auditor to exclu... |
| 4251 | 0.2346 | State-in-Time Select to configure Auditor to exclu... |
| 4252 | 0.2346 | Password Enter a password. Table 2: Option Descrip... |
| 4253 | 0.2344 | When finished, run the gpupdate /force command to ... |
| 4254 | 0.2344 | You can use * for cmdlets and their parameters. Li... |
| 4255 | 0.2343 | NOTE: Please consider the following: Logon activit... |
| 4256 | 0.2343 | Exports There are two export buttons above a table... |
| 4257 | 0.2341 | Check if your Oracle database has already been mig... |
| 4258 | 0.2340 | *) General HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001... |
| 4259 | 0.2338 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 4260 | 0.2336 | v10.7 Monitored Sign-In types: Delegate Admin Dele... |
| 4261 | 0.2335 | Step 4 – Click Add to add a new principal. You can... |
| 4262 | 0.2335 | See the Role-Based Access and Delegationtopic for ... |
| 4263 | 0.2334 | NOTE: If you want to reopen closed tickets, you mu... |
| 4264 | 0.2333 | Select File permissions option too if you want to ... |
| 4265 | 0.2333 | Select File permissions option too if you want to ... |
| 4266 | 0.2332 | between an object type and a property, the whole e... |
| 4267 | 0.2331 | between an object type and a property, the whole e... |
| 4268 | 0.2330 | Column omitpathlist.txt Specify the resource paths... |
| 4269 | 0.2330 | Configure Auditor service accounts. Software Requi... |
| 4270 | 0.2329 | 22.. On the Add Subscription page, complete the fo... |
| 4271 | 0.2328 | Thus, changes made to your Active Directory domain... |
| 4272 | 0.2328 | Copy it to a safe location. See the following Micr... |
| 4273 | 0.2327 | Send alert for <...> activity records within <...>... |
| 4274 | 0.2327 | Default retention period is 120 months. Audit data... |
| 4275 | 0.2326 | Depending on the type of the object you want to ex... |
| 4276 | 0.2326 | Step 4 – On the right, double-click the User Right... |
| 4277 | 0.2324 | Follow the steps to exclude data from Exchange Onl... |
| 4278 | 0.2324 | Slide the Table 1: Option Description switch to tu... |
| 4279 | 0.2324 | The product collects data from vCenter. Localos us... |
| 4280 | 0.2323 | See the Create a Review topic for additional infor... |
| 4281 | 0.2323 | omitscreadaccesslist.txt Contains a list of site c... |
| 4282 | 0.2323 | Example: CN=MJones,CN=Users,DC=enterprisedc1,DC=en... |
| 4283 | 0.2322 | PCIDSS. This filter shows activity records collect... |
| 4284 | 0.2322 | Step 6 – Click Install. Step 7 – When done, click ... |
| 4285 | 0.2321 | A Security Officer wants to monitor a file share, ... |
| 4286 | 0.2321 | – any machine with a 5-character name ? * - any ma... |
| 4287 | 0.2321 | If you are using Oracle Real Application Clusters ... |
| 4288 | 0.2320 | If the retention period is set to 0, the following... |
| 4289 | 0.2320 | Execute the following command... To create audit p... |
| 4290 | 0.2319 | To.. Do.. Click on a plan name. You will see all d... |
| 4291 | 0.2319 | The Active Directory service account password has ... |
| 4292 | 0.2318 | Format Example XML <Who>Admin</Who><Who>Analyst</W... |
| 4293 | 0.2317 | A custom account must be granted the same permissi... |
| 4294 | 0.2317 | It is assumed that you have a good understanding o... |
| 4295 | 0.2316 | User (domain\account) – select a specific user to ... |
| 4296 | 0.2316 | For security reasons, it is recommended to configu... |
| 4297 | 0.2315 | If you plan to audit an SQL Server for data change... |
| 4298 | 0.2315 | For example, to report on the database hosted on s... |
| 4299 | 0.2315 | Below is an example of the configuration: 11.. Nav... |
| 4300 | 0.2315 | Data Collection Accounts should meet the following... |
| 4301 | 0.2314 | A backslash (\) must be put in front of (*), (? ),... |
| 4302 | 0.2314 | Facility Netwrix recommends using default values. ... |
| 4303 | 0.2313 | See the Notification Options topic for additional ... |
| 4304 | 0.2311 | IP Range Complete the following fields: Table 1: O... |
| 4305 | 0.2310 | Qtree Security must be configured. The volume wher... |
| 4306 | 0.2307 | Configure the following: • Notify users if someone... |
| 4307 | 0.2306 | Then click Next to continue. Step 4 – On the Summa... |
| 4308 | 0.2305 | User type userType Example: "Member" A string valu... |
| 4309 | 0.2304 | Specify account inactivity period, after which a u... |
| 4310 | 0.2304 | The console will look similar to the following: Wi... |
| 4311 | 0.2304 | This value is set to 1 by default, which means tha... |
| 4312 | 0.2303 | A Security Officer wants to monitor a file share t... |
| 4313 | 0.2302 | Clear imported data Select to delete all previousl... |
| 4314 | 0.2300 | The modifications to the HTML email templates are ... |
| 4315 | 0.2300 | For example: ,*,*notepad.exe Windows File Share Co... |
| 4316 | 0.2300 | Select the desired active review(s) and click Send... |
| 4317 | 0.2298 | * You can use a wildcard (*) to replace any number... |
| 4318 | 0.2298 | Table 1: Error in PowerShell Resolution Select the... |
| 4319 | 0.2297 | object_type_name Available object types can be fou... |
| 4320 | 0.2296 | Remember that administrative hidden shares like de... |
| 4321 | 0.2296 | Admin A message or any of its pro perties Admin Co... |
| 4322 | 0.2296 | omituserlist.txt Contains a list of users you want... |
| 4323 | 0.2295 | The list of containers does not include child doma... |
| 4324 | 0.2295 | Helps find out who made Successful changes to your... |
| 4325 | 0.2295 | Instead of creating a new ticke t, reopen an exist... |
| 4326 | 0.2295 | Step 2 – Receive the response. Activity Records ar... |
| 4327 | 0.2295 | However, in some cases, organizations need to prov... |
| 4328 | 0.2294 | See the Run the Add-On with PowerShell topic for a... |
| 4329 | 0.2293 | Specify additional information to include in repor... |
| 4330 | 0.2290 | NEWYORKSRV10:81. If you do not want the server nam... |
| 4331 | 0.2287 | Defines a ticket status once it is reopened. By de... |
| 4332 | 0.2286 | Possible values: Empty—Check the certificate via W... |
| 4333 | 0.2284 | DOMAIN\username v10.7 File Description Syntax /Tes... |
| 4334 | 0.2284 | If you plan to collect state-in-time data from SQL... |
| 4335 | 0.2284 | When adding a DFS file share for auditing, specify... |
| 4336 | 0.2282 | The review for this resource is now complete. You ... |
| 4337 | 0.2280 | The My Reviews interface is available to any domai... |
| 4338 | 0.2278 | Cores Per Processor Restore from snapshot Memory S... |
| 4339 | 0.2276 | See the View and Search Collected Data topic for a... |
| 4340 | 0.2276 | Certificate Thumbprint AB:BB:CC—Check Auditor Serv... |
| 4341 | 0.2276 | When the selected threshold exceeded, an alert wil... |
| 4342 | 0.2274 | Table 2: Entry in EventData Activity Record field ... |
| 4343 | 0.2273 | Assign Permission to Read the Registry Key This pe... |
| 4344 | 0.2272 | A custom account must be granted the same permissi... |
| 4345 | 0.2271 | v10.7 Option Description Example Select if you wan... |
| 4346 | 0.2271 | v10.7 Option Description Example Select if you wan... |
| 4347 | 0.2269 | When the Review Administrator creates a new review... |
| 4348 | 0.2269 | The My Reviews interface is available if the logge... |
| 4349 | 0.2267 | Then you will need to download that new version. T... |
| 4350 | 0.2266 | These templates are designed to make the message v... |
| 4351 | 0.2265 | Consider the following: To exclude a single VM, pr... |
| 4352 | 0.2264 | This refers to the specified shared folder, its su... |
| 4353 | 0.2263 | Enter the IP subrange you want to exclude, and cli... |
| 4354 | 0.2262 | See Permissions for VMware Server Auditing topic f... |
| 4355 | 0.2262 | As an account for accessing Audit Databases. See R... |
| 4356 | 0.2258 | Start data collection manually Data collection wil... |
| 4357 | 0.2258 | v10.7 Step 6 – On the Summary page, review the set... |
| 4358 | 0.2258 | Step 4 – Review your search results. Step 5 – Navi... |
| 4359 | 0.2257 | If for some reason the product was unable to grant... |
| 4360 | 0.2257 | Lines that start with the # sign are treated as co... |
| 4361 | 0.2256 | Follow the steps to enable Exchange Online Auto Au... |
| 4362 | 0.2255 | See the following table for the certain reports: T... |
| 4363 | 0.2254 | Specify email address to be included in the list a... |
| 4364 | 0.2253 | 55.. Permissions-related considerations: v10.7 For... |
| 4365 | 0.2253 | When Yes dateTime The moment when the change occur... |
| 4366 | 0.2252 | Administrative hidden shares like default system r... |
| 4367 | 0.2252 | Filters You can narrow your reporting scope using ... |
| 4368 | 0.2249 | This will not affect the reports or data searches ... |
| 4369 | 0.2249 | If a ticket flood limit is reached, the service wr... |
| 4370 | 0.2248 | Obtain the Tenant Name Follow the steps to obtain ... |
| 4371 | 0.2248 | Complete the following fields: Option Description ... |
| 4372 | 0.2246 | This refers to the specified shared folder, its su... |
| 4373 | 0.2245 | See the Microsoft Entra ID topic for additional in... |
| 4374 | 0.2241 | Select Edit under Apply tags to associate tags wit... |
| 4375 | 0.2241 | Consider the following: By default, the add-on doe... |
| 4376 | 0.2240 | Oracle Object modification under Privileges and ob... |
| 4377 | 0.2239 | Select Edit under Apply tags to associate tags wit... |
| 4378 | 0.2239 | See the Add New Resource Wizard topic for addition... |
| 4379 | 0.2239 | To open the Long-Term Archive settings, click the ... |
| 4380 | 0.2238 | Workstation Limits your search to an originating w... |
| 4381 | 0.2237 | Periodic time interval for reading EventsReadingPe... |
| 4382 | 0.2236 | Program/script Input "Powershell.exe". Add argumen... |
| 4383 | 0.2235 | Use this tile to inspect the trend. v10.7 Top 5 al... |
| 4384 | 0.2234 | • -1 — disable timeout. Table 2: Event Description... |
| 4385 | 0.2233 | See theData C ollecting Account topic for addition... |
| 4386 | 0.2231 | For example, "\com\Corp\Users\Departments\IT\Usern... |
| 4387 | 0.2231 | For example, "\com\Corp\Users\Departments\IT\Usern... |
| 4388 | 0.2231 | Adjust video duration Limit video file length by a... |
| 4389 | 0.2231 | Step 7 – In the Reporting Services Configuration C... |
| 4390 | 0.2230 | Revoke a role assignment Click next to the user. S... |
| 4391 | 0.2230 | If a similar alert occurs in less than N seconds, ... |
| 4392 | 0.2230 | Currently, the cyberark-v2.xml rule file is shippe... |
| 4393 | 0.2228 | To force basic audit policies to be ignored and pr... |
| 4394 | 0.2228 | You can also: Select a particular computer type to... |
| 4395 | 0.2227 | See the N otifications Page topic for additional i... |
| 4396 | 0.2227 | This will not affect the Reports functionality and... |
| 4397 | 0.2226 | Use default SQL Server settings Select this option... |
| 4398 | 0.2225 | Data Collecting Account Scope By default, Auditor ... |
| 4399 | 0.2224 | If there is no such tab, it means a wrong security... |
| 4400 | 0.2224 | Make sure this account is granted the Content Mana... |
| 4401 | 0.2224 | If there is no such tab, it means a wrong security... |
| 4402 | 0.2223 | Example: mydomain\user1. You can provide the "Syst... |
| 4403 | 0.2222 | Step 12 – Type repadmin /syncall command and press... |
| 4404 | 0.2220 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 4405 | 0.2216 | Select this option for users to be notified three ... |
| 4406 | 0.2215 | Your firewall configura tion depends on network se... |
| 4407 | 0.2215 | Open the Group Policy Management console on the do... |
| 4408 | 0.2213 | Certificate Thumbprint AB:BB:CC—Check Auditor Serv... |
| 4409 | 0.2213 | The computer where the script will be executed • P... |
| 4410 | 0.2213 | Step 8 – Click Install. Step 9 – When done, click ... |
| 4411 | 0.2212 | — v10.7 Hardware component Minimum required Recomm... |
| 4412 | 0.2212 | You v10.7 can always adjust risk scores over time ... |
| 4413 | 0.2210 | During this time period, the service treats simila... |
| 4414 | 0.2209 | For Security Team & Administrator The Resource Own... |
| 4415 | 0.2208 | Step 4 – In the Advanced Security Settings for SOF... |
| 4416 | 0.2208 | As you investigate suspicious activity and review ... |
| 4417 | 0.2208 | The Review Details page opens. v10.7 Step 2 – Sele... |
| 4418 | 0.2208 | Navigate to Reports and generate a report. Apply r... |
| 4419 | 0.2207 | To disable filtering for these fields, specify an ... |
| 4420 | 0.2206 | Example: "Michael Jones" • Domain\User. Example: e... |
| 4421 | 0.2204 | Monitoring plan name,resource path, executable pat... |
| 4422 | 0.2203 | Use the omitlogonlist.txt to exclude logon activit... |
| 4423 | 0.2202 | You can enable predefined alerts or create your cu... |
| 4424 | 0.2201 | omitexchangeserverlist.txt Specify the Microsoft E... |
| 4425 | 0.2200 | Step 3 – It will be necessary to add your Console ... |
| 4426 | 0.2199 | Table 1: Description Failed Use this option to det... |
| 4427 | 0.2198 | omitstorelist.txt Contains a list of SQL Server ob... |
| 4428 | 0.2196 | To force basic audit policies to be ignored and pr... |
| 4429 | 0.2195 | See the Settings for Data Collection topic for mor... |
| 4430 | 0.2194 | Step 4 – Click Add and enter the name of the user ... |
| 4431 | 0.2194 | After the upgrade, all alerts with previously conf... |
| 4432 | 0.2191 | Wildcard (*) is supported. For example, to report ... |
| 4433 | 0.2190 | Manage resource Administrator role ownership by as... |
| 4434 | 0.2188 | Microsoft 365 Management APIs ActivityFeed.Read NO... |
| 4435 | 0.2187 | Here is an example of a CSV file structure: v10.7 ... |
| 4436 | 0.2185 | See the Use Group Managed Service Account (gMSA) t... |
| 4437 | 0.2185 | When finished, click OK. See also Using historical... |
| 4438 | 0.2185 | NOTE: In this case, the product s till collects st... |
| 4439 | 0.2185 | URL & Login The Access Reviews Console can be acce... |
| 4440 | 0.2185 | v10.7 Database Page The Access Reviews application... |
| 4441 | 0.2185 | By default, it is delivered once a day, at 3 Speci... |
| 4442 | 0.2184 | Object type Actions Message ID 103047 103082 10308... |
| 4443 | 0.2184 | A custom account must be granted the same permissi... |
| 4444 | 0.2183 | They need to set report filters as follows: Monito... |
| 4445 | 0.2182 | Read access is reported for documents and lists an... |
| 4446 | 0.2180 | Clicking the tile opens the Activity Record St ati... |
| 4447 | 0.2179 | Helps Failed identify potential intruders who trie... |
| 4448 | 0.2179 | Do one of the following depending on the OS: To co... |
| 4449 | 0.2178 | Save the settings.xml file. New configuration sett... |
| 4450 | 0.2178 | The computer where the add-on will be installed Th... |
| 4451 | 0.2178 | A filetype other than one of the types captured ab... |
| 4452 | 0.2177 | Table 1: Event Description replication_delete_sour... |
| 4453 | 0.2176 | The users assigned the Reviewer role on a certain ... |
| 4454 | 0.2175 | Mind that in this case, the product does not summa... |
| 4455 | 0.2175 | lsnrctl stop listener_name To find your listener n... |
| 4456 | 0.2175 | DC_name For example: <v v= "*ROOTDC1*"/> <n n="Hub... |
| 4457 | 0.2173 | Provide the name and password of the service accou... |
| 4458 | 0.2172 | Enabled accounts —total number of enabled accounts... |
| 4459 | 0.2172 | A Security Officer wants to monitor a file share b... |
| 4460 | 0.2171 | Select alert recipients. Click Add Recipient and s... |
| 4461 | 0.2170 | See the File Servers topic for additional informat... |
| 4462 | 0.2169 | Monitoring plan Limits your search to the selected... |
| 4463 | 0.2169 | Hardware component Minimum required Recommended An... |
| 4464 | 0.2168 | *) Hardware HKEY_LOCAL_MACHINE\SYSTEM\CurrentContr... |
| 4465 | 0.2168 | Table 1: Option Description Sender address Enter t... |
| 4466 | 0.2168 | SetDataSourceAsEventSource False Defines whether t... |
| 4467 | 0.2166 | Make sure this account has a password that expires... |
| 4468 | 0.2165 | The Create Review wizard closes. The new review di... |
| 4469 | 0.2165 | Who Shows the name of the account under which the ... |
| 4470 | 0.2164 | Lines that start with the # sign are treated as co... |
| 4471 | 0.2162 | For example: Exchange_Server.Adminis trativeGroup ... |
| 4472 | 0.2162 | When reverting to a snapshot, the tool reviews the... |
| 4473 | 0.2161 | ), and/or values in the To and From. LastSevenDays... |
| 4474 | 0.2161 | Step 6 – Navigate to the Notifications tab and com... |
| 4475 | 0.2160 | Each parameter is preceded with a dash; a space se... |
| 4476 | 0.2160 | user@tenant.com exomiteventuserlist.txt Contains a... |
| 4477 | 0.2159 | Scope Table 1: Option Description Monitor hidden s... |
| 4478 | 0.2158 | User/password – Provide a username and password fo... |
| 4479 | 0.2158 | Step 2 – Define parameters such as ServiceNow conn... |
| 4480 | 0.2157 | Step 1 – Navigate to your cluster management comma... |
| 4481 | 0.2157 | Roles are described briefly in the table below and... |
| 4482 | 0.2155 | Click Add Exclusion. Then, in the Specify Filters ... |
| 4483 | 0.2155 | Click Add Exclusion. Then, in the Specify Filters ... |
| 4484 | 0.2155 | Possible parameter values: • True — generate a num... |
| 4485 | 0.2155 | Delegate Admin SoftDelete A message was permanentl... |
| 4486 | 0.2154 | If needed, configure the exclusion rules in a simi... |
| 4487 | 0.2153 | The LocalSystem account is selected by Long-Term A... |
| 4488 | 0.2153 | Table 1: Oracle Database 12c, 18c, 19c Grant SELEC... |
| 4489 | 0.2153 | This option works in co mbination with UpdateTicke... |
| 4490 | 0.2152 | For an exact match, use quotation marks and provid... |
| 4491 | 0.2151 | Containers and Computers By default, Auditor will ... |
| 4492 | 0.2151 | See the Data Grid Features topic for additional in... |
| 4493 | 0.2150 | The alert keeps firing 20 times more within 10 min... |
| 4494 | 0.2150 | ), shares used by printers to enable remote admini... |
| 4495 | 0.2149 | Sender address RECOMMENDED: click Send Test Email.... |
| 4496 | 0.2149 | Support for modern authentication will allow you t... |
| 4497 | 0.2147 | See the Monitoring Planstopic for additional infor... |
| 4498 | 0.2147 | If you want to use a specific account (other than ... |
| 4499 | 0.2147 | Entitlement Reviews tab Administrator role Securit... |
| 4500 | 0.2147 | In this case, this user will have the most extende... |
| 4501 | 0.2145 | DataCollectionUserName (empty) Specify user accoun... |
| 4502 | 0.2145 | To apply tags to an alert, navigate to alert setti... |
| 4503 | 0.2144 | The maximum number of activity record requests v10... |
| 4504 | 0.2143 | your monitoring plan (e.g., two Active Directory d... |
| 4505 | 0.2142 | Use this report to identify data at high risk and ... |
| 4506 | 0.2142 | Click Exclude to specify AD domains, OUs, and cont... |
| 4507 | 0.2142 | Delete task Yes Message with subject <...> was mov... |
| 4508 | 0.2141 | Execution policy for powershell scripts is set to ... |
| 4509 | 0.2140 | Sensitive Files Count by Source This report shows ... |
| 4510 | 0.2140 | Data file path— .MDF file path. Log file path— .LD... |
| 4511 | 0.2139 | Helps identify who accessed important files beside... |
| 4512 | 0.2139 | Since the intruder can be the actor (Who), the obj... |
| 4513 | 0.2139 | A custom account must be granted the same permissi... |
| 4514 | 0.2138 | NOTE: If you are using a gMSA account for Active D... |
| 4515 | 0.2138 | Filter by organizational unit To audit inactive us... |
| 4516 | 0.2136 | Use semicolon to separate several addresses. Step ... |
| 4517 | 0.2135 | v10.7 Step 3 – On the Log On tab, select the This ... |
| 4518 | 0.2135 | DataCollection DataCollectionServer (empty) Specif... |
| 4519 | 0.2133 | Step 1 – On the Pending Reviews page, select the r... |
| 4520 | 0.2133 | v10.7 NOTE: For additional information about User ... |
| 4521 | 0.2132 | Table 1: File Description Syntax omituserlist.txt ... |
| 4522 | 0.2131 | Step 4 – Click Add and enter the name of the user ... |
| 4523 | 0.2130 | Select this option if you want Auditor to connect ... |
| 4524 | 0.2130 | Click Browse to select from the list of containers... |
| 4525 | 0.2126 | *) Services HKEY_LOCAL_MACHINE\SYSTEM\CurrentContr... |
| 4526 | 0.2125 | See the Notification to Owners topic for additiona... |
| 4527 | 0.2123 | v10.7 Owners assigned to resources within the Reso... |
| 4528 | 0.2123 | See the Specified time interval (in Working (logon... |
| 4529 | 0.2121 | Enter the address that will appear in the From fie... |
| 4530 | 0.2121 | Message with subject <...> Move email to another Y... |
| 4531 | 0.2121 | between an object type and aproperty, the whole en... |
| 4532 | 0.2120 | Step 2 – Select what type of data you want to excl... |
| 4533 | 0.2118 | Parameter Default value Description EventID genera... |
| 4534 | 0.2117 | These permissions are equivalent to the default pe... |
| 4535 | 0.2117 | All filters are applied using AND logic. Configure... |
| 4536 | 0.2115 | See the topics on the monitored items for details.... |
| 4537 | 0.2115 | Otherwise, you will not be able to run reviews on ... |
| 4538 | 0.2113 | Customize Home Screen Starting with version 10, yo... |
| 4539 | 0.2111 | Empty No items have been added to this data source... |
| 4540 | 0.2111 | The system will send a test message to the specifi... |
| 4541 | 0.2111 | The service will automatically substitut e Opened:... |
| 4542 | 0.2111 | Navigate to Computer Configuration > Administrativ... |
| 4543 | 0.2111 | Navigate to Computer Configuration > Administrativ... |
| 4544 | 0.2110 | User If you need to specify several users, you can... |
| 4545 | 0.2110 | See Release Notes for details. Related reports Cli... |
| 4546 | 0.2110 | Value — Specify filter value. See the View and Sea... |
| 4547 | 0.2109 | See the Data C ollecting Account topic for additio... |
| 4548 | 0.2107 | ≥ 25% — High Number of files that have been ≤ 5% —... |
| 4549 | 0.2107 | Considerations for gMSA Account If you are using g... |
| 4550 | 0.2107 | For example: <a n="Names"> Allows specifying a use... |
| 4551 | 0.2106 | Provide a name of the computer ArcSightHost – wher... |
| 4552 | 0.2104 | To audit users for expiring accounts/passwords tha... |
| 4553 | 0.2103 | See the Monitoring Planstopic for additional infor... |
| 4554 | 0.2103 | ArcSight trademarks and registered trademarks are ... |
| 4555 | 0.2102 | Basically, this option is enough for employees who... |
| 4556 | 0.2102 | v10.7 Once the anomaly is reviewed, it disappears ... |
| 4557 | 0.2102 | Reviewer — Primary owner assigned to the resource ... |
| 4558 | 0.2101 | Step 8 – In the <Share_Name> Properties dialog, se... |
| 4559 | 0.2100 | Below is a table of the Substitution Tokens, the v... |
| 4560 | 0.2097 | The service can store the ticket requests not olde... |
| 4561 | 0.2097 | v10.7 v10.7 At the top, the SMTP server and email ... |
| 4562 | 0.2097 | Understanding Scopes Scopes for different Auditor ... |
| 4563 | 0.2096 | Then enter the account information in the User Nam... |
| 4564 | 0.2095 | Hover over a status icon to display its tooltip. T... |
| 4565 | 0.2095 | Clicking the Expand group membership link opens th... |
| 4566 | 0.2094 | Thus, s/he configures the product not to monitor t... |
| 4567 | 0.2093 | Resource Ownership Configuration Ownership of reso... |
| 4568 | 0.2093 | In the Request API permissions window, click Micro... |
| 4569 | 0.2091 | Type the minus sign before selected event ID. For ... |
| 4570 | 0.2090 | SetDataSourceAsEventCategory True Defines whether ... |
| 4571 | 0.2090 | SetDataSourceAsEventCategory True Defines whether ... |
| 4572 | 0.2089 | Click Exclude to specify AD domains, OUs, and cont... |
| 4573 | 0.2089 | Click Exclude to specify AD domains, OUs, and cont... |
| 4574 | 0.2089 | Click Exclude to specify AD domains, OUs, and cont... |
| 4575 | 0.2086 | Predefined reports are helpful if you are looking ... |
| 4576 | 0.2085 | For example: DB_M0,EntSQL,SQLFailedLogon,guest ,Wk... |
| 4577 | 0.2084 | All filters are applied using AND logic. Depending... |
| 4578 | 0.2082 | netwrix_role) and RESTAPI role (e.g. netwrix_rest_... |
| 4579 | 0.2082 | Alternatively, you can use Windows Task Scheduler.... |
| 4580 | 0.2082 | New sensitive data-related risks for SharePoint On... |
| 4581 | 0.2082 | The account used to run the application must be a ... |
| 4582 | 0.2082 | You can use HTML tags when editing a template. v10... |
| 4583 | 0.2081 | Message with subject <...> was moved from folder D... |
| 4584 | 0.2081 | To exclude computers from within the specified ran... |
| 4585 | 0.2080 | See the Risk Score topic for additional informatio... |
| 4586 | 0.2080 | See the Risk Score topic for additional informatio... |
| 4587 | 0.2080 | ), shares used by printers to enable remote admini... |
| 4588 | 0.2077 | * - any machine with a 3-character name or longer ... |
| 4589 | 0.2077 | (empty) For localhost, leave this parameter empty.... |
| 4590 | 0.2077 | Step 7 – Check Allow next to the "Read" permission... |
| 4591 | 0.2077 | Windows Server which setting was changed: – provid... |
| 4592 | 0.2075 | Step 4 – Receive the next response. On success, th... |
| 4593 | 0.2074 | Any other account will be considered a risk factor... |
| 4594 | 0.2072 | The Resource Review page opens to the 1 Make chang... |
| 4595 | 0.2072 | NOTE: In this case, the product s till collects st... |
| 4596 | 0.2072 | See the Console Access Page topic for information.... |
| 4597 | 0.2071 | Default is Medium. v10.7 Parameter Description Spe... |
| 4598 | 0.2071 | Error Details Error Details On error, most request... |
| 4599 | 0.2070 | Task Category {DataSource ID} -OR1 Depending on Se... |
| 4600 | 0.2070 | You can use IP address, DataCollectionServer (empt... |
| 4601 | 0.2070 | In this case, this user will have the most extende... |
| 4602 | 0.2069 | Leave blank if you use Windows Authentication. Def... |
| 4603 | 0.2067 | A wildcard (*) is supported. You can use * for cmd... |
| 4604 | 0.2067 | * - any machine with a 3-character name or longer ... |
| 4605 | 0.2066 | Computer Specify a computer (as it is displayed in... |
| 4606 | 0.2066 | The user list with all users who provoked alerts a... |
| 4607 | 0.2065 | For example: .Identity .DomainController .Organiza... |
| 4608 | 0.2063 | Objects Specify restrictions for the objects to mo... |
| 4609 | 0.2062 | See the procedure below for A Security Officer wan... |
| 4610 | 0.2062 | See the procedure below for A Security Officer wan... |
| 4611 | 0.2059 | Helps identify who accessed important files beside... |
| 4612 | 0.2057 | For example: DB_M0,EntSQL,SQLFailedLogon,guest ,Wk... |
| 4613 | 0.2056 | ), shares used by printers to enable remote admini... |
| 4614 | 0.2056 | Usually it is recommended to configure a dedicated... |
| 4615 | 0.2054 | ◦◦ Sites.Read.All ◦◦ TeamMember.Read.All Microsoft... |
| 4616 | 0.2053 | This instance is included in the monitoring plan n... |
| 4617 | 0.2052 | Specify this parameter if you want to be alerted o... |
| 4618 | 0.2052 | Action Select an action type from the list (Added,... |
| 4619 | 0.2049 | Parameter Default value Description EventID genera... |
| 4620 | 0.2048 | See the procedure below for A Security Officer wan... |
| 4621 | 0.2048 | Download and unpack the new add-on package to the ... |
| 4622 | 0.2047 | Connect to your SonicWall device. Launch an Intern... |
| 4623 | 0.2046 | Recipients Select alert recipients. Click Add Reci... |
| 4624 | 0.2043 | Step 4 – Review imported Activity Records. Azure F... |
| 4625 | 0.2043 | *) RemovableMedia SYSTEM\CurrentControlSet\Enum v1... |
| 4626 | 0.2041 | The system will send a test message to the specifi... |
| 4627 | 0.2041 | The system will send a test message to the specifi... |
| 4628 | 0.2041 | If you want to use custom management interface for... |
| 4629 | 0.2041 | Sender address RECOMMENDED: click Send Test Email.... |
| 4630 | 0.2040 | A resource description can be supplied by either t... |
| 4631 | 0.2040 | v10.7 Report Description category, plan for data p... |
| 4632 | 0.2038 | General NOTE: Make sure that the Send alert when t... |
| 4633 | 0.2038 | This instance is included in the monitoring plan n... |
| 4634 | 0.2038 | See the Microsoft Entra ID topic for additional in... |
| 4635 | 0.2037 | RECOMMENDED: click Send Test Email. The system wil... |
| 4636 | 0.2037 | Troubleshoot Issues Error in PowerShell Resolution... |
| 4637 | 0.2037 | CorrelationInterval 2592000 Specify the time perio... |
| 4638 | 0.2037 | v10.7 v10.7 Reported data The report has a summary... |
| 4639 | 0.2036 | Compatibility notice The add-on is compatible with... |
| 4640 | 0.2036 | Workflow of Ownership Assignment Prerequisite: Opt... |
| 4641 | 0.2035 | Make sure the user has sufficient permissions to c... |
| 4642 | 0.2035 | This interface has multiple pages: Manage Reviews ... |
| 4643 | 0.2035 | If you want to write alert details into both field... |
| 4644 | 0.2033 | State: %state% Step 6 – Review the <ReopenTicketOp... |
| 4645 | 0.2032 | v10.7 The table below provides instructions on how... |
| 4646 | 0.2031 | "Your response has been saved. You may close this ... |
| 4647 | 0.2030 | Specify monitoring restrictions Specify restrictio... |
| 4648 | 0.2030 | Specify monitoring restrictions Specify restrictio... |
| 4649 | 0.2030 | Execution policy for powershell scripts is set to ... |
| 4650 | 0.2030 | Execution policy for powershell scripts is set to ... |
| 4651 | 0.2030 | Execution policy for powershell scripts is set to ... |
| 4652 | 0.2030 | Execution policy for powershell scripts is set to ... |
| 4653 | 0.2030 | Learn more about how these options work in the Con... |
| 4654 | 0.2029 | between an object type and a property, the whole e... |
| 4655 | 0.2027 | Click Add Rule and configure the following: v10.7 ... |
| 4656 | 0.2027 | You can use a wildcard (*). Click Add and specify ... |
| 4657 | 0.2027 | You can use IP address, FQDN or NETBIOS name. For ... |
| 4658 | 0.2026 | To collect activity data without logons, the privi... |
| 4659 | 0.2026 | The credentials are case sensitive. Specify the ac... |
| 4660 | 0.2026 | ◦◦ eDiscovery or eDiscovery (Premium) in the compl... |
| 4661 | 0.2024 | Remember that administrative hidden shares like de... |
| 4662 | 0.2024 | Review the tips for running the tool: Some command... |
| 4663 | 0.2023 | Select to exclude actions performed by specific us... |
| 4664 | 0.2022 | NOTE: This does require the Notification settings ... |
| 4665 | 0.2021 | Table 1: Option Description Click Exclude to speci... |
| 4666 | 0.2021 | Make sure that the Report Server URL resource is r... |
| 4667 | 0.2021 | RequestLimitInterval 604800 Internal parameter. Th... |
| 4668 | 0.2021 | In the example below, review how the shell script ... |
| 4669 | 0.2020 | Classname For example: exchangeAdminService msExch... |
| 4670 | 0.2020 | This window displays all recommended changes, note... |
| 4671 | 0.2019 | Step 6 – In the Manage auditing and security log P... |
| 4672 | 0.2017 | Microsoft Graph Directory.Read.All • Application.R... |
| 4673 | 0.2017 | v10.7 Obtain Tenant Name Follow the steps to obtai... |
| 4674 | 0.2015 | See the Registry Keys topic for additional informa... |
| 4675 | 0.2015 | Possible parameter values: SetDataSourceAsEventCat... |
| 4676 | 0.2015 | Possible parameter values: SetDataSourceAsEventCat... |
| 4677 | 0.2012 | See the corresponding Micr osoft article for more ... |
| 4678 | 0.2010 | Step 2 – Change the value for the AuthSessionTimeo... |
| 4679 | 0.2008 | Every now and then, you review the Behavior Anomal... |
| 4680 | 0.2007 | Specify AD container Click Exclude to specify AD d... |
| 4681 | 0.2005 | User name / Password Provide user name and passwor... |
| 4682 | 0.2004 | For example: This omit list does not affect SELECT... |
| 4683 | 0.2004 | Specify paths to XML file(s) with regular expressi... |
| 4684 | 0.2004 | This report shows ownership of files and folders t... |
| 4685 | 0.2004 | For report subscription—You cannot edit report nam... |
| 4686 | 0.2003 | Since you are only interested in the way this user... |
| 4687 | 0.2001 | I.e., this option defi nes the maximum delay for p... |
| 4688 | 0.2001 | Review Details Window The View Details button at t... |
| 4689 | 0.2001 | Defines whether the DataSource field of Activity R... |
| 4690 | 0.2001 | Defines whether the DataSource field of Activity R... |
| 4691 | 0.2000 | A scope can be limited to a single monitoring plan... |
| 4692 | 0.1993 | Modify an existing alert Select an alert from the ... |
| 4693 | 0.1993 | PowerShell 3.0 or later must be installed. .NET 4.... |
| 4694 | 0.1991 | The Entitlement Reviews tab opens the Entitlement ... |
| 4695 | 0.1988 | See the Microsoft Entra ID topic for additional in... |
| 4696 | 0.1985 | Helps Failed identify potential intruders who trie... |
| 4697 | 0.1985 | The My Reviews interface has two pages: Pending Re... |
| 4698 | 0.1985 | The ID property is optional and is assigned automa... |
| 4699 | 0.1984 | Ownership Confirmation Request Email The Ownership... |
| 4700 | 0.1984 | For example, if reporting on the database hosted o... |
| 4701 | 0.1983 | The default value is 2592000 seconds, i.e., 1 mont... |
| 4702 | 0.1982 | Step 1 – Accept EULA. Step 2 – Select the installa... |
| 4703 | 0.1981 | You can set this filter as equal to and specify th... |
| 4704 | 0.1981 | All filters are applied using AND logic. v10.7 Opt... |
| 4705 | 0.1980 | .config.cpuAllocation.s hares .level=low: .config.... |
| 4706 | 0.1979 | Step 1 – In Internet Explorer, navigate to Tools >... |
| 4707 | 0.1979 | SQL Server Databases This report lists the propert... |
| 4708 | 0.1977 | To subscribe to a custom report 1. Navigate to Rep... |
| 4709 | 0.1977 | Step 1 – On the Manage Reviews page, select a revi... |
| 4710 | 0.1976 | Switch to the Advanced permissions section. Check ... |
| 4711 | 0.1975 | Click Exclude to specify AD domains, OUs, and cont... |
| 4712 | 0.1973 | You will be asked to authenticate for your respons... |
| 4713 | 0.1971 | v10.7 Grant Required Permissions You need to grant... |
| 4714 | 0.1968 | Shows whether the account has the "User Yes User m... |
| 4715 | 0.1967 | Example: CN=MJones,CN=Users,DC=enterprisedc1,DC=en... |
| 4716 | 0.1967 | See the Enable Console Users topic for additional ... |
| 4717 | 0.1966 | Lines that start with the # sign are treated as co... |
| 4718 | 0.1962 | PathFile Currently, the qumulo.xml rules file is p... |
| 4719 | 0.1962 | Internal parameter. The service can store the acti... |
| 4720 | 0.1961 | Follow the steps to generate a self-signed certifi... |
| 4721 | 0.1959 | In this case, this user will have the most extende... |
| 4722 | 0.1959 | Step 4 – Do not specify a default file share mappe... |
| 4723 | 0.1958 | IncludeDataSourceToMakeEventId True Defines whethe... |
| 4724 | 0.1958 | See the Open Remote TCP Port 9004 topic for additi... |
| 4725 | 0.1958 | For details, refer to Create User Account to Acces... |
| 4726 | 0.1958 | This topic includes the following subtopics: Getti... |
| 4727 | 0.1956 | Its key fields and user (initiator) account detail... |
| 4728 | 0.1954 | Modify an existing alert Select an alert from the ... |
| 4729 | 0.1953 | Execution policy for powershell scripts is set to ... |
| 4730 | 0.1953 | Execution policy for powershell scripts is set to ... |
| 4731 | 0.1953 | Execution policy for powershell scripts is set to ... |
| 4732 | 0.1953 | Execution policy for powershell scripts is set to ... |
| 4733 | 0.1952 | Select Add Folder under the Custom section and spe... |
| 4734 | 0.1951 | Step 4 – Log in to this account and navigate to My... |
| 4735 | 0.1951 | format=json No Add this parameter to retrieve data... |
| 4736 | 0.1951 | By default, 3 minutes. Defines the co nnection tim... |
| 4737 | 0.1945 | Scheduled tasks—Enables auditing of enabled / disa... |
| 4738 | 0.1943 | Do the same if you need to generate Activity Summa... |
| 4739 | 0.1942 | All filters are applied using AND logic. Depending... |
| 4740 | 0.1940 | Default is all databases on selected SQL Server in... |
| 4741 | 0.1939 | Activity Specify restriction filters to narrow you... |
| 4742 | 0.1938 | Navigate to each group where the user belongs Send... |
| 4743 | 0.1937 | Windows Features Communication Follow the steps to... |
| 4744 | 0.1936 | The next time you run the script, it will start re... |
| 4745 | 0.1936 | The next time you run the script, it will start re... |
| 4746 | 0.1936 | The next time you run the script, it will start re... |
| 4747 | 0.1934 | Notify users by email every day if their accounts ... |
| 4748 | 0.1934 | Download the latest add-on version in the Add-on S... |
| 4749 | 0.1934 | Download the latest add-on version in the Add-on S... |
| 4750 | 0.1934 | You can install the product to a virtual machine o... |
| 4751 | 0.1933 | Perform a Membership Review A Membership review is... |
| 4752 | 0.1933 | TicketState To specify a new status, provide its I... |
| 4753 | 0.1932 | The hyperlink will open the Entitlement Reviews in... |
| 4754 | 0.1931 | v10.7 The information displayed in the table inclu... |
| 4755 | 0.1931 | Example: http:// sitecollection/list/document.docx... |
| 4756 | 0.1927 | Step 4 – Configure resource ownership through the ... |
| 4757 | 0.1926 | See the Batch Processing topic for instructions on... |
| 4758 | 0.1926 | Unless specified, the service runs under the accou... |
| 4759 | 0.1925 | Step 1 – Accept EULA. Step 2 – Select the installa... |
| 4760 | 0.1925 | To specify a new status, provide its ID in the <Ti... |
| 4761 | 0.1923 | Ignore users whose passwords have already expired ... |
| 4762 | 0.1923 | Use this report to determine the owners of particu... |
| 4763 | 0.1923 | Modify the new service-policy by adding services t... |
| 4764 | 0.1922 | Not responding Data collector for this data source... |
| 4765 | 0.1921 | Create firewall policy or edit existing policy to ... |
| 4766 | 0.1920 | Execution policy for powershell scripts is set to ... |
| 4767 | 0.1919 | The ActivityRecordList root element includes the A... |
| 4768 | 0.1919 | When calculating effective rights and permissions,... |
| 4769 | 0.1916 | v10.7 Parameter Default value Description The Even... |
| 4770 | 0.1916 | v10.7 Parameter Default value Description The Even... |
| 4771 | 0.1915 | Step 2 – Grant required permissions to that applic... |
| 4772 | 0.1914 | The workaround is to force data collection right a... |
| 4773 | 0.1913 | Grant Required Roles Follow the steps to grant the... |
| 4774 | 0.1913 | SQL Server database information: Server Name – Hos... |
| 4775 | 0.1912 | Data collector for this data source is not respond... |
| 4776 | 0.1912 | To get more information about their settings, you ... |
| 4777 | 0.1912 | Users Specify monitoring restrictions Select the u... |
| 4778 | 0.1912 | http(s)://URL Enter root web site URLs. If you hav... |
| 4779 | 0.1911 | SetDataSourceAsEventCategory True Defines whether ... |
| 4780 | 0.1910 | Allows specifying a user by name. User name For ex... |
| 4781 | 0.1908 | Step 2 – Under the App registrations section, sele... |
| 4782 | 0.1908 | In the main window, supply the name of the account... |
| 4783 | 0.1908 | RequestLimitInterval 604800 Internal parameter. Th... |
| 4784 | 0.1904 | In the pop-up window, select the Computer account ... |
| 4785 | 0.1904 | Follow the steps to manage recommendations: Step 1... |
| 4786 | 0.1904 | • Local users and groups—Enables auditing of local... |
| 4787 | 0.1904 | Specify email address to receive SMS notifications... |
| 4788 | 0.1903 | Runs the reports in the Favorites folder to displa... |
| 4789 | 0.1903 | Select the newly created virtual machine and click... |
| 4790 | 0.1902 | This option is helpful if you want to see if there... |
| 4791 | 0.1902 | File permissions define who has access to local fi... |
| 4792 | 0.1901 | collect state-in-time data for this folder. Select... |
| 4793 | 0.1901 | collect state-in-time data for this folder. Select... |
| 4794 | 0.1901 | You may want to modify these settings, for example... |
| 4795 | 0.1900 | If false, all activity records will be displayed i... |
| 4796 | 0.1900 | Otherwise some data may become unavailable for sea... |
| 4797 | 0.1897 | Console Users with Security Team role ◦◦ Visibilit... |
| 4798 | 0.1896 | Review User Profiles and Process Anomalies Review ... |
| 4799 | 0.1895 | Send notifications to all resource owners — This o... |
| 4800 | 0.1895 | A user specified in the Who filter made a lot of c... |
| 4801 | 0.1893 | During this period you have free, unlimited access... |
| 4802 | 0.1891 | The parameters inside this section correspond to C... |
| 4803 | 0.1891 | v10.7 Step 5 – Paste Azure Connection String in th... |
| 4804 | 0.1890 | If you do not enable the Network traffic compressi... |
| 4805 | 0.1889 | A Security Officer wants to monitor a file share, ... |
| 4806 | 0.1889 | A Security Officer wants to monitor a file share, ... |
| 4807 | 0.1888 | Configuration objects store the information on sit... |
| 4808 | 0.1887 | SCVMM versions: Microsoft System Center Virtual Ma... |
| 4809 | 0.1886 | The My Reviews interface is available if the logge... |
| 4810 | 0.1886 | Default retention period is 180 days. Table 1: Opt... |
| 4811 | 0.1885 | The user name and a date timestamp will appear at ... |
| 4812 | 0.1884 | Provide connection details in the following format... |
| 4813 | 0.1883 | The gMSA also helps to ensure that service account... |
| 4814 | 0.1881 | Action Select Allow the connection Profile Applies... |
| 4815 | 0.1881 | See the Grant Permissions for the Deleted Objects ... |
| 4816 | 0.1881 | Summary — This page provides a preview of the sett... |
| 4817 | 0.1879 | Step 1 – On the General page of the item propertie... |
| 4818 | 0.1879 | Step 1 – On the General page of the item propertie... |
| 4819 | 0.1879 | Step 3 – Save Client ID and Tenant ID. Step 4 – Cr... |
| 4820 | 0.1879 | Step 5 – Locate the Log on as a batch job policy a... |
| 4821 | 0.1878 | A user specified in the Who filter made a lot of c... |
| 4822 | 0.1878 | Updates to this partition are replicated only to d... |
| 4823 | 0.1877 | See the Navigation topic for information on each o... |
| 4824 | 0.1877 | A custom account must be granted the same permissi... |
| 4825 | 0.1877 | Task Category {DataSource ID} -OR1 Depending on Se... |
| 4826 | 0.1877 | The workaround is to force data collection right a... |
| 4827 | 0.1876 | Option Description Enter your SMTP server address.... |
| 4828 | 0.1874 | The content within the table varies, and additiona... |
| 4829 | 0.1873 | Apply filters to narrow your report scope. Please ... |
| 4830 | 0.1873 | • Oracle Wallet – select if you want to use Oracle... |
| 4831 | 0.1873 | Direct from login for owners without a role Data G... |
| 4832 | 0.1870 | Enter the IP subrange you want to exclude, and cli... |
| 4833 | 0.1869 | It is recommended to adjust this setting carefully... |
| 4834 | 0.1869 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 4835 | 0.1866 | https://URL For example: https:// Corp.sharepoint.... |
| 4836 | 0.1864 | Step 2 – Grant required permissions to that applic... |
| 4837 | 0.1863 | It opens the Saving review window, which displays ... |
| 4838 | 0.1863 | See the For Oracle Database Auditing topic for the... |
| 4839 | 0.1860 | Supported size: 21x21px (WxH). FooterImageFullPath... |
| 4840 | 0.1860 | Choose Appropriate Execution Scenario The Add-on r... |
| 4841 | 0.1859 | Enable Remote Registry Service Follow the steps to... |
| 4842 | 0.1858 | Add the text of this error message to this file to... |
| 4843 | 0.1856 | Modify as desired and relaunch the review. See the... |
| 4844 | 0.1856 | In Splunk expand the Settings drop-down menu and c... |
| 4845 | 0.1855 | The Action filt er in the Advanced mode contains a... |
| 4846 | 0.1854 | Step 2 – Register an Azure App and grant it the fo... |
| 4847 | 0.1854 | The pattern you provide here must match the applic... |
| 4848 | 0.1854 | Step 1 – Sign in to the Cisco Meraki Dashboard. St... |
| 4849 | 0.1853 | To audit users for expiring accounts/passwords tha... |
| 4850 | 0.1852 | snapshot_delete_snapshot A snapshot was deleted. s... |
| 4851 | 0.1849 | Password Enter a password. Clear imported data Sel... |
| 4852 | 0.1849 | Shows whether the account has the "Password not re... |
| 4853 | 0.1849 | Password last change lastPasswordChangeDateTi me E... |
| 4854 | 0.1846 | ◦◦ Make sure this user account has sufficient acce... |
| 4855 | 0.1846 | ◦◦ Make sure this user account has sufficient acce... |
| 4856 | 0.1846 | See the Update the Database Service Account Passwo... |
| 4857 | 0.1846 | Step 1 – On the General page of the item propertie... |
| 4858 | 0.1843 | After running the script, the RADIUS server logons... |
| 4859 | 0.1842 | Helps find out who made Successful changes to your... |
| 4860 | 0.1841 | See the Delete Review Window topic for additional ... |
| 4861 | 0.1841 | Enter event ID number or range of event IDs separa... |
| 4862 | 0.1840 | The Stop Review window closes. View Responses Wind... |
| 4863 | 0.1840 | Step 6 – When all recommendations are confirmed an... |
| 4864 | 0.1837 | Entering multiple individual addresses is not supp... |
| 4865 | 0.1837 | You are investigating an incident Limits your sear... |
| 4866 | 0.1836 | The review for this resource is now complete. You ... |
| 4867 | 0.1834 | Use this operator if you want to get precise resul... |
| 4868 | 0.1831 | Active Directory tombstones — This option is recom... |
| 4869 | 0.1831 | Create Review Wizard The Create Review wizard is o... |
| 4870 | 0.1829 | Step 5 – When all recommendations are confirmed an... |
| 4871 | 0.1829 | You can also change the password for the Builtin A... |
| 4872 | 0.1826 | Select a change to see its rollback details in the... |
| 4873 | 0.1824 | To create a filter for user activity monitoring, s... |
| 4874 | 0.1823 | The My Reviews interface provides owners with acce... |
| 4875 | 0.1822 | Account type —possible values: Windows Account, Lo... |
| 4876 | 0.1822 | Select the review in the list and click Mark Compl... |
| 4877 | 0.1822 | The service can store the Activity Record requests... |
| 4878 | 0.1821 | Step 1 – Open PowerShell Step 2 – Run the followin... |
| 4879 | 0.1820 | Active Directory Page The Access Reviews applicati... |
| 4880 | 0.1820 | Step 3 – In the Windows Firewall with Advanced Sec... |
| 4881 | 0.1819 | By default, the application is configured to send ... |
| 4882 | 0.1819 | Check your Visual Studio Redistributable version. ... |
| 4883 | 0.1819 | Max length: 255. • Contains (default) • DoesNotCon... |
| 4884 | 0.1819 | Limit row count in a file to – Select the desired ... |
| 4885 | 0.1818 | See the Data Grid Features topic for additional in... |
| 4886 | 0.1818 | Delete email Yes Message with subject <...> was mo... |
| 4887 | 0.1818 | Step 5 – Proceed with adding the permissions for t... |
| 4888 | 0.1817 | A custom account must be granted the same permissi... |
| 4889 | 0.1817 | Press Enter and repeat menu section. You will retu... |
| 4890 | 0.1817 | v10.7 Step 5 – The action status displays on the p... |
| 4891 | 0.1816 | Due to limited database size, Express Edition (wit... |
| 4892 | 0.1816 | Member— role member name. v10.7 Considerations and... |
| 4893 | 0.1815 | Object Permissions in SQL Server This report shows... |
| 4894 | 0.1813 | Declined Ownership Message If you have declined ow... |
| 4895 | 0.1812 | Use this option to detect suspicious activity on y... |
| 4896 | 0.1811 | The syntax greatly depends on the tool you use. St... |
| 4897 | 0.1810 | See the Update the Active Directory Service Accoun... |
| 4898 | 0.1810 | Step 5 – Navigate to HKEY_LOCAL_MACHINE\SECURITY\P... |
| 4899 | 0.1809 | Older activity record requests are cleared. Activi... |
| 4900 | 0.1808 | Read access Successful Use this option to supervis... |
| 4901 | 0.1807 | omituserlist.txt Contains a list of user names to ... |
| 4902 | 0.1807 | You are investigating a security incident and want... |
| 4903 | 0.1807 | Users Specify users to track their activity Select... |
| 4904 | 0.1806 | Port number Specify your SMTP server port number. ... |
| 4905 | 0.1806 | Port number Specify your SMTP server port number. ... |
| 4906 | 0.1806 | Updates to this partition are replicated only to d... |
| 4907 | 0.1805 | The platform provides security analytics to detect... |
| 4908 | 0.1803 | Clicking the Defined in link opens the object perm... |
| 4909 | 0.1801 | A Security Officer wants to monitor a file share b... |
| 4910 | 0.1801 | The ID of ConnectWise Manage subscriber (Managed C... |
| 4911 | 0.1800 | If you want to monitor user-defined hidden shares,... |
| 4912 | 0.1800 | If you want to monitor user-defined hidden shares,... |
| 4913 | 0.1798 | Rotating certificate s in the Entra ID application... |
| 4914 | 0.1797 | v10.7 Step 2 – Select Manifest on the left. Step 3... |
| 4915 | 0.1795 | See the Data Grid Features topic for additional in... |
| 4916 | 0.1793 | See the Approval Process topic for additional info... |
| 4917 | 0.1791 | Click Close to return to the review. Review Histor... |
| 4918 | 0.1791 | The default CorrelationInterval 2592000 value is 2... |
| 4919 | 0.1789 | In-script parameters are listed in the table below... |
| 4920 | 0.1789 | In-script parameters are listed in the table below... |
| 4921 | 0.1787 | Behavior Anomalies Assessment Tips and Tricks This... |
| 4922 | 0.1787 | Modify by adding new owners, removing owners, or c... |
| 4923 | 0.1786 | See the Ownership Confirmation Request Email topic... |
| 4924 | 0.1786 | classname.attrname=intel ligiblename For example, ... |
| 4925 | 0.1786 | So, in the example above, the program will track a... |
| 4926 | 0.1785 | See the Add New Resource Wizard topic for addition... |
| 4927 | 0.1785 | Create User Account to Access Nutanix REST API To ... |
| 4928 | 0.1784 | Step 4 – Configure client secret for that applicat... |
| 4929 | 0.1784 | Predefined reports are helpful if you Predefined r... |
| 4930 | 0.1783 | The following choices are available: User/password... |
| 4931 | 0.1783 | Port number Specify your SMTP server port number. ... |
| 4932 | 0.1782 | In this case, this user will have the most extende... |
| 4933 | 0.1781 | For the already existing tenants it is still possi... |
| 4934 | 0.1780 | the following line: Default Domain Policy. <settin... |
| 4935 | 0.1780 | Run Again Modify as desired and relaunch the revie... |
| 4936 | 0.1778 | Review history and complement EnableTicketCorrelat... |
| 4937 | 0.1778 | This value is an enumeration with one possible val... |
| 4938 | 0.1777 | In order to send a test email, click Test and sele... |
| 4939 | 0.1775 | ◦◦ Make sure this user account has sufficient acce... |
| 4940 | 0.1775 | Microsoft Graph Application.ReadWrite. All Directo... |
| 4941 | 0.1774 | v10.7 Step 7 – Check Allow next to the Read permis... |
| 4942 | 0.1773 | v10.7 Remember, click Save after making modificati... |
| 4943 | 0.1773 | Select Monitor userdefined hidden shares if necess... |
| 4944 | 0.1773 | Select Monitor userdefined hidden shares if necess... |
| 4945 | 0.1771 | Step 3 – Select the desired action for all recomme... |
| 4946 | 0.1771 | Step 3 – Review the script and provide parameters.... |
| 4947 | 0.1771 | Check the Notes for the resource to view this info... |
| 4948 | 0.1770 | collect state-in-time data for this folder. Table ... |
| 4949 | 0.1770 | The following choices are available: User/password... |
| 4950 | 0.1769 | v10.7 You can configure Group Policy Preferences t... |
| 4951 | 0.1767 | Select Monitor user-defined hidden shares if neces... |
| 4952 | 0.1767 | nfs_modify_export Modified NFS Export that the cli... |
| 4953 | 0.1766 | With Behavior Anomalies, you can step beyond indiv... |
| 4954 | 0.1766 | Table 1: Hardware HKEY_LOCAL_MACHINE\SYSTEM\Curren... |
| 4955 | 0.1764 | • Database — specify target database • Schema — sp... |
| 4956 | 0.1764 | System requirements for SQL Server are listed in t... |
| 4957 | 0.1762 | See the Update Resource Wizard topic for additiona... |
| 4958 | 0.1762 | Everyone in organization has a huge score Probably... |
| 4959 | 0.1762 | User Activity Select to exclude actions performed ... |
| 4960 | 0.1761 | By default, resolved, closed, and canceled tickets... |
| 4961 | 0.1761 | Max length: 536870911. • Contains (default) • Does... |
| 4962 | 0.1759 | Otherwise, you will receive an empty report. escap... |
| 4963 | 0.1758 | City city Example: "London" The city where a user ... |
| 4964 | 0.1758 | The Access Reviews begins to create the review. Ac... |
| 4965 | 0.1757 | The service uses the default values unless paramet... |
| 4966 | 0.1757 | Failed Use this option to detect suspicious activi... |
| 4967 | 0.1756 | The Search parameters fi le includes one or more f... |
| 4968 | 0.1755 | Table 1: Attribute Description Possible values Fil... |
| 4969 | 0.1754 | v10.7 Step 5 – Click Test Settings to ensure a con... |
| 4970 | 0.1752 | See the Search Parameters topic for more informati... |
| 4971 | 0.1752 | Step 1 – Navigate to Start > Windows Administrativ... |
| 4972 | 0.1752 | Example: C:\Powershellscripts\old scripts\script.p... |
| 4973 | 0.1751 | Activity Specify monitoring restrictions Specify r... |
| 4974 | 0.1750 | v10.7 On the Manage Reviews page in the Entitlemen... |
| 4975 | 0.1750 | CyperArk PAS Version 10.10. Accounts and Rights By... |
| 4976 | 0.1749 | Remember that administrative hidden shares like de... |
| 4977 | 0.1746 | The default-data-files parameter is the service-po... |
| 4978 | 0.1746 | Step 1 – Navigate to the Summary email recipient a... |
| 4979 | 0.1745 | User (domain\account) – select a specific user to ... |
| 4980 | 0.1743 | The 2 Review changes tab opens in the Resource Rev... |
| 4981 | 0.1743 | One of two messages will appear according to if yo... |
| 4982 | 0.1740 | This list is only relevant to operations with SQL ... |
| 4983 | 0.1740 | In the environments with root/child domains, the a... |
| 4984 | 0.1738 | Execution policy for powershell scripts is set to ... |
| 4985 | 0.1738 | Step 2 – Click Search. Table 1: Error in PowerShel... |
| 4986 | 0.1737 | Execution policy for powershell scripts is set to ... |
| 4987 | 0.1736 | To and From support the following date time format... |
| 4988 | 0.1735 | See the View Responses Window topic for additional... |
| 4989 | 0.1734 | Make sure to create a dedicated item inAuditor in ... |
| 4990 | 0.1732 | The 2 Review changes tab opens in the Resource Rev... |
| 4991 | 0.1732 | Review the full list in the Reported Attributes Re... |
| 4992 | 0.1731 | Make sure that the resource is reachable. Report M... |
| 4993 | 0.1731 | Information about manifest is also described in th... |
| 4994 | 0.1730 | Account details to show — set of AD attributes to ... |
| 4995 | 0.1727 | Read access Use this option to supervise access to... |
| 4996 | 0.1727 | Response Request Status Response The HTTP status c... |
| 4997 | 0.1727 | Response Request Status Response The HTTP status c... |
| 4998 | 0.1727 | See the procedure below for details. NOTE: In this... |
| 4999 | 0.1725 | Update Resource Wizard The Update resource wizard ... |
| 5000 | 0.1723 | See the Activity Records topic for additional info... |
| 5001 | 0.1723 | See the Activity Records topic for additional info... |
| 5002 | 0.1723 | See the Activity Records topic for additional info... |
| 5003 | 0.1723 | Step 8 – Type repadmin /syncall command and press ... |
| 5004 | 0.1722 | Even when this option is selected, the product wil... |
| 5005 | 0.1722 | Basic authentication: access on behalf of a user. ... |
| 5006 | 0.1722 | A custom account must be granted the same permissi... |
| 5007 | 0.1720 | Specify a computer. You will only be alerted on ev... |
| 5008 | 0.1719 | Only report on users with fine-grained password Se... |
| 5009 | 0.1719 | omitproplist_gp.txt The file contains a list of th... |
| 5010 | 0.1718 | Step 3 – Click Manage roles. v10.7 Step 4 – In the... |
| 5011 | 0.1718 | As an example, refer to the following Oracle help ... |
| 5012 | 0.1716 | With alerts, you can distinguish one alert from an... |
| 5013 | 0.1716 | Overexposed Files and Folders This report shows se... |
| 5014 | 0.1716 | ◦ If you plan to process the Active Directory Dele... |
| 5015 | 0.1715 | In this case, this user will have the most extende... |
| 5016 | 0.1714 | Remember, at any time you can save your recommenda... |
| 5017 | 0.1713 | Max length: 255. • Contains (default) • DoesNotCon... |
| 5018 | 0.1712 | Procedure for Nutanix Prism Element Follow the ste... |
| 5019 | 0.1712 | 5% of 10 GB limit remaining). v10.7 These properti... |
| 5020 | 0.1711 | This list omits changes made by users through Exch... |
| 5021 | 0.1710 | Format Example <Who Operator="Equals">Admin</Who><... |
| 5022 | 0.1709 | Step 5 – You can use a wildcard (*) only if you ne... |
| 5023 | 0.1709 | Step 5 – You can use a wildcard (*) only if you ne... |
| 5024 | 0.1709 | {DataSource ID} Depending on Task Category -ORSetD... |
| 5025 | 0.1709 | However, this can be customized on the Configurati... |
| 5026 | 0.1708 | EnableTicketCorrelation true This option is helpfu... |
| 5027 | 0.1707 | Assigned owners do not require a console user role... |
| 5028 | 0.1707 | For example: Using Oracle Wallet Manager. Refer to... |
| 5029 | 0.1706 | First/Second/Last time when password expires in <>... |
| 5030 | 0.1703 | Table 1: For metric... Use Customize risk indicato... |
| 5031 | 0.1703 | fs_read_data Read operation was performed. fs_writ... |
| 5032 | 0.1702 | It can be your company's Exchange server or any pu... |
| 5033 | 0.1700 | See the View Reports topic for additional informat... |
| 5034 | 0.1699 | Run the Add-On with PowerShell Follow the steps to... |
| 5035 | 0.1699 | Installation on the domain controller is not suppo... |
| 5036 | 0.1698 | Object Type Reported Action Reported Properties Cr... |
| 5037 | 0.1696 | Modify subscriptions Select the subscription that ... |
| 5038 | 0.1694 | Table 2: Request Status Response Success The HTTP ... |
| 5039 | 0.1692 | It can be opened for one or multiple resources. It... |
| 5040 | 0.1692 | Use this report to review the permissions granted ... |
| 5041 | 0.1691 | Table — Specify database table to monitor. Column—... |
| 5042 | 0.1691 | Remember, at any time you can save your recommenda... |
| 5043 | 0.1690 | Step 1 – Install the Exchange Online PowerShell V3... |
| 5044 | 0.1689 | v10.7 Cisco Meraki Dashboard Complete the followin... |
| 5045 | 0.1688 | Execution policy for powershell scripts is set to ... |
| 5046 | 0.1688 | File permissions define who has access to local fi... |
| 5047 | 0.1686 | Step 1 – In the dashboard pane, select the metric ... |
| 5048 | 0.1686 | Press Enter and repeat menu section. You will retu... |
| 5049 | 0.1685 | Step 10 – Close Group Policy Management console. v... |
| 5050 | 0.1684 | See the Use Group Managed Service Account (gMSA) t... |
| 5051 | 0.1684 | For example, you can exclude site collections docu... |
| 5052 | 0.1684 | When the owner confirmation notification has compl... |
| 5053 | 0.1684 | v10.7 Step 2 – Select Manifest on the left. Step 3... |
| 5054 | 0.1682 | Follow the steps to configure Internet Options to ... |
| 5055 | 0.1682 | Provide a different password if necessary. v10.7 P... |
| 5056 | 0.1680 | The two may be s pecified together; for example: "... |
| 5057 | 0.1680 | You noticed that some domain policies were changed... |
| 5058 | 0.1677 | Step 4 – Click the Security administrator or Secur... |
| 5059 | 0.1677 | Action Allow the connection Profile Applies to Dom... |
| 5060 | 0.1676 | 11.. Add the following line to the sqlnet.ora file... |
| 5061 | 0.1674 | Even when this option is selected, the product wil... |
| 5062 | 0.1674 | Write operation was performed (metadata was fs_wri... |
| 5063 | 0.1671 | Qumulo Complete the following fields: Table 1: Opt... |
| 5064 | 0.1671 | This refers to the specified shared folder, its su... |
| 5065 | 0.1669 | DisplayOnlyFirstActivityRecord true Add only the f... |
| 5066 | 0.1669 | Table 1: Parameter Default value Description Ticke... |
| 5067 | 0.1666 | ), (,), and (\) if they are a part of an entry val... |
| 5068 | 0.1666 | 400 Bad Request Error Error validating A ctivity R... |
| 5069 | 0.1665 | See the Data C ollecting Account topic for additio... |
| 5070 | 0.1663 | Grant Admin Consent to a Tenant Go to the Microsof... |
| 5071 | 0.1663 | Grant Admin Consent to a Tenant Go to the Microsof... |
| 5072 | 0.1662 | StartsWith EndsWith Contains (default) Limits your... |
| 5073 | 0.1661 | Example: "Michael Jones" Domain\User. Example: ent... |
| 5074 | 0.1661 | Filter — Select general type of filter (e.g., "Who... |
| 5075 | 0.1661 | Allow access to the following servers — When enabl... |
| 5076 | 0.1658 | Update a Resource Follow the steps to update owner... |
| 5077 | 0.1657 | Helps identify potential intruders who tried to mo... |
| 5078 | 0.1656 | Wildcard (*) is supported to replace any number of... |
| 5079 | 0.1656 | This refers to the specified shared folder, its su... |
| 5080 | 0.1654 | You can use * for cmdlets and their parameters. Li... |
| 5081 | 0.1654 | See the View Responses Window topic for a dditiona... |
| 5082 | 0.1653 | AppNameGroupID — Define application name value by ... |
| 5083 | 0.1651 | v10.7 Option Description Select this option to rec... |
| 5084 | 0.1650 | Table 2: Request Status Response Success The HTTP ... |
| 5085 | 0.1648 | Example: "Business The user's job title. Max Title... |
| 5086 | 0.1647 | Localos users. For these users, the product collec... |
| 5087 | 0.1647 | Follow the steps to enable the Remote Registry ser... |
| 5088 | 0.1647 | Select those owners and click Remove. Those owners... |
| 5089 | 0.1647 | Table 1: Option Description It is recommended to u... |
| 5090 | 0.1645 | State-in-time reports For each SharePoint site col... |
| 5091 | 0.1645 | This permission allows another user to send the me... |
| 5092 | 0.1645 | Step 2 – Modify the AccessInformationCenter.Servic... |
| 5093 | 0.1643 | Reveal sensitive content that has permissions diff... |
| 5094 | 0.1642 | Last name surname Example: "Smith" The user's surn... |
| 5095 | 0.1641 | Configure network • Select Y to use DHCP server to... |
| 5096 | 0.1641 | You do not have sufficient permissions to review i... |
| 5097 | 0.1641 | ◦ The user that is going to run the Core Service i... |
| 5098 | 0.1641 | Step 2 – In the Services snap-in, locate the Remot... |
| 5099 | 0.1639 | Console Users with Administrator role ◦◦ Can compl... |
| 5100 | 0.1636 | Follow the steps to configure the Log On As a Batc... |
| 5101 | 0.1636 | v10.7 The signed in user is displayed in the upper... |
| 5102 | 0.1635 | Use this report to identify data at high risk and ... |
| 5103 | 0.1634 | Use case Related documentation Active Directory I ... |
| 5104 | 0.1632 | Tool-tips display when hovering over the icons ind... |
| 5105 | 0.1632 | Step 2 – Locate the General tab. Step 3 – Click th... |
| 5106 | 0.1631 | Object type — monitored object type; for the full ... |
| 5107 | 0.1630 | See the Settings for Data Collection topic for add... |
| 5108 | 0.1629 | See the Behavior Anomalies topic for a dditional i... |
| 5109 | 0.1629 | Select Monitor userdefined hidden shares if necess... |
| 5110 | 0.1626 | Step 4 – Make sure you have disabled multi-factor ... |
| 5111 | 0.1625 | Step 4 – Click Select. v10.7 Step 5 – Enter your t... |
| 5112 | 0.1624 | For example: nwxtech.com,example.com Remember, cli... |
| 5113 | 0.1623 | A custom account must be granted the same permissi... |
| 5114 | 0.1623 | Step 3 – In the Group Policy Management Editor dia... |
| 5115 | 0.1623 | Step 3 – In the Group Policy Management Editor dia... |
| 5116 | 0.1622 | If you want to reopen closed tickets, you must be ... |
| 5117 | 0.1620 | If you leave this field empty, then the path to th... |
| 5118 | 0.1619 | Follow the steps to play a video: Step 1 – Navigat... |
| 5119 | 0.1618 | v10.7 Step 4 – Specify Active Directory credential... |
| 5120 | 0.1617 | If the trustee is a group, click the hyperlink to ... |
| 5121 | 0.1617 | See the Delete Review Window topic for additional ... |
| 5122 | 0.1616 | Filter Description Supported Operators Contains (d... |
| 5123 | 0.1615 | Opens the Review Details page for the selected Vie... |
| 5124 | 0.1615 | View Details Opens the Review Details page for the... |
| 5125 | 0.1615 | Once set, these parameter values must stay unchang... |
| 5126 | 0.1614 | NOTE: ONTAP REST API works only over HTTPS protoco... |
| 5127 | 0.1614 | You can select a whole AD domain, OU or container.... |
| 5128 | 0.1614 | You can select a whole AD domain, OU or container.... |
| 5129 | 0.1613 | Possible values are: Multi_user (for Multiple), Re... |
| 5130 | 0.1613 | If you select this option, the fields below are no... |
| 5131 | 0.1613 | To collect activity data only, the privileged role... |
| 5132 | 0.1612 | See the Edit Notes Window topic for a dditional in... |
| 5133 | 0.1612 | Configure a non-threshold alert, email recipients ... |
| 5134 | 0.1611 | See the Remove Changes Window topic for a dditiona... |
| 5135 | 0.1611 | The TCP 5985 port must be open on Windows Add-on i... |
| 5136 | 0.1610 | You can use * for cmdlets and their parameters. Li... |
| 5137 | 0.1608 | See the Data C ollecting Account topic for more in... |
| 5138 | 0.1608 | Examples: http://siteCollection1:3 https://siteCol... |
| 5139 | 0.1606 | Make sure the post data files (Continuation mark, ... |
| 5140 | 0.1605 | The Tags page contains a complete list of alerts t... |
| 5141 | 0.1604 | Configure SMTP Server Settings SMTP server informa... |
| 5142 | 0.1604 | Your configuration and data will be preserved duri... |
| 5143 | 0.1604 | SharePoint Activity reports Activity Related to Se... |
| 5144 | 0.1604 | Otherwise, leave the default value. RuleFileList P... |
| 5145 | 0.1604 | Execution policy for powershell scripts is set to ... |
| 5146 | 0.1603 | Sends an email to the assigned owner(s) for the se... |
| 5147 | 0.1603 | • 0 — Low • [1 – 2] — Medium • > 2 — High Disabled... |
| 5148 | 0.1603 | minOccurs="0" indicates that element is optional a... |
| 5149 | 0.1602 | ◦◦ Using Description can help to filter out severa... |
| 5150 | 0.1600 | Use this report to reveal the number of sensitive ... |
| 5151 | 0.1600 | The attributes marked with * are reported without ... |
| 5152 | 0.1600 | https://URL Contains the SharePoint Online For exa... |
| 5153 | 0.1598 | This is usually the combination of the user's firs... |
| 5154 | 0.1598 | Resource Review Page The Begin Review button opens... |
| 5155 | 0.1598 | v10.7 Try to review user tasks—you may find out th... |
| 5156 | 0.1597 | See Email address the corresponding Email address ... |
| 5157 | 0.1597 | Get the response - Response Code should be 200. In... |
| 5158 | 0.1594 | Step 2 – Right-click the ADSI Edit node and select... |
| 5159 | 0.1593 | Tool-tips display when hovering over the icons ind... |
| 5160 | 0.1591 | Data will be collected using the SQL Server traces... |
| 5161 | 0.1588 | A custom account must be granted the same permissi... |
| 5162 | 0.1588 | Table 2: Option Description Modify scheduled task ... |
| 5163 | 0.1587 | The following icons appear in this column to indic... |
| 5164 | 0.1586 | If disabled, only user session events will be coll... |
| 5165 | 0.1586 | Select Monitor user-defined hidden shares if neces... |
| 5166 | 0.1586 | Depending on your network environment, you may nee... |
| 5167 | 0.1586 | Copy search — copy the search filters that are cur... |
| 5168 | 0.1585 | These steps only apply for the SQL Authentication ... |
| 5169 | 0.1583 | Maximum length is 64 characters. Is licensed – – –... |
| 5170 | 0.1583 | TicketRequestsRetention RequestLimit 300000 Intern... |
| 5171 | 0.1580 | Yes No + Other Creation date Shows account cr eati... |
| 5172 | 0.1579 | See the Settings for Data Collection topic for mor... |
| 5173 | 0.1578 | This parameter is applied only if GenerateEventId ... |
| 5174 | 0.1578 | The maximum number of ticket requests the service ... |
| 5175 | 0.1577 | ◦◦ The Tenant name field then will be filled in au... |
| 5176 | 0.1576 | The Access Reviews application begins to send the ... |
| 5177 | 0.1575 | Select Monitor userdefined hidden shares if necess... |
| 5178 | 0.1574 | Information about manifest is also described in th... |
| 5179 | 0.1572 | To do this, Alert Details: rename <Name>work_notes... |
| 5180 | 0.1571 | See the Example: corresponding Micro soft Logon sc... |
| 5181 | 0.1568 | Applying tags to alerts allows you to distinguish ... |
| 5182 | 0.1567 | See Edit Notes the Edit Notes Window topic for a d... |
| 5183 | 0.1566 | To learn more about user activity, you can drill-d... |
| 5184 | 0.1565 | See the JSmith@domain.com corresponding Micr osoft... |
| 5185 | 0.1562 | Select Type — Reviews are limited to one type. Sel... |
| 5186 | 0.1559 | Rotating certificate s Collect activity and State-... |
| 5187 | 0.1559 | You can use HTML tags when editing a template. In ... |
| 5188 | 0.1559 | Application Redirect URI is optional, you can leav... |
| 5189 | 0.1559 | Step 7 – Next, in the REST API access users sectio... |
| 5190 | 0.1559 | Filtered business hours during the last data will ... |
| 5191 | 0.1558 | See Edit Notes the Edit Notes Window topic for a d... |
| 5192 | 0.1558 | It can be your SMTP server company's Exchange serv... |
| 5193 | 0.1558 | See the View Reports topic for additional informat... |
| 5194 | 0.1558 | Follow the steps to configure weekly reminders to ... |
| 5195 | 0.1556 | The resource name includes its location, such as t... |
| 5196 | 0.1556 | Possible values: Database, Server Instance. Permis... |
| 5197 | 0.1556 | To Collect Data via API Key To work with multi-fac... |
| 5198 | 0.1555 | RacNumber=16&Arg1= Request='GET /cgi-bin/ Remove /... |
| 5199 | 0.1553 | If you want to use a file path, run the following ... |
| 5200 | 0.1552 | The me 2:13:00 PM Timestamp type represents date a... |
| 5201 | 0.1552 | Check the box and enter the new password in both e... |
| 5202 | 0.1552 | These guidelines are based on security best practi... |
| 5203 | 0.1551 | v10.7 If you select to launch the RestAPI Explorer... |
| 5204 | 0.1550 | Once set, these parameter values must stay unchang... |
| 5205 | 0.1550 | Once set, these parameter values must stay unchang... |
| 5206 | 0.1550 | The maximum number of Activity Record requests the... |
| 5207 | 0.1550 | Approval Process After all owners assigned to a sp... |
| 5208 | 0.1547 | Use the path format as it appears in the "What" co... |
| 5209 | 0.1546 | Notes can be added by Ownership Administrators or ... |
| 5210 | 0.1546 | To edit a report template, click Customize. You ca... |
| 5211 | 0.1546 | Table 1: Option Description Only report on users w... |
| 5212 | 0.1544 | When the task has completed (100%), click Close. T... |
| 5213 | 0.1543 | Finished On — Date timestamp when the review is ma... |
| 5214 | 0.1543 | Review Instances After a review has been completed... |
| 5215 | 0.1542 | Use the path format as it appears in the "What" co... |
| 5216 | 0.1540 | Share permissions provide or deny access to the sa... |
| 5217 | 0.1539 | object_type.property_na me If there is no separato... |
| 5218 | 0.1538 | Step 2 – The Select Owners page lists the currentl... |
| 5219 | 0.1538 | Use the path format as it appears in the "What" co... |
| 5220 | 0.1537 | To prevent this, consider the recommendations and ... |
| 5221 | 0.1534 | object_type.property_na me If there is no separato... |
| 5222 | 0.1534 | See the Data Collecting Account topic for a dditio... |
| 5223 | 0.1534 | See the Data Collecting Account topic for a dditio... |
| 5224 | 0.1534 | See the Data Collecting Account topic for a dditio... |
| 5225 | 0.1533 | Wildcards are supported. For example, type %corp\a... |
| 5226 | 0.1531 | System requirements Make sure that the machine whe... |
| 5227 | 0.1530 | These group Managed Service Accounts should meet t... |
| 5228 | 0.1529 | It is possible to insert variables into the subjec... |
| 5229 | 0.1529 | It is possible to insert variables into the subjec... |
| 5230 | 0.1529 | Step 4 – If you are using a PowerShell-based add-o... |
| 5231 | 0.1528 | Review user actions and compare them to his or her... |
| 5232 | 0.1525 | This parameter is applied only if GenerateEventId ... |
| 5233 | 0.1525 | You can use * for cmdlets and their parameters. Li... |
| 5234 | 0.1524 | Click Add Rule. Specify a name of the Oracle datab... |
| 5235 | 0.1524 | Use semicolon to separate several names. Filter by... |
| 5236 | 0.1524 | If you want to authenticate with AD user account, ... |
| 5237 | 0.1523 | In sqlplus tool, execute the following command: Si... |
| 5238 | 0.1522 | ◦◦ All responses processed — Reviews have been app... |
| 5239 | 0.1522 | NOTE: Currently, Jakarta version has only experime... |
| 5240 | 0.1522 | NOTE: Currently, Jakarta version has only experime... |
| 5241 | 0.1521 | Type "mmc" in the box and click OK. This will open... |
| 5242 | 0.1521 | Use the path format as it appears in the "What" co... |
| 5243 | 0.1520 | printQueue object, add the following line: printQu... |
| 5244 | 0.1520 | See the following Microsoft article for additional... |
| 5245 | 0.1520 | See the IT Risk Assessment Overview topic for addi... |
| 5246 | 0.1516 | Share permissions provide or deny access to the sa... |
| 5247 | 0.1509 | This account should be able to create a dedicated ... |
| 5248 | 0.1509 | Replace Number with a number (e.g., &count=1500). ... |
| 5249 | 0.1508 | Make sure that the SQL Server Name and Database Na... |
| 5250 | 0.1508 | The review can be run as-is by navigating through ... |
| 5251 | 0.1506 | Refresh Runs the reports in the Favorites folder t... |
| 5252 | 0.1504 | Defines the co nnection timeout. TicketRequestsRet... |
| 5253 | 0.1503 | Edit the list of extensions you consider to be ind... |
| 5254 | 0.1502 | See the procedure below for a file share that cont... |
| 5255 | 0.1501 | Sensitive File and Folder Permissions Details This... |
| 5256 | 0.1500 | Unless specified, the service will run under the L... |
| 5257 | 0.1499 | resource_path — path as shown in the "What" column... |
| 5258 | 0.1499 | v10.7 Option Description Specify one or several us... |
| 5259 | 0.1499 | The script is starting to test your domain control... |
| 5260 | 0.1496 | <v v="*S-1-5-21-1180699209 877415012-318292XXXX-XX... |
| 5261 | 0.1496 | v10.7 The column selector menu shows all available... |
| 5262 | 0.1495 | It defines the tickets the add-on can reopen autom... |
| 5263 | 0.1495 | File permissions define who has access to local fi... |
| 5264 | 0.1495 | File permissions define who has access to local fi... |
| 5265 | 0.1494 | If you are going to use Modern authentication, pas... |
| 5266 | 0.1493 | Run secpol.msc. Browse to Security Settings\Local ... |
| 5267 | 0.1491 | Configure a thresholdbased alert with email recipi... |
| 5268 | 0.1491 | • Free disk space is less than <...> MB—Video reco... |
| 5269 | 0.1490 | Click Add and complete the following fields: User ... |
| 5270 | 0.1489 | While a standalone a ction is not suspicious, mult... |
| 5271 | 0.1486 | When desired, the Review Administrator runs anothe... |
| 5272 | 0.1486 | ActivityRecordWebRequests RequestLimit 200 Interna... |
| 5273 | 0.1486 | Configure the Log On As a Batch Job policy via Loc... |
| 5274 | 0.1483 | Step 6 – Click Add and enter the name of the user ... |
| 5275 | 0.1482 | Ready to Complete Review your virtual machine sett... |
| 5276 | 0.1481 | The script is starting to test your domain control... |
| 5277 | 0.1480 | Then specify domain administrator name and passwor... |
| 5278 | 0.1480 | Then specify domain administrator name and passwor... |
| 5279 | 0.1480 | view=graph-rest-1.0 Specifies password policies fo... |
| 5280 | 0.1477 | This account should be able to create a dedicated ... |
| 5281 | 0.1477 | See the Data Grid Features topic for additional in... |
| 5282 | 0.1474 | Port 1521 is the default client co nnections port,... |
| 5283 | 0.1473 | Monitor hidden shares Even when this option is sel... |
| 5284 | 0.1472 | If you are going to use Modern authentication, pas... |
| 5285 | 0.1472 | If you are going to use Modern authentication, pas... |
| 5286 | 0.1471 | For example: *.Role.DisplayName = MultiValued v10.... |
| 5287 | 0.1471 | See the following Microsoft article for more infor... |
| 5288 | 0.1469 | Same exit codes will be returned by response actio... |
| 5289 | 0.1469 | The response body contains Activity Records and Co... |
| 5290 | 0.1469 | The rest operation = object type For example: add ... |
| 5291 | 0.1468 | Sends an email to the assigned owner(s) for the se... |
| 5292 | 0.1467 | Step 2 – Generate the self-signed certificate. Ste... |
| 5293 | 0.1467 | For example, you can exclude system activity on a ... |
| 5294 | 0.1467 | This value is an enumeration with one possible val... |
| 5295 | 0.1465 | “DisablePasswordExpiratio n” can also be s pecifie... |
| 5296 | 0.1460 | The maximum number of Activity Records the Request... |
| 5297 | 0.1460 | Wrong HTTP request was sent (any except GET or POS... |
| 5298 | 0.1459 | Step 1 – On the computer where you want to execute... |
| 5299 | 0.1458 | You are investigating an incident and want to know... |
| 5300 | 0.1457 | v10.7 Step 5 – Click on the Generate new API key b... |
| 5301 | 0.1456 | Hover over the icon to view the date timestamp of ... |
| 5302 | 0.1455 | Replace Number with a number (e.g., ?count=1500). ... |
| 5303 | 0.1455 | This permission SendAs allows another user to send... |
| 5304 | 0.1454 | In this case, this user will have the most extende... |
| 5305 | 0.1454 | Then you will provide this account in the item. Fo... |
| 5306 | 0.1453 | You can set the After filter to this account's cur... |
| 5307 | 0.1451 | May contain multiple items with the same signInTyp... |
| 5308 | 0.1450 | omitstorelist_ecr.txt Contains a list of classes a... |
| 5309 | 0.1448 | collects stat-in-time data for this share. Follow ... |
| 5310 | 0.1448 | See the Data Collecting Account topic for a dditio... |
| 5311 | 0.1448 | See the Data Collecting Account topic for a dditio... |
| 5312 | 0.1448 | See the Data Collecting Account topic for a dditio... |
| 5313 | 0.1448 | See the Data Collecting Account topic for a dditio... |
| 5314 | 0.1448 | The mailbox is accessed by an account impersonatin... |
| 5315 | 0.1446 | By default, 5 years after a validFrom date. For ex... |
| 5316 | 0.1445 | A listener allows you to connect to a replica with... |
| 5317 | 0.1444 | While a single action is safe, multiple occurrence... |
| 5318 | 0.1442 | Monitor hidden shares Even when this option is sel... |
| 5319 | 0.1442 | Monitor hidden shares Even when this option is sel... |
| 5320 | 0.1442 | Step 4 – On the right, double-click the User Right... |
| 5321 | 0.1442 | Step 5 – Locate the Back up files and directories ... |
| 5322 | 0.1437 | See Filters for more information. Select as many A... |
| 5323 | 0.1435 | Once the limit is reached, the service clears tick... |
| 5324 | 0.1435 | You can set the Item filter to this domain name to... |
| 5325 | 0.1432 | The Filters section helps you show or hide anomali... |
| 5326 | 0.1432 | Step 3 – Set the date and time for when the remind... |
| 5327 | 0.1431 | Navigate to your cluster command prompt through th... |
| 5328 | 0.1430 | Sensitive documents accessible by Everyone Number ... |
| 5329 | 0.1430 | Specify the time period, in seconds. During this t... |
| 5330 | 0.1430 | For example: By default, the list contains add own... |
| 5331 | 0.1430 | Step 3 – Double-click the Log on as a batch job po... |
| 5332 | 0.1429 | Contact your Global administrator. 3. Review your ... |
| 5333 | 0.1429 | Right-click the effective domain controllers polic... |
| 5334 | 0.1429 | Owners with a console user role access the pending... |
| 5335 | 0.1428 | This can be a “no reply” address. Reply-Display — ... |
| 5336 | 0.1428 | RequestTimeout 180 Internal parameter. By default,... |
| 5337 | 0.1428 | Domain2\Johnny, John@domain.com. This operator sho... |
| 5338 | 0.1428 | Object type — monitored object type; for the full ... |
| 5339 | 0.1427 | Once the limit is reached, the service clears tick... |
| 5340 | 0.1426 | Step 2 – Navigate to Start > Run and type "cmd". S... |
| 5341 | 0.1426 | Use this report to Files and Folders Categories by... |
| 5342 | 0.1419 | Wildcard (*) is supported and can be used to repla... |
| 5343 | 0.1419 | The city where a user is City city Example: "Londo... |
| 5344 | 0.1418 | See the section below for the instructions on user... |
| 5345 | 0.1417 | Step 1 – Install the Windows Management Framework ... |
| 5346 | 0.1416 | Modern authentication: v10.7 ◦◦ Selected, Microsof... |
| 5347 | 0.1411 | Click Exclude from search or Include to search and... |
| 5348 | 0.1411 | The Create Review wizard opens. Step 2 – On the Re... |
| 5349 | 0.1409 | Ownership Confirmation The reason for assigning ow... |
| 5350 | 0.1408 | For more information, refer to the following micro... |
| 5351 | 0.1407 | Right-click the effective domain controllers polic... |
| 5352 | 0.1406 | Only tickets with this status can ClosedTicketStat... |
| 5353 | 0.1406 | Group Membership Window When a group trustee appea... |
| 5354 | 0.1406 | Click Pending Changes on the right. In the Pending... |
| 5355 | 0.1405 | Any other antivirus will be considered a risk fact... |
| 5356 | 0.1405 | Table 1: Option Description Filter by account name... |
| 5357 | 0.1404 | Edit the whitelist of permitted antivirus tools. A... |
| 5358 | 0.1404 | Contains a list of AD paths to be omitsnapshotpath... |
| 5359 | 0.1403 | ActivityRecordWebRequests Internal parameter. The ... |
| 5360 | 0.1402 | XLarge Evaluation, PoC Regular Large Hardware envi... |
| 5361 | 0.1401 | Subscribe to search 1. Navigate to Search and set ... |
| 5362 | 0.1399 | Select the following checkboxes: Authentication Au... |
| 5363 | 0.1398 | See the Data Grid Features topic for additional in... |
| 5364 | 0.1397 | For each user account listed, this report shows th... |
| 5365 | 0.1394 | To create a scheduled task: Step 1 – On the comput... |
| 5366 | 0.1393 | Free disk space is less than <...> MB—Video record... |
| 5367 | 0.1393 | There are two levels of access, or roles, which ca... |
| 5368 | 0.1393 | User name – Specify a user name to connect to Pris... |
| 5369 | 0.1392 | Run the following command: Import-PfxCertificate -... |
| 5370 | 0.1391 | Open Remote TCP Port 9004 Follow the steps to open... |
| 5371 | 0.1390 | The table data grid functions the same way as othe... |
| 5372 | 0.1388 | Perform the following steps to create a scheduled ... |
| 5373 | 0.1388 | Perform the following steps to create a scheduled ... |
| 5374 | 0.1388 | Owner performs a review. See the Pending Reviews t... |
| 5375 | 0.1387 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5376 | 0.1387 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5377 | 0.1384 | */ foldername will exclude the specified folder wh... |
| 5378 | 0.1383 | To edit SMS Notifications template, click Customiz... |
| 5379 | 0.1383 | Operator Description Example If you set the Who fi... |
| 5380 | 0.1382 | Filtering does not delete changes, but modifies th... |
| 5381 | 0.1382 | Open Local TCP Port 9003 Follow the steps to open ... |
| 5382 | 0.1381 | See the Settings for Data Collection topic for add... |
| 5383 | 0.1380 | Number of sensitive documents accessible by Everyo... |
| 5384 | 0.1377 | See the Role-Based Access and Delegation topic for... |
| 5385 | 0.1377 | 1122.. Navigate to System → Configuration → Advanc... |
| 5386 | 0.1376 | Select this option to notify users that their pass... |
| 5387 | 0.1375 | Step 2 – Specify what actions should be excluded: ... |
| 5388 | 0.1371 | Update Credential Passwords Credential passwords o... |
| 5389 | 0.1370 | For example, to exclude changes to the Service Des... |
| 5390 | 0.1370 | Select the desired resource(s) and click Add. The ... |
| 5391 | 0.1369 | Enter list or list item URI (Unique resource ident... |
| 5392 | 0.1368 | ≥60% — High Table 1: Risk Assessment formula Defau... |
| 5393 | 0.1366 | PCIDSS compliance standard. You can use this filte... |
| 5394 | 0.1366 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} Leg... |
| 5395 | 0.1365 | Step 5 – Replace the "?/network/admin" parameter w... |
| 5396 | 0.1363 | See the Add Items for Monitoring topic for additio... |
| 5397 | 0.1362 | By default, 3 RequestTimeout 180 minutes. Defines ... |
| 5398 | 0.1361 | By default, this option is disabled. Video Recordi... |
| 5399 | 0.1361 | Currently, the add-on supports only one Prism inst... |
| 5400 | 0.1361 | Once the limit is reached, the service clears acti... |
| 5401 | 0.1361 | Right-click the effective domain controllers polic... |
| 5402 | 0.1360 | lsnrctl start listener_name 99.. Restart the datab... |
| 5403 | 0.1360 | The Console Access wizard opens to the Select Acce... |
| 5404 | 0.1359 | Step 5 – Click the Register button. Application Re... |
| 5405 | 0.1359 | Step 5 – Click the Register button. Application Re... |
| 5406 | 0.1359 | Step 5 – Click the Register button. Application Re... |
| 5407 | 0.1356 | You can track Table 1: Filter Description Supporte... |
| 5408 | 0.1353 | See the Requirements topic for additional informat... |
| 5409 | 0.1352 | So some data may be outdated. – Logon script path ... |
| 5410 | 0.1350 | Make sure the post data files (Continuation mark, ... |
| 5411 | 0.1345 | MailboxSettings.Read 2. Microsoft 365 Management A... |
| 5412 | 0.1345 | The Home > Reports page opens. This page includes ... |
| 5413 | 0.1344 | Pick a subscription and select On or Off in the Mo... |
| 5414 | 0.1343 | v10.7 CAUTION: This will delete all historical dat... |
| 5415 | 0.1343 | Step 5 – In the left pane, expand the Security nod... |
| 5416 | 0.1343 | Table 1: Option Name Description Go to Original Ex... |
| 5417 | 0.1342 | ActivityRecordRequestsRetention RequestLimit 5000 ... |
| 5418 | 0.1341 | URI Reference Only specify URI reference to a list... |
| 5419 | 0.1340 | v10.7 Step 4 – If Microsoft Entra Kerberos or Acti... |
| 5420 | 0.1336 | Considerations and limitations Reporting for case-... |
| 5421 | 0.1336 | Stop Review Window The Stop Review window opens fr... |
| 5422 | 0.1336 | Step 6 – Click Add and enter the name of the user ... |
| 5423 | 0.1335 | The credentials are case sensitive. Specify the ac... |
| 5424 | 0.1333 | This may lead to your sensitive content being high... |
| 5425 | 0.1333 | If you need to modify it later, use this configura... |
| 5426 | 0.1332 | NotEqualTo Max length: 1073741822. StartsWith Ends... |
| 5427 | 0.1329 | Step 4 – Alternatively, you can use the following ... |
| 5428 | 0.1325 | The list of containers does not include child doma... |
| 5429 | 0.1325 | What Shows the path to the modified AD object. v10... |
| 5430 | 0.1324 | Step 8 – Close Group Policy Management console. St... |
| 5431 | 0.1322 | If you select this option, the fields below are no... |
| 5432 | 0.1321 | This page is opened by selecting a review on the M... |
| 5433 | 0.1319 | Use the omitreadaccess.txt to exclude SELECT state... |
| 5434 | 0.1318 | Notes displayed here can only be added or viewed b... |
| 5435 | 0.1318 | Process A ctivity ProcessActivityRecordQueueInterv... |
| 5436 | 0.1317 | Tool-tips display when hovering over the icons ind... |
| 5437 | 0.1316 | On the target SQL Server: 11.. To access SQL Serve... |
| 5438 | 0.1316 | Before configuring the "From" field for user email... |
| 5439 | 0.1315 | Note that hidden anomalies cannot be reviewed in b... |
| 5440 | 0.1315 | expire in <> days In order to send a test email, c... |
| 5441 | 0.1315 | Max length: 21 characters. FooterURL Defines URL t... |
| 5442 | 0.1314 | Select Resource — Select the resource or group to ... |
| 5443 | 0.1314 | You are investigating suspicious user activity. A ... |
| 5444 | 0.1312 | The platform provides security analytics to detect... |
| 5445 | 0.1310 | Scope v10.7 Option Description General Provide the... |
| 5446 | 0.1309 | This account must be granted the database owner (d... |
| 5447 | 0.1309 | Email address Example: JSmith@domain.com + Manager... |
| 5448 | 0.1308 | These filters will be applied using AND logic. Wil... |
| 5449 | 0.1306 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} • L... |
| 5450 | 0.1304 | Follow the steps to modify schema container settin... |
| 5451 | 0.1298 | In this case, you need to provide your API secret ... |
| 5452 | 0.1298 | Policy Name State Enable Persistent Time Stamp "En... |
| 5453 | 0.1296 | • ≤25% — Low • (25% - 50%) — Medium • ≥50% — High ... |
| 5454 | 0.1291 | Follow the steps to run add-on with PowerShell: St... |
| 5455 | 0.1291 | Follow the steps to run add-on with PowerShell: St... |
| 5456 | 0.1291 | Follow the steps to run add-on with PowerShell: St... |
| 5457 | 0.1290 | An identity can be provided by Microsoft (also kno... |
| 5458 | 0.1284 | Wrong HTTP request was sent (any except POST). Err... |
| 5459 | 0.1284 | CAUTION: This will delete all instances of the sel... |
| 5460 | 0.1284 | Step 1 – Under App registrations, select the newly... |
| 5461 | 0.1284 | Step 3 – Select the Exchange Administrator or Glob... |
| 5462 | 0.1284 | See the Filters topic for more information. Select... |
| 5463 | 0.1279 | Step 5 – Click New Rule. In the New Inbound Rule w... |
| 5464 | 0.1278 | Table 2: To... Use... Export Copy search — copy th... |
| 5465 | 0.1276 | Helps identify who accessed important files beside... |
| 5466 | 0.1276 | The minimum value specified across the plans will ... |
| 5467 | 0.1276 | When calculating effective rights and permissions,... |
| 5468 | 0.1276 | Step 3 – Add the Microsoft 365 tenant item. Step 4... |
| 5469 | 0.1275 | v10.7 The information displayed in the table inclu... |
| 5470 | 0.1275 | v10.7 Step 2 – On the Welcome page, click Next to ... |
| 5471 | 0.1275 | Choose Import Type Choose the import type that bes... |
| 5472 | 0.1274 | Follow the procedure described below. Follow the s... |
| 5473 | 0.1272 | For example: NewStation\Shared. Do not specify a d... |
| 5474 | 0.1271 | Internal parameter. Process a ctivity ProcessActiv... |
| 5475 | 0.1271 | However, if you have the Deny log on as a batch jo... |
| 5476 | 0.1270 | For example: dsacls "CN=Deleted Objects,DC=Corp,DC... |
| 5477 | 0.1269 | between an object type and a property, the Contain... |
| 5478 | 0.1269 | If the authentication scheme is different from Ker... |
| 5479 | 0.1269 | Enable monitoring of unauthorized access to mailbo... |
| 5480 | 0.1268 | Import Virtual Machine from Image to Hyper-V Perfo... |
| 5481 | 0.1267 | Limits your search to a unique key of the Activity... |
| 5482 | 0.1267 | Step 2 – Select authentication method that will be... |
| 5483 | 0.1266 | In addition, you can customize your view by select... |
| 5484 | 0.1264 | Step 3 – Click Add. Step 4 – The new secret will b... |
| 5485 | 0.1264 | Step 3 – Click Add. Step 4 – The new secret will b... |
| 5486 | 0.1263 | In this case, this user will have the most extende... |
| 5487 | 0.1261 | nfs_mount Mount to NFS share. replication_create_s... |
| 5488 | 0.1260 | Example: Production default instance: PROD-SQL-01 ... |
| 5489 | 0.1260 | Step 1 – On a target computer navigate to Start > ... |
| 5490 | 0.1258 | Follow the steps: Step 1 – Log on to any domain co... |
| 5491 | 0.1255 | Use this report to plan and control data protectio... |
| 5492 | 0.1255 | Video Recording For these settings to become effec... |
| 5493 | 0.1252 | Choose Network Type Select a virtual switch. Summa... |
| 5494 | 0.1251 | Follow the steps to create Firewall rules manually... |
| 5495 | 0.1250 | Helps identify who accessed important files beside... |
| 5496 | 0.1247 | replication_modify_source_relationship A replicati... |
| 5497 | 0.1247 | You can use HTML tags when editing a template. In ... |
| 5498 | 0.1246 | A featured set of the Privileged Access Security t... |
| 5499 | 0.1245 | This status can appear by accepting the review as-... |
| 5500 | 0.1244 | Step 2 – Specify search filters to narrow your sea... |
| 5501 | 0.1242 | Step 5 – Double-click the newly created rule and o... |
| 5502 | 0.1241 | See this Microsoft article for details Size (MB) S... |
| 5503 | 0.1241 | Step 2 – Navigate to Start > Control Panel and sel... |
| 5504 | 0.1241 | Step 2 – Select authentication method that will be... |
| 5505 | 0.1241 | Step 2 – Select authentication method that will be... |
| 5506 | 0.1239 | The following risk levels are used: Table 1: Risk ... |
| 5507 | 0.1238 | Number of days Shows password age for the account ... |
| 5508 | 0.1237 | To enter multiple accounts, use comma as a separat... |
| 5509 | 0.1237 | To enter multiple accounts, use comma as a separat... |
| 5510 | 0.1234 | Connect to the SQL Server instance. In the left pa... |
| 5511 | 0.1233 | Provide user names as shown in the "Who" column in... |
| 5512 | 0.1230 | See the Add Owner Window topic for additional info... |
| 5513 | 0.1228 | Enter the address that will appear in the "From" f... |
| 5514 | 0.1228 | 0% — Low (0% - 3%) — Medium ≥ 3% — High Documents ... |
| 5515 | 0.1228 | For example, to exclude data on the Disabled Accou... |
| 5516 | 0.1225 | Step 1 – Under App registrations, select the newly... |
| 5517 | 0.1224 | Table 1: Option Description User has been idle for... |
| 5518 | 0.1224 | Decline Declines, or rejects, the owner-recommende... |
| 5519 | 0.1224 | Qumulo Hybrid Cloud File Storage delivers real-tim... |
| 5520 | 0.1222 | + delegated See the corresponding No Microsoft art... |
| 5521 | 0.1222 | Table 1: File Description Syntax omitobjlist.txt C... |
| 5522 | 0.1220 | v10.7 Compatibility Notice Make sure to check your... |
| 5523 | 0.1219 | Before configuring the "From" field for user email... |
| 5524 | 0.1218 | AccessKeyID Access key is used to run requests to ... |
| 5525 | 0.1218 | These are general guidelines you can adopt when se... |
| 5526 | 0.1218 | See the Add Owner Window topic for additional info... |
| 5527 | 0.1218 | See the Navigation and Customize Home Screen topic... |
| 5528 | 0.1216 | Run the Add-On with PowerShell First, provide a pa... |
| 5529 | 0.1215 | Otherwise, leave the default value. Specify paths ... |
| 5530 | 0.1214 | If necessary, modify the parameters as required. F... |
| 5531 | 0.1214 | Remember, only resources with an assigned owner wi... |
| 5532 | 0.1213 | Process A ctivity Record queue every N seconds; in... |
| 5533 | 0.1211 | 33.. Search the group of risks you want to pin to ... |
| 5534 | 0.1210 | Step 2 – Browse to Services > Group Key Distributi... |
| 5535 | 0.1209 | Step 4 – Click New Rule. In the New Inbound Rule w... |
| 5536 | 0.1208 | ◦◦ If you plan to process the Active Directory Del... |
| 5537 | 0.1208 | smb_modify_share An SMB file share was modified. s... |
| 5538 | 0.1208 | Step 2 – Enter the SMTP Server Name in the textbox... |
| 5539 | 0.1207 | Step 2 – Under Groupsclick on the Mail-enabled sec... |
| 5540 | 0.1207 | The credentials are case sensitive. A custom accou... |
| 5541 | 0.1205 | category software Sets the incident Category to "S... |
| 5542 | 0.1204 | The review remains static until it is run again. ◦... |
| 5543 | 0.1203 | Step 5 – Double-click the newly created rule and o... |
| 5544 | 0.1202 | https_proxy_port — specify port used for HTTP prox... |
| 5545 | 0.1201 | Pending actions may include s outstanding reviews.... |
| 5546 | 0.1200 | v10.7 Builtin Administrator Account The Builtin Ad... |
| 5547 | 0.1199 | The body is endpoint. The body is 405 Method Not A... |
| 5548 | 0.1199 | v10.7 Means granted Description For more informati... |
| 5549 | 0.1199 | Multiple Domains The Allow authentication from the... |
| 5550 | 0.1197 | Select the item and click the View Notes button to... |
| 5551 | 0.1196 | This property is required when a user is created a... |
| 5552 | 0.1196 | Consider the following examples: In an Access revi... |
| 5553 | 0.1193 | account@example. *.com Enter root web site URLs. C... |
| 5554 | 0.1192 | This updates to ownership configuration have been ... |
| 5555 | 0.1191 | These individuals would have been asked to suggest... |
| 5556 | 0.1190 | v10.7 Retention Default retention period for repos... |
| 5557 | 0.1189 | An entity (file, link, directory) from the file st... |
| 5558 | 0.1189 | You can: Use the account that already exists OR - ... |
| 5559 | 0.1188 | All filters are applied using AND logic. v10.7 Opt... |
| 5560 | 0.1186 | If you have alternate access mapping configured in... |
| 5561 | 0.1185 | Account type —possible values: ◦ Windows Account ◦... |
| 5562 | 0.1185 | The date and me 6:17:00 PM time information uses I... |
| 5563 | 0.1182 | Delegate Admin SendAs A message was sent using the... |
| 5564 | 0.1180 | A baseline defines a certain safe level or state. ... |
| 5565 | 0.1180 | It allows users to securely access databases witho... |
| 5566 | 0.1180 | If so, data should be filtered accordingly before ... |
| 5567 | 0.1180 | If so, data should be filtered accordingly before ... |
| 5568 | 0.1176 | Enter the address that will appear in the "From" f... |
| 5569 | 0.1173 | Step 3 – Add the "Microsoft 365 tenant" item. Step... |
| 5570 | 0.1171 | Step 5 – Set a name and click Next. Step 6 – Set g... |
| 5571 | 0.1171 | Current access blue icon with a checkmark will tur... |
| 5572 | 0.1171 | v10.7 ◦ Enumerate permissions Also, state-in-time ... |
| 5573 | 0.1170 | If multiple owners were sent the request, the colu... |
| 5574 | 0.1170 | Starts with This operator shows all entries that s... |
| 5575 | 0.1167 | However, if it is enabled and a security policy re... |
| 5576 | 0.1166 | Step 3 – Locate the desired HTML message template.... |
| 5577 | 0.1166 | See the Access Reviews topic for a dditional infor... |
| 5578 | 0.1166 | To run the script with PowerShell: v10.7 Step 1 – ... |
| 5579 | 0.1166 | Step 2 – Click on your username in the top-right c... |
| 5580 | 0.1164 | Navigate to each group where the user belongs to, ... |
| 5581 | 0.1164 | Limits your search results to entries You are inve... |
| 5582 | 0.1164 | The ActivityRecordSearch root element includes the... |
| 5583 | 0.1163 | Enter the IP range you want to exclude, and click ... |
| 5584 | 0.1163 | Your What filter is set to Policy, and so you keep... |
| 5585 | 0.1163 | Once users have been granted console access, they ... |
| 5586 | 0.1162 | Display the following From address in email notifi... |
| 5587 | 0.1160 | Use the arrow buttons to order the owners. Use the... |
| 5588 | 0.1160 | Select this option for users to receive text messa... |
| 5589 | 0.1159 | The Active Directory service account is configured... |
| 5590 | 0.1158 | The next time you run the script, it will start re... |
| 5591 | 0.1158 | User principal name userPrincipalName Example: "us... |
| 5592 | 0.1158 | A user's last logon time is updated only once ever... |
| 5593 | 0.1157 | Examples: http://siteCollection1:3333/ https://sit... |
| 5594 | 0.1155 | Step 3 – In the Security Settings - Local Intranet... |
| 5595 | 0.1155 | v10.7 If you are using a government tenant, please... |
| 5596 | 0.1155 | Switch to Advanced mode to review your current sea... |
| 5597 | 0.1151 | Table 1: Button Description Create Launches the Cr... |
| 5598 | 0.1150 | To continue with this configuration, it will first... |
| 5599 | 0.1150 | When prompted to c onfirm, click Yes. NOTE: For Mi... |
| 5600 | 0.1149 | Reported Attributes The following account attribut... |
| 5601 | 0.1148 | The resource name can be a FQDN or NETBIOS server ... |
| 5602 | 0.1147 | Calculation formulas for each metric are provided ... |
| 5603 | 0.1146 | Provide user names as shown in the "Who" column in... |
| 5604 | 0.1146 | Provide user names as shown in the "Who" column in... |
| 5605 | 0.1146 | Provide user names as shown in the "Who" column in... |
| 5606 | 0.1145 | In this case, the script uses the DNS name of your... |
| 5607 | 0.1144 | Step 1 – On any domain controller in the target do... |
| 5608 | 0.1144 | Then re-enter your password. Click Finish. Step 3 ... |
| 5609 | 0.1141 | A custom account must be granted the same permissi... |
| 5610 | 0.1139 | Step 11 – Navigate to Start > Run and type cmd. In... |
| 5611 | 0.1139 | Step 11 – Navigate to Start > Run and type cmd. In... |
| 5612 | 0.1139 | Select this option to exclude users who do not hav... |
| 5613 | 0.1135 | Is anyone who is charge of "Failed..." anomaly a b... |
| 5614 | 0.1134 | Follow the steps to run the script with PowerShell... |
| 5615 | 0.1133 | impact 1 Sets Impact to "1 – High". urgency 1 Sets... |
| 5616 | 0.1133 | Input the gpupdate /force command and press Enter.... |
| 5617 | 0.1133 | Input the gpupdate /force command and press Enter.... |
| 5618 | 0.1131 | In this case, the script uses the DNS name of your... |
| 5619 | 0.1130 | There are no specific requirements for changing th... |
| 5620 | 0.1129 | Step 2 – In the Microsoft Entra ID admin center, c... |
| 5621 | 0.1128 | Make sure to provide a full object name or path. U... |
| 5622 | 0.1127 | any number of characters. Examples: list/document.... |
| 5623 | 0.1127 | v10.7 Option Description ◦ *computer* - machines w... |
| 5624 | 0.1125 | These can be filters copied from a previous search... |
| 5625 | 0.1124 | See the corresponding Micr osoft Password last cha... |
| 5626 | 0.1124 | membership. Employee details Example: First name S... |
| 5627 | 0.1123 | v10.7 Option Description User has been idle for <.... |
| 5628 | 0.1122 | Specify the account that you want to define this p... |
| 5629 | 0.1122 | Manage Recommendations For active recommendations,... |
| 5630 | 0.1120 | SMTP authentication Select this checkbox if your m... |
| 5631 | 0.1120 | v10.7 The Show Only Changes checkbox is selected b... |
| 5632 | 0.1120 | It must be eight or more characters long. After se... |
| 5633 | 0.1118 | The credentials are case sensitive. Specify the ac... |
| 5634 | 0.1118 | The credentials are case sensitive. Specify the ac... |
| 5635 | 0.1117 | Run the Add-On with PowerShell First, provide a pa... |
| 5636 | 0.1112 | Specify the account to connect to SSRS. Use the fo... |
| 5637 | 0.1112 | *) HKEY_LOCAL_MACHINE\Software\Microsoft\Wi ndows ... |
| 5638 | 0.1112 | Search field – Begin typing the name of the resour... |
| 5639 | 0.1112 | user@tenant.com Specify the user principal name fo... |
| 5640 | 0.1111 | You are investigating suspicious user activity. A ... |
| 5641 | 0.1110 | Follow the steps to assign permissions on the Long... |
| 5642 | 0.1110 | If you have multiple networks on your ESXi Server,... |
| 5643 | 0.1110 | The element may also include a modifier—a match ty... |
| 5644 | 0.1109 | Assign Permission using the Group Policy Managemen... |
| 5645 | 0.1108 | v10.7 Step 7 – Navigate to Start > Run and type cm... |
| 5646 | 0.1104 | Favorite Reports Initially, the Favorite Reports t... |
| 5647 | 0.1103 | ≤ 5% — Low Sharing sensitive data with external Se... |
| 5648 | 0.1103 | Example: "US" or "UK". Maximum length 128. Creatio... |
| 5649 | 0.1102 | The review remains static until it is run again. A... |
| 5650 | 0.1098 | Only resources with assigned Owners can be include... |
| 5651 | 0.1098 | Table 2: Option Description Filter by account name... |
| 5652 | 0.1098 | To perform this procedure, you will need the ADSI ... |
| 5653 | 0.1096 | In this case, you will be prompted to set up IP se... |
| 5654 | 0.1095 | See the corresponding Micro soft article for more ... |
| 5655 | 0.1094 | See the following Microsoft article for additional... |
| 5656 | 0.1094 | See the following Microsoft article for additional... |
| 5657 | 0.1091 | Step 2 – Edit the *.txt files, based on the follow... |
| 5658 | 0.1091 | Step 2 – Edit the *.txt files, based on the follow... |
| 5659 | 0.1091 | Step 2 – Edit the *.txt files, based on the follow... |
| 5660 | 0.1091 | Step 2 – Edit the *.txt files, based on the follow... |
| 5661 | 0.1090 | Step 7 – Click Next. Step 8 – Click Create. Add Em... |
| 5662 | 0.1090 | Table 2: Risk Assessment formula Default risk leve... |
| 5663 | 0.1088 | In this case, you will be prompted to set up IP se... |
| 5664 | 0.1086 | PublicKey Public key you obtained for the API Memb... |
| 5665 | 0.1086 | Max length: 1073741822. • Contains (default) • Doe... |
| 5666 | 0.1082 | User name Specify the account to connect to SSRS. ... |
| 5667 | 0.1082 | In the Connection Settings dialog, enable Select a... |
| 5668 | 0.1081 | If you have alternate access mapping configured in... |
| 5669 | 0.1078 | To do this, add two entries one after another. Ent... |
| 5670 | 0.1078 | Review roles that are already defined for this sco... |
| 5671 | 0.1078 | Step 2 – Enter the description. From the expiratio... |
| 5672 | 0.1078 | Step 2 – Enter the description. From the expiratio... |
| 5673 | 0.1078 | Step 2 – Enter the description. From the expiratio... |
| 5674 | 0.1077 | To edit a report template, click Customize. You ca... |
| 5675 | 0.1076 | You can use a wildcard (*) only if you need to exc... |
| 5676 | 0.1075 | Step 3 – On the right, locate the Organization Man... |
| 5677 | 0.1075 | Add Console Users Follow the steps to grant domain... |
| 5678 | 0.1068 | The request is unauthorized and the body is empty.... |
| 5679 | 0.1064 | To assign permission using the Group Policy Manage... |
| 5680 | 0.1064 | Step 1 – On any domain controller in the target do... |
| 5681 | 0.1063 | Example: John + Last name Shows the last name. Exa... |
| 5682 | 0.1063 | Specify an object type from the Value list or type... |
| 5683 | 0.1061 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 5684 | 0.1060 | v10.7 Remove Changes Window Select the desired res... |
| 5685 | 0.1060 | *.com OmitSitScStoreList.txt Contains a list of Sh... |
| 5686 | 0.1059 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5687 | 0.1059 | property=intelligiblena me Inner_type is optional.... |
| 5688 | 0.1058 | Risks are marked with red color and are easy to sp... |
| 5689 | 0.1053 | If necessary, modify the parameters as required. F... |
| 5690 | 0.1050 | NOTE: While this property can contain accent chara... |
| 5691 | 0.1048 | The most commonly used fi lters are described in U... |
| 5692 | 0.1048 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5693 | 0.1044 | Zone: Custom (policy) When you extend the web appl... |
| 5694 | 0.1044 | Step 1 – In the Resource Owners interface, select ... |
| 5695 | 0.1044 | User Landing Page Role based access controls what ... |
| 5696 | 0.1043 | Select this radio button if the configured Active ... |
| 5697 | 0.1042 | The interfaces available to console users are cont... |
| 5698 | 0.1041 | Table 1: Option Description Notify managers only o... |
| 5699 | 0.1039 | If you set the Who filter to starts with Domain1\J... |
| 5700 | 0.1038 | Step 2 – Under the App registrations section, sele... |
| 5701 | 0.1038 | Step 2 – Under the App registrations section, sele... |
| 5702 | 0.1038 | Step 2 – Under the App registrations section, sele... |
| 5703 | 0.1035 | Ireland Security Table 1: Attribute Description Po... |
| 5704 | 0.1034 | Configure a non-threshold alert with email recipie... |
| 5705 | 0.1034 | Administrative group membership sprawl Edit the wh... |
| 5706 | 0.1030 | Exclusion rules are optional. Click Add Inclusion ... |
| 5707 | 0.1027 | Step 1 – In the Exchange admin cente go to Groupsa... |
| 5708 | 0.1026 | The Delete Review window closes. Delete Review Ins... |
| 5709 | 0.1024 | Since you are looking for GPOs only, select GroupP... |
| 5710 | 0.1024 | The Add new resource wizard opens. Step 2 – On the... |
| 5711 | 0.1022 | Reference for Creating Search Parameters File Revi... |
| 5712 | 0.1021 | Table 2: Option Description Specify SQL Server ins... |
| 5713 | 0.1021 | Ignore users who must change password at next logo... |
| 5714 | 0.1017 | Step 1 – Navigate to Start > Server Manager. Step ... |
| 5715 | 0.1016 | For an exact match, use quotation marks and provid... |
| 5716 | 0.1016 | NOTE: The new password is encrypted in the AccessI... |
| 5717 | 0.1015 | Email address Example: JSmith@domain.com + Office ... |
| 5718 | 0.1012 | Follow the steps to install the certificate to the... |
| 5719 | 0.1010 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 5720 | 0.1008 | Instances are named with date timestamps indicatin... |
| 5721 | 0.1007 | NOTE: For Microsoft 365 permissions, go to Request... |
| 5722 | 0.1007 | Defines a full path to the png image with the new ... |
| 5723 | 0.1006 | The binding command has several environmental vari... |
| 5724 | 0.1006 | See the Grant Required Permissions topic for addit... |
| 5725 | 0.1006 | v10.7 Step 2 – In the command prompt of Windows Po... |
| 5726 | 0.1005 | The Records Management group is less powerful, and... |
| 5727 | 0.1004 | These Substitution Tokens begin and end with the “... |
| 5728 | 0.1003 | Account type —possible values: Windows Account, Lo... |
| 5729 | 0.1002 | You can access Cisco Meraki dashboard using API se... |
| 5730 | 0.1002 | Path The path must be provided in the same format ... |
| 5731 | 0.1002 | v10.7 NOTE: Perform this procedure only if the acc... |
| 5732 | 0.1002 | Step 1 – Under Identity go to Applications > App r... |
| 5733 | 0.1001 | v10.7 Selected Resources Window The Selected Resou... |
| 5734 | 0.1001 | Remember, a resource with declined ownership needs... |
| 5735 | 0.1000 | You can select Directly, Inherited, or both (defau... |
| 5736 | 0.0998 | Input the gpupdate /force command and press Enter.... |
| 5737 | 0.0997 | The ActivityRecordSearch root element includes the... |
| 5738 | 0.0996 | The syntax greatly depends on the tool you use. Yo... |
| 5739 | 0.0996 | If there are several owners of a resource, the lis... |
| 5740 | 0.0994 | The Substitution Tokens will display without suppl... |
| 5741 | 0.0992 | You can find examples of appropriate logo files in... |
| 5742 | 0.0989 | e.g., Who not for the Who filter. If you set the W... |
| 5743 | 0.0987 | Overexposed Sensitive Data Objects For each user a... |
| 5744 | 0.0983 | Step 4 – Open this XML file for edit and add the f... |
| 5745 | 0.0983 | Step 1 – Specify what user accounts should be excl... |
| 5746 | 0.0983 | Step 1 – Specify what user accounts should be excl... |
| 5747 | 0.0983 | NOTE: The password that is generated will contain ... |
| 5748 | 0.0983 | To do so, follow the steps below: 11.. Right-click... |
| 5749 | 0.0982 | Select an action type from the list (Added, Remove... |
| 5750 | 0.0981 | smb_delete_share An SMB file share was deleted. sm... |
| 5751 | 0.0981 | ◦◦ Permissions for ongoing data collection will de... |
| 5752 | 0.0979 | The credentials are case sensitive. A custom accou... |
| 5753 | 0.0979 | Description – Description or explanation of the re... |
| 5754 | 0.0978 | The table displays the following information: ◦◦ R... |
| 5755 | 0.0977 | Maximum length 128. The created date of the Creati... |
| 5756 | 0.0977 | Step 1 – On the Active Directory page, enter the n... |
| 5757 | 0.0976 | Step 1 – Open the Group Policy Management console ... |
| 5758 | 0.0974 | Step 4 – In the Back up files and directories Prop... |
| 5759 | 0.0973 | When using this mode, consider that the "What" fi ... |
| 5760 | 0.0973 | When using this mode, consider that the "What" fi ... |
| 5761 | 0.0973 | Storage Select the destination storage. Disk Forma... |
| 5762 | 0.0973 | Equals NotEqualTo Table 1: Filter Description Supp... |
| 5763 | 0.0972 | For more information, read the following Micr osof... |
| 5764 | 0.0971 | You can use * for cmdlets and their parameters. Li... |
| 5765 | 0.0971 | nfs_create_export Created NFS Export that the clie... |
| 5766 | 0.0970 | In this case, redefine the "Deny log on as a batch... |
| 5767 | 0.0969 | Password Enter a password for SMTP authentication.... |
| 5768 | 0.0969 | Step 6 – When remediation is complete, return to t... |
| 5769 | 0.0968 | If you need to find the $certHash value of a certi... |
| 5770 | 0.0967 | Click Add and complete the following: Option Descr... |
| 5771 | 0.0967 | Example: Ireland + Security v10.7 Attribute Descri... |
| 5772 | 0.0966 | attribute_name—Can be found in the Details column ... |
| 5773 | 0.0965 | Considerations and limitations Reporting for case-... |
| 5774 | 0.0965 | You can set the Before filter to the previous name... |
| 5775 | 0.0965 | a file share that contains a public User Activity ... |
| 5776 | 0.0965 | a file share that contains a public User Activity ... |
| 5777 | 0.0963 | Email address Equals the manager / mail Manager em... |
| 5778 | 0.0962 | The protocol works as follows: When a user tries t... |
| 5779 | 0.0960 | Requires the owner(s) to have responded. CAUTION: ... |
| 5780 | 0.0959 | Step 2 – On the Select Trustee page, enter the fol... |
| 5781 | 0.0955 | Administrators Administrators with access to the s... |
| 5782 | 0.0952 | Table 1: Operator Description Example Contains Thi... |
| 5783 | 0.0952 | Review Type – Type of review Resource Name – The i... |
| 5784 | 0.0951 | Step 2 – Edit the *.txt files, based on the follow... |
| 5785 | 0.0948 | Requires the owner(s) to have responded. Mark Comp... |
| 5786 | 0.0948 | NOTE: For Microsoft 365 permissions, go to Request... |
| 5787 | 0.0947 | 66.. To restore the original view configuration, c... |
| 5788 | 0.0945 | Department — provide the name of the department if... |
| 5789 | 0.0945 | Default is 9898. For details on how to open the po... |
| 5790 | 0.0944 | To edit a report template, click Customize. You ca... |
| 5791 | 0.0942 | Although this is a string collection, only one num... |
| 5792 | 0.0942 | The general format is alias@domain, where the doma... |
| 5793 | 0.0942 | object_type.property_na me=property_value:objec t_... |
| 5794 | 0.0938 | However, it may be changed because users can move ... |
| 5795 | 0.0937 | If you want the script to use another account to a... |
| 5796 | 0.0934 | Follow the steps to exclude specific user activity... |
| 5797 | 0.0934 | Follow the steps to exclude specific user activity... |
| 5798 | 0.0931 | The account must be granted the same permissions a... |
| 5799 | 0.0930 | Such account may have empty password. Yes No + Use... |
| 5800 | 0.0929 | Internet Explorer security settings must be config... |
| 5801 | 0.0928 | Specify an account name (e.g., John) to find all e... |
| 5802 | 0.0927 | These users— Select to exclude specific users' act... |
| 5803 | 0.0924 | If you want the script to use another account to a... |
| 5804 | 0.0923 | NOTE: Using a tool other than a text editor to edi... |
| 5805 | 0.0920 | classname.attrname If there is no full stop, the e... |
| 5806 | 0.0918 | If you renamed this database, provide a new name. ... |
| 5807 | 0.0916 | Each parameter is preceded with a dash; a space se... |
| 5808 | 0.0916 | See the Grant Required Permissions topic for addit... |
| 5809 | 0.0915 | v10.7 Parameter Description Defines whether to use... |
| 5810 | 0.0915 | Reviewer Name — Primary owner assigned to the reso... |
| 5811 | 0.0915 | v10.7 Follow the steps to exclude specific user ac... |
| 5812 | 0.0915 | v10.7 Follow the steps to exclude specific user ac... |
| 5813 | 0.0910 | Equals the Postal-Code attribute. See the Example:... |
| 5814 | 0.0909 | See the following topics for additional Notificati... |
| 5815 | 0.0908 | Step 7 – Run the following command to update group... |
| 5816 | 0.0907 | For example, to exclude a list item with the https... |
| 5817 | 0.0902 | - Last modified Equals the When-Changed attribute.... |
| 5818 | 0.0901 | Step 2 – In the Tenant Information menu, locate th... |
| 5819 | 0.0899 | A wildcard (*) is supported. You can use * for cmd... |
| 5820 | 0.0898 | NOTE: These steps are for modifying domain users w... |
| 5821 | 0.0897 | The Delete Review window closes. Rename Review Win... |
| 5822 | 0.0892 | Step 3 – Click OK when finished. The Rename Review... |
| 5823 | 0.0892 | sysadmin. Type— the security principal type, e.g. ... |
| 5824 | 0.0890 | Add additional input languages Select N to proceed... |
| 5825 | 0.0888 | Authentication Select the authentication type you ... |
| 5826 | 0.0887 | Resource Owners Interface The Resource Owners inte... |
| 5827 | 0.0886 | Farm account Farm account is a service account use... |
| 5828 | 0.0882 | See the procedure below on how to join the compute... |
| 5829 | 0.0881 | SELECT — Allows an account to retrieve data from o... |
| 5830 | 0.0881 | Delete accounts after Specify account inactivity p... |
| 5831 | 0.0880 | Revoke a role assignment • Click next to the user.... |
| 5832 | 0.0876 | To reduce the risk of data leaks and non-complianc... |
| 5833 | 0.0875 | You can select Directly, Inherited, or both (defau... |
| 5834 | 0.0874 | Specify an account name (e.g., John) to find all e... |
| 5835 | 0.0872 | The UPN is an Internetstyle login name for the use... |
| 5836 | 0.0872 | v10.7 Operator Description Example show only data ... |
| 5837 | 0.0870 | Review the table below to discover how different "... |
| 5838 | 0.0868 | For details on how to open the port, refer to the ... |
| 5839 | 0.0868 | The Excel file presents an easy to read format, in... |
| 5840 | 0.0866 | This option does not affect notifications sent to ... |
| 5841 | 0.0866 | Step 2 – Open settings.xml and configure the new a... |
| 5842 | 0.0858 | Yes No + Password last changed Equals the Pwd-Last... |
| 5843 | 0.0856 | Step 1 – Go to Manage > Certificates & secrets and... |
| 5844 | 0.0856 | Step 1 – Go to Manage > Certificates & secrets and... |
| 5845 | 0.0854 | Client Certificate Use default values. Filter Sele... |
| 5846 | 0.0854 | Owner Name — Name of the assigned owner Confirmed ... |
| 5847 | 0.0853 | Use a standard account for that purpose. Follow th... |
| 5848 | 0.0852 | Table 1: Step Description Rename virtual machine S... |
| 5849 | 0.0846 | Click Custom Level. Step 3 – In the Security Setti... |
| 5850 | 0.0845 | Equals This operator shows all entries with the ex... |
| 5851 | 0.0845 | v10.7 Follow the steps to add or remove a Favorite... |
| 5852 | 0.0844 | The credentials are case sensitive. If using a gro... |
| 5853 | 0.0843 | Opens the Remove changes window. Clears all reques... |
| 5854 | 0.0841 | The account must be granted the same permissions a... |
| 5855 | 0.0841 | The account must be granted the same permissions a... |
| 5856 | 0.0840 | Indicates the assigned owner confirmed ownership o... |
| 5857 | 0.0839 | See the procedure below on how to join the compute... |
| 5858 | 0.0836 | On the Action step, select the Allow the connectio... |
| 5859 | 0.0834 | A yellow checkmark icon indicates the new level of... |
| 5860 | 0.0834 | For more information on SharePoint permissions and... |
| 5861 | 0.0833 | See the Group Membership Window topic for addition... |
| 5862 | 0.0833 | *) HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432 NODE\MICROS... |
| 5863 | 0.0832 | Grant Permissions for the Deleted Objects Containe... |
| 5864 | 0.0829 | https://URL Enter list or list item URI (Unique re... |
| 5865 | 0.0821 | This mode allows you to get a sufficient level of ... |
| 5866 | 0.0820 | JSON file must be formatted in accordance with JSO... |
| 5867 | 0.0819 | Filter on Sort by to bring important accounts' dat... |
| 5868 | 0.0816 | For more information on application pool account, ... |
| 5869 | 0.0816 | v10.7 Restore the Default View Follow the steps to... |
| 5870 | 0.0813 | You can skip or define parameters depending on you... |
| 5871 | 0.0813 | To do this, right-click a task and click Run. Run ... |
| 5872 | 0.0805 | These permissions are normally given to a user by ... |
| 5873 | 0.0804 | Filter on Sort by to bring important accounts' dat... |
| 5874 | 0.0798 | However, the OU itself will not be excluded. dc11.... |
| 5875 | 0.0795 | Default retention period is 180 days. v10.7 Option... |
| 5876 | 0.0792 | User name Enter a user name for the SMTP authentic... |
| 5877 | 0.0790 | Resource Pool Select a resource pool to deploy the... |
| 5878 | 0.0785 | { "resourceAppId": "00000003-0000-0000-c000-000000... |
| 5879 | 0.0785 | Some SMTP servers traditionally have been configur... |
| 5880 | 0.0785 | NOTE: This is default location. However, it may be... |
| 5881 | 0.0781 | Step 4 – Right-click in the pane and select Add Ke... |
| 5882 | 0.0774 | These entries correspond to differen t The value l... |
| 5883 | 0.0772 | User name Enter a user name for the SMTP authentic... |
| 5884 | 0.0769 | Step 2 – Click Search to apply your filters. By de... |
| 5885 | 0.0765 | Failure to do this could result in being locked-ou... |
| 5886 | 0.0758 | See the Rename Review Window topic for additional ... |
| 5887 | 0.0758 | v10.7 Step 3 – By default, the table displays only... |
| 5888 | 0.0757 | Step 1 – In the Configuration interface on the Con... |
| 5889 | 0.0754 | Each individual permission can be enabled or disab... |
| 5890 | 0.0751 | To configure your Cisco IOS devices, do the follow... |
| 5891 | 0.0748 | Select this checkbox if your mail server requires ... |
| 5892 | 0.0748 | This can help you to simplify product administrati... |
| 5893 | 0.0748 | Press Enter to start. Step Description Specify a n... |
| 5894 | 0.0747 | See the corresponding Micro soft article for more ... |
| 5895 | 0.0740 | Do the following depending on your infrastructure:... |
| 5896 | 0.0740 | It helps organize and centralize sign-in procedure... |
| 5897 | 0.0738 | Specify account inactivity period, after which a S... |
| 5898 | 0.0737 | The user account should be a Cloud-only account. F... |
| 5899 | 0.0735 | Step 4 – Right-click in the pane and select Add Ke... |
| 5900 | 0.0734 | This allows you to add one resource at a time and ... |
| 5901 | 0.0731 | Hovering over the bar will display the number of i... |
| 5902 | 0.0730 | Edit Notes Opens the Edit Notes window for the sel... |
| 5903 | 0.0728 | Desired – Change suggested by the owner. It could ... |
| 5904 | 0.0724 | Data source Specify a data source from the Since y... |
| 5905 | 0.0723 | Port number Specify your SMTP server port number. ... |
| 5906 | 0.0720 | Selecting such databases leads to data overwrites ... |
| 5907 | 0.0719 | The account must be granted the same permissions a... |
| 5908 | 0.0719 | The account must be granted the same permissions a... |
| 5909 | 0.0713 | You can skip or define parameters depending on you... |
| 5910 | 0.0709 | The user is removed from the list on the Console A... |
| 5911 | 0.0709 | The selected user appears in the Owner list. Confi... |
| 5912 | 0.0707 | If you deployed your Oracle Database in a cluster ... |
| 5913 | 0.0705 | You can skip or define parameters depending on you... |
| 5914 | 0.0704 | However, it can be customized during installation.... |
| 5915 | 0.0699 | NOTE: If you use more than one region in your Regi... |
| 5916 | 0.0694 | Data categories Limits your search results to entr... |
| 5917 | 0.0690 | Update In-Script Parameters Step 1 – Right-click a... |
| 5918 | 0.0689 | The C onfirm Removal window opens. v10.7 Step 2 – ... |
| 5919 | 0.0689 | In the Connection Settings dialog, enable Select a... |
| 5920 | 0.0689 | Step 5 – Apply settings and return to the <Share_N... |
| 5921 | 0.0688 | The owner will be required to complete the review ... |
| 5922 | 0.0681 | First, provide a path to your add-on followed by s... |
| 5923 | 0.0668 | Users Select the users to be excluded from search ... |
| 5924 | 0.0664 | If the value is false, proceed with the steps belo... |
| 5925 | 0.0663 | Make sure to provide a full object name or path. T... |
| 5926 | 0.0660 | The credentials are case sensitive. If using a gro... |
| 5927 | 0.0659 | Assign a new SSL certificate APIAdminTool.exe api ... |
| 5928 | 0.0657 | Domain1\John, Domain1\Johnson, and Domain1\Johnny.... |
| 5929 | 0.0653 | Removing a resource from this table does not delet... |
| 5930 | 0.0651 | Example: New York + ZIP/postal code Equals the Pos... |
| 5931 | 0.0649 | RECOMMENDED: Prepare a dedicated gMSA for these pu... |
| 5932 | 0.0642 | Step 4 – On the Actions tab, click New and specify... |
| 5933 | 0.0642 | Step 4 – On the Actions tab, click New and specify... |
| 5934 | 0.0635 | Assign Permission Using the Group Policy Managemen... |
| 5935 | 0.0625 | If multiple domains are known, then the username n... |
| 5936 | 0.0623 | • Contains (default) • DoesNotContain • Equals • N... |
| 5937 | 0.0620 | Secure Console Access Enable Secure Sockets Layer ... |
| 5938 | 0.0619 | { "resourceAppId": "00000003-0000-0ff1-ce00-000000... |
| 5939 | 0.0618 | Historically, the default for SMTP has been port 2... |
| 5940 | 0.0614 | This key is created once, so if there are any gMSA... |
| 5941 | 0.0614 | This property is required when a user is created. ... |
| 5942 | 0.0613 | Use Secure Sockets Layer encrypted connection (SSL... |
| 5943 | 0.0612 | Specifies the password profile for a user. The pas... |
| 5944 | 0.0610 | Modify filter If you need to modify the When filte... |
| 5945 | 0.0608 | Virtual Machines Select the virtual machines to be... |
| 5946 | 0.0601 | This allows you to make changes to the assigned ow... |
| 5947 | 0.0600 | StartsWith Max length: 255. EndsWith Contains (def... |
| 5948 | 0.0596 | v10.7 CAUTION: This will prevent owners from compl... |
| 5949 | 0.0594 | gmail.com, hotmail.com, etc., may have to supply a... |
| 5950 | 0.0593 | APIAdminTool.exe api https certificate Run this co... |
| 5951 | 0.0591 | immediately. So some data may be outdated. Equals ... |
| 5952 | 0.0588 | Example: The Main Road; 10 + City Shows the locali... |
| 5953 | 0.0588 | Step 4 – In the Permission Entry for <Folder_Name>... |
| 5954 | 0.0584 | Step 2 – On the General tab, specify a task name. ... |
| 5955 | 0.0580 | Step 4 – The Windows PowerShell opens and automati... |
| 5956 | 0.0579 | Step 4 – On the Actions tab, click New and specify... |
| 5957 | 0.0575 | Most parameters are optional, the script uses the ... |
| 5958 | 0.0573 | On the other hand, including a filter value ensure... |
| 5959 | 0.0570 | See the Ownership Confirmation topic for additiona... |
| 5960 | 0.0560 | Example: John Smith + Logon name (sAMAccountName) ... |
| 5961 | 0.0560 | Follow the steps to remove a user’s configured con... |
| 5962 | 0.0559 | Step 3 – Configure the following settings: Enable ... |
| 5963 | 0.0559 | Then provide the full path of the machine to exclu... |
| 5964 | 0.0558 | When planning for hardware resources, consider tha... |
| 5965 | 0.0557 | Table 1: Operator Description Example Not equal to... |
| 5966 | 0.0557 | 0% — Low Files may be shared with any users Sensit... |
| 5967 | 0.0556 | Step 4 – On the Actions tab, click New and specify... |
| 5968 | 0.0555 | v10.7 Enter a name in the search field to find and... |
| 5969 | 0.0555 | attribute_name—Can be found in the Details column ... |
| 5970 | 0.0553 | Equals the sAMAccountName attribute. See the Examp... |
| 5971 | 0.0549 | Step 2 – In the <Share_Name> Properties dialog, se... |
| 5972 | 0.0545 | Servers with inappropriate operating systems Edit ... |
| 5973 | 0.0544 | The name may not consist entirely of digits and ma... |
| 5974 | 0.0538 | A custom account must be granted the same permissi... |
| 5975 | 0.0537 | This option allows the Review Administrator to pro... |
| 5976 | 0.0537 | The Main Road; 10 Shows the locality, such as Exam... |
| 5977 | 0.0533 | In this case, this user will have the most extende... |
| 5978 | 0.0533 | In this case, this user will have the most extende... |
| 5979 | 0.0533 | In this case, this user will have the most extende... |
| 5980 | 0.0533 | In this case, this user will have the most extende... |
| 5981 | 0.0533 | In this case, this user will have the most extende... |
| 5982 | 0.0533 | In this case, this user will have the most extende... |
| 5983 | 0.0527 | Characters may be also s pecified with hex value u... |
| 5984 | 0.0525 | A custom account must be granted the same permissi... |
| 5985 | 0.0524 | Client Certificate Use default values. Filter Sele... |
| 5986 | 0.0524 | ◦ validFrom—Optional, defines a certificat e start... |
| 5987 | 0.0524 | ◦ validFrom—Optional, defines a certificat e start... |
| 5988 | 0.0520 | Table 1: Attribute Description Possible values Fil... |
| 5989 | 0.0517 | Each parameter is preceded with a dash; a space se... |
| 5990 | 0.0505 | You can skip some parameters— the script uses a de... |
| 5991 | 0.0502 | The credentials are case sensitive. A custom accou... |
| 5992 | 0.0501 | NOTE: If you use more than one region in your envi... |
| 5993 | 0.0499 | Create a KDS Root Key If the KDS root key does not... |
| 5994 | 0.0498 | Managers will receive a notification in the day wh... |
| 5995 | 0.0489 | To exclude the certain user's mailbox, enter usern... |
| 5996 | 0.0488 | exclude the exact user specified and Not equal to ... |
| 5997 | 0.0485 | These granted or denied permissions take preferenc... |
| 5998 | 0.0485 | Sales Equals the TelephoneNumber attribute. See th... |
| 5999 | 0.0483 | Each parameter is preceded with a dash; a space se... |
| 6000 | 0.0474 | Edit the mailboxestoinclude.txt file to specify ma... |
| 6001 | 0.0471 | Owners are encouraged to leave notes explaining wh... |
| 6002 | 0.0469 | Owners are encouraged to leave notes explaining wh... |
| 6003 | 0.0465 | User runs program through Run As Application Run A... |
| 6004 | 0.0462 | Delete Console Users CAUTION: Confirmation is not ... |
| 6005 | 0.0460 | Opens the Rename Review window for modifying the R... |
| 6006 | 0.0456 | NotEqualTo Table 1: Filter Description Supported O... |
| 6007 | 0.0451 | Thus, there is no need to grant any permissions to... |
| 6008 | 0.0447 | Import Paste search — paste the search filters you... |
| 6009 | 0.0447 | v10.7 Access is enabled – A user's account must be... |
| 6010 | 0.0445 | Review the following for additional information. O... |
| 6011 | 0.0439 | See the corresponding Micr osoft Example: JSmith@d... |
| 6012 | 0.0437 | before and after values, start and end dates. You ... |
| 6013 | 0.0432 | server_instance:resource _path where: Contains a l... |
| 6014 | 0.0430 | You can skip some parameters— the script uses a de... |
| 6015 | 0.0430 | By default, 5 years after a validFrom date. For ex... |
| 6016 | 0.0426 | Click Add. Schema and object names are case sensit... |
| 6017 | 0.0425 | Assumes that the script runs on the RADIUS server.... |
| 6018 | 0.0425 | Step 2 – Type or edit the note in the textbox. Ste... |
| 6019 | 0.0418 | SharePoint Server permission levels are defined at... |
| 6020 | 0.0416 | If the OS has Internet access, it is granted 180 d... |
| 6021 | 0.0410 | In the Search field in the Simple mode, this opera... |
| 6022 | 0.0408 | Each parameter is preceded with a dash; a space se... |
| 6023 | 0.0408 | Each parameter is preceded with a dash; a space se... |
| 6024 | 0.0408 | Specifies the password profile for the user. The p... |
| 6025 | 0.0408 | ◦ store—Optional, defines the store name where cer... |
| 6026 | 0.0406 | Decline Declines, or rejects, the owner-recommende... |
| 6027 | 0.0405 | ◦ store—Optional, defines the store name where cer... |
| 6028 | 0.0405 | Each parameter is preceded with a dash; a space se... |
| 6029 | 0.0403 | [Partially filled bar] with a non-zero% – Indicate... |
| 6030 | 0.0401 | See the Update Resource Wizard topic for a ddition... |
| 6031 | 0.0390 | Check the columns you want to include and clear un... |
| 6032 | 0.0389 | In this case, this user will have the most extende... |
| 6033 | 0.0389 | In this case, this user will have the most extende... |
| 6034 | 0.0389 | In this case, this user will have the most extende... |
| 6035 | 0.0389 | In this case, this user will have the most extende... |
| 6036 | 0.0389 | In this case, this user will have the most extende... |
| 6037 | 0.0388 | precise results, e.g., \ \FS\Share\NewPolicy.docx.... |
| 6038 | 0.0374 | Column—Specify table column name. The following co... |
| 6039 | 0.0352 | A custom account must be granted the same permissi... |
| 6040 | 0.0318 | If you set the Not in group condition for Who filt... |
| 6041 | 0.0317 | Search results will be sorted by all selected filt... |
| 6042 | 0.0283 | Lock statuses apply to a site collection and are u... |
| 6043 | 0.0281 | Change password on next sign in passwordProfile Ye... |
| 6044 | 0.0280 | Move to a specific OU after OU name—Specify OU nam... |
| 6045 | 0.0256 | Step 1 – Select the review and click Rename. The R... |
| 6046 | 0.0252 | UserName Defines a username used to connect to SQL... |
| 6047 | 0.0240 | + Smith Equals the Title attribut e. See the corre... |
| 6048 | 0.0225 | See the following Microsoft article for additional... |
| 6049 | 0.0222 | Select Add User. Table 1: To... Do... 2. In the di... |
| 6050 | 0.0215 | For more information on SharePoint web applica tio... |
| 6051 | 0.0212 | Modify filter Double-click the filter and type a n... |
| 6052 | 0.0207 | Add to Favorites This option is greyed out when vi... |
| 6053 | 0.0193 | Otherwise, 'Before' and 'After' values will not be... |
| 6054 | 0.0175 | This option is greyed out when viewing the Favorit... |
| 6055 | 0.0174 | Wildcards (* and ?) are supported. A backslash (\)... |
| 6056 | 0.0171 | Unchecking this option allows you to configure acc... |
| 6057 | 0.0167 | After the application configuration, you can restr... |
| 6058 | 0.0166 | RADIUSHost localhost Assumes that the script runs ... |
| 6059 | 0.0159 | Refer to the following Oracle help article for mor... |
| 6060 | 0.0159 | v10.7 To Enable JavaScript Follow the steps to ena... |
| 6061 | 0.0150 | Spaces do not separate values, so the whole expres... |
| 6062 | 0.0145 | You are investigating an incident in which the SAM... |
| 6063 | 0.0144 | Change password on next sign in with MFA passwordP... |
| 6064 | 0.0113 | The element may also include a modifier—a match ty... |
| 6065 | 0.0107 | • Provider name — Specify provider name. Property ... |
| 6066 | 0.0098 | Disable accounts after Specify account inactivity ... |
| 6067 | 0.0084 | Maximum length is 64 characters. The name displaye... |
| 6068 | 0.0072 | Simply select the edges of the column headers and ... |
| 6069 | 0.0041 | Click Yes. v10.7 Step 7 – On the Configure Web Ser... |
| 6070 | 0.0026 | Does not contain This operator shows all entries e... |
| 6071 | 0.0018 | Follow the steps to add or edit a note. Step 1 – S... |
| 6072 | 0.0014 | Department department Example: "Accounting and Fin... |
| 6073 | 0.0010 | If you set the Who filter to ends with John, you w... |
| 6074 | -0.0003 | The filter acts as a wildcard, filtering the table... |
| 6075 | -0.0010 | If you set the Who filter to ends This operator sh... |
| 6076 | -0.0017 | See the corresponding Micro soft article for more ... |
| 6077 | -0.0018 | To further restrict your search, right-click the v... |
| 6078 | -0.0023 | Once the first user with the role of Administrator... |
| 6079 | -0.0029 | See Use Filters in Advanced Mode for details. By d... |
| 6080 | -0.0031 | An arrow will appear next to the column name indic... |
| 6081 | -0.0046 | Each ActivityRecord object is collected in braces ... |
| 6082 | -0.0075 | v10.7 Step 3 – Click close (x): Step 4 – Click App... |
| 6083 | -0.0088 | See the Example: corresponding Micro soft Canonica... |
| 6084 | -0.0092 | IE might be disabled with GPO, but it should not b... |
| 6085 | -0.0100 | This operator shows all entries except those that ... |
| 6086 | -0.0101 | Enter a value you want to search for. Alternativel... |
| 6087 | -0.0134 | If you want to specify several computers, you can ... |
| 6088 | -0.0144 | The $port value must be accurate for your environm... |
| 6089 | -0.0158 | v10.7 Click the filter icon for the column you wan... |
| 6090 | -0.0161 | Rest assured that your configurations and data wil... |
| 6091 | -0.0175 | Navigate to Tools 2. Click Select columns. The dia... |
| 6092 | -0.0185 | However, not every tile supports all types of size... |
| 6093 | -0.0199 | The permissions inheritance for any of these eleme... |
| 6094 | -0.0241 | Then the search query will return only data matchi... |
| 6095 | -0.0291 | Step 2 – Select Add tile. Either search for the ti... |
| 6096 | -0.0306 | It may contain letters (a-z, A-Z), numbers (0-9), ... |
| 6097 | -0.0321 | You can set the Details filter to 242464 to find t... |
| 6098 | -0.0330 | Below is an example of a mask: ◦ * - any machine ◦... |
| 6099 | -0.0360 | See the examples below for more information. v10.7... |
| 6100 | -0.0364 | The filter icon is highlighted orange for a column... |
| 6101 | -0.0398 | Step 1 – Click Customize in the upper right corner... |
| 6102 | -0.0452 | Below is an example of a mask: • * - any machine •... |
| 6103 | -0.0482 | Additionally, tiles with less information have sma... |
| 6104 | -0.0509 | dc11.local/OU will exclude the OU itself. However,... |
| 6105 | -0.0697 | Wildcards (*?) are supported and applied as follow... |
| 6106 | -0.0736 | Step 3 – Click Add and the selected tile appears o... |
| 6107 | -0.0769 | It cannot be locked out of any subsite, list, libr... |
| 6108 | -0.0999 | Remove a Tile from the Home Screen Follow the step... |

</details>

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

