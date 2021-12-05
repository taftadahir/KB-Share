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
***  Self-Service & Process Automation  ***
*** 	• Knowledge Management			***
*** 	• Service Catalog			20%	***
*** 	• Flow Designer			        ***
*******************************************
*******************************************

**********************************
***	   Knowledge Management	   ***
**********************************
- Knowledge management provides a centralized location for the creation, categorization, viewing, 
  and governance of information related to the flow of work through ServiceNow
- Information is stored in knowledge bases, or “KBs” for short
> Accessing the Knowledge home
- Platform UI or the Knowledge Management Service Portal homepage (Knowledge Portal)
- Self-Service > Knowledge
- https://dev64090.service-now.com/sp
- Featured articles are selected by the system administrator or KB managers for special attention
- Most Useful ranks articles according to the percentage of readers who marked them as helpful
- Most Viewed shows the latest viewing trends
> Browsing and searching for articles
- We can filter by Knowledge Bases, Category, Author, Rating, Last Modified, and View Count
> Viewing articles and providing feedback
- Response, Rating, Helpful (Most Useful), Comment, Share (Permalink)
- Flagging an article is a good way to suggest revisions to the knowledge manager
> Posting questions
- If Social Q&A is active for a KB, you can ask questions and respond to questions from other users
> Knowledge Article
- A knowledge article is a record in a knowledge base that provides information to knowledge consumers
> Create knowledge articles
- Create articles: Create articles using templates, and/or knowledge blocks directly in ServiceNow
- Create articles from cases or incidents: Allow agents and resolvers to quickly create and save knowledge to 
  share with users from cases in Customer Service Management or incidents in IT Service Management applications
- Import articles: Import Microsoft Word files into a knowledge base
- Integrate: Integrate to an existing, WebDAV (Web Distributed Authoring and Versioning) compliant knowledge 
  source outside of ServiceNow (Ex. Sharepoint)
- Add Blocks, Search for Duplicates
- If Knowledge-Centered Service (KCS) is used in your organization, agents and resolvers can create knowledge 
  articles directly from cases or incidents
- Knowledge > Articles > Import Articles
- When creating articles manually or by import, selecting Publish will trigger the publish workflow assigned 
  to the knowledge base. This may mean the article is automatically moved to a Published state, or it may first 
  require approval(s)
- Articles that populate a knowledge base via integration do not follow the publish workflow assigned to the 
  knowledge base

******************************
***	   Service Catalog	   ***
******************************
- Service Catalog: Multiple catalogs of products and shared services that your organization offers to its 
  employees, customers, suppliers, and others
> Categories
- The products and services in a catalog are organized into categories and subcategories
- End User: Self-Service > Service Catalog
> Catalog items
- Service Catalog > Catalog Definitions > Maintain Items
- Service Catalog > Catalog Definitions > Maintain Categories
- The fulfillment process specifies the various people and groups required to perform a series of tasks 
  to fulfill the request
> Service requests
- In general, these items are simplified versions of the full forms that are used to create such requests
- Create Incident is in the "Can we help you?" category
- These forms are called "Record Producers" because they add a record to a system table, like the Incident table
- "Record Producers" implement simplified forms allowing users to create task-based records with minimal input
- The service catalog in the base system includes several record producers
- Service Catalog > Catalog Definitions > Record Producers
- On the Generated Record Data tab, you can define a template to assign one or more static field values for 
  all records created by the record producer
> Service Catalog management roles
- There are several roles, providing different levels of access, that can be assigned to users to delegate 
  service catalog management tasks
- Administrators can manage all aspects of the Service Catalog application, including: catalogs, categories,
  catalog items, and scripting functions, such as creating business rules
- Catalog administrators also can manage all aspects of the Service Catalog except scripting functions
- Catalog managers can edit and update their assigned catalogs, including its categories and catalog items. 
  They may also assign catalog editors and assign the catalog to a different manager
- Catalog editors can perform the same functions as a catalog manager for their assigned catalogs, 
  including assigning editors to the catalog, but they cannot reassign the catalog manager
> Catalog Builder
- Create or edit catalog items using Catalog Builder
- This visual and guided tool enables you to delegate the creation and maintenance of the catalog
- Creating templates with "Catalog Builder" allows to specify values or restrictions for items created using 
  the template (ex. Restrictions to catalogs, categories, variable types, and portal settings)
- There are limitations to what you can do in Catalog Builder as it does not allow the creation and editing of 
  certain entities (ex. Price settings, Default value, Permissions...)
- Using the Catalog Builder you can:
    • Create a catalog item and item templates
    • View the available catalog items and item templates
    • View catalog items that are recently updated
    • View the configured content that describes the catalog building process in your organization

************************************
***	   Catalog Administration    ***
************************************
- Views can be defined for groups that view a Catalog, and Catalog Items can be shared by multiple catalogs.
  This results in the ability to dynamically control the ordering options from user to user
> Service Catalog Major Components
- ITEM: presents one product or service. Records are produced and stored in the Service Catalog tables
  Hardware, Software, Services
- ORDER GUIDE: presents multiple Catalog Items that are grouped together logically as one request.
  Records are produced and stored in the Service Catalog tables
- RECORD PRODUCER: presents one product or service for ordering. Records are produced and stored on tables
  outside of the Service Catalog space. They are a simplified forms that produces a task record
