# Article Types

Our knowledge base (KB) consists of two primary article types designed to help customers find solutions effectively.

## How-To Articles

How-to articles provide step-by-step guidance for accomplishing specific tasks. These come in two formats:

### Question and Answer Format

* **Title Structure:** How to \[Accomplish Specific Task\]
* **Example: **[“How to Optimize SEEK System Scans with System Resources”](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk000000227NKAQ.html)
* **Sections:** Question, Answer
* **Best for:** Simple procedures with straightforward answers

### Instructions Format

* **Title Structure:** How to \[Accomplish Specific Task\]
* **Example: **[“How to Re-enable the Built-in AIC Admin Account via SQL Server”](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA04u0000000Is4CAE.html)
* **Sections:** Overview, Instructions
* **Best for:** Complex procedures requiring context and detailed steps

## Resolution Articles

Error articles help customers troubleshoot specific errors or issues they encounter.

### Error Resolution Format

* **Title Structure:** Error: \[Unique Error Code/Message\]
* **Example: **[“Error: Ini Section Does Not Exist in SBTFileMon.ini”](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk0000001M05KAE.html)
* **Sections:** Symptom, Cause, Resolution
* **Best for:** Documenting specific error messages and their solutions

### Symptom Resolution Format

* **Title Structure:** \[Feature or Component\] \[Symptom or Issue\] \[Optional: Condition or Context\]
* **Example: **[Access Information Center Not Reporting Attribute Changes](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk0000001oQzKAI.html)
* **Sections:** Symptom, Cause, Resolution
* **Best for:** Documenting unexpected behavior or absence of expected results and their solutions

# Article Structure

## Section Organization

Articles should be structured with clear headings to help readers quickly find information. Each article type follows a specific organization pattern but should not exceed five main headings.

## Article Types and Their Required Sections

### How-to Articles

* **Overview** and **Description**: Briefly explain what the article will help the reader accomplish, followed by the main body of the article.
* **Question** and **Answer**: Present the core question and then the complete answer.

### Error and Symptom Resolution Articles

* **Symptom** (or **Symptoms** if multiple): Describe the error indicators or problems the user might encounter.
* **Cause** (or **Causes** if multiple): Explain what typically causes this error or issue.
* **Resolution** (or **Resolutions** if multiple): Provide step-by-step instructions to resolve the problem.

## Common Sections for All Article Types

### Related Query (or Queries)

* Position this as the first section when applicable
* Include quotations from related customer support ticket subjects and descriptions
* Use the exact wording from tickets (correcting only typos)
* This helps with searchability and ensures we're addressing real customer language

 ![](/api/attachments.redirect?id=b939c644-5558-4738-b2e3-26d66ba6f8ed " =599x269")

### Related Links

* List all relevant links contained within the article
* This provides readers with additional resources on the topic
* Helps create a connected knowledge ecosystem

 ![](/api/attachments.redirect?id=93aa0bb9-f9fe-4b3b-9040-22cf7dcb32a0 " =380x131")

# Article Titles

The title of a KB article is critical, as it’s often the first thing a customer or support engineer sees when searching. A clear, precise title ensures that users find information quickly.

## Title Guidelines

* **Avoid product names in titles.** Product names are in the metadata, so adding them to titles makes titles unnecessarily long and redundant.
* **Use keywords customers will search for.** Focus especially on any words used by the customer in a ticket subject or description.
* **Include unique identifiers like error codes.** Customers often include specific codes in their queries, so this helps
* **Use title case.** If you’re not sure how, use <https://capitalizemytitle.com/> and choose Chicago style.
* **Avoid vagueness and ambiguity.** The clearer the title, the more findable it is.

## Article Title Rules

| **Article Type**  | **Corresponding Ticket Type\*** | **Content Type Data Category** | **Format** | **Description**  | **Bad Example**s | **Good Example**s |
|----|----|----|----|----|----|----|
| **Error Resolution**  | Error | Troubleshooting | Error: \[Unique Error Code/Message\] | Focused on a specific error. The title should include the most unique part of the error message. If the error message contains the word “error”, don’t start the title with “Error:” | Error: Can’t Process Request **(too generic, not findable)** Event collection failed: Event log read failure. Error details: Data error (cyclic redundancy check). Error number: 0x80004005 **(too detailed)** | Error: Event Collection Failed 0x80004005 **(most unique part of message)**  An Unknown Error Occurred While Processing the Request on the Server **(didn’t start with “Error:” because “error” in the message)** |
| **Symptom Resolution** | Unexpected Behavior, Performance | Troubleshooting | \[Feature or Component\] \[Symptom or Issue\] \[Optional: Condition or Context\] | Focused on resolving behavioral or performance issues that do not produce explicit errors. The title should clearly summarize the symptom or issue the user experiences. Avoid vague or overly broad titles. | AD not working right **(too vague)**  Reports slow and sometimes fail when running a report in the web interface **(too wordy)** | Active Directory Users Missing from Search Results **(clear)**  Reports Time Out in Web Interface **(concise, specific)** |
| **How To** | Question | How To | \[Action Gerund\] \[Specific Task\] | Focused on answering a specific question, accomplishing a specific goal, or using a specific feature.  | How to Modify SSRS Report Timeouts? **(starts with “how to”, ends in a question mark)** Auditing a non-trusted domain **(sentence case)** | Modifying SSRS Report Timeouts **(starts with gerund, no punctuation)** Auditing a Non-trusted Domain **(title case)** |

