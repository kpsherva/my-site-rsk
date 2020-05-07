# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Blueprint used for loading templates.

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""

from __future__ import absolute_import, print_function

from flask import Blueprint, url_for
from flask import render_template
from flask_webpackext import current_manifest

blueprint = Blueprint(
    'my_site',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route('/wild-search')
def my_record_search():
    # import ipdb
    # ipdb.set_trace()
    config = {"searchID": "react-searchkit",
              "special": "second-kit",
              "overwriteMap": "my_searchkit/overwriteMap",
              }
    return render_template('my_site/wild_search.html', data=config)

