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
***  	Collaboration					***
***			• Task Management	  20%	***
***			• Notifications				***
***			• Reporting					***
*******************************************
*******************************************

*****************************
***	   Task Management    ***
*****************************
> Task Overview
- Task Table
- Incident, Problem, Request, Change Request Tables
- Approvals, Assignment rules, Service Level Agreements (SLA), Inactivity monitors, Workflow
> Task Assignment
- Users, Groups, Roles, Assign tasks
- Assignment rules: System Policy > Rules > Assignment
- Assignment rule criteria: 
  • The Task record has been created (or modified)
  • The Task record must be unassigned (no values in the Assigned to or Assignment group fields)
  • The assignment rule is the first rule that matches the specified table and conditions (lowest Order value)
- Assignment lookup rules: System Policy > Rules > Assignment Lookup Rules
- Predictive Intelligence
- Predictive Intelligence example: Populate fields according to key words in Short description
- My Work / My Groups Work: Service Desk > My Work or Service Desk > My Groups Work
> Task Collaboration
- User Presence, Following
- Real-time editing, Watch List
- Notes Tab: Work notes (Internal), Additional comments (customer visible), Activities
- Activity Stream inline editor
> Visual Task Boards
- Visual Task Boards (VTB): Guided, Flexible, and Freeform
- Elements of a Visual Task Board: Taskboard Tools, Quick Panel, Lanes, and Cards
- Taskboard tools: Filter, Chat, Info, Users, Labels, Activity Stream, and Configuration Tools
- Guided VTB: column context menu (reference or choice field with predefined values) > Show Visual Task Board
  Self-Service > Visual Task Boards > Create New Visual Task Board > Data Driven Board
- Flexible VTB: column context menu (Ex. Number) > Show Visual Task Board (Lanes: To Do, Doing, Done...)
  Self-Service > Visual Task Boards > Create New Visual Task Board > Data Driven Board
- Freeform VTB: Self-Service > Visual Task Boards > Create New Visual Task Board > Freeform Board
  Only way to add Tasks (Cards) to Freeform boards is by using form context menu

***************************
***	   Notifications    ***
***************************
- Inbound actions and Notifications
> Inbound actions
- Actions for inbound email from users
- Inbound email actions: Actions that the system takes in response to messages from users
- Inbound emails can update tables or send a reply email
> Notifications
- Notifications: email, text messages and meeting invitations
- Notifications are triggered by system events, such as changes to tables
- System Notification > Email > Notifications: notifications currently defined in the system
- New notification: When to send | Who will receive | What it will contain
- The When to send tab shows the conditions that trigger the notification
- The Who will receive tab shows who’ll get this notification
- The Users/Groups in fields icon lets you send notifications to users or groups referenced in the record 
  that triggers the notification
- Subscribable: Users can set their notification subscription preferences in System Settings
- Notification preferences in Settings: Notifications are organized by category
- The What it will contain tab shows the content of the notification
- In the Select variables pane, you can choose field values from the record to include within the message
- To preview how the Notification will appear to the user, click Preview Notification
- An email digest is a single email that summarizes the activity for a selected notification and its 
  target record during a specified time interval
- Subscribable and email digest are ways to prevent the notifications overuse

***********************
***	   Reporting    ***
***********************
- Report Designer
- ServiceNow has over 25 standard report types
- Bar charts and Pie charts
- Using dashboards
- Responsive Dashboards in the content frame let users share Widgets like Reports and Performance 
  Analytics visualizations
- Generating reports from Lists
- Generate bar chart and pie chart reports from Column Context Menu
- Report data is grouped by the column you click. Report only includes the filtered data
- Creating reports from Report Designer
- Reports (Application) > View/Run (Module)
- Reports > Create New
- Create New Report: Data | Type | Configure | Style (Order and navigating by next are not mandatory)
- You can create a report from a data source or a table
- Table: you need to provide all the conditions to select report data from the table, even if many of the 
  conditions are the same from one report to another
- Data Source: a standard set of conditions for querying a particular table which can be reused in other reports
- Report Types
  Bars                    : Bar, Histogram, Horizontal bar, Pareto
  Pies and Donuts         : Pie, Donuts, Semi donut
  Time Series             : Area, Column, Line, Spline, Step Line
  Multidimensional reports: Bubble, Heatmap, Multi-level pivot table
  Scores                  : Dial, Single Score, Speedometer
  Other                   : Box, Calendar, Control, Funnel, List, Map, Pivot table, Pyramid, Trend, Trendbox
- After you create a report, it appears in the Reports > View/Run module under the My reports list
- Sharing reports: Add to Dashboard or Export to PDF
- When you export to PDF, you lose the benefit of sharing real time information
- Additional report sharing options are available based on role: Share, Schedule, and Publish or Un-publish
- The suggested and recommended way to share a report is "Share" the report
- By default, a report is shared with the report creator only
- Remember to save the report after modifying its sharing settings
- Reports that present aggregate data such as pie or bar charts do not require access to underlying data
- Publishing creates a URL for others to access the report including people who are not ServiceNow users
- Scheduled report will be run and shared with users and groups by email*
- Scheduled report mail types: PDF-landscape/PDF/PNG/Embedded PNG
- Reports and Performance Analytics
- Performance Analytics: Create management dashboards, report on KPIs and metrics, and increase quality and 
  reduce the costs of service delivery
  • Widget: Saved view of indicator or breakdown
  • Tables: Indicator Source - calculates scores
  • Data Collector: Recurring jobs taking data snapshots
  • Dashboard: Custom arrangement of widgets
