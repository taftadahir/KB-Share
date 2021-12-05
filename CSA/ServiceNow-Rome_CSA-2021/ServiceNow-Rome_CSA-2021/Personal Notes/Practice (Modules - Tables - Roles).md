*******************************************
*******************************************
***   ServiceNow Rome CSA Notes 2021	***
*******************************************
*** 	      By Omar MOUMEN	   		***
*******************************************
***       Last Update	21/11/2021      ***
*******************************************
*******************************************

***************************************
***************************************
***  	  	• DOMAINES  	    	***
*** 	  	• MODULES				***
*** 	  	• TABLES				***
*** 	  	• ROLES			    	***
***************************************
***************************************

***************************
***	   ADDING POINTS    ***
***************************

- Business logic of a table: task.list > Open a record > Configure - All

********************
***	   TABLES    ***
********************

Applications Navigator: <table name>.list OR <table name>_list.do
						<table name>.form (New record form)

- Application Menu 			[sys_app_application] 		--> System Definition > Application Menus
- Welcome Page Section 		[sys_home]
- Template					[sys_template]				--> System Definition > Templates

- User 						[sys_user]					--> User Administration > Users
	User Administration (user_admin Role)					System Security > Users and Groups > Users
- Group						[sys_user_group]			--> User Administration > Groups
	System Security (admin Role)							System Security > Users and Groups > Groups
- Role						[sys_user_role]				--> User Administration > Roles
															System Security > Users and Groups > Roles
- Task						[task]
- Rule						[sysrule]					--> System Policy > Rules > Assignment
- Assignment Data Lookup	[dl_u_assignment]			--> System Policy > Rules > Assignment Lookup Rules
- Inbound Email Actions		[sysevent_in_email_action]	--> System Policy > Email > Inbound Actions
- Notification				[sysevent_email_action]		--> System Notification > Email > Notifications

- Dictionary Entry			[sys_dictionary]			--> System Definition > Dictionary
- Tables 					[sys_db_object]				--> System Definition > Tables
- Field Label				[sys_documentation]			--> System Definition > Language File
- Number					[sys_number]				--> System Definition > Number Maintenance
- Access Control			[sys_security_acl]			--> System Security > Access Control (ACL)
- Data Source				[sys_data_source]			--> System Import Sets > Administration > Data Sources
- Import Set				[sys_import_set]			--> System Import Sets > Advanced > Import Sets
- Table Transform Map		[sys_transform_map]			--> System Import Sets > Administration > Transform Maps
- Base Configuration Item 	[cmdb]
- Configuration Item 		[cmdb_ci]
- CI Relationship			[cmdb_rel_ci]
- Suggested Relationship	[cmdb_rel_type_suggest]		--> Configuration>Relationships>Suggested Relationships

- Knowledge 				[kb_knowledge] 				--> Knowledge > Articles > All
- Knowledge Base 			[kb_knowledge_base] 		--> Knowledge > Administration > Knowledge Bases
- Catalog Item				[sc_cat_item]				--> Service Catalog > Catalog Definitions > Maintain Items
- Record Producer			[sc_cat_item_producer]		--> Service Catalog > Catalog Definitions > Record Producers
- Request					[sc_request]				--> Service Catalog > Requests
- Requested Item			[sc_req_item]				--> Service Catalog > Items
- Catalog Task				[sc_task]					--> Service Catalog > Tasks

- Client Script				[sys_script_client]			--> System Definition > UI Actions
- UI Policy					[sys_ui_policy]				--> System UI > UI Policies
- UI Action					[sys_ui_action]				--> System Definition > UI Actions
- Business Rule				[sys_script]				--> System Definition > Business Rules
- Script Include			[sys_script_include]		--> System Definition > Script Includes
- Customer Update			[sys_update_xml]
- Update Set 				[sys_update_set]			--> System Update Sets > Local Update Sets
- Retrieved Update Set		[sys_remote_update_set]		--> System Update Sets > Retrieved Update Sets
- Event						[sysevent]					--> System Policy > Events > Event Log

