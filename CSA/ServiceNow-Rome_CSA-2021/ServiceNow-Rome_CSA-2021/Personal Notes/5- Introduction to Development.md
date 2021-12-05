*******************************************
*******************************************
***   ServiceNow Rome CSA Notes 2021	***
*******************************************
*** 	      By Omar MOUMEN	   		***
*******************************************
***       Last Update	21/11/2021      ***
*******************************************
*******************************************

***************************************************
***************************************************
***  	Introduction to Development				***
*** 		• Scripting							***
*** 		• Migration and Integration		20%	***
*** 		• Development			        	***
***************************************************
***************************************************

********************************
***	   Platform Scripting    ***
********************************
> Plugins
- Plugins are software components that provide additional optional features and functionalities within aPaaS
  ServiceNow instance. Check the list of available plugins before adding new scripts
- System Definition > Plugins
- Demo Data, Published plugins
> Client-side scripting
- Client scripts (CS) make "real-time" changes to the appearance of the user interface, especially forms
- CS allow for browser/form manipulation and verification such as making fields visible on a condition
- Several types of Client scripts are supported:
  • onLoad(): Runs when a form is first drawn and before control is given to the user to begin typing
  • onChange(): Runs when a particular field changes value
  • onSubmit(): Runs when a form is saved/submitted/updated
  • onCellEdit(): Runs when a cell on a list changes value through use of the list editor
- UI policy is a rule that is applied to a form or a list to dynamically change information or the form itself
- Use UI policies to add sophisticated controls without having to write scripts
- UI policy actions determine what happens on the form, including:
  • Setting a field as mandatory
  • Setting a field as hidden
  • Setting a field as read-only
> Server-side scripting
- A business rule is a server-side script that is configured to run when a record is displayed, inserted, 
  updated, deleted, or when a table is queried. They can be set to run "before" or "after" the database action
  has occurred  
- When to run and Actions
- Advanced: Condition and Script
- Business rules are NOT "real-time"
- The primary objective of "display" Business Rules is to use a shared scratchpad object, "g_scratchpad", which
  is also sent to the client as part of the form. This is useful when you need to build client scripts that 
  require server data that is not part of the record being displayed
- UI actions add buttons, links, and context menu items on forms and lists
- UI actions can execute client-side and/or server-side depending on the "client" checkbox selection
- UI actions conditions and actions can be scripted to define complex custom functionality
- Script Includes

***************************************
***	   Migration and Integration    ***
***************************************
> Update Sets
- An update set tracks changes to applications and platform features, then groups them together so they can be
  moved from one insatnce of ServiceNow to another
- Group of one or more changes that can be moved from one instance to another all together
- An update set record is a "point in time" XML snapshot of process records
- Update Sets work by writing changes from tracked tables to the Customer Update [sys_update_xml] table
- Newest changes overwrite older changes in an Update Set
- When merging multiple update sets, if several update sets have modified the same object (e.g. Incident form), 
  the most recent change will be the one moved to the merged update set
- The "Default Update Set" captures changes made to the instance without adding those changes to any 
  user-created update set
- It is recommended to avoid using the "Default Update Set" for moving customizations between instances
- customizations and configuration changes are captured in an update set, but NOT changes to data records
- Tracked: Business Rules, Client Scripts, Fields, Forms and Form Sections, Report Definitions, Tables, 
  Views, Roles, Published Flows
- NOT tracked: New Data Records, Modified Data Records, Tasks, Modified CIs, New Users and Groups, Schedules, 
  Scheduled Jobs, Dashboards, homepage
- NOT captured by default in an update set: 
  • Data records except when using the "Export XML" function
  • Dashboards but can be manually added by using the "Unload Dashboard" Function
- Instance Settings > Developer > Show update set picker in header
- To create an Update Set: System Update Sets > Local Update Sets and New
- To export it: change its State to "Complete" and "Export to XML" Related link
- To upload it: System Update Sets > Retrieved Update Sets and "Import Update Set from XML" Related link
  Locate and open the imported record, select the "Preview Update Set" button, and if no errors select the
  "Commit Update Set" button
- Retrieve --> Preview --> Commit
- Same Instance Version, 100 records max by Update Set recomended by ServiceNow, Records have matching "sys_id"
- To retrieve an update set from a remote instance: System Update Sets > Update Sources
  Select any existing remote instance or "New" to establishe connectivity to new one
  Click the "Retrieve Completed Update Sets" button or related link
  Select the "Retrieved Update Sets" Related list, select the one you want, and click the "Commit Update Set"
> Integration
- ServiceNow integrates with many third-party applications and data sources to share data with external systems
- Standard integrations for ServiceNow include: Login SSO, LDAP, Communications, Monitoring, System Management
- The most common processes required for integration are the CMDB, Incident Management, Problem Management, 
  Change Management, User Administration, and Single Sign-On (SSO)
