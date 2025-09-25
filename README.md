
# Payroll Run Totals (Odoo 18, OPL-1)

Adds a **Total Net** monetary field on payslip batches (`hr.payslip.run`).  
The field is **stored** and **auto-recomputed** whenever payslips/lines change.

## How it works
- Sums lines whose **code** is in `NET, NETAPAYER` (default).
- If no such code exists on a payslip, it **falls back** to lines where the **category** code is `NET`.
- Controlled by system parameter `payroll_run_totals.net_codes` (comma-separated).

## Installation
1. Copy this module into your addons path.
2. Update Apps list and install **Payroll Run Totals**.
3. (Optional) Set the parameter in *Settings > Technical > Parameters > System Parameters*:
   - Key: `payroll_run_totals.net_codes`
   - Value example: `NET,NETAPAYER`

## Usage
- Go to **Payroll > Payslip Batches** and open a batch to see **Total Net of Batch**.
- Recompute payslips as usual; the batch total follows automatically.

## Compatibility
- Odoo **18.0** (Community & Enterprise)
- Depends only on **hr_payroll**

## License
**OPL-1**. See `LICENSE`.