- Server [cmdb_ci_server] --> Computer [cmdb_ci_computer] --> Hardware [cmdb_ci_hardware] --> [cmdb_ci]
- System Property			[sys_properties]

*******************
***	   ROLES    ***
*******************

- Impersonate User: impersonator
- Create Report: report_user, itil
- Schema Map: personalize_dictionary
- cmdb_ci: itil, asset
- List Layout, Schema map, Tables & Columns: admin
- Import Set (All): import_admin
  Load Data, Transform: import_admin, import_set_loader, import_transformer
- Service Gatalog with Scripting: admin
  Service Gatalog without Scripting: catalog_admin
  Assigned Catalogs Edit/Update, assigning Managers/Editors: catalog_manager
  Assigned Catalogs Edit/Update, assigning Editors: catalog_editor
- Flow Designer: flow_designer, flow_operator, and action_designer
- UI Policies: ui_policy_admin
- Studio: admin or a delegated developer


***************************
***	   Tests Buttons    ***
***************************

- Report: Run
- Notification: "Preview Notification" (Advanced view)
- Catalog Item (Maintain Items): "Try It"
- Flow Designer (Flow): "Test"
- Update Sets: Submit and Make Current
			   Preview Update Set (Run Preview Again)
			   Commit Update Set

*****************************************
***	   User Interface & Navigation    ***
*****************************************

- Guided Setup > ITSM Guided Setup
  ITSM Guided Setup categories: Company, Connectivity, Foundation Data, CMDB, ...Go Live
  Company category: System Configuration and Welcome Page
  Company logo, Personalized banner text, Default date and time format, Desired corporate color scheme
  Colors can be changed by color slider, a color name, a hex color code, or a RGB color code
  category's tasks can be assigned individually to admin users or all tasks to a single admin
  "Assign" Link in top right of the Compagny category
  System Properties --> Basic Configuration UI16
  
  Welcome Page Section [sys_home]: About ${gs.getProperty('glide.product.name', 'ServiceNow')}
  
- System Settings > Developer - Show application picker in header on/off

- Update Application Menu in Application Navigator: Modify Name, Deactivate/Activate, ...
  Click on the pencil icon next to the Application name
  System Definitions > Application Menus

- Breadcrumbs: a quick form of filter navigation ordered from left to right. It summarize filter conditions
  Remove next condition (>) icon
  The condition builder allows you to filter on any table's field, not just those displayed in the list
- Filter save: Name - Visible to (Me, Everyone, group) - "Save" button
  Filter on field in list: RightClick a field in list - Show Matching/Filter Out

- List context menu (List controls):
  View.., Filters.., Group by.., Show..(records par page), Refresh List, Create Favorite
- Column context menu: 
  Sort, Show Visual Task Board, Group by/Ungroup, Bar Chart/Pie Chart, Configure: List Layout, Import/Export,
  Update Selected, ...
- Fields context menu:
  Show Matching/Filter Out, Copy URL to Clipboard/Copy sys_id, Assign Tag, Assign to me, ...
- Self-Service > My Tags
  Self-Service > My Tagged Documents
  
- Form context menu: ..., Configure (Form Designer, Form Layout, Related Lists), Export, View, ...
- Form Designer: Fields Panel (Fields (Formatters) and Field Types) - Sections (1 or 2 columns)
  Only Sections with titles are displayed as Tabs (if Tabbed forms is enabled in System Settings > Forms)
- Form Layout: Slushbucket (Available & Selected lists), View name, Section, Create new field
  |- begin_split -| <Fields> |- split -| <Fields> |- end_split -| --> Form with 2 columns
  |- begin_split -|: optional if no fields before
  |- end_split -|: optional if no fields after
- RightClick on field Label in Form: Configure Label/Dictionary/Styles - Show <field name> - Watch <field name>
  If a Choice List field type: Configure Choices - Show Choice List
- Tabs in Forms: System Settings > Forms - Tabbed forms on/off
  Form Design: Section with/without title
  Form Design has three components: Header, Field Navigator, and Form Layout

