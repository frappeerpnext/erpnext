from frappe import _


def get_data():
	return {
		"fieldname": "bom_no",
		"non_standard_fieldnames": {
			"Item": "default_bom",
			"Purchase Order": "bom",
			"Purchase Receipt": "bom",
			"Purchase Invoice": "bom",
		},
		"transactions": [
			{"label": _("Stock"), "items": ["Item", "Stock Entry"]},
			{
				"label": _("Subcontract"),
				"items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"],
			},
		],
		"disable_create_buttons": [
			"Item",
			"Purchase Order",
			"Purchase Receipt",
			"Purchase Invoice",
			"Stock Entry",
			"BOM",
		],
	}
