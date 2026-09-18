# Copyright 2017 LasLabs Inc.
# Copyright 2018 ACSONE SA/NV.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Recurring - Product Contract",
    "version": "15.0.1.1.1",
    "category": "Contract Management",
    "license": "AGPL-3",
    "author": "LasLabs, " "ACSONE SA/NV, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/contract",
    "depends": ["product", "contract", "sale"],
    "data": [
        "views/res_config_settings.xml",
        "views/contract.xml",
        "views/product_template.xml",
        "views/sale_order.xml",
    ],
    "installable": True,
    "application": False,
    # "dateutil" isn't a real PyPI distribution name (404) -- the import
    # name is dateutil but the package is python-dateutil. A build/
    # upgrade's combined pip install for every discovered module's
    # declared deps hard-fails on the first bad name and falls back to
    # installing every dependency one at a time, which can silently drop
    # another module's own exact-pinned dependency to whatever a later,
    # unrelated, unpinned package happens to pull in transitively instead.
    "external_dependencies": {"python": ["python-dateutil"]},
    "maintainers": ["sbejaoui"],
}