- Create a new form template: from a form (View permissions of form) OR from the Template Form (admin Role)
  From the Template Form: System Definition > Templates - New
  From a Form: "More Options" icon on the form header - "Toggle Template Bar" on
               Fill needed fields in the template - "Create a new one?" Link or "+" icon at the bottom
  New Template: Name - Application - Table - User - Groups - Fields and Values to include in the template
                "Active" Checkbox and "Global" (All views) Checkbox

- Personalize List/Form by icons to update just the curent User/View
  Configure > List/Form Layout to update for all users and selected views

*****************************************
***           Collaboration           ***
*****************************************

- Assignment Rules: System Policy > Rules > Assignment --> Any Task
  New: Name - Application - TABs: Applies To - Assign To - Script
  Create/Update a Task Record: When "Conditions" are true in "ANY TASK" Table Assign To "User" and/or "Group"
  Applies To: Table - Conditions
  Assignt To: User - Group
- Assignment Lookup Rules: System Policy > Rules > Assignment Lookup Rules --> Just Incident
  New: Category - Subcategory - Configuration Item - Location - Assignment Group - Assigned To
- Service Desk > My Work
  Service Desk > My Groups Work
- User Presence in a Form: Active Viewers icon - Show Activity Stream icon - Follow(ing) Button/List
  Follow(ing) List: Follow/Unfollow - Open Connect Mini - Open Connect Full (new window)
  User Presence in a Conversation: Message Time - Green/Orange Dot (Logged In/Just Logged Out) in User's Avatar
  Real-time editing: Pulse icon
  Notes Tab: Watch list/Work notes list, Work notes/Additional comments (customer visible), Activities, 
             Activities Filter icon
  Watch list: email notification with Additional Comments and the state changes
  Work notes list: email notification with Work Notes and the state changes
  Activity Stream Inline Editor: From a List Header - icon "Show Activity Stream in a flyout window"
- Visual Task Boards (VTB): Guided, Flexible, and Freeform
  Guided VTB: column context menu (reference or choice field with predefined values) > Show Visual Task Board
  Flexible VTB: column context menu (Ex. Number) > Show Visual Task Board
  Guided/Flexible VTB: Self-Service > Visual Task Boards > Create New Visual Task Board > Data Driven Board
  Freeform VTB: Self-Service > Visual Task Boards > Create New Visual Task Board > Freeform Board
  "Create New Visual Task Board" Link if no VTB exist and "New" button if at least one VTB exist
  Only way to add Tasks (Cards) to Freeform boards is by using Field context menu - "Add to Visual Task Board"
  Taskboard tools: Filter, Chat, Info, Users, Labels, Activity Stream, and Configuration Tools
  Guided VTB: reference or predefined values Lanes - +Add Lane (if reference field) - +Add Card
  Flexible/Freeform VTB: To Do, Doing, and Done Lanes - +Add Lane - +Add Card

- System Policy > Email > Inbound Actions - New
  New Record: Name, Application, Target table, Action type, TABs: When to run | Actions | Description
              "Active" Checkbox and "Stop processing" Checkbox
  Action type: "Record Action" or "Reply Email"
  When to run: Type (New/Reply/Fwd) - Required roles - Execution Order - From - Conditions
  Actions: Field actions - Script ("Record Action" type) Reply email (Reply Email type)
- System Notification > Email > Notifications - New
  New Record: Name, Application, Table, Category, TABs: When to send | Who will receive | What it will contain
              "Active" Checkbox and "Allow Digest" Checkbox
  "Allow Digest" Checked: A new Tab "What Digest will contain" is added
  When to send: Send when - Conditions
	Send when: "Record Inserted or Updated" - "Inserted" Checkbox - "Updated" Checkbox
	           "Event is fired" - Event name (from list)
			   "Triggered"
  Who will receive: Users - Groups - Users/Groups in fields - "Subscribable" Checkbox
	Users/Groups in fields: Send notification to users or groups referenced in the triggering record
	Subscribable: Users can set their notification subscription preferences in System Settings
				  System Settings > Notifications - Allow Notifications and Notifications by Category
  What it will contain: Email template - Subject - Message HTML - "Select variables" pane
	"Select variables" pane: Fields value from the triggering record to include within the Subject/Message
  "Preview Notification" Button to preview how the Notification will appear to the user:
  System Mailboxes > Outbound > Outbox --> To verify Notification was sent correctly
  "Advanced view" in Related Links allow to display More fields to Create Email Notification