\*Ticket types generally align with these types of articles, but there may be exceptions.

# Content Standard 

All KB articles should adhere to the following standards. 

| **Standard**  | **Definition**  |
|----|----|
| **Clarity**  | Another customer with the same problem could understand and solve their own issue.  |
| **Accuracy**  | The issue was reproduced, and the resolution was confirmed.  |
| **Structure**  | Structure is applied (e.g., symptom/cause/resolution or question/answer).  |
| **Uniqueness**  | No duplicate articles exist; the article is linked to other content instead of duplicating it.  |
| **Title**  | Title follows the style guide (*Error* or *How to*).  |
| Backlinks | All URL links open new tabs, point to up-to-date content, and are not broken. |
| **Metadata**  | All fields are correctly completed, particularly **Draft Status**, **Visibility**, **Netwrix Product**, **Formerly a Product of**, **Change Log**, **Confidence Level**.  |

# Voice and Tone Guidelines

Our KB articles should maintain a consistent voice and tone.

## General Voice Principles

* Use second person ("you") when addressing the reader.
* Write in active voice rather than passive voice.
* Be direct, clear, and concise.
* Avoid jargon and overly technical language unless necessary.
* Maintain a professional but approachable tone.

## Words and Phrases to Avoid

* Colloquialisms and idioms (e.g., instead of “hang,” use “stop loading”)
* Vague terms like "simply," "just," "easy," or "obviously"
* Unnecessarily complex terminology when simpler terms will do
* Humor (rarely translates well across cultures)
* Business jargon ("leverage," "synergy," "utilize" instead of "use")

# Article Length

Effective KB articles should be comprehensive yet concise. Follow these guidelines for optimal length.

## General Length Principles

* Focus on one topic per article
* Place the most important information at the beginning
* Break content into logical, digestible sections

## Content Chunking

* Keep paragraphs to 3-4 sentences maximum
* Use bullet points and numbered lists for better readability
* One idea per paragraph
* Use meaningful subheadings every 200-300 words

# Markup Conventions

Use markdown conventions in all KB articles:

* `##`, `###`, and `####` for level 2, 3, and 4 section headers (the article title is always level 1)
* Paragraphs are created by leaving a blank line between lines of text
* `[Link text](URL)` for links
* `![alt text](image_url)` for images and screenshots
* `1.`, `-`, and `*` for ordered and unordered lists
* Use fenced code blocks (triple backticks) for block-level code or scripts. For language-specific highlighting, specify the language after the backticks.
* Use single backticks `` ` `` for inline code (e.g., a PowerShell command like `cd ./myfilepath/myfilename`).
* For tables, use markdown table formatting with pipes `|`.
* For notes and warnings, use custom callout formatting using blockquotes starting with a chevron `>`:

  > **IMPORTANT:** ...
  >
  > **NOTE:** ... 
* **Bold** (`**...**`) for UI elements, actions, buttons, menu items, tabs, checkboxes, dropdown options, navigation steps, and form fields.
  * Buttons, menu items, tabs, checkboxes, dropdown options, and other interactive elements (e.g., “Click **Submit** to complete the process.”) 


  * Fields, form labels, and field names in databases or applications (e.g., “Enter your email address in the **Email** field.”) 


  * Use bold for user-initiated actions such as clicking, selecting, or pressing keys (e.g., “Select **File** > **Save As** to save the document.”) 


  * Tab names, page sections, and navigation steps (e.g., “Navigate to the **Settings** tab and select **Security**.”) 
  * Exception: Use single backticks `` ` `` for command-line inputs (e.g., “Type `git status` and press **Enter**.”) 

# Optimizing for Retrieval-Augmented Generation (RAG) AI

As AI systems increasingly access our KB to answer user queries, we must optimize our content for these systems.

## Keyword and Concept Clarity

