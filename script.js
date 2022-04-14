//Récupérer les SLAs dans la table Task SLA qui sont en cours alors que la tâche associée est terminée
var gr = new GlideRecord('task_sla')
var ScTask = 'schedule=8dffd6a9dbf8cf805fe8f5b31d961920'
// filter "schedule = SC_UOI_2" on [task_sla] table
gr.addEncodedQuery(ScTask)
gr.query()
var sla = new SLARepair()
while (gr.next()) {
  // gs.log("Repaired Records in [task_sla] table with schedule SC_UOI_2 : " + gr.task.number);
  var sysId = gr.getValue('sys_id')
  sla.repairBySysId(sysId, 'task_sla')
}
