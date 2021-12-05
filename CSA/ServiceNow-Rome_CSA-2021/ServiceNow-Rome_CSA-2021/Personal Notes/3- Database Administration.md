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
***		Database Administration					***
*** 		• Data Schema						***
*** 		• Application/Access Control	30%	***
*** 		• CMDB								***
*** 		• Import Sets						***
***************************************************
***************************************************

*************************
***	   Data Schema    ***
*************************
> Tables and Fields
- ServiceNow infrastructure: Tables, Records, and Fields
- Lists and forms provide a friendly user interface (UI) for managing the data in records and fields
- System Definition > {Dictionary, Tables, Tables & Columns}
- Dictionary: contains the definition for each and every table and field in the DB (Modify attributes)
  Table records are identified as a Collection type
- Tables: contains a record for each table in the DB
- Tables & Columns: lists existing tables in the DB. Selecting a table name displays its contents
- Tables and Tables & Columns modules can be used to create a new table
- A table is a collection of records in the DB. Each record corresponds to a row in a table
- Records: Are identified by a 32-character, globally unique ID, called a sys_id
- To manage record numbering: System Definition > Number Maintenance
- Every field has three attributes: Field Label, Field Name, and Value
- A reference field stores a unique system identifier (known as the sys_id) of a record on another table which
  is what establishes the reference relationship
- Reference fields are identified with the Reference Lookup icon. Information icon to preview referenced record
- Document ID element type can refer to records on any table
> Table Relationships
- Tables can be related to each other: One-to-Many, Many-to-Many, Database Views, and Extensions
- There are 3 One-to-Many relationship fields: Reference Fields, Glide List, and Document ID Fields
- Document ID Fields: Allows a user to select a record on any table in the instance
- Many-to-Many: Two or more tables can be related in a bi-directional relationship, so that the related records
  are visible from both tables in a related list
- Database Views: Two tables can be joined virtually to allow for reporting on data that might be stored in 
  more than one table. Database Views are read-only
- Extensions: A table can extend another table. The extended table includes unique fields plus all the fields
  and their properties from the parent table
> Extended tables
- For Stand alone tables, only the "global default" fields are automatically created
- The option to extend a table is only available when creating a new table. NOT all tables are extensible
- System Definition > Language File: To add a different label for an extended table (new entry)
- A table's Extensible field is used to control whether a table can be extended
- Dictionary overrides: provides the ability to define a field on a child table differently from the field
  on the parent table (default values, field dependencies, read-only status of a field, ...)
- If a table is extended but itself is not extending another table, it is called a "Base" table
- ARE inherited: Business rules, ACL, client scripts, UI policies, UI Actions
- NOT inherited: Workflows, notification
- "Core" tables are created by ServiceNow and provided with the base system
- "Custom" tables are created by admins or developers
- New Custom tables in the global application are prefixed with "u_", in a scoped application with "x_"
> Schema Map
- The Schema Map provides a graphical representation of other tables related to a specific table
- Schema Map is available to users with admin or personalize_dictionary Roles
- System Definition > Tables & Columns: Select a table and click Schema map button

- A custom table can be deleted after all the records in the table are deleted. The table and all items that 
  reference the table are deleted, including:
    • Choice list items
    • Forms, form sections, lists, and related lists
    • Reports and Performance Analytics widgets
    • Reference fields that reference the table
    • Access controls


****************************************
***	   Application/Access Control    ***
****************************************
> Access Control Overview
- User Authentication/Login: Users, Groups, and Roles
- Application and Modules Access: Controlled by roles configured at the Application and Modules level
- Database Access: Access to tables, records, and fields is controlled via globally defined system properties;
  as well as table and field level Access Controls (deny access is the default behavior)
- Three security modules on the Application Navigator:
	• System Properties > Security
	• System Security > Access Control (ACL)
	• System Security > High Security Settings
- An access control is a security rule defined to restrict the permissions of a user from viewing and 
  interacting with Data. Most security settings are implemented using access controls (row and/or column level)
- CRUD: Create, Read, Update (write), and Delete
- In addition to restricting CRUD operations, access control rules can restrict ServiceNow-specific operations
  on tables and fields (Ex. execute, edit_ci_relations, save_as_template, report_on, personalize_choices, ...)
- The access control list (ACL) contains a list of the instance's access control rules
- Users with the appropriate permissions can modify rules and their definitions
- In order for a user to create or update access control roles, they must have the "security_admin" role
- Each access control rule specifies:
	1- The object being secured (e.g. table, field)
	2- The permissions required to access the object (Roles, Conditional Expressions, Scripts)
	3- Operation - a valid action the system can take (CRUD)
- Access Control Rules allow access to the specified resource if all three of these checks evaluate to true:
    1- The user has one of the roles specified in the Role list, or the list is empty.
    2- Conditions in the Condition field evaluate to true, or conditions are empty.
    3- The script in the Script field (advanced) evaluates to true, or sets the variable "answer" to true, or is empty.
    The three checks are evaluated independently in the order displayed above.
