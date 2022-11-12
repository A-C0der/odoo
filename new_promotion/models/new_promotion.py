from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CouponNewRuless(models.Model):
    _inherit = 'coupon.program'
    _description = "New Promotion Rules"
    rule_maximum_amount = fields.Float(default=0.0, help="Maximum required amount to get the reward",String="Maximum Amount")