#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:06:53 2020

@author: atharva
"""


from MySqlBackendConnector import mysqlbackend

connector= mysqlbackend('hackathon', 'dbda', 'dbda')

connector.top_4_field()

connector.total_summary()

connector.top_ten_economy()

connector.top_nrr_team()

connector.top_april_team()
