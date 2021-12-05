*******************************************
*******************************************
***   ServiceNow Rome CSA Notes 2021	***
*******************************************
*** 	      By Omar MOUMEN	   		***
*******************************************
***       Last Update	21/11/2021      ***
*******************************************
*******************************************

*******************************************
*******************************************
***  User Interface & Navigation		***
*** 	• ServiceNow Overview			***
*** 	• Lists and Filters			20%	***
*** 	• Forms and Templates			***
*** 	• Branding						***
*******************************************
*******************************************

***********************************
***		Platform Overview		***
***********************************
- Now Platform is an Application Platform-as-a-Service (aPaaS)
- The applications delivered by ServiceNow are divided into four different workflows:
	IT Workflows, Employee Workflows, Customer Workflows, and Creator Workflows
- Now Platform use a single system of record and a common data model
- The Now Platform is a multi-instance (NOT a multi-tenant) architecture. Instance = Unique software stack
- ServiceNow provides four weekly full backups of your data, with six days of daily differential backups
- Now Support (HI - Hosted Instance) is the ServiceNow after-sales service and support control center
- The three Now Platform interfaces: Now Platform user interface, ServiceNow Mobile apps, and Service Portal
- ServiceNow Mobile apps: ServiceNow Agent, Now Mobile, and ServiceNow Onboarding
- Top 10 reasons to use ServiceNow Mobile apps:
	• Persona-focused for intuitive use
	• Mobile first and completely native, using the device's built-in features
	• Codeless and rapid development of new applets
	• Ability to submit, view, and update requests, issues, and tasks
	• Global search to find people, service and items, and articles
	• Offline access with Mobile Agent to enable fulfillers to complete work while not connected
	• Push notifications for access to important information instantly
	• Access to Virtual Agent, chat, and knowledge articles
	• Role-based access to customized information
	• Manageable from an MDM (mobile device management) or an MAM (mobile application management)
- A role is a collection of permissions
- Self-service users: Users without any assigned role permissions
- A group CAN contain other groups
- By default, only users with the itil role can have tasks assigned to them
- For ease of maintenance, avoid assigning roles directly to individual users
- Authentication: Local database, External Single Sign-on (SSO), LDAP, OAuth 2.0, Digest Token, and Multi-factor
- The local database authenticates the user name and password stored in their corresponding user record in the 
  ServiceNow instance
- External Single Sign-on (SSO) authenticates the user name and password configured in identity providers with 
  a matching user account in the ServiceNow instance
- Digest Token authenticates an encrypted digest of the username and password stored in the user record
- Multi-factor authenticates the user name and password in the ServiceNow instance and sends a passcode to the 
  user's mobile device where an authenticator supporting Time-based One-time Password (TOTP) is installed, such 
  as Google Authenticator
- OpenID Connect (OIDC) is an identity layer built on top of the OAuth protocol, which provides a modern and 
  intuitive Single Sign-on (SSO) experience. OIDC also improves the login experience for mobile applications 
  by enabling users to log in to ServiceNow applications using their third-party social identity provider

***********************************
***	  User Interface Overview	***
***********************************
- Elevated role lasts until session timeout or logout, or until the role is unassigned
- Impersonate User is available to all users with the admin or impersonator role
- Global search: Boolean operators must be in all caps
- System settings for logged-in user: individual users personalize the user interface for themselves
- Lists Tab: Wrap longer text in list columns
- Forms Tab: Tabbed forms - Form sections and related lists appear or not in tabs
- Global user interface configurations: System Properties - Basic Configuration UI16 (Banner logo and text)
- Applications - [Sections] - Modules
- Modules that run scripts or turn on debugging CAN not display its information in the content frame
- Filtering by word displays all modules containing the word with their section labels and applications
  it also displays all applications containing the word with their section labels and modules
- Navigation filter: sys_user.list (Users List) sys_user.form (User new record form) (Tables & Forms by name)
- Some content types -such as UI pages and other non-standard interfaces- aren’t tracked in the history
- By default, 30 history entries. Use glide.ui.nav.history_length in sys_properties table to modify it.

