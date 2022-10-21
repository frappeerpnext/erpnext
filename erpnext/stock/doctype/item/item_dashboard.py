from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _("This is based on stock movement. See {0} for details").format(
			'<a href="#query-report/Stock Ledger">' + _("Stock Ledger") + "</a>"
		),
		"fieldname": "item_code",
		"non_standard_fieldnames": {
			"Work Order": "production_item",
			"Product Bundle": "new_item_code",
			"BOM": "item",
			"Batch": "item",
		},
		"transactions": [
			{"label": _("Groups"), "items": ["BOM", "Product Bundle"]},
			{"label": _("Pricing"), "items": ["Item Price"]},
			{"label": _("Sell"), "items": ["Quotation", "Sales Order", "Delivery Note", "Sales Invoice"]},
			{
				"label": _("Buy"),
				"items": [
					"Material Request",
					"Supplier Quotation",
					"Request for Quotation",
					"Purchase Order",
					"Purchase Receipt",
					"Purchase Invoice",
				],
			},
			{"label": _("Stock Movement"), "items": ["Stock Entry", "Stock Reconciliation"]}
		],
	}
