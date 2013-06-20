# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Product Type",
    "version": "0.1",
    "depends": ["account", "procurement"],
    "author": "Smile",
    "description": """
    This module aims to facilitate product creation by using product type
    with accounting and procurement configuration.

    This module built and test on OpenERP v7.0.

    Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
    """,
    "website": "http://www.smile.fr",
    "category": 'Sales Management',
    "sequence": 20,
    "init_xml": [
        "security/ir.model.access.csv",
    ],
    "update_xml": [
        "view/product_view.xml",
    ],
    'demo_xml': [],
    'test': [],
    "auto_install": False,
    "installable": True,
    "application": True,
}