- Self-Service > Dashboards > New - Recent - Owned by Me - Shared with Me - All
  Add widgets to Dashboards: Reports, Performance Analytics, ..., Catalogs, Catalog Categories, ...
- Reports > View / Run > My reports - Group - Global - All - "Create a report" Button
  Reports > Create New
  From Filtred List: Column context menu - Bar Chart/Pie Chart
  Add widgets to Dashboards - #New Report
  Report Designer: Data > Type > Configure > Style
  Data: Report name, Source type (Data source/Table), Data source/Table
  If there is already a report based on chosen data source, a message is displayed
  Type: Bars (Bar/Pareto...), Pies and Donuts (Pie/Donut...), Time series (Area/Column/Line...), Other (List...)
  Configure: Group by - Additional group by - Configure function field - Aggregation - Set Value Formatting ... 
  Style: Size, colors, and other visual aspects
  Next - Refresh - Run - Save - Share - Sharing icon - Report info icon - Delete report icon
  Sharing Panel: Add to Dashboard - Export to PDF - Based on Role: Share - Schedule - Publish/Unpublish
  Share: Me - Everyone - Groups and Users

*****************************************
***      Database Administration      ***
*****************************************

- System Definition > Dictionary (Can NOT create a Collection (Table), just fields)
  System Definition > Tables (New: Label - Name - Extends table - Module... - Columns TAB Dictionary Entries)
  System Definition > Tables & Columns (Create Table - Create Application - Browse Applications - Schema map)
  sys_id: Globally unique ID 32-character
  System Definition > Number Maintenance
  System Definition > Language File (Relabel a field)
  When a Table is created a Role automatically created u_<table lable>_user
  Global Application: u_<table label>		Scoped Application: x_<scopedapplicationname>_<table label>
  Schema map --> Selected table: highlighted in yellow - Blue bars: Extending tables - Red bars: Extended table
- Dictionary on <field>: RightClick on <field> in form - Configure Dictionary
  Dictionary on <table>: <table> Records List - Column context menu - Configure - Dictionary

- System Properties > Security
  System Security > Access Control (ACL) (No New Button until Elevate Roles)
  System Security > High Security Settings
  <table name>.config (.CONFIG new window) and select the Access Controls tab (ACL associated with a Table)
  When a Table is created, 4 Access Control Rules CRUD are automatically created (Create, Read, write, Delete)
  System Security > Users and Groups > Roles - New
  System Definition > Application Menus - <application> - Roles ("Edit User Roles" icon (pencil))
  User Administration > Groups - Roles TAB to manage Roles
  System Security > Access Control (ACL) - Select a CRUD AC - (Ex.) Add Field - Insert and Stay (Without Roles)
										   Check "Advanced" to display Script

- Configuration > CI Class Manager - "Hierarchy" button
  Configuration > Relationships > Suggested Relationships - New: Base class - Relationship - Dependent class
  Add the "CI Relations" field to the form using Form Layout or Form Design
  CI form - Related Items - "Add CI Relationship" icon --> Relationship Editor:
  Suggested relationship types - Configuration Items, Select a CI - Save and Exit
  CI form - Related Items - "Show dependency views" icon

- Import Set: Load Data, Create Transform Map, Run Transform
- System Import Sets > Load Data - Create/Existing table - Label - Name (Auto from Label) - File/Data source...
  A "Data Source" - an "Import Set" - the "Import Set Table" are created
  The imported "File Label" is used to name the "Data Source" in Data Source [sys_data_source] Table
  System Import Sets > Administration > Data Sources
  Data Source: Name (infinity-data.xlsx (Uploaded)) - Import set table name - Type (File) - Format (Excel)...
  System Import Sets > Advanced > Import Sets
  Import Set: ... State (Loaded) - Data source - Import set table ... - Tab: Import Set Rows (Related Lists)
  System Import Sets > Import Set Tables > "Infinity Imports" (<Import Set Table Name>)
