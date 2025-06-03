# Article Processing Debug: ka04u000000HcTBAA0

**Generated:** 2025-06-03 12:41:05

## Article Content

```
Changing the name of your SQL Server causes database related errors
```

## Assessment Results

- **Update Level**: minor
- **Relevance Score**: 0.80
- **Model Used**: gpt-4o-mini-support

### Reasoning

The references provide relevant information about SQL Server connections and database naming conventions, which relate to the article's topic. However, there may be minor factual corrections needed regarding specific database names or connection details.

## Document Chunks Analysis

Total chunks analyzed: 6108

## Top Relevant Chunks Used

### Chunk 1 (Score: 0.5927)

```
The default name for the original database was NetwrixAIC. However, it could have been Customized. Use the same credentials for the SQL Server Connection. NOTE: The new destination folder will be ...\Netwrix\Access Reviews.
```

### Chunk 2 (Score: 0.5603)

```
There are no specific requirements for changing the path. v10.7 Step 5 – On the SQL Server Connection page, provide the required database information. Click Next to test the connection to the SQL Server. Server — Enter the database server hostname (NetBIOS name, FQDN, or IP address) with the instance name or non-standard port, if applicable, in one of the following formats: ◦◦ No named instance, use [SQLHostName], for example NT-SQL02 ◦◦ Named instance, use [SQLHostName]\[SQLInstanceName], for example NTSQL02\Netwrix ◦◦ No named instance with non-standard port, use [SQLHostName],[PortNumber], for example NT-SQL02,72 ◦◦ Named instance with non-standard port, use [SQLHostName]\ [SQLInstanceName],[PortNumber], for example NT-SQL02\Netwrix,72 Database — Enter the name of the database.
```

### Chunk 3 (Score: 0.5481)

```
Defines a SQL Server instance where your Audit SQLServerInstance Database resides. By default, local unnamed instance is selected. By default, the database responsible for Netwrix DBName Auditor look and feel is Netwrix_CommonDB. If you renamed this database, provide a new name.
```

### Chunk 4 (Score: 0.5112)

```
SQL Server database information: Server Name – Host name of the SQL Server serving the database in one of the following formats: ◦◦ No named instance: [SQLHostName] Example: NT-SQL02 ◦◦ Named instance: [SQLHostName]\[SQLInstanceName] v10.7 Example: NT-SQL02\Netwrix ◦◦ No named instance with non-standard port: [SQLHostName],[PortNumber] Example: NT-SQL02,1392 ◦◦ Named instance with non-standard port: [SQLHostName]\[SQLInstanceName], [PortNumber] Example: NT-SQL02\Netwrix,1392 Database – Name of the SQL database Database service account information: Use the windows account running this service — Local System, or computer account (NT AUTHORITY\SYSTEM) Use the following SQL account – Uses SQL Authentication to the database. Provide the properly provisioned SQL credentials for the database Remember, click Save when any changes are made to this page. Update the Database Service Account Password Follow the steps to update the Database service account password. These steps only apply for the SQL Authentication option.
```

### Chunk 5 (Score: 0.4684)

```
Table 1: Step Description Rename virtual machine Specify a new name for the virtual machine (e.g., NAServer). The computer name must be properly formatted. It may contain letters (a-z, A-Z), numbers (0-9), and hyphens (-), but no spaces and periods (.). The name may not consist entirely of digits and may not be longer than 15 characters.
```

