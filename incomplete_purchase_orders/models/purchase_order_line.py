from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line'

    received_quantity_is_less_than_requested = fields.Boolean(compute='_compute_received_quantity_is_less_than_requested',
                                                              store=True)

    @api.depends('qty_received', 'product_qty')
    def _compute_received_quantity_is_less_than_requested(self):
        for record in self:
            record.received_quantity_is_less_than_requested = record.qty_received < record.product_qty