- VARIABLES: Questions that help the requester specify item/service options. Variables can affect order price
- The Service Catalog allows you to attach individual variables to a catalog item, or multiple variables
  collected in a Variable Set. Service Catalog variables are global by default. Common Variable Types:
  Multiple Choice, Select Box, Single Line Text, Reference, Checkbox, ...
- VARIABLES SETS: A collection of Variables that can be reused across multiple Catalog Items and Order Guides
  Service Catalog > Catalog Variables > Variable Sets
- FLOWS: Run behind the scenes and communicate the stages of the approval process to the requester, as well as
  drive the request fulfillment
> Catalog Records
- For catalog items, a request record, a request item record, and catalog tasks are all created when an order
  is placed, each on a corresponding table:
  • Request [sc_request]: Records on this table begin with "REQ" and behave like containers (Top Level)
  • Requested Item [sc_req_item]: // "RITM" and manage the delivery of each individual item in the request
  • Catalog Task [sc_task]: // "SCTASK" and are the assigned tasks needed to complete the delivery of each 
    Request item from start to finish. Some of the more important fields are: Assignment group, Due date, 
	Work start, and Work end dates
- To track the SC Request: Self-Service > My Requests
- Flow Designer Stages
- Catalog security: user criteria
  Defines conditions that are evaluated against users to determine which users can access catalog items. You
  can apply several user criteria records to a single catalog item or category
- Add or edit user criteria for item or category: Available For or Not Available For Related List
- Not Available For settings override the Available For settings

***************************
***	   Flow Designer    ***
***************************
> What - When - How
- Flow Designer creates the flow of work for a repeatable process
- Flow Designer is a non-technical interface for building and enabling process automation capabilities, 
  known as flows
- Flows automate business logic for a particular application or process such as approvals, tasks, notifications,
  and record operations
- Centralized, Robust, User-friendly, Repeatable, Scalable
- Do use:
    • To orchestrate business processes across services with little technical user knowledge
    • To reduce technical debt; meaning reduce scripting to simplify upgrades and deployments
    • To integrate with 3rd party systems
- Do not use when:
    • Existing logic already developed using the ServiceNow workflow editor
    • ServiceNow Instance is running Jakarta or prior
- Process Automation > Flow Designer
- The different functionality available in Flow Designer is controlled by the following roles: 
  flow_designer, flow_operator, and action_designer
- Each flow consists of a trigger and one or more actions
- When the conditions of the trigger are met, the flow will execute the actions
- Each action is a reusable operation (Without code). Different actions are strung together to make a flow
- IntegrationHub & Spokes
- Flow Designer Help Panel offers information about working with data and spokes, building actions and flows, 
  and guided tours
> Process Automation Designer
- System Definition > Plugins to search and Install the Process Automation Designer plugin 
  (check the Load demo data box)
- The Process Automation Designer allows you to organize content built in Flow Designer and unify 
  cross-enterprise processes. Benefits of using the Process Automation Designer include: 
    • Connecting multiple flows and actions
    • Guiding end users to complete a process in a task-oriented interface
    • Consolidating separate business processes across your organization
    • Defining a consistent record lifecycle from beginning to end
    • Passing data between activities and stages of business processes
    • Specifying the conditions and the order for activities and stages
    • Visualizing and managing activities and stages in a Kanban-style board
> Flow Designer triggers
- Triggers can be record-based, schedule-based, or application-based
- Record-based triggers run a flow after a record has been created, updated, or deleted
- Schedule-based triggers run a flow at the specified date and time: daily, weekly, monthly, etc.
- Application-based triggers are added when the associated application spoke is activated
- A Spoke contains Flow Designer triggers and actions dedicated to a particular application (ex. ITSM Spoke)
> Flow Designer actions
- Flow Designer promotes reusability to see all actions across multiple spokes in a no-code/low-code environment
- Each installed Spoke can house several actions
- Ex. Actions: Ask for Approval, Create/Delete/Look Up Record, Look Up Records, Wait for Condition
> Flow Designer data
- Each time you add an action to a flow, Flow Designer adds a data pill to store its output results
- The Data section of the Flow Designer contains data pills that can be used in subsequent actions
- The Data Pill Picker icon provides an alternative way to select data pills from the data panel into the flow
- The Data Pill Picker can be a faster way to select data when dot-walking to other tables is required
- When designing a flow, you can use the results of an action as inputs for other flows, actions, or subflows
- When a flow runs an action, it generates the data pill runtime value, which remains the same for the duration 
  of the flow
- Prior to the introduction of Flow Designer, ServiceNow repeatable processes were created using a tool called 
  Workflow Editor. All new development should use Flow Designer

***************************
***	   Virtual Agent    ***
***************************
- Virtual Agent is a conversational bot platform that provides assistance to help users obtain information, 
  make decisions, and perform common work tasks
- This includes information stored in Knowledge Bases, Service Catalog, and System records
- Virtual Agent offers a personalized customer experience by automating typical Tier 1 support tasks 
  to be accomplished, including:
    • Answering FAQs
    • Providing tutorial (“how to”) information
    • Querying or updating records (for example, get the status on cases or incidents)
    • Gathering data, such as attachments, for the agent
    • Performing diagnostics
    • Resolving multi-step problems
- Virtual Agent offers a web-based interface available for Service Portal, iOS and Android mobile environments
- It supports third-party messaging applications through ServiceNow adapters for Slack, Workplace, and Teams
