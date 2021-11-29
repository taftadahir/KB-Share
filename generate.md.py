gene_query_name = 'Star Rewards Results - Vans'
gene_view_name = 'star_rewards_results_vans'
gene_description = 'Clarification of ranking or points allocation in Star Rewards'
gene_short_description = 'Clarification of ranking or points allocation in Star Rewards'
gene_category = '(Vans) -> Retail Sales'
gene_assignment_group = 'MBAuP Retail Sales Vans AU'
gene_priority = 'Critical'
gene_urgency = 'Medium'
gene_variables = ''
gene_variable_sets = '''
		- [ ] Generic OMGT-AU Case Variables'''
gene_add_variables_form = ''
gene_user_criteria = '''
		- [ ] Australia - Dealer - General Manager Vans Australia
		- [ ] Australia - Dealer - Director Vans
		- [ ] Australia - Dealer - Branch General Manager Vans
		- [ ] Australia - Dealer - General Sales Manager Vans Australia
		- [ ] Australia - Dealer - Stock Controller Vans
		- [ ] Australia - Dealer - Dealer Principal Vans Australia
		- [ ] Australia - Dealer - Sales Manager Vans'''
gene_ui_policies = '''
    - [ ] Additional detail : Mandatory'''
gene_add_fields_to_table = ''
gene_story_number = 'SFSTRY0005424'
gene_update_set_description = 'StarRewardsResultsVans' # Max length : 37



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