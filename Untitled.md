```javascript
// imac_ml_pc_or_laptop mrvs
var mrvs_imac_ml_pc_or_laptop = gr.variables.imac_ml_pc_or_laptop;

rowCount = mrvs_imac_ml_pc_or_laptop.getRowCount();
var mrvs_imac_ml_pc_or_laptop_data = [];

for(var i =0; i < rowCount; i++){
	mrvs_imac_ml_monitor.push({
		"ref_device_monitor": mrvs_imac_ml_monitor_data.getRow(i).ref_device_monitor,
		"ref_monitor": mrvs_imac_ml_monitor_data.getRow(i).ref_monitor,
		"sel_quantity_monitor": mrvs_imac_ml_monitor_data.getRow(i).sel_quantity_monitor,
		"sel_delivery_monitor": mrvs_imac_ml_monitor_data.getRow(i).sel_delivery_monitor,
	});
}
```

imac_ml_pc_or_laptop


[ServiceNow Flow Designer for Catalog Items](https://meatsac.github.io/servicenow-flow-designer-for-catalog-items/) -- Flow stage