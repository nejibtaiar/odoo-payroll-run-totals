
# -*- coding: utf-8 -*-
from odoo import api, fields, models

def _get_net_codes(env):
    """Read optional system parameter payroll_run_totals.net_codes (comma-separated).
    Fallback to default ('NET','NETAPAYER').
    """
    param = env["ir.config_parameter"].sudo().get_param("payroll_run_totals.net_codes")
    if not param:
        return ("NET", "NETAPAYER")
    codes = [c.strip() for c in param.split(",") if c.strip()]
    return tuple(codes) if codes else ("NET", "NETAPAYER")


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    total_net = fields.Monetary(
        string="Total Net of Batch",
        currency_field="currency_id",
        compute="_compute_total_net",
        store=True,
        readonly=True,
        help="Sum of Net lines across all payslips in this batch. "
             "Codes considered: system parameter 'payroll_run_totals.net_codes' (default: NET, NETAPAYER). "
             "Falls back to lines in category 'NET' if no code match."
    )

    @api.depends(
        "slip_ids.state",
        "slip_ids.line_ids.total",
        "slip_ids.line_ids.code",
        "slip_ids.line_ids.category_id.code",
    )
    def _compute_total_net(self):
        net_codes = _get_net_codes(self.env)
        for run in self:
            total = 0.0
            for slip in run.slip_ids:
                lines = slip.line_ids.filtered(lambda l: l.code in net_codes)
                if not lines:
                    lines = slip.line_ids.filtered(lambda l: l.category_id and l.category_id.code == "NET")
                total += sum(lines.mapped("total")) if lines else 0.0
            run.total_net = total
