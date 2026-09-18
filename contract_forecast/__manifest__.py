# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Contract Forecast",
    "summary": """
    Contract forecast""",
    "version": "16.0.1.1.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/contract",
    "depends": ["base", "account", "contract", "queue_job"],
    "data": [
        "data/queue_job_channel.xml",
        "data/queue_job_functions.xml",
        "security/contract_line_forecast_period.xml",
        "views/res_config_settings.xml",
        "views/contract_line_forecast_period.xml",
        "views/contract.xml",
    ],
    # Real PyPI distribution name is python-dateutil, not the bare import
    # name -- same fix already applied to product_contract's own manifest
    # on the 15.0 branch; verified live this module (contract_forecast, a
    # sibling in the same OCA/contract repo) still has the bug upstream at
    # 16.0, "ERROR: Could not find a version that satisfies the requirement
    # dateutil (from versions: none)" failing the whole combined pip
    # install and forcing this platform's own per-package fallback loop,
    # which has no cross-package version-pin coordination at all.
    "external_dependencies": {"python": ["python-dateutil"]},
    "post_init_hook": "post_init_hook",
}
