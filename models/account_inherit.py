# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def get_journal(self):
        lst = []
        for ids in self:
            if ids.journal_id:
                lst.append(ids.journal_id.id)
        lst = list(set(lst))
        return lst

    # def get_payment_type(self):
    #     lst = []
    #     lst1 = []
    #     for ids in self:
    #         if ids.payment_type == 'outbound':
    #             lst.append(ids.id)
    #         else:
    #             lst1.append(ids.id)
    #     lst = list(set(lst))
    #     lst1 = list(set(lst))
    #     return lst, lst1

