### Implementation
- [ ] Create a record producer
	- [ ] Application : Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]
	- [ ] For table : Order Management Case Australia [x_4dai_omgt_mbos_au_case] 
	- [ ] Name: General Query - Master Data
	- [ ] Short description: General query related to Master Data.
	- [ ] Description: General query related to Master Data.
	- [ ] Owner: Leonid Khaylov
	- [ ] Apply variable set : 
		- [ ] Generic OMGT-AU Case Variables
	- [ ] Create variables : 
		- [ ] Enquiry description: *Free text*- mandatory
	- [ ] Add picture
		- [ ] Icon
		- [ ] Picture
	- [ ] Catalog : Customer Service
	- [ ] Put the catalog item/record producer under the sub category : "Master Data" (Finance/ "Mercedes-Benz Cars AU")
	- [ ] Available For : 
		- [ ] Australia - Dealer - Branch General Manager Cars
		- [ ] Australia - Dealer - Certified Pre-Owned Sales Consultant Cars
		- [ ] Australian - Dealer - Certified Pre-Owned Sales Manager Cars
		- [ ] Australian - Dealer - Corporate Sales Consultant Cars
		- [ ] Australian - Dealer - Corporate Sales Manager Cars
		- [ ] Australian - Dealer - Dealer Principal Cars
		- [ ] Australian - Dealer - Fleet Sales Consultant Cars
		- [ ] Australian - Dealer - General Sales Manager Cars
		- [ ] Australian - Dealer - New Vehicle Sales Consultant - EQ Specialist Cars
		- [ ] Australian - Dealer - New Vehicle Sales Consultant Cars
		- [ ] Australian - Dealer - New Vehicle Sales Manager Cars
		- [ ] Australian - Dealer - Retail Floor Manager Cars
		- [ ] Australian - Dealer - Sales Consultant - AMG Specialist Cars
		- [ ] Australian - Dealer - Sales Operations Manager Cars
		- [ ] Australian - Dealer - Sales Consultant - AMG Specialist Cars
		- [ ] Australian - Dealer - Backup EQ coordinator
		- [ ] Australian - Dealer - EQ coordinator
		- [ ] Australian - Dealer - General Manager Cars
		- [ ] Australian - Dealer - Sales Cadet Cars
	- [ ] Script 
		- [ ] Mapping
			- [ ] Short description: General Query - Master Data
			- [ ] Query type : record producer sys_id

```javascript
// Mapping
current.short_description = "General Query - Master Data";
current.u_query_type = cat_item.sys_id;
```


- [ ] Create and configure form and view
	- [ ] create view
		- [ ] View name : general_query_master_data
		- [ ] Title : General Query - Master Data
	- [ ] Add fields to table : 
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
		- [ ] Add variables : 
			- [ ] Enquiry description
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
	- [ ] Name: General Query - Master Data
	- [ ] Order: 100
	- [ ] Active: checked
	- [ ] User Prompt: General Query - Master Data
	- [ ] Target url : x_4dai_omgt_mbos_au_case.do?sysparm_query=active=true&sysparm_view=general_query_master_data&sysparm_view_forced=true&sysparm_query=u_query_type=gene_sys_id_record_producer
	- [ ] Type: Answer
- [ ] Create view rule
	- [ ] Name : General Query - Master Data
	- [ ] Active : checked
	- [ ] Match conditions: All
	- [ ] Device type : Browser 
	- [ ] Table : x_4dai_omgt_mbos_au_case
	- [ ] View : general_query_master_data
	- [ ] Application: Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]
	- [ ] Conditions : 
		- [ ] Query type is : General Query - Master Data
- [ ] Assignment rule handling for the above record producer 
	- [ ] Assign after creation automatically to group : "MBAuP Master Data AU"
- [ ] Create new rule in x_4dai_omgt_mbos_dealer_query_overseas_lookup_rules
	- [ ] Query type : General Query - Master Data
	- [ ] Priority : Critical
	- [ ] Urgency : High
- [ ] UI policy : 
    - [ ] Enquiry Description: Mandatory



### Update Set

CSM_SFFEAT0001986_SFSTRY0005918_GeneralQueryMasterData_DTAFTAD_v1