# -*- coding: utf-8 -*-
##############################################################################
#
#    This module copyright :
#        (c) 2015 VMCloud Solution (http://vmcloudsolution.pe)
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

from datetime import datetime
from openerp import models, api, fields, exceptions


class PosboxProxyBackend(models.Model):
    _name = 'posbox.proxy.backend'

    name = fields.Char(string='Name', select=1, required=True)
    value_ip = fields.Char(string='Value IP', help='The hostname or ip address of the hardware proxy', size=45)

    @api.model
    def set_value_space(self, value, space=7, align='right'):
        if align == 'left':
            val_str = str(value) + ' ' * space
            result = val_str[:space]
        else:
            val_str = ' ' * space + str(value)
            result = val_str[-space:]
        return result

    @api.model
    def get_date_formats(self):
        lang = self._context.get('res.users').lang
        res_lang = self._context.get('res.lang')
        lang_params = {}
        if lang:
            ids = res_lang.search([("code", "=", lang)])
            if ids:
                lang_params = res_lang.read(ids[0], ["date_format", "time_format"])
        format_date = lang_params.get("date_format", '%m/%d/%Y').encode('utf-8')
        format_time = lang_params.get("time_format", '%H:%M:%S').encode('utf-8')
        return format_date, format_time