- A variety of techniques can be used, most notably web services, LDAP, Excel, CSV, and email
- IntegrationHub provides a single solution to quickly integrate with third-party services to build and share 
  content. Integrations are referred to as spokes and can be easily configured to integrate without scripting


*************************
***	   Development    ***
*************************
> Application Scope
- Every application has a scope:
  • Determines which of the application's resources are available to other applications in the instance
  • Protects applications by identifying and restricting access to available artifacts and data
  • Prevents naming conflicts and allows the contextual development environment to determine what changes, 
    if any, are permitted
  • Is assigned to an application when it is first created and cannot be changed
- The system automatically prepends the "unique namespace identifier" to the front of application artifacts
  such as tables, scripts, and configuration records when they are created
- The "Global" scope is a special application scope that identifies applications developed prior to application
  scoping or applications intended to be accessible to all other Global applications
> Application Development Tools
- Guided Application Creator
  • Creating an application record
  • Defining user roles
  • Designating data tables
  • Designing the application for different user experience
- ServiceNow Studio provides an "Integrated Development Environment (IDE)" like interface for creating custom
  applications. It offers a simple way to identify and interact with applications files, create files as you 
  develop, and modify existing application files in a tabbed environment
- Application developers can also access Studio to import or open applications
- With Studio, application developers can:
  • See exactly what files comprise their application in the Application Explorer
  • Add new files to their application using a single Create Application File Interface
  • Navigate to files using familiar search-by-name or by-type behavior with the Go To dialog
  • Find code both within and outside an application using the Code Search tool
  • Operate on multiple files at once using the tabbed interface
  • Operate on multiple applications at once using multiple studio windows
  • Publish the application to company instances or the ServiceNow Store
  • View information about the current application from the Status bar
- Accessing Studio requires an admin or a delegated developer role
- You can use Guided Application Creator to create an application record and then configure it in Studio later
- App Engine Studio (AES) for low-code development, automating business processes, and solving business problems
- AES allows to delegate development work that were once assigned to administrators, with little to no training
- With AES, you can leverage development tools and build apps quickly using templates for pre-build solutions
- Using AES, developers can also:
  • Create applications from scratch
  • Access a list of recent applications you have built
  • Access links to add objects to apps, browse app templates, and learn more about the available tools
  • Access a list of templates with preconfigured data, experience, automation, and security
- Automated Test Framework (ATF): Create and run automated tests to confirm your instance after making a change
- Tests include a series of steps that the test attempts to execute
- Once run, the ATF creates a Test Results record, which is available through a Related List on the test record
- All test records are defined with test steps. A step includes an action to take and needed data to take action
> Delegated Development
- Delegated developers are non-administrator users and groups that are assigned one or more permissions to 
  develop applications
- Permissions for specific actions to the assigned users in the current instance
- System Applications > My Company Applications
- Locate and open any application and select the "Manage Developers" Related Link
- Developer Permissions: All File Types, Allow Scripting, Integrations, Reporting, Workflow, Service Catalog, 
  Server Portal, Flow Designer, Forms, and Manage ACLs & Roles
- Deployment Permissions: Upgrade App, Publish To Update Set, Publish To App Store, Manage Update Set, and 
  Publish To App Repo

**********************
***     Events     ***
**********************
- Events are special "log records" the system generates when something notable has happened or certain 
  conditions occur
- They are then responded to with pre-defined actions in response to the condition(s)
- All base system events have built-in logic to respond when an event occurs
- The system uses "Business Rules" to monitor for system conditions
- The GlideSystem "eventQueue()" methode is used to insert event records, which means you can generate an event 
  wherever you can script. Including: Flows and Workflows
- When a condition is met, its responding action generates an event record in the "Event [sysevent]" table
- By convention, events are named using the syntax "<table name>.<unique event name>" (incident.updated)
- To see a log of every generated event navigate to "System Policy > Events > Event Log"
- An event must be registered before it can be used
- Navigate to the "System Policy > Events > Registry" module to create a new record

******************************
***     Instance Stats     ***
******************************
- The Stats module provides statistics for system activities that affect performance such as the execution of 
  queries, scripts, and transactions. Module used also to lookup which version, patch, and hotfix
- "System Diagnostics > Stats > Stats" or "stats.do" in the filter Navigator

*********************************************
***	   Additional ServiceNow Resources    ***
*********************************************
> Locate ServiceNow Resources
- ServiceNow website
- Product documentation
- Support on HI
- Community
- Social media links and support
- Additional resources: ServiceNow partner, Now Learning, Developer portal, ServiceNow store
> Now Creators
- With Now Creators you can map out a path dedicated to learning and exploration based on who you are and where 
  you want to go
- Now Creators can recommend how to leverage the ServiceNow resources available to build your skills and track 
  your accomplishments
- Three important steps: Get Skills, Earn badges, and Share your success
- Super badges: Star, Pro, and Legend
> Now Profile
- Your Now Profile is the basis for managing ServiceNow accomplishments
> Now Learning
- Now Learning is the single source for all of your ServiceNow course content, certification, 
  certification maintenance, and profile needs