* Define technical terms and concepts clearly the first time they appear
* Use consistent terminology throughout (avoid synonyms for technical terms)
* Include common phrasings of questions or problems in Q&A articles

## Chunking for AI Retrieval

* Create logical, self-contained sections that can stand alone if retrieved
* Keep related information together within the same section
* Use descriptive subheadings that convey the main point of each section

## Example Queries and Answers

* Include example queries that users might ask about the topic
* Provide direct answers to these questions within the content
* Format critical information (commands, settings, parameters) in a consistent, easily extractable way

## Avoid AI Confusion Patterns

* Use consistent headings (`##`, `###`, and `####` ) without skipping levels or using other headings.
* Don't split critical procedures across multiple sections.
* Avoid ambiguous pronoun references ("it," "this," "that").
* Clearly distinguish between similar features or concepts.
* Provide explicit transitions between related topics.

# Accessibility Considerations

All KB articles must be accessible to users with disabilities and comply with WCAG 2.1 AA standards.

### Text Accessibility

* Maintain a logical heading structure (don't skip heading levels).
* Use descriptive link text (avoid "click here" or "read more").
* The Knowledge Center maintains black text on a white background with no text colors or highlights. This is to avoid using color to denote meaning, which is less accessible to colorblind readers.

### Image Accessibility

* Include alternative text for all images:
  * Alt text formula: \[Action being shown\] + \[Key UI elements visible\]
  * Example: "Dialog box for selecting monitoring plan settings with the Schedule tab active"
* For decorative images, use empty alt text (alt="").
* Limit the use of images that contain text.

# Formatting and Naming

## Product Long and Short Names

Use the following long and short product names in KB articles. Do NOT use product abbreviations, such as NA for Netwrix Auditor.

| Full Product Name  | Short Product Name   | Old Product Names | API Key |
|----|----|----|----|
| Netwrix Activity Monitor  | Activity Monitor | Stealthbits Activity Monitor (SAM) | activity_monitor |
| Netwrix 1Secure  | 1Secure  | N/A | onesecure |
| Netwrix Auditor  | Auditor  | N/A | auditor |
| Netwrix Change Tracker  | Change Tracker  | N/A | change_tracker |
| Netwrix Data Classification  | Data Classification  | N/A | data_classification |
| Netwrix Directory Manager | Directory Manager  | Imanami GroupID | groupid |
| Netwrix Log Tracker  | Log Tracker  | N/A | log_tracker |
| Netwrix Password Policy Enforcer  | Password Policy Enforcer  | Anixis Password Policy Enforcer | password_policy_enforcer |
| Netwrix Password Reset  | Password Reset  | Anixis Password Reset Manager | password_reset_manager |
| Netwrix Password Secure  | Password Secure  | Mateso Password Secure | password_secure |
| Netwrix Endpoint Policy Manager | Endpoint Policy Manager | PolicyPak | policypak |
| Netwrix Endpoint Privilege Manager | Endpoint Privilege Manager | Privilege Secure for Endpoints | privilege_secure_endpoints |
| Netwrix Privilege Secure for Access Management  | Privilege Secure for Access Management  | N/A | privilege_secure |
| Netwrix Privilege Secure for Discovery  | Privilege Secure for Discovery  | Remediant SecureONE | privilege_secure_discovery |
| Netwrix Recovery for Active Directory  | Recovery for Active Directory  | StealthRECOVER | recovery_ad |
| Netwrix Access Analyzer  | Access Analyzer | Netwrix Enterprise Auditor (NEA), StealthAUDIT (SA) | enterprise_auditor |
| Netwrix Threat Manager  | Threat Manager  | StealthDEFEND | threat_manager |
| Netwrix Threat Prevention  | Threat Prevention  | StealthINTERCEPT | threat_prevention |
| Netwrix Platform Governance for NetSuite  | Platform Governance for NetSuite  | Strongpoint for Netsuite | strongpoint_netsuite |
| Netwrix Platform Governance for Salesforce  | Platform Governance for Salesforce  | Strongpoint for Salesforce | strongpoint_salesforce |
| Netwrix Identity Manager  | Identity Manager   | Usercube | usercube |
| Netwrix Vulnerability Tracker by Greenbone  | Vulnerability Tracker | N/A | vulnerability_tracker_gb |

## When to Use Long and Short Names

Use a full product name, such as “Netwrix Auditor”,

* Every time you introduce a product for the first time


* When mentioning service names (e.g., “Netwrix Auditor for File Servers Service”)


* With log names (e.g., “Netwrix Auditor Health Log”)

Use a short product name, such as “Auditor”, 

* Every time after the first mention of the product


* With the words “server” and “client”

Don't use a product name for product components if the product name has already been introduced. For example,  

* Audit Database 


* Long-Term Archive  


* Monitoring plans 


* Add-On names 


* Target systems 

## Headings and Subheadings

* Write in title case (use <https://capitalizemytitle.com/>).
  * Prepositions are capitalized only in case they exceed 4 letters.
  * Prepositions that are part of a phrasal verb (e.g., “Set Up”) should be capitalized.
  * Avoid punctuation marks.
* Avoid passive voice.
* Maine article section headings start with `##`.
* Sub-section headings start with `###` and `####`.

## Punctuation

The KB maintains consistent punctuation standards to ensure clarity and professionalism across all articles. Follow these guidelines:

### General Punctuation Rules

* Follow Chicago Manual of Style (CMOS) for all punctuation conventions.
* Use serial commas (the comma before "and" or "or" in a series of three or more items).
* Write out contractions in full (use "do not" instead of "don't", "cannot" instead of "can't").
* Avoid exclamation marks, even for warnings or important notes.

### Punctuation Guidelines

* **Colons:** Use only at the end of complete sentences to introduce lists or explanations (e.g., “Refer to the following steps:”). Capitalize the first word after a colon only if it begins a complete sentence.
* **Semicolons:** Use to separate closely related independent clauses or to separate items in a complex list where the items themselves contain commas.
* **Hyphens and Dashes:**
  * Use hyphens (-) for compound modifiers before nouns (e.g., "well-known feature").
  * Use en dashes (–) for ranges (e.g., "pages 10–15").
  * Use em dashes (—) for abrupt changes in thought or emphasis. Do not add spaces around em dashes.
* **Parentheses:** Use sparingly for supplementary information that would interrupt the flow of the main text.
* **Bullets and Numbering:** End each list item with appropriate punctuation (typically periods if the items are complete sentences).

## Code Blocks

Code blocks can be used to depict following items: 

* Error codes and messages

* Commands to be used

* URLs and paths (however, if a URL or a path needs to be on the same line as another part of the sentence, use single backticks)

Code blocks are recommended for when the contents are to be copied: 

```markup
```plaintext
This is a code block. 
Note that actual Enter\Return line breaks work here as intended. 
  Line indents like this will also be reflected.
This will allow an end user to easily copy the content from the Help Center.
```
```

## In-line Code

Recommended for use in case the contents are not to be copied. Example:

```markup
`This is a normal non-copyable code block.`
```

## Screenshots

Screenshots are a welcome addition to an article to clarify exactly where in a user interface to locate a specific feature, button, field, etc. Screenshots should follow these guidelines:


1. **Only red rectangles.** Arrows, circles, highlights, and other types of image markup introduce inconsistency to the KB.
2. **No more than 2 shapes per screenshot.** If more steps need to be indicated, consider using the same screenshot more than once but with different shapes.
3. **Add alt text to all images.** To make images more accessible, make sure they are clearly described in the al text.
4. **Clearly write all the steps a user should take in the article body.** The article should be clear enough to follow without screenshots. 

## Ordered and Unordered Lists

### List Rules


1. Capitalize the first word of each item on every list, unless not needed by design (e.g., “gMSA”). 
2. Adopt consistent punctuation. For example, all list items should end in a period or none should.

   
   1. If a list of items contains incomplete sentences, omit full stops for all items. (E.g., a list of operating systems, UI elements, etc.) 
3. Consider the use of either type of the list:

   
   1. Use default bulleted (unordered) lists for unordered sequences of recommendations or tools. 
   2. Use numbered (ordered) lists for specifically ordered sequences of events. 
4. Keep the number of lower-level lists (second-level lists and further) low. They are rarely needed — it is better to start a separate paragraph to explain an idea. 
5. Images work poorly in lists due to the platform formatting constraints. In some cases, it is better to omit images or provide them after the list has ended. 

# Referencing and Hyperlinks

## Links to Internal Content

When referring to Netwrix documentation articles, follow these recommendations:

* Avoid the “Read here” pattern. Be more descriptive of where a reader can expect the link to take them.
* When referring to a subsection, orient the reader by adding a subsection name and a parent section name.
* Insert links to a document article related to the latest product version.
* Add a version to a referencing article’s name.

## Links to External Content

When referring to third-party company articles, make sure that the referenced article name adheres to the following structure:

* An article’s name and a third-party company name are separated by a middot (`⸱`), with spaces before and after the middot.
* There is a space and then a wide-headed northeast light barb arrow (`🡥`) after the company name.

Example:

```markup
Learn more in Learn more in [SMB Security Enhancements ⸱ Microsoft 🡥](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security)
```