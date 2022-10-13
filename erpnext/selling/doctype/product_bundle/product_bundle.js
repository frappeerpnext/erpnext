// Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Product Bundle", {
	refresh: function (frm) {
		// frm.toggle_enable("new_item_code", frm.is_new());
		// frm.set_query("new_item_code", () => {
		// 	return {
		// 		query: "erpnext.selling.doctype.product_bundle.product_bundle.get_new_item_code",
		// 	};
		// });
	},
});

frappe.ui.form.on("Product Bundle Item", {

	qty(frm,cdt, cdn) {
		let doc=   locals[cdt][cdn];
		doc.total_cost=doc.qty*doc.cost;
		doc.total_rate=doc.qty*doc.rate;
	    frm.refresh_field('items');
		updateSumTotal(frm);
	},
	cost(frm,cdt, cdn) {
		let doc=   locals[cdt][cdn];
		doc.total_cost=doc.qty*doc.cost;
		doc.total_rate=doc.qty*doc.rate;
	    frm.refresh_field('items');
		updateSumTotal(frm);
	},
});

function updateSumTotal(frm) {
    let total_amount = 0;
	let total_qty = 0;
	let total_cost = 0;

    $.each(frm.doc.items, function(i, d) {
        total_amount += flt(d.total_rate);
		total_qty +=flt(d.qty);
		total_cost += flt(d.total_cost)
    });
	
 
    frm.set_value('total_amount', total_amount);
    frm.set_value('total_quantity', total_qty);
    frm.set_value('total_cost', total_cost);
	 
	frm.refresh_field("total_amount");
	frm.refresh_field("total_quantity");
	frm.refresh_field("total_cost");
}
