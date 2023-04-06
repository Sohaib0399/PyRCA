#
# Copyright (c) 2023 salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#
from pyrca.tools.dashboard.dashboard import app

if __name__ == "__main__":
    app.run_server(debug=False)
