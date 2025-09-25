# Payroll Run Totals — Odoo 18 (OPL-1)

**Turn payroll batches into instant KPIs.** This app adds a stored **Net Total** directly on *Payslip Batches* (`hr.payslip.run`) so HR and finance teams can see the overall payout at a glance — in the list view and on each batch form.

## Why you’ll love it
- **1-click visibility**: no more opening each payslip or exporting to Excel. The **Total Net** is right on the batch.
- **Auto-recompute**: totals update automatically when payslips/lines change.
- **Zero friction**: works out of the box with Odoo’s standard payroll (`hr_payroll`). Community & Enterprise friendly.
- **Configurable**: choose which line codes count as “Net” via a system parameter.

## Features
- Field **Total Net of Batch** on `hr.payslip.run` (monetary, stored).
- Recomputes when:
  - payslip **state** changes,
  - payslip **lines** totals or **codes** change.
- Default **net codes**: `NET`, `NETAPAYER`.
- **Fallback**: if no code matches, any line in **category `NET`** is included.
- **Parameter**: `payroll_run_totals.net_codes` (comma-separated) to override which codes are considered as “Net”.

## Screens (what you’ll see)
- **List view** of batches: new column “Total Net”.
- **Form view** of a batch: “Totals” section with “Total Net”.

*(Add your own screenshots when publishing on Odoo Apps: list & form of batches, plus the system parameter page.)*

## Installation
1. Install the app from Odoo Apps or copy into your `addons_path` and update Apps list.
2. Install **Payroll Run Totals**.
3. (Optional) Set the parameter in *Settings → Technical → Parameters → System Parameters*:
   - **Key**: `payroll_run_totals.net_codes`
   - **Value**: `NET,NETAPAYER` (or your own codes)

## Compatibility
- **Odoo 18.0** (Community & Enterprise)
- Depends on **hr_payroll** only

## FAQ
**Q. My Net line code is different.**  
A. Set `payroll_run_totals.net_codes` to your codes (comma-separated). The app will also fall back to the line **category** code `NET` if present.

**Q. Can I also show Gross or Employer Cost totals?**  
A. Yes — contact us; we can extend the module to add **Total Gross** and **Employer Cost**.

**Support & contact**
- Email: support@example.com
- GitHub (issues): https://github.com/your-user/odoo-payroll-run-totals/issues

## License
This app is distributed under **OPL-1** (Odoo Proprietary License). One license per production database.