- Create Transform Map (TM): System Import Sets > Create Transform Map
							 System Import Sets > Administration > Transform Maps - New
							 "Load Data" - "Next Steps..." Section (Progress screen) - "Create transform map"
							 "Data Source" - Transforms (Related Lists) Tab - New
  New TM: Name - Application - Source table - Target table - Enforce mandatory fields - Copy Empty Fields ...
  Saved TM: "Auto Map Matching Fields"/"Mapping Assist" Links to Create/Update "Field Maps" Related Lists
- Run Transform: Click on "Transform" in Related Links of the "Transform Map" - "Transform" Button
  Progress screen - "Next Steps..." Section - "Import set Number", "Transform history", and "Import log" Links
  TM Record - "Field Maps" Tab - "Coalesce" Column --> true/false
- System Import Sets > Import Set Tables > Cleanup
  Move the "Import Set Table" from "Available tables for deletion" to "Delete these tables"
  "Delete related transform maps" Checkbox and "Delete data only (preserve table structure)" Checkbox
  "Cleanup" button --> Actions taken are displayed in many Import Log Records
- System Policy > Rules > Data Policies - New: Table - Application - Conditions - Short description - Checkbox:
  Inherit, Reverse if false, Active, Apply to import sets, Apply to SOAP, Use as UI Policy on client
  Saved DP: Data Policy Rules New --> Field name - "Read only" Checkbox - "Mandatory" Checkbox

*****************************************
*** Self-Service & Process Automation ***
*****************************************

- Self-Service > Knowledge
  Service Portal > Knowledge Base
- Service Portal
  Knowledge Home: Knowledge Bases - Featured - Most Useful - Most Viewed
  Article sorted by Views in Service Portal and by Last Updated in Platform UI
  Filter by: Knowledge Bases, Category, Author, Tags, Rating, Last Modified, and View Count
  Listed articles include: Title, KB and category, a short preview, author’s name, number of views, 
                           last update, and rating
  Feedback: Helpful (Yes/No), Rating (one to five stars), Add a comment
  "Copy Permalink" to share an article
  "Actions" List on right top of the article: Flag Article - Edit Article
- Platform UI
  Populate Knowledge Base: Create Article, from cases or incidents, Import Article, Integrate with WebDAV
  Knowledge > Articles > Create New
  Knowledge Home: "Create an Article" icon or button on right top
  Self-Service > My Knowledge Articles
  Knowledge publishing workflow stages: Draft > Review > Published > Pending retirement > Retired
  Knowledge > Feedback Management > {Feedback, My Flagged...}
  Knowledge > Articles > Import Articles

- Service Portal > Request Something
  Self-Service > Service Catalog
  Service Catalog > Catalog Definitions > Maintain Items
  Service Catalog > Catalog Definitions > Maintain Categories
  Service Catalog > Catalog Definitions > Maintain Catalogs
  Item: Name - Catalogs - Category - Tabs: Item Details - Process Engine - Picture - Pricing - Portal Settings
        Related Lists Tabs: Variables - Variable Sets - UI Policies - Client Scripts - (Not) Available For... 
  Process Engine: flow or workflow
  Variables: Attachment/CheckBox/Date/Duration/Email/HTML/Multiple Choice/Select Box/URL/...
  Service Portal > Request Something > Can We Help You?
  Service Catalog > Catalog Definitions > Record Producers
  Record Producer: Accessibility tab (Catalogs, Category), Generated Record Data tab (Template)...
  Service Catalog > Catalog Builder
  Workflow/Flow stages: Waiting for Approval (Approved)- Fulfillment - Awaiting Delivery - Configuration -
                        Delivery - Completed - Request Approved
- Self-Service > My Requests
  Service Catalog > Open Records > Requests (sc_request)
  Service Catalog > Open Records > Items (sc_req_item)
  Service Catalog > Open Records > Tasks (sc_task)
  Item: Related Lists "Available For" and "Not Available For" - New/Edit User Criteria

