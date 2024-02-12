# Copyright (c) 2023, Tes Pheakdey and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	
	return get_columns(filters), get_data(filters)

def get_columns(filters):
	columns=[]
	columns.append({'fieldname':"parent",'label':"Invoice",'fieldtype':'Link','options':'Purchase Invoice','align':'left','width':200})
	columns.append({'fieldname':"purchase_receipt",'label':"Purchase Receipt",'align':'left','width':200})
	columns.append({'fieldname':"item",'label':"Item Code",'fieldtype':'Data','align':'left','width':200})
	columns.append({'fieldname':"description",'label':"Description",'fieldtype':'Data','align':'left','width':200})
	columns.append({'fieldname':"posting_date",'label':"Date",'fieldtype':'Date','align':'left','width':120})
	columns.append({'fieldname':"brand",'label':"Brand",'fieldtype':'Data','align':'left','width':200})
	columns.append({'fieldname':"item_group",'label':"Item Group",'fieldtype':'Data','align':'left','width':200})
	columns.append({'fieldname':"qty",'label':"Qty",'fieldtype':'Float','align':'center','width':90})
	columns.append({'fieldname':"price_list_rate",'label':"Price",'fieldtype':'Curreny','align':'right','width':120})
	columns.append({'fieldname':"uom",'label':"UOM",'fieldtype':'Data','align':'center','width':90})
	columns.append({'fieldname':"amount",'label':"Amount",'fieldtype':'Currency','align':'center','width':120})
	columns.append({'fieldname':"discount_amount",'label':"Discount Amount",'fieldtype':'Currency','right':'center','width':120})
	columns.append({'fieldname':"supplier",'label':"Supplier",'fieldtype':'Data','align':'left','width':200})
	
	return columns

def get_data(filters):
	data = []
	sql = """
			select 
				parent,
				a.purchase_receipt,
				CONCAT(item_code,":",item_name) as item,
				description,
				b.posting_date,
				brand,
				item_group,
				qty,
				price_list_rate,
				uom,
				amount,
				a.discount_amount,
				b.supplier
			from `tabPurchase Invoice Item` a
			inner join `tabPurchase Invoice` b on a.parent = b.name
			{}
			order by b.posting_date
	""".format(get_conditions(filters))
	data = frappe.db.sql(sql,filters,as_dict=1)
	return data

def get_conditions(filters):
	select_filters=[]
	select_filters.append("b.docstatus = 1")
	if filters.get('start_date') and filters.get('end_date'):
		select_filters.append("b.posting_date between %(start_date)s and %(end_date)s")
	if filters.get('supplier'):
		select_filters.append("b.supplier in %(supplier)s")

	if len(select_filters) > 0:
		return " WHERE " + " AND ".join(select_filters)
	else:
		return ''