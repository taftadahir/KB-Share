### Implementation
- [ ] Create a record producer
	- [ ] Application : gene_application_name
	- [ ] For table : gene_table_display_name 
	- [ ] Name: gene_query_name
	- [ ] Short description: gene_short_description
	- [ ] Description: gene_description
	- [ ] Owner: gene_owner
	- [ ] Apply variable set : gene_variable_sets
	- [ ] Create variables : gene_variables
	- [ ] Add picture
		- [ ] Icon
		- [ ] Picture
	- [ ] Catalog : gene_catalog_name
	- [ ] Put the catalog item/record producer under the sub category : gene_category
	- [ ] Available For : gene_user_criteria
	- [ ] Script 
		- [ ] Mapping
			- [ ] Short description: gene_query_name
			- [ ] Query type : record producer sys_id

```javascript
// Mapping
current.short_description = "gene_query_name";
current.u_query_type = cat_item.sys_id;
```


- [ ] Create and configure form and view
	- [ ] create view
		- [ ] View name : gene_view_name
		- [ ] Title : gene_query_name
	- [ ] Add fields to table : gene_add_fields_to_table
	- [ ] Form layout
		- [ ] Left column
			- [ ] Number
			- [ ] Account(ootb field and mandatory)
			- [ ] Contact
		- [ ] Right column
			- [ ] Needs attention (flag)
			- [ ] State
			- [ ] Opened
			- [ ] Opened by
			- [ ] Priority
			- [ ] Assignment Group
			- [ ] Assigned to
		- [ ] Short description (full row)
		- [ ] Add annotation
			- [ ] Annotation type: Section separator
		- [ ] Add variables : gene_add_variables_form
		- [ ] Add sections
			- [ ] Name: Notes (see default and other layout)
				- [ ] Left column
					- [ ] Watch list
				- [ ] Right column
					- [ ] Work notes list
				- [ ] Additional comments
				- [ ] Work notes
				- [ ] Activity Stream
			- [ ] Name: Related Records: Already applied
			- [ ] Name : Resolution Information 
				- [ ] Left column
					- [ ] Resolved by
					- [ ] Resolved
					- [ ] Resolution code
				- [ ] Right column
					- [ ] Closed by
					- [ ] Closed
				- [ ] Resolution notes
			- [ ] Name: Request Details
				- [ ] 1 column wide
				- [ ] Add 'AU Variable Editor' ui formatter
- [ ] Add interceptor answer
	- [ ] Question: Dealer Query (Australia)
	- [ ] Name: gene_query_name
	- [ ] Order: 100
	- [ ] Active: checked
	- [ ] User Prompt: gene_query_name
	- [ ] Target url : gene_table_name.do?sysparm_query=active=true&sysparm_view=gene_view_name&sysparm_view_forced=true&sysparm_query=u_query_type=gene_sys_id_record_producer
	- [ ] Type: Answer
- [ ] Create view rule
	- [ ] Name : gene_query_name
	- [ ] Active : checked
	- [ ] Match conditions: All
	- [ ] Device type : Browser 
	- [ ] Table : gene_table_name
	- [ ] View : gene_view_name
	- [ ] Application: gene_application_name
	- [ ] Conditions : 
		- [ ] Query type is : gene_query_name
- [ ] Assignment rule handling for the above record producer 
	- [ ] Assign after creation automatically to group : gene_assignment_group
- [ ] Create new rule in x_4dai_omgt_mbos_dealer_query_overseas_lookup_rules
	- [ ] Query type : gene_query_name
	- [ ] Priority : gene_priority
	- [ ] Urgency : gene_urgency
- [ ] UI policy : gene_ui_policies



### Update Set

CSM_gene_feature_number_gene_story_number_gene_update_set_description_gene_user_name_gene_update_set_version