### Implementation
- [ ] Create a record producer
	- [ ] Application : Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]
	- [ ] For table : Order Management Case Australia [x_4dai_omgt_mbos_au_case] 
	- [ ] Name: CRM+ / Salesforce Query
	- [ ] Short description: General query related to the use of CRM+/Salesforce
	- [ ] Description: General query related to the use of CRM+/Salesforce

	Note: general requests for access must go via the IT Service Desk.
	- [ ] Owner: Leonid Khaylov
	- [ ] Apply variable set : 
		- [ ] Generic OMGT-AU Case Variables
		- [ ] OMGT-Overseas Additional details
	- [ ] Create variables : 
		- [ ] Additional Details -> mandatory
		- [ ] Attachment: not mandatory
	- [ ] Add picture
		- [ ] Icon
		- [ ] Picture
	- [ ] Catalog : Customer Service
	- [ ] Put the catalog item/record producer under the sub category : General Marketing ( Marketing ( Mercedes-Benz Cars ) )
	- [ ] Available For : 
		- [ ] Australia - Dealer - CRM Coordinator Cars
		- [ ] Australia - Dealer - CRM Manager Cars
		- [ ] Australia - Dealer - Marketing Coordinator Cars
		- [ ] Australia - Dealer - Lead Manager Cars
		- [ ] Australia - Dealer - Lead Consultant Cars 
		- [ ] Australia - Dealer - General Sales Manager Cars
		- [ ] Australia - Dealer - Marketing Manager Cars
		- [ ] Australia - Dealer - New Vehicle Sales Manager Cars
	- [ ] Script 
		- [ ] Mapping
			- [ ] Short description: CRM+ / Salesforce Query
			- [ ] Query type : record producer sys_id

```javascript
// Mapping
current.short_description = "CRM+ / Salesforce Query";
current.u_query_type = cat_item.sys_id;
```


- [ ] Create and configure form and view
	- [ ] create view
		- [ ] View name : crm_salesforce_query
		- [ ] Title : CRM+ / Salesforce Query
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
			- [ ] Additional Details -> mandatory
			- [ ] Attachment: not mandatory
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
	- [ ] Name: CRM+ / Salesforce Query
	- [ ] Order: 100
	- [ ] Active: checked
	- [ ] User Prompt: CRM+ / Salesforce Query
	- [ ] Target url : x_4dai_omgt_mbos_au_case.do?sysparm_query=active=true&sysparm_view=crm_salesforce_query&sysparm_view_forced=true&sysparm_query=u_query_type=gene_sys_id_record_producer
	- [ ] Type: Answer
- [ ] Create view rule
	- [ ] Name : CRM+ / Salesforce Query
	- [ ] Active : checked
	- [ ] Match conditions: All
	- [ ] Device type : Browser 
	- [ ] Table : x_4dai_omgt_mbos_au_case
	- [ ] View : crm_salesforce_query
	- [ ] Application: Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]
	- [ ] Conditions : 
		- [ ] Query type is : CRM+ / Salesforce Query
- [ ] Assignment rule handling for the above record producer 
	- [ ] Assign after creation automatically to group : MBAuP PC Marketing Team AU
- [ ] Create new rule in x_4dai_omgt_mbos_dealer_query_overseas_lookup_rules
	- [ ] Query type : CRM+ / Salesforce Query
	- [ ] Priority : Moderate
	- [ ] Urgency : Medium
- [ ] UI policy : 



### Update Set

CSM_SFFEAT0002173_SFSTRY0006341_CRMSalesforceQuery_DTAFTAD_v1