gene_query_name = 'CRM+ / Salesforce Query'
gene_view_name = 'crm_salesforce_query'
gene_description = '''General query related to the use of CRM+/Salesforce

Note: general requests for access must go via the IT Service Desk.'''
gene_short_description = 'General query related to the use of CRM+/Salesforce'
gene_category = 'General Marketing ( Marketing ( Mercedes-Benz Cars ) )'
gene_assignment_group = 'MBAuP PC Marketing Team AU'
gene_priority = 'Moderate'
gene_urgency = 'Medium'
gene_variables = '''
		- [ ] Additional Details -> mandatory
		- [ ] Attachment: not mandatory'''
gene_variable_sets = '''
		- [ ] Generic OMGT-AU Case Variables
		- [ ] OMGT-Overseas Additional details'''
gene_add_variables_form = '''
			- [ ] Additional Details -> mandatory
			- [ ] Attachment: not mandatory'''
gene_user_criteria = '''
		- [ ] Australia - Dealer - CRM Coordinator Cars
		- [ ] Australia - Dealer - CRM Manager Cars
		- [ ] Australia - Dealer - Marketing Coordinator Cars
		- [ ] Australia - Dealer - Lead Manager Cars
		- [ ] Australia - Dealer - Lead Consultant Cars 
		- [ ] Australia - Dealer - General Sales Manager Cars
		- [ ] Australia - Dealer - Marketing Manager Cars
		- [ ] Australia - Dealer - New Vehicle Sales Manager Cars'''
gene_ui_policies = ''
gene_add_fields_to_table = ''
gene_story_number = 'SFSTRY0006341'
gene_update_set_description = 'CRMSalesforceQuery' # Max length : 37



gene_application_name = 'Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]'
gene_table_name = 'x_4dai_omgt_mbos_au_case'
gene_table_display_name = 'Order Management Case Australia [' + gene_table_name + ']'
gene_owner = 'Leonid Khaylov'
gene_catalog_name = 'Customer Service'
gene_feature_number = 'SFFEAT0002173'
gene_user_name = 'DTAFTAD'
gene_update_set_version = 'v1'

input_filename = 'Templates/Create Query.md'
output_filename = 'Create Query Generated.md'

variables = {
    'gene_add_fields_to_table' : gene_add_fields_to_table,
    'gene_application_name' : gene_application_name,
    'gene_assignment_group' : gene_assignment_group,
    'gene_catalog_name' : gene_catalog_name,
    'gene_category' : gene_category,
    'gene_description' : gene_description,
    'gene_feature_number' : gene_feature_number,
    'gene_owner' : gene_owner,
    'gene_priority' : gene_priority,
    'gene_query_name' : gene_query_name,
    'gene_short_description' : gene_short_description,
    'gene_story_number' : gene_story_number,
    'gene_table_name' : gene_table_name,
    'gene_table_display_name' : gene_table_display_name,
    'gene_ui_policies' : gene_ui_policies,
    'gene_update_set_description' : gene_update_set_description,
    'gene_update_set_version' : gene_update_set_version,
    'gene_urgency' : gene_urgency,
    'gene_user_criteria' : gene_user_criteria,
    'gene_user_name' : gene_user_name,
    'gene_variables' : gene_variables,
    'gene_add_variables_form' : gene_add_variables_form,
    'gene_variable_sets' : gene_variable_sets,
    'gene_view_name' : gene_view_name
}

input_file = open(input_filename, "rt")
output_file = open(output_filename, "wt")

for line in input_file:
    for variable in variables:
        line = line.replace(variable, variables[variable])
    output_file.write(line)

input_file.close()
output_file.close()