***********************
***     Branding    ***
***********************
- Platform Branding: Guided Setup --> ITSM Guided Setup
- Company logo, Personalized banner text, Default date and time format, Desired corporate color scheme
- ITSM Guided Setup categories: Company, Connectivity, Foundation Data, CMDB, ...Go Live
- Company category: System Configuration and Welcome Page
- Colors can be changed by color slider, a color name, a hex color code, or a RGB color code
- category's tasks can be assigned individually to admin users or all tasks to a single admin
- You can also set your branding configurations using System Properties --> Basic Configuration UI16
- CSM Configurable Workspace can be easy configured and extended using Now Experience UI Builder
- UI Builder enables you to preview the final interface of the workspace you're building
- UI Builder is not yet capable of building or configuration out-of-the-box Service portals, like 
  Employee Service Center. Continue to use the Service Portal Designer instead
- Now Experience Framework --> UI Builder

*****************************
***	  Lists and Filters   ***
*****************************
- List controls: View, Saved Filters, Group By, Show (Records per page), Refresh List and Create Favorite
- Personalize a list VIEW (Gear/Cog icon): Personalize the view of a list without affecting other users
- After personalizing a list, the Gear/Cog icon changed (a dot is added to the icon)
- It’s best not to change the first column in a list (Ex. Number)
- By default, a list is sorted by order field, else number field, else name field, else table's display field
- You can also sort options through the list column context menu
- Filter Out: A quick way to filter a list by right-clicking a value to exclude it (Not equal this value)
- Show Matching: Right-clicking a value to display only matching records with it (Equal this value)
- Breadcrumbs: a quick form of filter navigation ordered from left to right. It summarize filter conditions
- The condition builder allows you to filter on any table's field, not just those displayed in the list
- The system automatically applies a default wildcard if not present with the search term (% for Number)
- If the table was defined with a text index, we can run a keyword search across all its fields
  even those not visible in the list
- This text search supports uppercase Boolean operators and quotation marks
- The ServiceNow Zing text indexing and search engine is the default search engine used to search record data
- Searches are not case sensitive. Use advanced options for more specific queries
- Context menus provide list controls for the List, Columns and Fields:
- List title menu, list column context menu for each column, list fields context menu for each value in the list
- Show Visual Task Board allows you to create a new visual task board based on the filtred list of records
- This option is only available on lists of task records, such as incident, problem, or My Work
- The Group by option groups records by the column. Ungroup removes the groupings
- The Bar Chart and Pie Chart options allow you to view the list of records in a bar or pie chart, 
  also automatically grouped by values in the column
- Configure provides advanced (Multi-Views) list configuration options as List Layout FOR ALL Users
- Import allows you to insert new records or update existing records, using data from a Microsoft Excel file
- The List Editor allows to edit field values in a list without opening the form (except some field types) 
- Update Selected allows you to update one or more fields on multiple records at a time
- Right-click a field: Assign to me, Approve, Reject, Assign tag
- The Natural Language Query (NLQ) allows you to filter the list data using natural language, 
  instead of the condition builder
- You can edit tags you have created using the My Tags or My Tagged Documents modules

**********************************
***	   Forms and Templates	   ***
**********************************
- A shaded field means we can’t change the value. For example, Number is assigned by the system
  And Priority is calculated from the Impact and Urgency values
- Additional comments and Work notes are both Journal fields, record notes viewable by different users
- Comments are visible by all users whereas Work notes are viewable only by users with the itil role
- After the record is saved, a new option, Copy "Record", appears on the form context menu
- Some records - as surveys and catalog items - allow you to copy records through Insert and Insert and Stay
- Insert copies the record and redisplays the list. Insert and Stay copies the record and keeps it open
- Related lists don’t appear until the form has been submitted and the new record created
- Form Header: Manage Attachments, Show Activity Stream, Personalize Form, More Options icons
- Personalizing forms by clicking on the icon in the form's "Title Bar"
- Forms configured with the activity formatter display a stream of activities associated with the record
- A formatter is a form element used to display information that is not a field in the record.
  For example, the activity stream and Related Search Results (RSR) are formatters
- RSR displays contextual search results based on text entered in the Short Description field
- Following a record adds the logged-in user to the activity stream conversation in Connect and sends 
  notification of any new comments or work notes
- Form templates simplify the process of submitting new records by populating some form fields automatically
- We access form templates through the More Options icon on the form header: toggle on/off
- You can create and configure unique views for each form in the system
- Slushbucket: a list collector interface allows to Add/Remove multiple items to/from Available/Selected lists

