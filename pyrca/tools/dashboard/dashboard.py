#
# Copyright (c) 2022 salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from .utils.layout import create_banner, create_layout
from .pages.data import create_data_layout

from .callbacks import data


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Merlion Dashboard",
)
app.config["suppress_callback_exceptions"] = True
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content"),
    dcc.Store(id="data-state"),
])
server = app.server


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def _display_page(pathname):
    return html.Div(
        id="app-container",
        children=[
            create_banner(app),
            html.Br(),
            create_layout()
        ],
    )


@app.callback(
    Output("plots", "children"),
    Input("tabs", "value"),
    [
        State("data-state", "data"),
    ]
)
def _click_tab(
        tab,
        data_state,
):
    if tab == "file-manager":
        return create_data_layout()
    else:
        return create_data_layout()