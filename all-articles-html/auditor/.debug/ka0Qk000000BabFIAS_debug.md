# Article Processing Debug: ka0Qk000000BabFIAS

**Generated:** 2025-05-31 23:57:10

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
<details>
<summary>Full Similarity Score Distribution</summary>

| # | Score | Text Preview |
|---|-------|-------------|
| 1 | 0.7229 | v10.7 Review Past Event Log Entries Netwrix Audito... |
| 2 | 0.7136 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 3 | 0.7131 | Audit data is stored to the Audit databases and th... |
| 4 | 0.7047 | The current version of Netwrix Auditor contains th... |
| 5 | 0.6964 | EventStorePath — Select where to store temporary f... |
| 6 | 0.6855 | To review Event Trace Session objects' configurati... |
| 7 | 0.6841 | Auditor informs you if you are running out of spac... |
| 8 | 0.6832 | See File-Based Repository for Long-Term Archive fo... |
| 9 | 0.6832 | Netwrix recommends not to store these files out of... |
| 10 | 0.6811 | Download free add-ons from Netwrix Auditor Add-on ... |
| 11 | 0.6768 | The Netwrix Auditor Integration event log will be ... |
| 12 | 0.6763 | Netwrix_Auditor_API Stores activity records collec... |
| 13 | 0.6731 | Event Log Manager Netwrix Auditor Event Log Manage... |
| 14 | 0.6726 | Before you start monitoring your Oracle Database w... |
| 15 | 0.6722 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 16 | 0.6722 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 17 | 0.6722 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 18 | 0.6722 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 19 | 0.6722 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 20 | 0.6671 | Event log Select event log that contains desired e... |
| 21 | 0.6658 | To detect actual change initiator, Netwrix Auditor... |
| 22 | 0.6648 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 23 | 0.6645 | Netwrix Auditor Server — the central component tha... |
| 24 | 0.6641 | Step 2 – In the Netwrix Auditor Event Viewer windo... |
| 25 | 0.6635 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 26 | 0.6635 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 27 | 0.6599 | Make sure there is enough disk space allocated for... |
| 28 | 0.6584 | Use the Database statistics widget to examine data... |
| 29 | 0.6582 | Netwrix Auditor allows importing data from the Lon... |
| 30 | 0.6579 | If you want to investigate incidents that occurred... |
| 31 | 0.6574 | Please contact Netwrix Technical Support team to m... |
| 32 | 0.6540 | v10.7 Netwrix Auditor System Health Log When an er... |
| 33 | 0.6532 | See the Appendix. Netwrix Auditor Integration Even... |
| 34 | 0.6530 | Depending on the number of Activity Records stored... |
| 35 | 0.6530 | Depending on the number of Activity Records stored... |
| 36 | 0.6530 | Depending on the number of Activity Records stored... |
| 37 | 0.6524 | Step 4 – Hit Enter. Depending on the number of Act... |
| 38 | 0.6483 | Event Log You can fine-tune Netwrix Auditor by spe... |
| 39 | 0.6480 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 40 | 0.6466 | Step 3 – Navigate to the Monitored computers list ... |
| 41 | 0.6465 | Netwrix Auditor supports integration with Netwrix ... |
| 42 | 0.6455 | See Data Collecting Account for a dditional inform... |
| 43 | 0.6454 | Netwrix Auditor Serverthen writes the Activity Rec... |
| 44 | 0.6454 | Select where to store temporary files of syslog me... |
| 45 | 0.6452 | Other users can obtain audit data by email or with... |
| 46 | 0.6450 | Audit Configuration Assistant is a part of Netwrix... |
| 47 | 0.6446 | Other users obtain the data they need via email or... |
| 48 | 0.6443 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 49 | 0.6419 | Depending on the number of Activity Records stored... |
| 50 | 0.6418 | The add-on connects to the Auditor server and retr... |
| 51 | 0.6416 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 52 | 0.6409 | See the Supported Data Sources configuration topic... |
| 53 | 0.6405 | Review the table below for more information. To...... |
| 54 | 0.6402 | To do this, right-click a task and click Run. Work... |
| 55 | 0.6380 | Work with Collected Data Follow the steps to work ... |
| 56 | 0.6359 | After you click View details, the following inform... |
| 57 | 0.6356 | Specify an item name. Make sure to create a dedica... |
| 58 | 0.6353 | Collect data for state-in-time reports Configure N... |
| 59 | 0.6344 | To do this, right-click a task and click Run. Work... |
| 60 | 0.6335 | Navigate to C:\ProgramData\Netwrix Auditor\Windows... |
| 61 | 0.6334 | Go to the Audit Database section and make sure tha... |
| 62 | 0.6325 | Shows all activity records imported with Netwrix A... |
| 63 | 0.6324 | Netwrix Auditor will inform you if you are running... |
| 64 | 0.6310 | Remember to set the filter to “Data Sourceequals O... |
| 65 | 0.6303 | Step 1 – In Auditor, navigate to Reports > Organiz... |
| 66 | 0.6295 | See the Normal and Enterprise Modes for Clusters t... |
| 67 | 0.6295 | Monitoring plan for File Server data source with '... |
| 68 | 0.6287 | The add-on connects to the Netwrix Auditor server ... |
| 69 | 0.6287 | The add-on connects to the Netwrix Auditor server ... |
| 70 | 0.6282 | Manually – Native audit settings must be adjusted ... |
| 71 | 0.6280 | Its key capabilities are as follows: Allows Audito... |
| 72 | 0.6276 | Netwrix_ImportDB Stores data imported from Long-Te... |
| 73 | 0.6275 | Working Folder The working folder is a file-based ... |
| 74 | 0.6259 | Table 1: Service account Description Account for d... |
| 75 | 0.6257 | For this data to be provided to Splunk, it adds a ... |
| 76 | 0.6250 | See the Adjust Security Event Log Size and Retenti... |
| 77 | 0.6248 | Monitoring plans Select monitoring plans whose aud... |
| 78 | 0.6247 | To reduce the volume of the stored logs and the co... |
| 79 | 0.6245 | Netwrix Auditor Event Log Manager synchronizes Aud... |
| 80 | 0.6242 | Proper audit configuration is required to ensure a... |
| 81 | 0.6242 | Proper audit configuration is required to ensure a... |
| 82 | 0.6242 | Proper audit configuration is required to ensure a... |
| 83 | 0.6242 | Proper audit configuration is required to ensure a... |
| 84 | 0.6242 | Proper audit configuration is required to ensure a... |
| 85 | 0.6242 | Proper audit configuration is required to ensure a... |
| 86 | 0.6242 | Proper audit configuration is required to ensure a... |
| 87 | 0.6238 | v10.7 Investigations By default, the Audit Databas... |
| 88 | 0.6223 | Step 2 – Select Netwrix Auditor Event Log Compress... |
| 89 | 0.6222 | It means you retrieved all Activity Records matchi... |
| 90 | 0.6219 | ◦◦ Enable SharePoint Administration Service on the... |
| 91 | 0.6213 | v10.7 To instruct Netwrix Auditor to collect data ... |
| 92 | 0.6202 | Overexposed Files and Folders Monitoring plan for ... |
| 93 | 0.6194 | Proper audit configuration is required to ensure a... |
| 94 | 0.6193 | v10.7 Logon Activity Netwrix Auditor relies on nat... |
| 95 | 0.6190 | See the View Reports topic for additional informat... |
| 96 | 0.6189 | Work with Collected Data Step 1 – On the computer ... |
| 97 | 0.6180 | The add-on processes these Syslog messages into Au... |
| 98 | 0.6178 | Step 2 – Select the Netwrix Auditor User Activity ... |
| 99 | 0.6178 | Stores data collected by Netwrix Auditor self-audi... |
| 100 | 0.6175 | Monitoring plan for File Server data source with '... |
| 101 | 0.6174 | v10.7 33.. The add-on creates a special Windows ev... |
| 102 | 0.6173 | For that, start Netwrix Auditor client and navigat... |
| 103 | 0.6171 | Table 1: Option Description To find out a log’s na... |
| 104 | 0.6171 | Step 1 – Navigate to Start > Netwrix Auditor > Net... |
| 105 | 0.6154 | NetwrixAuditorPlanItem — Specify an item name here... |
| 106 | 0.6151 | Select monitoring plans whose audit data you want ... |
| 107 | 0.6149 | Complete the following fields: Table 1: Option Des... |
| 108 | 0.6144 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 109 | 0.6141 | The add-on connects to the Netwrix Auditor Server ... |
| 110 | 0.6138 | Netwrix Auditor is a visibility platform for user ... |
| 111 | 0.6125 | Ensure the script execution completed successfully... |
| 112 | 0.6124 | For that, start Auditor client and navigate to Sea... |
| 113 | 0.6122 | For that, start Auditor client and navigate to Sea... |
| 114 | 0.6113 | Netwrix Auditor allows auditing the entire SharePo... |
| 115 | 0.6113 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 116 | 0.6109 | 44.. After that, you will be able to attach the fi... |
| 117 | 0.6106 | For that, start Auditor client and navigate to Sea... |
| 118 | 0.6103 | Ensure the script execution completed successfully... |
| 119 | 0.6102 | All Integration API Activity Shows all activity re... |
| 120 | 0.6099 | ◦◦ To provide a coherent picture of changes that o... |
| 121 | 0.6094 | You can choose whether to import the list once, or... |
| 122 | 0.6092 | Once troubleshooting has finished, it is recommend... |
| 123 | 0.6088 | Table 1: To monitor... Execute the command... Conf... |
| 124 | 0.6088 | For that, start Auditor client and navigate to Sea... |
| 125 | 0.6087 | For example, warnings on failed data collection or... |
| 126 | 0.6083 | Accept List Address Specify a list of IP addresses... |
| 127 | 0.6080 | Step 1 – Start Netwrix Auditor Event Log Manager a... |
| 128 | 0.6069 | By default, the Netwrix Auditor Integration event ... |
| 129 | 0.6069 | By default, the Netwrix Auditor Integration event ... |
| 130 | 0.6066 | The product does not log any errors on these event... |
| 131 | 0.6062 | When prompted to configure the Audit database sett... |
| 132 | 0.6050 | v10.7 Create Your First Monitoring Plan To start c... |
| 133 | 0.6044 | Work with Collected Data Follow the steps to work ... |
| 134 | 0.6043 | On the computer where Auditor Server resides, you ... |
| 135 | 0.6035 | Self-Audit Built-in Netwrix Auditor self-audit all... |
| 136 | 0.6029 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 137 | 0.6026 | Step 2 – In the Event Viewer dialog, navigate to E... |
| 138 | 0.6023 | Netwrix Auditor Settings In the Settings section, ... |
| 139 | 0.5994 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 140 | 0.5993 | v10.7 Configure Audit Database Settings When you f... |
| 141 | 0.5988 | CAUTION: Folder associated with NETWRIX AUDITOR mu... |
| 142 | 0.5986 | General On the General tab you can configure globa... |
| 143 | 0.5984 | By default, the Netwrix Auditor Integration event ... |
| 144 | 0.5981 | ◦◦ To get ‘Who’ (initiator) and ‘When’ (date and t... |
| 145 | 0.5976 | So, when planning your Netwrix Auditor deployment,... |
| 146 | 0.5976 | App — points where the index configuration is stor... |
| 147 | 0.5964 | See the Monitoring Overview topic for additional i... |
| 148 | 0.5959 | For more information on audit configuration, refer... |
| 149 | 0.5958 | v10.7 Requirements This topic provides the require... |
| 150 | 0.5957 | Table 1: Option Description Monitor this data sour... |
| 151 | 0.5956 | This procedure describes the basic steps, required... |
| 152 | 0.5952 | Netwrix_CommonDB Stores views to provide cross-dat... |
| 153 | 0.5951 | Specify the time range for which you want to retri... |
| 154 | 0.5948 | Click Run to start collecting data with the Add-On... |
| 155 | 0.5948 | Data collection for this monitoring plan might not... |
| 156 | 0.5947 | The helpdesk supervisor has access to both folders... |
| 157 | 0.5945 | To review data sources and items included in each ... |
| 158 | 0.5943 | EventData is filled in with data from the Activity... |
| 159 | 0.5942 | v10.7 Exchange Netwrix Auditor relies on native lo... |
| 160 | 0.5939 | The option is not available for auditing User Acti... |
| 161 | 0.5937 | Log File: By default the Access Reviews applicatio... |
| 162 | 0.5933 | See the following Netwrix knowledge base article f... |
| 163 | 0.5931 | See the Monitoring Planstopic for additional infor... |
| 164 | 0.5928 | Aggregating data into a single audit trail simplif... |
| 165 | 0.5926 | These settings must be configured for Everyone sec... |
| 166 | 0.5923 | To review Event Trace Session objects' configurati... |
| 167 | 0.5921 | Therefore, successful change and access auditing r... |
| 168 | 0.5921 | Therefore, successful change and access auditing r... |
| 169 | 0.5921 | Therefore, successful change and access auditing r... |
| 170 | 0.5921 | Therefore, successful change and access auditing r... |
| 171 | 0.5921 | Therefore, successful change and access auditing r... |
| 172 | 0.5921 | Therefore, successful change and access auditing r... |
| 173 | 0.5921 | Therefore, successful change and access auditing r... |
| 174 | 0.5921 | Therefore, successful change and access auditing r... |
| 175 | 0.5921 | Therefore, successful change and access auditing r... |
| 176 | 0.5921 | Therefore, successful change and access auditing r... |
| 177 | 0.5920 | Netwrix recommends you to create a dedicated folde... |
| 178 | 0.5919 | Netwrix Auditor Event Log Manager does not collect... |
| 179 | 0.5915 | • Enable Audit Log Send to Syslog Server in Audit ... |
| 180 | 0.5915 | For more information on the Activity Record struct... |
| 181 | 0.5915 | v10.7 Netwrix Auditor Integration API operates wit... |
| 182 | 0.5914 | Follow the basic steps, required for creation of t... |
| 183 | 0.5908 | Prerequisites Before running the add-on, ensure th... |
| 184 | 0.5905 | Monitoring plan for File Server data source with '... |
| 185 | 0.5905 | If you plan to collect state-in-time data from a S... |
| 186 | 0.5897 | Step 3 – Review events. Table 1: Event log field n... |
| 187 | 0.5895 | Its data is also stored in the Long-Term Archive. ... |
| 188 | 0.5895 | Its data is also stored in the Long-Term Archive. ... |
| 189 | 0.5889 | To reduce the impact on the system drive in large ... |
| 190 | 0.5884 | Compatibility Notice Make sure to check your produ... |
| 191 | 0.5881 | Self-audit allows tracking every change to monitor... |
| 192 | 0.5880 | Each data source has a dedicated item type. Netwri... |
| 193 | 0.5878 | Such instances may have a lot of maintenance plans... |
| 194 | 0.5878 | Fine-tune logon activity monitoring Specify interv... |
| 195 | 0.5877 | You can also launch data collection and Activity S... |
| 196 | 0.5875 | Certain applications can also be added to Exceptio... |
| 197 | 0.5874 | When Filter data by the time interval when the cha... |
| 198 | 0.5872 | Synology Netwrix Auditor relies on native logs for... |
| 199 | 0.5869 | See the Integration Event Log Fields topic for add... |
| 200 | 0.5867 | empty string. For example: ,,\\\\*\\System Volume ... |
| 201 | 0.5865 | Configuring your IT infrastructure may also includ... |
| 202 | 0.5863 | Role-Based Access and Delegation Configure general... |
| 203 | 0.5862 | 1144.. Locate the Syslog parameter and set it to I... |
| 204 | 0.5861 | v10.7 CAUTION: Folder associated with NETWRIX AUDI... |
| 205 | 0.5856 | See the Netwrix Auditor Health Log topic for addit... |
| 206 | 0.5855 | In this case audit data is For example: still bein... |
| 207 | 0.5853 | See the Monitoring Planstopic for additional infor... |
| 208 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 209 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 210 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 211 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 212 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 213 | 0.5852 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 214 | 0.5852 | If you are going to configure Fine Grained Auditin... |
| 215 | 0.5847 | Therefore, successful change and access auditing r... |
| 216 | 0.5844 | See the Group Policy configuration topic for a ddi... |
| 217 | 0.5844 | Splunk is a log management solution that enables s... |
| 218 | 0.5843 | Its convenient interactive search interface enable... |
| 219 | 0.5843 | Syntax: server\instance name Each entry must be a ... |
| 220 | 0.5843 | ◦◦ The following inbound Firewall rules must be en... |
| 221 | 0.5843 | collection at least twice. For example: #*,server,... |
| 222 | 0.5842 | EventStorePath — Netwrix recommends to store these... |
| 223 | 0.5837 | Configuring your IT infrastructure may also includ... |
| 224 | 0.5837 | Configuring your IT infrastructure may also includ... |
| 225 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 226 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 227 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 228 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 229 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 230 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 231 | 0.5834 | Configuring your IT infrastructure may also includ... |
| 232 | 0.5833 | Netwrix.Nutanix.IntegrationService.exe Main add-on... |
| 233 | 0.5833 | Mixed Mode—Default auditing in a newly installed d... |
| 234 | 0.5825 | Audit Database service account An account used by ... |
| 235 | 0.5823 | Monitored Objects Netwrix Auditor tracks changes m... |
| 236 | 0.5822 | Netwrix Auditor ConnectWise Manage Integration Ser... |
| 237 | 0.5821 | Your current audit settings will be checked on eac... |
| 238 | 0.5816 | Complete the following fields: Option Description ... |
| 239 | 0.5816 | Create Monitoring Plan for System Health Log If yo... |
| 240 | 0.5812 | ◦◦ Remember to set the filter to “Data Sourceequal... |
| 241 | 0.5811 | You can copy and archive this folder manually, or ... |
| 242 | 0.5806 | Define what events will be saved to the Long-Term ... |
| 243 | 0.5806 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432NODE\Netwrix Au... |
| 244 | 0.5798 | Step 3 – On the syslog panel, click Add and select... |
| 245 | 0.5798 | Step 13 – Ensure that new GPO settings were applie... |
| 246 | 0.5790 | Installation Overview The Netwrix Auditor Access R... |
| 247 | 0.5788 | Specify IP address of the computer that hosts your... |
| 248 | 0.5788 | Using the Integration API, the add-on sends the ac... |
| 249 | 0.5785 | Note that a CSV file will exist only while the exe... |
| 250 | 0.5785 | Syslog Level Enable Audit Log Send to Syslog Serve... |
| 251 | 0.5782 | The user retrieving data from the Audit Database i... |
| 252 | 0.5782 | v10.7 How It Works Netwrix Auditor add-on for Splu... |
| 253 | 0.5778 | Standard Auditing (trail a uditing Oracle Database... |
| 254 | 0.5777 | Tip for reading the table: For example, on the com... |
| 255 | 0.5775 | Step 3 – The add-on processes these events into Ne... |
| 256 | 0.5771 | To open User Activity report for the selected user... |
| 257 | 0.5770 | On a high level, the add-on works as follows: 11..... |
| 258 | 0.5770 | On a high level, the add-on works as follows: 11..... |
| 259 | 0.5770 | On a high level, the add-on works as follows: 11..... |
| 260 | 0.5769 | By default, Netwrix Auditor will monitor all share... |
| 261 | 0.5765 | Review Auditor Self-Audit Report Also, there is a ... |
| 262 | 0.5764 | Step 1 – Start the Auditor client and navigate to ... |
| 263 | 0.5762 | It will be also selected by default if you are upg... |
| 264 | 0.5762 | https:// Corp.sharepoint.com/* Contains a list of ... |
| 265 | 0.5760 | Click Import, select object type (Web applica tion... |
| 266 | 0.5757 | Monitored Computers For a newly created monitoring... |
| 267 | 0.5748 | Specify a resource name (e.g., Enterprise) to find... |
| 268 | 0.5741 | You can enable Auditor to continually enforce the ... |
| 269 | 0.5741 | The default path is "C:\Program Files (x86)\Netwri... |
| 270 | 0.5735 | Unless specified, data is not associated with a sp... |
| 271 | 0.5734 | Name of the event log where the events will be Fil... |
| 272 | 0.5734 | Protocols and Ports Required v10.7 Detect insider ... |
| 273 | 0.5733 | Audit Database settings are properly configured fo... |
| 274 | 0.5732 | Netwrix Auditor Access Reviews is now configured a... |
| 275 | 0.5732 | On the computer where Auditor Server resides, you ... |
| 276 | 0.5730 | Follow the steps to change trace log location. Ste... |
| 277 | 0.5729 | This method is recommended for evaluation purposes... |
| 278 | 0.5727 | Table 1: Event log field name Filled in with value... |
| 279 | 0.5727 | Table 1: Event log field name Filled in with value... |
| 280 | 0.5721 | computer that hosts Internal error Netwrix Auditor... |
| 281 | 0.5720 | Table 1: Setting Value Max event log size 4 GB Ret... |
| 282 | 0.5710 | v10.7 After that it is strongly recommended to re-... |
| 283 | 0.5709 | The add-on processes Netwrix Auditor-compatible da... |
| 284 | 0.5709 | The add-on processes Netwrix Auditor-compatible da... |
| 285 | 0.5709 | This refers, for example, to Netwrix Auditor for N... |
| 286 | 0.5706 | For both new and existing monitoring plans, you ca... |
| 287 | 0.5704 | The add-on listens to the specified UDP ports and ... |
| 288 | 0.5704 | The add-on listens to the specified UDP ports and ... |
| 289 | 0.5704 | Review a full list of object types Netwrix Auditor... |
| 290 | 0.5703 | By default, Netwrix Auditor only tracks changes to... |
| 291 | 0.5702 | For monitoring Windows Server and User Activity, e... |
| 292 | 0.5701 | Netwrix recommends to store all audit data on the ... |
| 293 | 0.5700 | * @name:514;RSYSLOG_SyslogProt ocol23Format where ... |
| 294 | 0.5699 | Use this report to identify data at high risk and ... |
| 295 | 0.5694 | Start Abandoned Data Source Auditing If you have a... |
| 296 | 0.5693 | Table 1: Option Description Long-Term Archive sett... |
| 297 | 0.5691 | The Services Control Manager opens. Step 2 – Right... |
| 298 | 0.5687 | v10.7 When requested by Netwrix Support, click Dow... |
| 299 | 0.5682 | Leave blank if you use Windows Authentication. SQL... |
| 300 | 0.5682 | Integration Event Log Fields This section describe... |
| 301 | 0.5681 | On a high level, the add-on works as follows: 11..... |
| 302 | 0.5680 | Filter data by the time interval when the change o... |
| 303 | 0.5679 | Databases To store data from the data sources incl... |
| 304 | 0.5678 | Store that file content to a safe location. Step 3... |
| 305 | 0.5677 | • Enable Audit Log Send to Syslog Server in Audit ... |
| 306 | 0.5675 | Option to save and send a report at the same time.... |
| 307 | 0.5670 | To learn more about Netwrix Auditor Core Services,... |
| 308 | 0.5669 | Click View to generate the selected report. Moreov... |
| 309 | 0.5669 | See the Integration API topic for additional infor... |
| 310 | 0.5669 | See the Integration API topic for additional infor... |
| 311 | 0.5667 | See the Configure Scope topic for a dditional info... |
| 312 | 0.5666 | The Working Folder widget—Helps you to estimate th... |
| 313 | 0.5664 | Data is retrieved via Oracle Instant Client applic... |
| 314 | 0.5661 | It is recommended to create a dedicated monitoring... |
| 315 | 0.5655 | Recommendations This section covers the Recommenda... |
| 316 | 0.5655 | Otherwise, Netwrix Auditor may not operate properl... |
| 317 | 0.5655 | If you want to change root directory, do the follo... |
| 318 | 0.5653 | 22.. Navigate to HKEY_LOCAL_MACHINE → SOFTWARE → W... |
| 319 | 0.5649 | NetwrixAuditorPlanItem — Unless specified, data is... |
| 320 | 0.5644 | Step 1 – In the Auditor main screen, select Settin... |
| 321 | 0.5642 | To monitor the mount points targeted at the subfol... |
| 322 | 0.5639 | Click Browse to select from the list of containers... |
| 323 | 0.5639 | Behavior Anomalies Schedule email delivery of a va... |
| 324 | 0.5636 | When the free disk space is less than 3 GB, the Ne... |
| 325 | 0.5636 | This value is filled in automatically. time zone w... |
| 326 | 0.5635 | Table 1: To.. Do.. See how data collection goes on... |
| 327 | 0.5630 | Owner Performs Review — Owners process the review,... |
| 328 | 0.5630 | To reduce the volume of the stored logs and the co... |
| 329 | 0.5627 | Oracle Database has the following options: Databas... |
| 330 | 0.5626 | For example, in the Apply Filters dialog you can s... |
| 331 | 0.5624 | Start Assessment 3. View Results 4. Complete the p... |
| 332 | 0.5624 | See the Integration API topic for additional infor... |
| 333 | 0.5622 | Sensitive Files and Folders by Source Monitoring p... |
| 334 | 0.5619 | If the Event Level check box is cleared, all event... |
| 335 | 0.5617 | Shows all changes across your IT infrastructure, A... |
| 336 | 0.5615 | Data out: Further automate your business processes... |
| 337 | 0.5614 | Review the following for additional information: N... |
| 338 | 0.5612 | v10.7 Using historical data For many data sources,... |
| 339 | 0.5605 | In the Web Interface, navigate Log → Settings and ... |
| 340 | 0.5600 | See the Configure Removable Storage Media for Moni... |
| 341 | 0.5596 | In addition to the restrictions for a monitoring p... |
| 342 | 0.5595 | user activity or state-in-time data. Table 1: Opti... |
| 343 | 0.5592 | v10.7 Report Requirement Netwrix Data Classificati... |
| 344 | 0.5592 | View Reports Create alerts to be notified about su... |
| 345 | 0.5590 | For a Windows File Server, the service is the Netw... |
| 346 | 0.5586 | If you are using SharePoint 2019 or SharePoint Sub... |
| 347 | 0.5584 | For ONTAP 8.3, just check file-ops. To configure l... |
| 348 | 0.5583 | The service will collect and process events from t... |
| 349 | 0.5583 | The service will collect and process events from t... |
| 350 | 0.5583 | v10.7 Access Reviews Netwrix Auditor supports inte... |
| 351 | 0.5582 | Role-Based Access and Delegation Configure general... |
| 352 | 0.5579 | Specify a name of associated monitoring plan in Au... |
| 353 | 0.5579 | Specify a name of associated monitoring plan in Au... |
| 354 | 0.5578 | File Share UNC path to audit logs Path to the file... |
| 355 | 0.5577 | monitoring. For example: SQLPlan,Ent-SQL,Table,gue... |
| 356 | 0.5577 | If you plan to have more than one Netwrix Auditor ... |
| 357 | 0.5576 | This file is shipped separately. Table 1: Where Pr... |
| 358 | 0.5576 | Database Settings At this step, you need to specif... |
| 359 | 0.5572 | Once the script execution completed, you can start... |
| 360 | 0.5572 | If you select to automatically configure audit in ... |
| 361 | 0.5570 | From the Logon Activity source properties. Start A... |
| 362 | 0.5568 | Here you can review a brief description of each co... |
| 363 | 0.5568 | Required role Retrieve all activity records and wr... |
| 364 | 0.5566 | Netwrix Auditor helps you gain complete visibility... |
| 365 | 0.5565 | The installation wizard placed a Netwrix Auditor A... |
| 366 | 0.5565 | To review collected data, you must be assigned the... |
| 367 | 0.5563 | Step 2 – Out of the box, messages from Red Hat Ent... |
| 368 | 0.5561 | See the Prerequisites topic for additional informa... |
| 369 | 0.5561 | See the Prerequisites topic for additional informa... |
| 370 | 0.5561 | See the Prerequisites topic for additional informa... |
| 371 | 0.5559 | Step 1 – An IT administrator configures Netwrix Au... |
| 372 | 0.5558 | Specify a name of associated monitoring plan in Au... |
| 373 | 0.5558 | Specify a name of associated monitoring plan in Au... |
| 374 | 0.5558 | The TCP 9699 port (default Auditor Integr ation AP... |
| 375 | 0.5556 | *) To configure the audit settings manually, refer... |
| 376 | 0.5556 | Specify an object name (e.g., Policy) to find all ... |
| 377 | 0.5556 | In the Performance Monitor snap-in, navigate to Pe... |
| 378 | 0.5553 | SIEM Generic Integration for Event Log Export Netw... |
| 379 | 0.5552 | For monitoring Active Directory, File Servers, Sha... |
| 380 | 0.5550 | Each Activity Record contains the user account, lo... |
| 381 | 0.5549 | A custom account must be granted the same permissi... |
| 382 | 0.5544 | Using the Integration API, the add-on sends the ac... |
| 383 | 0.5544 | See the Audit Configuration Assistant topic for a ... |
| 384 | 0.5544 | Auditor Monitoring Plan settings Auditor Plan Unle... |
| 385 | 0.5544 | Auditor Monitoring Plan settings Auditor Plan Unle... |
| 386 | 0.5542 | Applicable for: File Servers SharePoint SharePoint... |
| 387 | 0.5539 | Netwrix suggests the following execution scenarios... |
| 388 | 0.5538 | See the Permissions for Oracle Database Auditing t... |
| 389 | 0.5536 | The tool is located in the Netwrix Auditor install... |
| 390 | 0.5534 | Table 1: Description Enabling this option on publi... |
| 391 | 0.5533 | Considerations for Oracle Database 11g Starting wi... |
| 392 | 0.5532 | Specify a name of associated monitoring plan in Au... |
| 393 | 0.5532 | It means you reached the end of the Audit Database... |
| 394 | 0.5531 | This includes all Audit databases, Integration API... |
| 395 | 0.5528 | This functionality is currently available for the ... |
| 396 | 0.5525 | Expand the Options section and complete the follow... |
| 397 | 0.5524 | Auditor settings The Audit Database settings shoul... |
| 398 | 0.5523 | Failed Enabling this option on public shares will ... |
| 399 | 0.5519 | Another example: a user creates a new document con... |
| 400 | 0.5517 | Process computer accounts Select this checkbox to ... |
| 401 | 0.5514 | When enabled, Netwrix users can also browse sensit... |
| 402 | 0.5513 | View Reports Create alerts to be notified about su... |
| 403 | 0.5511 | With Netwrix Auditor, AWS audit data is kept for m... |
| 404 | 0.5508 | This option controls how often audit data is expor... |
| 405 | 0.5506 | OutputFolder — This is a mandatory parameter. Choo... |
| 406 | 0.5506 | set csv disable Table 1: Option Description Name/I... |
| 407 | 0.5504 | Enterprise Overview Dashboard Enterprise Overview ... |
| 408 | 0.5504 | Otherwise — if you change the storage location whi... |
| 409 | 0.5502 | Rolebased access system ensures that only relevant... |
| 410 | 0.5501 | Each event contains the user account, action, time... |
| 411 | 0.5501 | Each event contains the user account, action, time... |
| 412 | 0.5495 | SQL Server Objects Review a full list of all objec... |
| 413 | 0.5492 | The anomalies list displays details for each anoma... |
| 414 | 0.5491 | Configuration objects store the information on sit... |
| 415 | 0.5489 | Default is Medium. v10.7 Parameter Description [Ne... |
| 416 | 0.5489 | Also notice that the response action will be launc... |
| 417 | 0.5487 | Major benefits: Gain a high-level view of the data... |
| 418 | 0.5485 | v10.7 Clicking the Go to Notifications button open... |
| 419 | 0.5485 | WriteAgentsToApplicationLog Defines whether to wri... |
| 420 | 0.5485 | See the Custom Search-Based Reports topic for addi... |
| 421 | 0.5483 | Integration Event Log Fields This section describe... |
| 422 | 0.5481 | Step 1 – Install the Netwrix Auditor Access Review... |
| 423 | 0.5480 | See the State–In–Time Reports topic for additional... |
| 424 | 0.5478 | Alternatively, you can limit the auditing scope to... |
| 425 | 0.5475 | Defines a SQL Server instance where your Audit SQL... |
| 426 | 0.5472 | Statement ID — This attribute appears if an object... |
| 427 | 0.5471 | Work with Collected Data Follow the steps to work ... |
| 428 | 0.5470 | Opens the list of the configuration reco mmendatio... |
| 429 | 0.5470 | You will be alerted on events from this event log.... |
| 430 | 0.5466 | Each event contains the user account, action, time... |
| 431 | 0.5466 | Auditor settings • The Audit Database settings sho... |
| 432 | 0.5464 | Select the index that will be used to store the co... |
| 433 | 0.5463 | See Permissions for SharePoint Auditing topic for ... |
| 434 | 0.5463 | Specify a name of associated monitoring plan in Au... |
| 435 | 0.5462 | ArcSight Netwrix Auditor helps you extend auditing... |
| 436 | 0.5459 | The list of available add-ons keeps growing becaus... |
| 437 | 0.5458 | For that, a unified audit trail is required, suppo... |
| 438 | 0.5456 | Starting with version 10.5, Netwrix Auditor provid... |
| 439 | 0.5456 | EventID {Calculated by add-on} -OR0 Depending on G... |
| 440 | 0.5454 | Write audit data to Subscriptions created in the A... |
| 441 | 0.5452 | Step 4 – Splunk starts pulling activity records vi... |
| 442 | 0.5448 | For example, if you grant the data collecting acco... |
| 443 | 0.5444 | Then, do one of the following: • Click Add and pro... |
| 444 | 0.5440 | Step 5 – You can specify any other user group, but... |
| 445 | 0.5439 | v10.7 Option Description By default, Netwrix Audit... |
| 446 | 0.5439 | Do one of the following, depending on your Oracle ... |
| 447 | 0.5439 | Step 1 – Stop the old version of Netwrix Auditor a... |
| 448 | 0.5438 | Follow the steps to troubleshoot data input from N... |
| 449 | 0.5437 | In this case, the product still collects stat-in-t... |
| 450 | 0.5436 | For that purpose, special Netwrix utilities should... |
| 451 | 0.5436 | You can delegate control over a monitoring plan to... |
| 452 | 0.5436 | Main add-on component, responsible for audit data ... |
| 453 | 0.5432 | Specify the account for collecting data Scope Tabl... |
| 454 | 0.5430 | v10.7 Option Description Unless specified, data is... |
| 455 | 0.5428 | Step 1 – Create a monitoring plan in Netwrix Audit... |
| 456 | 0.5427 | Step 4 – Configure audit manually. For 8.3, review... |
| 457 | 0.5426 | For example: #*,server,MicrosoftDNS_S #*,*,StdServ... |
| 458 | 0.5426 | For each item, you can: Specify a custom account f... |
| 459 | 0.5425 | The data collected by Auditor is updated at least ... |
| 460 | 0.5418 | On a high level, the add-on works as follows: 11..... |
| 461 | 0.5417 | When the add-on operates normally there should be ... |
| 462 | 0.5416 | The custom Long-Term Archive service account can b... |
| 463 | 0.5414 | On the target server: The account requires Read sh... |
| 464 | 0.5409 | The product has the following limitations dependin... |
| 465 | 0.5409 | Netwrix Auditor Access Reviews is configured and r... |
| 466 | 0.5408 | The user retrieving data from the Audit Database i... |
| 467 | 0.5406 | Install for User Activity Core Service By default,... |
| 468 | 0.5402 | Netwrix Auditor allows you to assign differen t ac... |
| 469 | 0.5400 | Configure audit settings Do not select the checkbo... |
| 470 | 0.5400 | If the event source for p articular DataSource doe... |
| 471 | 0.5398 | v10.7 Step 2 – Review the results. Successfully ap... |
| 472 | 0.5398 | The product has the following limitations dependin... |
| 473 | 0.5396 | Please consider the following: For the data collec... |
| 474 | 0.5396 | For example, you may need to change logging and re... |
| 475 | 0.5392 | Each Activity Record contains initiator’s account,... |
| 476 | 0.5391 | Where Specify a resource name (e.g., Enterprise) t... |
| 477 | 0.5388 | Internet Information Services (IIS) Auditor suppor... |
| 478 | 0.5387 | Netwrix Auditor ignores changes to system data (e.... |
| 479 | 0.5387 | File Description Syntax Contains a list of data c ... |
| 480 | 0.5384 | Event Log Review the basic registry keys that you ... |
| 481 | 0.5383 | Also, several dedicated databases are created auto... |
| 482 | 0.5381 | Each Activity Record contains the user account, ac... |
| 483 | 0.5379 | See the Predefi ned Reports topic for additional i... |
| 484 | 0.5379 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 485 | 0.5378 | Table 1: On... Ensure that... The Netwrix Auditor ... |
| 486 | 0.5378 | Locate the NetwrixAuditorForWindowsServer object, ... |
| 487 | 0.5377 | Table 1: Database name Description Netwrix_AlertsD... |
| 488 | 0.5377 | NOTE: For the Netwrix Auditor Access Reviews appli... |
| 489 | 0.5376 | Aggregating data into a single audit trail simplif... |
| 490 | 0.5375 | See the Data C ollecting Account topic for additio... |
| 491 | 0.5374 | Execute the command... AUDIT POLICY nwx_actions_po... |
| 492 | 0.5373 | *) Services HKEY_LOCAL_MACHINE\SYSTEM\ControlSet00... |
| 493 | 0.5373 | See the Configure a Response Action for Alert topi... |
| 494 | 0.5369 | Step 2 – Make sure that the Enable event log colle... |
| 495 | 0.5369 | Currently, Netwrix Auditor processes details for t... |
| 496 | 0.5366 | Netwrix suggests the following execution scenarios... |
| 497 | 0.5364 | Table 2: Registry key (REG_DWORD type) Description... |
| 498 | 0.5364 | Netwrix Privilege Secure is ready to use as an acc... |
| 499 | 0.5363 | This option controls how often audit data is expor... |
| 500 | 0.5363 | After you click Connect, the connection with Netwr... |
| 501 | 0.5363 | Follow the steps to install Netwrix Auditor agent ... |
| 502 | 0.5358 | Table 1: Option Setting Log Format "XML" or "EVTX"... |
| 503 | 0.5358 | Example: SQLSRV01\MSSQL2016\|C:\Logs\NA trace logs\... |
| 504 | 0.5349 | After creating a task, wait for the next scheduled... |
| 505 | 0.5349 | After creating a task, wait for the next scheduled... |
| 506 | 0.5348 | • For monitoring Windows Server and User Activity,... |
| 507 | 0.5348 | See the Navigation and Customize Home Screen topic... |
| 508 | 0.5347 | Unless specified, the service runs under the accou... |
| 509 | 0.5346 | Refer to the following documentation to learn more... |
| 510 | 0.5345 | This option controls how often audit data is expor... |
| 511 | 0.5345 | EventID {Calculated by add-on} -ORDepending on Gen... |
| 512 | 0.5343 | If you want to clear Netwrix Auditor Health Log, s... |
| 513 | 0.5343 | In Object Explorer, right-click each Netwrix datab... |
| 514 | 0.5342 | Capacity To examine the repository capacity and da... |
| 515 | 0.5337 | Overexposed Sensitive Data Objects Monitoring plan... |
| 516 | 0.5334 | Refer to the Netwrix Privilege Secure documentatio... |
| 517 | 0.5332 | User account under which data will be w ritten to ... |
| 518 | 0.5332 | For more information on the structure of the Activ... |
| 519 | 0.5330 | Execute... Store audit records to XML audit trail ... |
| 520 | 0.5329 | By default, the Netwrix Auditor Integration event ... |
| 521 | 0.5329 | All Changes by Data Source Shows all changes acros... |
| 522 | 0.5328 | In workgroups The computer where Auditor Server is... |
| 523 | 0.5327 | Monitoring plan name,server name,error text For ex... |
| 524 | 0.5323 | Step 1 – On Netwrix Auditor server, go to the %Net... |
| 525 | 0.5320 | Only the latest snapshot is available for reportin... |
| 526 | 0.5319 | • Location • Name • Ownership Permissions: ◦ Group... |
| 527 | 0.5315 | You can click Browse to select a computer from the... |
| 528 | 0.5314 | CIM might not have data models for some of the act... |
| 529 | 0.5313 | The User Activity Core Service is installed on the... |
| 530 | 0.5311 | Table 1: Netwrix Auditor Per 1 Million Files Per 5... |
| 531 | 0.5310 | Later, you can always create custom report from in... |
| 532 | 0.5310 | For your change management workflow, Netwrix Audit... |
| 533 | 0.5309 | In addition to the restrictions for a monitoring p... |
| 534 | 0.5305 | Only the latest snapshot is available for reportin... |
| 535 | 0.5304 | v10.7 After environment variable substitution, the... |
| 536 | 0.5302 | For a full list of the rights and permissions, and... |
| 537 | 0.5300 | Step 8 – Complete the Event Filter dialog. In the ... |
| 538 | 0.5299 | The body is empty. The posted file exceeds support... |
| 539 | 0.5298 | If you want Netwrix Auditor to audit custom regist... |
| 540 | 0.5295 | For example, if you are using the add-on that impo... |
| 541 | 0.5295 | Unless specified, the service runs under the accou... |
| 542 | 0.5293 | See theNetwork Devices topic for additional inform... |
| 543 | 0.5293 | Use this report to investigate how permissions are... |
| 544 | 0.5289 | The Netwrix Auditor Integration API provides acces... |
| 545 | 0.5284 | • The Audit Database settings are configured in Au... |
| 546 | 0.5280 | Implemented as a PowerShell script, this add-on fa... |
| 547 | 0.5280 | Implemented as a PowerShell script, this add-on fa... |
| 548 | 0.5279 | The Audit Database settings are configured in Audi... |
| 549 | 0.5277 | For example, if you grant the data collecting acco... |
| 550 | 0.5276 | Some settings in Auditor are configure d incorrect... |
| 551 | 0.5274 | For example: #*,server,MicrosoftDNS_Server #*,*,St... |
| 552 | 0.5274 | Other Activity Summaries generated and delivered b... |
| 553 | 0.5273 | Implemented as a service, this add-on facilitates ... |
| 554 | 0.5271 | Monitoring plan name,server name, resource path Wi... |
| 555 | 0.5270 | Oracle administrator prepares a dedicated service ... |
| 556 | 0.5269 | Step 2 – Click Manage. v10.7 Step 3 – Select the d... |
| 557 | 0.5262 | Step 3 – Add script parameters. The console will l... |
| 558 | 0.5262 | To configure Core Audit for Qumulo file servers 11... |
| 559 | 0.5262 | Configure Video Recordings Playback Settings Video... |
| 560 | 0.5262 | For example: Add arguments (optional) file "C:\Add... |
| 561 | 0.5261 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 562 | 0.5260 | Major benefits: Gain a high-level view of the data... |
| 563 | 0.5260 | The syntax greatly depends on the tool you use. Sc... |
| 564 | 0.5258 | Table 2: Entry in EventData Activity Record field ... |
| 565 | 0.5257 | The user retrieving data from the Audit The Audito... |
| 566 | 0.5257 | The user retrieving data from the Audit The Audito... |
| 567 | 0.5256 | By default, it is set to "C:\ProgramData\Netwrix A... |
| 568 | 0.5255 | For a full list of the rights and permissions, and... |
| 569 | 0.5255 | It is recommended to create a dedicated monitoring... |
| 570 | 0.5255 | See the Adjust DHCP Server Operational Log Setting... |
| 571 | 0.5253 | For other dist ributions, deployment of rsyslog pa... |
| 572 | 0.5253 | This data is not associated with any monitoring pl... |
| 573 | 0.5251 | It is installed together with Netwrix Auditor clie... |
| 574 | 0.5251 | Step 10 – Assign a less-privileged role to this ac... |
| 575 | 0.5247 | The Resource name in this case is where the activi... |
| 576 | 0.5246 | • Netwrix Auditor license has expired. • Internal ... |
| 577 | 0.5244 | Logon Activity Monitoring Scope You can fine-tune ... |
| 578 | 0.5242 | In busy environments and during activity peaks, wo... |
| 579 | 0.5240 | For that purpose, you can use a specially designed... |
| 580 | 0.5239 | If you want to run searches and generate reports, ... |
| 581 | 0.5234 | The Read share permission on the audited shared fo... |
| 582 | 0.5233 | Then, do one of the following: Audit SharePoint re... |
| 583 | 0.5226 | Each event contains the user account, action, time... |
| 584 | 0.5225 | If not set, <not set> is reported. Total objects c... |
| 585 | 0.5225 | For a full list of audit settings required for Net... |
| 586 | 0.5224 | Netwrix Auditor shows only the top 2,000 anomalies... |
| 587 | 0.5223 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 588 | 0.5221 | The user retrieving data from the Audit Database i... |
| 589 | 0.5221 | The user retrieving data from the Audit Database i... |
| 590 | 0.5221 | The user retrieving data from the Audit Database i... |
| 591 | 0.5221 | The user retrieving data from the Audit Database i... |
| 592 | 0.5221 | The user retrieving data from the Audit Database i... |
| 593 | 0.5221 | The user retrieving data from the Audit Database i... |
| 594 | 0.5221 | The user retrieving data from the Audit Database i... |
| 595 | 0.5221 | Aggregating data into a single audit trail simplif... |
| 596 | 0.5219 | Step 1 – On the computer where Auditor Server resi... |
| 597 | 0.5217 | Netwrix suggests the following execution scenarios... |
| 598 | 0.5215 | v10.7 Time zone — time zone where Netwrix Auditor ... |
| 599 | 0.5215 | RECOMMENDED: The notification should include: Why ... |
| 600 | 0.5215 | You can configure these settings automatically usi... |
| 601 | 0.5213 | The Audit Database settings are configured in Audi... |
| 602 | 0.5209 | Sub-elements: Name and ID. If you provide a monito... |
| 603 | 0.5209 | Subscriptions can be uploaded either to a file sha... |
| 604 | 0.5208 | Configure Netwrix Auditor to store daily snapshots... |
| 605 | 0.5207 | It instructs Netwrix Auditor to Not in group Domai... |
| 606 | 0.5207 | Second monitoring plan for collecting data from Or... |
| 607 | 0.5206 | Consider the following: To store data from the dat... |
| 608 | 0.5205 | Implemented as a service, this add-on facilitates ... |
| 609 | 0.5201 | When an update is available, a user is immediately... |
| 610 | 0.5199 | Registry key (REG_DWORD type) Description / Value ... |
| 611 | 0.5199 | For input Activity Records, the data source is aut... |
| 612 | 0.5196 | NetwrixAuditorPlan – Unless specified, data is wri... |
| 613 | 0.5188 | Do not select the checkbox if you want to configur... |
| 614 | 0.5188 | The downloaded logs have the debug logging informa... |
| 615 | 0.5182 | The dashboard includes the following widgets: The ... |
| 616 | 0.5175 | Monitored Object Types, Actions, and Attributes Ne... |
| 617 | 0.5173 | The summary section shows: Role name Role type — F... |
| 618 | 0.5173 | For example: *,server,MicrosoftDNS_Se rver *,*,Std... |
| 619 | 0.5172 | * @name:514;RSYSLOG_SyslogProtocol23Fo rmat where ... |
| 620 | 0.5171 | SharePoint Monitoring Scope You can fine-tune Netw... |
| 621 | 0.5169 | The chart shows how many events with different sev... |
| 622 | 0.5167 | History Allows for on-demand subscription delivery... |
| 623 | 0.5167 | The best practice is to review user profile after ... |
| 624 | 0.5166 | Tip for reading the table: For example, on the com... |
| 625 | 0.5164 | Write Activity Records Schema The Activity Records... |
| 626 | 0.5161 | Title Default: [Netwrix Auditor] %AlertName% That ... |
| 627 | 0.5160 | NOTE: Right after setting up the integration the d... |
| 628 | 0.5156 | 1166.. Start Netwrix Auditor. 1177.. Navigate to y... |
| 629 | 0.5156 | Activity Records are -NetwrixAuditorUserName expor... |
| 630 | 0.5155 | See the Access Reviews topic for a dditional infor... |
| 631 | 0.5155 | • For monitoring Windows Server and User Activity,... |
| 632 | 0.5154 | First, you should decide on the objects and action... |
| 633 | 0.5153 | This command is required to create a shared folder... |
| 634 | 0.5153 | Required role The user must be assigned the Global... |
| 635 | 0.5152 | You can specify any other user group, but in this ... |
| 636 | 0.5151 | Make sure to provide correct path to the script fi... |
| 637 | 0.5149 | v10.7 Option Description Refer to Configure Scope ... |
| 638 | 0.5145 | All filters are applied using AND logic. By defaul... |
| 639 | 0.5143 | If, for some reason, installation has failed, you ... |
| 640 | 0.5142 | You can configure your IT Infrastructure for monit... |
| 641 | 0.5140 | Later, you can always run it from the Start menu o... |
| 642 | 0.5138 | EventData is filled in with data from the Activity... |
| 643 | 0.5138 | See the State–In–Time Reports topic for a dditiona... |
| 644 | 0.5137 | To find out a log’s name, navigate to Start > Wind... |
| 645 | 0.5134 | <NetwrixAuditorPassword>NetwrixIsCoo l </NetwrixAu... |
| 646 | 0.5132 | The Netwrix Auditor One or more A ctivity 500 Inte... |
| 647 | 0.5132 | The output Activity Records may contain the follow... |
| 648 | 0.5131 | The body is empty. The posted Error Large file exc... |
| 649 | 0.5131 | A Security Officer wants to monitor a file share, ... |
| 650 | 0.5128 | The details for each role include its name, type, ... |
| 651 | 0.5126 | Time zone — time zone where Netwrix Auditor server... |
| 652 | 0.5125 | Netwrix suggests the following execution scenarios... |
| 653 | 0.5125 | Active Directory State-In-Time Reports Examine the... |
| 654 | 0.5123 | Step 4 – On the Select Installation Type step, you... |
| 655 | 0.5122 | For example: Router# configure terminal 33.. Enabl... |
| 656 | 0.5122 | The add-on creates a special Windows event log nam... |
| 657 | 0.5121 | Service which helps Netwrix Auditor SQL Server Bro... |
| 658 | 0.5121 | It may include the data source type (e.g. Exchange... |
| 659 | 0.5120 | Prior to the Netwrix Auditor for SharePoint Core S... |
| 660 | 0.5117 | v10.7 Configure Audit Settings for CIFS File Share... |
| 661 | 0.5113 | 503 Service Unavailable Error The Netwrix Auditor ... |
| 662 | 0.5112 | Step 2 – Run the installation package. Step 3 – Fo... |
| 663 | 0.5112 | Once the required steps are done, the recommendati... |
| 664 | 0.5112 | For example: https://siteColl* v10.7 File Descript... |
| 665 | 0.5110 | The add-on creates a special Windows event log nam... |
| 666 | 0.5109 | You cannot select event categories if you use Clus... |
| 667 | 0.5107 | NOTE: Event records with more than 30,000 characte... |
| 668 | 0.5106 | * @name:514;RSYSLOG_SyslogProtocol23Fo rmat where ... |
| 669 | 0.5106 | The Audit Database settings are configured in the ... |
| 670 | 0.5105 | For that purpose, you can use a specially designed... |
| 671 | 0.5103 | Step 1 – Navigate to the Search page of the add-on... |
| 672 | 0.5101 | C:\Add-ons\Netwrix_Auditor_Event_Log_ Export_Add-o... |
| 673 | 0.5099 | To find out a log’s name, navigate to Start > Wind... |
| 674 | 0.5097 | Recipients will be notified by email, and response... |
| 675 | 0.5096 | Local Admin on the Netwrix Auditor server. The com... |
| 676 | 0.5094 | Contains a list of AD paths to be For example, you... |
| 677 | 0.5093 | v10.7 Option Description Read Access Configure Net... |
| 678 | 0.5092 | ◦◦ The following Windows Firewall inbound rules mu... |
| 679 | 0.5089 | Ensure your computer is listed as Receiver (e.g., ... |
| 680 | 0.5089 | Object type Action What Details Successful Logon N... |
| 681 | 0.5087 | Execute the following commands: # configure Table ... |
| 682 | 0.5087 | Step 5 – Review sensitive data. Netwrix suggests t... |
| 683 | 0.5087 | Actions reported by Auditor vary depending on the ... |
| 684 | 0.5084 | VMware Monitoring Scope You can fine-tune Netwrix ... |
| 685 | 0.5081 | You can configure Netwrix Auditor to use an existi... |
| 686 | 0.5074 | Currently, auditing is available for SMB shares on... |
| 687 | 0.5072 | You will get a list of activity records with detai... |
| 688 | 0.5067 | It may include the data source type (e.g. Exchange... |
| 689 | 0.5066 | Refer to the following sections for detailed infor... |
| 690 | 0.5066 | You can also configure and receive alerts on the e... |
| 691 | 0.5062 | Alert Handler: Receives the IDs of the alert and a... |
| 692 | 0.5061 | The Resource name in this case is where the activi... |
| 693 | 0.5060 | It might cause performance issues on the medium an... |
| 694 | 0.5059 | They will help to ensure imported data consistency... |
| 695 | 0.5059 | Data Collecting Account This is a service account ... |
| 696 | 0.5058 | Major benefits: Table 1: Pre-installation procedur... |
| 697 | 0.5057 | To check or configure these settings, navigate to ... |
| 698 | 0.5056 | Default prefix is NA, for example:NA Windows Serve... |
| 699 | 0.5055 | Set the Max Size of Entire Index to match the expe... |
| 700 | 0.5055 | C:\Add-ons\Netwrix_Auditor_Addon_for_ LogRhythm.ps... |
| 701 | 0.5054 | Manage auditing and security log. See the Configur... |
| 702 | 0.5052 | The console will look similar to the following: Wi... |
| 703 | 0.5052 | The add-on creates a special Windows event log nam... |
| 704 | 0.5050 | See the Netwrix Privilege Secure topic for additio... |
| 705 | 0.5049 | Assessment results are reported on the screen and ... |
| 706 | 0.5048 | Remember, the Access Reviews version must align to... |
| 707 | 0.5048 | See the Integrations topic for additional informat... |
| 708 | 0.5047 | Activity Records are exported to a local event log... |
| 709 | 0.5040 | Core Service Deploy Netwrix Auditor for SharePoint... |
| 710 | 0.5039 | See the Prerequisites and Audit Database topics fo... |
| 711 | 0.5037 | The account must be a member of the BUILTIN\Admini... |
| 712 | 0.5036 | • The Netwrix Auditor Archive Service is unreachab... |
| 713 | 0.5036 | Auditor Server • Integration API and Audit Databas... |
| 714 | 0.5035 | When prompted, accept the license agreement and sp... |
| 715 | 0.5032 | All filters are applied using AND logic. See the C... |
| 716 | 0.5032 | Make sure that you have the Access Reviews license... |
| 717 | 0.5030 | In Netwrix Auditor settings, go to the Integration... |
| 718 | 0.5028 | The Netwrix Auditor Archive Service is busy or unr... |
| 719 | 0.5027 | If so, consider that current user account (logged ... |
| 720 | 0.5026 | Specify notification delivery time Modify the Even... |
| 721 | 0.5025 | See the Health Status Dashboard topic for addition... |
| 722 | 0.5025 | Netwrix has built a ready-to-use add-on that autom... |
| 723 | 0.5025 | Aggregating data into a single audit trail simplif... |
| 724 | 0.5025 | By default, the LongTerm Archive (repository) and ... |
| 725 | 0.5023 | Step 3 – On the General tab, specify a task name, ... |
| 726 | 0.5022 | Splunk Enterprise Splunk Administrator or any othe... |
| 727 | 0.5020 | Domain Audit Policy Settings Effective domain cont... |
| 728 | 0.5019 | To be able to watch video files captured by Netwri... |
| 729 | 0.5018 | These requirements will add up to the requirements... |
| 730 | 0.5018 | Refer to the Netwrix Privilege Secure documentatio... |
| 731 | 0.5013 | Navigate to Start → Netwrix Auditor. 22.. Log into... |
| 732 | 0.5013 | The Microsoft-IIS-Configuration/Operational log mu... |
| 733 | 0.5010 | Table 1: Option Description Read Access Audit Shar... |
| 734 | 0.5009 | In this case audit data is still being collected. ... |
| 735 | 0.5009 | Maximum number of Audit Records ARsNumberAtTime th... |
| 736 | 0.5008 | Step 1 – Upgrade Netwrix Auditor Server OS to the ... |
| 737 | 0.5008 | the fi le path. Alternatively, the command line wi... |
| 738 | 0.5002 | Working with Mount Points You can specify a mount ... |
| 739 | 0.5001 | Ensure that... The user retrieving data from the A... |
| 740 | 0.5000 | For more information on additional deployment opti... |
| 741 | 0.4999 | Step 2 – Download the add-on package and copy it t... |
| 742 | 0.4998 | Step 2 – Click Save. Step 3 – Reproduce the issue ... |
| 743 | 0.4996 | See the User Management topic in the Netwrix Data ... |
| 744 | 0.4994 | 135 Retrieve Exchange Netwrix Auditor and dynamic ... |
| 745 | 0.4992 | For your convenience, the account specified will b... |
| 746 | 0.4989 | Typically, data collected from the certain data so... |
| 747 | 0.4986 | If you have not already started using Netwrix Audi... |
| 748 | 0.4985 | If you provide a monitoring plan name for input Ac... |
| 749 | 0.4984 | 22.. Access the global configuration mode. For exa... |
| 750 | 0.4983 | Activity Records are exported to a local event log... |
| 751 | 0.4983 | See the Objects topic for additional information. ... |
| 752 | 0.4982 | v10.7 Reported data The report has a summary secti... |
| 753 | 0.4982 | For the account, worksta tion, application name fi... |
| 754 | 0.4982 | If you want to restart monitoring these objects, r... |
| 755 | 0.4981 | Reason: unexpected shutdown or system failure Comp... |
| 756 | 0.4978 | By deafult, only events with processed details wil... |
| 757 | 0.4977 | If your deployment planning reveals that SQL Serve... |
| 758 | 0.4977 | ObjectType Yes nvarchar 255 An type of affected ob... |
| 759 | 0.4975 | v10.7 Review the following for additional informat... |
| 760 | 0.4973 | However, consider the following: If a mount point ... |
| 761 | 0.4973 | Schedule email delivery of a variety of reports or... |
| 762 | 0.4972 | Step 1 – Configure Data Collecting Account, as des... |
| 763 | 0.4971 | There you can use the UI controls to run the varie... |
| 764 | 0.4969 | The email looks like shown below: v10.7 v10.7 The ... |
| 765 | 0.4969 | Netwrix Auditor Alerts to Event Log Add-on On... E... |
| 766 | 0.4968 | Auditor skips all automated deactivation actions f... |
| 767 | 0.4967 | For a full list of audit s ettings required to col... |
| 768 | 0.4966 | Reports with Video Netwrix Auditor can be configur... |
| 769 | 0.4963 | v10.7 In this case, you need to provide the userna... |
| 770 | 0.4962 | The following considerations and limitations refer... |
| 771 | 0.4962 | Object path —path to the monitored object, as form... |
| 772 | 0.4960 | Password Provide the password for the selected acc... |
| 773 | 0.4959 | Table 2: On... Ensure that... The Auditor Server s... |
| 774 | 0.4958 | Refer to the Permissions for Active Directory A ud... |
| 775 | 0.4956 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 776 | 0.4954 | Set the value to "730" (which equals 2 years). Act... |
| 777 | 0.4953 | An account used by Netwrix Auditor to upload data ... |
| 778 | 0.4953 | To report on other snapshots, make sure they are a... |
| 779 | 0.4953 | Step 3 – Add script parameters. The console will l... |
| 780 | 0.4952 | How It Works On a high level, the add-on works as ... |
| 781 | 0.4952 | The Audit Database settings are configured in Audi... |
| 782 | 0.4952 | The Audit Database settings are configured in Audi... |
| 783 | 0.4952 | The Audit Database settings are configured in Audi... |
| 784 | 0.4952 | The Audit Database settings are configured in Audi... |
| 785 | 0.4952 | The Audit Database settings are configured in Audi... |
| 786 | 0.4952 | The Audit Database settings are configured in Audi... |
| 787 | 0.4952 | The Audit Database settings are configured in Audi... |
| 788 | 0.4952 | The Audit Database settings are configured in Audi... |
| 789 | 0.4952 | Step 3 – Create a shared folder named netwrix_audi... |
| 790 | 0.4950 | The user writing data to the Audit Database is gra... |
| 791 | 0.4950 | Activity Records are retrieved according to the ac... |
| 792 | 0.4949 | These Email Templates (multiple files) Located in ... |
| 793 | 0.4948 | The Audit Database settings are configured in Audi... |
| 794 | 0.4948 | The Audit Database settings are configured in Audi... |
| 795 | 0.4946 | The account must be assigned the Contributor role ... |
| 796 | 0.4944 | If you select a plan name in the addon, make sure ... |
| 797 | 0.4943 | Also, this folder includes a report on Auditor sel... |
| 798 | 0.4942 | Step 3 – In the General tab, set the Startup type ... |
| 799 | 0.4941 | Refer to the Netwrix Privilege Secure documentatio... |
| 800 | 0.4940 | General Considerations and Known Issues During the... |
| 801 | 0.4935 | ImportAllEvents — By deafult, only events with pro... |
| 802 | 0.4935 | During the Netwrix Auditor for SharePoint Core Ser... |
| 803 | 0.4934 | Manually – Native audit settings must be adjusted ... |
| 804 | 0.4933 | You can configure Netwrix Auditor Access Reviews i... |
| 805 | 0.4932 | See the Netwrix Privilege Secure topic for additio... |
| 806 | 0.4932 | In this case, data will be written to a database l... |
| 807 | 0.4931 | Format Select IETF. Facility Netwrix recommends us... |
| 808 | 0.4930 | See the View Reports topic for additional informat... |
| 809 | 0.4929 | Specify a name of associated monitoring plan in Au... |
| 810 | 0.4928 | Refer to Create Alerts for Event Log for Table 1: ... |
| 811 | 0.4927 | Add the following line: auth.*;authpriv. * @name:5... |
| 812 | 0.4926 | If you select a plan name in the addon, make sure ... |
| 813 | 0.4925 | For example: hostname(config)# logging enable 44..... |
| 814 | 0.4925 | For that, click Notification settings, then follow... |
| 815 | 0.4924 | Scope Specify restriction filters to narrow your m... |
| 816 | 0.4924 | The MonitoringPlan element contains sub-elements s... |
| 817 | 0.4924 | Click Manage to review the full list of accounts a... |
| 818 | 0.4923 | If you plan, however, not to use Netwrix Auditor b... |
| 819 | 0.4923 | Step 1 – On the computer where AuditorServer resid... |
| 820 | 0.4918 | If any conflicts are detected with your current au... |
| 821 | 0.4916 | Navigate to this directory and locate Netwrix_Audi... |
| 822 | 0.4915 | Step 3 – In the Remote Registry Properties dialog ... |
| 823 | 0.4912 | The credentials are case sensitive. A custom accou... |
| 824 | 0.4911 | Unless specified, data is written to Netwrix_Audit... |
| 825 | 0.4910 | See the User Activity topic for additional informa... |
| 826 | 0.4909 | For example: Add arguments (optional) file "C:\Add... |
| 827 | 0.4908 | You can use the Search field, or apply a filter to... |
| 828 | 0.4905 | See the Permissions for Oracle Database Auditing t... |
| 829 | 0.4904 | Policy Subnode Policy Name Audit Events Audit Secu... |
| 830 | 0.4903 | Auditor can monitor for operations with MS Teams e... |
| 831 | 0.4903 | Special Considerations The originally released Net... |
| 832 | 0.4902 | To store data to the database, leave this check bo... |
| 833 | 0.4901 | An IT administrator configures the Integration API... |
| 834 | 0.4901 | The product updates the latest snapshot on the reg... |
| 835 | 0.4897 | See the Use Group Managed Service Account (gMSA) t... |
| 836 | 0.4896 | This database is always created but is involved in... |
| 837 | 0.4893 | Activity Records are exported to a local event log... |
| 838 | 0.4892 | If you select a plan name in the addon, make sure ... |
| 839 | 0.4892 | If you select a plan name in the addon, make sure ... |
| 840 | 0.4889 | By default, Auditor allows generating reports and ... |
| 841 | 0.4887 | Specify an item name. Auditor Plan Item Make sure ... |
| 842 | 0.4887 | You may need to limit their scope to a specific mo... |
| 843 | 0.4886 | This email lists VMware infrastructure changes and... |
| 844 | 0.4884 | The issues occur because the product applies data ... |
| 845 | 0.4884 | Use Netwrix Privilege Secure as a Data Collecting ... |
| 846 | 0.4884 | v10.7 The user writing data to the Audit Database ... |
| 847 | 0.4883 | Specify the account that you want to define this p... |
| 848 | 0.4883 | To use the account currently logged in, leave this... |
| 849 | 0.4881 | You will get a list of activity records with detai... |
| 850 | 0.4880 | These events are structured and ready for integrat... |
| 851 | 0.4880 | See the File Servers topic for additional informat... |
| 852 | 0.4879 | See the Netwrix Privilege Secure topic for additio... |
| 853 | 0.4877 | NOTE: You might want to apply a filter to narrow d... |
| 854 | 0.4877 | Changes Audit SharePoint farm configuration change... |
| 855 | 0.4876 | In this case, you need to provide the username of ... |
| 856 | 0.4875 | User/password – Provide a username and password fo... |
| 857 | 0.4875 | Alternatively, you can grant the Global administra... |
| 858 | 0.4874 | Netwrix Auditor Integration API is enabled by defa... |
| 859 | 0.4874 | Auditor Plan Item Make sure to create a dedicated ... |
| 860 | 0.4874 | Auditor Plan Item Make sure to create a dedicated ... |
| 861 | 0.4873 | RECOMMENDED: click Send Test Email. The system wil... |
| 862 | 0.4872 | Visit Netwrix Corporation Software License Agreeme... |
| 863 | 0.4871 | Step 3 – On the Triggers tab, click New and define... |
| 864 | 0.4871 | If you select a plan name in the addon, make sure ... |
| 865 | 0.4871 | Step 3 – On the Triggers tab, click New and define... |
| 866 | 0.4871 | Step 3 – On the Triggers tab, click New and define... |
| 867 | 0.4871 | Step 3 – On the Triggers tab, click New and define... |
| 868 | 0.4870 | NOTE: Perform this procedure only if you enabled t... |
| 869 | 0.4869 | Although you can always use the add-on as is, but ... |
| 870 | 0.4869 | Besides notifying you on who changed what, when an... |
| 871 | 0.4869 | For Microsoft Entra ID Auditing To collect audit d... |
| 872 | 0.4869 | Credential-based is the default option. Refer to t... |
| 873 | 0.4869 | Credential-based is the default option. Refer to t... |
| 874 | 0.4869 | Credential-based is the default option. Refer to t... |
| 875 | 0.4868 | See the Considerations for Oracle Database 11g top... |
| 876 | 0.4865 | Unless specified, data is written to the Netwrix_ ... |
| 877 | 0.4864 | Activity Records are exported to a local event log... |
| 878 | 0.4863 | Monitor SQL Server configuration changes Always en... |
| 879 | 0.4863 | Migrate to Unified Audit Starting with 10.5 versio... |
| 880 | 0.4862 | For detailed information, review the Planning the ... |
| 881 | 0.4862 | All you have to do is provide connection details a... |
| 882 | 0.4862 | All you have to do is provide connection details a... |
| 883 | 0.4862 | Each activity record contains the Who-What-When-Wh... |
| 884 | 0.4861 | Table 1: Option Description General Monitor this d... |
| 885 | 0.4861 | Also, remember to perform the following steps for ... |
| 886 | 0.4859 | See the Audit Database topic for additional inform... |
| 887 | 0.4858 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 888 | 0.4858 | Specify the account for collecting data Starting w... |
| 889 | 0.4857 | And make sure that the UDP port is used for sendin... |
| 890 | 0.4856 | Follow the steps to use Netwrix Auditor Access Rev... |
| 891 | 0.4856 | Table 1: Option Description You can review a sampl... |
| 892 | 0.4855 | Always enabled, as SQL Server configuration change... |
| 893 | 0.4854 | The designated service team performs data analysis... |
| 894 | 0.4852 | Troubleshooting Log files of Netwrix Account Locko... |
| 895 | 0.4851 | and dynamic range: TCP Domain controllers Server g... |
| 896 | 0.4851 | Aggregating data into a single audit trail simplif... |
| 897 | 0.4851 | Aggregating data into a single audit trail simplif... |
| 898 | 0.4851 | Aggregating data into a single audit trail simplif... |
| 899 | 0.4849 | v10.7 6. Using the Integration API, the add-on sen... |
| 900 | 0.4847 | To learn more about modern authentication, refer t... |
| 901 | 0.4847 | Thus, it is recommended that instead of retrievein... |
| 902 | 0.4847 | Windows File Server. Table 1: Component Version Ne... |
| 903 | 0.4844 | ShortTermFolder ShortTerm Specify path to the shor... |
| 904 | 0.4843 | • The alert response action settings in Auditor Se... |
| 905 | 0.4842 | If you have configured alerting in Netwrix Auditor... |
| 906 | 0.4841 | You can add it in NDC console > Settings > Users. ... |
| 907 | 0.4841 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Solarwinds_L... |
| 908 | 0.4840 | Table 2: Configure custom location of session reco... |
| 909 | 0.4839 | The add-on uploads audit trails to ArcSight Logger... |
| 910 | 0.4839 | Step 9 – Click OK to save the changes and close th... |
| 911 | 0.4837 | v10.7 Configuration parameters to specify in setti... |
| 912 | 0.4837 | Prior to the Netwrix Auditor for SharePoint Core S... |
| 913 | 0.4837 | To retrieve activity logs on Copilot interactions,... |
| 914 | 0.4833 | In the Event Log field enter "Netwrix Non-Owner Ma... |
| 915 | 0.4833 | You will get a list of activity records with detai... |
| 916 | 0.4833 | ): No special configuration required to audit RMAN... |
| 917 | 0.4832 | See the Audit Database topic for additional inform... |
| 918 | 0.4831 | Currently, auditing is available for SMB shares on... |
| 919 | 0.4828 | It should be a running Netwrix Syslog service or a... |
| 920 | 0.4826 | In this case, Netwrix Auditor Server will retrieve... |
| 921 | 0.4823 | How the Copilot Add-on Works On a high level, the ... |
| 922 | 0.4821 | See the Microsoft Turn auditing on or off article ... |
| 923 | 0.4820 | Netwrix Auditor 53 UDP DNS Server DNS Client Serve... |
| 924 | 0.4817 | The account must be a member of the local Administ... |
| 925 | 0.4817 | The user retrieving data from the Audit Database i... |
| 926 | 0.4815 | The account must be assigned the Global reviewer r... |
| 927 | 0.4815 | You will get a list of activity records with detai... |
| 928 | 0.4815 | If not set, <not set> is reported. Object path —pa... |
| 929 | 0.4813 | For ONTAP 8.3, just check file-ops. v10.7 33.. Cre... |
| 930 | 0.4813 | Implemented as a service, this add-on facilitates ... |
| 931 | 0.4810 | Usage example Database administrators in the Corp ... |
| 932 | 0.4809 | If you cannot log into Netwrix Auditor with your W... |
| 933 | 0.4808 | For details, see Manage historical snapshots optio... |
| 934 | 0.4807 | Remember, for Exchange auditing, do the following:... |
| 935 | 0.4806 | Make sure the account that runs the task has all n... |
| 936 | 0.4806 | Make sure the account that runs the task has all n... |
| 937 | 0.4806 | Make sure the account that runs the task has all n... |
| 938 | 0.4804 | The status is 200 OK and the body is empty. HTTP/1... |
| 939 | 0.4803 | See the About Netwrix Auditor topic for additional... |
| 940 | 0.4803 | * — these actions are reported for SharePoint Onli... |
| 941 | 0.4803 | Security Event Log Settings Security event log set... |
| 942 | 0.4803 | See the State–In–Time Reports topic for additional... |
| 943 | 0.4801 | On a high level, the add-on works as follows: 11..... |
| 944 | 0.4799 | Registry key (REG_DWORD type) Description / Value ... |
| 945 | 0.4799 | They list all activity that occurred across the au... |
| 946 | 0.4798 | SQL Server Instance As a Auditor administrator I w... |
| 947 | 0.4796 | For detailed information, refer to the Microsoft a... |
| 948 | 0.4796 | Controls ticket resolution and corrective measures... |
| 949 | 0.4795 | Follow the steps to exclude data from the Windows ... |
| 950 | 0.4794 | What Specify an object name (e.g., Policy) to find... |
| 951 | 0.4794 | You can configure your IT Infrastructure for monit... |
| 952 | 0.4793 | To report on other snapshots, make sure they are a... |
| 953 | 0.4793 | In the Web Interface, navigate to Manage → Log Set... |
| 954 | 0.4792 | Consider the following: Step 1 – Configure Securit... |
| 955 | 0.4792 | Attachments larger than 50MB will be uploaded to \... |
| 956 | 0.4791 | To... Execute... Netwrix.ITSM.AlertsUploaderTool.e... |
| 957 | 0.4791 | EventData is filled in with data from the Activity... |
| 958 | 0.4788 | Step 2 – Select Audit module and select 5 - Notice... |
| 959 | 0.4787 | Advanced permissions: ◦ Create files / write data ... |
| 960 | 0.4787 | Synology Auditor supports monitoring the following... |
| 961 | 0.4786 | See the Prerequisites and Audit Database topics fo... |
| 962 | 0.4786 | See the Prerequisites and Audit Database topics fo... |
| 963 | 0.4786 | Tip for reading the table: For example, on the com... |
| 964 | 0.4785 | If both components are installed on the same machi... |
| 965 | 0.4785 | Run a search request to /netwrix/api/v1/activity_r... |
| 966 | 0.4784 | The Audit Database settings are configured in Audi... |
| 967 | 0.4783 | The filters may vary slightly depending on the aud... |
| 968 | 0.4782 | Users open Auditor Client to work with collected d... |
| 969 | 0.4781 | Make sure to grant sufficient permissions on folde... |
| 970 | 0.4780 | StartsWith EndsWith Table 1: Filter Description Su... |
| 971 | 0.4779 | For exclusive: all Windows logs events will be exc... |
| 972 | 0.4778 | If you need to be alerted on specific events in yo... |
| 973 | 0.4776 | Starting with version 10.7, you can implement the ... |
| 974 | 0.4776 | To process all anomalies In the Actions section, s... |
| 975 | 0.4775 | ServiceNow Incident Management The add-on works in... |
| 976 | 0.4773 | C:\Add-ons\Netwrix_Auditor_Addon_for_Intel_Securit... |
| 977 | 0.4773 | Otherwise, enabling this option may lead to issues... |
| 978 | 0.4772 | The Activity Record structure is described in the ... |
| 979 | 0.4772 | The Activity Record structure is described in the ... |
| 980 | 0.4771 | Step 2 – Download the Add-On. Step 3 – Configure P... |
| 981 | 0.4771 | For example: http:// sharepointsrv:3333/ omitscsto... |
| 982 | 0.4770 | Table 1: Data source Components • Microsoft Entra ... |
| 983 | 0.4768 | monitoring plan name,server name,class name,proper... |
| 984 | 0.4766 | Table 1: File Description Syntax OmitErrorsList.tx... |
| 985 | 0.4765 | Specify the account for collecting data Select the... |
| 986 | 0.4765 | If AD FS Admin logging is disabled, you should ena... |
| 987 | 0.4764 | These steps must be taken each time a new audit da... |
| 988 | 0.4759 | Follow the steps to exclude data from the Active D... |
| 989 | 0.4759 | Specify path to the short-term archive (Netwrix Au... |
| 990 | 0.4757 | The TCP 9699 port (default Auditor Integr ation AP... |
| 991 | 0.4756 | Ensure that... Step 5 – Open the / etc/ rsyslog.co... |
| 992 | 0.4755 | In the same domain No restrictions In two-way trus... |
| 993 | 0.4751 | See the Netwrix Privilege Secure topic for additio... |
| 994 | 0.4751 | DataCollection UDP port for receiving incoming Sys... |
| 995 | 0.4750 | XML: <Item> <Name>Item name</Name> — </Item> JSON:... |
| 996 | 0.4748 | In this Table 1: Parameter Default value Descripti... |
| 997 | 0.4747 | See the Use Netwrix Privilege Secure as a Data Col... |
| 998 | 0.4746 | The add-ons comes with a special set of alerts dev... |
| 999 | 0.4745 | POST Activity Records activity_records/ Write Acti... |
| 1000 | 0.4745 | 50-100 concurrent sessions per terminal server. Ne... |
| 1001 | 0.4745 | To store data from the data sources included in th... |
| 1002 | 0.4744 | State-in-time configuration snapshots are also use... |
| 1003 | 0.4743 | Are there any files likely to contain credentials,... |
| 1004 | 0.4743 | The console will look similar to the following: Wi... |
| 1005 | 0.4743 | All Netwrix product announcements have moved to th... |
| 1006 | 0.4742 | Step 4 – Navigate to the Send data for Access Revi... |
| 1007 | 0.4742 | DataCollectionPassword Specify user account passwo... |
| 1008 | 0.4741 | The user writing data to the Audit Database is gra... |
| 1009 | 0.4741 | The user writing data to the Audit Database is gra... |
| 1010 | 0.4741 | Auditor time format. By default, set NetwrixAudito... |
| 1011 | 0.4739 | The system will send a test message to the s pecif... |
| 1012 | 0.4739 | In this case, data will be written to a database A... |
| 1013 | 0.4739 | In this case, data will be written to a database A... |
| 1014 | 0.4738 | Now you can augment SIEM with data collected by Au... |
| 1015 | 0.4738 | NOTE: Netwrix recommends using different credentia... |
| 1016 | 0.4737 | Create Alerts for Non-Owner Mailbox Access Events ... |
| 1017 | 0.4737 | v10.7 Option Description Password Provide the pass... |
| 1018 | 0.4737 | On Ubuntu 16: Navigate to the /etc/rsyslog.d/50def... |
| 1019 | 0.4737 | On Ubuntu 16: Navigate to the /etc/rsyslog.d/50def... |
| 1020 | 0.4736 | Dell Isilon Dell VNX VNXe NetApp Windows File Shar... |
| 1021 | 0.4736 | In this case, the credentials will not be stored b... |
| 1022 | 0.4736 | In this case, the credentials will not be stored b... |
| 1023 | 0.4736 | Password Provide the password for the selected acc... |
| 1024 | 0.4734 | Execute... ALTER SYSTEM SET audit_trail=XML SCOPE=... |
| 1025 | 0.4734 | Download the Add-On 1. Download the distribution p... |
| 1026 | 0.4730 | Event parameter descriptions can also be added. In... |
| 1027 | 0.4730 | Oracle Database Monitoring Scope You can fine-tune... |
| 1028 | 0.4730 | Pay attention to the "Data categories" column in s... |
| 1029 | 0.4729 | Click Add to add a new principal. You can also sel... |
| 1030 | 0.4726 | Step 5 – In case some computers are still present ... |
| 1031 | 0.4726 | See the Netwrix Privilege Secure topic for additio... |
| 1032 | 0.4726 | Then you will provide this account in the monitori... |
| 1033 | 0.4726 | Microsoft Exchange Server 2010 is no longer suppor... |
| 1034 | 0.4724 | You can configure your IT Infrastructure for monit... |
| 1035 | 0.4723 | Navigate to Start → Run and type "regedit". Regist... |
| 1036 | 0.4721 | Manually – Native audit settings must be adjusted ... |
| 1037 | 0.4720 | SQL Server Reporting Services Netwrix Auditor util... |
| 1038 | 0.4717 | Step 2 – Add the following line: auth.*;authpriv. ... |
| 1039 | 0.4716 | For removable storages, the When value reports act... |
| 1040 | 0.4713 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 1041 | 0.4713 | The account must be assigned the Contributor role ... |
| 1042 | 0.4712 | Configure Auditor to monitor SharePoint Online rea... |
| 1043 | 0.4712 | Activity Records are exported to a local event log... |
| 1044 | 0.4711 | Click Accept. Navigate to Log → Categories. Select... |
| 1045 | 0.4711 | Health Status Dashboard Schedule Health Summary em... |
| 1046 | 0.4710 | Review the event IDs available in the Netwrix Non-... |
| 1047 | 0.4710 | The user account for running the service and conne... |
| 1048 | 0.4710 | v10.7 Prepare Netwrix Auditor for Data Processing ... |
| 1049 | 0.4709 | Step 4 – The selected account is displayed in the ... |
| 1050 | 0.4708 | Execute... Upload alert set shipped with the addon... |
| 1051 | 0.4707 | Integration API and Audit Database settings are co... |
| 1052 | 0.4706 | Use this path—UNC path to the file share located o... |
| 1053 | 0.4705 | v10.7 Option Description To import snapshots, you ... |
| 1054 | 0.4705 | When prompted to configure the Audit database sett... |
| 1055 | 0.4704 | Table 1: Object type Actions Event ID Cisco ASA de... |
| 1056 | 0.4704 | Do not change this setting unless advised accordin... |
| 1057 | 0.4704 | Step 9 – Ensure that new GPO settings applied on a... |
| 1058 | 0.4703 | You can add any elements (a dashboard, report, ale... |
| 1059 | 0.4700 | Step 2 – By default, the security log is set to ov... |
| 1060 | 0.4696 | Sufficient access rights in Netwrix Auditor, which... |
| 1061 | 0.4696 | NetwrixAuditorUserPassword Current user credential... |
| 1062 | 0.4696 | To create the Event Trace Session object: logman i... |
| 1063 | 0.4694 | Step 1 – Log in to the Nasuni Management Console a... |
| 1064 | 0.4693 | search results. For example to exclude the adminCo... |
| 1065 | 0.4692 | You can configure your IT Infrastructure for monit... |
| 1066 | 0.4692 | Step 8 – Apply the following settings to your Perm... |
| 1067 | 0.4691 | See File-Based Repository for Long-Term Archive fo... |
| 1068 | 0.4690 | Netwrix Privilege Secure is ready to use as an acc... |
| 1069 | 0.4689 | Lines that start with the # sign are treated as co... |
| 1070 | 0.4685 | Continuation Mark POST /netwrix/api/v1/ activity_r... |
| 1071 | 0.4685 | These events are structured and ready for integrat... |
| 1072 | 0.4683 | The tool will be launched in a new window. See the... |
| 1073 | 0.4683 | The Auditor Server side User account under which d... |
| 1074 | 0.4683 | Note that events exceeding 4000 symbols are trimme... |
| 1075 | 0.4682 | What column. For example, if you only want to moni... |
| 1076 | 0.4682 | You can put a wildcard (*) in the omitpathlist.txt... |
| 1077 | 0.4681 | v10.7 Notify owners of their responsibilities. See... |
| 1078 | 0.4680 | NOTE: Netwrix recommends using different credentia... |
| 1079 | 0.4680 | NOTE: Netwrix recommends using different credentia... |
| 1080 | 0.4680 | Step 6 – Specify a plan name. Settings for Data Co... |
| 1081 | 0.4678 | timeout Defines the Audit Database connection time... |
| 1082 | 0.4678 | Step 2 – Fine-tune data source settings, if necess... |
| 1083 | 0.4677 | Follow the steps to exclude data from the Active D... |
| 1084 | 0.4677 | If you select a plan name in the addon, make sure ... |
| 1085 | 0.4677 | Windows File Share Nutanix SMB Shares File Servers... |
| 1086 | 0.4676 | DBName By default, the database responsible for Ne... |
| 1087 | 0.4675 | For NetApp Clustered Data ONTAP 8 and ONTAP 9, onl... |
| 1088 | 0.4675 | For Managed Service Providers: Netwrix Auditor Net... |
| 1089 | 0.4673 | NetwrixAuditorPassword Current user credentials Pr... |
| 1090 | 0.4670 | Server instance, use * for all servers Audit data,... |
| 1091 | 0.4670 | User account under which data will be w ritten Aud... |
| 1092 | 0.4669 | Step 2 – Click Search. NOTE: You might want to app... |
| 1093 | 0.4669 | See the File-Based Repository for LongTerm Archive... |
| 1094 | 0.4669 | See the Compliance Reports topic for additional in... |
| 1095 | 0.4667 | Subscribe to the Health Summary Email The Health S... |
| 1096 | 0.4666 | v10.7 Attribute 1: Member of - equals \| Value: Dom... |
| 1097 | 0.4666 | Manually – Native audit settings must be adjusted ... |
| 1098 | 0.4664 | If you select a plan name in the add-on, make sure... |
| 1099 | 0.4663 | See the following topics for additional informatio... |
| 1100 | 0.4662 | The Audit object access policy must be set to "Suc... |
| 1101 | 0.4661 | Audit data will still be collected. Monitoring pla... |
| 1102 | 0.4661 | The section below explains how to create, disable ... |
| 1103 | 0.4661 | Step 1 – In main Netwrix Auditor menu, select Moni... |
| 1104 | 0.4659 | To use the account currently logged in, leave this... |
| 1105 | 0.4657 | You can select Everyone (or another u ser-defined ... |
| 1106 | 0.4657 | Then click OK to confirm. The Database service acc... |
| 1107 | 0.4655 | These operations can be performed in any of the fo... |
| 1108 | 0.4655 | Otherwise, the add-on will not be able to write da... |
| 1109 | 0.4655 | Then, s/he does not want the product to NetApp mon... |
| 1110 | 0.4654 | Alternatively, you can install Auditor client usin... |
| 1111 | 0.4654 | See Configure Integration API and Audit Database. ... |
| 1112 | 0.4653 | or generating reports, or I am sure that some data... |
| 1113 | 0.4653 | Delete Netwrix Auditor for Active Directory Compre... |
| 1114 | 0.4652 | Unpack the ZIP archive to a folder of your choice;... |
| 1115 | 0.4648 | The user account for running the service and conne... |
| 1116 | 0.4648 | Task read attempt No — Message located in \Tasks T... |
| 1117 | 0.4648 | Time zone — time zone where Netwrix Auditor server... |
| 1118 | 0.4646 | Alternatively, a fter NetwrixAuditorUserName Curre... |
| 1119 | 0.4646 | Step 3 – After configuring all filters, click Add ... |
| 1120 | 0.4645 | To do that, copy and edit the file with processing... |
| 1121 | 0.4645 | Users open Auditor Client to work with collected d... |
| 1122 | 0.4643 | Careful review of successful and failed logons fro... |
| 1123 | 0.4641 | Considerations for Netwrix Privilege Secure Integr... |
| 1124 | 0.4641 | Table 1: Element Mandatory Datatype Description Da... |
| 1125 | 0.4641 | Possible values: • Empty—Check Netwrix Auditor cer... |
| 1126 | 0.4641 | Activity Records are exported to -NetwrixAuditorUs... |
| 1127 | 0.4640 | v10.7 Endpoint Use to export data from the Audit D... |
| 1128 | 0.4640 | Alternatively, you can grant it the Global adminis... |
| 1129 | 0.4637 | Example: For: PROD-SQL-01-AG1 SQL Server Monitorin... |
| 1130 | 0.4637 | See the How to Migrate Netwrix Auditor Working Fol... |
| 1131 | 0.4636 | Step 3 – Configure the following audit policies. T... |
| 1132 | 0.4636 | Default retention period is 120 months. Audit data... |
| 1133 | 0.4636 | Table 1: Scenario Example The add-on runs on the A... |
| 1134 | 0.4636 | Configure alerts triggered by specific events in t... |
| 1135 | 0.4635 | On a high level, the add-on works as follows: The ... |
| 1136 | 0.4635 | In this case, the credentials will not be stored b... |
| 1137 | 0.4634 | v10.7 Prepare for Using Netwrix Auditor Integratio... |
| 1138 | 0.4630 | Follow the steps to add an account to the Netwrix ... |
| 1139 | 0.4628 | Click Add Recipient and provide email summaries ad... |
| 1140 | 0.4626 | Starting with version 10.7, you can implement the ... |
| 1141 | 0.4625 | NOTE: Access Reviews is a separately licensed prod... |
| 1142 | 0.4625 | You may also want to apply audit settings via GPO ... |
| 1143 | 0.4622 | Configure Default SQL Server Settings On the Setti... |
| 1144 | 0.4621 | If the monitoring plan name in the <NetwrixAuditor... |
| 1145 | 0.4619 | %ProgramData%\Netwrix Auditor\AuditCore\AuditA v10... |
| 1146 | 0.4618 | See the File Servers topic for additional informat... |
| 1147 | 0.4618 | The CEF log file will be created in the destinatio... |
| 1148 | 0.4617 | Device class: ◦◦ CD and DVD ◦◦ Floppy Drives Remov... |
| 1149 | 0.4617 | At the end of each run, the script creates the Net... |
| 1150 | 0.4616 | Registry key (REG_DWORD type) Description / Value ... |
| 1151 | 0.4615 | Activity Records are exported to -NetwrixAuditorUs... |
| 1152 | 0.4614 | Table 1: Parameter Default value Description The a... |
| 1153 | 0.4614 | However, if you want to use specific settings for ... |
| 1154 | 0.4613 | See the Create a New Plan topic for additional inf... |
| 1155 | 0.4613 | Each Activity Record contains the user account, ac... |
| 1156 | 0.4612 | Selected mailbox 11.. On the computer where the mo... |
| 1157 | 0.4612 | Starting with version 10.7, you can implement the ... |
| 1158 | 0.4612 | Starting with version 10.7, you can implement the ... |
| 1159 | 0.4611 | For example, if you are going to audit Internet In... |
| 1160 | 0.4609 | See the Netwrix Privilege Secure topic for v10.7 a... |
| 1161 | 0.4607 | In Netwrix Auditor 9.0, Netwrix has updated API sc... |
| 1162 | 0.4605 | If you select to automatically configure audit in ... |
| 1163 | 0.4604 | Table 1: Version Edition SQl Server 2022 • Standar... |
| 1164 | 0.4603 | Review a full list of object types and attributes ... |
| 1165 | 0.4602 | Older tickets requests are cleared. Step 3 – Resta... |
| 1166 | 0.4601 | Effective grant —the effective set of permissions ... |
| 1167 | 0.4600 | Specify Active Directory credentials Provide the n... |
| 1168 | 0.4600 | Specify Active Directory credentials Provide the n... |
| 1169 | 0.4598 | See the Netwrix Privilege Secure topic for additio... |
| 1170 | 0.4596 | NETWRIX AUDITOR is unable to work in a workgroup. ... |
| 1171 | 0.4595 | You can configure your IT Infrastructure for monit... |
| 1172 | 0.4593 | Activity Records are exported to NetwrixAuditorUse... |
| 1173 | 0.4591 | Collected via MS Graph on endpoint /devices All se... |
| 1174 | 0.4591 | Port Protocol Source Target Purpose Monitored netw... |
| 1175 | 0.4590 | Click Browse to select a folder on the computer th... |
| 1176 | 0.4590 | Otherwise, the program will automatically search f... |
| 1177 | 0.4590 | At the end of each run, the script creates the Net... |
| 1178 | 0.4589 | Activity Records are exported to a local event log... |
| 1179 | 0.4587 | The second option is Resource-based. To use this o... |
| 1180 | 0.4586 | To audit successful changes on NetApp 8.x or earli... |
| 1181 | 0.4584 | In this case, data will be written to a database l... |
| 1182 | 0.4584 | In this case, data will be written to a database l... |
| 1183 | 0.4584 | In this case, data will be written to a database l... |
| 1184 | 0.4584 | See the Audit Database topic for additional inform... |
| 1185 | 0.4583 | To review data sources and items included in each ... |
| 1186 | 0.4583 | At the end of each run, the script creates the Net... |
| 1187 | 0.4583 | At the end of each run, the script creates the Net... |
| 1188 | 0.4582 | When finished, click OK. Table 1: File Description... |
| 1189 | 0.4582 | For example: -file "C:\Addons\Netwrix_Auditor_Add-... |
| 1190 | 0.4580 | Table 1: On... Ensure that... The Auditor Server s... |
| 1191 | 0.4579 | C:\Addons\Netwrix_Auditor_Activity_Records_ to_Eve... |
| 1192 | 0.4578 | v10.7 Automatically through a monitoring plan – Th... |
| 1193 | 0.4577 | In addition to the restrictions for a monitoring p... |
| 1194 | 0.4577 | In the Manage historical snapshots section, click ... |
| 1195 | 0.4577 | You can enable Auditor to continually enforce the ... |
| 1196 | 0.4574 | Depending on the network traffic compression setti... |
| 1197 | 0.4574 | If any conflicts are detected with your current se... |
| 1198 | 0.4572 | You can use a single account to collect audit data... |
| 1199 | 0.4572 | v10.7 Step 3 – In the Windows Firewall with Advanc... |
| 1200 | 0.4571 | To configure removable storage media monitoring re... |
| 1201 | 0.4569 | See Configure Integration API and Audit Database. ... |
| 1202 | 0.4569 | Change and Activity Reports Change and activity re... |
| 1203 | 0.4568 | The account used to run Netwrix Account Lockout Ex... |
| 1204 | 0.4568 | Once all the Activity Records are retrieved, you w... |
| 1205 | 0.4568 | Possible values: NetwrixAuditorCertificateThumbpr ... |
| 1206 | 0.4568 | See the Netwrix Privilege Secure topic for additio... |
| 1207 | 0.4567 | v10.7 Review the following for additional informat... |
| 1208 | 0.4567 | Activity Records are exported to a local event log... |
| 1209 | 0.4566 | To check it, navigate to Settings → Integrations t... |
| 1210 | 0.4565 | Step 1 – In the audited SharePoint farm, navigate ... |
| 1211 | 0.4565 | When prompted, accept the license agreement and sp... |
| 1212 | 0.4564 | In the same domain No restrictions In two-way trus... |
| 1213 | 0.4562 | If not selected, then your current Windows cr eden... |
| 1214 | 0.4559 | Step 5 – Open the / etc/ rsyslog.conf file. Step 6... |
| 1215 | 0.4558 | v10.7 The second option is Resource-based. To use ... |
| 1216 | 0.4558 | In the Netwrix Auditor API location field provide ... |
| 1217 | 0.4558 | You can enable Auditor to continually enforce the ... |
| 1218 | 0.4558 | Step 1 – On the audited server, open the Local Sec... |
| 1219 | 0.4557 | It is recommended to create a dedicated monitoring... |
| 1220 | 0.4555 | Make sure the Windows File Servers you want to mon... |
| 1221 | 0.4554 | The CIM contains a number of standard data models ... |
| 1222 | 0.4553 | Step 4 – Run the shell script by executing the fol... |
| 1223 | 0.4553 | These group Managed Service Accounts should meet t... |
| 1224 | 0.4553 | The DetailList element is Table 1: Format Schema d... |
| 1225 | 0.4553 | On Red Hat Enterprise Linux 7, perform the followi... |
| 1226 | 0.4552 | Item—name of the SQL Server instance monitored wit... |
| 1227 | 0.4552 | Item—name of the SQL Server instance monitored wit... |
| 1228 | 0.4551 | Seamless upgrade to Netwrix Auditor 10.7 is suppor... |
| 1229 | 0.4548 | Allow outbound connections from the dynamic (1024 ... |
| 1230 | 0.4548 | In this case audit data is still being collected. ... |
| 1231 | 0.4547 | For that, follow the procedure below. If you enabl... |
| 1232 | 0.4547 | Configure Logging for CTERA Edge Filer Prior to st... |
| 1233 | 0.4544 | This ensures that dedicated specialists have acces... |
| 1234 | 0.4544 | NetwrixAuditorPlan — When specified, overrides the... |
| 1235 | 0.4543 | NOTE: The account must be assigned the Contributor... |
| 1236 | 0.4541 | To use this option, you need to provide the Activi... |
| 1237 | 0.4541 | To use this option, you need to provide the Activi... |
| 1238 | 0.4539 | For example: hostname(config)# logging trap 5 77..... |
| 1239 | 0.4539 | Make sure to select this parameter if you plan to ... |
| 1240 | 0.4539 | Microsoft 365 Microsoft 365 audit configuration wi... |
| 1241 | 0.4539 | Parameter Default value Description General parame... |
| 1242 | 0.4538 | v10.7 Option Description Events collected from any... |
| 1243 | 0.4538 | It is recommended to select Adjust audit settings ... |
| 1244 | 0.4537 | Registry key (REG_DWORD type) Description / Value ... |
| 1245 | 0.4537 | See Permissions for Table 1: Option Description Sh... |
| 1246 | 0.4536 | Using the Integration API, the add-on sends the ac... |
| 1247 | 0.4535 | You can also create a subscription to any report y... |
| 1248 | 0.4532 | Click the Details link to examine the product log.... |
| 1249 | 0.4531 | v10.7 Delete Netwrix Auditor Mailbox Access Core S... |
| 1250 | 0.4530 | Scenario A: Advanced audit policies Enable the fol... |
| 1251 | 0.4530 | Also, Netwrix prepares add-ons—sample scripts—to h... |
| 1252 | 0.4527 | type,what,property name Table 1: File Description ... |
| 1253 | 0.4526 | Table 1: File name Description ta-netwrix-auditor-... |
| 1254 | 0.4526 | Otherwise, the add-on will not be able to write da... |
| 1255 | 0.4525 | Audit SharePoint Online configuration and content ... |
| 1256 | 0.4524 | This will facilitate operations tracking and possi... |
| 1257 | 0.4524 | Configuration Tile This tile helps you set up and ... |
| 1258 | 0.4522 | If you plan to enable this option, make sure the a... |
| 1259 | 0.4520 | Step 2 – In the right pane, select the Items tab. ... |
| 1260 | 0.4520 | The credentials are case sensitive. A custom accou... |
| 1261 | 0.4518 | v10.7 Object type Details Description Administrato... |
| 1262 | 0.4518 | By default, set to zero offset. MonitoringPlan — U... |
| 1263 | 0.4514 | v10.7 Database name Description Intended for integ... |
| 1264 | 0.4514 | If not yet existing on the specified SQL server in... |
| 1265 | 0.4513 | Possible values: Empty—Check Netwrix Auditor certi... |
| 1266 | 0.4511 | Navigate to Reports and select one of the followin... |
| 1267 | 0.4511 | This option controls how often audit data is expor... |
| 1268 | 0.4510 | The TCP 9699 port (default Integration API port) i... |
| 1269 | 0.4509 | v10.7 44.. Click Search next to Login Name and spe... |
| 1270 | 0.4506 | (Unlike that, without network traffic compression ... |
| 1271 | 0.4505 | Required permissions • Unless specified, the Netwr... |
| 1272 | 0.4505 | Make sure to create a dedicated item in Auditor in... |
| 1273 | 0.4504 | It will deploy and enable the Netwrix Auditor Conn... |
| 1274 | 0.4503 | Before installing Auditor, make sure that the Wind... |
| 1275 | 0.4503 | Retention period for the video files can be adjust... |
| 1276 | 0.4501 | For v10.7 Windows Server NOTE: Prior to configurin... |
| 1277 | 0.4499 | For that, you should estimate the required capacit... |
| 1278 | 0.4499 | See the Network Traffic Compression topic for addi... |
| 1279 | 0.4498 | Plan for the file servers and shares you want to a... |
| 1280 | 0.4497 | When auditing file servers, changes to both access... |
| 1281 | 0.4496 | It also generates summary reports that can be deli... |
| 1282 | 0.4496 | This topic focuses on the CEF Export SIEM solution... |
| 1283 | 0.4496 | The alert response action settings in Auditor Serv... |
| 1284 | 0.4495 | If you select to automatically configure audit in ... |
| 1285 | 0.4495 | <Address>172.28.4.15</Address> <Address>172.28.3.1... |
| 1286 | 0.4494 | timeout Defines the Audit Database connection time... |
| 1287 | 0.4493 | Provide the new data input parameters: Name of the... |
| 1288 | 0.4490 | The Insertion Strings tab Specify this parameter i... |
| 1289 | 0.4488 | For the purpose of the Access Reviewsapplication, ... |
| 1290 | 0.4487 | Netwrix.ITSM.AlertsUploaderTool.exe / List Review ... |
| 1291 | 0.4486 | Companies leverage these policies to empower users... |
| 1292 | 0.4482 | .Net Framework 4.7.2 and above is installed. The c... |
| 1293 | 0.4481 | Step 4 – In a separate Advanced Security Settings ... |
| 1294 | 0.4481 | Implemented as a PowerShell script, this add-on au... |
| 1295 | 0.4479 | By default, it will contain the following detailed... |
| 1296 | 0.4478 | To collect event data from the domain, this servic... |
| 1297 | 0.4478 | Since Netwrix Auditor shows only the top 2,000 ano... |
| 1298 | 0.4477 | Auditor Server host by its DNS or NetBIOS name. Th... |
| 1299 | 0.4472 | If you select to automatically configure audit in ... |
| 1300 | 0.4472 | .NET 4.8 must be installed. See the following topi... |
| 1301 | 0.4472 | Step 9 – Ensure that new GPO settings applied on a... |
| 1302 | 0.4471 | Step 2 – Mount this file system on a mount point, ... |
| 1303 | 0.4471 | If a domain account is used, make sure to use the ... |
| 1304 | 0.4470 | When prompted to configure the Audit database sett... |
| 1305 | 0.4469 | By default, the Collect data for self-audit checkb... |
| 1306 | 0.4469 | It instructs Netwrix Auditor to In group Domain\Ad... |
| 1307 | 0.4467 | If you select to automatically configure audit in ... |
| 1308 | 0.4465 | See the Fine-tune Monitoring Scope for a dditional... |
| 1309 | 0.4465 | You have already identified the intruder and now y... |
| 1310 | 0.4463 | Perform the following steps to integrate alerts wi... |
| 1311 | 0.4463 | VMware groups. The product collects data from vCen... |
| 1312 | 0.4462 | Make sure Do not overwrite events (Clear logs manu... |
| 1313 | 0.4461 | v10.7 The add-on operates as a syslog listener for... |
| 1314 | 0.4461 | Installation of Netwrix Auditor and SQL Server on ... |
| 1315 | 0.4460 | ◦◦ On the Netwrix Auditor host system/server: The ... |
| 1316 | 0.4459 | You can use this file to track possible duplicates... |
| 1317 | 0.4458 | Add more ticket parameters or update values if nec... |
| 1318 | 0.4457 | With that automated flow, you can use Splunk Enter... |
| 1319 | 0.4455 | In the Services snap-in, locate the Microsoft Exch... |
| 1320 | 0.4454 | Follow the steps to exclude data from the Group Po... |
| 1321 | 0.4454 | For all Windows server versions Run the auditpol u... |
| 1322 | 0.4454 | Depending on your auditing requirements, you may n... |
| 1323 | 0.4452 | You can also configure and receive alerts on the e... |
| 1324 | 0.4451 | If you accept, Netwrix collects statistical inform... |
| 1325 | 0.4451 | Logon Activity Ports Review a full list of protoco... |
| 1326 | 0.4450 | It should be a third-party Syslog forward service ... |
| 1327 | 0.4450 | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Netwrix Au... |
| 1328 | 0.4449 | AD FS Servers Data Collection For Active Directory... |
| 1329 | 0.4448 | Note that these actions are system, not user-effec... |
| 1330 | 0.4446 | On the computer where Auditor Server is installed:... |
| 1331 | 0.4445 | Uninstall Compression and Core Services Perform th... |
| 1332 | 0.4444 | An originating worksta tion from which the change ... |
| 1333 | 0.4443 | v10.7 Parameter Default value Description The add-... |
| 1334 | 0.4441 | Download the product installation package. Open th... |
| 1335 | 0.4441 | v10.7 Before you start creating a monitoring plan ... |
| 1336 | 0.4441 | Password Provide the password for the selected acc... |
| 1337 | 0.4438 | Select which of your Active Directory environment ... |
| 1338 | 0.4438 | This information will help you to take corrective ... |
| 1339 | 0.4437 | As the interactive search in the Netwrix Auditor c... |
| 1340 | 0.4437 | format=json} {&count=Number} — POST https://{host:... |
| 1341 | 0.4437 | Ensure that... ◦ Command line preview looks like t... |
| 1342 | 0.4437 | Specifies the length of ti meout before events fro... |
| 1343 | 0.4436 | Please note that all audit types should be enabled... |
| 1344 | 0.4435 | File Description Syntax Name This file defines a l... |
| 1345 | 0.4434 | You can perform this procedure on any of the Excha... |
| 1346 | 0.4434 | In the Add Syslog Server dialog, find the IP addre... |
| 1347 | 0.4434 | See State–In–Time Reports for more information. CA... |
| 1348 | 0.4433 | Collect data for state-in-time reports When auditi... |
| 1349 | 0.4432 | As soon as the item is added, to the monitoring pl... |
| 1350 | 0.4431 | v10.7 This feature is supported only for SQL Serve... |
| 1351 | 0.4429 | See the Data C ollecting Account topic for additio... |
| 1352 | 0.4424 | See the Monitoring Scope topic for additional info... |
| 1353 | 0.4424 | Click OK to save the settings and close the dialog... |
| 1354 | 0.4422 | You are looking for changes that occurred more tha... |
| 1355 | 0.4421 | /netwrix/api/v1/ GET — activity_records/enum Retri... |
| 1356 | 0.4418 | Collect data for state-in-time reports Configure A... |
| 1357 | 0.4418 | MonitoringPlan — Unless specified, data is written... |
| 1358 | 0.4418 | The add-on works in collaboration with Netwrix Aud... |
| 1359 | 0.4418 | The add-on works in collaboration with Netwrix Aud... |
| 1360 | 0.4418 | Step 1 – Turn the switch to On if you want a respo... |
| 1361 | 0.4416 | Compatibility Notice Make sure to check your produ... |
| 1362 | 0.4416 | File Servers State-In-Time Reports This section co... |
| 1363 | 0.4415 | State — as set in the database properties at snaps... |
| 1364 | 0.4414 | NetwrixAuditorDateTimeFormat yyyy-MM-ddTHH:mm:ssZ ... |
| 1365 | 0.4414 | v10.7 Step 7 – Click Run and close the window. The... |
| 1366 | 0.4413 | The resource name can Where Yes nvarchar 255 be a ... |
| 1367 | 0.4413 | Make sure that the folder is accessible from compu... |
| 1368 | 0.4411 | For example: APIAdminTool.exe api https certificat... |
| 1369 | 0.4411 | AWS CloudTrail is an internal tracking service tha... |
| 1370 | 0.4408 | NOTE: Make sure that your Netwrix Auditor Integrat... |
| 1371 | 0.4407 | Step 4 – Provide retention settings and access cre... |
| 1372 | 0.4405 | Enabling this option on public shares will result ... |
| 1373 | 0.4403 | Opens the listed Auditor report. See the Custom Se... |
| 1374 | 0.4402 | Max length: 255. • Contains (default) • DoesNotCon... |
| 1375 | 0.4401 | Select this checkbox if you want to verify securit... |
| 1376 | 0.4400 | Allow outbound connections from the dynamic (1024 ... |
| 1377 | 0.4399 | See the Adjust Security Event Log Size and Retenti... |
| 1378 | 0.4398 | See the Netwrix Privilege Secure topic for additio... |
| 1379 | 0.4398 | Available for report and search subscriptions only... |
| 1380 | 0.4398 | When specified, overrides the NetwrixAuditorPlanIt... |
| 1381 | 0.4394 | NOTE: Before installing Netwrix Auditor, make sure... |
| 1382 | 0.4393 | Add the requirements for 5 million files which are... |
| 1383 | 0.4390 | See the Launch Audit Configuration Assistant secti... |
| 1384 | 0.4387 | You can use a single account to collect audit data... |
| 1385 | 0.4386 | Make sure this account has sufficient rights to co... |
| 1386 | 0.4386 | Open Administrative Tools > Services, right-click ... |
| 1387 | 0.4386 | Make sure the volume you specified is mounted on S... |
| 1388 | 0.4385 | So, you should register an Microsoft Entra ID app ... |
| 1389 | 0.4384 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1390 | 0.4384 | This file is located in the same folder as SyslogS... |
| 1391 | 0.4382 | Pay attention to the "Data categories" column in s... |
| 1392 | 0.4382 | Supported versions are SQL Server 2012 and later (... |
| 1393 | 0.4382 | The account must be assigned the Global reviewer r... |
| 1394 | 0.4382 | Object Access Audit Detailed File Share "Failure" ... |
| 1395 | 0.4380 | Ensure that... .NET Framework 4.5 or later is inst... |
| 1396 | 0.4379 | ◦◦ To use this option for NetApp Clustered Data ON... |
| 1397 | 0.4377 | In this case audit data is still being collected. ... |
| 1398 | 0.4377 | • .NET 4.5 or later must be installed. Execution p... |
| 1399 | 0.4377 | Step 3 – Configure the following audit policies. P... |
| 1400 | 0.4376 | Permissions Permissions are needed to the Netwrix ... |
| 1401 | 0.4375 | Review and Manage Subscriptions On the main Netwri... |
| 1402 | 0.4373 | Depending on the execution scenario you choose, yo... |
| 1403 | 0.4372 | Application permissions are consented by an admini... |
| 1404 | 0.4372 | Auditor Administrators Global administrator Audito... |
| 1405 | 0.4371 | Name For example: *OU=C,OU=B,OU=A* v10.7 NOTE: Tip... |
| 1406 | 0.4371 | Alternatively, you can grant the Global administra... |
| 1407 | 0.4370 | NetwrixAuditorDateTimeFormat yyyy-MM-ddTHH:mm:ssZ ... |
| 1408 | 0.4368 | You can configure your IT Infrastructure for monit... |
| 1409 | 0.4368 | C:\Addons\Netwrix_Auditor_CEF_Export_Addon. ps1 -O... |
| 1410 | 0.4368 | Subscriptions can be uploaded either to a file sha... |
| 1411 | 0.4367 | The name cannot be changed. ◦ <path to the EventTr... |
| 1412 | 0.4367 | The 'When' column shows the time when the syslog m... |
| 1413 | 0.4367 | Step 3 – Add script parameters. The console will l... |
| 1414 | 0.4366 | This capability is supported for the following rep... |
| 1415 | 0.4363 | <Address>172.28.3.18</Address> The add-on runs on ... |
| 1416 | 0.4363 | If the utility is installed on the remote machine ... |
| 1417 | 0.4361 | By default, SQL Server trace logs will be stored i... |
| 1418 | 0.4361 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1419 | 0.4361 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1420 | 0.4360 | property name and property value are optional, but... |
| 1421 | 0.4358 | If you want to audit Dell VNX/VNXe, select Adjust ... |
| 1422 | 0.4357 | See the Table 1: On... Ensure that... Role-Based A... |
| 1423 | 0.4356 | Activity Records are exported to -NetwrixAuditorUs... |
| 1424 | 0.4356 | For auditing cloud-based applications (Microsoft E... |
| 1425 | 0.4355 | On the computer where Netwrix Auditor Server resid... |
| 1426 | 0.4355 | Manually – Native audit settings must be adjusted ... |
| 1427 | 0.4354 | You can skip some parameters—the script uses a def... |
| 1428 | 0.4354 | The add-on enriches your SIEM data with actionable... |
| 1429 | 0.4353 | The body empty. contains Activity Records. 200 OK ... |
| 1430 | 0.4351 | In this case, Auditor will Table 1: Option Descrip... |
| 1431 | 0.4351 | v10.7 On... Ensure that... Role-Based Access and D... |
| 1432 | 0.4350 | • NOCHECK—Do not check Netwrix Auditor certificat ... |
| 1433 | 0.4350 | For Managed Service Providers: 443 TCP Netwrix Aud... |
| 1434 | 0.4349 | Required permissions Unless specified, the Netwrix... |
| 1435 | 0.4346 | v10.7 Follow the steps to review the recommendatio... |
| 1436 | 0.4345 | Manually – Native audit settings must be adjusted ... |
| 1437 | 0.4345 | Perform the procedure below, prior to the Core Ser... |
| 1438 | 0.4344 | Netwrix Privilege Secure Starting with version 10.... |
| 1439 | 0.4344 | While you can send Netwrix Auditor data to one of ... |
| 1440 | 0.4342 | Table 1: Scenario Example The add-on runs on theAu... |
| 1441 | 0.4340 | Overview diagrams—System-specific diagram reports ... |
| 1442 | 0.4340 | If Auditor Server becomes unavailable for some tim... |
| 1443 | 0.4340 | Step 2 – Depending on the user's delegated scope, ... |
| 1444 | 0.4339 | At least the first script run should be performed ... |
| 1445 | 0.4338 | Database service account – This is the same accoun... |
| 1446 | 0.4337 | To learn more about modern authentication, refer t... |
| 1447 | 0.4337 | NOTE: This is applicable for NetApp and Dell Data ... |
| 1448 | 0.4336 | To do it, click Configure next to Audit archiving ... |
| 1449 | 0.4335 | For that: On the computer where Netwrix Auditor is... |
| 1450 | 0.4335 | Table 1: Platform API (ISI_PRIV_LOGIN_PAPI) readon... |
| 1451 | 0.4334 | Netwrix Auditor 53 UDP DNS Server DNS Client Serve... |
| 1452 | 0.4332 | Allow outbound connections to remote ports on the ... |
| 1453 | 0.4332 | Tip for reading the table: For example, on the com... |
| 1454 | 0.4331 | The maximum size of the attachment file is 50 MB. ... |
| 1455 | 0.4330 | Adding the widlcard (*) to omitpathlist.txt will n... |
| 1456 | 0.4330 | The account must be assigned the Global reviewer r... |
| 1457 | 0.4328 | You can configure a single Netwrix Auditor client ... |
| 1458 | 0.4327 | ◦◦ If your file shares are stored within one folde... |
| 1459 | 0.4327 | After creating a task, wait for the next scheduled... |
| 1460 | 0.4326 | Specifies the length of ti meout before events fro... |
| 1461 | 0.4325 | It defines mapping between the Activity Records an... |
| 1462 | 0.4325 | Issues encountered during examination section is s... |
| 1463 | 0.4325 | See the Role-Based Access and Delegation topic for... |
| 1464 | 0.4324 | v10.7 Parameter Default value Description Instruct... |
| 1465 | 0.4323 | v10.7 Work with Collected Data To leverage data co... |
| 1466 | 0.4321 | Under the Root directory option, click Browse and ... |
| 1467 | 0.4320 | Duplicates, if any, are written to the Netwrix_Aud... |
| 1468 | 0.4320 | The user writing data to the Audit Database is gra... |
| 1469 | 0.4320 | Deploy the required number of Netwrix Auditor clie... |
| 1470 | 0.4320 | Alternatively, you can grant the Global administra... |
| 1471 | 0.4319 | Activity Records are on_for_Intel_Security.ps1 exp... |
| 1472 | 0.4319 | Step 5 – Configure and run reviews. The Entitlemen... |
| 1473 | 0.4319 | v10.7 Option Description available for 7 days. Che... |
| 1474 | 0.4318 | References details. Detail sub-elements (provided ... |
| 1475 | 0.4317 | The account must be assigned the Global reviewer r... |
| 1476 | 0.4317 | The account must be assigned the Global reviewer r... |
| 1477 | 0.4316 | Create a shortcut for this executable file. Right-... |
| 1478 | 0.4315 | You will only have to enter password. v10.7 To cre... |
| 1479 | 0.4314 | <domain\user> The file contains a list of user For... |
| 1480 | 0.4314 | Starting with version 10.7, you can implement the ... |
| 1481 | 0.4313 | Follow the steps to delete the Netwrix Auditor for... |
| 1482 | 0.4313 | NOTE: Stop and then restart the service every time... |
| 1483 | 0.4312 | Remember, a “resource” refers to the file system s... |
| 1484 | 0.4311 | Use this option to track suspicious Failed activit... |
| 1485 | 0.4311 | Netwrix recommends limiting the input Activity Rec... |
| 1486 | 0.4311 | For example: ,,CORP\\jsmith,*,*, Monitoring plan n... |
| 1487 | 0.4309 | Step 1 – To create or modify an audit archiving fi... |
| 1488 | 0.4309 | Disable integration NOTE: You can disable integrat... |
| 1489 | 0.4308 | v10.7 Duplicates, if any, are written to the Netwr... |
| 1490 | 0.4308 | v10.7 Duplicates, if any, are written to the Netwr... |
| 1491 | 0.4308 | Set Applies to to "This folder, subfolders and fil... |
| 1492 | 0.4307 | To grant required permissions, assign granular App... |
| 1493 | 0.4307 | To grant required permissions, assign granular App... |
| 1494 | 0.4305 | For example: mydomain\user1. Consider the followin... |
| 1495 | 0.4305 | Assign the Observers role to the user using Cluste... |
| 1496 | 0.4304 | At least the first script run should be performed ... |
| 1497 | 0.4304 | If you select to automatically configure audit in ... |
| 1498 | 0.4303 | monitoring plan name,who,where,object type,what,pr... |
| 1499 | 0.4300 | This role is also granted Audit Database. to servi... |
| 1500 | 0.4300 | I want to suppress errors from this server by excl... |
| 1501 | 0.4299 | The alerts have preset filters and can be easily u... |
| 1502 | 0.4298 | • Group Policy On the computer where Auditor Serve... |
| 1503 | 0.4298 | See the Audit Configuration Assistant topic for ad... |
| 1504 | 0.4298 | Configure a Response Action for Alert Upon the ale... |
| 1505 | 0.4296 | For a full list of audit settings and instructions... |
| 1506 | 0.4294 | If you select to automatically configure audit in ... |
| 1507 | 0.4291 | v10.7 Each report has a set of filters which help ... |
| 1508 | 0.4291 | Active Directory Auditor supports monitoring the f... |
| 1509 | 0.4290 | Step 1 – On the computer where SharePoint Central ... |
| 1510 | 0.4290 | See the Requirements for SQL Server to Store Audit... |
| 1511 | 0.4289 | You can also copy event details. Select the event ... |
| 1512 | 0.4288 | Deploy the required number of Netwrix Auditor clie... |
| 1513 | 0.4288 | Netwrix Auditor periodically checks for updates so... |
| 1514 | 0.4287 | Step 4 – Hit Enter. Depending on the number of Act... |
| 1515 | 0.4285 | In the Event Fields tab, select event levels that ... |
| 1516 | 0.4285 | Place the Netwrix.xsl file there, too, so that def... |
| 1517 | 0.4285 | Step 3 – In the Netwrix Auditor Client Users Prope... |
| 1518 | 0.4285 | Step 1 – On the computer where Auditor is installe... |
| 1519 | 0.4284 | Ongoing audit data collection will leverage Micros... |
| 1520 | 0.4283 | You can configure your IT Infrastructure for monit... |
| 1521 | 0.4282 | A custom account must be granted the same permissi... |
| 1522 | 0.4282 | File Servers Dell Data Storage Auditor supports mo... |
| 1523 | 0.4281 | Note that the new monitoring scope restrictions ap... |
| 1524 | 0.4280 | In this case, a single alert will be sent instead ... |
| 1525 | 0.4280 | This folder points to / ifs: isi smb shares create... |
| 1526 | 0.4279 | <NetwrixAuditorEndpoint>https:// 172.28.6.19:9699/... |
| 1527 | 0.4277 | Please refer to the Managing Indexers and Clusters... |
| 1528 | 0.4276 | MonitoringPlanItem — Specify an item name. Make su... |
| 1529 | 0.4276 | Review the table below for more information. Step ... |
| 1530 | 0.4275 | Maintenance and Troubleshooting If you cannot see ... |
| 1531 | 0.4275 | See the Role-Based Access and Delegation topic for... |
| 1532 | 0.4275 | Step 6 – Run the following command to update group... |
| 1533 | 0.4275 | See the Configure Integration API SettingsAudit Da... |
| 1534 | 0.4274 | The sysadmin server role on SQL Server instance is... |
| 1535 | 0.4274 | This role is also granted to service accounts or a... |
| 1536 | 0.4273 | Within timeframe: • Today • Yesterday • LastSevenD... |
| 1537 | 0.4273 | 33.. Right-click the Operational log and select Pr... |
| 1538 | 0.4273 | Table 1: File name Description HVARunner.exe Main ... |
| 1539 | 0.4273 | The account must be assigned the Global reviewer r... |
| 1540 | 0.4273 | See SQL Server Reporting Services for a dditional ... |
| 1541 | 0.4272 | You can deploy Auditor on a virtual machine runnin... |
| 1542 | 0.4271 | The same SQL Server instance cannot be used to sto... |
| 1543 | 0.4270 | { "resourceAppId": "00000003-0000-0000-c000-000000... |
| 1544 | 0.4268 | This may happen due to Secondary Logon Service Whe... |
| 1545 | 0.4267 | Table 1: Auditing type Oracle version Details Unif... |
| 1546 | 0.4266 | Configurator Access to monitoring plan configurati... |
| 1547 | 0.4265 | To feed data, send a POST request containing Activ... |
| 1548 | 0.4264 | Click Next. Step 3 – Click Run and close the windo... |
| 1549 | 0.4261 | Get the most from your SIEM investment — To maximi... |
| 1550 | 0.4261 | Personalize the home page of the product depending... |
| 1551 | 0.4260 | monitoring plan name,server name,error text For ex... |
| 1552 | 0.4260 | Location (optional) Provides a link to a corrupted... |
| 1553 | 0.4257 | v10.7 Windows Server 2012 R2 Windows Server 2012 C... |
| 1554 | 0.4257 | Step 3 – Right-click the service and on the Genera... |
| 1555 | 0.4256 | Activity Records are exported to NetwrixAuditorUse... |
| 1556 | 0.4256 | SMB Azure file shares are accessible from Windows,... |
| 1557 | 0.4255 | Step 1 – On the computer where Auditor Server resi... |
| 1558 | 0.4254 | The changes include creation, modifica tion, delet... |
| 1559 | 0.4254 | See the Manage Sources and Control Data Processing... |
| 1560 | 0.4254 | C:\Add-ons\Netwrix_Auditor_Addon_for_HPE_ ArcSight... |
| 1561 | 0.4253 | A service ticket is then created manually or autom... |
| 1562 | 0.4250 | Step 2 – Navigate to Network wide > Configure > Ge... |
| 1563 | 0.4249 | Ensure that... Role-Based Access and Delegation to... |
| 1564 | 0.4249 | The service will connect to Auditor Server using t... |
| 1565 | 0.4248 | It also illustrates the customization process with... |
| 1566 | 0.4248 | Creating, sending, or Admin receiving a message is... |
| 1567 | 0.4247 | Permissions for Windows File Server Auditing Befor... |
| 1568 | 0.4244 | See the SQL Server Reporting Services topic for ad... |
| 1569 | 0.4243 | Consider the following: • Use NetBIOS format for d... |
| 1570 | 0.4241 | At least the first script run should be performed ... |
| 1571 | 0.4241 | In group This operator relates to the Who filter. ... |
| 1572 | 0.4240 | (not displayed) The data source status is unknown.... |
| 1573 | 0.4240 | Specify port and protocol for incoming connections... |
| 1574 | 0.4239 | The add-on works in collaboration with Netwrix Aud... |
| 1575 | 0.4239 | In particular, the script deploys and starts Netwr... |
| 1576 | 0.4238 | Select the Informational value for the following p... |
| 1577 | 0.4237 | Clicking the Add plan button opens the New Monitor... |
| 1578 | 0.4235 | When using this mode, consider that the "What" fi ... |
| 1579 | 0.4235 | Select one of the following options: Table 1: Opti... |
| 1580 | 0.4235 | See the Configure Basic Domain Audit Policies or C... |
| 1581 | 0.4234 | For example, clicking Go to Original Go to Origina... |
| 1582 | 0.4234 | Added and Moved v10.7 After configuring all filter... |
| 1583 | 0.4233 | See the Role-Based Access and Delegation topic for... |
| 1584 | 0.4233 | Fine Grained Auditing Oracle Database 23c, 21c, 19... |
| 1585 | 0.4232 | Logon Activity Auditor supports monitoring the fol... |
| 1586 | 0.4228 | The add-on will match the application name and the... |
| 1587 | 0.4228 | If you want to use modern authentication and the N... |
| 1588 | 0.4228 | For example: mydomain\user1. Consider the followin... |
| 1589 | 0.4228 | v10.7 Step 6 – Click Configure. Next, for the most... |
| 1590 | 0.4227 | Data is sent in the request body and must be forma... |
| 1591 | 0.4226 | See State–In–Time Reports for more information. CA... |
| 1592 | 0.4226 | Upgrade Procedure You can upgrade Netwrix Auditor ... |
| 1593 | 0.4226 | NOTE: On the Netwrix Auditor Server, the gMSA acco... |
| 1594 | 0.4226 | Starting with version 10.7, you can implement the ... |
| 1595 | 0.4225 | Netwrix provides a command-line tool for enabling ... |
| 1596 | 0.4225 | Example 4 SCVMM and/or Auditor run on the machines... |
| 1597 | 0.4223 | You can also: Select a particular computer type to... |
| 1598 | 0.4223 | Local TCP Port 9004 is opened for inbound connecti... |
| 1599 | 0.4222 | Location XML is considered a default format for Ne... |
| 1600 | 0.4221 | In addition to the restrictions for a monitoring p... |
| 1601 | 0.4221 | Successful SELECT statement execution will be repo... |
| 1602 | 0.4221 | Duplicates, if any, are written to the Netwrix_Aud... |
| 1603 | 0.4220 | Most parameters are optional, the service uses the... |
| 1604 | 0.4220 | v10.7 Audit SELECT Use the settings in this sectio... |
| 1605 | 0.4219 | Table 1: Parameter Default value Description Gener... |
| 1606 | 0.4219 | Table 1: Feature Version 4.1 Version 5.x Network/d... |
| 1607 | 0.4218 | If you want to reopen closed tickets, you must be ... |
| 1608 | 0.4216 | Table 1: Hardware component Requirement Processor ... |
| 1609 | 0.4215 | NetwrixAuditorPassword Current user credentials Un... |
| 1610 | 0.4213 | Data is retrieved from a remote Auditor repository... |
| 1611 | 0.4207 | Write event descriptions to Audit Database Select ... |
| 1612 | 0.4207 | The Auditor server side • Auditor version is 10.0 ... |
| 1613 | 0.4205 | Otherwise, reports will contain limited data and w... |
| 1614 | 0.4204 | Alert Details: Instructs the system to fill in the... |
| 1615 | 0.4204 | • The TCP 9699 port must be open on Windows firewa... |
| 1616 | 0.4203 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} (DN... |
| 1617 | 0.4203 | Step 1 – Navigate to Start > Windows Administrativ... |
| 1618 | 0.4202 | Out of the box, messages from Red Hat Enterprise L... |
| 1619 | 0.4201 | See the Configure Security Event Log Maximum Size ... |
| 1620 | 0.4197 | In a separate Advanced Security Settings for <Shar... |
| 1621 | 0.4196 | Provide the IP address of the interface you specif... |
| 1622 | 0.4195 | Make sure the data source you are going to audit i... |
| 1623 | 0.4194 | Step 2 – Unpack the installation package. The foll... |
| 1624 | 0.4192 | Parameter Default value Description General parame... |
| 1625 | 0.4191 | Collect activity data only 1. For initial connecti... |
| 1626 | 0.4191 | If you have alternate access mapping configured in... |
| 1627 | 0.4190 | For example: Create ONTAPI role: security login ro... |
| 1628 | 0.4189 | ): No special configuration required to audit RMAN... |
| 1629 | 0.4188 | following line: .adminDesciption=Admin Screen Desc... |
| 1630 | 0.4185 | Follow the steps to configure Event Log Size and R... |
| 1631 | 0.4185 | Add the following parameters to the end: /s:server... |
| 1632 | 0.4184 | See the Configure Dell Isilon/PowerScale Cluster i... |
| 1633 | 0.4181 | Default is Priority 3 — Priority Normal Response. ... |
| 1634 | 0.4181 | Table 1: Event log field name Filled in with value... |
| 1635 | 0.4180 | Your current audit settings will be checked on eac... |
| 1636 | 0.4179 | See the Use Netwrix Privilege Secure as a Data Col... |
| 1637 | 0.4177 | Splunk Enterprise Splunk version is 8.0.6 or highe... |
| 1638 | 0.4176 | See the following topics for additional informatio... |
| 1639 | 0.4174 | If the monitoring plan name in the <NetwrixAuditor... |
| 1640 | 0.4173 | An event that indicates a significant problem such... |
| 1641 | 0.4171 | As a next step, click Add item to specify an objec... |
| 1642 | 0.4168 | How to Include/Exclude Applications To create a li... |
| 1643 | 0.4168 | Password Enter a password. NOTE: If you want to us... |
| 1644 | 0.4166 | Client Users group. See the Role-Based Access and ... |
| 1645 | 0.4165 | Check the password for this account. v10.7 NOTE: Y... |
| 1646 | 0.4161 | After you click View details, the Monitoring Overv... |
| 1647 | 0.4160 | Make sure to select this parameter if you plan to ... |
| 1648 | 0.4160 | For your convenience, the product provides predefi... |
| 1649 | 0.4159 | Data is ArcSightHost 172.28.6.24 - retrieved from ... |
| 1650 | 0.4156 | For example, you had a monitoring plan corp.local ... |
| 1651 | 0.4156 | Default prefix is NA, for example:NA Windows Serve... |
| 1652 | 0.4154 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 1653 | 0.4154 | The following step-bystep instructions are for mod... |
| 1654 | 0.4154 | NOTE: If you select a plan name in the add-on, mak... |
| 1655 | 0.4154 | Make sure Virtual Directory is set correctly, and ... |
| 1656 | 0.4153 | This significant ly improves data transfer and min... |
| 1657 | 0.4153 | Remember to do the following: v10.7 Prepare a Data... |
| 1658 | 0.4153 | cmdlet.param=friendlyna me For example: RoleGroupM... |
| 1659 | 0.4153 | Setting Recording Settings Configure custom locati... |
| 1660 | 0.4153 | To connect to NetApp Clustered Data ONTAP 8 or ONT... |
| 1661 | 0.4150 | To apply tags to an alert, navigate to alert setti... |
| 1662 | 0.4150 | Step 4 – Click Save. Optionally, you can select Do... |
| 1663 | 0.4149 | Check that you have configured the audit s ettings... |
| 1664 | 0.4147 | By default, each v10.7 monitoring plan will use a ... |
| 1665 | 0.4145 | Adding the widlcard (*) to omitpathlist.txt will n... |
| 1666 | 0.4141 | Alternatively, you can instruct Auditor not to sto... |
| 1667 | 0.4139 | If you set the In group condition for Who filter t... |
| 1668 | 0.4139 | Each Activity Record contains the user information... |
| 1669 | 0.4138 | How Risk Levels Are Estimated As mentioned, dashbo... |
| 1670 | 0.4138 | See Configure Fine Grained A uditing topic for mor... |
| 1671 | 0.4137 | By the way of example, this section provides instr... |
| 1672 | 0.4134 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1673 | 0.4134 | Step 3 – In the Advanced Security Settings for <Sh... |
| 1674 | 0.4133 | See the Check the Windows Services Status topic fo... |
| 1675 | 0.4132 | Troubleshooting The following are several troubles... |
| 1676 | 0.4131 | • NOCHECK—Do not check Netwrix Auditor certificate... |
| 1677 | 0.4131 | v10.7 New Features Integration with Netwrix Privil... |
| 1678 | 0.4130 | to the Auditor Home screen to access them instantl... |
| 1679 | 0.4130 | The tool transfers information on service accounts... |
| 1680 | 0.4128 | You can configure your IT Infrastructure for monit... |
| 1681 | 0.4128 | v10.7 You can use a single account to collect audi... |
| 1682 | 0.4128 | Table 1: Option Description Do not select the chec... |
| 1683 | 0.4127 | Auditor provides out-of-box reports that allow val... |
| 1684 | 0.4126 | See the Role-Based Access and Delegation topic for... |
| 1685 | 0.4123 | You will need to create this fi le manually and co... |
| 1686 | 0.4123 | Netwrix Privilege Secure. Starting with version 10... |
| 1687 | 0.4123 | • Services—Enables auditing of started/stopped ser... |
| 1688 | 0.4122 | Starting with version 10.5, Auditor provides limit... |
| 1689 | 0.4121 | This account should be assigned the following role... |
| 1690 | 0.4121 | NetwrixAuditorUserName Current user credentials Un... |
| 1691 | 0.4121 | For that, in the dashboard window click Subscribe ... |
| 1692 | 0.4119 | On the computer where Netwrix Auditor Server resid... |
| 1693 | 0.4117 | Specify a list of IP addresses of syslog events so... |
| 1694 | 0.4117 | NOTE: If you previously used a non-privileged acco... |
| 1695 | 0.4116 | Step 1 – Download the product installation package... |
| 1696 | 0.4112 | To audit users and groups, vCenter 6.5 and above r... |
| 1697 | 0.4112 | Similarly, the add-on also creates the Netwrix_Aud... |
| 1698 | 0.4111 | If you want to use another account, make sure it h... |
| 1699 | 0.4109 | Use them to create the lists of specific objects t... |
| 1700 | 0.4109 | Manually – Native audit settings must be adjusted ... |
| 1701 | 0.4109 | ◦ DNSHostName — FQDN of the new gMSA account, here... |
| 1702 | 0.4108 | In addition to the restrictions for a monitoring p... |
| 1703 | 0.4105 | • Workstation where activity was initiated — enter... |
| 1704 | 0.4105 | Work with Collected Data To leverage data collecte... |
| 1705 | 0.4105 | Work with Collected Data To leverage data collecte... |
| 1706 | 0.4105 | Work with Collected Data To leverage data collecte... |
| 1707 | 0.4105 | In the Auditing Entry dialog, click the Select a p... |
| 1708 | 0.4105 | In the Auditing Entry dialog, click the Select a p... |
| 1709 | 0.4103 | See the First Launch topic for additional informat... |
| 1710 | 0.4102 | Table 1: on... Ensure that... The Auditor Server s... |
| 1711 | 0.4102 | For the newly created app, you should use the Appl... |
| 1712 | 0.4102 | Netwrix Privilege Secure. Starting with version 10... |
| 1713 | 0.4098 | This topic focuses on the AlienVault USM SIEM solu... |
| 1714 | 0.4098 | This topic focuses on the AlienVault USM SIEM solu... |
| 1715 | 0.4096 | The add-on and Auditor must be installed on the sa... |
| 1716 | 0.4094 | object=friendlyname Contains a list of human-reada... |
| 1717 | 0.4093 | For more information on this deployment option, re... |
| 1718 | 0.4091 | In the Specify a name for your custom report dialo... |
| 1719 | 0.4090 | See the Microsoft Turn auditing on or off article ... |
| 1720 | 0.4090 | The dashboard comprises a set of widgets that disp... |
| 1721 | 0.4090 | Otherwise, your audit scope may contain warnings, ... |
| 1722 | 0.4088 | v10.7 Step 6 – Click Next. Step 7 – You need to ma... |
| 1723 | 0.4086 | By default, you can log in with your Windows crede... |
| 1724 | 0.4085 | Set the Network Security: Restrict NTLM: Outgoing ... |
| 1725 | 0.4085 | Auditor add-on for SIEMNetwrixAuditorUserName Tabl... |
| 1726 | 0.4084 | This significantly improves data transfer and mini... |
| 1727 | 0.4084 | This significantly improves data transfer and mini... |
| 1728 | 0.4081 | If the same account is being used for multiple pur... |
| 1729 | 0.4080 | v10.7 You might want to apply a filter to narrow d... |
| 1730 | 0.4080 | Starting with version 10.7, you can implement the ... |
| 1731 | 0.4078 | Data source: %DataSource% Step 2 – Then open Conne... |
| 1732 | 0.4078 | Table 1: Option Description Event Log Select an ev... |
| 1733 | 0.4078 | Step 2 – Delete the HKEY_LOCAL_MACHINE\SYSTEM\Curr... |
| 1734 | 0.4076 | Step 3 – Add script parameters. The console will l... |
| 1735 | 0.4074 | IsArchiveOnly No — IsArchiveOnly allows to save Ac... |
| 1736 | 0.4073 | Netwrix Auditor Certificat e Thumbprint Property. ... |
| 1737 | 0.4072 | Alternatively, you can grant the Global administra... |
| 1738 | 0.4072 | Step 1 – Check prerequisites. Since the add-ons wo... |
| 1739 | 0.4071 | Step 3 – If you have a client-server deployment, t... |
| 1740 | 0.4070 | To Summary emails. In this case audit disable filt... |
| 1741 | 0.4068 | Later, you can always create custom report from in... |
| 1742 | 0.4065 | Step 2 – Select a monitoring plan and the time ran... |
| 1743 | 0.4064 | Investigate incidents by running interactive searc... |
| 1744 | 0.4064 | This option is recommended for organizations that ... |
| 1745 | 0.4063 | If you set the Not in group Not in group This oper... |
| 1746 | 0.4062 | System-specific dashboards reflect all changes acr... |
| 1747 | 0.4062 | Work with Collected Data Review the examples below... |
| 1748 | 0.4060 | For example, you had a monitoring plan corp.local ... |
| 1749 | 0.4060 | v10.7 Option Description Accept List Specify a lis... |
| 1750 | 0.4060 | -NetwrixAuditorHost 172.28.6.15 C:\Add-ons\Netwrix... |
| 1751 | 0.4060 | This action is also logged when the admin or deleg... |
| 1752 | 0.4060 | property name Contains a list of objects to be and... |
| 1753 | 0.4058 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 1754 | 0.4058 | NOTE: This step is only required when changing the... |
| 1755 | 0.4058 | Monitoring Overview Aggregated statistics on the m... |
| 1756 | 0.4056 | To collect data from Windows Failover Cluster, net... |
| 1757 | 0.4056 | Also view historical reviews. My Reviews tab Direc... |
| 1758 | 0.4056 | Any additional role assignments will not be necess... |
| 1759 | 0.4056 | Any additional role assignments will not be necess... |
| 1760 | 0.4056 | Step 8 – Complete the following fields: Option Des... |
| 1761 | 0.4055 | See the Monitoring Planstopic for additional infor... |
| 1762 | 0.4054 | To do this, right-click a task and click Run. Work... |
| 1763 | 0.4054 | In addition to the restrictions for a monitoring p... |
| 1764 | 0.4053 | Group UMHuntGroup = U nified Messaging Hunt Group ... |
| 1765 | 0.4052 | Make sure that you specified the same names as in ... |
| 1766 | 0.4052 | Make sure that you specified the same names as in ... |
| 1767 | 0.4052 | Make sure that you specified the same names as in ... |
| 1768 | 0.4051 | The account must belong to the same domain where N... |
| 1769 | 0.4051 | Audit successful SELECT statements Auditing SELECT... |
| 1770 | 0.4050 | See the Exchange Administrator Audit Logging Setti... |
| 1771 | 0.4049 | ◦◦ By default, Auditor will monitor all shares sto... |
| 1772 | 0.4048 | NetwrixAuditorUserName Current user credentials Un... |
| 1773 | 0.4047 | For example, the product failed to process a domai... |
| 1774 | 0.4047 | State-in-Time reports to monitor data source state... |
| 1775 | 0.4047 | Auditor will automatically configure audit setting... |
| 1776 | 0.4046 | See the topics on the monitored items for details.... |
| 1777 | 0.4045 | By default, Netwrix Auditor Integration API works ... |
| 1778 | 0.4045 | Thus, s/he configures the product not to monitor t... |
| 1779 | 0.4045 | Thus, s/he configures the product not to monitor t... |
| 1780 | 0.4045 | Thus, s/he configures the product not to monitor t... |
| 1781 | 0.4044 | See next: Navigation Automate Sign-in to the Clien... |
| 1782 | 0.4043 | Prepare a machine for Microsoft SQL Server meeting... |
| 1783 | 0.4043 | State-in-time configuration snapshots are also use... |
| 1784 | 0.4043 | It is not recommended to store your Long-Term Arch... |
| 1785 | 0.4041 | will not be monitored. See the topics on the monit... |
| 1786 | 0.4040 | The retention method of the log must be set to “Ov... |
| 1787 | 0.4039 | Each data collecting accounts should meet the requ... |
| 1788 | 0.4038 | Failed change attempts The Auditing Entry below sh... |
| 1789 | 0.4038 | Active Directory service account – The Access Revi... |
| 1790 | 0.4038 | PaloAlto Devices Review a full list of object type... |
| 1791 | 0.4037 | See the SQL Server Reporting Services topic for ad... |
| 1792 | 0.4036 | omitlogonlist.txt to exclude logon activity from m... |
| 1793 | 0.4036 | Group Policy. See the Use Netwrix Privilege Secure... |
| 1794 | 0.4036 | Review Event Description Review the example of the... |
| 1795 | 0.4036 | The TCP 9699 port (default Auditor Integr ation AP... |
| 1796 | 0.4035 | If you set the In group condition for This operato... |
| 1797 | 0.4034 | -NetwrixAuditorUserName enterprise\NAuser NetwrixA... |
| 1798 | 0.4034 | If you select to automatically configure audit in ... |
| 1799 | 0.4032 | Otherwise, reports will contain limited data and w... |
| 1800 | 0.4032 | The non-replicated attributes pertain to a particu... |
| 1801 | 0.4031 | Add arguments (optional) Add a path to the add-on ... |
| 1802 | 0.4030 | Thus, s/he configures the product not to monitor t... |
| 1803 | 0.4029 | Review a full list of object types Netwrix Auditor... |
| 1804 | 0.4028 | See Configure Oracle Database for Auditing topic f... |
| 1805 | 0.4028 | Path The path must be provided in the same format ... |
| 1806 | 0.4027 | For example: Word\x0020 where \x0020 (with space a... |
| 1807 | 0.4027 | The user who runs the script is granted the db_own... |
| 1808 | 0.4027 | Effective grant —the effective set of permissions ... |
| 1809 | 0.4023 | v10.7 Option Description Do not select the checkbo... |
| 1810 | 0.4021 | Parameter Default value Description Connection to ... |
| 1811 | 0.4021 | v10.7 You can configure your IT Infrastructure for... |
| 1812 | 0.4021 | For example: Add arguments (optional) file "C:\Add... |
| 1813 | 0.4019 | 53 UDP Netwrix Auditor Server DNS Server DNS Clien... |
| 1814 | 0.4018 | Netwrix recommends installing the latest available... |
| 1815 | 0.4017 | Table 1: Action Object Type Attributes Interactive... |
| 1816 | 0.4017 | Manually – Native audit settings must be adjusted ... |
| 1817 | 0.4015 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 1818 | 0.4014 | See the State–In–Time Reports topic for additional... |
| 1819 | 0.4014 | See the State–In–Time Reports topic for additional... |
| 1820 | 0.4014 | See the State–In–Time Reports topic for additional... |
| 1821 | 0.4014 | The credentials are case sensitive. A custom accou... |
| 1822 | 0.4012 | Step 3 – Click the Add button. You can use a singl... |
| 1823 | 0.4011 | You can click Browse to select a computer from the... |
| 1824 | 0.4011 | v10.7 Then follow the steps in the Monitoring Plan... |
| 1825 | 0.4008 | Password field can be empty. Starting with version... |
| 1826 | 0.4006 | See theData C ollecting Account topic for addition... |
| 1827 | 0.4004 | The checklist will be replaced by statistics acros... |
| 1828 | 0.4003 | v10.7 NOTE: Netwrix Data Classification and Netwri... |
| 1829 | 0.4001 | The product will not collect any user activity or ... |
| 1830 | 0.4000 | Unless you are going to audit logon events, the ci... |
| 1831 | 0.4000 | You may keep the existing audit log retention prov... |
| 1832 | 0.4000 | Adjust Security Event Log Size and Retention Defin... |
| 1833 | 0.4000 | SQL Server Auditor supports monitoring the followi... |
| 1834 | 0.3999 | With enabled HTTPS, provide the computer name as i... |
| 1835 | 0.3999 | In addition to the restrictions for a monitoring p... |
| 1836 | 0.3999 | If an object has been moved between file shares, t... |
| 1837 | 0.3998 | v10.7 Option Description Enabling this option on p... |
| 1838 | 0.3998 | NOTE: The account must be assigned the Global revi... |
| 1839 | 0.3998 | Auditor Plan Item Unless specified, data is not as... |
| 1840 | 0.3997 | v10.7 set facility <facility_name> set port 514 se... |
| 1841 | 0.3997 | COMPLIANCE MAPPING Enables you to review how Audit... |
| 1842 | 0.3997 | ALTER SYSTEM SET audit_trail=XML SCOPE=SPFILE; If ... |
| 1843 | 0.3997 | ◦ Continue video recording regardless of the user ... |
| 1844 | 0.3996 | At least the first script run should be performed ... |
| 1845 | 0.3996 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 1846 | 0.3995 | Change Log Level The AccessInformationCenter.Servi... |
| 1847 | 0.3995 | If you plan to monitor Dell Isilon, clear the chec... |
| 1848 | 0.3994 | Make sure to specify a unique name. To modify a cu... |
| 1849 | 0.3991 | See the Network Traffic Compression topic for addi... |
| 1850 | 0.3990 | The Long-Term Archive widget—Helps you to estimate... |
| 1851 | 0.3990 | The credentials are case sensitive. Take into cons... |
| 1852 | 0.3990 | 88.. Switch to the Admin Access tab. Under the Sel... |
| 1853 | 0.3989 | This account must have at least Read Only role on ... |
| 1854 | 0.3989 | Table 1: Auditing Entry Successful reads The Audit... |
| 1855 | 0.3988 | Do one of the following: To configure Fortinet For... |
| 1856 | 0.3986 | See the Isilon OneFS 8.2.1 CLI Administration Guid... |
| 1857 | 0.3984 | You must define connection details: Auditor Server... |
| 1858 | 0.3983 | Specify the account for collecting data A custom a... |
| 1859 | 0.3982 | For initial connection to SharePoint Online, initi... |
| 1860 | 0.3980 | If you want to generate a report to assess your sy... |
| 1861 | 0.3980 | Step 4 – Depending on your monitoring requirements... |
| 1862 | 0.3980 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1863 | 0.3977 | Select an event log from the drop-down list. You w... |
| 1864 | 0.3977 | These features allow enabling Windows Media Player... |
| 1865 | 0.3976 | -ArcSightHost 172.28.6.18 C:\Add-ons\Netwrix_Audit... |
| 1866 | 0.3976 | Data is activity_records</ written to a remote Net... |
| 1867 | 0.3976 | The TCP 9699 port must be open on firew alls betwe... |
| 1868 | 0.3976 | The account used for data collection must meet the... |
| 1869 | 0.3976 | Notification — Configure the Notification settings... |
| 1870 | 0.3975 | This will not affect the reports or data searches ... |
| 1871 | 0.3973 | To be able to audit and report who made those chan... |
| 1872 | 0.3973 | Step 3 – Click Modify under the API settings secti... |
| 1873 | 0.3971 | property name Contains a list of objects to be and... |
| 1874 | 0.3971 | If you have more than one Auditor Server running S... |
| 1875 | 0.3969 | The output Activity Records may contain the follow... |
| 1876 | 0.3969 | In this case, data will be written to a database l... |
| 1877 | 0.3967 | Step 4 – Configure Audit Settings for CIFS File Sh... |
| 1878 | 0.3966 | NetwrixAuditorUserName Current user credentials If... |
| 1879 | 0.3966 | NetwrixAuditorUserName Current user credentials If... |
| 1880 | 0.3966 | For example: *,,CORP\\jsmith,*,*, omitstorelist.tx... |
| 1881 | 0.3964 | v10.7 Step 12 – After the validation, click Finish... |
| 1882 | 0.3963 | The appearance of the license will be reflected in... |
| 1883 | 0.3962 | Event log field name Filled in with value Details ... |
| 1884 | 0.3959 | See the Configure SMTP Server Settings topic for i... |
| 1885 | 0.3959 | Run the Command Prompt as Administrator. Execute t... |
| 1886 | 0.3959 | Data Discovery and Classification Reports Follow t... |
| 1887 | 0.3954 | Every time you run the script, Auditor makes a tim... |
| 1888 | 0.3954 | Specify the account for collecting data A custom a... |
| 1889 | 0.3954 | Add this parameter to write data in JSON format. O... |
| 1890 | 0.3954 | This method is recommended for evaluation purposes... |
| 1891 | 0.3952 | Default is 514. Note that if you are using Netwrix... |
| 1892 | 0.3952 | Failed read attempts Table 1: Auditing Entry The A... |
| 1893 | 0.3949 | User name This account must be granted the databas... |
| 1894 | 0.3949 | Unless specified, data is not associated with a s ... |
| 1895 | 0.3946 | Table 1: Policy Subnode Policy Name Audit Events A... |
| 1896 | 0.3946 | : Dell Data Storage Dell Isilon/PowerScale NetApp ... |
| 1897 | 0.3946 | Netwrix _Auditor_Integration_API Depending on Gene... |
| 1898 | 0.3944 | Table 1: Option Description Do not select the chec... |
| 1899 | 0.3944 | Default prefix is NA, for example:NA Windows Serve... |
| 1900 | 0.3943 | Updates to this partition are replicated to all do... |
| 1901 | 0.3943 | Program/script Input "Powershell.exe". Add argumen... |
| 1902 | 0.3943 | NetwrixAuditorUserName Current user credentials Un... |
| 1903 | 0.3943 | For example: -file "C:\Addons\Netwrix_Auditor_Addv... |
| 1904 | 0.3943 | Also, it lists requirements for the accounts used ... |
| 1905 | 0.3940 | By default, the LocalSystem account is used for th... |
| 1906 | 0.3940 | Currently, not every detail about permission and a... |
| 1907 | 0.3940 | As a next step, click Add item to specify an objec... |
| 1908 | 0.3940 | NetwrixAuditorPassword Current user credentials Un... |
| 1909 | 0.3935 | Step 3 – Specify SQL Server instance that you need... |
| 1910 | 0.3935 | This method is recommended for evaluation purposes... |
| 1911 | 0.3932 | If you have alternate access mapping configured in... |
| 1912 | 0.3932 | Configure audit settings You can adjust audit sett... |
| 1913 | 0.3932 | Configure audit settings You can adjust audit sett... |
| 1914 | 0.3932 | Configure audit settings You can adjust audit sett... |
| 1915 | 0.3932 | Configure audit settings You can adjust audit sett... |
| 1916 | 0.3931 | Windows PowerShell ISE will start. Step 3 – Run th... |
| 1917 | 0.3931 | If you have an on-premises Exchange server in your... |
| 1918 | 0.3931 | Your current audit settings will be checked on eac... |
| 1919 | 0.3930 | To get the add-on up and running, refer the follow... |
| 1920 | 0.3930 | To delete a custom report Navigate to Reports → Cu... |
| 1921 | 0.3929 | StartsWith EndsWith Contains (default) DoesNotCont... |
| 1922 | 0.3929 | If an ESXi host was specified as a monitored item ... |
| 1923 | 0.3929 | These settings cannot be modified for a certain pl... |
| 1924 | 0.3927 | I do not receive any results while searching audit... |
| 1925 | 0.3926 | Configure audit settings You can adjust audit sett... |
| 1926 | 0.3925 | For a full list of the rights and permissions requ... |
| 1927 | 0.3923 | You can set them to audit the following: Configura... |
| 1928 | 0.3922 | v10.7 You can apply a filter to narrow down your s... |
| 1929 | 0.3921 | The addon must always run locally, on the computer... |
| 1930 | 0.3920 | To specify a nondefault port, provide a new port n... |
| 1931 | 0.3920 | If you want to generate reports based on differen ... |
| 1932 | 0.3917 | share. Thus, s/he configures the product not to mo... |
| 1933 | 0.3917 | share. Thus, s/he configures the product not to mo... |
| 1934 | 0.3916 | Licenses The Licenses tab allows you to review the... |
| 1935 | 0.3915 | Log in to HPE Aruba web interface. Navigate to Mob... |
| 1936 | 0.3915 | Data Collecting Account Start data collection. Con... |
| 1937 | 0.3915 | Data Collecting Account Start data collection. Con... |
| 1938 | 0.3914 | The following inbound Firewall rules must be enabl... |
| 1939 | 0.3914 | For example to switch to the SVM called svm1: clus... |
| 1940 | 0.3913 | Any of them are required if you want to get the "W... |
| 1941 | 0.3912 | v10.7 Parameter Default value Description is not a... |
| 1942 | 0.3911 | When configuring audit manually, you see the follo... |
| 1943 | 0.3911 | The System account is used to launch the add-on vi... |
| 1944 | 0.3911 | This significantly improves data transfer and mini... |
| 1945 | 0.3910 | Table 1: On... Ensure that... The Audit Database s... |
| 1946 | 0.3910 | The credentials are case sensitive. If using a gro... |
| 1947 | 0.3909 | Step 1 – Create organizational units within audite... |
| 1948 | 0.3908 | • HTTP HTTPS v10.7 Option Description General Prov... |
| 1949 | 0.3906 | Using the Integration API, the add-on sends the ac... |
| 1950 | 0.3906 | Step 1 – In Netwrix Auditor, find your Exchange On... |
| 1951 | 0.3904 | v10.7 Option Description Do not select the checkbo... |
| 1952 | 0.3904 | v10.7 If an event occurs that triggers an alert, a... |
| 1953 | 0.3904 | The Security event log maximum size must be set to... |
| 1954 | 0.3903 | Specify monitoring restrictions Remember that admi... |
| 1955 | 0.3902 | See the Create a New Monitoring Plan topic for add... |
| 1956 | 0.3900 | Step 2 – Navigate to the Groups node and locate th... |
| 1957 | 0.3899 | Provide alert names as they appear in Auditor. NOT... |
| 1958 | 0.3898 | The same SQL Server instance cannot be used to sto... |
| 1959 | 0.3898 | See the Dell Upsilon CLI Administration Guide for ... |
| 1960 | 0.3897 | Select import database name. By default, data is i... |
| 1961 | 0.3895 | See the Prerequisites and Audit Database topics fo... |
| 1962 | 0.3894 | v10.7 On... Ensure that... The Audit Database sett... |
| 1963 | 0.3894 | v10.7 On... Ensure that... The Audit Database sett... |
| 1964 | 0.3893 | Use this option to track suspicious activity. Help... |
| 1965 | 0.3891 | Starting with version 10.7, you can implement the ... |
| 1966 | 0.3891 | The product will be automatically installed on com... |
| 1967 | 0.3890 | Table 2: Option Description From... To... Specify ... |
| 1968 | 0.3890 | Specify actions for monitoring Specify actions you... |
| 1969 | 0.3888 | See the Choose Appropriate Execution Scenario topi... |
| 1970 | 0.3888 | See the Choose Appropriate Execution Scenario topi... |
| 1971 | 0.3887 | Step 2 – Complete the following fields: Option Des... |
| 1972 | 0.3886 | Starting with version 10.7, you can implement the ... |
| 1973 | 0.3885 | Path The path must be provided in the same format ... |
| 1974 | 0.3885 | See the Monitoring Planstopic for additional infor... |
| 1975 | 0.3884 | ◦ Continue video recording regardless of the user ... |
| 1976 | 0.3881 | v10.7 Parameter Default value Description Specifie... |
| 1977 | 0.3879 | The add-on processes these events into Auditor-com... |
| 1978 | 0.3878 | If you select to automatically configure audit in ... |
| 1979 | 0.3878 | Try modifying your search. You are looking for cha... |
| 1980 | 0.3877 | Allow outbound connections to the remote ports on ... |
| 1981 | 0.3877 | NOTE: In this case,Auditor does not adjust audit s... |
| 1982 | 0.3877 | NOTE: In this case,Auditor does not adjust audit s... |
| 1983 | 0.3877 | NOTE: In this case,Auditor does not adjust audit s... |
| 1984 | 0.3875 | Step 4 – In the CN=Configuration, DC=<name>, DC=<n... |
| 1985 | 0.3874 | Audit logon events policy must be set to "Success.... |
| 1986 | 0.3874 | Table 1: Option Description When auditing file ser... |
| 1987 | 0.3873 | See the Role-Based Access and Delegation topic for... |
| 1988 | 0.3872 | The changes include creation, modifica tion, delet... |
| 1989 | 0.3872 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 1990 | 0.3872 | See the Customizing Favorite Reports topic for add... |
| 1991 | 0.3872 | managers, chief info rmation security officer, and... |
| 1992 | 0.3871 | By default, it is set to 120 months. Use custom cr... |
| 1993 | 0.3871 | SQL Server Express Edition with Advanced Services ... |
| 1994 | 0.3870 | DNS resource records—Enables auditing of all types... |
| 1995 | 0.3870 | Step 5 – Specify the application name and Netwrix ... |
| 1996 | 0.3868 | You can also use group Managed Service Accounts (g... |
| 1997 | 0.3868 | object_type.property_nam e If there is no separato... |
| 1998 | 0.3868 | Auditor version is 9.8 or later. The Audit Databas... |
| 1999 | 0.3867 | For example, to exclude inf ormation about databas... |
| 2000 | 0.3867 | v10.7 Add Microsoft Entra ID monitoring plan Follo... |
| 2001 | 0.3864 | Thus, the account should be a member of the follow... |
| 2002 | 0.3862 | C:\Add-ons\Netwrix_Auditor_Addon_for_ AlienVault_U... |
| 2003 | 0.3860 | If you want to audit all access types (successful ... |
| 2004 | 0.3858 | See the COMPLIANCE MAPPING Compliance Mappings top... |
| 2005 | 0.3857 | Refer to the following sections below for manual i... |
| 2006 | 0.3857 | Once the product is configured to collect data fro... |
| 2007 | 0.3857 | Your current audit settings will be checked on eac... |
| 2008 | 0.3857 | Your current audit settings will be checked on eac... |
| 2009 | 0.3856 | Configuring mailbox access tracking for Exchange 2... |
| 2010 | 0.3855 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 2011 | 0.3855 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 2012 | 0.3855 | that are less important. See Configure Fine Graine... |
| 2013 | 0.3855 | Failed change attempts The Auditing Entry below sh... |
| 2014 | 0.3855 | Step 1 – Navigate to Start > Netwrix Auditor > Net... |
| 2015 | 0.3855 | v10.7 To manage API security settings with APIAdmi... |
| 2016 | 0.3854 | This status applies to the monitoring plans target... |
| 2017 | 0.3854 | See the Use Group Managed Service Account (gMSA) t... |
| 2018 | 0.3854 | See the Use Group Managed Service Account (gMSA) t... |
| 2019 | 0.3854 | See the Use Group Managed Service Account (gMSA) t... |
| 2020 | 0.3854 | See the Use Group Managed Service Account (gMSA) t... |
| 2021 | 0.3854 | See the Use Group Managed Service Account (gMSA) t... |
| 2022 | 0.3854 | NOTE: In some cases, Who will be the system and Wh... |
| 2023 | 0.3853 | Additional Configuration to Review Changes Made vi... |
| 2024 | 0.3851 | Data Collecting Account Scope By default, Auditor ... |
| 2025 | 0.3850 | Step 4 – Save the dbparam.ini file. Download the A... |
| 2026 | 0.3850 | See the Audit Database topic for additional inform... |
| 2027 | 0.3848 | Provide alert names as they appear in Auditor. NOT... |
| 2028 | 0.3847 | Access key is used to run requests to AWS SDK, CLI... |
| 2029 | 0.3847 | Your current audit settings will be checked on eac... |
| 2030 | 0.3846 | If you want to monitor userv10.7 Data Source Item ... |
| 2031 | 0.3846 | NOTE: If you want to get only state-in-time snapsh... |
| 2032 | 0.3846 | Step 1 – On the computer where Microsoft Exchange ... |
| 2033 | 0.3845 | Right-click it and select Properties from the pop-... |
| 2034 | 0.3845 | Reviewer Access to data collected by Auditor and i... |
| 2035 | 0.3844 | v10.7 You might want to apply a filter to narrow d... |
| 2036 | 0.3844 | Version Related documentation Clustered Data ONTAP... |
| 2037 | 0.3844 | Deployment Scenarios The Add-On can run on any com... |
| 2038 | 0.3843 | See the Fine-tune Monitoring ScopeFine-tune Monito... |
| 2039 | 0.3843 | See the Netwrix Privilege Secure and How to Add Mi... |
| 2040 | 0.3841 | See the Fine-tune Monitoring ScopeFine-tune Monito... |
| 2041 | 0.3841 | SQL Server When planning for SQL Server that will ... |
| 2042 | 0.3840 | If a user is removed from this list, agentomituser... |
| 2043 | 0.3838 | Data is C:\Add-ons\Netwrix_Auditor_Addwritten to a... |
| 2044 | 0.3837 | Select this option if you want to use other creden... |
| 2045 | 0.3837 | Collect data for state-in-time reports Configure A... |
| 2046 | 0.3836 | Table 1: Object Type Reported Action Reported Prop... |
| 2047 | 0.3835 | OutputFolder C:\CEF_Export C:\Addons\Netwrix_Audit... |
| 2048 | 0.3835 | Unless specified, data is not associated with a s ... |
| 2049 | 0.3834 | Add-on running on the same machine as Auditor Serv... |
| 2050 | 0.3834 | See this Knowledge Base article for more inf ormat... |
| 2051 | 0.3834 | These settings are global, that is, they will be a... |
| 2052 | 0.3834 | To restore original look and feel, run the script ... |
| 2053 | 0.3833 | To be able to audit and report who made those chan... |
| 2054 | 0.3832 | If selected, this option instructs Auditor to depl... |
| 2055 | 0.3831 | Inner_type is optional. Table 1: File Description ... |
| 2056 | 0.3830 | to the Auditor Home screen to access them instantl... |
| 2057 | 0.3830 | Use this option to supervise access to files conta... |
| 2058 | 0.3823 | According to the RESTful model, each operation is ... |
| 2059 | 0.3822 | You can apply a filter to narrow down your search ... |
| 2060 | 0.3822 | Clicking a Role link opens the detailed report on ... |
| 2061 | 0.3822 | ◦◦ Upload to a file share—Select this option to sa... |
| 2062 | 0.3822 | For more information on the structure of the Activ... |
| 2063 | 0.3821 | See the NetApp Data ONTAP topic for additional inf... |
| 2064 | 0.3820 | Step 2 – Navigate to Event Viewer tree > Windows L... |
| 2065 | 0.3820 | Launch an Internet browser and enter the following... |
| 2066 | 0.3820 | After specifying the criteria you need, click Sear... |
| 2067 | 0.3819 | See Add Items for Monitoringfor more information. ... |
| 2068 | 0.3819 | with a huge amount of objects, so s/he does not wa... |
| 2069 | 0.3818 | Wait until the tool has finished restoring the sel... |
| 2070 | 0.3817 | Specify a name of associated monitoring plan in Au... |
| 2071 | 0.3817 | This file contains a list of users who must be exc... |
| 2072 | 0.3816 | Activity Records are exported to a local folder. C... |
| 2073 | 0.3816 | You might want to apply a filter to narrow down yo... |
| 2074 | 0.3815 | VMware Servers Auditor supports monitoring the fol... |
| 2075 | 0.3815 | Allowed-addresses are: 192.168.1.0/24. Check the c... |
| 2076 | 0.3815 | Ensure that your account meets the requirements an... |
| 2077 | 0.3812 | To ensure proper operation, the VM template must b... |
| 2078 | 0.3812 | object_type_name.propert y_name.attribute_name Con... |
| 2079 | 0.3812 | Your current audit settings will be checked on eac... |
| 2080 | 0.3812 | Your current audit settings will be checked on eac... |
| 2081 | 0.3811 | Otherwise, specify custom path to logo file. Defau... |
| 2082 | 0.3808 | NetwrixAuditorUserName Current user credentials Un... |
| 2083 | 0.3806 | Step 2 – On the General tab, specify a task name. ... |
| 2084 | 0.3806 | Step 2 – On the General tab, specify a task name. ... |
| 2085 | 0.3805 | Grant —the set of permissions granted to this acco... |
| 2086 | 0.3803 | The Audit Database settings are configured in Audi... |
| 2087 | 0.3803 | Step 3 – Select the type of the Access Policy you ... |
| 2088 | 0.3802 | To control who does what in the IT infrastructure ... |
| 2089 | 0.3801 | Defines the Audit Database connection timeout (in ... |
| 2090 | 0.3800 | ◦◦ On the Auditor console computer: If you have en... |
| 2091 | 0.3800 | ◦◦ On the Auditor console computer: If you have en... |
| 2092 | 0.3800 | In the report filters, select a monitoring plan yo... |
| 2093 | 0.3799 | Auditor version is 9.8 or later. The Audit Databas... |
| 2094 | 0.3798 | Depending on your Oracle Database version, the SEL... |
| 2095 | 0.3796 | To modify conditions for the selected filters, mak... |
| 2096 | 0.3796 | Otherwise, reports will contain limited data and w... |
| 2097 | 0.3796 | Microsoft Entra ID (formerly Azure AD) Auditor sup... |
| 2098 | 0.3795 | A Security Officer wants to monitor a file share, ... |
| 2099 | 0.3791 | Step 1 – On the main Auditor page, navigate to the... |
| 2100 | 0.3791 | If you want the add-on to use another account to c... |
| 2101 | 0.3790 | Table 1: Parameter Default value Description Conne... |
| 2102 | 0.3790 | Table 1: Parameter Default value Description Conne... |
| 2103 | 0.3790 | Changes to Domain local groups of a different doma... |
| 2104 | 0.3789 | Verify the parameters you provided in Settings.xml... |
| 2105 | 0.3789 | If you upgraded Netwrix Auditor from the version 1... |
| 2106 | 0.3787 | The credentials are case sensitive. If using a gro... |
| 2107 | 0.3785 | If you select to automatically configure audit in ... |
| 2108 | 0.3785 | Cisco FTD Auditor supports monitoring the followin... |
| 2109 | 0.3784 | Step 2 – In the upper-left of your site collection... |
| 2110 | 0.3783 | Use the account with a privileged role on a regula... |
| 2111 | 0.3783 | REPORTS Access the predefined reports for each dat... |
| 2112 | 0.3782 | And UDP port (for, example 514) is used for sendin... |
| 2113 | 0.3782 | C:\Add-ons\Netwrix_Auditor_Addon_for_HPE_ ArcSight... |
| 2114 | 0.3782 | Possible parameter values: • True — fill in the Ev... |
| 2115 | 0.3782 | Possible parameter values: • True — fill in the Ev... |
| 2116 | 0.3782 | A custom account must be granted the same permissi... |
| 2117 | 0.3781 | See the Audit Configuration Assistant topic for ad... |
| 2118 | 0.3781 | View and Search Collected Data how to apply filter... |
| 2119 | 0.3781 | Activity Records are exported to a local folder. C... |
| 2120 | 0.3780 | Step 4 – Click Apply. Table 1: Port Protocol Sourc... |
| 2121 | 0.3779 | Table 2: Opens the Alerts Overview dashboard, whic... |
| 2122 | 0.3779 | 66.. Run the following command to update group pol... |
| 2123 | 0.3779 | on the fi rst server you have set up in the farm: ... |
| 2124 | 0.3778 | You can enable Auditor to continually enforce the ... |
| 2125 | 0.3777 | See this Microsoft article for details. Last full ... |
| 2126 | 0.3774 | To exclude a change from reports, search results a... |
| 2127 | 0.3774 | Also, creating a mailbox folder isn't audited. Tab... |
| 2128 | 0.3773 | Table 1: Parameter Default value Description Provi... |
| 2129 | 0.3772 | The Auditor Server side • Auditor version is 9.8 o... |
| 2130 | 0.3770 | Table 1: Report Description File Servers Activity ... |
| 2131 | 0.3770 | For some antiviruses (for example, Trend Micro) yo... |
| 2132 | 0.3770 | You can specify a custom account only for the Long... |
| 2133 | 0.3770 | To get the add-on up and running, please read the ... |
| 2134 | 0.3769 | Use the omitreadaccess.txt to exclude MYSERVER\* S... |
| 2135 | 0.3769 | (See the Microsoft Placing fi les directly in the ... |
| 2136 | 0.3769 | Append help to any command to see available parame... |
| 2137 | 0.3769 | Table 2: Parameter Default value Description Event... |
| 2138 | 0.3768 | Ensure that... Auditor version is 10.0 or later. T... |
| 2139 | 0.3767 | For these users, the product collects data from ES... |
| 2140 | 0.3767 | A Security Officer wants to monitor a file share, ... |
| 2141 | 0.3766 | See this Knowledge Base article for more informati... |
| 2142 | 0.3766 | As a next step, click Add item to specify an objec... |
| 2143 | 0.3764 | See the Configure Dell Isilon/PowerScale Cluster i... |
| 2144 | 0.3764 | Auditor Server side • Auditor version is 9.8 or la... |
| 2145 | 0.3763 | Step 7 – In Auditor, create a monitoring plan for ... |
| 2146 | 0.3763 | Besides, Netwrix Auditor Password Expiration Notif... |
| 2147 | 0.3762 | Make sure to create a dedicated item inAuditor in ... |
| 2148 | 0.3760 | Step 7 – In Auditor, create a monitoring plan for ... |
| 2149 | 0.3760 | Applies to—Set to "Files only". Advanced permissio... |
| 2150 | 0.3759 | Server and Client It is recommended to deploy Audi... |
| 2151 | 0.3759 | Review the following for additional information: C... |
| 2152 | 0.3759 | Action Type – select what types of a ctions perfor... |
| 2153 | 0.3758 | Enable automatic audit configuration— If any confl... |
| 2154 | 0.3758 | * v10.7 A wildcard (*) is supported. You can use *... |
| 2155 | 0.3758 | The retention method of the Security event log mus... |
| 2156 | 0.3756 | v10.7 Step 2 – The level value is set in the LogLe... |
| 2157 | 0.3755 | Applies to—Set to"This folder, subfolders and file... |
| 2158 | 0.3755 | C:\Add-ons\Netwrix_Auditor_Addon_for_RADIUS_Server... |
| 2159 | 0.3755 | Delegate FolderBind NOTE: Audit records for folder... |
| 2160 | 0.3754 | Contact your Auditor Global administrator to make ... |
| 2161 | 0.3753 | To exclude computers from within the s pecified ra... |
| 2162 | 0.3752 | Successful changes The Auditing Entry below shows ... |
| 2163 | 0.3752 | Step 2 – In the Tenant information locate the Prim... |
| 2164 | 0.3752 | Step 2 – In the Tenant information locate the Prim... |
| 2165 | 0.3752 | For more information on the attributes marked with... |
| 2166 | 0.3752 | v10.7 Step 2 – Unzip the package to any folder on ... |
| 2167 | 0.3752 | Data is collected from a NetwrixAuditorHost remote... |
| 2168 | 0.3751 | The Auditor Server side The Audit Database setting... |
| 2169 | 0.3751 | The Auditor Server side The Audit Database setting... |
| 2170 | 0.3750 | Failed Use this option to detect suspicious activi... |
| 2171 | 0.3749 | For example, you can run the add-on on the compute... |
| 2172 | 0.3748 | CertificateThumbprint NOCHECK Auditor Certificate ... |
| 2173 | 0.3747 | C:\Add-ons\Netwrix_Auditor_Addon_for_IBM_ QRadar.p... |
| 2174 | 0.3745 | will not be monitored. See the topics on the monit... |
| 2175 | 0.3744 | Review the following for a dditional information: ... |
| 2176 | 0.3742 | In this case, Netwrix Auditor Server will retrieve... |
| 2177 | 0.3741 | See Assign Roles topic for more information. Navig... |
| 2178 | 0.3741 | This is optional unless you plan to create index c... |
| 2179 | 0.3740 | During the Netwrix Auditor for SharePoint Core Ser... |
| 2180 | 0.3739 | v10.7 44.. Make sure the Enable logging option is ... |
| 2181 | 0.3739 | See the Role-Based Access and Delegation topic for... |
| 2182 | 0.3738 | Provide the port configured in your monitoring pla... |
| 2183 | 0.3738 | The retention method must be set to “Overwrite eve... |
| 2184 | 0.3738 | Feature comparison is provided in the table below.... |
| 2185 | 0.3737 | v10.7 Prerequisites Netwrix Auditor Integration AP... |
| 2186 | 0.3737 | For details about metrics calculation, see How Ris... |
| 2187 | 0.3733 | Monitoring plan configuration List folders + + + +... |
| 2188 | 0.3733 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 2189 | 0.3731 | If any conflicts are detected with your current au... |
| 2190 | 0.3731 | Configure Scope You can narrow your monitoring sco... |
| 2191 | 0.3731 | Specify data collection method You can enable netw... |
| 2192 | 0.3731 | Specify data collection method You can enable netw... |
| 2193 | 0.3730 | For example: DB_M0,EntSQL,SQLFailedLogon,guest ,Wk... |
| 2194 | 0.3730 | In addition to the restrictions for a monitoring p... |
| 2195 | 0.3728 | Specify actions you want to track and auditing mod... |
| 2196 | 0.3727 | See the Create a New Monitoring Plan topic for add... |
| 2197 | 0.3726 | Step 1 – Select the AD FS data source in this moni... |
| 2198 | 0.3726 | v10.7 Required Roles and Permissions To... Require... |
| 2199 | 0.3726 | If you want the add-on to use another account to c... |
| 2200 | 0.3726 | The Auditor server side • Auditor version is 10.0 ... |
| 2201 | 0.3725 | Allow outbound connections from the dynamic (1024 ... |
| 2202 | 0.3725 | Step 3 – Use the Access reviews configuration tool... |
| 2203 | 0.3725 | NOTE: You can disable integration with one alert a... |
| 2204 | 0.3724 | Step 7 – Navigate to Event Filters and click Add t... |
| 2205 | 0.3724 | Table 1: Option Description Example All Data Selec... |
| 2206 | 0.3724 | Table 1: Option Description Example All Data Selec... |
| 2207 | 0.3723 | Step 2 – Open a port for inbound connections. See ... |
| 2208 | 0.3722 | Provide the name of the UDP port used to listen to... |
| 2209 | 0.3722 | The LocalSystem account is selected by Long-Term A... |
| 2210 | 0.3721 | If you use the following combination of the audit ... |
| 2211 | 0.3721 | Error details: 0x80040204 Cannot convert the attri... |
| 2212 | 0.3720 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 2213 | 0.3720 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 2214 | 0.3720 | Do not modify the endpoint part (/ netwrix/ api ) ... |
| 2215 | 0.3719 | See the Placing files directly in the namespace sh... |
| 2216 | 0.3718 | v10.7 Issue Reason and solution Monitoring Plan: <... |
| 2217 | 0.3718 | • Applies to—Set to"Files only". • Advanced permis... |
| 2218 | 0.3718 | Configurator to make sure that the monitoring plan... |
| 2219 | 0.3717 | Option Description Specify the name of the SQL Ser... |
| 2220 | 0.3717 | Configure Scope You can narrow your monitoring sco... |
| 2221 | 0.3715 | This is a mandatory parameter. v10.7 Parameter Def... |
| 2222 | 0.3715 | This URL is used to get OneFS web administration i... |
| 2223 | 0.3715 | See RoleBased Access and Delegation. Alternatively... |
| 2224 | 0.3714 | Method Endpoint POST Data https://{host:port}/ net... |
| 2225 | 0.3713 | Step 3 – Select the type of the Access Policy you ... |
| 2226 | 0.3712 | Step 3 – After configuring all filters, click Add ... |
| 2227 | 0.3711 | Specify how long data will be stored. By default, ... |
| 2228 | 0.3711 | For detailed information about Qumulo Web UI. refe... |
| 2229 | 0.3711 | OR Table 1: To... Requirement Comment Cloud Applic... |
| 2230 | 0.3710 | Successful changes The Auditing Entry below shows ... |
| 2231 | 0.3710 | gpupdate / force 445 TCP Netwrix Auditor Server Do... |
| 2232 | 0.3709 | All audit data from your search query results will... |
| 2233 | 0.3708 | OR In the main screen, in the Configuration sectio... |
| 2234 | 0.3708 | v10.7 Account Lockout Examiner Overview Netwrix Ac... |
| 2235 | 0.3708 | Subscription to Risk Assessment Overview This subs... |
| 2236 | 0.3707 | See the Monitoring Planstopic for additional infor... |
| 2237 | 0.3706 | Step 1 – Get your certificate or generate a self-s... |
| 2238 | 0.3705 | ◦ To export filtered data to PDF or CSV, click Exp... |
| 2239 | 0.3705 | v10.7 Step 6 – Click OK. Step 7 – In Auditor, crea... |
| 2240 | 0.3705 | Active Directory Ports Review a full list of proto... |
| 2241 | 0.3705 | Set up protocols and ports. See the Dell Data Stor... |
| 2242 | 0.3705 | For example: OracleUser as sysdba Step 3 – Enter y... |
| 2243 | 0.3704 | omitreporterrors.txt Contains a list of errors to ... |
| 2244 | 0.3703 | Alternatively, you can grant the Global administra... |
| 2245 | 0.3702 | Click Apply. Fortinet FortiGate Devices Review a f... |
| 2246 | 0.3701 | See the Fine-Tune Your Plan and Edit Settings topi... |
| 2247 | 0.3701 | Step 6 – (optional) To adjust the add-on operation... |
| 2248 | 0.3701 | I want to suppress errors from this server by excl... |
| 2249 | 0.3700 | The service will collect and process events from t... |
| 2250 | 0.3699 | It is shipped with the add-on and creates the RADI... |
| 2251 | 0.3699 | • .NET Framework 4.5 or later must be installed. Q... |
| 2252 | 0.3699 | Optionally, you can click the Create Test Ticket b... |
| 2253 | 0.3698 | Click Examine. Table 1: Option Description Default... |
| 2254 | 0.3698 | Windows Server Ports Review a full list of protoco... |
| 2255 | 0.3698 | You can select both Active Directory and Logon Act... |
| 2256 | 0.3697 | Provide a different password if necessary. Table 2... |
| 2257 | 0.3697 | Provide a different password if necessary. Table 2... |
| 2258 | 0.3697 | In addition to the restrictions for a monitoring p... |
| 2259 | 0.3696 | You can enable Auditor to continually enforce the ... |
| 2260 | 0.3694 | Helps find out who was trying to access your priva... |
| 2261 | 0.3694 | The product will audit only user accounts that bel... |
| 2262 | 0.3694 | Extra-Large Environment Recommendations below refe... |
| 2263 | 0.3694 | • 1—Full installation v10.7 where %Temp% can be re... |
| 2264 | 0.3691 | For example, you can run the add-on on the compute... |
| 2265 | 0.3691 | For example, you can run the add-on on the compute... |
| 2266 | 0.3690 | Accept List Specify a list of IP addresses of sysl... |
| 2267 | 0.3690 | See the Role-Based Access and Delegation topic for... |
| 2268 | 0.3690 | See the Role-Based Access and Delegation topic for... |
| 2269 | 0.3689 | For example, an IT manager can easily provide audi... |
| 2270 | 0.3688 | • Advanced permissions—SelectList folder / read da... |
| 2271 | 0.3686 | File Servers (including Windows file server, Dell,... |
| 2272 | 0.3686 | Install the Add-on Follow the steps to install the... |
| 2273 | 0.3685 | Table 1: To monitor for... Execute... Successful d... |
| 2274 | 0.3684 | A Security Officer wants to monitor a file share, ... |
| 2275 | 0.3683 | If you want to audit all access types (successful ... |
| 2276 | 0.3681 | • Applies to—Set to "Files only". • Advanced permi... |
| 2277 | 0.3680 | Applies to—Set to "This folder, subfolders and fil... |
| 2278 | 0.3679 | Some data sources require additional system compon... |
| 2279 | 0.3679 | The message indicates to the recipient who the Tab... |
| 2280 | 0.3679 | <domain\user> For example, to exclude changes made... |
| 2281 | 0.3678 | Oracle Auditor supports monitoring the following v... |
| 2282 | 0.3674 | See the following topics for additional informatio... |
| 2283 | 0.3674 | CAUTION: Once you click UNINSTALL you cannot cance... |
| 2284 | 0.3673 | All devices Collected via MS Graph on endpoint /de... |
| 2285 | 0.3673 | list/ document.docx. SQL Server NOTE: Prior to con... |
| 2286 | 0.3673 | For that, use the Monitoring Plan wizard or naviga... |
| 2287 | 0.3673 | See RoleBased Access and Delegation. Alternatively... |
| 2288 | 0.3672 | If you want to run the add-on on another machine, ... |
| 2289 | 0.3672 | If you want to run the add-on on another machine, ... |
| 2290 | 0.3672 | If you are going to use a gMSA to access Audit Dat... |
| 2291 | 0.3672 | ◦ Download the appropriate package from Oracle web... |
| 2292 | 0.3668 | This refers to the specified shared folder, its su... |
| 2293 | 0.3665 | 44.. Configure the following audit policies. Table... |
| 2294 | 0.3664 | As an account for accessing Audit Databases. See R... |
| 2295 | 0.3664 | Run Windows PowerShell as administrator and execut... |
| 2296 | 0.3664 | Step 3 – Run the NetwrixOktaAddon.exe and follow t... |
| 2297 | 0.3664 | Step 5 – Click on the arrow button next to any of ... |
| 2298 | 0.3663 | Have there been any unusual spikes in failed activ... |
| 2299 | 0.3663 | If you want to run the add-on on another machine, ... |
| 2300 | 0.3660 | Whenever the alert is triggered, the add-on uses t... |
| 2301 | 0.3659 | 44.. Configure the following audit policies. Polic... |
| 2302 | 0.3659 | This refers to the specified shared folder, its su... |
| 2303 | 0.3658 | All fi lters required to store events for all avai... |
| 2304 | 0.3657 | Some network compression services must be removed ... |
| 2305 | 0.3657 | NetwrixAuditorUserName Current user credentials Un... |
| 2306 | 0.3657 | Add an Exchange Online Monitoring Plan Follow the ... |
| 2307 | 0.3657 | In Auditor settings, go to the Integrations sectio... |
| 2308 | 0.3655 | For example, "MyOracle". Alias name in Netwrix Aud... |
| 2309 | 0.3654 | See the Assign Permission To Read the Registry Key... |
| 2310 | 0.3652 | v10.7 File Description Syntax For example, if you ... |
| 2311 | 0.3652 | Remember that replication of namespace roots is no... |
| 2312 | 0.3652 | Oracle recommends using Unified Auditing, which en... |
| 2313 | 0.3651 | This script creates a Windows scheduled task that ... |
| 2314 | 0.3651 | v10.7 IBM QRadar Netwrix Auditor Add-on for SIEM h... |
| 2315 | 0.3651 | • To exclude the certain user's mailbox, enter use... |
| 2316 | 0.3650 | To collect data from 32-bit operating systems, net... |
| 2317 | 0.3650 | See the Compliance Reports topic for additional in... |
| 2318 | 0.3648 | NetwrixAuditorPassword Current user credentials Un... |
| 2319 | 0.3648 | On the computer where Auditor Server is installed:... |
| 2320 | 0.3646 | Change and activity reports—System-specific report... |
| 2321 | 0.3646 | v10.7 Favorites Sub-Folder Options Favorites > [Re... |
| 2322 | 0.3646 | This policy should be configured manually since Au... |
| 2323 | 0.3643 | Ensure that... The Audit Database settings are con... |
| 2324 | 0.3643 | To audit users and groups, vCenter 6.5 and above r... |
| 2325 | 0.3643 | A custom account must be granted the same permissi... |
| 2326 | 0.3642 | In the next menu, select Paste all certificates in... |
| 2327 | 0.3642 | If enabled, a Compression Service will be automati... |
| 2328 | 0.3642 | If you want to audit all actions (successful reads... |
| 2329 | 0.3642 | The credentials are case sensitive. If using a gro... |
| 2330 | 0.3642 | The credentials are case sensitive. If using a gro... |
| 2331 | 0.3642 | The credentials are case sensitive. If using a gro... |
| 2332 | 0.3641 | v10.7 Parameter Default value Description Unless s... |
| 2333 | 0.3640 | Access to global environment. settings, monitoring... |
| 2334 | 0.3640 | NetwrixAuditorCertificateThumbpr int NOCHECK Netwr... |
| 2335 | 0.3640 | • File shares—Enables auditing of created / remove... |
| 2336 | 0.3640 | The URL for the Access Reviews Console is now acce... |
| 2337 | 0.3638 | For example, a new file share was created on the a... |
| 2338 | 0.3638 | This SQL Server will be used as default host for A... |
| 2339 | 0.3636 | Customize Branding Netwrix Auditor allows customiz... |
| 2340 | 0.3635 | RECOMMENDED: Adjust retention period for the backu... |
| 2341 | 0.3634 | The changes include creation, modifica tion, delet... |
| 2342 | 0.3632 | For example: DB_M0,EntSQL,SQLFailedLogon,guest ,Wk... |
| 2343 | 0.3631 | audit_sys_operations=TRUE SCOPE=SPFILE; Table 1: S... |
| 2344 | 0.3631 | You can skip or define parameters depending on you... |
| 2345 | 0.3631 | You can skip or define parameters depending on you... |
| 2346 | 0.3628 | In the Add New Syslog Servers dialog, complete the... |
| 2347 | 0.3627 | See the Database SQL Language Reference for additi... |
| 2348 | 0.3627 | For Dell Isilon/PowerScale storage 8.2 and above, ... |
| 2349 | 0.3626 | Move the selected snapshots to the Snapshots avail... |
| 2350 | 0.3626 | See the Use Filters in Advanced Mode topic for add... |
| 2351 | 0.3626 | v10.7 Manage Data Sources You can fine-tune data c... |
| 2352 | 0.3625 | Helps find out who was trying to access your priva... |
| 2353 | 0.3625 | Scope Table 1: Option Description Monitor hidden s... |
| 2354 | 0.3625 | Same logic applies to the inclusion rules. Example... |
| 2355 | 0.3624 | Step 3 – Locate the InitialDescription parameter a... |
| 2356 | 0.3624 | • Advanced permissions—Select List folder / read d... |
| 2357 | 0.3623 | Consider the following: Specify monitoring restric... |
| 2358 | 0.3623 | You can adjust audit settings automatically. Your ... |
| 2359 | 0.3622 | logons), use the omitlogonlist.txt. Use the omitre... |
| 2360 | 0.3622 | Containers and Computers By default, Auditor will ... |
| 2361 | 0.3621 | Specify UNC path to the shared folder where user s... |
| 2362 | 0.3621 | Successful changes The Auditing Entry below shows ... |
| 2363 | 0.3621 | Step 1 – Log in to your CyberArk system. Step 2 – ... |
| 2364 | 0.3620 | You can also create lists of specific file shares ... |
| 2365 | 0.3620 | Tip for reading the table: For example, on the com... |
| 2366 | 0.3620 | Unless specified, the add-on runs with the current... |
| 2367 | 0.3618 | Specify an item name. Make sure to create a dedica... |
| 2368 | 0.3618 | Specify an item name. Make sure to create a dedica... |
| 2369 | 0.3617 | Enable integration Netwrix.ITSM.AlertsUploaderTool... |
| 2370 | 0.3616 | Export data When exporting large amount of data (e... |
| 2371 | 0.3616 | Account Lockout Examiner machine and the domain co... |
| 2372 | 0.3615 | Advanced permissions—Select List folder / read dat... |
| 2373 | 0.3615 | Data is written a remote on_for_HPE_ ArcSight.ps1 ... |
| 2374 | 0.3614 | The Remove changes window closes. Owners & Access ... |
| 2375 | 0.3614 | Table 1: Port Protocol Source Target Purpose 9004 ... |
| 2376 | 0.3614 | Possible parameter values: True — fill in the Even... |
| 2377 | 0.3614 | Possible parameter values: True — fill in the Even... |
| 2378 | 0.3614 | See the Configuring Your Dell Isilon/PowerScale Cl... |
| 2379 | 0.3613 | See the Integration API topic for additional infor... |
| 2380 | 0.3612 | For example, your DNS security parameters' changes... |
| 2381 | 0.3612 | Table 1: Option Description Accept List Address Sp... |
| 2382 | 0.3611 | For example, your network adapter configuration ch... |
| 2383 | 0.3610 | Configure audit settings Do not select the checkbo... |
| 2384 | 0.3610 | Equals (default) Netwrix Auditor supports the 2. N... |
| 2385 | 0.3609 | NOTE: Make sure that the AD Computer account for t... |
| 2386 | 0.3609 | Use an existing SQL Server instance — select this ... |
| 2387 | 0.3608 | Step 3 – Configure Audit Object Access Policy. Set... |
| 2388 | 0.3607 | Data will be collected using a set of triggers. Fo... |
| 2389 | 0.3607 | AB:BB:CC—Check Auditor Server certificat e thumbpr... |
| 2390 | 0.3607 | AB:BB:CC—Check Auditor Server certificat e thumbpr... |
| 2391 | 0.3607 | Check the required audit settings in your monitore... |
| 2392 | 0.3607 | Exclude—Add users to be excluded from the auditing... |
| 2393 | 0.3606 | Table 1: XML curl -H "Content-Type:application/xml... |
| 2394 | 0.3605 | Regular Environment Recommendations below refer to... |
| 2395 | 0.3605 | During the initial data collection, the product au... |
| 2396 | 0.3604 | Network Devices Cisco ASA Devices Auditor supports... |
| 2397 | 0.3604 | This role is granted to specialists who use the In... |
| 2398 | 0.3603 | ◦◦ The Advanced audit policy settings can be confi... |
| 2399 | 0.3603 | Only the latest snapshot is available for reportin... |
| 2400 | 0.3602 | You can create as many shortcuts with different pa... |
| 2401 | 0.3601 | v10.7 44.. Double-click CleanAutoBackupLogs. The E... |
| 2402 | 0.3600 | The wizard will start and ask the additional param... |
| 2403 | 0.3598 | For example, the Windows Firewall service stopped.... |
| 2404 | 0.3597 | Please note the following rebranding limitations a... |
| 2405 | 0.3596 | v10.7 You can also create lists of specific file s... |
| 2406 | 0.3596 | Instead, they will be managed by Netwrix Privilege... |
| 2407 | 0.3595 | Reports are sent according to a specified schedule... |
| 2408 | 0.3595 | Method Endpoint POST Data https://{host:port}/ net... |
| 2409 | 0.3593 | Applies to—Set to "This folder, subfolders and fil... |
| 2410 | 0.3593 | The role should be assigned to a very limited numb... |
| 2411 | 0.3593 | v10.7 Add MS Teams monitoring plan Follow the step... |
| 2412 | 0.3593 | Tip for reading the table: For example, on any mon... |
| 2413 | 0.3593 | It has dbo access to the configuration database. F... |
| 2414 | 0.3592 | v10.7 Option Description audit data. Note that the... |
| 2415 | 0.3591 | On the main Auditor page, navigate to Behavior Sub... |
| 2416 | 0.3591 | Step 1 – In Auditor, navigate to Search. Step 2 – ... |
| 2417 | 0.3590 | Select Monitor userdefined hidden shares if necess... |
| 2418 | 0.3589 | See the Antivirus Exclusions for Netwrix Auditor k... |
| 2419 | 0.3589 | See the Permissions for SharePoint Online Auditing... |
| 2420 | 0.3589 | At least the first script run should be performed ... |
| 2421 | 0.3589 | At least the first script run should be performed ... |
| 2422 | 0.3588 | To be able to audit and report v10.7 who made thos... |
| 2423 | 0.3588 | Allow outbound connections from the dynamic (1024 ... |
| 2424 | 0.3588 | Do not specify a default file share mapped to a lo... |
| 2425 | 0.3587 | Upon s electing Combination of file and share perm... |
| 2426 | 0.3587 | • Advanced permissions—Select List folder / read d... |
| 2427 | 0.3587 | Unless specified, the add-on runs with the current... |
| 2428 | 0.3586 | parameter, it cannot be replaced omitcollectlist.t... |
| 2429 | 0.3586 | The list of Exchange object classes is version-dep... |
| 2430 | 0.3585 | In the Maximum security log size Properties dialog... |
| 2431 | 0.3585 | For example: ◦ "\\domain\dfsnamespace\" (domain-ba... |
| 2432 | 0.3585 | It means that data collection from at least one en... |
| 2433 | 0.3585 | It means that data collection from at least one en... |
| 2434 | 0.3585 | See the Integration API topic for additional infor... |
| 2435 | 0.3584 | You can automate this process, as described in the... |
| 2436 | 0.3583 | To collect data from Windows Failover Cluster, net... |
| 2437 | 0.3580 | Step 5 – Complete the Event Filters wizard. Comple... |
| 2438 | 0.3580 | Execute the following command: Get-MailboxDatabase... |
| 2439 | 0.3580 | For example, account.corp.lab Access Zone Enter th... |
| 2440 | 0.3577 | This account must be included in the following gro... |
| 2441 | 0.3576 | Table 2: Format Example XML <?xml version="1.0" en... |
| 2442 | 0.3575 | See the State–In–Time Reports topic for a dditiona... |
| 2443 | 0.3575 | See the State–In–Time Reports topic for a dditiona... |
| 2444 | 0.3575 | Password Enter a password for SMTP authentication.... |
| 2445 | 0.3574 | The log is available on Windows Server 2012 R2 and... |
| 2446 | 0.3574 | 11.. On the DHCP server, navigate to Event Viewer.... |
| 2447 | 0.3574 | • NOCHECK—Do not check the certificate. Make sure ... |
| 2448 | 0.3573 | It displays currently triggered alerts with detail... |
| 2449 | 0.3573 | You can use server name or IP address, for example... |
| 2450 | 0.3573 | See the Prerequisites and Audit Database topics fo... |
| 2451 | 0.3569 | Name and Location Select a name for the new virtua... |
| 2452 | 0.3568 | A custom account must be granted the same permissi... |
| 2453 | 0.3568 | See the Add Account to the Organization Management... |
| 2454 | 0.3567 | Soft-deleted items are Admin moved to the Recovera... |
| 2455 | 0.3567 | SharePoint I want to exclude the domain\nwxservice... |
| 2456 | 0.3567 | For the User Password Changes report to function p... |
| 2457 | 0.3567 | Table 1: Hardware component Evaluation, PoC or sta... |
| 2458 | 0.3564 | Automate Add-On Execution To ensure you feed the m... |
| 2459 | 0.3564 | SharePoint Farm As a Auditor Administrator I want ... |
| 2460 | 0.3563 | Provide a different password if necessary. v10.7 P... |
| 2461 | 0.3562 | To disable Activity Summary Emails, you need to di... |
| 2462 | 0.3561 | For example: list/document.docx http(s)://URL Ente... |
| 2463 | 0.3559 | Pay attention to the "Data categories" column in s... |
| 2464 | 0.3558 | See the procedure below for details. NOTE: In this... |
| 2465 | 0.3558 | See the procedure below for details. NOTE: In this... |
| 2466 | 0.3558 | View and Search Collected Data how to apply filter... |
| 2467 | 0.3558 | In the latter case, make sure the directory exists... |
| 2468 | 0.3558 | Table 1: To... Execute... Disable API APIAdminTool... |
| 2469 | 0.3551 | Execute... AUDIT SELECT,INSERT,DELETE,UPDATE,RENAM... |
| 2470 | 0.3550 | RECOMMENDED: Netwrix recommends reviewing your cur... |
| 2471 | 0.3550 | Access MS Teams Using Modern Authentication This o... |
| 2472 | 0.3550 | NOTE: In some scenarios multi-factor authenticatio... |
| 2473 | 0.3550 | NetwrixAuditorCertificateThumbpr int NOCHECK Audit... |
| 2474 | 0.3549 | Note that the new monitoring scope restrictions ap... |
| 2475 | 0.3549 | Step 5 – Continue retrieving Activity Records. Sen... |
| 2476 | 0.3549 | This codec is installed automatically on the compu... |
| 2477 | 0.3548 | This helps you keep track of all changes in your I... |
| 2478 | 0.3547 | See the Data Collecting Account topic for User/Pas... |
| 2479 | 0.3546 | By default, set to zero offse t (UTC). Define a cu... |
| 2480 | 0.3546 | If any conflicts are detected with your current au... |
| 2481 | 0.3544 | HEALTH STATUS Opens the Health Status dashboard, w... |
| 2482 | 0.3543 | You will also need to configure Exchange Administr... |
| 2483 | 0.3543 | If you want the add-on to use another account to c... |
| 2484 | 0.3543 | Microsoft Entra ID applications can be assigned De... |
| 2485 | 0.3543 | Microsoft Entra ID applications can be assigned De... |
| 2486 | 0.3543 | BatchTimeOut Defines batch writing timeout (in sec... |
| 2487 | 0.3542 | Review details and play a video by clicking the Sh... |
| 2488 | 0.3541 | Step 5 – Navigate to File → Connect Network Regist... |
| 2489 | 0.3541 | Application that initiated the activity — enter th... |
| 2490 | 0.3541 | ps1 -OutputFolder C:\CEF_Export - NetwrixAuditorHo... |
| 2491 | 0.3541 | Table 1: On... Ensure that... The Auditor Server s... |
| 2492 | 0.3540 | Configure Scope how to narrow your monitoring scop... |
| 2493 | 0.3539 | If you set the Who filter to does not contain John... |
| 2494 | 0.3539 | For input Activity Records, the data source is aut... |
| 2495 | 0.3538 | will not be monitored. See the topics on the monit... |
| 2496 | 0.3538 | Method Endpoint POST Data https://{host:port}/ net... |
| 2497 | 0.3537 | For SSRS-based reports - verify that SSRS (SQL Ser... |
| 2498 | 0.3537 | Step 5 – Click on the arrow button next to any of ... |
| 2499 | 0.3536 | For example, "MyOracle". Wallet alias Alias name i... |
| 2500 | 0.3535 | Make Reports Handy In addition to reviewing report... |
| 2501 | 0.3533 | In this case, Auditor will v10.7 Option Descriptio... |
| 2502 | 0.3531 | By default, the report includes data obtained duri... |
| 2503 | 0.3531 | By default, the report includes data obtained duri... |
| 2504 | 0.3530 | Enter: Application ID; Application secret. ◦◦ See ... |
| 2505 | 0.3530 | Enter: Application ID; Application secret. ◦◦ See ... |
| 2506 | 0.3530 | Mark all as reviewed – Click to mark all alerts in... |
| 2507 | 0.3529 | All members of the local Administrators group are ... |
| 2508 | 0.3529 | For that, review the following procedures: Configu... |
| 2509 | 0.3528 | Instead, they will be managed by Netwrix Privilege... |
| 2510 | 0.3528 | Parameter Default value Description NetwrixIntegra... |
| 2511 | 0.3528 | Step 1 – Click Update. Step 2 – In the dialog that... |
| 2512 | 0.3525 | Configure Data Collecting Account, as described in... |
| 2513 | 0.3525 | Your current audit settings will be checked on eac... |
| 2514 | 0.3524 | • Make sure that the Only apply these auditing set... |
| 2515 | 0.3523 | Supported Data Sources Configure Auditor service a... |
| 2516 | 0.3523 | Unless specified, the add-on runs with the current... |
| 2517 | 0.3523 | Unless specified, the add-on runs with the current... |
| 2518 | 0.3522 | Take action Click the Details link to examine the ... |
| 2519 | 0.3519 | v10.7 Option Description Select this checkbox if y... |
| 2520 | 0.3519 | If you want to run the add-on on another machine, ... |
| 2521 | 0.3518 | Configuration parameters to specify in settings.xm... |
| 2522 | 0.3518 | Table 1: Option Description Example All Data Selec... |
| 2523 | 0.3517 | Configure Dell Isilon/PowerScale Cluster in Normal... |
| 2524 | 0.3516 | Authentication Select the authentication type you ... |
| 2525 | 0.3516 | • The servers within the farm are located in diffe... |
| 2526 | 0.3515 | If you want the add-on to use another account to c... |
| 2527 | 0.3514 | SqlLogon — Successful logon attempt made through S... |
| 2528 | 0.3514 | Open a web browser and type the Report Manager URL... |
| 2529 | 0.3513 | Thus, s/he configures the product not to monitor t... |
| 2530 | 0.3512 | v10.7 Create a Group Policy to Deploy Netwrix Audi... |
| 2531 | 0.3512 | See also: Enterprise Overview Dashboard All Activi... |
| 2532 | 0.3511 | Configure Audit Database Account This is the accou... |
| 2533 | 0.3509 | If you want to run the add-on on another machine, ... |
| 2534 | 0.3508 | The newly created data source will appear in the D... |
| 2535 | 0.3508 | Not in group This operator relates to the Who filt... |
| 2536 | 0.3507 | When configuring the IncludeDataSourceToMakeEventI... |
| 2537 | 0.3507 | Item— name of the SQL Server instance monitored wi... |
| 2538 | 0.3506 | Specify Nutanix File Server If you need to audit a... |
| 2539 | 0.3506 | Table 1: To... Execute the command... Apply audit ... |
| 2540 | 0.3504 | Unless specified, the script runs with the current... |
| 2541 | 0.3504 | Step 2 – Select Netwrix Privilege Secure. Step 3 –... |
| 2542 | 0.3502 | The Activity Records have the format similar to th... |
| 2543 | 0.3502 | See the Deploy the Service topic for additional in... |
| 2544 | 0.3502 | NetwrixAuditorEndpoint https://localhost:9699/netw... |
| 2545 | 0.3502 | By default, the report includes data obtained duri... |
| 2546 | 0.3501 | v10.7 After creating a task, wait for the next sch... |
| 2547 | 0.3501 | Step 4 – Hit Enter. Depending on the number of Act... |
| 2548 | 0.3501 | If the configuration is correct, you will see the ... |
| 2549 | 0.3500 | Subscribe to a report On the main Auditor page, na... |
| 2550 | 0.3499 | You can use * for cmdlets and their parameters. Li... |
| 2551 | 0.3498 | .Net Framework 4.7.2 and above is installed. Revie... |
| 2552 | 0.3498 | The IT risks are grouped into the following catego... |
| 2553 | 0.3498 | Table 1: Issue Reason and solution Monitoring Plan... |
| 2554 | 0.3496 | Specify custom connection parameters Make sure thi... |
| 2555 | 0.3495 | Data is written a remote ArcSight through UDP prot... |
| 2556 | 0.3495 | Optionally, you can select Download to edit the ma... |
| 2557 | 0.3494 | Click Configure to specify the import scope. Optio... |
| 2558 | 0.3494 | See the Behavior Anomalies topic for additional in... |
| 2559 | 0.3494 | If network traffic compression will be disabled, a... |
| 2560 | 0.3494 | Netwrix Privilege Secure is ready to use as an acc... |
| 2561 | 0.3494 | File Description Syntax Contains a list of account... |
| 2562 | 0.3494 | A custom account must be granted the same permissi... |
| 2563 | 0.3493 | Download and install Netwrix Auditor on that machi... |
| 2564 | 0.3493 | SqlLogon — Successful logon attempt made through S... |
| 2565 | 0.3491 | Netwrix gathers the following information about MS... |
| 2566 | 0.3488 | Alternatively, you can grant the Global administra... |
| 2567 | 0.3488 | Alternatively, you can grant the Global administra... |
| 2568 | 0.3488 | Specify the Audit Database retention period. This ... |
| 2569 | 0.3488 | Do one of the following: To configure HPE Aruba de... |
| 2570 | 0.3487 | Before running or scheduling the add-on, you shoul... |
| 2571 | 0.3486 | omitscreadaccesslist.txt Contains a list of site c... |
| 2572 | 0.3486 | Tip for reading the table: For example, on the com... |
| 2573 | 0.3486 | As a next step, click Add item to specify an objec... |
| 2574 | 0.3485 | For more details about gMSA usage, see the Use Gro... |
| 2575 | 0.3485 | For more details about gMSA usage, see the Use Gro... |
| 2576 | 0.3484 | See the Add Items for Monitoring topic for additio... |
| 2577 | 0.3483 | Step 5 – On the Destination Folder step, specify t... |
| 2578 | 0.3480 | All Users Used for previous values in users Activi... |
| 2579 | 0.3479 | For example, if you selected Services, the program... |
| 2580 | 0.3479 | Step 3 – Adjust the security event log size and re... |
| 2581 | 0.3479 | Select Monitor userdefined hidden shares if necess... |
| 2582 | 0.3479 | Current data should be stored in other access zone... |
| 2583 | 0.3477 | Using Modern Authentication with SharePoint Online... |
| 2584 | 0.3477 | Step 1 – Open Nutanix Prism web portal. Step 2 – S... |
| 2585 | 0.3476 | Usage example Database administrators need to disc... |
| 2586 | 0.3475 | v10.7 Option Description Example Select if you wan... |
| 2587 | 0.3475 | v10.7 Option Description Example Select if you wan... |
| 2588 | 0.3475 | See the Manage Data Sources topic for additional i... |
| 2589 | 0.3475 | On the add-on installation server, the administrat... |
| 2590 | 0.3474 | ALTER SYSTEM SET audit_trail=DB SCOPE=SPFILE; Stor... |
| 2591 | 0.3473 | SQL Server Ports Review a full list of protocols a... |
| 2592 | 0.3472 | Helps find out who was trying to access your priva... |
| 2593 | 0.3472 | Execute... Database audit trail (default setting) ... |
| 2594 | 0.3471 | v10.7 Do.. Recommended use This is helpful when yo... |
| 2595 | 0.3471 | Table 1: Auditing Entry Failed change attempts The... |
| 2596 | 0.3471 | All diagrams provide the drill-down functionality,... |
| 2597 | 0.3471 | If enabled, a Compression Service will be automati... |
| 2598 | 0.3470 | If you want to run the add-on on another machine, ... |
| 2599 | 0.3469 | For XML audit trail: Only ALTER actions will be re... |
| 2600 | 0.3467 | You can specify custom delivery time and frequency... |
| 2601 | 0.3467 | Data Collection Accounts should meet the following... |
| 2602 | 0.3466 | OR ◦◦ Modern authentication has ever been selected... |
| 2603 | 0.3466 | Default prefix is NA, for example:NA Windows Serve... |
| 2604 | 0.3465 | Password Enter a password for SMTP authentication.... |
| 2605 | 0.3465 | ◦◦ The following advanced audit policy settings mu... |
| 2606 | 0.3464 | Symbol XML entity & &amp; e.g., Ally & Sons e.g., ... |
| 2607 | 0.3463 | Virtual Deployment Overview In addition to on-prem... |
| 2608 | 0.3463 | contain John, you will exclude the Does not contai... |
| 2609 | 0.3461 | If enabled, a Compression Service will be automati... |
| 2610 | 0.3461 | If enabled, a Compression Service will be automati... |
| 2611 | 0.3459 | Select one of the custom reports in the list and r... |
| 2612 | 0.3459 | Under Permissions, select all checkboxes except th... |
| 2613 | 0.3458 | See the Integration API topic for additional infor... |
| 2614 | 0.3458 | See the Prerequisites and Audit Database topics fo... |
| 2615 | 0.3458 | Prerequisites Before running the add-on, ensure th... |
| 2616 | 0.3456 | For more information on this deployment option, re... |
| 2617 | 0.3456 | Helps find out who was trying to access your priva... |
| 2618 | 0.3455 | Automate Add-On Execution To ensure you feed the m... |
| 2619 | 0.3455 | The add-on exports Activity Records from a remote ... |
| 2620 | 0.3455 | Make sure this account is granted the Content Mana... |
| 2621 | 0.3455 | You can also create lists of specific file shares ... |
| 2622 | 0.3454 | Table 2: Port Protocol Source Target Purpose 389 T... |
| 2623 | 0.3453 | Password – Provide password for this account. Summ... |
| 2624 | 0.3453 | You can append other options, such as n to hide th... |
| 2625 | 0.3453 | Windows Installer 3.1 and Windows Installer 3.1 an... |
| 2626 | 0.3452 | When configuring the IncludeDataSourceToMakeEventI... |
| 2627 | 0.3451 | In this case audit data is ,*,*,Scheduled still be... |
| 2628 | 0.3451 | Step 4 – Click New Rule. In the New Inbound Rule w... |
| 2629 | 0.3450 | See the Audit Configuration Assistant topic for in... |
| 2630 | 0.3450 | Step 2 – Navigate to Security Settings > Local Pol... |
| 2631 | 0.3447 | You can get add-ons within the product. To do so, ... |
| 2632 | 0.3447 | Check that your data collecting account has all re... |
| 2633 | 0.3446 | If enabled, a Compression Service will be automati... |
| 2634 | 0.3446 | If enabled, a Compression Service will be automati... |
| 2635 | 0.3445 | The list contains computer name, its current statu... |
| 2636 | 0.3445 | You can enable network traffic compression. If Spe... |
| 2637 | 0.3445 | Step 1 – On the audited server, open the Local Sec... |
| 2638 | 0.3445 | See the Change and Activity Reports topic for addi... |
| 2639 | 0.3444 | Step 2 – When adding a cluster file server for aud... |
| 2640 | 0.3443 | Allow outbound connections to the remote ports on ... |
| 2641 | 0.3442 | Data communication is performed using TCP protocol... |
| 2642 | 0.3440 | See Assigning 'System Administrator' Role section ... |
| 2643 | 0.3440 | The following table lists actions that can be perf... |
| 2644 | 0.3439 | Failed read attempts v10.7 Auditing Entry Type—Set... |
| 2645 | 0.3439 | To change the add-on logging level, use the LogLev... |
| 2646 | 0.3439 | The credentials are case sensitive. Specify the ac... |
| 2647 | 0.3438 | Step 4 – Enable auditing: 11.. On the Volumes tab,... |
| 2648 | 0.3438 | See the State–In–Time Reports topic for additional... |
| 2649 | 0.3438 | See the View Reports topic for additional informat... |
| 2650 | 0.3438 | Step 1 – Select an alert from the list and enable ... |
| 2651 | 0.3436 | Make sure to create a dedicated item in Auditor in... |
| 2652 | 0.3436 | See the Prerequisites and Audit Database topics fo... |
| 2653 | 0.3435 | -NetwrixAuditorHost 172.28.6.15 -NetwrixAuditorUse... |
| 2654 | 0.3434 | Enter: Application ID; Application secret. ◦◦ See ... |
| 2655 | 0.3434 | Step 1 – In Auditor client, click Settings > Long-... |
| 2656 | 0.3434 | 126"} Retrieves all activity records where adminis... |
| 2657 | 0.3432 | For bigger SharePoint farms, consider up to 10 min... |
| 2658 | 0.3431 | Step 2 – Start Windows PowerShell and specify a pa... |
| 2659 | 0.3430 | Run the fs list command in ncli to get the list of... |
| 2660 | 0.3430 | Possible parameter values: True — fill in the Even... |
| 2661 | 0.3428 | In the Filter by organizational unit dialog that o... |
| 2662 | 0.3427 | If you later clear this option to start saving dat... |
| 2663 | 0.3427 | Table 1: Port Protocol Source Target Purpose 443 T... |
| 2664 | 0.3426 | The add-on will operate as a Syslog listener for N... |
| 2665 | 0.3425 | You should specify only the account name in the do... |
| 2666 | 0.3425 | Also, remember to do the following: Configure Data... |
| 2667 | 0.3425 | You can enable Auditor to continually enforce the ... |
| 2668 | 0.3425 | Helps Failed identify potential intruders who trie... |
| 2669 | 0.3424 | Configure Syslog Message Forwarding in CyberArk On... |
| 2670 | 0.3423 | If you want to run the add-on on another machine, ... |
| 2671 | 0.3421 | Column omitpathlist.txt Specify the resource paths... |
| 2672 | 0.3421 | Configure ONTAPI\RESTAPI Web Access Netwrix Audito... |
| 2673 | 0.3419 | Data is collected from a remote RADIUS server with... |
| 2674 | 0.3419 | Execute the following command: Add-SPShellAdmin –U... |
| 2675 | 0.3419 | Follow the steps to configure syslog forwarding. S... |
| 2676 | 0.3417 | Enter local user account name and password, then c... |
| 2677 | 0.3416 | Events collected from any other source will be ign... |
| 2678 | 0.3415 | For example, dsacls "CN=Deleted Objects,DC=Corp,DC... |
| 2679 | 0.3414 | Users not included in this list will not be notifi... |
| 2680 | 0.3414 | See the Assign Permission To Read the Registry Key... |
| 2681 | 0.3414 | Alternatively, you can grant the Global administra... |
| 2682 | 0.3413 | Microsoft System Center Virtual Machine Manager SC... |
| 2683 | 0.3412 | v10.7 Option Description Create rules for objects ... |
| 2684 | 0.3411 | Follow the steps to define the Log On As a Service... |
| 2685 | 0.3409 | cluster1::> vserver services web access show -name... |
| 2686 | 0.3408 | v10.7 Apply a gMSA as a Data Collecting Account Ap... |
| 2687 | 0.3408 | (not displayed) The data source status is unknown.... |
| 2688 | 0.3407 | Table 1: Option Description The Event tab Name Spe... |
| 2689 | 0.3405 | For that, under Specify monitoring restrictions, s... |
| 2690 | 0.3402 | • Applies to—Set to "This folder, subfolders and f... |
| 2691 | 0.3402 | ◦◦ Create a shared directory /ifs/.ifsvar/audit/ o... |
| 2692 | 0.3402 | Clicking the second link opens a dashboard that li... |
| 2693 | 0.3401 | The default name for the original database was Net... |
| 2694 | 0.3401 | Collect activity data Any of the following roles: ... |
| 2695 | 0.3400 | Write to/Don't write to Select the location to wri... |
| 2696 | 0.3400 | Prerequisites Before running the add-on, ensure th... |
| 2697 | 0.3400 | In addition to the restrictions for a monitoring p... |
| 2698 | 0.3400 | If the retention period is set to 0, the following... |
| 2699 | 0.3400 | See the Assign Permission to Read the Registry Key... |
| 2700 | 0.3400 | Enterprise Overview—A dashboard with a set of widg... |
| 2701 | 0.3399 | If you have an on-premises Exchange server 2019, 2... |
| 2702 | 0.3397 | However, in some cases, organizations need to prov... |
| 2703 | 0.3395 | /q Specify the user interface (UI) that displays d... |
| 2704 | 0.3393 | See the Reports topic for additional information. ... |
| 2705 | 0.3391 | Table 1: On... Ensure that... The Auditor server s... |
| 2706 | 0.3390 | Add / Remove Programs Installed For** Add or Remov... |
| 2707 | 0.3389 | Sensitive Files Count by Source This report shows ... |
| 2708 | 0.3388 | For example, you can run the add-on on the compute... |
| 2709 | 0.3385 | ForNDC Endpoint Provider: Browse your data with Ne... |
| 2710 | 0.3385 | Step 7 – Select Server roles on the left and assig... |
| 2711 | 0.3384 | Table 1: On... Ensure that... The Auditor server s... |
| 2712 | 0.3384 | Follow the steps to review and update global Audit... |
| 2713 | 0.3383 | Prerequisites Before running the add-on, ensure th... |
| 2714 | 0.3382 | Database retention Configure retention if you want... |
| 2715 | 0.3382 | Step 1 – On the computer where Auditor Server resi... |
| 2716 | 0.3381 | Table 1: File name Description install.ps1 PowerSh... |
| 2717 | 0.3381 | Examples: *admin*@corp.com */Drafts - exclude Draf... |
| 2718 | 0.3381 | To review currently applied capabilities, you can ... |
| 2719 | 0.3380 | Table 1: Option Description Applications Specify a... |
| 2720 | 0.3379 | When a new object is added, Auditor does not show ... |
| 2721 | 0.3377 | It is located in the installation directory: ...\N... |
| 2722 | 0.3377 | Monitor Oracle Database logon activity Specify wha... |
| 2723 | 0.3377 | NOTE: The template remains the same for all alerts... |
| 2724 | 0.3376 | See the Create a New Monitoring Plan topic for add... |
| 2725 | 0.3376 | 22.. Connect to your Oracle Database—use Oracle ac... |
| 2726 | 0.3375 | Sub-element: Name. The item type is added inside t... |
| 2727 | 0.3375 | You can add any elements (a dashboard, report, ale... |
| 2728 | 0.3374 | Ensure that... Set-ExecutionPolicy Unrestricted Th... |
| 2729 | 0.3374 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 2730 | 0.3373 | In the Schedule state-in-time data collection sect... |
| 2731 | 0.3372 | All filters are applied using AND logic. v10.7 Opt... |
| 2732 | 0.3371 | See the Monitoring Planstopic for additional infor... |
| 2733 | 0.3371 | Remember, when auditing SQL Server availability on... |
| 2734 | 0.3370 | The newly created data source will appear in the D... |
| 2735 | 0.3369 | A custom account must be granted the same permissi... |
| 2736 | 0.3368 | As a Auditor administrator I want to exclude the d... |
| 2737 | 0.3368 | Failed change attempts The Auditing Entry below sh... |
| 2738 | 0.3367 | Follow the steps to configure settings for other l... |
| 2739 | 0.3366 | To upgrade the Access Reviews application to a new... |
| 2740 | 0.3365 | Monitoring Plan Summary At this step of the wizard... |
| 2741 | 0.3365 | See the Role-Based Access and Delegation topic for... |
| 2742 | 0.3364 | To specify a non-default port, provide a server na... |
| 2743 | 0.3364 | To specify a non-default port, provide a server na... |
| 2744 | 0.3364 | Failed read attempts The Auditing Entry below show... |
| 2745 | 0.3364 | • File server helpdesk personnel have access to a ... |
| 2746 | 0.3362 | Subscriptions Opens the Subscriptions wizard, whic... |
| 2747 | 0.3362 | Configure the Event Log Size Using Group Policy Pe... |
| 2748 | 0.3361 | v10.7 Prerequisites Before running the add-on, ens... |
| 2749 | 0.3360 | Step 2 – Complete the fields. Review the following... |
| 2750 | 0.3359 | ExcludedCmdlets *-InboxRule, *-MailboxAutoReplyCon... |
| 2751 | 0.3359 | In the dialog that opens, specify the groups that ... |
| 2752 | 0.3358 | Table 1: This tile shows the current number of use... |
| 2753 | 0.3356 | Configure Auditor service accounts. Software Requi... |
| 2754 | 0.3353 | Every time you run a script, Auditor makes a check... |
| 2755 | 0.3352 | v10.7 Parameter Default value Description naplanit... |
| 2756 | 0.3351 | Netwrix recommends assigning a unique identificato... |
| 2757 | 0.3351 | Then you will provide this account in the monitori... |
| 2758 | 0.3350 | Helps Failed identify potential intruders who trie... |
| 2759 | 0.3350 | If you need a data source that is not listed on th... |
| 2760 | 0.3350 | For production deployment planning in bigger envir... |
| 2761 | 0.3350 | RECOMMENDED: For security reasons, enable only SSL... |
| 2762 | 0.3348 | Step 5 – In the Manage Snapshots window, select th... |
| 2763 | 0.3347 | - SSD Table 1: Hardware component Requirement Proc... |
| 2764 | 0.3346 | Exchange_Server.Adminis trativeGroup Exchange_Serv... |
| 2765 | 0.3346 | Step 2 – Select the log you need. Step 3 – Edit Sp... |
| 2766 | 0.3346 | Prerequisites Before running the add-on, ensure th... |
| 2767 | 0.3345 | Object type:property: When a new object is added, ... |
| 2768 | 0.3343 | v10.7 Option Description your current audit settin... |
| 2769 | 0.3342 | v10.7 Configure Advanced Audit Policies Configure ... |
| 2770 | 0.3341 | Microsoft Entra ID monitoring plan has been added ... |
| 2771 | 0.3341 | Default is Priority 3 — Normal Response. Table 2: ... |
| 2772 | 0.3340 | All filters are applied using AND logic. See the F... |
| 2773 | 0.3340 | Depending on the execution scenario you choose, yo... |
| 2774 | 0.3340 | Step 6 – Select what type of data you want to excl... |
| 2775 | 0.3340 | Step 6 – Select what type of data you want to excl... |
| 2776 | 0.3338 | See the MS Teams topic for additional information.... |
| 2777 | 0.3337 | You should specify only the account name in the do... |
| 2778 | 0.3336 | Currently, the Windows Server State-in-Time report... |
| 2779 | 0.3335 | The procedure below provides a possible way to spe... |
| 2780 | 0.3335 | A custom account must be granted the same permissi... |
| 2781 | 0.3335 | NOTE: You can specify any other user group, but in... |
| 2782 | 0.3335 | IP Address — server IP address. Port— port for inc... |
| 2783 | 0.3335 | This instance is included in the monitoring plan n... |
| 2784 | 0.3335 | For example, you can run the add-on on the compute... |
| 2785 | 0.3334 | Subscription emails may vary slightly depending on... |
| 2786 | 0.3331 | You can write RESTful requests using any tool or a... |
| 2787 | 0.3330 | NOTE: If you are using a gMSA account for Active D... |
| 2788 | 0.3330 | and modifying attributes of these objects (listed ... |
| 2789 | 0.3329 | Table 1: On... Ensure that... The Auditor side • A... |
| 2790 | 0.3328 | For example: -file "C:\Addons\Netwrix_Auditor_Addo... |
| 2791 | 0.3327 | See the State–In–Time Reports topic for additional... |
| 2792 | 0.3323 | Step 3 – Configure basic parameters as follows: En... |
| 2793 | 0.3321 | You should specify only the account name in the do... |
| 2794 | 0.3321 | You should specify only the account name in the do... |
| 2795 | 0.3320 | Specify what types of logon events you want to mon... |
| 2796 | 0.3320 | Helps identify potential intruders who tried to mo... |
| 2797 | 0.3319 | v10.7 Step 6 – In the dialog that opens, locate Ne... |
| 2798 | 0.3318 | AccessInformationCenter.Service.e xe Located in th... |
| 2799 | 0.3318 | You can enable network traffic compression. If ena... |
| 2800 | 0.3318 | You can enable network traffic compression. If ena... |
| 2801 | 0.3316 | If you want to generate reports based on differen ... |
| 2802 | 0.3316 | DOMAIN\username agentomitusers.txt This file conta... |
| 2803 | 0.3315 | See Import Audit Data with the Database Importer f... |
| 2804 | 0.3313 | You can skip or define parameters depending on you... |
| 2805 | 0.3313 | Password Enter a password. Table 2: Option Descrip... |
| 2806 | 0.3312 | See the Monitoring Planstopic for additional infor... |
| 2807 | 0.3310 | v10.7 Notes for Managed Service Providers Being a ... |
| 2808 | 0.3309 | RID is included in output A ctivity Records only. ... |
| 2809 | 0.3308 | Auditor Endpoint Assumes that the add-on runs on t... |
| 2810 | 0.3308 | v10.7 String Description String5 The GUID of the m... |
| 2811 | 0.3307 | Users can also configure Only the latest snapshot ... |
| 2812 | 0.3307 | Users can also configure Only the latest snapshot ... |
| 2813 | 0.3307 | • The user running the script must be a member of ... |
| 2814 | 0.3306 | Enable Secondary Logon Service Follow the steps to... |
| 2815 | 0.3306 | The product updates the latest snapshot on the reg... |
| 2816 | 0.3303 | Table 2: Option Description Specify account which ... |
| 2817 | 0.3301 | Do not specify a default file share mapped to a lo... |
| 2818 | 0.3300 | settings.xml Contains parameters for the add-on se... |
| 2819 | 0.3300 | Use semicolon to separate several addresses. Monit... |
| 2820 | 0.3300 | This permission should be assigned on each domain ... |
| 2821 | 0.3300 | RID is included in output A ctivity Records only. ... |
| 2822 | 0.3299 | Then you will provide this account in the monitori... |
| 2823 | 0.3299 | Specify restriction filters to narrow your monitor... |
| 2824 | 0.3299 | Then you will provide this account in the monitori... |
| 2825 | 0.3298 | QueueSizeLimit 100 Specifies the maximum number of... |
| 2826 | 0.3298 | Troubleshoot SharePoint Auditing Problem Descripti... |
| 2827 | 0.3297 | NotEqualTo Max length: 255. StartsWith EndsWith Li... |
| 2828 | 0.3296 | Table 1: Description Failed Use this option to det... |
| 2829 | 0.3296 | Step 2 – Configure Syslog message forwarding in Cy... |
| 2830 | 0.3296 | This is the initial product installation. Requirem... |
| 2831 | 0.3296 | See the Prerequisites and Audit Database topics fo... |
| 2832 | 0.3295 | For example: OracleUser as sysdba Table 1: To moni... |
| 2833 | 0.3294 | Step 1 – Download the distribution package Netwrix... |
| 2834 | 0.3293 | SonicWall Devices Review a full list of object typ... |
| 2835 | 0.3293 | Users can also configure Only the latest snapshot ... |
| 2836 | 0.3292 | Table 1: Successful changes 1 Failed change attemp... |
| 2837 | 0.3292 | Manually, as described in the corresponding topics... |
| 2838 | 0.3292 | Multiple occurrences of a ction sets may indicate ... |
| 2839 | 0.3291 | To adjust your Security event log size and retenti... |
| 2840 | 0.3290 | See the following Microsoft article for additional... |
| 2841 | 0.3289 | This instance is included in the monitoring plan n... |
| 2842 | 0.3289 | Helps identify who accessed important files beside... |
| 2843 | 0.3288 | See the Add Items for Monitoring topic for additio... |
| 2844 | 0.3287 | Unless specified, the add-on runs with the current... |
| 2845 | 0.3287 | Step 5 – Review the account configuration scope an... |
| 2846 | 0.3287 | See the Health Status Dashboard topic for addition... |
| 2847 | 0.3287 | For that, execute: GRANT DBA TO <account_name>; Fo... |
| 2848 | 0.3286 | Make sure that theOnly apply these auditing settin... |
| 2849 | 0.3286 | The newly created data source will appear in the D... |
| 2850 | 0.3286 | User type userType Example: "Member" A string valu... |
| 2851 | 0.3286 | This account should have the following minimal rig... |
| 2852 | 0.3285 | To add users to the list, click Add and provide us... |
| 2853 | 0.3285 | See the Integration API topic for additional infor... |
| 2854 | 0.3285 | Wildcards (*) are not supported. In addition to th... |
| 2855 | 0.3282 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} • (... |
| 2856 | 0.3281 | Thus, s/he configures the product not to monitor t... |
| 2857 | 0.3281 | This data can help you to assess the activity reco... |
| 2858 | 0.3281 | Select the event types that you want to be save. I... |
| 2859 | 0.3279 | Copy it to a safe location. See the following Micr... |
| 2860 | 0.3278 | • Advanced permissions: ◦ Create files / write dat... |
| 2861 | 0.3278 | For example: ,sqlserver1.corp.local, Access is den... |
| 2862 | 0.3276 | See the Notifications Page topic for additional in... |
| 2863 | 0.3275 | Depending on Error the error code, the response bo... |
| 2864 | 0.3275 | Password – Provide a password for that account Ena... |
| 2865 | 0.3275 | Under Permissions, select all checkboxes except th... |
| 2866 | 0.3274 | You are trying to connect to a remote Auditor spec... |
| 2867 | 0.3274 | Step 10 – Type repadmin /syncall command and press... |
| 2868 | 0.3273 | Select the Security tab and click Advanced. In the... |
| 2869 | 0.3273 | See the Role-Based Access and Delegation topic for... |
| 2870 | 0.3272 | I see a blank window instead of a report. Contact ... |
| 2871 | 0.3272 | For example: http:// webApplication1:3333/ SharePo... |
| 2872 | 0.3270 | v10.7 File Description Syntax Use the omitlogonlis... |
| 2873 | 0.3269 | Make sure that the Only apply these auditing setti... |
| 2874 | 0.3268 | JSON: [0x00007FFDCC06BBC8,0x00007FFDB99EF4BA; 0x00... |
| 2875 | 0.3268 | The newly created data source will appear in the D... |
| 2876 | 0.3266 | Synology Ports Review a full list of protocols and... |
| 2877 | 0.3266 | Successful Enabling this option on public shares w... |
| 2878 | 0.3266 | A scope can be limited to a single monitoring plan... |
| 2879 | 0.3265 | v10.7 Type—Set to "Fail". Applies to—Set to "This ... |
| 2880 | 0.3265 | For example, an unknown user was added to the Admi... |
| 2881 | 0.3265 | Review your data source settings and click Add to ... |
| 2882 | 0.3265 | Review your data source settings and click Add to ... |
| 2883 | 0.3265 | Review your data source settings and click Add to ... |
| 2884 | 0.3265 | This report shows ownership of files and folders t... |
| 2885 | 0.3263 | v10.7 For example, if you selected the 'Enable Sta... |
| 2886 | 0.3263 | Example: System Properties*. You can use a wildcar... |
| 2887 | 0.3263 | Example: System Properties*. You can use a wildcar... |
| 2888 | 0.3262 | AD Container I want to exclude specific computers ... |
| 2889 | 0.3261 | In this case the "Who", "Workstation" and "When" v... |
| 2890 | 0.3260 | Enable network traffic compression If selected, th... |
| 2891 | 0.3260 | User/password – Provide a username and password fo... |
| 2892 | 0.3259 | Path *OU=OUNAME* For example: If the OU is "sample... |
| 2893 | 0.3259 | Normally contains information specific to your dat... |
| 2894 | 0.3258 | object type:property: When an object is deleted, A... |
| 2895 | 0.3258 | v10.7 Adjust Active Directory Tombstone Lifetime (... |
| 2896 | 0.3258 | Allow outbound connections to remote ports on the ... |
| 2897 | 0.3257 | Then click OK to confirm. Assigned resource owners... |
| 2898 | 0.3257 | Prerequisites Before running the add-on, ensure th... |
| 2899 | 0.3257 | omitarlist.txt SELECT statements auditing and SQL ... |
| 2900 | 0.3256 | v10.7 To... Follow the steps... Use the Filter by ... |
| 2901 | 0.3256 | If any conflicts are detected with Table 1: Option... |
| 2902 | 0.3255 | v10.7 Export Activity Records in Bulk As said, Net... |
| 2903 | 0.3254 | Verify the parameters you provided in settings.xml... |
| 2904 | 0.3254 | See the Assign Permission to Read the Registry Key... |
| 2905 | 0.3254 | For that, run the following command: ncli> rsyslog... |
| 2906 | 0.3253 | v10.7 Parameter Default value Description Connecti... |
| 2907 | 0.3253 | AD Container Complete the following fields: Option... |
| 2908 | 0.3253 | Scale-Out File Server (SOFS) cluster is not suppor... |
| 2909 | 0.3252 | Step 2 – In the item configuration menu, select Ne... |
| 2910 | 0.3251 | Failed read attempts The Auditing Entry below show... |
| 2911 | 0.3251 | Failed read attempts The Auditing Entry below show... |
| 2912 | 0.3251 | NOTE: This covers all the required permissions bel... |
| 2913 | 0.3251 | RuleFileList cyberark-v2.xml You can specify sever... |
| 2914 | 0.3251 | Review the following for additional information: E... |
| 2915 | 0.3250 | Step 6 – Choose modern authentication. Step 7 – En... |
| 2916 | 0.3250 | If you plan to use modern authentication, see the ... |
| 2917 | 0.3248 | Review Behavior Anomalies Dashboard To review the ... |
| 2918 | 0.3248 | See the Configure Local Audit Policies topic and t... |
| 2919 | 0.3247 | To specify a non-default port, provide a server na... |
| 2920 | 0.3245 | State-in-Time Select to configure Auditor to exclu... |
| 2921 | 0.3245 | State-in-Time Select to configure Auditor to exclu... |
| 2922 | 0.3245 | State-in-Time Select to configure Auditor to exclu... |
| 2923 | 0.3244 | See the Reported Attributes topic for more informa... |
| 2924 | 0.3242 | This app will allow you to collect both activity a... |
| 2925 | 0.3241 | Otherwise, the add-on will not be v10.7 Parameter ... |
| 2926 | 0.3240 | Facility Select desired facility. v10.7 55.. Under... |
| 2927 | 0.3240 | Review the following for additional information: O... |
| 2928 | 0.3240 | To specify a non-default port, provide a server na... |
| 2929 | 0.3240 | To specify a non-default port, provide a server na... |
| 2930 | 0.3238 | Step 2 – On the Home page, navigate to Folder Sett... |
| 2931 | 0.3236 | Provide the name of the UDP port used to listen to... |
| 2932 | 0.3236 | Specify an item name. Make sure to create a dedica... |
| 2933 | 0.3236 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 2934 | 0.3236 | • Check "Successful" and "Failed" next to List fol... |
| 2935 | 0.3235 | The custom account must be granted the following r... |
| 2936 | 0.3235 | v10.7 Step 4 – Double-click the searchFlags attrib... |
| 2937 | 0.3234 | See SharePoint for more information. ◦ The user th... |
| 2938 | 0.3234 | Periodic time interval for reading EventsReadingPe... |
| 2939 | 0.3233 | Error message will not appear on the screen; inste... |
| 2940 | 0.3233 | For that, the user account will need an administra... |
| 2941 | 0.3233 | You can also configure and receive alerts on the e... |
| 2942 | 0.3233 | PCIDSS. This filter shows activity records collect... |
| 2943 | 0.3230 | Run the following command in nlci: v10.7 ncli> rsy... |
| 2944 | 0.3228 | — Address The Address parameter may be followed by... |
| 2945 | 0.3228 | In the response, locate the uuids of the target fo... |
| 2946 | 0.3228 | See the View Reports topic for additional informat... |
| 2947 | 0.3226 | Ensure that... The Auditor server side • Auditor v... |
| 2948 | 0.3226 | If a specific account is designated to run the add... |
| 2949 | 0.3226 | Configure the Microsoft Entra ID App for Auditing ... |
| 2950 | 0.3224 | Program/script Input "Powershell.exe". Add a path ... |
| 2951 | 0.3224 | For example, if you have advanced omitreporterrors... |
| 2952 | 0.3223 | Table 1: Audit subcategory Command Security Group ... |
| 2953 | 0.3223 | Auditing of System zone is not supported. As state... |
| 2954 | 0.3223 | The latter ones are listed in the table below. Fil... |
| 2955 | 0.3223 | Auditor supports automated size calculation for al... |
| 2956 | 0.3222 | Enterprise Overview See also: Enterprise Overview ... |
| 2957 | 0.3222 | For example: -file "C:\Addons\Netwrix_Auditor_Audi... |
| 2958 | 0.3222 | Name of the event log where the events will be Fil... |
| 2959 | 0.3222 | Roles are described briefly in the table below and... |
| 2960 | 0.3221 | Example: Shows the path to Parent OU/container acc... |
| 2961 | 0.3220 | Logons Cause (for failed attempts) Successful logo... |
| 2962 | 0.3220 | To specify a non-default port, provide a server na... |
| 2963 | 0.3219 | To configure them manually, refer to the Configure... |
| 2964 | 0.3218 | StateUpdatingPeriodicity Periodic time interval fo... |
| 2965 | 0.3218 | Upon s electing Combination of file and share perm... |
| 2966 | 0.3218 | Upon s electing Combination of file and share perm... |
| 2967 | 0.3218 | Upon s electing Combination of file and share perm... |
| 2968 | 0.3218 | Activity record stands for one operable chunk of i... |
| 2969 | 0.3218 | Software Compatibility & Versions For proper funct... |
| 2970 | 0.3218 | See the Data Collection from VMware Servers topic ... |
| 2971 | 0.3217 | Active Directory Ports AD FS Ports Microsoft Entra... |
| 2972 | 0.3217 | The Auditor server side Auditor version is 10.0 or... |
| 2973 | 0.3217 | The Auditor server side Auditor version is 10.0 or... |
| 2974 | 0.3217 | The Auditor server side Auditor version is 10.0 or... |
| 2975 | 0.3216 | Or simply drag and drop the add-on file in the con... |
| 2976 | 0.3216 | How owners should log into the application console... |
| 2977 | 0.3216 | Default value is -1 (switch off concurrent forward... |
| 2978 | 0.3215 | MS Teams monitoring plan has been added to Auditor... |
| 2979 | 0.3213 | If you want to use a specific account (other than ... |
| 2980 | 0.3213 | Audited domain Specify domain name in the FQDN for... |
| 2981 | 0.3213 | The Auditor Server side The TCP 9699 port (default... |
| 2982 | 0.3212 | Step 2 – In the item configuration menu, select Ne... |
| 2983 | 0.3212 | Troubleshooting If no data is displayed in the rep... |
| 2984 | 0.3211 | See the following Microsoft article for additional... |
| 2985 | 0.3211 | AD Container Complete the following fields: Option... |
| 2986 | 0.3208 | Possible values: Empty—Check Auditor certificate v... |
| 2987 | 0.3208 | Possible values: Empty—Check Auditor certificate v... |
| 2988 | 0.3208 | Most parameters are optional, the script uses the ... |
| 2989 | 0.3205 | Configure Audit Object Access Policy Netwrixrecomm... |
| 2990 | 0.3205 | Snapshot date —select the date of state-in-time sn... |
| 2991 | 0.3205 | Snapshot date —select the date of state-in-time sn... |
| 2992 | 0.3204 | You can delegate control over a monitoring plan to... |
| 2993 | 0.3204 | 1=yes 0=no (default) Parameters within SourceList ... |
| 2994 | 0.3201 | Syslog Server Provide a server name by entering it... |
| 2995 | 0.3201 | v10.7 Export SSRS-based reports To export SSRS-bas... |
| 2996 | 0.3200 | Step 3 – Make sure Enable logging is selected. Ste... |
| 2997 | 0.3197 | C:\Add-ons\Netwrix_Auditor_Addon_for_ RADIUS_Serve... |
| 2998 | 0.3197 | DefaultTsTimezone — Define the time zone of syslog... |
| 2999 | 0.3197 | If a credential password for one of these accounts... |
| 3000 | 0.3195 | See the Choose Appropriate Execution Scenario topi... |
| 3001 | 0.3195 | By default, data is imported to a specially create... |
| 3002 | 0.3192 | Please be aware that monitoring of actions perform... |
| 3003 | 0.3192 | Helps find out who made Successful changes to your... |
| 3004 | 0.3192 | Detect additional details Specify additional infor... |
| 3005 | 0.3191 | Note that the new monitoring scope restrictions ap... |
| 3006 | 0.3190 | As you investigate suspicious activity and review ... |
| 3007 | 0.3188 | Perform the following procedures to configure obje... |
| 3008 | 0.3187 | v10.7 Parameter Default value Description The numb... |
| 3009 | 0.3185 | Step 3 – Move the selected snapshots to the Snapsh... |
| 3010 | 0.3185 | Configure Local Audit Policies You can choose to c... |
| 3011 | 0.3184 | Using Basic Authentication with Microsoft Entra ID... |
| 3012 | 0.3183 | File permissions define who has access to local fi... |
| 3013 | 0.3183 | Table 1: Option Description Okta Connection Settin... |
| 3014 | 0.3181 | Specify monitoring restrictions Add Computer – Pro... |
| 3015 | 0.3180 | Otherwise, the addon will not be able to write dat... |
| 3016 | 0.3180 | Otherwise, the addon will not be able to write dat... |
| 3017 | 0.3180 | To track the copy action, enable successful read a... |
| 3018 | 0.3179 | Pager is the default property. If the Pager proper... |
| 3019 | 0.3178 | Then s/he adds items to the monitoring plan – thes... |
| 3020 | 0.3178 | Complete the process After you click Apply require... |
| 3021 | 0.3178 | Max length: 21 HeaderText characters. Defines URL ... |
| 3022 | 0.3177 | If you plan to use modern authentication, see the ... |
| 3023 | 0.3177 | If you plan to use modern authentication, see the ... |
| 3024 | 0.3177 | Use this report to determine the owners of particu... |
| 3025 | 0.3177 | Allow outbound connections from the dynamic (1024 ... |
| 3026 | 0.3176 | If any conflicts are detected with your current au... |
| 3027 | 0.3175 | See the following table for the certain reports: T... |
| 3028 | 0.3173 | You can also change these settings later. See the ... |
| 3029 | 0.3173 | Advanced permissions: ◦ Create files / write data ... |
| 3030 | 0.3172 | You cannot disable auditing the Domain partition f... |
| 3031 | 0.3172 | You can use a wildcard (*). In this case you will ... |
| 3032 | 0.3172 | Apply gMSA to Access Long-Term Archive To write da... |
| 3033 | 0.3171 | Once have created a monitoring plan and verified t... |
| 3034 | 0.3171 | Sub-element: Name. The item type is added inside t... |
| 3035 | 0.3169 | Table 1: Registry key (REG_DWORD type) Description... |
| 3036 | 0.3169 | As a next step, click Add item to specify an objec... |
| 3037 | 0.3168 | If you also want to audit changes to AD configurat... |
| 3038 | 0.3168 | v10.7 For evaluation and PoC projects you can depl... |
| 3039 | 0.3165 | Follow the steps to use Netwrix Privilege Secure a... |
| 3040 | 0.3165 | Follow the steps to use Netwrix Privilege Secure a... |
| 3041 | 0.3165 | In sqlplus tool, execute the following command: sq... |
| 3042 | 0.3165 | Enable State-in-Time Data Collection If you want t... |
| 3043 | 0.3165 | Palo Alto Pulse Secure Provide this account in the... |
| 3044 | 0.3164 | SharePoint NOTE: Prior to configuring your monitor... |
| 3045 | 0.3164 | When you restore deleted accounts with the Netwrix... |
| 3046 | 0.3163 | See the Configure the Back up Files and Directorie... |
| 3047 | 0.3162 | A management IP is an IP address that is used for ... |
| 3048 | 0.3161 | Allow outbound connections from the dynamic (1024 ... |
| 3049 | 0.3161 | At least the first script run should be performed ... |
| 3050 | 0.3161 | At least the first script run should be performed ... |
| 3051 | 0.3161 | At least the first script run should be performed ... |
| 3052 | 0.3159 | between an object type and a property, the whole e... |
| 3053 | 0.3158 | If you want to generate reports based on differen ... |
| 3054 | 0.3158 | If you want to generate reports based on differen ... |
| 3055 | 0.3158 | If you want to generate reports based on differen ... |
| 3056 | 0.3157 | Specify users to track their activity Exclude—Add ... |
| 3057 | 0.3156 | Step 3 – Specify default SQL Server instance and c... |
| 3058 | 0.3154 | Activity Record for groups membership $deltaToken=... |
| 3059 | 0.3154 | Review your configuration and click Save. Review R... |
| 3060 | 0.3154 | Perform this action with other computers. Step 4 –... |
| 3061 | 0.3153 | The instructions below apply only if you are going... |
| 3062 | 0.3152 | Use a standard account for that. See the SQL Serve... |
| 3063 | 0.3151 | Ensure that... The Auditor server side • Auditor v... |
| 3064 | 0.3150 | SHOW PARAMETERS audit%r; If you want to clean your... |
| 3065 | 0.3150 | Password – Provide password for this account. Summ... |
| 3066 | 0.3150 | You can click Browse Specify syslog host or networ... |
| 3067 | 0.3150 | The product updates the latest snapshot on the reg... |
| 3068 | 0.3149 | When an object is deleted, Auditor does not show a... |
| 3069 | 0.3148 | Successful Enabling this option on public shares w... |
| 3070 | 0.3148 | Do not select the checkbox if you want to configur... |
| 3071 | 0.3148 | Make sure that the Apply these auditing entries to... |
| 3072 | 0.3146 | In the Schedule state-in-time data collection sect... |
| 3073 | 0.3145 | The service automatically creates incident tickets... |
| 3074 | 0.3145 | In the Schedule state-in-time data collection sect... |
| 3075 | 0.3145 | In the Schedule state-in-time data collection sect... |
| 3076 | 0.3144 | Otherwise, the addon will not be able to write dat... |
| 3077 | 0.3144 | Otherwise, the addon will not be able to write dat... |
| 3078 | 0.3144 | Table 1: Description Changes Successful Use this o... |
| 3079 | 0.3144 | See the Subscriptions topic for additional informa... |
| 3080 | 0.3144 | NOTE: For Microsoft Entra ID, only the current dat... |
| 3081 | 0.3143 | Using Modern Authentication with Microsoft Entra I... |
| 3082 | 0.3143 | The entry may also include a modifier—a match type... |
| 3083 | 0.3143 | Helps identify who accessed important files beside... |
| 3084 | 0.3142 | Add a path to the add-on in double quotes and spec... |
| 3085 | 0.3141 | Port Protocol Source Target Purpose For a full lis... |
| 3086 | 0.3140 | Click Modify and select day(s) of week you want yo... |
| 3087 | 0.3140 | Click Modify and select day(s) of week you want yo... |
| 3088 | 0.3139 | To check that a new policy was included in the lis... |
| 3089 | 0.3138 | *) HKEY_LOCAL_MACHINE\SYSTEM\CurrentContro lSet\Se... |
| 3090 | 0.3138 | C:\Add-ons\Netwrix_Auditor_Addon_for_RADIUS_Server... |
| 3091 | 0.3137 | You can adjust audit settings automatically. Your ... |
| 3092 | 0.3135 | You can use group Managed Service Accounts (gMSA) ... |
| 3093 | 0.3135 | See the State–In–Time Reports topic for additional... |
| 3094 | 0.3133 | If you want to use a specific account (other than ... |
| 3095 | 0.3133 | See the Monitoring Overview topic for additional i... |
| 3096 | 0.3132 | See the Reported Attributes topic below for more i... |
| 3097 | 0.3131 | The wizard will start and ask the additional param... |
| 3098 | 0.3131 | Use this option to detect suspicious activity on y... |
| 3099 | 0.3131 | To receive an invitation to the Partner Portal, pl... |
| 3100 | 0.3130 | See the Microsoft Entra ID topic for additional in... |
| 3101 | 0.3130 | See the Choose Appropriate Execution Scenario topi... |
| 3102 | 0.3130 | v10.7 Parameter Default value Description Server r... |
| 3103 | 0.3128 | Step 3 – In the Settings list, locate Downloads > ... |
| 3104 | 0.3128 | Use this report to discover user accounts with set... |
| 3105 | 0.3127 | See the procedure below for A Security Officer wan... |
| 3106 | 0.3127 | See the procedure below for A Security Officer wan... |
| 3107 | 0.3127 | A Security Officer wants to monitor a file share b... |
| 3108 | 0.3126 | A Security Officer wants to monitor a file share t... |
| 3109 | 0.3125 | Step 5 – Double-click the newly created rule and o... |
| 3110 | 0.3124 | Then s/he adds items to the monitoring plan – thes... |
| 3111 | 0.3124 | v10.7 The "Create a monitoring plan" link prompts ... |
| 3112 | 0.3123 | Add/Remove programs—Enables auditing of installed ... |
| 3113 | 0.3122 | Your monitoring plan is configure d to track domai... |
| 3114 | 0.3121 | Step 2 – In the upper-left of your site collection... |
| 3115 | 0.3121 | If you want to run the add-on on another machine, ... |
| 3116 | 0.3120 | ◦ Additional configuration if auto-backup is enabl... |
| 3117 | 0.3118 | Monitoring plan configuration List folders + + + +... |
| 3118 | 0.3115 | Use this report to identify data at high risk and ... |
| 3119 | 0.3111 | The changes include creation, modification, deleti... |
| 3120 | 0.3111 | • For subscription to risk assessment overview —Se... |
| 3121 | 0.3111 | ◦◦ Target Nutanix File Server must be located in t... |
| 3122 | 0.3110 | For that, run the following command in ncli : fs a... |
| 3123 | 0.3109 | If you audit multiple servers, you may want to cre... |
| 3124 | 0.3107 | Compliance Mappings This tile contains links to th... |
| 3125 | 0.3106 | Follow the steps to define log on as a service pol... |
| 3126 | 0.3105 | When you add the first item (Nutanix SMB shares) t... |
| 3127 | 0.3104 | will not be monitored. Step 3 – Review considerati... |
| 3128 | 0.3104 | Specify monitoring restrictions Specify restrictio... |
| 3129 | 0.3103 | *) v10.7 This refers to the following keys: HKEY_L... |
| 3130 | 0.3102 | See the Health Status Dashboard topic for addition... |
| 3131 | 0.3102 | Specify additional information to include in repor... |
| 3132 | 0.3102 | Specify additional information to include in repor... |
| 3133 | 0.3102 | To exclude events containing “System” instead of i... |
| 3134 | 0.3101 | Assume, each department has its own field of respo... |
| 3135 | 0.3101 | Event level Select level of the events that you wa... |
| 3136 | 0.3100 | Note that the new monitoring scope restrictions ap... |
| 3137 | 0.3100 | Major benefit of the integrated solution implement... |
| 3138 | 0.3100 | To specify a non-default port, provide a server na... |
| 3139 | 0.3100 | To specify a non-default port, provide a server na... |
| 3140 | 0.3098 | v10.7 Step 1 – On the computer where Netwrix Audit... |
| 3141 | 0.3097 | Step 1 – Open the monitored item properties for ed... |
| 3142 | 0.3096 | XML: XML: <ActivityRecord><Action>Successful L ogo... |
| 3143 | 0.3095 | This list is only relevant to operations with SQL ... |
| 3144 | 0.3095 | Subscribe Subscription to the search results is no... |
| 3145 | 0.3094 | Move the selected snapshots to the Snapshots avail... |
| 3146 | 0.3094 | Allow outbound connections from the dynamic (1024 ... |
| 3147 | 0.3094 | See the procedure below for A Security Officer wan... |
| 3148 | 0.3093 | You can add several IDs separated by comma. Event ... |
| 3149 | 0.3093 | A Security Officer wants to monitor a file share b... |
| 3150 | 0.3092 | Add Computer – Provide the name of the Specify mon... |
| 3151 | 0.3091 | 55.. Run the following command to update group pol... |
| 3152 | 0.3090 | AD Container Complete the following fields: Option... |
| 3153 | 0.3089 | The users assigned the Reviewer role on a certain ... |
| 3154 | 0.3087 | • Make sure that the Apply these auditing entries ... |
| 3155 | 0.3086 | For example: Format Request curl https://WKSWin201... |
| 3156 | 0.3085 | Data file path— .MDF file path. Log file path— .LD... |
| 3157 | 0.3085 | To collect activity data, the account must have at... |
| 3158 | 0.3085 | To specify a non-default port, provide a server na... |
| 3159 | 0.3085 | Specify the name from the Value list or type it yo... |
| 3160 | 0.3084 | NOTE: The new destination folder will be ...\Netwr... |
| 3161 | 0.3084 | • Make sure that the Apply these auditing entries ... |
| 3162 | 0.3083 | Click Search. Navigate to Tools and select Subscri... |
| 3163 | 0.3083 | When configuring, mind that your data will be dele... |
| 3164 | 0.3083 | CAUTION: Monitoring of non-default hidden shares i... |
| 3165 | 0.3081 | NOTE: Please consider the following: Logon activit... |
| 3166 | 0.3081 | For example: Table 1: Event ID Description 22 Pass... |
| 3167 | 0.3081 | Window Application Run As: <account_name> Standard... |
| 3168 | 0.3079 | Advanced permissions: ◦ Create files / write data ... |
| 3169 | 0.3078 | Recent alerts – Shows all the triggered alerts in ... |
| 3170 | 0.3076 | You can add several IDs separated by comma. Select... |
| 3171 | 0.3075 | You can use a wildcard (*). In this case you will ... |
| 3172 | 0.3073 | If not, the service will proceed to the next rule ... |
| 3173 | 0.3073 | To do so, perform the following steps: Step 1 – Go... |
| 3174 | 0.3073 | v10.7 Option Description they will not be collecte... |
| 3175 | 0.3070 | Table 1: Port Protocol Source Target Purpose 137 1... |
| 3176 | 0.3069 | A monitoring plan defines data collection, notific... |
| 3177 | 0.3069 | Failed read attempts The Auditing Entry below show... |
| 3178 | 0.3069 | Failed read attempts The Auditing Entry below show... |
| 3179 | 0.3068 | This will not affect the Reports functionality and... |
| 3180 | 0.3068 | On the Name step, specify the rule's name, for exa... |
| 3181 | 0.3065 | Program/script Input "Powershell.exe". Add argumen... |
| 3182 | 0.3065 | NetwrixAuditorHost localhost:9699 If you want to r... |
| 3183 | 0.3065 | Only the lowest 9 bits of the calculation result a... |
| 3184 | 0.3065 | On the computer where your database is deployed, r... |
| 3185 | 0.3062 | Click Finish to Summary exit the wizard. The newly... |
| 3186 | 0.3062 | Table 1: Step Description Locate Folder Browse for... |
| 3187 | 0.3062 | When the port is set as desired, click Next. NOTE:... |
| 3188 | 0.3060 | If you need to modify them later, run the Netwrix.... |
| 3189 | 0.3060 | Failed change attempts The Auditing Entry below sh... |
| 3190 | 0.3058 | All filters are applied using AND logic. Configure... |
| 3191 | 0.3057 | Nutanix AHV is a fully integrated component of the... |
| 3192 | 0.3057 | See the Deployment Proceduretopic for more informa... |
| 3193 | 0.3056 | When a new object is created, Auditor does not sho... |
| 3194 | 0.3055 | — v10.7 Hardware component Minimum required Recomm... |
| 3195 | 0.3054 | This account requires administrative rights. Then ... |
| 3196 | 0.3053 | Review the following Microsoft technical a rticle ... |
| 3197 | 0.3053 | Step 6 – For auditing Logon Activity, you also nee... |
| 3198 | 0.3052 | Step 6 – Register the Add-On Prepare Auditor for D... |
| 3199 | 0.3052 | Helps find out who made changes to your fi les, in... |
| 3200 | 0.3049 | For example, -76. v10.7 Option Description Select ... |
| 3201 | 0.3047 | ◦◦ See the Configure AD FS farm manually topic for... |
| 3202 | 0.3046 | Table 1: Option Description Events collected from ... |
| 3203 | 0.3046 | Table 1: Option Description Events collected from ... |
| 3204 | 0.3044 | Make sure that the Apply these auditing entries to... |
| 3205 | 0.3044 | Make sure that the Apply these auditing entries to... |
| 3206 | 0.3044 | Step 5 – Expand Directory role and select the role... |
| 3207 | 0.3044 | Step 5 – Expand Directory role and select the role... |
| 3208 | 0.3043 | Requirements Installation If you are using previou... |
| 3209 | 0.3043 | See the Data C ollecting Account topic for additio... |
| 3210 | 0.3041 | This filter can be helpful when you are looking fo... |
| 3211 | 0.3038 | Step 2 – Configure System Access Control List (SAC... |
| 3212 | 0.3038 | If a different log level is needed or desired, the... |
| 3213 | 0.3037 | server\instance name In this case the "Who", "Work... |
| 3214 | 0.3035 | You may have insufficient permissions. Contact you... |
| 3215 | 0.3034 | Collect data on non-owner access to mailboxes Revi... |
| 3216 | 0.3034 | Select the account that will be used to collect da... |
| 3217 | 0.3034 | Select the account that will be used to collect da... |
| 3218 | 0.3033 | ), shares Table 1: Option Description used by prin... |
| 3219 | 0.3031 | fs_create_hard_link A new hard link was created. f... |
| 3220 | 0.3031 | Configuration Activity Records to Event Log Add-on... |
| 3221 | 0.3029 | v10.7 Error in PowerShell Resolution Select the ac... |
| 3222 | 0.3029 | By default, it is set to "0" (decimal). Modify thi... |
| 3223 | 0.3024 | Helps find out who made Successful changes to your... |
| 3224 | 0.3024 | Basically, this option is enough for employees who... |
| 3225 | 0.3023 | Tip for reading the table: For example, on the com... |
| 3226 | 0.3022 | Enable / disable an existing alert Step 1 – Select... |
| 3227 | 0.3022 | In addition, you can exclude data from non-owner a... |
| 3228 | 0.3022 | At least the first script run should be performed ... |
| 3229 | 0.3020 | • .NET Framework versions 4.5 or later Nutanix Pri... |
| 3230 | 0.3020 | The machine where the add-on will be installed .NE... |
| 3231 | 0.3020 | ◦◦ User name – Provide the name of account that wi... |
| 3232 | 0.3019 | To specify a non-default port, provide a server na... |
| 3233 | 0.3019 | When finished, click OK. See also Using historical... |
| 3234 | 0.3017 | On successful subscription generation you will rec... |
| 3235 | 0.3017 | Configure ConnectWise This section describes how t... |
| 3236 | 0.3017 | Understanding Scopes Scopes for different Auditor ... |
| 3237 | 0.3016 | Click Search. Navigate to Tools and select Subscri... |
| 3238 | 0.3016 | Select the account that will be used to collect da... |
| 3239 | 0.3016 | Specify a name of associated monitoring plan in Au... |
| 3240 | 0.3015 | Otherwise, you will not be able to run reviews on ... |
| 3241 | 0.3014 | * Inactive User Tracker Auditor Inactive User Trac... |
| 3242 | 0.3013 | Clicking the tile opens the Activity Record St ati... |
| 3243 | 0.3013 | Create a special user account with permissions to ... |
| 3244 | 0.3012 | Depending on the execution scenario you choose, yo... |
| 3245 | 0.3010 | Windows File Server NOTE: Prior to configuring you... |
| 3246 | 0.3010 | So, you should register an Microsoft Entra ID app ... |
| 3247 | 0.3008 | Follow the steps to assign the dbcreator and db_ow... |
| 3248 | 0.3008 | If you are running the add-on for the first time (... |
| 3249 | 0.3007 | The risk score assigned to a user does not qualify... |
| 3250 | 0.3007 | Report Summary with Star icon unchecked Other Acti... |
| 3251 | 0.3005 | Step 1 – Select the desired item. Step 2 – In the ... |
| 3252 | 0.3003 | fields. The DetailList field is not mandatory, it ... |
| 3253 | 0.3000 | Step 2 – Log in to your cluster as a root user. Ta... |
| 3254 | 0.3000 | PauseWhenSendingFailed Pause after a failed attemp... |
| 3255 | 0.3000 | The machine where the Add-On will be installed The... |
| 3256 | 0.2999 | See SharePoint for more information. v10.7 The use... |
| 3257 | 0.2999 | AD Container Complete the following fields: Option... |
| 3258 | 0.2999 | See the following Microsoft article for more infor... |
| 3259 | 0.2998 | Step 4 – Hit Enter. Depending on the number of eve... |
| 3260 | 0.2997 | v10.7 Step 4 – In the Services window, ensure that... |
| 3261 | 0.2996 | Check the Database, Active Directory, and Notifica... |
| 3262 | 0.2996 | For example, you want to receive an alert on suspi... |
| 3263 | 0.2996 | Step 2 – Disable the Object Access, Account Manage... |
| 3264 | 0.2996 | Table 1: Option Description Use implicit SSL Selec... |
| 3265 | 0.2995 | Step 8 – Provide the object name and configure ite... |
| 3266 | 0.2995 | Table 1: Option Setting Rule Type Program Program ... |
| 3267 | 0.2994 | NOTE: This covers all the required permissions bel... |
| 3268 | 0.2993 | PaloAlto Devices Auditor supports monitoring the f... |
| 3269 | 0.2993 | The following operations will be audited: "FILE_RE... |
| 3270 | 0.2992 | Enforce certificate validation to ensure security ... |
| 3271 | 0.2992 | The status is 200 OK. For XML, a response body con... |
| 3272 | 0.2990 | Account type —possible values: Windows Account, Lo... |
| 3273 | 0.2988 | This account should meet the requirements listed b... |
| 3274 | 0.2987 | In the list of servers, select the server you want... |
| 3275 | 0.2987 | To specify a non-default port, provide a server na... |
| 3276 | 0.2986 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3277 | 0.2985 | By default, the remote Syslog listening server is ... |
| 3278 | 0.2985 | Step 4 – The new secret will be displayed in the l... |
| 3279 | 0.2985 | Check "Successful" next to the following permissio... |
| 3280 | 0.2983 | Specify the account for collecting data Group Mana... |
| 3281 | 0.2983 | Advanced filters to make your results context matc... |
| 3282 | 0.2981 | On domain controllers in your domain (target), all... |
| 3283 | 0.2981 | Table 1: Data source Required rights and permissio... |
| 3284 | 0.2981 | Alternatively, you can grant the Global administra... |
| 3285 | 0.2981 | Alternatively, you can grant the Global administra... |
| 3286 | 0.2980 | Follow the steps to enable object-level auditing f... |
| 3287 | 0.2980 | Item — name of the item within your monitoring pla... |
| 3288 | 0.2979 | Unless specified, the script runs with the current... |
| 3289 | 0.2979 | The Detail field may contain sub-fields with value... |
| 3290 | 0.2978 | NetwrixAuditorHost localhost:9699 Assumes that the... |
| 3291 | 0.2978 | In the Group Policy Management Editor dialog, expa... |
| 3292 | 0.2977 | See the Settings for Data Collection topic for add... |
| 3293 | 0.2976 | If enabled, a Compression Service will be automati... |
| 3294 | 0.2974 | Customers who are logged in to the Netwrix Custome... |
| 3295 | 0.2973 | See the Data C ollecting Account topic for additio... |
| 3296 | 0.2973 | collect state-in-time data for this folder. Select... |
| 3297 | 0.2973 | collect state-in-time data for this folder. Select... |
| 3298 | 0.2973 | Create a special user account with permissions to ... |
| 3299 | 0.2973 | Create Role on NetApp Clustered Data ONTAP 8 or ON... |
| 3300 | 0.2972 | Table 2: Option Description General Specify AD con... |
| 3301 | 0.2972 | Step 1 – Select the desired item. Step 2 – In the ... |
| 3302 | 0.2972 | Step 1 – Select the desired item. Step 2 – In the ... |
| 3303 | 0.2972 | See the Use Filters in Advanced Mode topic for a d... |
| 3304 | 0.2971 | For example, if reporting on the database hosted o... |
| 3305 | 0.2971 | When specified, overrides the NetwrixAuditorPlan —... |
| 3306 | 0.2971 | SQL Server Databases This report lists the propert... |
| 3307 | 0.2970 | Do one of the following, depending on your Dell Is... |
| 3308 | 0.2970 | The OU itself, however, will not be monitored, mea... |
| 3309 | 0.2970 | What Shows the path to the modified AD object. Tab... |
| 3310 | 0.2970 | object type:property: When a new object is created... |
| 3311 | 0.2968 | The resource name includes its location, such as t... |
| 3312 | 0.2967 | Remember that administrative hidden shares like de... |
| 3313 | 0.2965 | If you plan to audit an SQL Server for data change... |
| 3314 | 0.2965 | v10.7 The information displayed in the table inclu... |
| 3315 | 0.2964 | Table 1: Event Type Description Information An eve... |
| 3316 | 0.2964 | When Yes dateTime The moment when the change occur... |
| 3317 | 0.2963 | Upon login, you will be directed to the My Reviews... |
| 3318 | 0.2962 | Max length: 255. • Contains (default) • DoesNotCon... |
| 3319 | 0.2961 | This refers to the specified shared folder, its su... |
| 3320 | 0.2960 | object_type_name Available object types can be fou... |
| 3321 | 0.2960 | If you want to generate reports based on differen ... |
| 3322 | 0.2960 | VMware Ports Review a full list of protocols and p... |
| 3323 | 0.2960 | All Internet Explorer-related settings are relevan... |
| 3324 | 0.2959 | v10.7 Report Description category, plan for data p... |
| 3325 | 0.2959 | Execute the command... TRIGGER,DROP TRIGGER,CREATE... |
| 3326 | 0.2959 | Table 1: Option Description Specify the account fo... |
| 3327 | 0.2958 | This refers to the specified shared folder, its su... |
| 3328 | 0.2956 | Use this report to see who has permissions to what... |
| 3329 | 0.2955 | Configuration objects store the information on sit... |
| 3330 | 0.2955 | For most data sources, if an Activity Summaries co... |
| 3331 | 0.2954 | Mailboxes: UserMailbox SharedMailbox EquipmentMail... |
| 3332 | 0.2954 | Unless specified, the service runs under the accou... |
| 3333 | 0.2954 | Unless specified, the service runs under the accou... |
| 3334 | 0.2953 | Clicking the link opens the corresponding report: ... |
| 3335 | 0.2953 | In the dialog that opens, specify the OUs that you... |
| 3336 | 0.2953 | For details, see Manage historical snapshots optio... |
| 3337 | 0.2953 | VMware vCenter or ESX(i) host ◦◦ VMware events tha... |
| 3338 | 0.2952 | autoDetect Set to False. Step 5 – Start the Audito... |
| 3339 | 0.2952 | See the corresponding Oracle documentation article... |
| 3340 | 0.2951 | You can click Browse to select a array computer fr... |
| 3341 | 0.2947 | To specify a non-default port, provide a server na... |
| 3342 | 0.2947 | Currently, you cannot assign or create tags on thi... |
| 3343 | 0.2945 | To open the Long-Term Archive settings, click the ... |
| 3344 | 0.2945 | If your issue is not listed in the table below, tr... |
| 3345 | 0.2943 | Move the selected snapshots to the Snapshots avail... |
| 3346 | 0.2943 | exomiteventuserlist.txt user@tenant.com will be re... |
| 3347 | 0.2940 | For example: .Identity .DomainController .Organiza... |
| 3348 | 0.2940 | Requirements Installation If you are using previou... |
| 3349 | 0.2939 | Every now and then, you review the Behavior Anomal... |
| 3350 | 0.2937 | Failed Use this option to detect suspicious activi... |
| 3351 | 0.2937 | All filters are applied using AND logic. Configure... |
| 3352 | 0.2936 | Trailing comma is not supported. Table 1: Method E... |
| 3353 | 0.2936 | Tip for reading the table: For example, on the com... |
| 3354 | 0.2936 | v10.7 Step 4 – In the Maximum security log size Pr... |
| 3355 | 0.2935 | Ensure that... • The user running the script must ... |
| 3356 | 0.2935 | Subscribe Create subscription for periodic deliver... |
| 3357 | 0.2933 | Only the lowest 9 bits of the calculation result a... |
| 3358 | 0.2932 | v10.7 v10.7 Reported data The report has a summary... |
| 3359 | 0.2931 | Netwrix recommends setting it to 2 years (730 days... |
| 3360 | 0.2930 | Use the omitlogonlist.txt to exclude SQL logons fr... |
| 3361 | 0.2930 | See the Permissions for Microsoft Entra ID Auditin... |
| 3362 | 0.2929 | your monitoring plan (e.g., two Active Directory d... |
| 3363 | 0.2929 | Table 1: Interface Purpose Opened By Accessible To... |
| 3364 | 0.2928 | To specify a non-default port, provide a server na... |
| 3365 | 0.2927 | Syslog Device Network Devices Cisco Meraki Dashboa... |
| 3366 | 0.2927 | • XML: <ActivityRecord><Action>Added</Action ><Mon... |
| 3367 | 0.2927 | Use the omitreadaccess.txt to exclude SELECT state... |
| 3368 | 0.2925 | For example: ONTAPI cluster1::> vserver services w... |
| 3369 | 0.2925 | Depending on Error the error code, the response bo... |
| 3370 | 0.2924 | v10.7 Configuring Microsoft Entra ID App for Audit... |
| 3371 | 0.2924 | Create login for ONTAPI role: security login creat... |
| 3372 | 0.2923 | v10.7 Option Description switch to turn the featur... |
| 3373 | 0.2923 | See the Configuration topic for additional informa... |
| 3374 | 0.2922 | Qtree Security must be configured. The volume wher... |
| 3375 | 0.2922 | Specify a file server Do not specify a default fil... |
| 3376 | 0.2922 | Example As a database administrator, you can have ... |
| 3377 | 0.2922 | Possible deployment options are as follows (here i... |
| 3378 | 0.2921 | Hardware component Minimum required Recommended An... |
| 3379 | 0.2921 | StartsWith EndsWith Contains (default) Limits your... |
| 3380 | 0.2920 | Defines destination IP address. In case of multipl... |
| 3381 | 0.2919 | See the Add Items for Monitoring topic for additio... |
| 3382 | 0.2919 | If you also want to audit changes to the Schema pa... |
| 3383 | 0.2918 | Table 2: Option Description General Specify ShareP... |
| 3384 | 0.2917 | Table 1: Object type Action What Description User ... |
| 3385 | 0.2916 | Item is added and SQL Server monitoring plan is re... |
| 3386 | 0.2916 | ◦◦ The logging trap option is selected from 1 to 6... |
| 3387 | 0.2915 | See the For Oracle Database Auditing topic for the... |
| 3388 | 0.2915 | Configure Windows Registry Audit Settings Windows ... |
| 3389 | 0.2915 | A custom account must be granted the same permissi... |
| 3390 | 0.2913 | Workstation Limits your search to an originating w... |
| 3391 | 0.2912 | Supported object types and attributes are listed i... |
| 3392 | 0.2912 | Supported object types and attributes are listed i... |
| 3393 | 0.2912 | Assumes that the add-on runs on the computer hosti... |
| 3394 | 0.2911 | RacNumber=31&Arg1= Request='GET /cgi-bin/ Read / R... |
| 3395 | 0.2911 | initiato r's account) as System. Network Protocol*... |
| 3396 | 0.2910 | Step 2 – Enable audit in the Azure Files settings.... |
| 3397 | 0.2910 | Port Protocol Source Target Purpose Exchange Onlin... |
| 3398 | 0.2909 | Step 1 – Make sure you have completed the preparat... |
| 3399 | 0.2909 | Applicable packages for each Oracle Database versi... |
| 3400 | 0.2908 | This can be helpful, for example, if you want to e... |
| 3401 | 0.2908 | http(s)://URL Enter root web site URLs. If you hav... |
| 3402 | 0.2907 | any number of characters. Examples: list/document.... |
| 3403 | 0.2907 | For example, backupsrv01.mydomain.local. Wildcards... |
| 3404 | 0.2907 | For example, backupsrv01.mydomain.local. Wildcards... |
| 3405 | 0.2906 | Reveal sensitive content that has permissions diff... |
| 3406 | 0.2904 | You can configur e Auditor to publish reports to f... |
| 3407 | 0.2903 | Configuring Windows registry audit settings on Win... |
| 3408 | 0.2902 | The credentials are case sensitive. Specify the ac... |
| 3409 | 0.2902 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Amazon_Web_S... |
| 3410 | 0.2901 | The logging trap option is selected from 1 to 6 in... |
| 3411 | 0.2901 | Here is an example of a CSV file structure: v10.7 ... |
| 3412 | 0.2900 | See the Dell Data Storage topic for additional inf... |
| 3413 | 0.2900 | NOTE: In this case, the product s till collects st... |
| 3414 | 0.2900 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3415 | 0.2899 | Leave blank if you use Windows Authentication. Def... |
| 3416 | 0.2898 | See the Define Parameters topic for additional inf... |
| 3417 | 0.2897 | Only the lowest 9 bits of the calculation result a... |
| 3418 | 0.2896 | Success. The body contains Activity Records. Activ... |
| 3419 | 0.2896 | Currently, not every detail about permission and a... |
| 3420 | 0.2894 | Successful changes v10.7 Configure Object-level ac... |
| 3421 | 0.2893 | The subscription (email attachment or file uploade... |
| 3422 | 0.2893 | 44.. Configure the following audit policies. Polic... |
| 3423 | 0.2890 | To view all groups the account is member of, expor... |
| 3424 | 0.2890 | v10.7 Option Description When the retention period... |
| 3425 | 0.2887 | Do one of the following, depending on your Dell Is... |
| 3426 | 0.2887 | Creating a ticket with Customer portal 11.. Sign i... |
| 3427 | 0.2886 | Step 4 – Select Content Manager. Grant Additional ... |
| 3428 | 0.2884 | v10.7 You can also use the Search window to examin... |
| 3429 | 0.2883 | Direct from login for owners without a role Data G... |
| 3430 | 0.2883 | It can be any custom name, for example a server na... |
| 3431 | 0.2882 | Step 4 – Obtain the tenant ID. You will need it wh... |
| 3432 | 0.2882 | Configure required protocols and ports, as describ... |
| 3433 | 0.2881 | Follow the steps to configure local audit policies... |
| 3434 | 0.2881 | v10.7 Monitored Sign-In types: Delegate Admin Dele... |
| 3435 | 0.2881 | Specify the account for collecting data Select the... |
| 3436 | 0.2881 | Specify the account for collecting data Select the... |
| 3437 | 0.2881 | Specify the account for collecting data Select the... |
| 3438 | 0.2881 | Specify the account for collecting data Select the... |
| 3439 | 0.2880 | ONTAPI/ONTAP REST API Select one of the following:... |
| 3440 | 0.2880 | Delegate Admin SoftDelete A message was permanentl... |
| 3441 | 0.2879 | Contact your virtual infrastructure administrator ... |
| 3442 | 0.2879 | v10.7 Option Description your current audit settin... |
| 3443 | 0.2878 | Complete the following fields: Option Description ... |
| 3444 | 0.2878 | See the Microsoft Entra ID topic for additional in... |
| 3445 | 0.2877 | Table 1: Item Action Audited How this change is re... |
| 3446 | 0.2877 | If not, the service will proceed to the next rule ... |
| 3447 | 0.2877 | If not, the service will proceed to the next rule ... |
| 3448 | 0.2877 | Table 1: Option Description It is recommended to u... |
| 3449 | 0.2876 | Details Shows the before and after values of the m... |
| 3450 | 0.2874 | v10.7 To.. Do.. 1. Select a plan and click Edit. I... |
| 3451 | 0.2874 | Step 2 – On the Summary page, select the Event Sum... |
| 3452 | 0.2873 | This helps to optimize solution performance during... |
| 3453 | 0.2873 | This helps to optimize solution performance during... |
| 3454 | 0.2872 | v10.7 Step 2 – Configure Access Reviews. The Confi... |
| 3455 | 0.2872 | This account should have sufficient REST API privi... |
| 3456 | 0.2871 | Table 1: File Description Syntax omituserlist.txt ... |
| 3457 | 0.2871 | v10.7 Complete the following fields: Option Descri... |
| 3458 | 0.2871 | minOccurs="0" indicates that element is optional a... |
| 3459 | 0.2870 | Monitor SSO users/groups on vCenter and Local user... |
| 3460 | 0.2869 | Enabled Examine all domain controllers Select this... |
| 3461 | 0.2868 | Assumes that the add-on runs on the computer hosti... |
| 3462 | 0.2868 | Assumes that the add-on runs on the computer hosti... |
| 3463 | 0.2868 | After deploying and configuring the add-on as desc... |
| 3464 | 0.2868 | Information specific to the data source, e.g., ass... |
| 3465 | 0.2867 | Specify the account for collecting data Select the... |
| 3466 | 0.2867 | Specify the account for collecting data Select the... |
| 3467 | 0.2866 | The ActivityRecordList root element includes the A... |
| 3468 | 0.2866 | 55.. Permissions-related considerations: v10.7 For... |
| 3469 | 0.2865 | Table 1: Option Description General Specify Nutani... |
| 3470 | 0.2865 | • Check that network connectivity between the Acco... |
| 3471 | 0.2865 | For other dist ributions, deployment of the rsyslo... |
| 3472 | 0.2864 | Overexposed Files and Folders This report shows se... |
| 3473 | 0.2864 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 3474 | 0.2862 | SharePoint Farm Complete the following fields: Opt... |
| 3475 | 0.2862 | Remember that administrative hidden shares like de... |
| 3476 | 0.2860 | The string descriptions for 10 actFolderMoveCopy S... |
| 3477 | 0.2858 | To execute commands in the context of Cluster, add... |
| 3478 | 0.2857 | Events collected from any other source will be ign... |
| 3479 | 0.2857 | Step 4 – In the Advanced Security Settings for SOF... |
| 3480 | 0.2856 | The add-on was renamed due to HPE acquisition by M... |
| 3481 | 0.2855 | Select the account that will be used to collect da... |
| 3482 | 0.2854 | Configure console access, Active Directory service... |
| 3483 | 0.2853 | See the s ection below for special considerations.... |
| 3484 | 0.2853 | Make sure to install the latest version. Step 2 – ... |
| 3485 | 0.2852 | Predefined reports are helpful if you are looking ... |
| 3486 | 0.2849 | Step 3 – Right-click the newly created GPO and sel... |
| 3487 | 0.2847 | See the Alertstopic for a dditional information. T... |
| 3488 | 0.2846 | Select a plan and click Edit. In the monitoring pl... |
| 3489 | 0.2846 | See the Interactive Reports for Change Management ... |
| 3490 | 0.2846 | Parameter Default value Description Assumes that t... |
| 3491 | 0.2845 | Port 1433 is the default connections port, however... |
| 3492 | 0.2845 | v10.7 Add Exclusion Follow the steps to add exclus... |
| 3493 | 0.2844 | Table 1: Attribute Description Possible values Fil... |
| 3494 | 0.2843 | When calculating effective rights and permissions,... |
| 3495 | 0.2842 | Unless specified, the add-on runs with the current... |
| 3496 | 0.2842 | Failed change attempts The Auditing Entry below sh... |
| 3497 | 0.2840 | * You can use a wildcard (*) to replace any number... |
| 3498 | 0.2840 | Unless specified, the script runs with the current... |
| 3499 | 0.2839 | Step 7 – Click Show advanced permissions and selec... |
| 3500 | 0.2838 | • Advanced permissions: ◦ Create files / write dat... |
| 3501 | 0.2838 | Also, consider that all risk metrics and related r... |
| 3502 | 0.2836 | Server — Enter the database server hostname (NetBI... |
| 3503 | 0.2836 | See the Notification to Owners topic for additiona... |
| 3504 | 0.2833 | Only the lowest 9 bits of the calculation result a... |
| 3505 | 0.2832 | In group/Not in group filters don’t not process gr... |
| 3506 | 0.2832 | Event Collection Provide UNC path to a file server... |
| 3507 | 0.2832 | Step 1 – Create a monitoring plan with the wizard.... |
| 3508 | 0.2831 | If selected, change the retention method to Overwr... |
| 3509 | 0.2830 | Specify data collection method You can enable netw... |
| 3510 | 0.2830 | Select to exclude actions performed by specific us... |
| 3511 | 0.2829 | Monitoring plan Limits your search to the selected... |
| 3512 | 0.2829 | Alerts are helpful if you want to be notified abou... |
| 3513 | 0.2828 | omitstorelist.txt Contains a list of SQL Server ob... |
| 3514 | 0.2828 | To specify a non-default port, provide a new port ... |
| 3515 | 0.2827 | For that, the user account will need an administra... |
| 3516 | 0.2827 | Account for Accessing REST API You will also need ... |
| 3517 | 0.2827 | Another o ption is to install the add-on and Audit... |
| 3518 | 0.2826 | Table 2: Windows File Server Dell Data storage Net... |
| 3519 | 0.2826 | The state-in-time reports are available under the ... |
| 3520 | 0.2825 | Specify the account for collecting data Select the... |
| 3521 | 0.2825 | See the Data Grid Features topic for additional in... |
| 3522 | 0.2825 | In the page that opens, navigate to the report you... |
| 3523 | 0.2825 | To verify the necessary settings of the existing p... |
| 3524 | 0.2824 | In the right pane, go to the Intelligence s ection... |
| 3525 | 0.2823 | Object type — monitored object type; for the full ... |
| 3526 | 0.2823 | Depending on the type of the object you want to ex... |
| 3527 | 0.2821 | So you can easily discover what is going on in you... |
| 3528 | 0.2821 | Step 3 – In the Remote Registry Properties dialog ... |
| 3529 | 0.2821 | Step 2 – Select the snapshots that you want to imp... |
| 3530 | 0.2820 | NOCHECK—Do not check Auditor certificat e. Make su... |
| 3531 | 0.2817 | Table 1: Vserver Type Service Name Description Ena... |
| 3532 | 0.2817 | SyslogServerProtocol – communication protocol for ... |
| 3533 | 0.2814 | Compatibility Notice The file must be formatted in... |
| 3534 | 0.2814 | v10.7 7. The add-on starts collecting and forwardi... |
| 3535 | 0.2813 | Configure Parameters for Data Collection In the ad... |
| 3536 | 0.2813 | Step 1 – After the installation, the add-on config... |
| 3537 | 0.2811 | Step 2 – Enable auditing of Oracle Database change... |
| 3538 | 0.2809 | If you want to run the add-on on another machine, ... |
| 3539 | 0.2809 | If you want to run the add-on on another machine, ... |
| 3540 | 0.2809 | If any conflicts are detected with Configure audit... |
| 3541 | 0.2809 | Step 2 – Navigate to Security Settings > Local Pol... |
| 3542 | 0.2808 | For example, computer name or workgroup changes. H... |
| 3543 | 0.2808 | Complete the following fields: Option Description ... |
| 3544 | 0.2808 | NetwrixAuditorPassword – Provide a password for th... |
| 3545 | 0.2806 | See the Monitoring Planstopic for additional infor... |
| 3546 | 0.2804 | Step 2 – Select what type of data you want to excl... |
| 3547 | 0.2803 | Upgrade in progress Database is being upgraded. Al... |
| 3548 | 0.2802 | Table 2: XML <?xml version="1.0" encoding="utf-8"?... |
| 3549 | 0.2801 | Prerequisites Before running the add-on, ensure th... |
| 3550 | 0.2801 | Alerts use the same interface and logic as search.... |
| 3551 | 0.2801 | See the JSmith@domain.com corresponding Micr osoft... |
| 3552 | 0.2798 | Share permissions provide or deny access to the sa... |
| 3553 | 0.2798 | Step 2 – Locate the ConnectWiseSettings.xml file a... |
| 3554 | 0.2798 | Shows the name of the account under which the Who ... |
| 3555 | 0.2798 | The events will be saved into the local repository... |
| 3556 | 0.2798 | Table 2: Option Description v10.7 Options Descript... |
| 3557 | 0.2797 | For example: *,sqlserver1.corp.local, *Access is d... |
| 3558 | 0.2796 | Share permissions provide or deny access to the sa... |
| 3559 | 0.2795 | Step 5 – Make sure the Do not overwrite events (Cl... |
| 3560 | 0.2795 | By default, you will receive data on all risk cate... |
| 3561 | 0.2794 | Step 10 – Assign a less-privileged role to this ac... |
| 3562 | 0.2794 | Step 3 – In the Allow an app or feature through Wi... |
| 3563 | 0.2793 | Specify Windows file share Do not specify a defaul... |
| 3564 | 0.2793 | You can configure advanced audit policies for the ... |
| 3565 | 0.2792 | Table 1: Port Protocol Source Target Purpose 8080 ... |
| 3566 | 0.2791 | Use the omitlogonlist.txt to exclude logon activit... |
| 3567 | 0.2788 | You can use a wildcard (*). For inclusive filters:... |
| 3568 | 0.2788 | Step 6 – Click OK to save the changes and close th... |
| 3569 | 0.2788 | To specify a non-default port, provide a server na... |
| 3570 | 0.2788 | To specify a non-default port, provide a server na... |
| 3571 | 0.2787 | During this time period, the service treats simila... |
| 3572 | 0.2786 | On your Oracle Database Server (target), allow inb... |
| 3573 | 0.2786 | NOTE: If you want to reopen closed tickets, you mu... |
| 3574 | 0.2786 | Table 1: Oracle Database 12c, 18c, 19c Grant SELEC... |
| 3575 | 0.2786 | Auditor Server IP address and port number followed... |
| 3576 | 0.2785 | See the Other Components topic for a dditional inf... |
| 3577 | 0.2783 | Find the Group Policy Object (GPO) that is applied... |
| 3578 | 0.2783 | Read access Use this option to supervise access to... |
| 3579 | 0.2781 | description %AlertDescription% %PreviousTicketRefe... |
| 3580 | 0.2780 | For JSON, a response body contains the ActivityRec... |
| 3581 | 0.2780 | Remember that administrative hidden shares like de... |
| 3582 | 0.2780 | The alerts contain pre-configured filters and in m... |
| 3583 | 0.2780 | At least the first script run should be performed ... |
| 3584 | 0.2779 | v10.7 Retention Default retention period for repos... |
| 3585 | 0.2777 | The My Reviews interface is available to any domai... |
| 3586 | 0.2774 | Run the setup and select the Data Provider for .NE... |
| 3587 | 0.2774 | Collect data for state-in-time reports is switched... |
| 3588 | 0.2772 | To specify a non-default port, provide a server na... |
| 3589 | 0.2772 | See the Amazon Web Services topic for additional i... |
| 3590 | 0.2771 | NOTE: In this case, the product s till collects st... |
| 3591 | 0.2771 | The product collects data from vCenter. Localos us... |
| 3592 | 0.2770 | DOMAIN\username v10.7 File Description Syntax /Tes... |
| 3593 | 0.2770 | * .msExchEdgeSyncCredent ial .msExchMailboxMoveTar... |
| 3594 | 0.2768 | between an object type and a property, the whole e... |
| 3595 | 0.2766 | The user list with all users who provoked alerts a... |
| 3596 | 0.2765 | The add-on will operate as a Syslog listener for t... |
| 3597 | 0.2765 | ◦◦ If you plan to process Active Directory Deleted... |
| 3598 | 0.2764 | Other federation servers you add to the farm will ... |
| 3599 | 0.2764 | If you have multiple Auditor servers, you can spec... |
| 3600 | 0.2764 | attempt) RacNumber=12&Arg1= Received AV Alert The ... |
| 3601 | 0.2764 | Unless specified, the script runs with the current... |
| 3602 | 0.2763 | Step 2 – Receive the response. Activity Records ar... |
| 3603 | 0.2763 | All reviews will be visible on the Entitlement Rev... |
| 3604 | 0.2760 | No items have been added to this Empty data source... |
| 3605 | 0.2759 | This is determined by the following formula: (Lice... |
| 3606 | 0.2759 | Table 1: Sign-In types Action Types Description De... |
| 3607 | 0.2759 | Copy it to a safe location. See the following Micr... |
| 3608 | 0.2759 | Supported editions are Enterprise, Standard and Ex... |
| 3609 | 0.2758 | Table 1: Location Prerequisites Auditor Server • T... |
| 3610 | 0.2757 | Users Select the users whose activity should be re... |
| 3611 | 0.2756 | Step 9 – In the Advanced Deployment Options dialog... |
| 3612 | 0.2756 | If you plan to collect state-in-time data from SQL... |
| 3613 | 0.2755 | Do not select the checkbox if you want to configur... |
| 3614 | 0.2754 | Apply a new service-policy to the SVM LIFs. Run th... |
| 3615 | 0.2754 | Table 1: Option Value Action Set to "Start a progr... |
| 3616 | 0.2754 | Specifies number of threads and TaskLimit 8 queues... |
| 3617 | 0.2754 | The content within the table varies, and additiona... |
| 3618 | 0.2753 | Your notification policy can include any of them. ... |
| 3619 | 0.2751 | You can configure advanced audit policies for the ... |
| 3620 | 0.2751 | ◦◦ *TestVM* — exclude VMs with names containing Te... |
| 3621 | 0.2750 | Default is all databases on selected SQL Server in... |
| 3622 | 0.2750 | To set up a response action, this account must als... |
| 3623 | 0.2748 | See for API Endpoints more information. 404 Not Fo... |
| 3624 | 0.2747 | Remember that administrative hidden shares like de... |
| 3625 | 0.2747 | v10.7 The dashboards includes the following sectio... |
| 3626 | 0.2746 | v10.7 Step 4 – Click Save. Optionally, you can sel... |
| 3627 | 0.2746 | You can use a wildcard (*) to replace any number o... |
| 3628 | 0.2745 | The response body should contain the list of serve... |
| 3629 | 0.2743 | 44.. Hit the Save Auditing Settings button. Accoun... |
| 3630 | 0.2742 | v10.7 Local TCP Port 9003 is opened for inbound co... |
| 3631 | 0.2742 | v10.7 How this change is Item Action Audited repor... |
| 3632 | 0.2741 | To migrate to Unified Auditing for Oracle Database... |
| 3633 | 0.2740 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 3634 | 0.2740 | Step 4 – Click Add to add a new principal. You can... |
| 3635 | 0.2740 | To modify the timeframe, use the drop-down list in... |
| 3636 | 0.2739 | You can enable Auditor to continually enforce the ... |
| 3637 | 0.2739 | Read access Successful Use this option to supervis... |
| 3638 | 0.2739 | To create a filter for user activity monitoring, s... |
| 3639 | 0.2738 | The Browser role is required to generate reports. ... |
| 3640 | 0.2737 | This can be helpful when Auditor detects many acti... |
| 3641 | 0.2737 | To specify a non-default port, provide a server na... |
| 3642 | 0.2735 | When finished, run the gpupdate /force command to ... |
| 3643 | 0.2733 | Microsoft System Center Virtual Machine Manager (S... |
| 3644 | 0.2733 | This permission should be assigned on each domain ... |
| 3645 | 0.2731 | enterprise\NAuser NetwrixAuditorPassword NetwrixIs... |
| 3646 | 0.2731 | You can, for example, open any SSRS-based report u... |
| 3647 | 0.2731 | Send a POST request containing your search paramet... |
| 3648 | 0.2731 | Objects Specify restrictions for the objects to mo... |
| 3649 | 0.2731 | v10.7 NOTE: For additional information about User ... |
| 3650 | 0.2731 | File permissions define who has access to local fi... |
| 3651 | 0.2731 | File permissions define who has access to local fi... |
| 3652 | 0.2730 | Option Description General Name Update a plan name... |
| 3653 | 0.2729 | • Local users and groups—Enables auditing of local... |
| 3654 | 0.2729 | Step 2 – Edit the *.txt files, based on the follow... |
| 3655 | 0.2728 | Predefined reports are helpful if you Predefined r... |
| 3656 | 0.2727 | v10.7 Step 5 – Configure Add-on parameters Prepare... |
| 3657 | 0.2725 | Wildcards (*) are not supported. In addition to th... |
| 3658 | 0.2724 | As a next step, click Add item to specify an objec... |
| 3659 | 0.2723 | Note that the new monitoring scope restrictions ap... |
| 3660 | 0.2721 | Configure Integration API Settings Follow the step... |
| 3661 | 0.2721 | Navigate to Manage → Log Settings → Syslog. 77.. S... |
| 3662 | 0.2719 | Object Permissions in SQL Server This report shows... |
| 3663 | 0.2717 | You will also need to configure Exchange Administr... |
| 3664 | 0.2716 | See the Obtain the Tenant Name topic for additiona... |
| 3665 | 0.2716 | Administrative hidden shares like default system r... |
| 3666 | 0.2715 | Step 5 – Check Allow next to the Read permission. ... |
| 3667 | 0.2714 | Select File permissions option too if you want to ... |
| 3668 | 0.2714 | Select File permissions option too if you want to ... |
| 3669 | 0.2714 | Permission assignment will depend on the data you ... |
| 3670 | 0.2714 | Unless specified, RFC 3164/5424 format is used. If... |
| 3671 | 0.2712 | The My Reviews interface is available if the logge... |
| 3672 | 0.2710 | Table 2: XML Retrieve Activity Records <?xml versi... |
| 3673 | 0.2710 | This value is filled in automatically. Snapshot da... |
| 3674 | 0.2710 | Below is the default hardware configuration for th... |
| 3675 | 0.2709 | Allow outbound connections from the dynamic (1024 ... |
| 3676 | 0.2708 | Failed change attempts The Auditing Entry below sh... |
| 3677 | 0.2707 | Create and Register a New App in Microsoft Entra I... |
| 3678 | 0.2707 | Create and Register a New App in Microsoft Entra I... |
| 3679 | 0.2707 | Create and Register a New App in Microsoft Entra I... |
| 3680 | 0.2706 | Supported Browsers Supported browsers for the Acce... |
| 3681 | 0.2706 | If the Pager property of an AD User contains a ful... |
| 3682 | 0.2706 | For example: This omit list does not affect SELECT... |
| 3683 | 0.2704 | .config.cpuAllocation.s hares .level=low: .config.... |
| 3684 | 0.2703 | A user specified in the Who filter made a lot of c... |
| 3685 | 0.2702 | Check if your Oracle database has already been mig... |
| 3686 | 0.2701 | v10.7 Domain Complete the following fields: Option... |
| 3687 | 0.2701 | To configure audit settings for the CIFS fi le sha... |
| 3688 | 0.2700 | .Net Framework 4.7.2 and above is installed. The c... |
| 3689 | 0.2700 | Step 3 – Click Edit data source on the right. Step... |
| 3690 | 0.2699 | When running Free Community Edition, at any time y... |
| 3691 | 0.2698 | For example: Table 1: Symbol XML entity & e.g., Al... |
| 3692 | 0.2697 | For example, the product Information successfully ... |
| 3693 | 0.2696 | Data will be collected using the SQL Server traces... |
| 3694 | 0.2694 | Reports with review status to track team workflow.... |
| 3695 | 0.2694 | Make sure this account is granted the Content Mana... |
| 3696 | 0.2693 | The UDP 514 port is open for inbound connections. ... |
| 3697 | 0.2692 | Step 6 – Choose modern authentication. Step 7 – En... |
| 3698 | 0.2691 | To report on copy actions on remote file shares, m... |
| 3699 | 0.2690 | You have already identified the intruder (e.g., Ba... |
| 3700 | 0.2690 | Member— role member name. v10.7 Considerations and... |
| 3701 | 0.2689 | No manual configurations are required. Review a fu... |
| 3702 | 0.2688 | Step 3 – In the With parameters field, enter the p... |
| 3703 | 0.2688 | If you want to use a specific account (other than ... |
| 3704 | 0.2688 | If you want to use a specific account (other than ... |
| 3705 | 0.2688 | If you want to use a specific account (other than ... |
| 3706 | 0.2688 | For that, in the Manage historical snapshots secti... |
| 3707 | 0.2687 | A backslash (\) must be put in front of (*), (? ),... |
| 3708 | 0.2686 | Success HTTP/1.1 200 OK Server: Microsoft-HTTPAPI/... |
| 3709 | 0.2685 | Table 1: Option Description General Specify Dell V... |
| 3710 | 0.2684 | A Security Officer wants to monitor a file share, ... |
| 3711 | 0.2684 | A Security Officer wants to monitor a file share, ... |
| 3712 | 0.2684 | Settings for a certain event source (within the So... |
| 3713 | 0.2682 | The Access Reviews application begins to send the ... |
| 3714 | 0.2681 | ◦ .Net Framework 3.5 SP1 is installed on the compu... |
| 3715 | 0.2681 | fields. The MonitoringPlan element contains sub-el... |
| 3716 | 0.2680 | cluster1::>network interface modify -vserver svm -... |
| 3717 | 0.2678 | Failed Use this option to track suspicious activit... |
| 3718 | 0.2674 | By default, Auditor uses the LocalSystem account t... |
| 3719 | 0.2674 | Step 4 – The new secret will be displayed in the l... |
| 3720 | 0.2673 | "sampledomain.sample/sampling", the syntax should ... |
| 3721 | 0.2673 | Review User Profiles and Process Anomalies Review ... |
| 3722 | 0.2671 | If you want to use a specific account (other than ... |
| 3723 | 0.2671 | If you want to use a specific account (other than ... |
| 3724 | 0.2671 | If you want to use a specific account (other than ... |
| 3725 | 0.2671 | If you want to use a specific account (other than ... |
| 3726 | 0.2671 | If you want to use a specific account (other than ... |
| 3727 | 0.2671 | If you want to use a specific account (other than ... |
| 3728 | 0.2671 | Step 2 – In the Help Protect your computer with Wi... |
| 3729 | 0.2669 | Read access is reported for documents and lists an... |
| 3730 | 0.2668 | Filter by organizational unit To audit inactive us... |
| 3731 | 0.2668 | If you configured a dedicated monitoring plan, mak... |
| 3732 | 0.2668 | Then you will provide this account in the monitori... |
| 3733 | 0.2668 | Free Community Edition helps you maintain visibili... |
| 3734 | 0.2668 | Do not specify a default file share mapped to a lo... |
| 3735 | 0.2667 | To audit users for expiring accounts/passwords tha... |
| 3736 | 0.2666 | Process user accounts Select this checkbox to audi... |
| 3737 | 0.2666 | Monitoring plan name,resource path, executable pat... |
| 3738 | 0.2664 | ≥ 25% — High Number of files that have been ≤ 5% —... |
| 3739 | 0.2664 | SharePoint Activity reports Activity Related to Se... |
| 3740 | 0.2664 | To check this, start the Group Policy Management c... |
| 3741 | 0.2663 | Since you are only interested in the way this user... |
| 3742 | 0.2662 | Lines that start with the # sign are treated as co... |
| 3743 | 0.2661 | For example, to report on the database hosted on s... |
| 3744 | 0.2660 | If you want to use a specific account (other than ... |
| 3745 | 0.2660 | Modify plan settings, add or delete data sources, ... |
| 3746 | 0.2660 | Specify additional information to include in repor... |
| 3747 | 0.2659 | A user specified in the Who filter made a lot of c... |
| 3748 | 0.2659 | The default value is 2592000 seconds, i.e., 1 mont... |
| 3749 | 0.2655 | Considerations for gMSA Account If you are using g... |
| 3750 | 0.2652 | Execute... https certificate subject= "Netwrix Int... |
| 3751 | 0.2651 | For example, you can exclude site collections docu... |
| 3752 | 0.2650 | See the Configure Advanced Audit Policies topic fo... |
| 3753 | 0.2650 | Unless an account is specified, the NetwrixAuditor... |
| 3754 | 0.2649 | Unless specified, the script runs with the current... |
| 3755 | 0.2649 | Oracle Object modification under Privileges and ob... |
| 3756 | 0.2648 | Assumes that the add-on runs on the computer hosti... |
| 3757 | 0.2648 | The report is added to the Favorite reports sectio... |
| 3758 | 0.2647 | To specify a non-default port, provide a server na... |
| 3759 | 0.2645 | For example: v1.0\powershell.exe v10.7 In the With... |
| 3760 | 0.2644 | Unless an account is specified, the NetwrixAuditor... |
| 3761 | 0.2643 | IncludeDataSourceToMakeEventId * True Defines whet... |
| 3762 | 0.2643 | The hyperlink will open the Entitlement Reviews in... |
| 3763 | 0.2643 | The Syslog daemon must be configured to redirect e... |
| 3764 | 0.2642 | Configure a threshold-based alert, email recipient... |
| 3765 | 0.2642 | Select a plan and click Edit. On the page that ope... |
| 3766 | 0.2642 | See the Ownership Confirmation Request Email topic... |
| 3767 | 0.2640 | accounts (disable, move, delete) Table 1: File Des... |
| 3768 | 0.2640 | Classname For example: exchangeAdminService msExch... |
| 3769 | 0.2637 | Endure that image file is located in the default d... |
| 3770 | 0.2637 | ◦ Provide this user name and password in the monit... |
| 3771 | 0.2635 | Monitor SSO users/groups on vCenter and Local user... |
| 3772 | 0.2635 | The moment when the change occurred. When When Yes... |
| 3773 | 0.2635 | The servers within the farm are located in differe... |
| 3774 | 0.2633 | v10.7 Step 1 – Go to Configuration > Monitoring pl... |
| 3775 | 0.2633 | The newly created data source will appear in the D... |
| 3776 | 0.2633 | Below is an example of a mask: ◦ * - any machine ◦... |
| 3777 | 0.2632 | Thus, changes made to your Active Directory domain... |
| 3778 | 0.2632 | By default, Personal. ◦ thumbprint—Mandatory, defi... |
| 3779 | 0.2632 | The default period is set to 30 days. Select the r... |
| 3780 | 0.2631 | If you leave this field empty, then the path to th... |
| 3781 | 0.2631 | In the right pane, go to the Intelligence s ection... |
| 3782 | 0.2630 | (514 by default). Auditor Endpoint Auditor Server ... |
| 3783 | 0.2630 | Example: mydomain\user1. Object URL – provide URL ... |
| 3784 | 0.2630 | Modify the timeframe to narrow down the results. T... |
| 3785 | 0.2629 | The Syslog service – main add-on component, Syslog... |
| 3786 | 0.2629 | If there is no such tab, it means a wrong security... |
| 3787 | 0.2628 | Click Change to browse for a different location. W... |
| 3788 | 0.2628 | between an object type and a property, the whole e... |
| 3789 | 0.2626 | Availability group name Enter a name of your SQL S... |
| 3790 | 0.2625 | ), shares used by printers to enable remote admini... |
| 3791 | 0.2624 | A filetype other than one of the types captured ab... |
| 3792 | 0.2624 | Select this checkbox if the implicit SSL mode is u... |
| 3793 | 0.2623 | See the Configure Client Secret topic for addition... |
| 3794 | 0.2623 | ), shares used by printers to enable remote admini... |
| 3795 | 0.2623 | At the end of the first run, the timestamp will be... |
| 3796 | 0.2622 | To force basic audit policies to be ignored and pr... |
| 3797 | 0.2622 | When the selected threshold exceeded, an alert wil... |
| 3798 | 0.2621 | Manage resource Administrator role ownership by as... |
| 3799 | 0.2621 | Select the data source you need (for example, Acti... |
| 3800 | 0.2620 | The procedure below describes how to apply Advance... |
| 3801 | 0.2620 | File Servers Dell Isilon Dell VNX VNXe NetApp Wind... |
| 3802 | 0.2619 | Active Directory tombstones — This option is recom... |
| 3803 | 0.2619 | See Release Notes for details. Related reports Cli... |
| 3804 | 0.2616 | The body is empty. The 404 Not Found Error request... |
| 3805 | 0.2615 | RacNumber=25&Arg1= • Rename / Renamed (Failed atte... |
| 3806 | 0.2614 | AppNameRegExp — If you provide a pattern for appli... |
| 3807 | 0.2613 | For example: ,*,*notepad.exe Windows File Share Co... |
| 3808 | 0.2611 | See the Data Collecting Account topic for addition... |
| 3809 | 0.2611 | Information on alerts that are older than 1 month ... |
| 3810 | 0.2610 | When calculating effective rights and permissions,... |
| 3811 | 0.2609 | See the topics on the monitored items for details.... |
| 3812 | 0.2609 | Table 1: CorrelationTicketFormat Description Previ... |
| 3813 | 0.2609 | See the Role-Based Access and Delegation topic for... |
| 3814 | 0.2607 | To audit users for expiring accounts/passwords tha... |
| 3815 | 0.2606 | Applying Filters Every time you run the script, Au... |
| 3816 | 0.2606 | Sensitive File and Folder Permissions Details This... |
| 3817 | 0.2605 | Once you completed all filters, click Preview on t... |
| 3818 | 0.2605 | The My Reviews interface has two pages: Pending Re... |
| 3819 | 0.2604 | The default CorrelationInterval 2592000 value is 2... |
| 3820 | 0.2601 | <v v= "*ROOTDC1*"/> <n n="localhost"> <a n="DCWith... |
| 3821 | 0.2600 | Table 2: Parameter Default value Description Event... |
| 3822 | 0.2600 | Object type — monitored object type; for the full ... |
| 3823 | 0.2599 | If there is no such tab, it means a wrong security... |
| 3824 | 0.2598 | v10.7 Owners assigned to resources within the Reso... |
| 3825 | 0.2597 | The next time you run the script, it will start re... |
| 3826 | 0.2597 | Assigned owners can log in to complete reviews. Th... |
| 3827 | 0.2596 | Default retention period is 180 days. Table 1: Opt... |
| 3828 | 0.2595 | In the left pane, navigate to Forest: <forest_name... |
| 3829 | 0.2595 | In the left pane, navigate to Forest: <forest_name... |
| 3830 | 0.2595 | v10.7 Option Description General Specify an IP ran... |
| 3831 | 0.2595 | For Security Team & Administrator The Resource Own... |
| 3832 | 0.2595 | NotEqualTo Max length: 536870911. StartsWith EndsW... |
| 3833 | 0.2594 | Select Group membershipif you want to include Grou... |
| 3834 | 0.2594 | Start data collection manually Data collection wil... |
| 3835 | 0.2592 | Table 2: Entry in EventData Activity Record field ... |
| 3836 | 0.2592 | Add a path to the add-on in double quotes and spec... |
| 3837 | 0.2589 | By default, this email is generated daily at 7:00 ... |
| 3838 | 0.2588 | Click Add Exclusion. Then, in the Specify Filters ... |
| 3839 | 0.2588 | Click Add Exclusion. Then, in the Specify Filters ... |
| 3840 | 0.2588 | To.. Do.. Click on a plan name. You will see all d... |
| 3841 | 0.2585 | Consider the following: To exclude a single VM, pr... |
| 3842 | 0.2584 | If you want to use a specific account (other than ... |
| 3843 | 0.2584 | If you want to use a specific account (other than ... |
| 3844 | 0.2582 | Table 1: Option Description Logging level Select I... |
| 3845 | 0.2582 | Alerts Configure alerts that will be triggered by ... |
| 3846 | 0.2581 | (514 by default). v10.7 Click Proceed and complete... |
| 3847 | 0.2581 | Allow the following process to use the port: %syst... |
| 3848 | 0.2580 | Clear imported data Select to delete all previousl... |
| 3849 | 0.2577 | The score, that is between 1 and 100 points, refle... |
| 3850 | 0.2575 | v10.7 Database Page The Access Reviews application... |
| 3851 | 0.2573 | See the Reports with Video topic for additional in... |
| 3852 | 0.2572 | If you want to use a specific account (other Table... |
| 3853 | 0.2571 | Set the TNS_ADMIN environment variable to the dire... |
| 3854 | 0.2570 | Under the Syslog Servers, complete the following f... |
| 3855 | 0.2570 | Monitor VMware configuration changes Configuration... |
| 3856 | 0.2570 | See the Monitoring Planstopic for additional infor... |
| 3857 | 0.2570 | You can enable Auditor to continually enforce the ... |
| 3858 | 0.2570 | Assign Permission to Read the Registry Key This pe... |
| 3859 | 0.2566 | • Run the setup and select the Data Provider for .... |
| 3860 | 0.2566 | The resource name can be a FQDN or NETBIOS server ... |
| 3861 | 0.2566 | Table 1: Port Protocol Source Target Purpose 389 T... |
| 3862 | 0.2563 | Is anyone who is charge of "Failed..." anomaly a b... |
| 3863 | 0.2560 | Table 1: File Description Syntax adomiteventuserli... |
| 3864 | 0.2560 | The subscription (email attachment or file uploade... |
| 3865 | 0.2559 | Users can also configure Only the latest snapshot ... |
| 3866 | 0.2558 | This permission should be assigned on each domain ... |
| 3867 | 0.2556 | For example, 1, 3, 5-99. You can also exclude unwa... |
| 3868 | 0.2556 | Max length: 536870911. • Contains (default) • Does... |
| 3869 | 0.2555 | Table 1: Option Description You must be assigned t... |
| 3870 | 0.2555 | See the Export A ctivity Records topic for a dditi... |
| 3871 | 0.2554 | If you have not specified the default settings bef... |
| 3872 | 0.2553 | Unless specified, the add-on runs with the current... |
| 3873 | 0.2553 | Group Managed Service Account (gMSA). You should s... |
| 3874 | 0.2552 | Error message text v10.7 File Description Syntax C... |
| 3875 | 0.2551 | CorrelationInterval 2592000 Specify the time perio... |
| 3876 | 0.2550 | Thus, changes made to your Active Directory domain... |
| 3877 | 0.2549 | omituserlist.txt Contains a list of users you want... |
| 3878 | 0.2549 | To import snapshots, you must be assigned the Glob... |
| 3879 | 0.2548 | v10.7 Option Description monitoring plan you are g... |
| 3880 | 0.2546 | State-in-time reports For each SharePoint site col... |
| 3881 | 0.2546 | Table 1: Parameter Description Company Organizatio... |
| 3882 | 0.2546 | See the Resource Owners Overview topic for additio... |
| 3883 | 0.2544 | 14 actFolderCreated String9 The new folder URL v10... |
| 3884 | 0.2543 | Delete event Yes Message with subject <...> was mo... |
| 3885 | 0.2543 | Unless specified, the script runs with the current... |
| 3886 | 0.2542 | A custom account must be granted the same permissi... |
| 3887 | 0.2541 | collect state-in-time data for this folder. Table ... |
| 3888 | 0.2540 | You should specify only the account name in the do... |
| 3889 | 0.2539 | Customizing Metrics for Your Organization Default ... |
| 3890 | 0.2538 | Depending on the type of the object you want to ex... |
| 3891 | 0.2537 | Who Shows the name of the account under which the ... |
| 3892 | 0.2537 | Attach Activity Summary as a CSV file — You can co... |
| 3893 | 0.2536 | See the Review User Profiles and Process Anomalies... |
| 3894 | 0.2536 | Step 1 – On the main Auditor page, click the Alert... |
| 3895 | 0.2535 | See the Navigation topic for information on each o... |
| 3896 | 0.2535 | Automate Add-On Execution To ensure you feed the m... |
| 3897 | 0.2535 | Automate Add-On Execution To ensure you feed the m... |
| 3898 | 0.2534 | Table 1: Option Description General Specify a comp... |
| 3899 | 0.2534 | For example, to report on the database hosted on s... |
| 3900 | 0.2534 | Select this checkbox to write data to a SQL Server... |
| 3901 | 0.2532 | Make sure the account has sufficient permissions t... |
| 3902 | 0.2531 | See the Export A ctivity Records topic for a dditi... |
| 3903 | 0.2530 | Table 2: Option Description Specify Active Directo... |
| 3904 | 0.2530 | Table 2: Option Description Specify Active Directo... |
| 3905 | 0.2529 | See the Data C ollecting Account topic for additio... |
| 3906 | 0.2528 | DNS AAAA • Container name • IPv6 Address • Owner n... |
| 3907 | 0.2528 | Step 3 – Provide Auditor Server IP address and por... |
| 3908 | 0.2525 | The My Reviews interface is available if the logge... |
| 3909 | 0.2525 | Adjust the audit policy settings using the Active ... |
| 3910 | 0.2523 | Wildcard (*) is supported to replace any number of... |
| 3911 | 0.2521 | Each parameter is preceded with a dash; a space se... |
| 3912 | 0.2520 | Right-click the effective domain controllers polic... |
| 3913 | 0.2520 | v10.7 Follow the steps to restore original look. S... |
| 3914 | 0.2520 | v10.7 It has the following pages: Console Access P... |
| 3915 | 0.2519 | Changes (per transaction) to collect and report: I... |
| 3916 | 0.2517 | In the left pane, navigate to Forest: <forest_name... |
| 3917 | 0.2516 | Optionally, you can select Download to edit the ma... |
| 3918 | 0.2515 | Use this report to Files and Folders Categories by... |
| 3919 | 0.2514 | Administrator & Privileged Role Administrator & Te... |
| 3920 | 0.2514 | Term Archive. Error validating request parameters ... |
| 3921 | 0.2512 | NOTE: Make sure that the Send alert when the actio... |
| 3922 | 0.2511 | User (domain\account) – select a specific user to ... |
| 3923 | 0.2511 | In the search box, type Mail.ReadWrite and Mail.Se... |
| 3924 | 0.2511 | Click Close to return to the review. Review Histor... |
| 3925 | 0.2511 | Under Log/Monitoring, expand the User Access link.... |
| 3926 | 0.2509 | Hover over a status icon to display its tooltip. T... |
| 3927 | 0.2508 | This is usually the combination of the user's firs... |
| 3928 | 0.2508 | v10.7 Prerequisites Before running the add-on, ens... |
| 3929 | 0.2508 | ADPermission #RBAC: -MailboxAuditLogSearch -AdminA... |
| 3930 | 0.2505 | Domain Complete the following fields: Option Descr... |
| 3931 | 0.2505 | See Permissions for VMware Server Auditing topic f... |
| 3932 | 0.2504 | Non-owner Mailbox Access Audit: Manual Configurati... |
| 3933 | 0.2502 | For Dell VNX: server_security <NAS Server Name> -u... |
| 3934 | 0.2502 | To create a filter for user activity monitoring, s... |
| 3935 | 0.2501 | Certificate Thumbprint AB:BB:CC—Check Auditor Serv... |
| 3936 | 0.2501 | Add Items for Monitoring Once you completed monito... |
| 3937 | 0.2501 | ◦ If you plan to process the Active Directory Dele... |
| 3938 | 0.2500 | The default value is 3600 seconds, i.e., 1 hour. C... |
| 3939 | 0.2500 | Click Show user activity below the total risk scor... |
| 3940 | 0.2499 | For example, "company.local". Specify the account ... |
| 3941 | 0.2499 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 3942 | 0.2499 | Use U nified and Standard audit policies to keep t... |
| 3943 | 0.2499 | Note that the new monitoring scope restrictions ap... |
| 3944 | 0.2497 | Table 1: Option Description Auditor Endpoint Audit... |
| 3945 | 0.2497 | Table 1: Option Description Auditor Endpoint Audit... |
| 3946 | 0.2496 | You are investigating a security incident and want... |
| 3947 | 0.2496 | String9 The internal message URL 5 actMessageDelet... |
| 3948 | 0.2495 | Examples: http://siteCollection1:3 https://siteCol... |
| 3949 | 0.2493 | If you are using Oracle Real Application Clusters ... |
| 3950 | 0.2492 | Review Details Window The View Details button at t... |
| 3951 | 0.2492 | Step 2 – If you are running VMware 6.0, connect to... |
| 3952 | 0.2492 | For example: By default, the list contains add own... |
| 3953 | 0.2491 | v10.7 Option Description Auditor Server IP address... |
| 3954 | 0.2491 | Instances are named with date timestamps indicatin... |
| 3955 | 0.2491 | A custom account must be granted the same permissi... |
| 3956 | 0.2490 | See the Configuring client secret topic for additi... |
| 3957 | 0.2490 | See the Create a New Monitoring Plan topic for add... |
| 3958 | 0.2487 | Table 1: Port Protocol Source Target Purpose 9898 ... |
| 3959 | 0.2487 | Use case Related documentation Active Directory I ... |
| 3960 | 0.2486 | Follow the step to configure integration service s... |
| 3961 | 0.2486 | Add a path to the add-on in double quotes and spec... |
| 3962 | 0.2485 | If you want to run the add-on on another machine, ... |
| 3963 | 0.2484 | The attributes marked with * are reported without ... |
| 3964 | 0.2482 | The gMSA also helps to ensure that service account... |
| 3965 | 0.2482 | Step 3 – In the Group Policy Management Editor dia... |
| 3966 | 0.2482 | Add a path to the add-on in double quotes and spec... |
| 3967 | 0.2481 | ), shares used by printers to enable remote admini... |
| 3968 | 0.2480 | Wildcard (*) is supported. For example, to report ... |
| 3969 | 0.2480 | v10.7 Configure the following: Setting Description... |
| 3970 | 0.2478 | or moved, and emails sent. Since you are intereste... |
| 3971 | 0.2477 | The status is 200 OK. For XML, a response body con... |
| 3972 | 0.2477 | Follow the steps to configure Audit Object Access ... |
| 3973 | 0.2477 | File Description Syntax monitoring plan name,serve... |
| 3974 | 0.2474 | This automatically downloads the file. See the Dat... |
| 3975 | 0.2474 | Format Select None. Click Submit. The new server i... |
| 3976 | 0.2473 | DataCollection DataCollectionServer (empty) Specif... |
| 3977 | 0.2471 | The RADIUS server The account collecting RADIUS lo... |
| 3978 | 0.2470 | Certificate Thumbprint AB:BB:CC—Check Auditor Serv... |
| 3979 | 0.2469 | Computer Select the account that will be used to c... |
| 3980 | 0.2465 | Set up the auditing as described in Planning and P... |
| 3981 | 0.2465 | Data collector for this data source is not respond... |
| 3982 | 0.2463 | The platform provides security analytics to detect... |
| 3983 | 0.2463 | Note that the new monitoring scope restrictions ap... |
| 3984 | 0.2463 | Use this report to identify data at high risk and ... |
| 3985 | 0.2463 | Membership in one of the following groups: Adminis... |
| 3986 | 0.2463 | The following choices are available: User/password... |
| 3987 | 0.2462 | Review user actions and compare them to his or her... |
| 3988 | 0.2462 | Possible values: Database, Server Instance. Permis... |
| 3989 | 0.2461 | The following choices are available: User/password... |
| 3990 | 0.2460 | Creating and registering a new app in Microsoft En... |
| 3991 | 0.2459 | Click the Details link to examine the product log.... |
| 3992 | 0.2459 | Step 4 – Do not specify a default file share mappe... |
| 3993 | 0.2458 | For an exact match, use quotation marks and provid... |
| 3994 | 0.2458 | They need to set report filters as follows: Monito... |
| 3995 | 0.2456 | When reverting to a snapshot, the tool reviews the... |
| 3996 | 0.2454 | JSON may contain a ContinuationMark object. Each F... |
| 3997 | 0.2445 | SenderSleepTime 30 Specifies retry interval in sec... |
| 3998 | 0.2445 | URI Reference Only specify URI reference to a list... |
| 3999 | 0.2444 | snapshot_modify_snapshot A snapshot was modified. ... |
| 4000 | 0.2443 | Step 4 – In the left pane, select Containers and C... |
| 4001 | 0.2441 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 4002 | 0.2441 | The resource is returned to a ‘Waiting’ status, re... |
| 4003 | 0.2439 | For example: dsacls "CN=Deleted Objects,DC=Corp,DC... |
| 4004 | 0.2439 | The default values is 900 seconds, i.e., 15 minute... |
| 4005 | 0.2438 | Step 5 – Run the installation package. Step 6 – Ac... |
| 4006 | 0.2438 | Review and Pin Risks Follow the steps to review ri... |
| 4007 | 0.2437 | If you want to monitor user-defined hidden shares,... |
| 4008 | 0.2437 | If you want to monitor user-defined hidden shares,... |
| 4009 | 0.2437 | Select Monitor userdefined hidden shares if necess... |
| 4010 | 0.2437 | Select Monitor userdefined hidden shares if necess... |
| 4011 | 0.2436 | Clicking the tile opens the Behavior Anomalies das... |
| 4012 | 0.2436 | While inputting text inline is easy, your baseline... |
| 4013 | 0.2434 | Recipients RECOMMENDED: click Send Test Email. The... |
| 4014 | 0.2434 | Assign Permission To Read the Registry Key NOTE: T... |
| 4015 | 0.2433 | Shows whether the account has the "User Yes User m... |
| 4016 | 0.2433 | Max length: 255. • Contains (default) • DoesNotCon... |
| 4017 | 0.2432 | Table 1: Option Description Consider the following... |
| 4018 | 0.2431 | NOTE: If you are going to configure monitoring rul... |
| 4019 | 0.2431 | Step 2 – Select Settings > Email and Alerts > Sysl... |
| 4020 | 0.2431 | Type the minus sign before selected event ID. For ... |
| 4021 | 0.2430 | You can also configure and receive alerts on the e... |
| 4022 | 0.2430 | RADIUSPassword Current user credentials Provide a ... |
| 4023 | 0.2429 | Example: CN=MJones,CN=Users,DC=enterprisedc1,DC=en... |
| 4024 | 0.2429 | When configuring the IncludeDataSourceToMakeEventI... |
| 4025 | 0.2429 | Filtered business hours during the last data will ... |
| 4026 | 0.2429 | Use the following format: <parameter>value</parame... |
| 4027 | 0.2428 | This mode allows you to get a sufficient level of ... |
| 4028 | 0.2428 | Example: CN=MJones,CN=Users,DC=enterprisedc1,DC=en... |
| 4029 | 0.2428 | See the RoleBased Access and Delegation topic for ... |
| 4030 | 0.2427 | Send report to administrators Enable this option a... |
| 4031 | 0.2426 | The image is also configured to use Microsoft Edge... |
| 4032 | 0.2426 | To enable the policy 1. On the audited server, ope... |
| 4033 | 0.2426 | XLarge Evaluation, PoC Regular Large Hardware envi... |
| 4034 | 0.2426 | The account used to run the application must be a ... |
| 4035 | 0.2425 | Step 1 – On the main Auditor page, click the Repor... |
| 4036 | 0.2425 | will be reported, but the Who value will be "syste... |
| 4037 | 0.2425 | You can use full or relative path. v10.7 Parameter... |
| 4038 | 0.2424 | When adding a DFS file share for auditing, specify... |
| 4039 | 0.2423 | This interface has multiple pages: Manage Reviews ... |
| 4040 | 0.2422 | Use semicolon to separate several names. Filter by... |
| 4041 | 0.2420 | • PowerShell connections: ◦ 5985 - for HTTP ◦ 5986... |
| 4042 | 0.2420 | XML <?xml version="1.0" encoding="UTF-8" ?> <Activ... |
| 4043 | 0.2419 | NotEqualTo Max length: 1073741822. StartsWith Ends... |
| 4044 | 0.2419 | Partners and MSPs who are logged into the Netwrix ... |
| 4045 | 0.2419 | Since the intruder can be the actor (Who), the obj... |
| 4046 | 0.2418 | Example: http:// sitecollection/list/document.docx... |
| 4047 | 0.2416 | Review the following for additional information: T... |
| 4048 | 0.2416 | Until then, data collection will not be performed.... |
| 4049 | 0.2416 | Until then, data collection will not be performed.... |
| 4050 | 0.2415 | See the File Servers topic for additional informat... |
| 4051 | 0.2413 | You should also provide links to the appropriate t... |
| 4052 | 0.2412 | The Action filt er in the Advanced mode contains a... |
| 4053 | 0.2411 | When prompted, accept the end-user license agreeme... |
| 4054 | 0.2410 | Facility Netwrix recommends using default values. ... |
| 4055 | 0.2410 | Credentials for connection to Nutanix Prism server... |
| 4056 | 0.2409 | Use this report to review the permissions granted ... |
| 4057 | 0.2407 | For each user account listed, this report shows th... |
| 4058 | 0.2406 | Allows specifying a user by name. User name For ex... |
| 4059 | 0.2405 | Not responding Data collector for this data source... |
| 4060 | 0.2403 | This helps to optimize solution performance during... |
| 4061 | 0.2403 | Port Protocol Source Target Purpose LDAP Netwrix A... |
| 4062 | 0.2403 | The option is Enforce certificate validation to en... |
| 4063 | 0.2402 | Console Users with Security Team role ◦◦ Visibilit... |
| 4064 | 0.2399 | Events collected from any other source will be ign... |
| 4065 | 0.2398 | Table 1: Criteria Data model Description DataSourc... |
| 4066 | 0.2397 | The account collecting RADIUS logon events is memb... |
| 4067 | 0.2396 | Step 3 – Run the installation package. Step 4 – Ac... |
| 4068 | 0.2396 | Step 3 – Run the installation package. Step 4 – Ac... |
| 4069 | 0.2395 | An entity (file, link, directory) from the file st... |
| 4070 | 0.2394 | Specify the recipients who will receive daily a ct... |
| 4071 | 0.2392 | • DHCP configuration—Enables auditing of DHCP conf... |
| 4072 | 0.2392 | Finished On — Date timestamp when the review is ma... |
| 4073 | 0.2391 | Logging facility Leave empty. v10.7 # logging secu... |
| 4074 | 0.2390 | In this case, you will only be able to receive act... |
| 4075 | 0.2390 | After No ntext The new value of the modified prope... |
| 4076 | 0.2389 | Filters You can narrow your reporting scope using ... |
| 4077 | 0.2389 | The ActivityRecordSearch root element includes the... |
| 4078 | 0.2388 | Tickets for new alert types are created immediatel... |
| 4079 | 0.2387 | See the Data C ollecting Account topic for additio... |
| 4080 | 0.2386 | To force basic audit policies to be ignored and pr... |
| 4081 | 0.2386 | Clicking the Expand group membership link opens th... |
| 4082 | 0.2385 | Thus, only the latest snapshot is available for on... |
| 4083 | 0.2384 | AlienVault USM 53 UDP/TCP Script host DNS Server D... |
| 4084 | 0.2383 | * @172.28.18.25:514;RSYSLOG_SyslogProt ocol23Forma... |
| 4085 | 0.2382 | For example: -file "C:\Addons\Netwrix_Auditor_Addo... |
| 4086 | 0.2382 | To force basic audit policies to be ignored and pr... |
| 4087 | 0.2382 | 0% — Low (0% - 3%) — Medium ≥ 3% — High Documents ... |
| 4088 | 0.2380 | In case all required components have been already ... |
| 4089 | 0.2379 | Use the server_name\instance_name format, for exam... |
| 4090 | 0.2379 | Select Monitor user-defined hidden shares if neces... |
| 4091 | 0.2378 | See the procedure below for a file share that cont... |
| 4092 | 0.2375 | v10.7 The timeout parameter is configured within t... |
| 4093 | 0.2371 | Use other options (Computer, IP range to specify t... |
| 4094 | 0.2371 | Use other options (Computer, IP range to specify t... |
| 4095 | 0.2371 | Use other options (Computer, IP range to specify t... |
| 4096 | 0.2370 | Remember, deploy the add-on on the same machine wi... |
| 4097 | 0.2370 | This helps to optimize solution performance during... |
| 4098 | 0.2369 | Specify monitoring restrictions Specify restrictio... |
| 4099 | 0.2369 | Specify monitoring restrictions Specify restrictio... |
| 4100 | 0.2368 | Then specify how you want the report to be deliver... |
| 4101 | 0.2368 | Then specify how you want the report to be deliver... |
| 4102 | 0.2368 | Then specify how you want the report to be deliver... |
| 4103 | 0.2368 | Then specify how you want the report to be deliver... |
| 4104 | 0.2368 | Then specify how you want the report to be deliver... |
| 4105 | 0.2368 | Then specify how you want the report to be deliver... |
| 4106 | 0.2367 | Internal parameter. The service can store the acti... |
| 4107 | 0.2366 | Review the full list in the Reported Attributes Re... |
| 4108 | 0.2365 | Delete folder Yes Folder <...> was moved from fold... |
| 4109 | 0.2365 | You must be assigned the Global administrator or t... |
| 4110 | 0.2365 | You must be assigned the Global administrator or t... |
| 4111 | 0.2365 | You must be assigned the Global administrator or t... |
| 4112 | 0.2364 | Deployment Scenarios The add-on can be deployed on... |
| 4113 | 0.2362 | The credentials are case sensitive. A custom accou... |
| 4114 | 0.2360 | On the ServiceNow side ServiceNow version should b... |
| 4115 | 0.2357 | Select Monitor user-defined hidden shares if neces... |
| 4116 | 0.2357 | Use default SQL Server settings Select this option... |
| 4117 | 0.2357 | Account details to show — set of AD attributes to ... |
| 4118 | 0.2354 | All filters are applied using AND logic. Depending... |
| 4119 | 0.2353 | To disable outgoing NTLM authentication traffic vi... |
| 4120 | 0.2353 | Settings for a certain event source (within the So... |
| 4121 | 0.2351 | Step 2 – If some issues occurred due to the lack o... |
| 4122 | 0.2350 | Scheduled Tasks Account Name Application Comment S... |
| 4123 | 0.2347 | State description ORCapacity error Size limit for ... |
| 4124 | 0.2346 | For example: Exchange_Server.Adminis trativeGroup ... |
| 4125 | 0.2346 | v10.7 For example, you can create a gMSA using the... |
| 4126 | 0.2341 | To add items right after finishing the monitoring ... |
| 4127 | 0.2341 | Step 9 – Open Microsoft Entra ID portal and remove... |
| 4128 | 0.2340 | The following audit permissions must be set to "Su... |
| 4129 | 0.2340 | Use other options (Computer, IP range to specify t... |
| 4130 | 0.2340 | Use other options (Computer, IP range to specify t... |
| 4131 | 0.2340 | Use other options (Computer, IP range to specify t... |
| 4132 | 0.2340 | Use other options (Computer, IP range to specify t... |
| 4133 | 0.2337 | In the Maximum Password Age Setting dialog that op... |
| 4134 | 0.2335 | Thus, you will need to prepare an Microsoft 365 us... |
| 4135 | 0.2335 | Step 7 – Enter Application ID and Application secr... |
| 4136 | 0.2333 | Execute... APIAdminTool.exe api disable Disable AP... |
| 4137 | 0.2332 | Use this tile to inspect the trend. v10.7 Top 5 al... |
| 4138 | 0.2332 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 4139 | 0.2332 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 4140 | 0.2332 | Unless an account is specified, the service runs u... |
| 4141 | 0.2331 | Activity Specify monitoring restrictions Specify r... |
| 4142 | 0.2330 | -InboxRule, -MailboxAutoReplyConfiguration, SetMai... |
| 4143 | 0.2330 | Example: WALLET_LOCATION = (SOURCE = (METHOD = fil... |
| 4144 | 0.2325 | If you want to run the add-on on another machine, ... |
| 4145 | 0.2323 | Step 1 – On the Pending Reviews page, select the r... |
| 4146 | 0.2322 | You are investigating an incident Limits your sear... |
| 4147 | 0.2320 | Associate a risk score with the alert — Assign a r... |
| 4148 | 0.2320 | The ActivityRecordSearch root element includes the... |
| 4149 | 0.2320 | Click the Details link to examine the product log.... |
| 4150 | 0.2316 | {DataSource ID} Depending on Task Category -ORSetD... |
| 4151 | 0.2315 | Configuration If you are using Oracle Wallet to co... |
| 4152 | 0.2315 | Enable this option and specify one or several emai... |
| 4153 | 0.2314 | Step 4 – Specify syslog server parameters: Paramet... |
| 4154 | 0.2313 | You can also create a subscription to any report y... |
| 4155 | 0.2310 | Table 1: Item Action Audited How this change is re... |
| 4156 | 0.2309 | 55.. Run the following command to update group pol... |
| 4157 | 0.2309 | Edit the template by deleting or inserting informa... |
| 4158 | 0.2307 | Follow the steps to install Oracle Instant Client ... |
| 4159 | 0.2307 | Step 2 – Define operational parameters such as Aud... |
| 4160 | 0.2306 | Message with subject <...> Move email to another Y... |
| 4161 | 0.2306 | • Oracle Wallet – select if you want to use Oracle... |
| 4162 | 0.2306 | Example: C:\Powershellscripts\old scripts\script.p... |
| 4163 | 0.2305 | Active Directory Page The Access Reviews applicati... |
| 4164 | 0.2305 | Service accounts (svc_%) must be skipped in the re... |
| 4165 | 0.2305 | • Starting with add-on build 1.0.12.0, TLS 1.2 pro... |
| 4166 | 0.2305 | Step 5 – You can use a wildcard (*) only if you ne... |
| 4167 | 0.2305 | Step 5 – You can use a wildcard (*) only if you ne... |
| 4168 | 0.2304 | Netwrixrecommends scheduling a daily task. Step 4 ... |
| 4169 | 0.2304 | Step 3 – Download the Add-On. Step 4 – Configure A... |
| 4170 | 0.2304 | Click Add Rule and configure the following: v10.7 ... |
| 4171 | 0.2302 | All filters are applied using AND logic. Depending... |
| 4172 | 0.2302 | Select Add User. v10.7 Scope Roles Global administ... |
| 4173 | 0.2302 | Click Browse to select from the list of containers... |
| 4174 | 0.2302 | omituserlist.txt Contains a list of user names to ... |
| 4175 | 0.2301 | Step 5 – Review the <CorrelationTicketFormat> sect... |
| 4176 | 0.2300 | Filter Description Supported Operators Contains (d... |
| 4177 | 0.2300 | Step 4 – Accept the license agreement and follow t... |
| 4178 | 0.2299 | Note that the new monitoring scope restrictions ap... |
| 4179 | 0.2298 | Table — Specify database table to monitor. Column—... |
| 4180 | 0.2298 | Network Devices NOTE: Prior to configuring your mo... |
| 4181 | 0.2298 | See the Use Group Managed Service Account (gMSA) t... |
| 4182 | 0.2298 | See the procedure below for details. NOTE: In this... |
| 4183 | 0.2293 | See the Data C ollecting Account topic for additio... |
| 4184 | 0.2293 | Admin A message or any of its pro perties Admin Co... |
| 4185 | 0.2292 | Risk Assessment, Compliance Mapping, Live News, an... |
| 4186 | 0.2291 | https://URL For example: https:// Corp.sharepoint.... |
| 4187 | 0.2290 | If you are using Netwrix Auditor for Network Devic... |
| 4188 | 0.2289 | OneDrive for Business changes are reported as Shar... |
| 4189 | 0.2288 | Right-click the effective domain controllers polic... |
| 4190 | 0.2287 | Table 1: Option Value Action Set to "Start a progr... |
| 4191 | 0.2287 | Event Description fs_create_directory A new direct... |
| 4192 | 0.2284 | Empty No items have been added to this data source... |
| 4193 | 0.2284 | Do one of the following depending on the OS: To co... |
| 4194 | 0.2283 | Enabled accounts —total number of enabled accounts... |
| 4195 | 0.2282 | See the Create and Register a New App in Microsoft... |
| 4196 | 0.2281 | ), and/or values in the To and From. LastSevenDays... |
| 4197 | 0.2281 | To be able to perform the test run, current user a... |
| 4198 | 0.2280 | On the target SQL Server: 11.. To access SQL Serve... |
| 4199 | 0.2280 | If a change seems unauthorized, or requires furthe... |
| 4200 | 0.2280 | Service Team Service team that will be responsible... |
| 4201 | 0.2278 | Execute the following command: Table 1: Track... S... |
| 4202 | 0.2277 | Step 3 – Add script parameters. The console will l... |
| 4203 | 0.2274 | v10.7 Option Setting Rule Type Program Specify the... |
| 4204 | 0.2274 | Step 3 – In the Windows Firewall with Advanced Sec... |
| 4205 | 0.2274 | Rotating certificate s Collect activity and State-... |
| 4206 | 0.2273 | To prevent this, consider the recommendations and ... |
| 4207 | 0.2273 | Step 3 – Navigate to Users tab and click Add next ... |
| 4208 | 0.2272 | To make Windows operating system use more secure p... |
| 4209 | 0.2272 | • XML: <ActivityRecord><Action>Modified</Acti on><... |
| 4210 | 0.2272 | See the Create Alerts topic for additional informa... |
| 4211 | 0.2272 | Default value is -1 (switch off concurrent forward... |
| 4212 | 0.2271 | Option Setting Rule Type Program Specify the path ... |
| 4213 | 0.2270 | Step 2 – Go to Manage > API permissions and click ... |
| 4214 | 0.2269 | Resource Owners Interface The Resource Owners inte... |
| 4215 | 0.2265 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 4216 | 0.2264 | The Resource Review page opens to the 1 Make chang... |
| 4217 | 0.2263 | Max length: 1073741822. • Contains (default) • Doe... |
| 4218 | 0.2261 | You v10.7 can always adjust risk scores over time ... |
| 4219 | 0.2261 | See the To Enable JavaScript topic for additional ... |
| 4220 | 0.2260 | Check "Failed" next to the following permissions: ... |
| 4221 | 0.2259 | This functionality is currently available for the ... |
| 4222 | 0.2258 | Opens the Send Send Reminders Reminders window, wh... |
| 4223 | 0.2257 | Step 2 – Within the monitoring plan window, highli... |
| 4224 | 0.2257 | d625dccec0a8016700a22a0 assignment_ group NOTE: Yo... |
| 4225 | 0.2254 | Notifications Notification settings are configured... |
| 4226 | 0.2253 | Starting with add-on build 1.0.12.0, TLS 1.2 proto... |
| 4227 | 0.2253 | Step 4 – The new secret will be displayed in the l... |
| 4228 | 0.2253 | See the Grant Permissions for the Deleted Objects ... |
| 4229 | 0.2248 | You can also: Select a particular computer type to... |
| 4230 | 0.2248 | For more information about authentication, refer t... |
| 4231 | 0.2247 | You can also configure and receive alerts on the e... |
| 4232 | 0.2247 | For example: Set-Item wsman:\localhost\Client\ Tru... |
| 4233 | 0.2245 | More informative subject lines in email notificati... |
| 4234 | 0.2244 | For search subscription, you can also select a par... |
| 4235 | 0.2243 | However, the OU itself will not be excluded. dc11.... |
| 4236 | 0.2243 | User Activity Select to exclude actions performed ... |
| 4237 | 0.2243 | Reason: Computer Reason type System state changed ... |
| 4238 | 0.2242 | Select this checkbox if your SMTP server requires ... |
| 4239 | 0.2242 | In this scenario, you only deploy Auditor Server a... |
| 4240 | 0.2241 | Or simply drag and drop the add-on file in the con... |
| 4241 | 0.2240 | The maximum number of Activity Record requests the... |
| 4242 | 0.2240 | Licenses – Example: Microsoft 365 E1 – The user or... |
| 4243 | 0.2239 | Tool-tips display when hovering over the icons ind... |
| 4244 | 0.2238 | For example, it helps monitor the usage of SUDO as... |
| 4245 | 0.2238 | Filters You can narrow your reporting scope using ... |
| 4246 | 0.2238 | Filters You can narrow your reporting scope using ... |
| 4247 | 0.2236 | Cores Per Processor Restore from snapshot Memory S... |
| 4248 | 0.2232 | Step 4 – Configure resource ownership through the ... |
| 4249 | 0.2232 | Adjust video duration Limit video file length by a... |
| 4250 | 0.2231 | Users with the Configurator role can create plans ... |
| 4251 | 0.2231 | Infrastructure Table 1: Risk Assessment formula De... |
| 4252 | 0.2230 | To learn more about user activity, you can drill-d... |
| 4253 | 0.2227 | Lines that start with the # sign are treated as co... |
| 4254 | 0.2223 | Table 1: Parameter Description proxyaddress Specif... |
| 4255 | 0.2222 | Define the Log On As a Service Policy On the Logon... |
| 4256 | 0.2222 | Add-On Parameters To configure the add-on paramete... |
| 4257 | 0.2221 | Allow outbound connections to remote ports on the ... |
| 4258 | 0.2219 | classname.attrname=intel ligiblename For example, ... |
| 4259 | 0.2217 | The service can store the Activity Record requests... |
| 4260 | 0.2215 | Configure the following: • Notify users if someone... |
| 4261 | 0.2213 | These settings cannot be modified for a certain pl... |
| 4262 | 0.2213 | Step 3 – Assign the required permissions. Permissi... |
| 4263 | 0.2212 | See the Use Group Managed Service Account (gMSA) t... |
| 4264 | 0.2212 | If necessary, enable threshold to trigger the new ... |
| 4265 | 0.2211 | User SID For example: <v v="*S-1-5-21-11806992 -87... |
| 4266 | 0.2208 | Refer to the Netwrix Privilege Secure documentatio... |
| 4267 | 0.2208 | IP Range Complete the following fields: Table 1: O... |
| 4268 | 0.2207 | Step 3 – Specify a data source. Step 4 – Configure... |
| 4269 | 0.2207 | object_type.property_na me If there is no separato... |
| 4270 | 0.2205 | Check your Visual Studio Redistributable version. ... |
| 4271 | 0.2205 | Devices 514 UDP Service host devices However, you ... |
| 4272 | 0.2204 | Helps identify who accessed important files beside... |
| 4273 | 0.2204 | You may want to modify these settings, for example... |
| 4274 | 0.2203 | DC_name For example: <v v= "*ROOTDC1*"/> <n n="Hub... |
| 4275 | 0.2202 | Filter — Select general type of filter (e.g., "Who... |
| 4276 | 0.2201 | This option is helpful if you want to see if there... |
| 4277 | 0.2200 | If Modern Authentication is used: ◦ Microsoft Entr... |
| 4278 | 0.2200 | between an object type and aproperty, the whole en... |
| 4279 | 0.2198 | The table displays the following information: ◦◦ R... |
| 4280 | 0.2197 | Move the selected snapshots to the Snapshots avail... |
| 4281 | 0.2197 | Move the selected snapshots to the Snapshots avail... |
| 4282 | 0.2197 | Move the selected snapshots to the Snapshots avail... |
| 4283 | 0.2196 | A wildcard (*) is supported. You can use * for cmd... |
| 4284 | 0.2195 | NetwrixAuditorPassword Current user credentials Un... |
| 4285 | 0.2195 | Step 3 – Assign the required permissions. Permissi... |
| 4286 | 0.2195 | A listener allows you to connect to a replica with... |
| 4287 | 0.2194 | User name / Password Provide user name and passwor... |
| 4288 | 0.2193 | Parameter or switch Default value Description By d... |
| 4289 | 0.2193 | Use other options (Computer name, IP address range... |
| 4290 | 0.2193 | Select this option if you want Auditor to connect ... |
| 4291 | 0.2191 | Table 1: For metric... Use Customize risk indicato... |
| 4292 | 0.2190 | You can set the After filter to this account's cur... |
| 4293 | 0.2190 | Step 5 – On the Destination Folder step, specify t... |
| 4294 | 0.2189 | In most cases the default values should be used. P... |
| 4295 | 0.2186 | Table 1: Add-on Port Protocol Source Target Purpos... |
| 4296 | 0.2186 | URL & Login The Access Reviews Console can be acce... |
| 4297 | 0.2186 | Step 2 – Type a path to the add-on. Or simply drag... |
| 4298 | 0.2185 | Select this option to receive reports attached to ... |
| 4299 | 0.2185 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 4300 | 0.2184 | You can also configure and receive alerts on the e... |
| 4301 | 0.2184 | Request Error details returned 400 Bad Request Inv... |
| 4302 | 0.2183 | resource_path — path as shown in the "What" column... |
| 4303 | 0.2183 | Netwrix encrypts data with a self-signed automatic... |
| 4304 | 0.2183 | If an alerts is triggered a fter the UpdateInterva... |
| 4305 | 0.2183 | See Edit Notes the Edit Notes Window topic for a d... |
| 4306 | 0.2183 | If an alerts is triggered a fter the UpdateInterva... |
| 4307 | 0.2182 | These guidelines are based on security best practi... |
| 4308 | 0.2181 | For that, you need to set the Network Security: Re... |
| 4309 | 0.2181 | cmdlet.attrname For example: Set-User Set-ContactS... |
| 4310 | 0.2180 | Use semicolon to separate several addresses. Step ... |
| 4311 | 0.2180 | The Action filt er in the Advanced mode contains a... |
| 4312 | 0.2178 | Possible values are: Multi_user (for Multiple), Re... |
| 4313 | 0.2177 | The My Reviews interface provides owners with acce... |
| 4314 | 0.2176 | RacNumber=16&Arg1= • Remove / Removed (Failed atte... |
| 4315 | 0.2175 | Step 4 – Review imported Activity Records. Azure F... |
| 4316 | 0.2173 | Specify custom connection parameters Make sure to ... |
| 4317 | 0.2173 | See the Monitoring Planstopic for additional infor... |
| 4318 | 0.2172 | omitstorelist_ecr.txt Contains a list of classes a... |
| 4319 | 0.2170 | Access is denied.” error. member of the local Admi... |
| 4320 | 0.2169 | v10.7 Once the anomaly is reviewed, it disappears ... |
| 4321 | 0.2168 | With Behavior Anomalies, you can step beyond indiv... |
| 4322 | 0.2167 | • ≤25% — Low • (25% - 50%) — Medium • ≥50% — High ... |
| 4323 | 0.2167 | Monitoring plan Select to display events from one ... |
| 4324 | 0.2166 | Due to limited database size, Express Edition (wit... |
| 4325 | 0.2165 | • Database — specify target database • Schema — sp... |
| 4326 | 0.2165 | Step 2 – Navigate to Start > Run and type "cmd". S... |
| 4327 | 0.2165 | Step 2 – In the Help Protect your computer with Wi... |
| 4328 | 0.2165 | v10.7 Step 7 – When done, click Finish. Define Par... |
| 4329 | 0.2161 | • Contains subscription generation details (interv... |
| 4330 | 0.2160 | See the Subscriptions topic for additional informa... |
| 4331 | 0.2158 | Example: "US" or "UK". Maximum length 128. Creatio... |
| 4332 | 0.2157 | Step 2 – Unzip the Add-On to a desired folder. Ste... |
| 4333 | 0.2154 | v10.7 Try to review user tasks—you may find out th... |
| 4334 | 0.2152 | Depending on the selected virtual appliance config... |
| 4335 | 0.2151 | Any other account will be considered a risk factor... |
| 4336 | 0.2150 | For that, you will need an executable file stored ... |
| 4337 | 0.2150 | v10.7 Assign Permission Via the Registry Editor Sn... |
| 4338 | 0.2149 | Department — provide the name of the department if... |
| 4339 | 0.2147 | For example, you can run the add-on on the compute... |
| 4340 | 0.2146 | v10.7 on... Ensure that... The UDP Receiver is ena... |
| 4341 | 0.2145 | CAUTION: This field should never be empty. Checkpo... |
| 4342 | 0.2144 | v10.7 ◦ Enumerate permissions Also, state-in-time ... |
| 4343 | 0.2144 | Resources — Select resources to be included in the... |
| 4344 | 0.2144 | Account type —possible values: ◦ Windows Account ◦... |
| 4345 | 0.2143 | Make sure you have at least one monitored item in ... |
| 4346 | 0.2143 | v10.7 If you are using Netwrix Auditor for Network... |
| 4347 | 0.2142 | To disable filtering for these fields, specify an ... |
| 4348 | 0.2141 | Qumulo Complete the following fields: Table 1: Opt... |
| 4349 | 0.2140 | Computer Specify a computer. You will only be aler... |
| 4350 | 0.2140 | To import Active Directory data from the removed m... |
| 4351 | 0.2140 | Table 1: Option Description Slide the switch under... |
| 4352 | 0.2140 | Select Monitor userdefined hidden shares if necess... |
| 4353 | 0.2139 | A user's last logon time is updated only once ever... |
| 4354 | 0.2136 | Select Monitor userdefined hidden shares if necess... |
| 4355 | 0.2135 | CAUTION: UPD 514 port can only be used by one serv... |
| 4356 | 0.2134 | You are investigating suspicious user activity. A ... |
| 4357 | 0.2134 | • Windows Server (with enabled network tra ffic co... |
| 4358 | 0.2134 | It is recommended to adjust this setting carefully... |
| 4359 | 0.2131 | File permissions define who has access to local fi... |
| 4360 | 0.2130 | Step 2 – Type a path to the add-on. Or simply drag... |
| 4361 | 0.2129 | Lines that start with the # sign are treated as co... |
| 4362 | 0.2128 | For example: v10.7 ◦◦ If you want to periodically ... |
| 4363 | 0.2128 | For example: v10.7 ◦◦ If you want to periodically ... |
| 4364 | 0.2128 | Step 2 – Run data collection. Step 3 – Consider th... |
| 4365 | 0.2127 | Send a POST request containing this Continuation m... |
| 4366 | 0.2127 | You are investigating suspicious user activity. A ... |
| 4367 | 0.2126 | Several examples are provided below. v10.7 In the ... |
| 4368 | 0.2126 | Action Select an action type from the list (Added,... |
| 4369 | 0.2126 | v10.7 Click Proceed and complete the following fie... |
| 4370 | 0.2126 | A resource description can be supplied by either t... |
| 4371 | 0.2125 | It is recommended to assign the API Member Connect... |
| 4372 | 0.2125 | Monitor hidden shares Even when this option is sel... |
| 4373 | 0.2125 | Monitor hidden shares Even when this option is sel... |
| 4374 | 0.2124 | Lines that start with the # sign are treated as co... |
| 4375 | 0.2123 | See the Selected Resources Window topic for additi... |
| 4376 | 0.2122 | Make sure to copy and save the API key in a secure... |
| 4377 | 0.2122 | For example: ◦◦ If you want to periodically receiv... |
| 4378 | 0.2122 | Enabling TLS 1.2 Usage The add-on supports Transpo... |
| 4379 | 0.2118 | Step 8 – Review sample tnsnames.ora file where myO... |
| 4380 | 0.2118 | Follow the steps to exclude data from Exchange Onl... |
| 4381 | 0.2117 | Table 1: Option Name Description Go to Original Ex... |
| 4382 | 0.2116 | This does require the Access Reviews application t... |
| 4383 | 0.2116 | Older activity record requests are cleared. Activi... |
| 4384 | 0.2115 | <Who>Administrator</Who><DataSource>S harePoint</D... |
| 4385 | 0.2115 | See the Search Parameters topic for more informati... |
| 4386 | 0.2115 | If you want to use a specific account (other than ... |
| 4387 | 0.2114 | Any other antivirus will be considered a risk fact... |
| 4388 | 0.2113 | However, you can adjust them manually, using the i... |
| 4389 | 0.2112 | In the dialog appears, select Create new address o... |
| 4390 | 0.2110 | Rotating certificate s in the Entra ID application... |
| 4391 | 0.2110 | This topic includes the following subtopics: Getti... |
| 4392 | 0.2109 | Object type Actions Event ID LOGIN_INFORMATION Acc... |
| 4393 | 0.2109 | Follow the steps to manage recommendations: Step 1... |
| 4394 | 0.2108 | To import Active Directory data from the removed m... |
| 4395 | 0.2106 | Make sure that your carrier supports sms to email ... |
| 4396 | 0.2106 | This page is opened by selecting a review on the M... |
| 4397 | 0.2106 | Example: "Business The user's job title. Max Title... |
| 4398 | 0.2105 | See the Settings for Data Collection topic for mor... |
| 4399 | 0.2104 | You are investigating an incident and want to know... |
| 4400 | 0.2104 | ◦ The user that is going to run the Core Service i... |
| 4401 | 0.2103 | Review the following for additional information: R... |
| 4402 | 0.2102 | A backslash (\) must be put in front of (*), (? ),... |
| 4403 | 0.2101 | If you configured a dedicated monitoring plan, mak... |
| 4404 | 0.2100 | You can set this filter as equal to and specify th... |
| 4405 | 0.2099 | Entitlement Reviews tab Administrator role Securit... |
| 4406 | 0.2098 | SetDataSourceAsEventSource False Defines whether t... |
| 4407 | 0.2096 | omitexchangeserverlist.txt Specify the Microsoft E... |
| 4408 | 0.2095 | These permissions are equivalent to the default pe... |
| 4409 | 0.2093 | For this report to function properly, you must ena... |
| 4410 | 0.2092 | Number of sensitive documents accessible by Everyo... |
| 4411 | 0.2091 | NOTE: If you are going to configure monitoring rul... |
| 4412 | 0.2091 | You can click Browse to select a computer from the... |
| 4413 | 0.2089 | You can use IP address, DataCollectionServer (empt... |
| 4414 | 0.2088 | Overexposed Sensitive Data Objects For each user a... |
| 4415 | 0.2087 | Helps identify who accessed important files beside... |
| 4416 | 0.2086 | Step 2 – Double-click SQL Server monitoring plan. ... |
| 4417 | 0.2085 | Allows specifying report delivery schedule (daily,... |
| 4418 | 0.2085 | Step 2 – Type a path to the add-on. Or simply drag... |
| 4419 | 0.2082 | JSON-formatted Continuation mark includes the fi e... |
| 4420 | 0.2082 | The most commonly used fi lters are described in U... |
| 4421 | 0.2081 | For security reasons, it is recommended to configu... |
| 4422 | 0.2080 | Task Category {DataSource ID} -OR1 Depending on Se... |
| 4423 | 0.2080 | Specify Active Directory domain For example, "comp... |
| 4424 | 0.2079 | user@tenant.com exomiteventuserlist.txt Contains a... |
| 4425 | 0.2074 | Monitor hidden shares Even when this option is sel... |
| 4426 | 0.2073 | ◦◦ eDiscovery or eDiscovery (Premium) in the compl... |
| 4427 | 0.2073 | Maximum length 128. The created date of the Creati... |
| 4428 | 0.2072 | RECOMMENDED: click Send Test Email. The system wil... |
| 4429 | 0.2072 | This configuration procedure involves creation of ... |
| 4430 | 0.2070 | The spaces are trimmed. If they are required, use ... |
| 4431 | 0.2069 | DataCollectionUserName (empty) Specify user accoun... |
| 4432 | 0.2067 | Add-on Internal Parameters Internal parameters lis... |
| 4433 | 0.2067 | Step 8 – In the <Share_Name> Properties dialog, se... |
| 4434 | 0.2066 | Program/script Input "Powershell.exe". Add a path ... |
| 4435 | 0.2066 | These templates are designed to make the message v... |
| 4436 | 0.2066 | Runs the reports in the Favorites folder to displa... |
| 4437 | 0.2066 | See the Settings for Data Collection topic for mor... |
| 4438 | 0.2065 | Step 3 – Right-click the Security node and select ... |
| 4439 | 0.2064 | 55.. Go to Certificates (Local Computer) > Persona... |
| 4440 | 0.2063 | Review the following for additional information: O... |
| 4441 | 0.2060 | See the Enable Console Users topic for additional ... |
| 4442 | 0.2057 | Each Activity Record contains the user account, ac... |
| 4443 | 0.2057 | While a standalone a ction is not suspicious, mult... |
| 4444 | 0.2056 | Starts with This operator shows all entries that s... |
| 4445 | 0.2055 | format=json No Add this parameter to retrieve data... |
| 4446 | 0.2054 | For outbound rules, create or enable predefined Wi... |
| 4447 | 0.2053 | a file share that contains a public User Activity ... |
| 4448 | 0.2053 | a file share that contains a public User Activity ... |
| 4449 | 0.2052 | Step 2 – In the left pane, navigate to HKEY_LOCAL_... |
| 4450 | 0.2051 | Wildcards are supported. For example, type %corp\a... |
| 4451 | 0.2051 | Behavior Anomalies Assessment Tips and Tricks This... |
| 4452 | 0.2051 | See the Specified time interval (in Working (logon... |
| 4453 | 0.2050 | Then click Next to continue. Step 4 – On the Summa... |
| 4454 | 0.2049 | The mailbox is accessed by an account impersonatin... |
| 4455 | 0.2046 | lsnrctl stop listener_name To find your listener n... |
| 4456 | 0.2046 | Maximum length is 64 characters. Is licensed – – –... |
| 4457 | 0.2045 | v10.7 Step 6 – On the Summary page, review the set... |
| 4458 | 0.2045 | Adds the full alert text to Work notes, including ... |
| 4459 | 0.2045 | Template Name Message Type Description Reminds own... |
| 4460 | 0.2044 | Source Specify this parameter if you want to save ... |
| 4461 | 0.2043 | Message No string Object-specific details about th... |
| 4462 | 0.2043 | IncludeDataSourceToMakeEventId True Defines whethe... |
| 4463 | 0.2039 | These group Managed Service Accounts should meet t... |
| 4464 | 0.2038 | User name Table 1: Option Description • Password S... |
| 4465 | 0.2038 | You can use IP address, FQDN or NETBIOS name. For ... |
| 4466 | 0.2038 | Localos users. For these users, the product collec... |
| 4467 | 0.2038 | + delegated See the corresponding No Microsoft art... |
| 4468 | 0.2037 | User (domain\account) – select a specific user to ... |
| 4469 | 0.2035 | We welcome any feedback and ideas you might have. ... |
| 4470 | 0.2032 | For example, a new alert is triggered —the service... |
| 4471 | 0.2031 | Delete task Yes Message with subject <...> was mov... |
| 4472 | 0.2030 | Open the File Server REST API Explorer client usin... |
| 4473 | 0.2028 | See Filters for more information. Select as many A... |
| 4474 | 0.2027 | The Entitlement Reviews tab opens the Entitlement ... |
| 4475 | 0.2026 | Equals NotEqualTo Table 1: Filter Description Supp... |
| 4476 | 0.2026 | A custom account must be granted the same permissi... |
| 4477 | 0.2023 | To read more about activity records, see the Refer... |
| 4478 | 0.2022 | You can use * for cmdlets and their parameters. Li... |
| 4479 | 0.2021 | The workaround is to force data collection right a... |
| 4480 | 0.2021 | SetDataSourceAsEventCategory True Defines whether ... |
| 4481 | 0.2021 | SetDataSourceAsEventCategory True Defines whether ... |
| 4482 | 0.2021 | v10.7 In the Insertion Strings tab: Option Descrip... |
| 4483 | 0.2020 | Examples: http://siteCollection1:3333/ https://sit... |
| 4484 | 0.2020 | To collect activity data only, the privileged role... |
| 4485 | 0.2019 | Task Category {DataSource ID} -OR1 Depending on Se... |
| 4486 | 0.2019 | Updates to this partition are replicated only to d... |
| 4487 | 0.2019 | You can also review the <TicketParameterRefs> sect... |
| 4488 | 0.2018 | Specify email address to be included in the list a... |
| 4489 | 0.2018 | It can be opened for one or multiple resources. It... |
| 4490 | 0.2018 | Step 4 – Click Add and enter the name of the user ... |
| 4491 | 0.2018 | This window displays all recommended changes, note... |
| 4492 | 0.2018 | For example: cluster1::> system services web show ... |
| 4493 | 0.2017 | The maximum number of activity record requests v10... |
| 4494 | 0.2017 | Select this checkbox if the implicit SSL mode is u... |
| 4495 | 0.2017 | Filters You can narrow your reporting scope using ... |
| 4496 | 0.2016 | 55.. Run the following command to update group pol... |
| 4497 | 0.2015 | v10.7 Track... Steps... Set-Mailbox -Identity {0} ... |
| 4498 | 0.2013 | Name and Location Select a name for the new virtua... |
| 4499 | 0.2012 | Step 2 – Run the install.cmd file. The file deploy... |
| 4500 | 0.2012 | Use this report to reveal the number of sensitive ... |
| 4501 | 0.2011 | The default value is 3600 seconds, i.e., 1 hour. S... |
| 4502 | 0.2010 | See the Run the Add-On with PowerShell topic for a... |
| 4503 | 0.2010 | Enter the account's password in both the Password ... |
| 4504 | 0.2010 | SQL Server database information: Server Name – Hos... |
| 4505 | 0.2009 | Notify users about activity monitoring You can ena... |
| 4506 | 0.2008 | Message No string Message is included in output Ac... |
| 4507 | 0.2007 | Possible parameter values: • True — generate a num... |
| 4508 | 0.2006 | Updates to this partition are replicated only to d... |
| 4509 | 0.2002 | Time zone — is set automatically. Snapshot date —s... |
| 4510 | 0.2001 | Installation on the domain controller is not suppo... |
| 4511 | 0.1999 | Defines whether the DataSource field of Activity R... |
| 4512 | 0.1999 | Defines whether the DataSource field of Activity R... |
| 4513 | 0.1998 | So, in the example above, the program will track a... |
| 4514 | 0.1997 | Only alerts grouped by the Who parameter can be in... |
| 4515 | 0.1997 | If you want to run the addon on another machine, p... |
| 4516 | 0.1995 | Example: John + Last name Shows the last name. Exa... |
| 4517 | 0.1995 | Check the Notes for the resource to view this info... |
| 4518 | 0.1995 | The workaround is to force data collection right a... |
| 4519 | 0.1994 | Description – Description or explanation of the re... |
| 4520 | 0.1994 | What Shows the path to the modified AD object. v10... |
| 4521 | 0.1994 | Support for modern authentication will allow you t... |
| 4522 | 0.1991 | Table 1: To... Follow the steps... Find an alert U... |
| 4523 | 0.1991 | See the Remove Changes Window topic for a dditiona... |
| 4524 | 0.1989 | You can install the product to a virtual machine o... |
| 4525 | 0.1988 | v10.7 2. Click View button in the right pane. To l... |
| 4526 | 0.1987 | It allows users to securely access databases witho... |
| 4527 | 0.1986 | Even when this option is selected, the product wil... |
| 4528 | 0.1984 | This account requires at least Read permission for... |
| 4529 | 0.1984 | Ownership Confirmation Request Email The Ownership... |
| 4530 | 0.1982 | Sensitive documents accessible by Everyone Number ... |
| 4531 | 0.1982 | Resource Ownership Configuration Ownership of reso... |
| 4532 | 0.1982 | Step 2 – Edit the following parameters of the cust... |
| 4533 | 0.1982 | The service can store the ticket requests not olde... |
| 4534 | 0.1981 | Account type —possible values: Windows Account, Lo... |
| 4535 | 0.1981 | NOTE: This does require the Notification settings ... |
| 4536 | 0.1980 | Farm account Farm account is a service account use... |
| 4537 | 0.1979 | See the Data Collecting Account topic for a dditio... |
| 4538 | 0.1979 | See the Data Collecting Account topic for a dditio... |
| 4539 | 0.1979 | See the Data Collecting Account topic for a dditio... |
| 4540 | 0.1978 | • 0 — Low • [1 – 2] — Medium • > 2 — High Disabled... |
| 4541 | 0.1978 | Reported Attributes The following account attribut... |
| 4542 | 0.1976 | Last name surname Example: "Smith" The user's surn... |
| 4543 | 0.1975 | Select Type — Reviews are limited to one type. Sel... |
| 4544 | 0.1972 | Below is a table of the Substitution Tokens, the v... |
| 4545 | 0.1972 | If the trustee is a group, click the hyperlink to ... |
| 4546 | 0.1972 | Shows the before and after values of the modified ... |
| 4547 | 0.1971 | See the corresponding Micr osoft article for more ... |
| 4548 | 0.1969 | See the Notification to Owners topic for additiona... |
| 4549 | 0.1969 | See the View Responses Window topic for a dditiona... |
| 4550 | 0.1967 | Table 1: Name Value Description assignment_ group ... |
| 4551 | 0.1967 | v10.7 Selected Resources Window The Selected Resou... |
| 4552 | 0.1966 | Scheduled tasks—Enables auditing of enabled / disa... |
| 4553 | 0.1965 | RequestLimitInterval 604800 Internal parameter. Th... |
| 4554 | 0.1962 | To find out a field name in ServiceNow, switch to ... |
| 4555 | 0.1961 | attribute_name—Can be found in the Details column ... |
| 4556 | 0.1960 | Step 1 – On your target server, open Registry Edit... |
| 4557 | 0.1960 | Locate the POST request for partner_servers endpoi... |
| 4558 | 0.1958 | The maximum number of ticket requests the service ... |
| 4559 | 0.1957 | For example, you can run the add-on on the compute... |
| 4560 | 0.1957 | The user must have sufficient v10.7 Step 2 – Defin... |
| 4561 | 0.1957 | ArcSight trademarks and registered trademarks are ... |
| 4562 | 0.1956 | While a single action is safe, multiple occurrence... |
| 4563 | 0.1956 | For example: auth.*;authpriv. * @172.28.18.25:514;... |
| 4564 | 0.1955 | The review for this resource is now complete. You ... |
| 4565 | 0.1955 | See the Create Alertstopic for additional informat... |
| 4566 | 0.1954 | Even when this option is selected, the product wil... |
| 4567 | 0.1954 | 5% of 10 GB limit remaining). v10.7 These properti... |
| 4568 | 0.1951 | Step 12 – Type repadmin/syncall command and press ... |
| 4569 | 0.1949 | After running the script, the RADIUS server logons... |
| 4570 | 0.1948 | A featured set of the Privileged Access Security t... |
| 4571 | 0.1948 | Table 1: Option Value Add arguments (optional) Add... |
| 4572 | 0.1948 | v10.7 Review the following for additional informat... |
| 4573 | 0.1947 | These filters will be applied using AND logic. Wil... |
| 4574 | 0.1946 | Indicates the assigned owner confirmed ownership o... |
| 4575 | 0.1946 | Step 4 – Right-click the newly created GPO and sel... |
| 4576 | 0.1946 | To find out what is included in the alert details,... |
| 4577 | 0.1946 | Operator Description Example If you set the Who fi... |
| 4578 | 0.1945 | Make sure this account has Log on as batch job pri... |
| 4579 | 0.1942 | Message with subject <...> was moved from folder D... |
| 4580 | 0.1936 | Use the omitreadaccess.txt to exclude SELECT state... |
| 4581 | 0.1935 | The modifications to the HTML email templates are ... |
| 4582 | 0.1935 | Provide this account in the monitoring plan wizard... |
| 4583 | 0.1935 | */ foldername will exclude the specified folder wh... |
| 4584 | 0.1932 | Table 1: Object Action Property Virtual Machine1 C... |
| 4585 | 0.1932 | In the main window, supply the name of the account... |
| 4586 | 0.1932 | The Filters section helps you show or hide anomali... |
| 4587 | 0.1929 | Use this report to plan and control data protectio... |
| 4588 | 0.1925 | Perform a Membership Review A Membership review is... |
| 4589 | 0.1924 | Format Example XML <Who>Admin</Who><Who>Analyst</W... |
| 4590 | 0.1924 | You can set the Before filter to the previous name... |
| 4591 | 0.1924 | The add-on will only collect and process events yo... |
| 4592 | 0.1920 | For example: *.Role.DisplayName = MultiValued v10.... |
| 4593 | 0.1920 | Possible parameter values: • True — generate uniqu... |
| 4594 | 0.1919 | Step 3 – Navigate to the Monitored computers list ... |
| 4595 | 0.1918 | Yes No + Other Creation date Shows account cr eati... |
| 4596 | 0.1916 | Send a POST request containing Continuation mark t... |
| 4597 | 0.1914 | Resource Review Page The Begin Review button opens... |
| 4598 | 0.1914 | Example: mydomain\user1. You can provide the "Syst... |
| 4599 | 0.1913 | Navigate to Reports and generate a report. Apply r... |
| 4600 | 0.1910 | If you have alternate access mapping configured in... |
| 4601 | 0.1910 | Define Parameters The configuration wizard opens i... |
| 4602 | 0.1909 | ConsolidationInterval 900 Specify the time period,... |
| 4603 | 0.1909 | Table 1: Error in PowerShell Resolution Select the... |
| 4604 | 0.1901 | Step 2 – Select Microsoft Entra ID on the left. St... |
| 4605 | 0.1901 | Step 2 – Select Microsoft Entra ID on the left. St... |
| 4606 | 0.1901 | v10.7 Step 5 – On the Select a creation type step,... |
| 4607 | 0.1900 | In this case, this user will have the most extende... |
| 4608 | 0.1898 | v10.7 Attribute (display Microsoft Entra ID Possib... |
| 4609 | 0.1897 | Table 2: Option Description Filter by account name... |
| 4610 | 0.1897 | Step 1 – Navigate to the target file share, right-... |
| 4611 | 0.1897 | See the following Microsoft article for more infor... |
| 4612 | 0.1896 | Step 3 – On the Select Rollback Source step, speci... |
| 4613 | 0.1894 | The alert keeps firing 20 times more within 10 min... |
| 4614 | 0.1891 | Assigned owners do not require a console user role... |
| 4615 | 0.1891 | Number of days Shows password age for the account ... |
| 4616 | 0.1888 | For example: <a n="Names"> Allows specifying a use... |
| 4617 | 0.1887 | Supported size: 21x21px (WxH). FooterImageFullPath... |
| 4618 | 0.1887 | Add-on installation server, i.e. the machine where... |
| 4619 | 0.1886 | Remove subscriptions Click icon next to the select... |
| 4620 | 0.1886 | (empty) For localhost, leave this parameter empty.... |
| 4621 | 0.1883 | fs_read_data Read operation was performed. fs_writ... |
| 4622 | 0.1883 | Console Users with Administrator role ◦◦ Can compl... |
| 4623 | 0.1881 | The Active Directory service account password has ... |
| 4624 | 0.1881 | The ID property is optional and is assigned automa... |
| 4625 | 0.1880 | See the Data Grid Features topic for additional in... |
| 4626 | 0.1876 | The Review Details page opens. v10.7 Step 2 – Sele... |
| 4627 | 0.1875 | The review for this resource is now complete. You ... |
| 4628 | 0.1872 | As an example, refer to the following Oracle help ... |
| 4629 | 0.1872 | Hover over the icon to view the date timestamp of ... |
| 4630 | 0.1870 | Table 1: Operator Description Example Not equal to... |
| 4631 | 0.1860 | The me 2:13:00 PM Timestamp type represents date a... |
| 4632 | 0.1858 | Parameter Default value Description EventID genera... |
| 4633 | 0.1858 | sysadmin. Type— the security principal type, e.g. ... |
| 4634 | 0.1858 | StartsWith Max length: 255. EndsWith Contains (def... |
| 4635 | 0.1857 | ◦◦ If you plan to process the Active Directory Del... |
| 4636 | 0.1857 | ≥60% — High Table 1: Risk Assessment formula Defau... |
| 4637 | 0.1857 | If false, all activity records will be displayed i... |
| 4638 | 0.1856 | New sensitive data-related risks for SharePoint On... |
| 4639 | 0.1853 | See the corresponding Micro soft article for more ... |
| 4640 | 0.1853 | CyperArk PAS Version 10.10. Accounts and Rights By... |
| 4641 | 0.1851 | RequestLimitInterval 604800 Internal parameter. Th... |
| 4642 | 0.1848 | When planning for hardware resources, consider tha... |
| 4643 | 0.1846 | ◦◦ Using Description can help to filter out severa... |
| 4644 | 0.1844 | If you want to use custom management interface for... |
| 4645 | 0.1842 | Clicking the Defined in link opens the object perm... |
| 4646 | 0.1839 | Contains a list of AD paths to be omitsnapshotpath... |
| 4647 | 0.1839 | ), (,), and (\) if they are a part of an entry val... |
| 4648 | 0.1837 | Review Type – Type of review Resource Name – The i... |
| 4649 | 0.1837 | Step 4 – In the Advanced Security Settings for SOF... |
| 4650 | 0.1837 | Description Network Protocol** Status Configuratio... |
| 4651 | 0.1837 | The Active Directory service account is configured... |
| 4652 | 0.1833 | If disabled, only user session events will be coll... |
| 4653 | 0.1832 | In this case, this user will have the most extende... |
| 4654 | 0.1831 | You can select to collect event data from the same... |
| 4655 | 0.1830 | Click Add to add a new monitoring plan. Step 3 – C... |
| 4656 | 0.1830 | Default retention period is 180 days. v10.7 Option... |
| 4657 | 0.1829 | Refresh Runs the reports in the Favorites folder t... |
| 4658 | 0.1828 | Ownership Confirmation The reason for assigning ow... |
| 4659 | 0.1827 | The Search parameters fi le includes one or more f... |
| 4660 | 0.1823 | Specify the time period, in seconds. During this t... |
| 4661 | 0.1823 | You can set the Item filter to this domain name to... |
| 4662 | 0.1822 | To check receiver settings or add a new receiver, ... |
| 4663 | 0.1821 | Configuration parameters to specify in settings.xm... |
| 4664 | 0.1821 | Provide the name and password of the service accou... |
| 4665 | 0.1820 | Table 1: Name Description IgnoreUploadAttachmentEr... |
| 4666 | 0.1820 | Ensure that... auth.*;authpriv. * @172.28.18.25:51... |
| 4667 | 0.1820 | Ensure that... auth.*;authpriv. * @172.28.18.25:51... |
| 4668 | 0.1818 | Procedure for Nutanix Command-Line Interface Alter... |
| 4669 | 0.1817 | e.g., Who not for the Who filter. If you set the W... |
| 4670 | 0.1816 | Opens the Send Reminders window, which indicates a... |
| 4671 | 0.1816 | Limits your search results to entries You are inve... |
| 4672 | 0.1813 | Step 3 – Double-click the Log on as a service poli... |
| 4673 | 0.1811 | When the Review Administrator creates a new review... |
| 4674 | 0.1811 | Use this operator if you want to get precise resul... |
| 4675 | 0.1810 | Troubleshoot Issues Error in PowerShell Resolution... |
| 4676 | 0.1809 | Follow the steps to perform distributed deployment... |
| 4677 | 0.1808 | Step 4 – Review your search results. Step 5 – Navi... |
| 4678 | 0.1808 | See the Filters topic for more information. Select... |
| 4679 | 0.1805 | Table 1: Location Prerequisites ConnectWise Manage... |
| 4680 | 0.1803 | City city Example: "London" The city where a user ... |
| 4681 | 0.1802 | Table 1: Button Description Export CSV Exports the... |
| 4682 | 0.1802 | You do not have sufficient permissions to review i... |
| 4683 | 0.1802 | If you set the Who filter to starts with Domain1\J... |
| 4684 | 0.1801 | Group Membership Window When a group trustee appea... |
| 4685 | 0.1799 | ActivityRecordRequestsRetention RequestLimit 5000 ... |
| 4686 | 0.1796 | See the Settings for Data Collection topic for add... |
| 4687 | 0.1796 | Parameter Default value Description EventID genera... |
| 4688 | 0.1795 | Owners with a console user role access the pending... |
| 4689 | 0.1794 | You can use a wildcard (*) only if you need to exc... |
| 4690 | 0.1792 | Owner performs a review. See the Pending Reviews t... |
| 4691 | 0.1792 | See the View Reports topic for additional informat... |
| 4692 | 0.1792 | collects stat-in-time data for this share. Follow ... |
| 4693 | 0.1792 | This may lead to your sensitive content being high... |
| 4694 | 0.1791 | Add arguments (optional) Add a path to the add-on ... |
| 4695 | 0.1790 | See the Data Collecting Account topic for a dditio... |
| 4696 | 0.1790 | See the Data Collecting Account topic for a dditio... |
| 4697 | 0.1790 | See the Data Collecting Account topic for a dditio... |
| 4698 | 0.1790 | See the Data Collecting Account topic for a dditio... |
| 4699 | 0.1790 | This list omits changes made by users through Exch... |
| 4700 | 0.1789 | Use the path format as it appears in the "What" co... |
| 4701 | 0.1789 | • Contains (default) • DoesNotContain • Equals • N... |
| 4702 | 0.1787 | Click Exclude to specify AD domains, OUs, and cont... |
| 4703 | 0.1787 | Use the path format as it appears in the "What" co... |
| 4704 | 0.1786 | In this case, this user will have the most extende... |
| 4705 | 0.1784 | To collect activity data without logons, the privi... |
| 4706 | 0.1783 | To import snapshots, you must be assigned the Glob... |
| 4707 | 0.1783 | In large environments, it is required to wait 10 h... |
| 4708 | 0.1782 | Use the path format as it appears in the "What" co... |
| 4709 | 0.1780 | Select the necessary actions (successful or failed... |
| 4710 | 0.1778 | Table 1: Option Description Click Exclude to speci... |
| 4711 | 0.1777 | System requirements for SQL Server are listed in t... |
| 4712 | 0.1775 | Data source Specify a data source from the Since y... |
| 4713 | 0.1775 | Use the path format as it appears in the "What" co... |
| 4714 | 0.1771 | Table 1: Requirement Comment Microsoft Entra ID ap... |
| 4715 | 0.1770 | See the Activity Records topic for additional info... |
| 4716 | 0.1770 | See the Activity Records topic for additional info... |
| 4717 | 0.1770 | See the Activity Records topic for additional info... |
| 4718 | 0.1769 | 22.. On the Add Subscription page, complete the fo... |
| 4719 | 0.1768 | https://URL Contains the SharePoint Online For exa... |
| 4720 | 0.1768 | Shows whether the account has the "Password not re... |
| 4721 | 0.1767 | Example: winsrv2016-01.mydomain.local. • Setting c... |
| 4722 | 0.1767 | See the Example: corresponding Micro soft Logon sc... |
| 4723 | 0.1766 | Table 1: Event Description replication_delete_sour... |
| 4724 | 0.1766 | This property is required when a user is created a... |
| 4725 | 0.1766 | This account should be able to create a dedicated ... |
| 4726 | 0.1764 | See the Delete Review Window topic for additional ... |
| 4727 | 0.1764 | The following risk levels are used: Table 1: Risk ... |
| 4728 | 0.1760 | Slide the Table 1: Option Description switch to tu... |
| 4729 | 0.1759 | Customize Home Screen Starting with version 10, yo... |
| 4730 | 0.1758 | In the Specific local ports field specify the port... |
| 4731 | 0.1757 | You can select Directly, Inherited, or both (defau... |
| 4732 | 0.1757 | Execute the following command... To create audit p... |
| 4733 | 0.1757 | See Edit Notes the Edit Notes Window topic for a d... |
| 4734 | 0.1754 | Remember, only resources with an assigned owner wi... |
| 4735 | 0.1753 | See Email address the corresponding Email address ... |
| 4736 | 0.1752 | If you want to use a specific account (other than ... |
| 4737 | 0.1751 | Users Specify users to track their activity Select... |
| 4738 | 0.1749 | Follow the steps to assign the role you need: Step... |
| 4739 | 0.1748 | When desired, the Review Administrator runs anothe... |
| 4740 | 0.1748 | A custom account must be granted the same permissi... |
| 4741 | 0.1745 | Step 4 – Run the shell script by executing the fol... |
| 4742 | 0.1742 | The requested endpoint does not exist (e.g., / net... |
| 4743 | 0.1742 | By default, it is delivered once a day, at 3 Speci... |
| 4744 | 0.1739 | This account should be able to create a dedicated ... |
| 4745 | 0.1739 | Activity Specify restriction filters to narrow you... |
| 4746 | 0.1737 | For report subscription—You cannot edit report nam... |
| 4747 | 0.1735 | Defines the co nnection timeout. TicketRequestsRet... |
| 4748 | 0.1733 | Table 2: Option Description Specify SQL Server ins... |
| 4749 | 0.1733 | All filters are applied using AND logic. v10.7 Opt... |
| 4750 | 0.1732 | Download the latest add-on version in the Add-on S... |
| 4751 | 0.1732 | Download the latest add-on version in the Add-on S... |
| 4752 | 0.1732 | Download the latest add-on version in the Add-on S... |
| 4753 | 0.1732 | - Last modified Equals the When-Changed attribute.... |
| 4754 | 0.1732 | In this case, this user will have the most extende... |
| 4755 | 0.1731 | If you have alternate access mapping configured in... |
| 4756 | 0.1730 | Table 1: Option Description User has been idle for... |
| 4757 | 0.1728 | Format Example <Who Operator="Equals">Admin</Who><... |
| 4758 | 0.1727 | Step 1 – Sign in to Microsoft Entra ID portal usin... |
| 4759 | 0.1727 | If false, a corresponding error message will be di... |
| 4760 | 0.1727 | SetDataSourceAsEventSource False Defines whether t... |
| 4761 | 0.1725 | Windows Server which setting was changed: – provid... |
| 4762 | 0.1725 | Everyone in organization has a huge score Probably... |
| 4763 | 0.1723 | v10.7 Step 3 – On the Log On tab, select the This ... |
| 4764 | 0.1723 | The maximum number of ticket requests the service ... |
| 4765 | 0.1723 | Exports the selected review instance information t... |
| 4766 | 0.1722 | Added and Moved. v10.7 Step 3 – After configuring ... |
| 4767 | 0.1721 | The default values is 900 seconds, i.e., 15 minute... |
| 4768 | 0.1721 | v10.7 Option Description To specify what data chan... |
| 4769 | 0.1720 | See the Registry Keys topic for additional informa... |
| 4770 | 0.1720 | It is assumed that you have a good understanding o... |
| 4771 | 0.1717 | Limits your search to a unique key of the Activity... |
| 4772 | 0.1716 | Step 2 – On the Alert Properties step, specify the... |
| 4773 | 0.1715 | Please note that modern authentication must alread... |
| 4774 | 0.1715 | Department department Example: "Accounting and Fin... |
| 4775 | 0.1714 | Review the following Microsoft technical a rticle ... |
| 4776 | 0.1714 | In the right pane, click Configure, next to Advanc... |
| 4777 | 0.1713 | membership. Employee details Example: First name S... |
| 4778 | 0.1712 | The two may be s pecified together; for example: "... |
| 4779 | 0.1712 | Add a Data Source to an Existing Plan Follow the s... |
| 4780 | 0.1712 | server_instance:resource _path where: Contains a l... |
| 4781 | 0.1712 | When the owner confirmation notification has compl... |
| 4782 | 0.1710 | v10.7 Option Description Ensure that the requireme... |
| 4783 | 0.1709 | The city where a user is City city Example: "Londo... |
| 4784 | 0.1706 | Step 5 – In the Alert Properties wizard, specify t... |
| 4785 | 0.1706 | I.e., this option defi nes the maximum delay for p... |
| 4786 | 0.1704 | Review Instances After a review has been completed... |
| 4787 | 0.1702 | You can track Table 1: Filter Description Supporte... |
| 4788 | 0.1700 | v10.7 Operator Description Example show only data ... |
| 4789 | 0.1699 | This value is an enumeration with one possible val... |
| 4790 | 0.1697 | Otherwise some data may become unavailable for sea... |
| 4791 | 0.1697 | Qumulo Hybrid Cloud File Storage delivers real-tim... |
| 4792 | 0.1696 | Click Exclude to specify AD domains, OUs, and cont... |
| 4793 | 0.1696 | Click Exclude to specify AD domains, OUs, and cont... |
| 4794 | 0.1696 | Click Exclude to specify AD domains, OUs, and cont... |
| 4795 | 0.1696 | Click Add Rule and configure the following: Table ... |
| 4796 | 0.1695 | object_type.property_na me If there is no separato... |
| 4797 | 0.1694 | between an object type and a property, the Contain... |
| 4798 | 0.1694 | Ireland Security Table 1: Attribute Description Po... |
| 4799 | 0.1694 | By default, add-ons are configured to accept all c... |
| 4800 | 0.1693 | C:\Add-ons\Netwrix_Auditor_Addon_for_ Amazon_Web_S... |
| 4801 | 0.1692 | In Splunk expand the Settings drop-down menu and c... |
| 4802 | 0.1692 | Object type Actions Message ID 103047 103082 10308... |
| 4803 | 0.1691 | Follow the steps: Step 1 – Log on to any domain co... |
| 4804 | 0.1691 | Step 1 – Connect to your PaloAlto device: launch a... |
| 4805 | 0.1689 | You can use HTML tags when editing a template. Att... |
| 4806 | 0.1689 | Step 6 – In the Manage auditing and security log P... |
| 4807 | 0.1686 | See the Notifications topic for additional informa... |
| 4808 | 0.1683 | Reviewer Name — Primary owner assigned to the reso... |
| 4809 | 0.1683 | Do the same if you need to generate Activity Summa... |
| 4810 | 0.1679 | Subscription options - delivery by email or upload... |
| 4811 | 0.1678 | Data categories Limits your search results to entr... |
| 4812 | 0.1678 | Table 1: Operator Description Example Contains Thi... |
| 4813 | 0.1678 | Obtain the Tenant Name Follow the steps to obtain ... |
| 4814 | 0.1678 | Step 4 – On the General tab, click Configure next ... |
| 4815 | 0.1676 | Step 4 – Click Add and enter the name of the user ... |
| 4816 | 0.1675 | Table 1: CorrelationTicketFormat Description Previ... |
| 4817 | 0.1675 | Enter list or list item URI (Unique resource ident... |
| 4818 | 0.1675 | Then you will need to download that new version. T... |
| 4819 | 0.1675 | See the Add Owner Window topic for additional info... |
| 4820 | 0.1675 | v10.7 CAUTION: This will delete all historical dat... |
| 4821 | 0.1675 | Step 4 – Review the <TicketParameters> section. Th... |
| 4822 | 0.1674 | v10.7 Option Description Specify one or several us... |
| 4823 | 0.1672 | Step 4 – Receive the next response. On success, th... |
| 4824 | 0.1672 | Connect to your SonicWall device. Launch an Intern... |
| 4825 | 0.1671 | Wrong HTTP request was sent (any request was sent ... |
| 4826 | 0.1669 | Use... To... Save as report Save your search resul... |
| 4827 | 0.1665 | The credentials are case sensitive. A custom accou... |
| 4828 | 0.1665 | You can select Directly, Inherited, or both (defau... |
| 4829 | 0.1664 | Program/script Input "Powershell.exe". Add a path ... |
| 4830 | 0.1663 | Specify the switch during the addon execution if y... |
| 4831 | 0.1663 | Click Add to create an alert for non-owner mailbox... |
| 4832 | 0.1661 | Allow access to the following servers — When enabl... |
| 4833 | 0.1656 | ActivityRecordWebRequests RequestLimit 200 Interna... |
| 4834 | 0.1656 | SetDataSourceAsEventCategory True Defines whether ... |
| 4835 | 0.1656 | These individuals would have been asked to suggest... |
| 4836 | 0.1655 | If it is not, double-click the service. In the Rem... |
| 4837 | 0.1653 | Step 2 – On the main page, you will be prompted to... |
| 4838 | 0.1653 | You can Specify a host or network resource select ... |
| 4839 | 0.1650 | See the Requirements topic for additional informat... |
| 4840 | 0.1649 | Step 4 – Click Add and enter the name of the user ... |
| 4841 | 0.1649 | netwrix_role) and RESTAPI role (e.g. netwrix_rest_... |
| 4842 | 0.1649 | *) General HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001... |
| 4843 | 0.1648 | Contact your Global administrator. 3. Review your ... |
| 4844 | 0.1647 | Consider the following examples: In an Access revi... |
| 4845 | 0.1647 | Enter the IP subrange you want to exclude, and cli... |
| 4846 | 0.1646 | Make Search Results Actionnable You can export you... |
| 4847 | 0.1645 | Enter the IP subrange you want to exclude, and cli... |
| 4848 | 0.1643 | Its key fields and user (initiator) account detail... |
| 4849 | 0.1641 | Table 2: Option Description Send report to the use... |
| 4850 | 0.1640 | Workflow of Ownership Assignment Prerequisite: Opt... |
| 4851 | 0.1640 | Usually it is recommended to configure a dedicated... |
| 4852 | 0.1640 | Follow the steps to import snapshots. Step 1 – In ... |
| 4853 | 0.1639 | Enter the IP subrange you want to exclude, and cli... |
| 4854 | 0.1639 | Enter the IP subrange you want to exclude, and cli... |
| 4855 | 0.1639 | Follow the steps to enable Exchange Online Auto Au... |
| 4856 | 0.1638 | The Stop Review window closes. View Responses Wind... |
| 4857 | 0.1638 | Example: Production default instance: PROD-SQL-01 ... |
| 4858 | 0.1638 | *) Hardware HKEY_LOCAL_MACHINE\SYSTEM\CurrentContr... |
| 4859 | 0.1637 | In the environments with root/child domains, the a... |
| 4860 | 0.1635 | For example, "\com\Corp\Users\Departments\IT\Usern... |
| 4861 | 0.1635 | For example, "\com\Corp\Users\Departments\IT\Usern... |
| 4862 | 0.1634 | Expand the Recipients list and click Add to add mo... |
| 4863 | 0.1634 | Make sure that the Report Server URL resource is r... |
| 4864 | 0.1634 | Step 2 – In the Help Protect your computer with Wi... |
| 4865 | 0.1632 | Favorite Reports Initially, the Favorite Reports t... |
| 4866 | 0.1632 | Add the text of this error message to this file to... |
| 4867 | 0.1631 | printQueue object, add the following line: printQu... |
| 4868 | 0.1630 | Ensure that... On the ArcSight side The UDP Receiv... |
| 4869 | 0.1628 | A custom account must be granted the same permissi... |
| 4870 | 0.1627 | If so, data should be filtered accordingly before ... |
| 4871 | 0.1627 | If so, data should be filtered accordingly before ... |
| 4872 | 0.1625 | Instead of updating the ticket every time, the ser... |
| 4873 | 0.1624 | account@example. *.com Enter root web site URLs. C... |
| 4874 | 0.1624 | ActivityRecordWebRequests Internal parameter. The ... |
| 4875 | 0.1623 | Service Board Service tickets created by the add-o... |
| 4876 | 0.1623 | Each <TicketParameter> includes the <Name></Name> ... |
| 4877 | 0.1623 | v10.7 Step 5 – Configure Data Collecting Account. ... |
| 4878 | 0.1621 | See the Edit Notes Window topic for a dditional in... |
| 4879 | 0.1621 | Error Details Error Details On error, most request... |
| 4880 | 0.1621 | The hyperlink will open the Entitlement Reviews in... |
| 4881 | 0.1617 | Filter on Sort by to bring important accounts' dat... |
| 4882 | 0.1616 | In the Change Status dialog, set the status to "re... |
| 4883 | 0.1616 | The Records Management group is less powerful, and... |
| 4884 | 0.1615 | v10.7 Web Application Firewall Geo IP & Botnet Fil... |
| 4885 | 0.1614 | If a similar alert occurs in less than N seconds, ... |
| 4886 | 0.1613 | You can also refresh the alerts information by cli... |
| 4887 | 0.1609 | Sends an email to the assigned owner(s) for the se... |
| 4888 | 0.1608 | The maximum number of Activity Records the Request... |
| 4889 | 0.1608 | In addition, you can customize your view by select... |
| 4890 | 0.1605 | Send alert for <...> activity records within <...>... |
| 4891 | 0.1602 | See the N otifications Page topic for additional i... |
| 4892 | 0.1602 | Manage Recommendations For active recommendations,... |
| 4893 | 0.1599 | Write operation was performed (metadata was fs_wri... |
| 4894 | 0.1598 | The console will look similar to the following: Wi... |
| 4895 | 0.1595 | *) RemovableMedia SYSTEM\CurrentControlSet\Enum v1... |
| 4896 | 0.1594 | The credentials are case sensitive. Specify the ac... |
| 4897 | 0.1594 | The credentials are case sensitive. Specify the ac... |
| 4898 | 0.1593 | Update the template if necessary. CorrelationTicke... |
| 4899 | 0.1593 | *) Services HKEY_LOCAL_MACHINE\SYSTEM\CurrentContr... |
| 4900 | 0.1592 | The 2 Review changes tab opens in the Resource Rev... |
| 4901 | 0.1592 | Possible values: Empty—Check the certificate via W... |
| 4902 | 0.1591 | Click Add and complete the following fields: User ... |
| 4903 | 0.1590 | See the Behavior Anomalies topic for a dditional i... |
| 4904 | 0.1590 | This value is an enumeration with one possible val... |
| 4905 | 0.1588 | Date Created Date Modified Disabled ID Instead of ... |
| 4906 | 0.1585 | This permission allows another user to send the me... |
| 4907 | 0.1584 | Filter on Sort by to bring important accounts' dat... |
| 4908 | 0.1581 | Opens the Remove changes window. Clears all reques... |
| 4909 | 0.1580 | Click Exclude to specify AD domains, OUs, and cont... |
| 4910 | 0.1580 | If you need to change user name or password for ac... |
| 4911 | 0.1580 | Add-on running on the same machine as SCVMM Manage... |
| 4912 | 0.1579 | Step 2 – Select the required data source and click... |
| 4913 | 0.1579 | In the example below, review how the shell script ... |
| 4914 | 0.1577 | For example, to exclude data on the Disabled Accou... |
| 4915 | 0.1577 | Notes can be added by Ownership Administrators or ... |
| 4916 | 0.1577 | Step 7 – In the Reporting Services Configuration C... |
| 4917 | 0.1576 | Specify AD container Click Exclude to specify AD d... |
| 4918 | 0.1576 | Source If you need to specify several sources, you... |
| 4919 | 0.1575 | Otherwise, you will receive an empty report. escap... |
| 4920 | 0.1575 | Same exit codes will be returned by response actio... |
| 4921 | 0.1574 | The 2 Review changes tab opens in the Resource Rev... |
| 4922 | 0.1573 | SCVMM versions: Microsoft System Center Virtual Ma... |
| 4923 | 0.1573 | The credentials are case sensitive. A custom accou... |
| 4924 | 0.1572 | See the Data Grid Features topic for additional in... |
| 4925 | 0.1569 | To obtain them, you will need an API Member accoun... |
| 4926 | 0.1569 | NEWYORKSRV10:81. If you do not want the server nam... |
| 4927 | 0.1568 | Make sure that the resource is reachable. Report M... |
| 4928 | 0.1567 | v10.7 Builtin Administrator Account The Builtin Ad... |
| 4929 | 0.1566 | Notes displayed here can only be added or viewed b... |
| 4930 | 0.1565 | Free disk space is less than <...> MB—Video record... |
| 4931 | 0.1562 | EnableTicketCorrelation true This option is helpfu... |
| 4932 | 0.1562 | The Home > Reports page opens. This page includes ... |
| 4933 | 0.1558 | See the Add Items for Monitoring topic for additio... |
| 4934 | 0.1556 | ◦◦ Permissions for ongoing data collection will de... |
| 4935 | 0.1556 | Consider the following: By default, the add-on doe... |
| 4936 | 0.1555 | • It is recommended to assign the API Member accou... |
| 4937 | 0.1555 | See the Delete Review Window topic for additional ... |
| 4938 | 0.1554 | v10.7 Obtain Tenant Name Follow the steps to obtai... |
| 4939 | 0.1552 | The default value is 86400 seconds, i.e., 24 hours... |
| 4940 | 0.1550 | Download the latest add-on version in the Add-on S... |
| 4941 | 0.1549 | Review the table below to discover how different "... |
| 4942 | 0.1547 | The credentials are case sensitive. Specify the ac... |
| 4943 | 0.1546 | See the Update the Database Service Account Passwo... |
| 4944 | 0.1545 | Once the limit is reached, the service clears acti... |
| 4945 | 0.1545 | Follow the steps to configure Microsoft 365 tenant... |
| 4946 | 0.1544 | Review history and complement EnableTicketCorrelat... |
| 4947 | 0.1543 | v10.7 Step 1 – Navigate to the Access Reviews inst... |
| 4948 | 0.1541 | See Download Client Credentials (Wallets) for more... |
| 4949 | 0.1540 | It opens the Saving review window, which displays ... |
| 4950 | 0.1536 | The following icons appear in this column to indic... |
| 4951 | 0.1534 | Wildcard (*) is supported and can be used to repla... |
| 4952 | 0.1533 | severity 1 Sets Severity to "1 – High". v10.7 <Con... |
| 4953 | 0.1531 | Revoke a role assignment Click next to the user. S... |
| 4954 | 0.1530 | If there are several owners of a resource, the lis... |
| 4955 | 0.1529 | Subscribe to search 1. Navigate to Search and set ... |
| 4956 | 0.1526 | Yes No + Password last changed Equals the Pwd-Last... |
| 4957 | 0.1525 | v10.7 Option Description User has been idle for <.... |
| 4958 | 0.1525 | Mind that in this case, the product does not summa... |
| 4959 | 0.1522 | Port 1521 is the default client co nnections port,... |
| 4960 | 0.1521 | See the View and Search Collected Data topic for a... |
| 4961 | 0.1521 | For example, "Successful read attempts on importan... |
| 4962 | 0.1517 | In the Search field in the Simple mode, this opera... |
| 4963 | 0.1516 | attribute_name—Can be found in the Details column ... |
| 4964 | 0.1516 | Check and process the alert queue every N seconds;... |
| 4965 | 0.1516 | v10.7 The table below provides instructions on how... |
| 4966 | 0.1515 | TicketRequestsRetention RequestLimit 300000 Intern... |
| 4967 | 0.1515 | There are two levels of access, or roles, which ca... |
| 4968 | 0.1514 | Tool-tips display when hovering over the icons ind... |
| 4969 | 0.1514 | Configure Exchange Online State-in-Time Modern Aut... |
| 4970 | 0.1507 | Select the review in the list and click Mark Compl... |
| 4971 | 0.1506 | Apply filters to narrow your report scope. Please ... |
| 4972 | 0.1505 | Lines that start with the # sign are treated as co... |
| 4973 | 0.1504 | A yellow checkmark icon indicates the new level of... |
| 4974 | 0.1504 | Log format – Set to "IETF (RFC 5424)". Enable secu... |
| 4975 | 0.1503 | v10.7 Define Parameters Before running or scheduli... |
| 4976 | 0.1498 | Currently, the cyberark-v2.xml rule file is shippe... |
| 4977 | 0.1498 | * - any machine with a 3-character name or longer ... |
| 4978 | 0.1497 | * - any machine with a 3-character name or longer ... |
| 4979 | 0.1496 | AccessKeyID Access key is used to run requests to ... |
| 4980 | 0.1494 | Configure a non-threshold alert, email recipients ... |
| 4981 | 0.1493 | Filtering does not delete changes, but modifies th... |
| 4982 | 0.1488 | Tool-tips display when hovering over the icons ind... |
| 4983 | 0.1487 | v10.7 Assign Permission via the Registry Editor Sn... |
| 4984 | 0.1486 | Note that hidden anomalies cannot be reviewed in b... |
| 4985 | 0.1484 | If for some reason the product was unable to grant... |
| 4986 | 0.1482 | See the Delete Review Window topic for additional ... |
| 4987 | 0.1481 | Below is an example of the configuration: 11.. Nav... |
| 4988 | 0.1480 | By default, 3 RequestTimeout 180 minutes. Defines ... |
| 4989 | 0.1480 | One of two messages will appear according to if yo... |
| 4990 | 0.1479 | See the Integration API topic for additional infor... |
| 4991 | 0.1478 | See the Add New Resource Wizard topic for addition... |
| 4992 | 0.1478 | Specify delivery options • File format—Configure r... |
| 4993 | 0.1478 | Example: Ireland + Security v10.7 Attribute Descri... |
| 4994 | 0.1478 | The user running the script must have sufficient p... |
| 4995 | 0.1478 | Select Add Folder under the Custom section and spe... |
| 4996 | 0.1477 | The service will automatically substitut e Opened:... |
| 4997 | 0.1476 | Desired – Change suggested by the owner. It could ... |
| 4998 | 0.1476 | In sqlplus tool, execute the following command: Si... |
| 4999 | 0.1475 | Only resources with assigned Owners can be include... |
| 5000 | 0.1473 | The Create Review wizard closes. The new review di... |
| 5001 | 0.1472 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} Leg... |
| 5002 | 0.1471 | Provide a name of the computer ArcSightHost – wher... |
| 5003 | 0.1470 | See the Notification Options topic for additional ... |
| 5004 | 0.1469 | System requirements Make sure that the machine whe... |
| 5005 | 0.1469 | However, to ensure that Reporting Services is prop... |
| 5006 | 0.1468 | CAUTION: This will delete all instances of the sel... |
| 5007 | 0.1468 | Provide connection details in the following format... |
| 5008 | 0.1465 | See the Data Grid Features topic for additional in... |
| 5009 | 0.1462 | Although this is a string collection, only one num... |
| 5010 | 0.1460 | Use the arrow buttons to order the owners. Use the... |
| 5011 | 0.1460 | These can be filters copied from a previous search... |
| 5012 | 0.1460 | The selected user appears in the Owner list. Confi... |
| 5013 | 0.1460 | Step 5 – Navigate to the Actions tab and complete ... |
| 5014 | 0.1458 | Only one usage of each socket address (protocol/ne... |
| 5015 | 0.1456 | The account must be granted the same permissions a... |
| 5016 | 0.1456 | snapshot_delete_snapshot A snapshot was deleted. s... |
| 5017 | 0.1456 | If a ticket flood limit is reached, the service wr... |
| 5018 | 0.1455 | Sends an email to the assigned owner(s) for the se... |
| 5019 | 0.1454 | • Free disk space is less than <...> MB—Video reco... |
| 5020 | 0.1454 | See the Batch Processing topic for instructions on... |
| 5021 | 0.1453 | 66.. To restore the original view configuration, c... |
| 5022 | 0.1450 | Then enter the account information in the User Nam... |
| 5023 | 0.1450 | PathFile Currently, the qumulo.xml rules file is p... |
| 5024 | 0.1448 | The list of containers does not include child doma... |
| 5025 | 0.1447 | For more information on application pool account, ... |
| 5026 | 0.1447 | Ignore users whose passwords have already expired ... |
| 5027 | 0.1445 | Select Edit under Apply tags to associate tags wit... |
| 5028 | 0.1444 | This can help you to simplify product administrati... |
| 5029 | 0.1443 | PCIDSS compliance standard. You can use this filte... |
| 5030 | 0.1441 | These entries correspond to differen t The value l... |
| 5031 | 0.1440 | Your configuration and data will be preserved duri... |
| 5032 | 0.1440 | v10.7 Parameter Default value Description The Even... |
| 5033 | 0.1440 | v10.7 Parameter Default value Description The Even... |
| 5034 | 0.1440 | If necessary, modify the parameters as required. P... |
| 5035 | 0.1440 | before and after values, start and end dates. You ... |
| 5036 | 0.1439 | A baseline defines a certain safe level or state. ... |
| 5037 | 0.1438 | To do it, click Configure next to Alerts. Follow t... |
| 5038 | 0.1437 | Select the desired resource(s) and click Add. The ... |
| 5039 | 0.1436 | NotEqualTo Table 1: Filter Description Supported O... |
| 5040 | 0.1435 | The user name and a date timestamp will appear at ... |
| 5041 | 0.1435 | classname.attrname If there is no full stop, the e... |
| 5042 | 0.1433 | Click Explore. In the File Server REST API Explore... |
| 5043 | 0.1431 | Step 12 – Type repadmin /syncall command and press... |
| 5044 | 0.1431 | A custom account must be granted the same permissi... |
| 5045 | 0.1429 | When prompted to c onfirm granting, click Yes. Ste... |
| 5046 | 0.1428 | Max length: 21 characters. FooterURL Defines URL t... |
| 5047 | 0.1428 | Define Parameters Before running or scheduling the... |
| 5048 | 0.1428 | Define Parameters Before running or scheduling the... |
| 5049 | 0.1427 | You can use a wildcard (*). Click Add and specify ... |
| 5050 | 0.1426 | Table 2: Risk Assessment formula Default risk leve... |
| 5051 | 0.1425 | "Your response has been saved. You may close this ... |
| 5052 | 0.1420 | These permissions are normally given to a user by ... |
| 5053 | 0.1418 | The protocol works as follows: When a user tries t... |
| 5054 | 0.1416 | Table 1: File Description Syntax omitobjlist.txt C... |
| 5055 | 0.1412 | The next time you run the script, it will start re... |
| 5056 | 0.1412 | The next time you run the script, it will start re... |
| 5057 | 0.1412 | The next time you run the script, it will start re... |
| 5058 | 0.1412 | Unavailable Failed to connect to the database. Upg... |
| 5059 | 0.1412 | You can: Use the account that already exists OR - ... |
| 5060 | 0.1411 | This property is required when a user is created. ... |
| 5061 | 0.1410 | For an exact match, use quotation marks and provid... |
| 5062 | 0.1408 | For example, to exclude changes to the Service Des... |
| 5063 | 0.1407 | Health Status Dashboard Schedule Health Summary em... |
| 5064 | 0.1407 | Example: {c43a7694-ba06-46d2ac9b-205f25dfb32d} • L... |
| 5065 | 0.1405 | If you set the Not in group condition for Who filt... |
| 5066 | 0.1405 | Table 1: Option Description Filter by account name... |
| 5067 | 0.1401 | By default, 3 minutes. Defines the co nnection tim... |
| 5068 | 0.1400 | Select Edit under Apply tags to associate tags wit... |
| 5069 | 0.1398 | v10.7 Parameter Mandatory Description Add this par... |
| 5070 | 0.1397 | When using this mode, consider that the "What" fi ... |
| 5071 | 0.1397 | When using this mode, consider that the "What" fi ... |
| 5072 | 0.1396 | Microsoft 365 Management APIs ActivityFeed.Read NO... |
| 5073 | 0.1395 | This option works in co mbination with UpdateTicke... |
| 5074 | 0.1392 | You can enable predefined alerts or create your cu... |
| 5075 | 0.1392 | Possible parameter values: SetDataSourceAsEventCat... |
| 5076 | 0.1392 | Possible parameter values: SetDataSourceAsEventCat... |
| 5077 | 0.1388 | See the Update Resource Wizard topic for additiona... |
| 5078 | 0.1386 | Domain1\John, Domain1\Johnson, and Domain1\Johnny.... |
| 5079 | 0.1385 | For details, refer to Create User Account to Acces... |
| 5080 | 0.1384 | Password last change lastPasswordChangeDateTi me E... |
| 5081 | 0.1384 | For the already existing tenants it is still possi... |
| 5082 | 0.1384 | Table 1: Option Description Notify managers only o... |
| 5083 | 0.1382 | v10.7 The Show Only Changes checkbox is selected b... |
| 5084 | 0.1381 | Source Specify this parameter if you want to be al... |
| 5085 | 0.1380 | The Event Fields tab Event ID Enter the identifier... |
| 5086 | 0.1380 | Each individual permission can be enabled or disab... |
| 5087 | 0.1380 | Assign Permission Via the Registry Editor Snap-in ... |
| 5088 | 0.1379 | See the Integration API topic for additional infor... |
| 5089 | 0.1377 | Value — Specify filter value. See the View and Sea... |
| 5090 | 0.1376 | You can find examples of appropriate logo files in... |
| 5091 | 0.1375 | Step 9 – To create a self-signed certificate to be... |
| 5092 | 0.1375 | Complete the following fields: Option Description ... |
| 5093 | 0.1375 | By default, new. To specify another status, provid... |
| 5094 | 0.1373 | v10.7 Configuration of government Microsoft 365 te... |
| 5095 | 0.1373 | To modify most plan settings, you must be assigned... |
| 5096 | 0.1371 | Be sure to use a different installation folder. St... |
| 5097 | 0.1368 | The syntax greatly depends on the tool you use. St... |
| 5098 | 0.1368 | You can select a whole AD domain, OU or container.... |
| 5099 | 0.1368 | You can select a whole AD domain, OU or container.... |
| 5100 | 0.1366 | Send empty subscriptions when no a ctivity occurre... |
| 5101 | 0.1364 | Navigate to Computer Configuration > Administrativ... |
| 5102 | 0.1364 | Navigate to Computer Configuration > Administrativ... |
| 5103 | 0.1364 | Table 1: Option Description Only report on users w... |
| 5104 | 0.1363 | The ID of ConnectWise Manage subscriber (Managed C... |
| 5105 | 0.1359 | Selecting such databases leads to data overwrites ... |
| 5106 | 0.1359 | Program/script Input "Powershell.exe". Add argumen... |
| 5107 | 0.1358 | Select an action type from the list (Added, Remove... |
| 5108 | 0.1356 | user@tenant.com Specify the user principal name fo... |
| 5109 | 0.1356 | Depending on the error code, the response body may... |
| 5110 | 0.1356 | Specify the time period, in seconds. UpdateInterva... |
| 5111 | 0.1352 | The account must be granted the same permissions a... |
| 5112 | 0.1352 | The account must be granted the same permissions a... |
| 5113 | 0.1352 | As you inspect anomalies and respond to threats, u... |
| 5114 | 0.1352 | Configure Message Forwarding for Nutanix Prism To ... |
| 5115 | 0.1352 | Table 1: Hardware HKEY_LOCAL_MACHINE\SYSTEM\Curren... |
| 5116 | 0.1349 | The group policy will be updated. Step 12 – Type r... |
| 5117 | 0.1349 | Approval Process After all owners assigned to a sp... |
| 5118 | 0.1348 | Only report on users with fine-grained password Se... |
| 5119 | 0.1348 | Grouped alerts for different computers will be del... |
| 5120 | 0.1347 | The credentials are case sensitive. If using a gro... |
| 5121 | 0.1344 | The procedure below explains how to configure redi... |
| 5122 | 0.1344 | If needed, configure the exclusion rules in a simi... |
| 5123 | 0.1341 | In this case, this user will have the most extende... |
| 5124 | 0.1341 | The user account should be a Cloud-only account. F... |
| 5125 | 0.1341 | Execution policy for powershell scripts is set to ... |
| 5126 | 0.1340 | See the View Reports topic for additional informat... |
| 5127 | 0.1339 | Or simply drag and drop the add-on file in the con... |
| 5128 | 0.1336 | Example: "Michael Jones" • Domain\User. Example: e... |
| 5129 | 0.1328 | Facility Netwrix recommends using default values. ... |
| 5130 | 0.1326 | You can use HTML tags when editing a template. v10... |
| 5131 | 0.1324 | nfs_mount Mount to NFS share. replication_create_s... |
| 5132 | 0.1323 | Edit the list of extensions you consider to be ind... |
| 5133 | 0.1323 | Reference for Creating Search Parameters File Revi... |
| 5134 | 0.1323 | User name and password for connection to Nutanix P... |
| 5135 | 0.1322 | During this period you have free, unlimited access... |
| 5136 | 0.1320 | v10.7 Option Description Select this option to rec... |
| 5137 | 0.1318 | If you want to authenticate with AD user account, ... |
| 5138 | 0.1311 | Create Review Wizard The Create Review wizard is o... |
| 5139 | 0.1310 | Calculation formulas for each metric are provided ... |
| 5140 | 0.1310 | See this Microsoft article for details Size (MB) S... |
| 5141 | 0.1309 | NOTE: ONTAP REST API works only over HTTPS protoco... |
| 5142 | 0.1309 | Delete email Yes Message with subject <...> was mo... |
| 5143 | 0.1308 | For example: Using Oracle Wallet Manager. Refer to... |
| 5144 | 0.1308 | It helps organize and centralize sign-in procedure... |
| 5145 | 0.1307 | Equals the Postal-Code attribute. See the Example:... |
| 5146 | 0.1306 | You are investigating an incident in which the SAM... |
| 5147 | 0.1305 | This option works in co mbination with UpdateTicke... |
| 5148 | 0.1304 | This status can appear by accepting the review as-... |
| 5149 | 0.1303 | Make sure this account has a password that expires... |
| 5150 | 0.1303 | Click Add Recipient and provide email address. REC... |
| 5151 | 0.1303 | A custom account must be granted the same permissi... |
| 5152 | 0.1300 | If multiple owners were sent the request, the colu... |
| 5153 | 0.1298 | Copy it to a safe location. See the following Micr... |
| 5154 | 0.1298 | This value is set to 1 by default, which means tha... |
| 5155 | 0.1297 | Basic authentication: access on behalf of a user. ... |
| 5156 | 0.1294 | Scope v10.7 Option Description General Provide the... |
| 5157 | 0.1294 | See the Open Remote TCP Port 9004 topic for additi... |
| 5158 | 0.1292 | See the Access Reviews topic for a dditional infor... |
| 5159 | 0.1291 | Multiple Domains The Allow authentication from the... |
| 5160 | 0.1291 | Specify this parameter if you want to be alerted o... |
| 5161 | 0.1289 | – any machine with a 5-character name ? * - any ma... |
| 5162 | 0.1286 | The review remains static until it is run again. A... |
| 5163 | 0.1284 | Considerations and limitations Reporting for case-... |
| 5164 | 0.1281 | Step 5 – Click Upload. v10.7 The Upload button tex... |
| 5165 | 0.1281 | The pattern you provide here must match the applic... |
| 5166 | 0.1277 | “DisablePasswordExpiratio n” can also be s pecifie... |
| 5167 | 0.1277 | See the corresponding Micr osoft Example: JSmith@d... |
| 5168 | 0.1275 | To apply tags to an alert, navigate to alert setti... |
| 5169 | 0.1275 | ≤ 5% — Low Sharing sensitive data with external Se... |
| 5170 | 0.1273 | The interfaces available to console users are cont... |
| 5171 | 0.1269 | Specify account inactivity period, after which a u... |
| 5172 | 0.1268 | The platform provides security analytics to detect... |
| 5173 | 0.1266 | smb_modify_share An SMB file share was modified. s... |
| 5174 | 0.1265 | Step 2 – Change the value for the AuthSessionTimeo... |
| 5175 | 0.1264 | Execute... cluster1::> system services firewall po... |
| 5176 | 0.1261 | To do this, add two entries one after another. Ent... |
| 5177 | 0.1261 | On the other hand, including a filter value ensure... |
| 5178 | 0.1258 | exclude the exact user specified and Not equal to ... |
| 5179 | 0.1257 | • -1 — disable timeout. Table 2: Event Description... |
| 5180 | 0.1256 | Step 1 – Navigate to your cluster management comma... |
| 5181 | 0.1253 | NOTE: While this property can contain accent chara... |
| 5182 | 0.1251 | Make sure that the SQL Server Name and Database Na... |
| 5183 | 0.1251 | v10.7 The signed in user is displayed in the upper... |
| 5184 | 0.1250 | If you deployed your Oracle Database in a cluster ... |
| 5185 | 0.1249 | Navigate to each group where the user belongs Send... |
| 5186 | 0.1248 | This parameter is applied only if GenerateEventId ... |
| 5187 | 0.1247 | This updates to ownership configuration have been ... |
| 5188 | 0.1247 | When the task has completed (100%), click Close. T... |
| 5189 | 0.1247 | See the View Reports topic for additional informat... |
| 5190 | 0.1247 | To exclude computers from within the specified ran... |
| 5191 | 0.1246 | This can be a “no reply” address. Reply-Display — ... |
| 5192 | 0.1246 | By default, 5 years after a validFrom date. For ex... |
| 5193 | 0.1246 | object_type.property_na me=property_value:objec t_... |
| 5194 | 0.1244 | * - any machine with a 3-character name or longer ... |
| 5195 | 0.1244 | When a successful status is indicated, assigned ow... |
| 5196 | 0.1241 | The table data grid functions the same way as othe... |
| 5197 | 0.1240 | The Console Access wizard opens to the Select Acce... |
| 5198 | 0.1240 | Step 2 – Right-click Registry and select New > Reg... |
| 5199 | 0.1240 | The date and me 6:17:00 PM time information uses I... |
| 5200 | 0.1238 | You can create a custom file or use rules provided... |
| 5201 | 0.1238 | Step 2 – Click Search. Table 1: Error in PowerShel... |
| 5202 | 0.1237 | This option works only when ReopenTicketOnRepetiti... |
| 5203 | 0.1237 | Since you are looking for GPOs only, select GroupP... |
| 5204 | 0.1235 | To edit a report template, click Customize. You ca... |
| 5205 | 0.1235 | With enabled HTTPS, provide the computer name as i... |
| 5206 | 0.1234 | Select Resource — Select the resource or group to ... |
| 5207 | 0.1232 | Such account may have empty password. Yes No + Use... |
| 5208 | 0.1229 | Table 1: Attribute Description Possible values Fil... |
| 5209 | 0.1225 | The default-data-files parameter is the service-po... |
| 5210 | 0.1225 | To get more information about their settings, you ... |
| 5211 | 0.1224 | Reviewer — Primary owner assigned to the resource ... |
| 5212 | 0.1223 | Modify the AccessInformationCenter.Service.exe.Con... |
| 5213 | 0.1222 | Learn more about how these options work in the Con... |
| 5214 | 0.1221 | The service uses the default values unless paramet... |
| 5215 | 0.1220 | Internal parameter. Check and CheckAlertQueueInter... |
| 5216 | 0.1219 | view=graph-rest-1.0 Specifies password policies fo... |
| 5217 | 0.1219 | Microsoft Graph Application.ReadWrite. All Directo... |
| 5218 | 0.1216 | Search field – Begin typing the name of the resour... |
| 5219 | 0.1215 | After the upgrade, all alerts with previously conf... |
| 5220 | 0.1213 | If you have several monitoring plans for monitorin... |
| 5221 | 0.1213 | NOTE: If you want to reopen closed tickets, you mu... |
| 5222 | 0.1213 | Step 4 – Click the Security administrator or Secur... |
| 5223 | 0.1205 | May contain multiple items with the same signInTyp... |
| 5224 | 0.1205 | Click Add and complete the following fields: User ... |
| 5225 | 0.1203 | Each parameter is preceded with a dash; a space se... |
| 5226 | 0.1202 | Password Enter a password. Clear imported data Sel... |
| 5227 | 0.1202 | Exports There are two export buttons above a table... |
| 5228 | 0.1200 | *.com OmitSitScStoreList.txt Contains a list of Sh... |
| 5229 | 0.1200 | The View Responses window closes. Step 5 – Repeat ... |
| 5230 | 0.1199 | Spaces do not separate values, so the whole expres... |
| 5231 | 0.1197 | See the corresponding Micr osoft Password last cha... |
| 5232 | 0.1197 | Specify paths to XML file(s) with regular expressi... |
| 5233 | 0.1196 | Make sure to create a dedicated item inAuditor in ... |
| 5234 | 0.1195 | Edit the whitelist of permitted antivirus tools. A... |
| 5235 | 0.1194 | To subscribe to a custom report 1. Navigate to Rep... |
| 5236 | 0.1193 | v10.7 The information displayed in the table inclu... |
| 5237 | 0.1190 | property=intelligiblena me Inner_type is optional.... |
| 5238 | 0.1189 | Configure a thresholdbased alert with email recipi... |
| 5239 | 0.1188 | The system will send a test message to the specifi... |
| 5240 | 0.1186 | You can use * for cmdlets and their parameters. Li... |
| 5241 | 0.1186 | Domain2\Johnny, John@domain.com. This operator sho... |
| 5242 | 0.1186 | User name Enter a user name for the SMTP authentic... |
| 5243 | 0.1186 | This parameter is applied only if GenerateEventId ... |
| 5244 | 0.1185 | Opens the Review Details page for the selected Vie... |
| 5245 | 0.1184 | Step 2 – Under the App registrations section, sele... |
| 5246 | 0.1183 | RECOMMENDED: Prepare a dedicated gMSA for these pu... |
| 5247 | 0.1182 | However, if it is enabled and a security policy re... |
| 5248 | 0.1181 | At least the first script run should be performed ... |
| 5249 | 0.1181 | You noticed that some domain policies were changed... |
| 5250 | 0.1181 | The Main Road; 10 Shows the locality, such as Exam... |
| 5251 | 0.1178 | Email address Example: JSmith@domain.com + Manager... |
| 5252 | 0.1178 | In such cases, contact your network administrator ... |
| 5253 | 0.1175 | Switch to HTTP APIAdminTool.exe api http Netwrix r... |
| 5254 | 0.1174 | v10.7 v10.7 At the top, the SMTP server and email ... |
| 5255 | 0.1174 | Removing a resource from this table does not delet... |
| 5256 | 0.1173 | To and From support the following date time format... |
| 5257 | 0.1172 | To edit a report template, click Customize. You ca... |
| 5258 | 0.1172 | The credentials are case sensitive. A custom accou... |
| 5259 | 0.1165 | Equals the sAMAccountName attribute. See the Examp... |
| 5260 | 0.1164 | Select the item and click the View Notes button to... |
| 5261 | 0.1164 | So some data may be outdated. – Logon script path ... |
| 5262 | 0.1163 | Step 3 – On the right, locate the Organization Man... |
| 5263 | 0.1161 | [Partially filled bar] with a non-zero% – Indicate... |
| 5264 | 0.1160 | By default, the application is configured to send ... |
| 5265 | 0.1160 | See the Create a Review topic for additional infor... |
| 5266 | 0.1158 | See the Rename Review Window topic for additional ... |
| 5267 | 0.1154 | Follow the steps to assign permissions on the Long... |
| 5268 | 0.1153 | Step 7 – Click Save. Then click OK to confirm. The... |
| 5269 | 0.1153 | Once the limit is reached, the service clears tick... |
| 5270 | 0.1153 | Current access blue icon with a checkmark will tur... |
| 5271 | 0.1152 | Choose Appropriate Execution Scenario The Add-on r... |
| 5272 | 0.1152 | The list of containers does not include child doma... |
| 5273 | 0.1151 | v10.7 Parameter Description Defines whether to use... |
| 5274 | 0.1151 | This value is set to 1 by default, which means tha... |
| 5275 | 0.1148 | The review remains static until it is run again. ◦... |
| 5276 | 0.1148 | ◦◦ All responses processed — Reviews have been app... |
| 5277 | 0.1147 | Process A ctivity Record queue every N seconds; in... |
| 5278 | 0.1145 | The system will send a test message to the specifi... |
| 5279 | 0.1145 | The system will send a test message to the specifi... |
| 5280 | 0.1142 | See the Group Membership Window topic for addition... |
| 5281 | 0.1141 | Declined Ownership Message If you have declined ow... |
| 5282 | 0.1140 | Select those owners and click Remove. Those owners... |
| 5283 | 0.1139 | Administrative group membership sprawl Edit the wh... |
| 5284 | 0.1137 | To open a new ticket for every alert, set the para... |
| 5285 | 0.1136 | replication_modify_source_relationship A replicati... |
| 5286 | 0.1135 | AppNameGroupID — Define application name value by ... |
| 5287 | 0.1134 | Specify an account name (e.g., John) to find all e... |
| 5288 | 0.1132 | For more information on SharePoint permissions and... |
| 5289 | 0.1129 | v10.7 The column selector menu shows all available... |
| 5290 | 0.1129 | Step 2 – Specify search filters to narrow your sea... |
| 5291 | 0.1129 | An identity can be provided by Microsoft (also kno... |
| 5292 | 0.1128 | Register the Add-On Run the install.ps1 PowerShell... |
| 5293 | 0.1128 | Your firewall configura tion depends on network se... |
| 5294 | 0.1127 | Step 3 – Double-click the Log on as a batch job po... |
| 5295 | 0.1127 | Specify the account that you want to define this p... |
| 5296 | 0.1126 | Example: John Smith + Logon name (sAMAccountName) ... |
| 5297 | 0.1125 | Click Customize to edit the notification template,... |
| 5298 | 0.1123 | RacNumber=16&Arg1= Request='GET /cgi-bin/ Remove /... |
| 5299 | 0.1119 | Defines a full path to the png image with the new ... |
| 5300 | 0.1118 | Microsoft Graph Directory.Read.All • Application.R... |
| 5301 | 0.1117 | The account must be granted the same permissions a... |
| 5302 | 0.1117 | The account must be granted the same permissions a... |
| 5303 | 0.1116 | Pending actions may include s outstanding reviews.... |
| 5304 | 0.1114 | View Details Opens the Review Details page for the... |
| 5305 | 0.1114 | Update Credential Passwords Credential passwords o... |
| 5306 | 0.1113 | Step 9 – Repeat the steps 4-8 for keys below: HKEY... |
| 5307 | 0.1113 | However, it can be customized during installation.... |
| 5308 | 0.1110 | smb_delete_share An SMB file share was deleted. sm... |
| 5309 | 0.1109 | The Delete Review window closes. Delete Review Ins... |
| 5310 | 0.1106 | Accepted changes must be implemented outside of th... |
| 5311 | 0.1105 | Step 2 – On the Select Trustee page, enter the fol... |
| 5312 | 0.1103 | lsnrctl start listener_name 99.. Restart the datab... |
| 5313 | 0.1103 | User Landing Page Role based access controls what ... |
| 5314 | 0.1103 | v10.7 Means granted Description For more informati... |
| 5315 | 0.1101 | The element may also include a modifier—a match ty... |
| 5316 | 0.1100 | This account must be granted the database owner (d... |
| 5317 | 0.1099 | *) HKEY_LOCAL_MACHINE\Software\Microsoft\Wi ndows ... |
| 5318 | 0.1097 | Otherwise, XMLTable 1: Parameter Mandatory Descrip... |
| 5319 | 0.1097 | Specify an object type from the Value list or type... |
| 5320 | 0.1094 | With alerts, you can distinguish one alert from an... |
| 5321 | 0.1094 | Changes could only occur between September 16, 201... |
| 5322 | 0.1094 | Compatibility notice The add-on is compatible with... |
| 5323 | 0.1090 | The procedure below explains how to configure redi... |
| 5324 | 0.1088 | The general format is alias@domain, where the doma... |
| 5325 | 0.1085 | DisplayOnlyFirstActivityRecord true Add only the f... |
| 5326 | 0.1085 | Update Resource Wizard The Update resource wizard ... |
| 5327 | 0.1084 | Users Specify monitoring restrictions Select the u... |
| 5328 | 0.1084 | Step 6 – When all recommendations are confirmed an... |
| 5329 | 0.1082 | Specify an account name (e.g., John) to find all e... |
| 5330 | 0.1078 | The Access Reviews begins to create the review. Ac... |
| 5331 | 0.1075 | Application Redirect URI is optional, you can leav... |
| 5332 | 0.1074 | This allows you to make changes to the assigned ow... |
| 5333 | 0.1073 | Step 1 – On the General page of the item propertie... |
| 5334 | 0.1073 | Step 1 – On the General page of the item propertie... |
| 5335 | 0.1072 | This permission SendAs allows another user to send... |
| 5336 | 0.1066 | See the Role-Based Access and Delegationtopic for ... |
| 5337 | 0.1066 | Step 4 – Make sure you have disabled multi-factor ... |
| 5338 | 0.1066 | For example, you can exclude system activity on a ... |
| 5339 | 0.1065 | Select a change to see its rollback details in the... |
| 5340 | 0.1064 | Summary — This page provides a preview of the sett... |
| 5341 | 0.1062 | Navigate to each group where the user belongs to, ... |
| 5342 | 0.1062 | However, if you have specified a time period for A... |
| 5343 | 0.1060 | These granted or denied permissions take preferenc... |
| 5344 | 0.1060 | Step 2 – Modify the AccessInformationCenter.Servic... |
| 5345 | 0.1057 | Object Type Reported Action Reported Properties Cr... |
| 5346 | 0.1054 | Step 5 – When all recommendations are confirmed an... |
| 5347 | 0.1054 | See the Data Grid Features topic for additional in... |
| 5348 | 0.1051 | If you want to write alert details into both field... |
| 5349 | 0.1051 | Step 1 – On the Manage Reviews page, select a revi... |
| 5350 | 0.1049 | Select this option for users to be notified three ... |
| 5351 | 0.1048 | Path The path must be provided in the same format ... |
| 5352 | 0.1047 | For more information on SharePoint web applica tio... |
| 5353 | 0.1046 | Step 1 – On the General page of the item propertie... |
| 5354 | 0.1044 | Step 4 – On the right, double-click the User Right... |
| 5355 | 0.1044 | Information about manifest is also described in th... |
| 5356 | 0.1043 | Hovering over the bar will display the number of i... |
| 5357 | 0.1043 | nfs_modify_export Modified NFS Export that the cli... |
| 5358 | 0.1040 | Specify email address to receive SMS notifications... |
| 5359 | 0.1038 | Your What filter is set to Policy, and so you keep... |
| 5360 | 0.1034 | Select the desired active review(s) and click Send... |
| 5361 | 0.1033 | Step 4 – Modify the default scheduled task name: $... |
| 5362 | 0.1033 | SELECT — Allows an account to retrieve data from o... |
| 5363 | 0.1028 | Once set, these parameter values must stay unchang... |
| 5364 | 0.1026 | ◦◦ Sites.Read.All ◦◦ TeamMember.Read.All Microsoft... |
| 5365 | 0.1020 | This option allows the Review Administrator to pro... |
| 5366 | 0.1018 | Table 1: Parameter Default value Description Ticke... |
| 5367 | 0.1018 | When finished, run the gpupdate /force command to ... |
| 5368 | 0.1015 | Once the limit is reached, the service clears tick... |
| 5369 | 0.1014 | Modify by adding new owners, removing owners, or c... |
| 5370 | 0.1014 | Follow the steps to edit your plan settings: Step ... |
| 5371 | 0.1012 | Considerations and limitations Reporting for case-... |
| 5372 | 0.1011 | If you renamed this database, provide a new name. ... |
| 5373 | 0.1011 | Press Enter and repeat menu section. You will retu... |
| 5374 | 0.1010 | Remember, at any time you can save your recommenda... |
| 5375 | 0.1009 | Zone: Custom (policy) When you extend the web appl... |
| 5376 | 0.1006 | Limit row count in a file to – Select the desired ... |
| 5377 | 0.1003 | Owner Name — Name of the assigned owner Confirmed ... |
| 5378 | 0.1002 | Older tickets requests are cleared. NOTE: Stop and... |
| 5379 | 0.1001 | Internal parameter. Process a ctivity ProcessActiv... |
| 5380 | 0.1001 | Resource Pool Select a resource pool to deploy the... |
| 5381 | 0.0998 | Remember, at any time you can save your recommenda... |
| 5382 | 0.0998 | Step 5 – Finally, at the Summary step, review the ... |
| 5383 | 0.0998 | Edit Notes Opens the Edit Notes window for the sel... |
| 5384 | 0.0997 | See the Fine-Tune Your Plan and Edit Settings topi... |
| 5385 | 0.0995 | See the Add New Resource Wizard topic for addition... |
| 5386 | 0.0995 | Then specify domain administrator name and passwor... |
| 5387 | 0.0995 | Then specify domain administrator name and passwor... |
| 5388 | 0.0994 | In this case, this user will have the most extende... |
| 5389 | 0.0994 | Run secpol.msc. Browse to Security Settings\Local ... |
| 5390 | 0.0993 | Configure a non-threshold alert with email recipie... |
| 5391 | 0.0992 | See the Update Resource Wizard topic for a ddition... |
| 5392 | 0.0992 | Lock statuses apply to a site collection and are u... |
| 5393 | 0.0991 | To specify another status, provide its ID in the <... |
| 5394 | 0.0991 | Otherwise, 'Before' and 'After' values will not be... |
| 5395 | 0.0985 | First/Second/Last time when password expires in <>... |
| 5396 | 0.0985 | Opens the Rename Review window for modifying the R... |
| 5397 | 0.0984 | The script is starting to test your domain control... |
| 5398 | 0.0982 | Response Request Status Response The HTTP status c... |
| 5399 | 0.0982 | Response Request Status Response The HTTP status c... |
| 5400 | 0.0981 | The script is starting to test your domain control... |
| 5401 | 0.0981 | If you want to reopen closed ticke ts, you must be... |
| 5402 | 0.0980 | For that, set up the TrustedHosts list: ◦ to inclu... |
| 5403 | 0.0980 | The Excel file presents an easy to read format, in... |
| 5404 | 0.0979 | Check and process the alert queue every N seconds;... |
| 5405 | 0.0978 | ◦◦ The Tenant name field then will be filled in au... |
| 5406 | 0.0978 | Make sure the post data files (Continuation mark, ... |
| 5407 | 0.0976 | Once users have been granted console access, they ... |
| 5408 | 0.0976 | Follow the steps to play a video: Step 1 – Navigat... |
| 5409 | 0.0975 | Computer Specify a computer (as it is displayed in... |
| 5410 | 0.0974 | Step 4 – Configure client secret for that applicat... |
| 5411 | 0.0974 | Unless specified, the service runs under the accou... |
| 5412 | 0.0973 | v10.7 Cisco Meraki Dashboard Complete the followin... |
| 5413 | 0.0972 | Each ActivityRecord object is collected in braces ... |
| 5414 | 0.0972 | Step 12 – Click Save to save your changes. v10.7 T... |
| 5415 | 0.0971 | Does not contain This operator shows all entries e... |
| 5416 | 0.0971 | The C onfirm Removal window opens. v10.7 Step 2 – ... |
| 5417 | 0.0967 | Step 5 – Proceed with adding the permissions for t... |
| 5418 | 0.0965 | Step 2 – The Select Owners page lists the currentl... |
| 5419 | 0.0960 | The Add new resource wizard opens. Step 2 – On the... |
| 5420 | 0.0957 | Option Description Enter your SMTP server address.... |
| 5421 | 0.0957 | Older tickets requests are cleared. Table 2: <Conn... |
| 5422 | 0.0956 | Maximum length is 64 characters. The name displaye... |
| 5423 | 0.0955 | v10.7 NOTE: Perform this procedure only if the acc... |
| 5424 | 0.0954 | You can set the Details filter to 242464 to find t... |
| 5425 | 0.0953 | Search results will be sorted by all selected filt... |
| 5426 | 0.0953 | User principal name userPrincipalName Example: "us... |
| 5427 | 0.0952 | Remember, a resource with declined ownership needs... |
| 5428 | 0.0952 | Otherwise, leave the default value. RuleFileList P... |
| 5429 | 0.0951 | Use a standard account for that purpose. Follow th... |
| 5430 | 0.0949 | NOTE: This is default location. However, it may be... |
| 5431 | 0.0947 | Risks are marked with red color and are easy to sp... |
| 5432 | 0.0946 | Email address Equals the manager / mail Manager em... |
| 5433 | 0.0945 | There are no specific requirements for changing th... |
| 5434 | 0.0943 | v10.7 Parameter Default value Description Instead ... |
| 5435 | 0.0942 | See the following Microsoft article for additional... |
| 5436 | 0.0940 | The credentials are case sensitive. If using a gro... |
| 5437 | 0.0939 | Video Recording For these settings to become effec... |
| 5438 | 0.0938 | Storage Select the destination storage. Disk Forma... |
| 5439 | 0.0937 | See the corresponding Micro soft article for more ... |
| 5440 | 0.0935 | The computer where the add-on will be installed Th... |
| 5441 | 0.0932 | See the Data C ollecting Account topic for more in... |
| 5442 | 0.0932 | Select this option to exclude users who do not hav... |
| 5443 | 0.0931 | v10.7 Remove Changes Window Select the desired res... |
| 5444 | 0.0926 | Delete accounts after Specify account inactivity p... |
| 5445 | 0.0925 | APIAdminTool.exe api https Switch to HTTPS Run thi... |
| 5446 | 0.0924 | Ready to Complete Review your virtual machine sett... |
| 5447 | 0.0924 | The element may also include a modifier—a match ty... |
| 5448 | 0.0924 | Grant Required Roles Follow the steps to grant the... |
| 5449 | 0.0923 | Revoke a role assignment • Click next to the user.... |
| 5450 | 0.0922 | To reduce the risk of data leaks and non-complianc... |
| 5451 | 0.0921 | Step 2 – Right-click the ADSI Edit node and select... |
| 5452 | 0.0921 | Step 5 – Remediation of the accepted changes must ... |
| 5453 | 0.0919 | A custom account must be granted the same permissi... |
| 5454 | 0.0919 | These are general guidelines you can adopt when se... |
| 5455 | 0.0918 | https://URL Enter list or list item URI (Unique re... |
| 5456 | 0.0915 | Step 3 – Review the script and provide parameters.... |
| 5457 | 0.0914 | Then provide the full path of the machine to exclu... |
| 5458 | 0.0914 | v10.7 Remember, click Save after making modificati... |
| 5459 | 0.0912 | v10.7 Follow the steps to add or remove a Favorite... |
| 5460 | 0.0909 | MailboxSettings.Read 2. Microsoft 365 Management A... |
| 5461 | 0.0906 | Once set, these parameter values must stay unchang... |
| 5462 | 0.0906 | Once set, these parameter values must stay unchang... |
| 5463 | 0.0905 | You can use * for cmdlets and their parameters. Li... |
| 5464 | 0.0903 | See the Microsoft Entra ID topic for additional in... |
| 5465 | 0.0903 | A wildcard (*) is supported. You can use * for cmd... |
| 5466 | 0.0901 | v10.7 Follow the steps to exclude specific user ac... |
| 5467 | 0.0901 | v10.7 Follow the steps to exclude specific user ac... |
| 5468 | 0.0900 | 0% — Low Files may be shared with any users Sensit... |
| 5469 | 0.0897 | Add Console Users Follow the steps to grant domain... |
| 5470 | 0.0895 | Grant Permissions for the Deleted Objects Containe... |
| 5471 | 0.0894 | v10.7 On the Manage Reviews page in the Entitlemen... |
| 5472 | 0.0891 | Table 1: Option Description Sender address Enter t... |
| 5473 | 0.0890 | Step 3 – Click OK when finished. The Rename Review... |
| 5474 | 0.0887 | Enter the IP subrange you want to exclude, and cli... |
| 5475 | 0.0886 | RequestTimeout 180 Internal parameter. By default,... |
| 5476 | 0.0880 | Connect to the SQL Server instance. In the left pa... |
| 5477 | 0.0879 | the following line: Default Domain Policy. <settin... |
| 5478 | 0.0876 | User name Specify the account to connect to SSRS. ... |
| 5479 | 0.0874 | Enable monitoring of unauthorized access to mailbo... |
| 5480 | 0.0872 | Review roles that are already defined for this sco... |
| 5481 | 0.0871 | .NET 4.5 or later must be installed. The computer ... |
| 5482 | 0.0868 | Enter event ID number or range of event IDs separa... |
| 5483 | 0.0865 | https_proxy_port — specify port used for HTTP prox... |
| 5484 | 0.0865 | Notify users by email every day if their accounts ... |
| 5485 | 0.0864 | You can use * for cmdlets and their parameters. Li... |
| 5486 | 0.0864 | Step 5 – Replace the "?/network/admin" parameter w... |
| 5487 | 0.0863 | Update a Resource Follow the steps to update owner... |
| 5488 | 0.0863 | Step 7 – Check Allow next to the "Read" permission... |
| 5489 | 0.0863 | If you set the Who filter to ends with John, you w... |
| 5490 | 0.0860 | See the View Responses Window topic for additional... |
| 5491 | 0.0858 | Step 2 – Grant required permissions to that applic... |
| 5492 | 0.0855 | Table 2: Request Status Response Success The HTTP ... |
| 5493 | 0.0854 | Modify an existing alert Select an alert from the ... |
| 5494 | 0.0853 | See the Approval Process topic for additional info... |
| 5495 | 0.0846 | Specify the account to connect to SSRS. Use the fo... |
| 5496 | 0.0846 | These users— Select to exclude specific users' act... |
| 5497 | 0.0843 | See the Microsoft Entra ID topic for additional in... |
| 5498 | 0.0841 | Step 1 – Navigate to Start > Windows Administrativ... |
| 5499 | 0.0839 | NOTE: The new password is encrypted in the AccessI... |
| 5500 | 0.0839 | However, this can be customized on the Configurati... |
| 5501 | 0.0837 | It is possible to insert variables into the subjec... |
| 5502 | 0.0837 | It is possible to insert variables into the subjec... |
| 5503 | 0.0828 | v10.7 Access is enabled – A user's account must be... |
| 5504 | 0.0828 | Example: "Michael Jones" Domain\User. Example: ent... |
| 5505 | 0.0828 | A listener allows you to connect to a replica with... |
| 5506 | 0.0827 | Exclusion rules are optional. Click Add Inclusion ... |
| 5507 | 0.0826 | Follow the steps to configure the Log On As a Batc... |
| 5508 | 0.0825 | Step 6 – When remediation is complete, return to t... |
| 5509 | 0.0824 | + Smith Equals the Title attribut e. See the corre... |
| 5510 | 0.0824 | dc11.local/OU will exclude the OU itself. However,... |
| 5511 | 0.0820 | Copy search — copy the search filters that are cur... |
| 5512 | 0.0819 | Specify a computer. You will only be alerted on ev... |
| 5513 | 0.0817 | See the Add Owner Window topic for additional info... |
| 5514 | 0.0814 | To exclude the certain user's mailbox, enter usern... |
| 5515 | 0.0813 | Provide user names as shown in the "Who" column in... |
| 5516 | 0.0812 | In-Script Parameters You may also need to modify t... |
| 5517 | 0.0812 | In-Script Parameters You may also need to modify t... |
| 5518 | 0.0812 | In-Script Parameters You may also need to modify t... |
| 5519 | 0.0812 | Switch to the Advanced permissions section. Check ... |
| 5520 | 0.0811 | Select the newly created virtual machine and click... |
| 5521 | 0.0810 | Check the box and enter the new password in both e... |
| 5522 | 0.0809 | Create User Account to Access Nutanix REST API To ... |
| 5523 | 0.0807 | The minimum value specified across the plans will ... |
| 5524 | 0.0806 | Select this option to notify users that their pass... |
| 5525 | 0.0806 | Delegate Admin SendAs A message was sent using the... |
| 5526 | 0.0805 | Follow the steps to exclude specific user activity... |
| 5527 | 0.0805 | Follow the steps to exclude specific user activity... |
| 5528 | 0.0804 | Step 1 – In the Resource Owners interface, select ... |
| 5529 | 0.0804 | Step 2 – Grant required permissions to that applic... |
| 5530 | 0.0796 | 400 Bad Request Error Error validating A ctivity R... |
| 5531 | 0.0792 | precise results, e.g., \ \FS\Share\NewPolicy.docx.... |
| 5532 | 0.0792 | The UPN is an Internetstyle login name for the use... |
| 5533 | 0.0791 | Email address Example: JSmith@domain.com + Office ... |
| 5534 | 0.0790 | • .NET 4.5 or later must be installed. Execution p... |
| 5535 | 0.0789 | You will be asked to authenticate for your respons... |
| 5536 | 0.0787 | Column—Specify table column name. The following co... |
| 5537 | 0.0786 | The next time you run the script, it will start re... |
| 5538 | 0.0785 | Ensure that... Set-ExecutionPolicy Unrestricted • ... |
| 5539 | 0.0779 | Table 1: Button Description Create Launches the Cr... |
| 5540 | 0.0778 | UserName Defines a username used to connect to SQL... |
| 5541 | 0.0777 | Click Add Rule. Specify a name of the Oracle datab... |
| 5542 | 0.0775 | { "resourceAppId": "00000003-0000-0ff1-ce00-000000... |
| 5543 | 0.0775 | Click Exclude from search or Include to search and... |
| 5544 | 0.0772 | The first thing that should be done is to configur... |
| 5545 | 0.0770 | An arrow will appear next to the column name indic... |
| 5546 | 0.0770 | Stop Review Window The Stop Review window opens fr... |
| 5547 | 0.0766 | Step 1 – Specify what user accounts should be excl... |
| 5548 | 0.0766 | Step 1 – Specify what user accounts should be excl... |
| 5549 | 0.0765 | ◦◦ Make sure this user account has sufficient acce... |
| 5550 | 0.0763 | Step 2 – In the Services snap-in, locate the Remot... |
| 5551 | 0.0761 | Characters may be also s pecified with hex value u... |
| 5552 | 0.0759 | The Create Review wizard opens. Step 2 – On the Re... |
| 5553 | 0.0759 | If you want the script to use another account to a... |
| 5554 | 0.0758 | Authentication Select the authentication type you ... |
| 5555 | 0.0757 | Sender address RECOMMENDED: click Send Test Email.... |
| 5556 | 0.0756 | ◦◦ Make sure this user account has sufficient acce... |
| 5557 | 0.0756 | ◦◦ Make sure this user account has sufficient acce... |
| 5558 | 0.0754 | Run Windows PowerShell as administrator and execut... |
| 5559 | 0.0751 | immediately. So some data may be outdated. Equals ... |
| 5560 | 0.0750 | Step 4 – In the Back up files and directories Prop... |
| 5561 | 0.0749 | category software Sets the incident Category to "S... |
| 5562 | 0.0745 | <v v="*S-1-5-21-1180699209 877415012-318292XXXX-XX... |
| 5563 | 0.0744 | Equals This operator shows all entries with the ex... |
| 5564 | 0.0743 | Provide user names as shown in the "Who" column in... |
| 5565 | 0.0743 | Provide user names as shown in the "Who" column in... |
| 5566 | 0.0743 | Provide user names as shown in the "Who" column in... |
| 5567 | 0.0741 | Ignore users who must change password at next logo... |
| 5568 | 0.0740 | In this case, this user will have the most extende... |
| 5569 | 0.0740 | Example: The Main Road; 10 + City Shows the locali... |
| 5570 | 0.0739 | This allows you to add one resource at a time and ... |
| 5571 | 0.0738 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 5572 | 0.0735 | v10.7 Option Description ◦ *computer* - machines w... |
| 5573 | 0.0735 | See the Risk Score topic for additional informatio... |
| 5574 | 0.0735 | See the Risk Score topic for additional informatio... |
| 5575 | 0.0735 | This operator shows all entries except those that ... |
| 5576 | 0.0734 | Step 2 – Click Add Inclusion. Step 3 – Provide UNC... |
| 5577 | 0.0733 | It can be your company's Exchange server or any pu... |
| 5578 | 0.0732 | Then the search query will return only data matchi... |
| 5579 | 0.0732 | Switch to Advanced mode to review your current sea... |
| 5580 | 0.0731 | v10.7 Step 5 – The action status displays on the p... |
| 5581 | 0.0730 | For more information, read the following Micr osof... |
| 5582 | 0.0725 | Applying tags to alerts allows you to distinguish ... |
| 5583 | 0.0721 | v10.7 Grant Required Permissions You need to grant... |
| 5584 | 0.0720 | See the Update the Active Directory Service Accoun... |
| 5585 | 0.0719 | See the Ownership Confirmation topic for additiona... |
| 5586 | 0.0716 | Modify as desired and relaunch the review. See the... |
| 5587 | 0.0712 | Virtual Machines Select the virtual machines to be... |
| 5588 | 0.0709 | However, if you have the Deny log on as a batch jo... |
| 5589 | 0.0709 | { "resourceAppId": "00000003-0000-0000-c000-000000... |
| 5590 | 0.0709 | See the corresponding Micro soft article for more ... |
| 5591 | 0.0708 | v10.7 You can configure Group Policy Preferences t... |
| 5592 | 0.0708 | Decline Declines, or rejects, the owner-recommende... |
| 5593 | 0.0704 | Save the settings.xml file. New configuration sett... |
| 5594 | 0.0703 | Sender address RECOMMENDED: click Send Test Email.... |
| 5595 | 0.0700 | *) HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432 NODE\MICROS... |
| 5596 | 0.0700 | Run Again Modify as desired and relaunch the revie... |
| 5597 | 0.0699 | See Response Status Codes for more information. v1... |
| 5598 | 0.0698 | See the Console Access Page topic for information.... |
| 5599 | 0.0697 | If you want to use a file path, run the following ... |
| 5600 | 0.0696 | The Tags page contains a complete list of alerts t... |
| 5601 | 0.0695 | Table 2: Option Description Modify scheduled task ... |
| 5602 | 0.0693 | Step 1 – In the dashboard pane, select the metric ... |
| 5603 | 0.0692 | For example: NewStation\Shared. Do not specify a d... |
| 5604 | 0.0692 | The computer where the script will be executed • P... |
| 5605 | 0.0691 | RECOMMENDED: click Send Test Email. The system wil... |
| 5606 | 0.0687 | Step 8 – Type repadmin /syncall command and press ... |
| 5607 | 0.0685 | v10.7 Step 7 – Check Allow next to the Read permis... |
| 5608 | 0.0681 | Modern authentication: v10.7 ◦◦ Selected, Microsof... |
| 5609 | 0.0673 | nfs_create_export Created NFS Export that the clie... |
| 5610 | 0.0671 | The parameters inside this section correspond to C... |
| 5611 | 0.0670 | If you are going to use Modern authentication, pas... |
| 5612 | 0.0670 | If you are going to use Modern authentication, pas... |
| 5613 | 0.0669 | omitproplist_gp.txt The file contains a list of th... |
| 5614 | 0.0668 | ◦ If necessary, add the IP addresses of required A... |
| 5615 | 0.0668 | Create firewall policy or edit existing policy to ... |
| 5616 | 0.0667 | For example, to exclude a list item with the https... |
| 5617 | 0.0665 | Currently, the add-on supports only one Prism inst... |
| 5618 | 0.0664 | User runs program through Run As Application Run A... |
| 5619 | 0.0662 | ◦ validFrom—Optional, defines a certificat e start... |
| 5620 | 0.0662 | ◦ validFrom—Optional, defines a certificat e start... |
| 5621 | 0.0661 | SharePoint Server permission levels are defined at... |
| 5622 | 0.0660 | Example: New York + ZIP/postal code Equals the Pos... |
| 5623 | 0.0658 | If you are going to use Modern authentication, pas... |
| 5624 | 0.0655 | Wrong HTTP request was sent (any except GET or POS... |
| 5625 | 0.0649 | Follow the steps to modify schema container settin... |
| 5626 | 0.0647 | If you want the script to use another account to a... |
| 5627 | 0.0647 | In the Connection Settings dialog, enable Select a... |
| 5628 | 0.0646 | Servers with inappropriate operating systems Edit ... |
| 5629 | 0.0646 | See the following Microsoft article for additional... |
| 5630 | 0.0646 | See the following Microsoft article for additional... |
| 5631 | 0.0643 | Step 4 – Alternatively, you can use the following ... |
| 5632 | 0.0642 | Type "mmc" in the box and click OK. This will open... |
| 5633 | 0.0640 | Step 5 – In the left pane, expand the Security nod... |
| 5634 | 0.0640 | Step 3 – Click Manage roles. v10.7 Step 4 – In the... |
| 5635 | 0.0640 | By default, this option is disabled. Video Recordi... |
| 5636 | 0.0639 | Step 2 – Specify what actions should be excluded: ... |
| 5637 | 0.0639 | impact 1 Sets Impact to "1 – High". urgency 1 Sets... |
| 5638 | 0.0631 | Make sure to provide a full object name or path. U... |
| 5639 | 0.0630 | Review the tips for running the tool: Some command... |
| 5640 | 0.0630 | The review can be run as-is by navigating through ... |
| 5641 | 0.0630 | count=Number No Add this parameter to define the n... |
| 5642 | 0.0624 | v10.7 CAUTION: This will prevent owners from compl... |
| 5643 | 0.0622 | Make sure to provide a full object name or path. T... |
| 5644 | 0.0622 | Table 2: Request Status Response Success The HTTP ... |
| 5645 | 0.0621 | The rest operation = object type For example: add ... |
| 5646 | 0.0620 | Process A ctivity ProcessActivityRecordQueueInterv... |
| 5647 | 0.0618 | Table 2: To... Use... Export Copy search — copy th... |
| 5648 | 0.0615 | Connect to your SonicWall device. Launch an Intern... |
| 5649 | 0.0613 | Modify an existing alert Select an alert from the ... |
| 5650 | 0.0612 | Step 1 – Sign in to the Cisco Meraki Dashboard. St... |
| 5651 | 0.0611 | To specify another status, provide its ID in the <... |
| 5652 | 0.0610 | Information about manifest is also described in th... |
| 5653 | 0.0610 | PowerShell 3.0 or later must be installed. .NET 4.... |
| 5654 | 0.0608 | If you set the Who filter to ends This operator sh... |
| 5655 | 0.0607 | User If you need to specify several users, you can... |
| 5656 | 0.0606 | See the Example: corresponding Micro soft Canonica... |
| 5657 | 0.0605 | Send notifications to all resource owners — This o... |
| 5658 | 0.0603 | For example: nwxtech.com,example.com Remember, cli... |
| 5659 | 0.0599 | Step 3 – Configure the following settings: Enable ... |
| 5660 | 0.0597 | Managers will receive a notification in the day wh... |
| 5661 | 0.0594 | Instead of creating a new ticke t, reopen an exist... |
| 5662 | 0.0594 | Otherwise, leave the default value. Specify paths ... |
| 5663 | 0.0594 | In this case, this user will have the most extende... |
| 5664 | 0.0594 | Default is Medium. v10.7 Parameter Description Spe... |
| 5665 | 0.0589 | Enable Remote Registry Service Follow the steps to... |
| 5666 | 0.0580 | Specify a user account. Make sure the user has suf... |
| 5667 | 0.0577 | Step 4 – Log in to this account and navigate to My... |
| 5668 | 0.0577 | Send the request, clicking Try it out. Get the res... |
| 5669 | 0.0573 | The response body contains Activity Records and Co... |
| 5670 | 0.0572 | Some SMTP servers traditionally have been configur... |
| 5671 | 0.0568 | Add to Favorites This option is greyed out when vi... |
| 5672 | 0.0564 | Follow the steps of the wizard to configure connec... |
| 5673 | 0.0563 | This option is greyed out when viewing the Favorit... |
| 5674 | 0.0561 | ◦ store—Optional, defines the store name where cer... |
| 5675 | 0.0559 | Grant Admin Consent to a Tenant Go to the Microsof... |
| 5676 | 0.0559 | Grant Admin Consent to a Tenant Go to the Microsof... |
| 5677 | 0.0558 | Move to a specific OU after OU name—Specify OU nam... |
| 5678 | 0.0558 | Follow the steps to generate a self-signed certifi... |
| 5679 | 0.0555 | You can also change the password for the Builtin A... |
| 5680 | 0.0555 | The Delete Review window closes. Rename Review Win... |
| 5681 | 0.0555 | Alternatively, you can use Windows Task Scheduler.... |
| 5682 | 0.0553 | Modify the new service-policy by adding services t... |
| 5683 | 0.0553 | Then you will provide this account in the item. Fo... |
| 5684 | 0.0552 | Step 6 – Navigate to the Notifications tab and com... |
| 5685 | 0.0552 | Decline Declines, or rejects, the owner-recommende... |
| 5686 | 0.0551 | v10.7 Step 4 – Specify Active Directory credential... |
| 5687 | 0.0551 | ◦ store—Optional, defines the store name where cer... |
| 5688 | 0.0548 | v10.7 Enter a name in the search field to find and... |
| 5689 | 0.0546 | Enter the address that will appear in the From fie... |
| 5690 | 0.0539 | Specify the time period, in seconds. During this t... |
| 5691 | 0.0539 | It can be your SMTP server company's Exchange serv... |
| 5692 | 0.0536 | Step 2 – Under the App registrations section, sele... |
| 5693 | 0.0536 | Step 2 – Under the App registrations section, sele... |
| 5694 | 0.0536 | Step 2 – Under the App registrations section, sele... |
| 5695 | 0.0535 | State: %state% Step 6 – Review the <ReopenTicketOp... |
| 5696 | 0.0535 | Unchecking this option allows you to configure acc... |
| 5697 | 0.0534 | Import Virtual Machine from Image to Hyper-V Perfo... |
| 5698 | 0.0534 | It defines the tickets the add-on can reopen autom... |
| 5699 | 0.0532 | Click Finish to restart the add-on service so that... |
| 5700 | 0.0530 | These Substitution Tokens begin and end with the “... |
| 5701 | 0.0524 | Defines a ticket status once it is reopened. By de... |
| 5702 | 0.0522 | Follow the steps to enable the Remote Registry ser... |
| 5703 | 0.0521 | Step 5 – Navigate to HKEY_LOCAL_MACHINE\SECURITY\P... |
| 5704 | 0.0516 | Make sure the user has sufficient permissions to c... |
| 5705 | 0.0515 | 11.. Add the following line to the sqlnet.ora file... |
| 5706 | 0.0512 | If the value is false, proceed with the steps belo... |
| 5707 | 0.0509 | You can use * for cmdlets and their parameters. Li... |
| 5708 | 0.0509 | Unless specified, the service will run under the L... |
| 5709 | 0.0508 | Table 1: Step Description Rename virtual machine S... |
| 5710 | 0.0506 | v10.7 Step 4 – If Microsoft Entra Kerberos or Acti... |
| 5711 | 0.0505 | If you need to find the $certHash value of a certi... |
| 5712 | 0.0503 | The syntax greatly depends on the tool you use. St... |
| 5713 | 0.0502 | Make sure the post data files (Continuation mark, ... |
| 5714 | 0.0500 | The syntax greatly depends on the tool you use. Yo... |
| 5715 | 0.0496 | The user is removed from the list on the Console A... |
| 5716 | 0.0486 | See the Navigation and Customize Home Screen topic... |
| 5717 | 0.0485 | Step 4 – In the Permission Entry for <Folder_Name>... |
| 5718 | 0.0484 | Follow the steps to configure weekly reminders to ... |
| 5719 | 0.0482 | Configure the Log On As a Batch Job policy via Loc... |
| 5720 | 0.0479 | Download and unpack the new add-on package to the ... |
| 5721 | 0.0465 | It must be eight or more characters long. After se... |
| 5722 | 0.0462 | In this case, redefine the "Deny log on as a batch... |
| 5723 | 0.0459 | Step 3 – It will be necessary to add your Console ... |
| 5724 | 0.0459 | General NOTE: Make sure that the Send alert when t... |
| 5725 | 0.0455 | Step 2 – Register an Azure App and grant it the fo... |
| 5726 | 0.0454 | Step 2 – Browse to Services > Group Key Distributi... |
| 5727 | 0.0452 | Action Select Allow the connection Profile Applies... |
| 5728 | 0.0451 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5729 | 0.0451 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5730 | 0.0443 | Edit the mailboxestoinclude.txt file to specify ma... |
| 5731 | 0.0441 | Step 5 – Click the Register button. Application Re... |
| 5732 | 0.0441 | Step 5 – Click the Register button. Application Re... |
| 5733 | 0.0441 | Step 5 – Click the Register button. Application Re... |
| 5734 | 0.0436 | v10.7 Step 5 – Click Test Settings to ensure a con... |
| 5735 | 0.0434 | Click Add and complete the following: Option Descr... |
| 5736 | 0.0426 | Open the Group Policy Management console on the do... |
| 5737 | 0.0424 | Select the following checkboxes: Authentication Au... |
| 5738 | 0.0423 | To do this, Alert Details: rename <Name>work_notes... |
| 5739 | 0.0422 | In-script parameters are listed in the table below... |
| 5740 | 0.0422 | In-script parameters are listed in the table below... |
| 5741 | 0.0421 | Execution policy for powershell scripts is set to ... |
| 5742 | 0.0421 | Execution policy for powershell scripts is set to ... |
| 5743 | 0.0421 | Execution policy for powershell scripts is set to ... |
| 5744 | 0.0421 | Execution policy for powershell scripts is set to ... |
| 5745 | 0.0420 | Execution policy for powershell scripts is set to ... |
| 5746 | 0.0420 | Execution policy for powershell scripts is set to ... |
| 5747 | 0.0420 | Execution policy for powershell scripts is set to ... |
| 5748 | 0.0420 | Execution policy for powershell scripts is set to ... |
| 5749 | 0.0418 | v10.7 Step 5 – Paste Azure Connection String in th... |
| 5750 | 0.0418 | The TCP 5985 port must be open on Windows Add-on i... |
| 5751 | 0.0416 | Check the columns you want to include and clear un... |
| 5752 | 0.0413 | To Collect Data via API Key To work with multi-fac... |
| 5753 | 0.0410 | NOTE: The password that is generated will contain ... |
| 5754 | 0.0410 | Action Allow the connection Profile Applies to Dom... |
| 5755 | 0.0408 | To perform this procedure, you will need the ADSI ... |
| 5756 | 0.0405 | See the following Microsoft article for more infor... |
| 5757 | 0.0403 | To edit SMS Notifications template, click Customiz... |
| 5758 | 0.0402 | Specify account inactivity period, after which a S... |
| 5759 | 0.0400 | See Use Filters in Advanced Mode for details. By d... |
| 5760 | 0.0397 | Procedure for Nutanix Prism Element Follow the ste... |
| 5761 | 0.0397 | Step 3 – In the Windows Firewall with Advanced Sec... |
| 5762 | 0.0396 | Administrators Administrators with access to the s... |
| 5763 | 0.0393 | Click Add. Schema and object names are case sensit... |
| 5764 | 0.0392 | Step 4 – Click Select. v10.7 Step 5 – Enter your t... |
| 5765 | 0.0390 | If you select this option, the fields below are no... |
| 5766 | 0.0382 | Display the following From address in email notifi... |
| 5767 | 0.0381 | Step 6 – Click Install. Table 1: Option Descriptio... |
| 5768 | 0.0380 | Step 1 – Accept EULA. Step 2 – Select the installa... |
| 5769 | 0.0379 | This key is created once, so if there are any gMSA... |
| 5770 | 0.0378 | You can access Cisco Meraki dashboard using API se... |
| 5771 | 0.0378 | Modify subscriptions Select the subscription that ... |
| 5772 | 0.0377 | If you do not enable the Network traffic compressi... |
| 5773 | 0.0362 | Port number Specify your SMTP server port number. ... |
| 5774 | 0.0362 | Port number Specify your SMTP server port number. ... |
| 5775 | 0.0357 | v10.7 Step 2 – Select Manifest on the left. Step 3... |
| 5776 | 0.0356 | Step 3 – Select the desired action for all recomme... |
| 5777 | 0.0355 | Right-click the effective domain controllers polic... |
| 5778 | 0.0348 | If multiple domains are known, then the username n... |
| 5779 | 0.0346 | See the Grant Required Permissions topic for addit... |
| 5780 | 0.0344 | Below is an example of a mask: ◦ * - any machine ◦... |
| 5781 | 0.0343 | See the section below for the instructions on user... |
| 5782 | 0.0342 | If you want to reopen closed tickets, you must be ... |
| 5783 | 0.0341 | Entering multiple individual addresses is not supp... |
| 5784 | 0.0340 | v10.7 If you select to launch the RestAPI Explorer... |
| 5785 | 0.0339 | Sales Equals the TelephoneNumber attribute. See th... |
| 5786 | 0.0332 | Step 6 – If the SMTP settings are configured corre... |
| 5787 | 0.0329 | In the Request API permissions window, click Micro... |
| 5788 | 0.0326 | In the Connection Settings dialog, enable Select a... |
| 5789 | 0.0319 | PublicKey Public key you obtained for the API Memb... |
| 5790 | 0.0317 | Step 1 – Accept EULA. Step 2 – Select the installa... |
| 5791 | 0.0316 | Execution policy for powershell scripts is set to ... |
| 5792 | 0.0316 | Before configuring the "From" field for user email... |
| 5793 | 0.0312 | Configure network • Select Y to use DHCP server to... |
| 5794 | 0.0312 | v10.7 Step 2 – Select Manifest on the left. Step 3... |
| 5795 | 0.0311 | Follow the steps to remove a user’s configured con... |
| 5796 | 0.0308 | To enter multiple accounts, use comma as a separat... |
| 5797 | 0.0308 | To enter multiple accounts, use comma as a separat... |
| 5798 | 0.0303 | See the IT Risk Assessment Overview topic for addi... |
| 5799 | 0.0299 | Provide a different password if necessary. v10.7 P... |
| 5800 | 0.0298 | User name – Specify a user name to connect to Pris... |
| 5801 | 0.0297 | Specifies the password profile for a user. The pas... |
| 5802 | 0.0297 | Step 1 – On any domain controller in the target do... |
| 5803 | 0.0288 | Step 2 – Define parameters such as ServiceNow conn... |
| 5804 | 0.0285 | Step 1 – In Internet Explorer, navigate to Tools >... |
| 5805 | 0.0283 | Step 1 – Navigate to Start > Server Manager. Step ... |
| 5806 | 0.0283 | Port number Specify your SMTP server port number. ... |
| 5807 | 0.0282 | The permissions inheritance for any of these eleme... |
| 5808 | 0.0280 | The binding command has several environmental vari... |
| 5809 | 0.0278 | Step 3 – Select the Exchange Administrator or Glob... |
| 5810 | 0.0272 | Follow the procedure described below. Follow the s... |
| 5811 | 0.0271 | If you select this option, the fields below are no... |
| 5812 | 0.0267 | Step 3 – Save Client ID and Tenant ID. Step 4 – Cr... |
| 5813 | 0.0266 | SMTP authentication Select this checkbox if your m... |
| 5814 | 0.0263 | The owner will be required to complete the review ... |
| 5815 | 0.0258 | Below is an example of a mask: • * - any machine •... |
| 5816 | 0.0253 | Windows Features Communication Follow the steps to... |
| 5817 | 0.0253 | NOTE: These steps are for modifying domain users w... |
| 5818 | 0.0247 | 33.. Search the group of risks you want to pin to ... |
| 5819 | 0.0246 | Execution policy for powershell scripts is set to ... |
| 5820 | 0.0246 | Depending on your network environment, you may nee... |
| 5821 | 0.0241 | 1122.. Navigate to System → Configuration → Advanc... |
| 5822 | 0.0236 | Enter the address that will appear in the "From" f... |
| 5823 | 0.0235 | Select this option for users to receive text messa... |
| 5824 | 0.0234 | Enter the IP range you want to exclude, and click ... |
| 5825 | 0.0234 | To edit a report template, click Customize. You ca... |
| 5826 | 0.0233 | Navigate to Tools 2. Click Select columns. The dia... |
| 5827 | 0.0232 | v10.7 Compatibility Notice Make sure to check your... |
| 5828 | 0.0231 | v10.7 Step 2 – On the Welcome page, click Next to ... |
| 5829 | 0.0230 | In this case, this user will have the most extende... |
| 5830 | 0.0230 | In this case, this user will have the most extende... |
| 5831 | 0.0230 | In this case, this user will have the most extende... |
| 5832 | 0.0230 | In this case, this user will have the most extende... |
| 5833 | 0.0230 | In this case, this user will have the most extende... |
| 5834 | 0.0230 | In this case, this user will have the most extende... |
| 5835 | 0.0228 | In this case, you need to provide your API secret ... |
| 5836 | 0.0225 | Each guide contains detailed instructions for depl... |
| 5837 | 0.0224 | Configure SMTP Server Settings SMTP server informa... |
| 5838 | 0.0220 | v10.7 Restore the Default View Follow the steps to... |
| 5839 | 0.0215 | • Provider name — Specify provider name. Property ... |
| 5840 | 0.0214 | TicketState To specify a new status, provide its I... |
| 5841 | 0.0210 | When prompted to c onfirm, click Yes. NOTE: For Mi... |
| 5842 | 0.0208 | Step 2 – Enter the description. From the expiratio... |
| 5843 | 0.0208 | Step 2 – Enter the description. From the expiratio... |
| 5844 | 0.0208 | Step 2 – Enter the description. From the expiratio... |
| 5845 | 0.0206 | However, not every tile supports all types of size... |
| 5846 | 0.0205 | Step 1 – Under Identity go to Applications > App r... |
| 5847 | 0.0201 | To further restrict your search, right-click the v... |
| 5848 | 0.0199 | Step 1 – Open PowerShell Step 2 – Run the followin... |
| 5849 | 0.0193 | Enter the address that will appear in the "From" f... |
| 5850 | 0.0193 | In this case, this user will have the most extende... |
| 5851 | 0.0193 | In this case, this user will have the most extende... |
| 5852 | 0.0193 | In this case, this user will have the most extende... |
| 5853 | 0.0193 | In this case, this user will have the most extende... |
| 5854 | 0.0193 | In this case, this user will have the most extende... |
| 5855 | 0.0193 | For more information, refer to the following micro... |
| 5856 | 0.0191 | To continue with this configuration, it will first... |
| 5857 | 0.0189 | Right-click the effective domain controllers polic... |
| 5858 | 0.0185 | v10.7 Step 3 – By default, the table displays only... |
| 5859 | 0.0185 | Execution policy for powershell scripts is set to ... |
| 5860 | 0.0184 | NOTE: Currently, Jakarta version has only experime... |
| 5861 | 0.0184 | NOTE: Currently, Jakarta version has only experime... |
| 5862 | 0.0172 | Execution policy for powershell scripts is set to ... |
| 5863 | 0.0169 | Step 4 – On the right, double-click the User Right... |
| 5864 | 0.0167 | Step 1 – Under App registrations, select the newly... |
| 5865 | 0.0164 | Open Local TCP Port 9003 Follow the steps to open ... |
| 5866 | 0.0159 | Step 6 – Click Add and enter the name of the user ... |
| 5867 | 0.0158 | Users Select the users to be excluded from search ... |
| 5868 | 0.0154 | If the authentication scheme is different from Ker... |
| 5869 | 0.0152 | Delete Console Users CAUTION: Confirmation is not ... |
| 5870 | 0.0149 | Step 7 – When done, click Finish. Define Parameter... |
| 5871 | 0.0149 | Step 2 – Click Search to apply your filters. By de... |
| 5872 | 0.0142 | Step 1 – On any domain controller in the target do... |
| 5873 | 0.0142 | It may contain letters (a-z, A-Z), numbers (0-9), ... |
| 5874 | 0.0141 | However, it may be changed because users can move ... |
| 5875 | 0.0140 | Right-click the effective domain controllers polic... |
| 5876 | 0.0135 | Step 1 – Install the Windows Management Framework ... |
| 5877 | 0.0133 | Step 1 – Under App registrations, select the newly... |
| 5878 | 0.0132 | In order to send a test email, click Test and sele... |
| 5879 | 0.0131 | Do the following depending on your infrastructure:... |
| 5880 | 0.0131 | Step 1 – On the Active Directory page, enter the n... |
| 5881 | 0.0127 | Disable accounts after Specify account inactivity ... |
| 5882 | 0.0124 | See the examples below for more information. v10.7... |
| 5883 | 0.0118 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5884 | 0.0116 | See the Role-Based Access and Delegation topic for... |
| 5885 | 0.0109 | Step 1 – Open the Group Policy Management console ... |
| 5886 | 0.0109 | Run the following command: Import-PfxCertificate -... |
| 5887 | 0.0103 | Step 2 – In the left pane, navigate to Forest: <fo... |
| 5888 | 0.0102 | The filter acts as a wildcard, filtering the table... |
| 5889 | 0.0101 | Step 5 – Locate the Log on as a batch job policy a... |
| 5890 | 0.0099 | Execution policy for powershell scripts is set to ... |
| 5891 | 0.0098 | Step 1 – Select the review and click Rename. The R... |
| 5892 | 0.0092 | Step 1 – In the Configuration interface on the Con... |
| 5893 | 0.0092 | Press Enter and repeat menu section. You will retu... |
| 5894 | 0.0091 | Step 1 – Install the Exchange Online PowerShell V3... |
| 5895 | 0.0089 | Client Certificate Use default values. Filter Sele... |
| 5896 | 0.0076 | Get the response - Response Code should be 200. In... |
| 5897 | 0.0072 | expire in <> days In order to send a test email, c... |
| 5898 | 0.0072 | v10.7 Step 2 – In the command prompt of Windows Po... |
| 5899 | 0.0072 | Step 3 – In the Group Policy Management Editor dia... |
| 5900 | 0.0072 | Step 3 – In the Group Policy Management Editor dia... |
| 5901 | 0.0069 | It cannot be locked out of any subsite, list, libr... |
| 5902 | 0.0063 | NOTE: For Microsoft 365 permissions, go to Request... |
| 5903 | 0.0060 | Policy Name State Enable Persistent Time Stamp "En... |
| 5904 | 0.0059 | gmail.com, hotmail.com, etc., may have to supply a... |
| 5905 | 0.0055 | Step 2 – Locate the General tab. Step 3 – Click th... |
| 5906 | 0.0054 | To specify a new status, provide its ID in the <Ti... |
| 5907 | 0.0051 | Specifies the password profile for the user. The p... |
| 5908 | 0.0049 | Step 2 – Edit the *.txt files, based on the follow... |
| 5909 | 0.0049 | Step 2 – Edit the *.txt files, based on the follow... |
| 5910 | 0.0049 | Step 2 – Edit the *.txt files, based on the follow... |
| 5911 | 0.0049 | Step 2 – Edit the *.txt files, based on the follow... |
| 5912 | 0.0042 | The Substitution Tokens will display without suppl... |
| 5913 | 0.0041 | In the pop-up window, select the Computer account ... |
| 5914 | 0.0036 | NOTE: For Microsoft 365 permissions, go to Request... |
| 5915 | 0.0036 | NOTE: If you use more than one region in your envi... |
| 5916 | 0.0034 | To configure your Cisco IOS devices, do the follow... |
| 5917 | 0.0033 | This option does not affect notifications sent to ... |
| 5918 | 0.0031 | Step 2 – Generate the self-signed certificate. Ste... |
| 5919 | 0.0030 | Step 2 – Select authentication method that will be... |
| 5920 | 0.0029 | To assign permission using the Group Policy Manage... |
| 5921 | 0.0026 | Choose Import Type Choose the import type that bes... |
| 5922 | 0.0024 | Once the first user with the role of Administrator... |
| 5923 | 0.0021 | Assign Permission using the Group Policy Managemen... |
| 5924 | 0.0019 | Step 2 – In the Tenant Information menu, locate th... |
| 5925 | 0.0009 | Follow the steps to configure Internet Options to ... |
| 5926 | 0.0009 | v10.7 If you are using a government tenant, please... |
| 5927 | 0.0008 | To do so, follow the steps below: 11.. Right-click... |
| 5928 | 0.0008 | Thus, there is no need to grant any permissions to... |
| 5929 | 0.0006 | These steps only apply for the SQL Authentication ... |
| 5930 | 0.0004 | Select this radio button if the configured Active ... |
| 5931 | 0.0002 | Password Enter a password for SMTP authentication.... |
| 5932 | 0.0002 | Step 6 – Click Install. Step 7 – When done, click ... |
| 5933 | -0.0013 | Step 2 – Select authentication method that will be... |
| 5934 | -0.0013 | Step 2 – Select authentication method that will be... |
| 5935 | -0.0017 | By default, resolved, closed, and canceled tickets... |
| 5936 | -0.0027 | In this case, the script uses the DNS name of your... |
| 5937 | -0.0030 | Step 1 – In the Exchange admin cente go to Groupsa... |
| 5938 | -0.0031 | Failure to do this could result in being locked-ou... |
| 5939 | -0.0036 | Select alert recipients. Click Add Recipient and s... |
| 5940 | -0.0036 | Recipients Select alert recipients. Click Add Reci... |
| 5941 | -0.0041 | Enter a value you want to search for. Alternativel... |
| 5942 | -0.0041 | Step 3 – Set the date and time for when the remind... |
| 5943 | -0.0043 | Wrong HTTP request was sent (any except POST). Err... |
| 5944 | -0.0045 | Step 3 – Locate the desired HTML message template.... |
| 5945 | -0.0045 | In this case, the script uses the DNS name of your... |
| 5946 | -0.0047 | Wildcards (*?) are supported and applied as follow... |
| 5947 | -0.0050 | Step 6 – Click Add and enter the name of the user ... |
| 5948 | -0.0050 | Step 7 – Run the following command to update group... |
| 5949 | -0.0051 | See the following Microsoft article for additional... |
| 5950 | -0.0057 | NOTE: If you use more than one region in your Regi... |
| 5951 | -0.0059 | Step 2 – Edit the *.txt files, based on the follow... |
| 5952 | -0.0061 | If you have multiple networks on your ESXi Server,... |
| 5953 | -0.0062 | Step 2 – Enter the SMTP Server Name in the textbox... |
| 5954 | -0.0062 | Modify filter If you need to modify the When filte... |
| 5955 | -0.0064 | Import Paste search — paste the search filters you... |
| 5956 | -0.0065 | Step 5 – Locate the Back up files and directories ... |
| 5957 | -0.0066 | Navigate to your cluster command prompt through th... |
| 5958 | -0.0069 | Internet Explorer security settings must be config... |
| 5959 | -0.0070 | Download the latest add-on version in the Add-on S... |
| 5960 | -0.0070 | Download the latest add-on version in the Add-on S... |
| 5961 | -0.0074 | Step 2 – In the Microsoft Entra ID admin center, c... |
| 5962 | -0.0074 | Follow the steps to install the certificate to the... |
| 5963 | -0.0075 | Step 1 – Go to Manage > Certificates & secrets and... |
| 5964 | -0.0075 | Step 1 – Go to Manage > Certificates & secrets and... |
| 5965 | -0.0079 | Default is 9898. For details on how to open the po... |
| 5966 | -0.0092 | Requires the owner(s) to have responded. CAUTION: ... |
| 5967 | -0.0098 | Open Remote TCP Port 9004 Follow the steps to open... |
| 5968 | -0.0098 | Pick a subscription and select On or Off in the Mo... |
| 5969 | -0.0107 | User name Enter a user name for the SMTP authentic... |
| 5970 | -0.0110 | JSON file must be formatted in accordance with JSO... |
| 5971 | -0.0122 | Assumes that the script runs on the RADIUS server.... |
| 5972 | -0.0122 | Before configuring the "From" field for user email... |
| 5973 | -0.0131 | The name may not consist entirely of digits and ma... |
| 5974 | -0.0131 | If the OS has Internet access, it is granted 180 d... |
| 5975 | -0.0139 | Secure Console Access Enable Secure Sockets Layer ... |
| 5976 | -0.0147 | Click Custom Level. Step 3 – In the Security Setti... |
| 5977 | -0.0156 | See the Grant Required Permissions topic for addit... |
| 5978 | -0.0158 | Step 8 – Click Install. Step 9 – When done, click ... |
| 5979 | -0.0158 | Requires the owner(s) to have responded. Mark Comp... |
| 5980 | -0.0161 | Press Enter to start. Step Description Specify a n... |
| 5981 | -0.0164 | Step 7 – Next, in the REST API access users sectio... |
| 5982 | -0.0165 | Step 2 – Under Groupsclick on the Mail-enabled sec... |
| 5983 | -0.0175 | The body is endpoint. The body is 405 Method Not A... |
| 5984 | -0.0187 | Step 10 – Close Group Policy Management console. v... |
| 5985 | -0.0192 | User name Enter a user name for the SMTP authentic... |
| 5986 | -0.0193 | Step 2 – Type or edit the note in the textbox. Ste... |
| 5987 | -0.0202 | Historically, the default for SMTP has been port 2... |
| 5988 | -0.0216 | Wildcards (* and ?) are supported. A backslash (\)... |
| 5989 | -0.0217 | See the following topics for additional Notificati... |
| 5990 | -0.0222 | Replace Number with a number (e.g., ?count=1500). ... |
| 5991 | -0.0244 | By default, 5 years after a validFrom date. For ex... |
| 5992 | -0.0247 | You can use HTML tags when editing a template. In ... |
| 5993 | -0.0252 | Replace Number with a number (e.g., &count=1500). ... |
| 5994 | -0.0258 | For details on how to open the port, refer to the ... |
| 5995 | -0.0265 | In this case, you will be prompted to set up IP se... |
| 5996 | -0.0265 | Each parameter is preceded with a dash; a space se... |
| 5997 | -0.0269 | Assign Permission Using the Group Policy Managemen... |
| 5998 | -0.0271 | Select this checkbox if your mail server requires ... |
| 5999 | -0.0274 | The request is unauthorized and the body is empty.... |
| 6000 | -0.0277 | RADIUSHost localhost Assumes that the script runs ... |
| 6001 | -0.0291 | If you want to specify several computers, you can ... |
| 6002 | -0.0292 | Step 3 – Click Add. Step 4 – The new secret will b... |
| 6003 | -0.0292 | Step 3 – Click Add. Step 4 – The new secret will b... |
| 6004 | -0.0299 | Each parameter is preceded with a dash; a space se... |
| 6005 | -0.0306 | Simply select the edges of the column headers and ... |
| 6006 | -0.0307 | Only tickets with this status can ClosedTicketStat... |
| 6007 | -0.0311 | You can use HTML tags when editing a template. In ... |
| 6008 | -0.0312 | Step 2 – On the General tab, specify a task name. ... |
| 6009 | -0.0331 | Step 4 – If you are using a PowerShell-based add-o... |
| 6010 | -0.0333 | Step 2 – Navigate to Start > Control Panel and sel... |
| 6011 | -0.0337 | Owners are encouraged to leave notes explaining wh... |
| 6012 | -0.0339 | Step 1 – Navigate to the Summary email recipient a... |
| 6013 | -0.0356 | Step 5 – Set a name and click Next. Step 6 – Set g... |
| 6014 | -0.0358 | You can skip or define parameters depending on you... |
| 6015 | -0.0358 | Owners are encouraged to leave notes explaining wh... |
| 6016 | -0.0358 | Perform the following steps to create a scheduled ... |
| 6017 | -0.0358 | Perform the following steps to create a scheduled ... |
| 6018 | -0.0359 | NOTE: Using a tool other than a text editor to edi... |
| 6019 | -0.0363 | If you need to modify it later, use this configura... |
| 6020 | -0.0371 | In this case, you will be prompted to set up IP se... |
| 6021 | -0.0372 | Step 4 – Open this XML file for edit and add the f... |
| 6022 | -0.0387 | Step 1 – On the computer where you want to execute... |
| 6023 | -0.0406 | Step 1 – On a target computer navigate to Start > ... |
| 6024 | -0.0407 | Step 5 – Apply settings and return to the <Share_N... |
| 6025 | -0.0409 | Client Certificate Use default values. Filter Sele... |
| 6026 | -0.0410 | Run the Add-On with PowerShell First, provide a pa... |
| 6027 | -0.0417 | Step 3 – Add the Microsoft 365 tenant item. Step 4... |
| 6028 | -0.0421 | Run the Add-On with PowerShell Follow the steps to... |
| 6029 | -0.0429 | Click Pending Changes on the right. In the Pending... |
| 6030 | -0.0430 | To create a scheduled task: Step 1 – On the comput... |
| 6031 | -0.0434 | Step 3 – Add the "Microsoft 365 tenant" item. Step... |
| 6032 | -0.0441 | v10.7 Click the filter icon for the column you wan... |
| 6033 | -0.0444 | Step 2 – Open settings.xml and configure the new a... |
| 6034 | -0.0450 | Create a KDS Root Key If the KDS root key does not... |
| 6035 | -0.0454 | Select Add User. Table 1: To... Do... 2. In the di... |
| 6036 | -0.0473 | Follow the steps to create Firewall rules manually... |
| 6037 | -0.0484 | See the procedure below on how to join the compute... |
| 6038 | -0.0488 | Follow the steps to run the script with PowerShell... |
| 6039 | -0.0498 | You can skip or define parameters depending on you... |
| 6040 | -0.0511 | Refer to the following Oracle help article for mor... |
| 6041 | -0.0512 | You can skip or define parameters depending on you... |
| 6042 | -0.0534 | Use Secure Sockets Layer encrypted connection (SSL... |
| 6043 | -0.0540 | Step 7 – Click Next. Step 8 – Click Create. Add Em... |
| 6044 | -0.0541 | Modify filter Double-click the filter and type a n... |
| 6045 | -0.0542 | See the procedure below on how to join the compute... |
| 6046 | -0.0543 | Step 3 – In the Security Settings - Local Intranet... |
| 6047 | -0.0551 | v10.7 Step 5 – Click on the Generate new API key b... |
| 6048 | -0.0553 | To run the script with PowerShell: v10.7 Step 1 – ... |
| 6049 | -0.0553 | Then re-enter your password. Click Finish. Step 3 ... |
| 6050 | -0.0553 | Run the Add-On with PowerShell First, provide a pa... |
| 6051 | -0.0560 | Most parameters are optional, the script uses the ... |
| 6052 | -0.0560 | The filter icon is highlighted orange for a column... |
| 6053 | -0.0563 | Step 8 – Close Group Policy Management console. St... |
| 6054 | -0.0566 | Choose Network Type Select a virtual switch. Summa... |
| 6055 | -0.0567 | Each parameter is preceded with a dash; a space se... |
| 6056 | -0.0570 | Step 2 – Click on your username in the top-right c... |
| 6057 | -0.0579 | Follow the steps to run add-on with PowerShell: St... |
| 6058 | -0.0579 | Follow the steps to run add-on with PowerShell: St... |
| 6059 | -0.0579 | Follow the steps to run add-on with PowerShell: St... |
| 6060 | -0.0608 | v10.7 Step 7 – Navigate to Start > Run and type cm... |
| 6061 | -0.0612 | Input the gpupdate /force command and press Enter.... |
| 6062 | -0.0612 | Input the gpupdate /force command and press Enter.... |
| 6063 | -0.0636 | Each parameter is preceded with a dash; a space se... |
| 6064 | -0.0637 | Step 11 – Navigate to Start > Run and type cmd. In... |
| 6065 | -0.0637 | Step 11 – Navigate to Start > Run and type cmd. In... |
| 6066 | -0.0637 | Review the following for additional information. O... |
| 6067 | -0.0644 | Step 4 – Right-click in the pane and select Add Ke... |
| 6068 | -0.0664 | Additionally, tiles with less information have sma... |
| 6069 | -0.0670 | Step 4 – On the Actions tab, click New and specify... |
| 6070 | -0.0670 | Step 4 – On the Actions tab, click New and specify... |
| 6071 | -0.0675 | Update In-Script Parameters Step 1 – Right-click a... |
| 6072 | -0.0676 | Each parameter is preceded with a dash; a space se... |
| 6073 | -0.0676 | Each parameter is preceded with a dash; a space se... |
| 6074 | -0.0690 | Step 4 – On the Actions tab, click New and specify... |
| 6075 | -0.0692 | Change password on next sign in with MFA passwordP... |
| 6076 | -0.0706 | Assign a new SSL certificate APIAdminTool.exe api ... |
| 6077 | -0.0716 | Step 5 – Double-click the newly created rule and o... |
| 6078 | -0.0717 | Step 2 – In the <Share_Name> Properties dialog, se... |
| 6079 | -0.0744 | Step 4 – Click New Rule. In the New Inbound Rule w... |
| 6080 | -0.0747 | APIAdminTool.exe api https certificate Run this co... |
| 6081 | -0.0753 | If necessary, modify the parameters as required. F... |
| 6082 | -0.0766 | Change password on next sign in passwordProfile Ye... |
| 6083 | -0.0771 | Step 4 – Right-click in the pane and select Add Ke... |
| 6084 | -0.0771 | Follow the steps to add or edit a note. Step 1 – S... |
| 6085 | -0.0773 | Step 4 – On the Actions tab, click New and specify... |
| 6086 | -0.0774 | After the application configuration, you can restr... |
| 6087 | -0.0788 | Step 5 – Click New Rule. In the New Inbound Rule w... |
| 6088 | -0.0798 | Port number Specify your SMTP server port number. ... |
| 6089 | -0.0813 | To do this, right-click a task and click Run. Run ... |
| 6090 | -0.0819 | If necessary, modify the parameters as required. F... |
| 6091 | -0.0822 | Add additional input languages Select N to proceed... |
| 6092 | -0.0831 | Click Yes. v10.7 Step 7 – On the Configure Web Ser... |
| 6093 | -0.0848 | Step 2 – Select Add tile. Either search for the ti... |
| 6094 | -0.0865 | Input the gpupdate /force command and press Enter.... |
| 6095 | -0.0867 | v10.7 Step 3 – Click close (x): Step 4 – Click App... |
| 6096 | -0.0917 | Step 5 – Double-click the newly created rule and o... |
| 6097 | -0.0928 | First, provide a path to your add-on followed by s... |
| 6098 | -0.0965 | You can skip some parameters— the script uses a de... |
| 6099 | -0.0965 | Step 4 – The Windows PowerShell opens and automati... |
| 6100 | -0.0983 | You can skip some parameters— the script uses a de... |
| 6101 | -0.1055 | The $port value must be accurate for your environm... |
| 6102 | -0.1081 | v10.7 To Enable JavaScript Follow the steps to ena... |
| 6103 | -0.1082 | Step 1 – Click Customize in the upper right corner... |
| 6104 | -0.1163 | IE might be disabled with GPO, but it should not b... |
| 6105 | -0.1201 | On the Action step, select the Allow the connectio... |
| 6106 | -0.1286 | Rest assured that your configurations and data wil... |
| 6107 | -0.1557 | Step 3 – Click Add and the selected tile appears o... |
| 6108 | -0.1657 | Remove a Tile from the Home Screen Follow the step... |

</details>

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

