gene_query_name = 'General Query - Master Data'
gene_view_name = 'general_query_master_data'
gene_description = 'General query related to Master Data.'
gene_short_description = 'General query related to Master Data.'
gene_category = '"Master Data" (Finance/ "Mercedes-Benz Cars AU")'
gene_assignment_group = '"MBAuP Master Data AU"'
gene_priority = 'Critical'
gene_urgency = 'High'
gene_variables = '''
		- [ ] Enquiry description: *Free text*- mandatory'''
gene_variable_sets = '''
		- [ ] Generic OMGT-AU Case Variables'''
gene_add_variables_form = '''
			- [ ] Enquiry description'''
gene_user_criteria = '''
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
		- [ ] Australian - Dealer - General Manager Cars
		- [ ] Australian - Dealer - Sales Cadet Cars'''
gene_ui_policies = '''
    - [ ] Enquiry Description: Mandatory'''
gene_add_fields_to_table = ''
gene_story_number = 'SFSTRY0005918'
gene_update_set_description = 'GeneralQueryMasterData' # Max length : 37



gene_application_name = 'Mercedes-Benz Dealer Query Management Overseas [x_4dai_omgt_mbos]'
gene_table_name = 'x_4dai_omgt_mbos_au_case'
gene_table_display_name = 'Order Management Case Australia [' + gene_table_name + ']'
gene_owner = 'Leonid Khaylov'
gene_catalog_name = 'Customer Service'
gene_feature_number = 'SFFEAT0001986'
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