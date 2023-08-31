###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################

__version__ = '0.1.dev'

import json
import os


THISDIR = os.path.dirname(os.path.realpath(__file__))

def load_template(template_name):
    template_file =  f"{THISDIR}{os.sep}resources{os.sep}{template_name}.json"
    if os.path.isfile(template_file):
        with open(template_file,'r') as fh :
            template = json.load(fh)
    else:
        template = None
    return template


def get_version():
    return __version__