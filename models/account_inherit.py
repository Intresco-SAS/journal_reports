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
        print(lst)
        return lst

    def get_records(self, journal_id):
        data_list = []
        # income = 0
        # expenses = 0
        for rec in self:
            if rec.journal_id.id == journal_id:
                if rec.payment_type == 'outbound':
                    # expenses += rec.amount
                    vals = {
                        'name': rec.name,
                        'payment_date': rec.payment_date,
                        'type': 'outbound',
                        'amount': rec.amount,
                        'ref': rec.communication,
                        'destination_account_id': self.get_total(rec.destination_account_id.id),
                    }
                    data_list.append(vals)

        for rec in self:
            if rec.journal_id.id == journal_id:
                if rec.payment_type == 'inbound':
                    # income += rec.amount
                    vals = {
                        'name': rec.name,
                        'payment_date': rec.payment_date,
                        'type': 'inbound',
                        'amount': rec.amount,
                        'ref': rec.communication,
                        'destination_account_id': self.get_total(rec.destination_account_id.id),
                    }
                    data_list.append(vals)

        return data_list

    def get_total(self, vals):
        total = 0
        data = self.env['account.move.line'].search([('account_id', '=', vals)])
        for rec in data:
            total += rec.balance
        return total

    def get_journal_name(self, val):
        return self.env['account.journal'].search([('id', '=', val)]).name