- When a custom table is created, the system creates 4 access control rules by default: CRUD
- A role is also created by default and associated with these access control rules
- <table name>.config (.CONFIG new window) and select the Access Controls tab
> Access Control Evaluation
- Record ACL rules are processed in the following order:
	1- Match the object against "table" ACL rules - most specific to most general:
	   table?, parent table?, *?
	2- Match the object against "field" ACL rules - most specific to most general:
	   table.field?, parent table.field?, *.field?, table.*?, parent table.*?, *.*?
- Each access control specifies the table or type of record (including fields), operation being secured,
  and unique object identifier
	• "table.None" applies to the entire table
	• "table.field" is one specific field on the table
	• "table.*" represents all other fields in the table
- Wildcard ACL rules reduce the amount of rules required to control access (less required maintenance)

******************
***	   CMDB    ***
******************
- The Configuration Management Database (CMDB) is a series of tables and fields that store all of the 
  information about the configuration items (CIs) controlled by your organization, as well as their attributes
  and relationships to other CIs
- Access to the CMDB tables and underlying data requires certain permissions, such as the following roles:
  asset, itil, itil_admin, cmdb_read
- CIs can be tangible or intangible (material or non-material) devices or applications in the CMDB such as 
  firewalls, computers, email services, and business services, that need to be managed in order to deliver 
  services
- The Configuration application provides core functionality for the CMDB, including modules for hardware and 
  other CIs. This functionality is part of the CMDB plugin, which is activated in a base install
- The CMDB provides a logical model of company infrastructure by identifying, controlling, maintaining, and
  verifying the CIs that exist
- CMDB Data Manager tool
- Key CMDB tables:
	• "Base Configuration Item [cmdb]" is the base CMDB table for non IT CIs
	• "Configuration Item [cmdb_ci]" stores the basic attributes of all the CIs
	• "CI Relationship [cmdb_rel_ci]" contains CI relationship data
- Configuration > Relationships > Suggested Relationships
- ServiceNow Discovery and Service Mapping
> Using the CMDB
- Typically in business, a high percentage of incidents are caused by failed changes
- The benefits of having an accurate and up-to-date CMDB include:
	• Locating failed changes and associated incidents
	• Facilitating quick analysis of impact, helping reduce or eliminate downtime
	• Increase cost saving to business
- Some of the IT challenges that can be solved with the CMDB are:
	• Consolidating disparate Configuration Item (CI) data into a single Configuration
	• Regularly maintaining complex data for accuracy
	• Making sense of data to drive decisions and services
- CI relationship editor to create configuration item relationships
- Use the "CI Class Manager" to centrally view, create, or edit basic class definitions, and class settings 
  for identification, reconciliation, and CMDB Health
- Dependency View, map icons
- The Common Service Data Model (CSDM)
- CSDM is a CMDB-based framework that identifies where to place data for the products you are using
- Common Service (CS)
- Data Model (DM)
- Use the CSDM to:
	• Show you how to do a specific activity
	• List the in-scope and out-of-scope activities
	• Details the tables and configuration items (CIs) associated with the use case
	• Describes the benefit (value proposition) of the use case
	• Track assets through their life-cycle transitions
- Configuration > CI Class Manager - "Hierarchy" button

*************************
***	   Import Sets    ***
*************************
> Import Sets
- System Import Sets > Load Data
- Roles: import_admin, import_set_loader, or import_transformer
- Import data from various data sources and then map that data into ServiceNow tables
- Local Data Source File: CSV, Excel, JSON, XML, Custom (Parse by Script)
- File retrieval method: Attachment, FTP, FTPS, HTTP, HTTPS, SCP, SFTP
- External Data Source types: JDBC, LDAP, OIDC, REST (IntegrationHub) and Custom (Load by Script)
- Must have admin or import_admin role to manage all aspects of import sets
- Import set table: Staging area for records imported from a data source. Fields are generated automatically
  based on imported data and should not be modified manually
- Transform map: determines the relationships between fields in an import set table and fields in an existing
  ServiceNow table. Once defined, a transform map can be reused
- "Any table" is a potential destination for transformation of an Import Set. "Any field" within a table can 
  serve as a potential destination for transformation from a field within an Import Set
- Automatic mapping utility and Mapping assist utility
- Import Sets run as user System and therefore cannot add data to encrypted fields
> Coalesce Fields
- If more than one record matches the specified coalesce options, only the first matching record is updated
- No coalesce, Single-field coalesce, Multiple-field coalesce, Conditional coalesce
> Data Policy
- A data policy is a rule that enforces data consistency by setting fields as mandatory and/or read-only.
  Its purpose is to standardize data across ServiceNow application
- Data policies can apply rules to all data entered into the system.
- Can be applied to the list view to make a field read-only (field editable but update will fail)
- Data policies are NOT about security, they are about managing the integrity of the information stored in DB
- A Data Policy can also run as a UI policy client-side --> "Use as UI Policy on client" attribute to true