- Process Automation > Flow Designer
  Flow Designer: Properties - Test - Executions - Deactivate - Activate - Save - ... More Actions menu
  Flow Designer "Help Panel": Question mark icon in the main header - General help
							  Open help panel icon (?) next to the name for any action in the flow - Action help
  System Definition > Plugins - "Process Automation Designer" plugin
  Triggers: Record-based / Schedule-based / Application-based
  Record-based: Created / Updated / Created or Updated
  Schedule-based (Date): Daily / Weekly / Monthly / Run Once / Repeat
  Application-based: SLA Task / Inbound Email / Service Catalog
  Advanced Options (Can be): 
        Interactive/Non-Interactive/Both
        Do Not Run if Triggered by <Users>/Only run if Triggered by <Users>/Run for any user
		Current Table/Extends Tables
		Background (Default)/Foreground
  Actions - Installed Spokes: ServiceNow Core / Connect / CICD /.../ Microsoft Teams /.../ VTB
  ServiceNow Core Sections: Default, Attachments, Change, Email, and Service Catalog
  Default: Ask for Approval, Create/Delete/Look Up Record, Look Up Records, Wait for Condition, ...
  Data Pill Panel: Flow Variables, Trigger - <Type>, Actions by number
  Data Pill Picker icon using the Dot-walking

*****************************************
***    Introduction to Development    ***
*****************************************

- System Definition > Plugins (Demo Data)
- Client Scripts: Application - Table - UI Type - Type - Script
  Types and Script functions: onLoad, onChange, onSubmit, and onCellEdit
  System Definition > Client Scripts
  Column context menu > Configure > Client Scripts
  Form context menu > Configure > Client Scripts
- UI Policies: Application - Table - Conditions (When to Apply) - UI Policy Actions Related List
  UI Policy Actions: Form field Mandatory, Visible, and Read-only
  System UI > UI Policies
  Column context menu > Configure > UI Policies
  Form context menu > Configure > UI Policies
- UI Actions: Name - Application - Table - Action name - Messages - Condition - Script ...
  Checkbox: Client, Form button, Form/List context menu, Form/List link, Form/List style, 
            List banner/bottom button, List choice
  System Definition > UI Actions
  Column context menu > Configure > UI Actions
  Form context menu > Configure > UI Actions
- Business Rules: Application - Table - Advanced Checkbox ON/OFF - When to Apply - Actions - Advanced (if ON)
  When to Apply: before/after/async/display - Insert/Update/Delete/Query - Conditions - Role conditions
  Actions: Set field values - Add message - Abort action
  Advanced: Condition (Expression) - Script (function executeRule(current, previous /*null when async*/))
  System Definition > Business Rules
  Column context menu > Configure > Business Rules
  Form context menu > Configure > Business Rules

- Customer Update [sys_update_xml]
- Update Set: Creation and Export
  • Admin - Instance Settings - "Developer" tab - "Show update set picker in header" on
  • Create an Update Set: System Update Sets > Local Update Sets - New - Submit and Make Current
  • Mark Update Set Complete: Modify the "State" field to "Complete"
  • Export the Update Set: Related Links - Export to XML
- Update Set: Retrieve --> Preview --> Commit
  • Retrieve: System Update Sets > Retrieved Update Sets - "Import Update Set from XML" Related link
              State --> Loaded
  • Preview: "Preview Update Set" button
              State --> Previewed
  • Commit: "Commit Update Set" button
              State --> Commited
- Update Set: Retrieval from a remote instance
  • Connect to remote instance: System Update Sets > Update Sources - New - "Test Connection" button
  • Retrieve: "Retrieve Completed Update Sets" button or related link
              "Retrieved Update Sets" Related list
  • Preview: No need - Automatic with Retrieve
  • Commit: "Commit Update Set" button
  
- System Applications > Studio
  Studio has 4 components: Header, Application Explorer, Content Frame, Status Bar
- System Applications > My Company Applications - "Manage Developers" Related Link
- Guided Application Creator: Two access ways
	System Applications > My Company Applications - "Create New" button
	System Applications > Studio - "Create Application" button

- System Policy > Events > Event Log [sysevent]
  <table name>.<unique event name>
  System Policy > Events > Registry

- System Diagnostics > Stats > Stats	OR		stats.do
