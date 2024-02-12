// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase Invoice Item"] = {
	onload: function(report) {
		report.page.add_inner_button ("Preview Report", function () {
			frappe.query_report.refresh();
		});
		
	},
	"filters": [
		{
			"fieldname": "start_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"width": "80",
			on_change: function (query_report) {},
			"reqd": 1
		},
		{
			"fieldname": "end_date",
			"label": __("End Date"),
			"fieldtype": "Date",
			"width": "80",
			on_change: function (query_report) {},
			"reqd": 1
		},
		{
			fieldname: "supplier",
			label: "Supplier",
			"fieldtype": "MultiSelectList",
			on_change: function (query_report) {},
			"reqd": 1,
			get_data: function(txt) {
				return frappe.db.get_link_options('Supplier', txt);
			}
		},
	]
};
