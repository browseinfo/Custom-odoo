# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Browseinfo
#    Copyright (C) 2004-2010.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Custom Odoo',
    'version': '1.1',
    'author': 'Browseinfo',
    'description': "Remove odoo's defaults link.",
    'website': 'https://www.browseinfo.in',
    'depends': ['base','website','web'],
    'data': [
        'views/custom_link_rm.xml',
    ],
    'qweb': [
        'static/src/xml/custom_link_remove.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: