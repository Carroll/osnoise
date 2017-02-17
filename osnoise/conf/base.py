# Copyright 2016 Orange
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_config import cfg


base_options = [
    cfg.StrOpt(
        'log_file_name',
        default='osnoise.log',
        help='Osnoise file name.'),
    cfg.StrOpt(
        'log_dir',
        default='/var/log/osnoise/',
        help='Osnoise log directory.'),
    cfg.StrOpt(
        'log_level',
        default='info',
        help='Log level.'),

    cfg.StrOpt(
        'log_file',
        default='/var/log/osnoise/osnoise.log',
        help='Log file'),

    cfg.IntOpt(
        'log_maxBytes',
        default=1000000,
        #min=1000,
        help='Log level.'),
    cfg.IntOpt(
        'log_backupCount',
        default=5,
        #min=1,
        help='Log level.'),
    cfg.BoolOpt('log_config_append',
                default=False,
                deprecated_group='DEFAULT',
                help='To append logs to existent log file or not.'),

]


def register_opts(conf):
    conf.register_opts(base_options)

def list_opts():
    return {'DEFAULT' : base_options}
