# -*- coding: utf-8 -*-

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('North', 'North'), ('South', 'Sount'), ('East', 'East'), ('West', 'West')])
    active = fields.Boolean(default=False)
    state = fields.Selection(
         required=True,
         copy=False,
         selection=[('New', 'New'), ('Offer Received', 'Offer Recieved'), ('Offer Accepted', 'Offer Accepted'), ('Sold', 'Sold'), ('Canceled','Canceled')],
         default='New')