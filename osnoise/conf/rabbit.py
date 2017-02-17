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

# Full list can be found at oslo_messaging/_drivers/impl_rabbit.py
rabbitmq_section = cfg.OptGroup('rabbit_conf',
                                title='RabbitMQ options',
                                help='Configuration section of RabbitMQ.')


rabbit_options = [
    #rabbit config
    cfg.StrOpt('rabbit_transport',
               default='amqp://guest:guest@localhost:5672//',
               help='The RabbitMQ transport URL.'),
    #deprecated options in oslo_messaging
    cfg.StrOpt('rabbit_host',
               default='localhost',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               #deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ broker address where a single node is '
                    'used.'),
#    cfg.PortOpt('rabbit_port',
    cfg.StrOpt('rabbit_port',
                default=5672,
                deprecated_group='DEFAULT',
                deprecated_for_removal=True,
                #deprecated_reason="Replaced by [DEFAULT]/transport_url",
                help='The RabbitMQ broker port where a single node is used.'),
    cfg.StrOpt('rabbit_virtual_host',
               default='/',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               #deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ virtual host.'),
    cfg.StrOpt('rabbit_userid',
               default='guest',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               #deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ userid.'),
    cfg.StrOpt('rabbit_password',
               default='guest',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               #deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ password.',
               secret=True),
    #pika config
    cfg.IntOpt('pika_channel_max',
               default=1,
               help='Maximum number of channels.'),
    cfg.IntOpt('pika_frame_max',
               default=131072,
               help='Maximum byte size for an AMQP frame.'),
    #rabbit config
    cfg.IntOpt('heartbeat_rate',
               default=2,
               help='How often times we check the heartbeat.'),
    cfg.BoolOpt('rabbit_use_ssl',
                default=False,
                deprecated_group='DEFAULT',
                help='Connect over SSL for RabbitMQ.'),
    #pika config
    cfg.DictOpt('pika_ssl_options',
                default = {},
                help = 'Connect over SSL for RabbitMQ.'),
    #rabbit config
    cfg.IntOpt('rabbit_max_retries',
               default=None,
               deprecated_for_removal=True,
               deprecated_group='DEFAULT',
               help='Maximum number of RabbitMQ connection retries. '
                    'Default is 0 (infinite retry count).'),
    cfg.IntOpt('rabbit_retry_interval',
               default=1,
               help='How frequently to retry connecting with RabbitMQ.'),
    #pika config
    cfg.IntOpt('pika_socket_timeout',
               default=10,
               help='Socket timeout to use for high latency networks.'),
    cfg.StrOpt('pika_set_locale',
               default='en_US.UTF-8',
               help='Socket timeout to use for high latency networks.'),

    #addtional rabbit config options
    cfg.ListOpt('rabbit_hosts',
                default=['$rabbit_host:$rabbit_port'],
                deprecated_group='DEFAULT',
                deprecated_for_removal=True,
                #deprecated_reason="Replaced by [DEFAULT]/transport_url",
                help='RabbitMQ HA cluster host:port pairs.'),
    cfg.StrOpt('rabbit_login_method',
               default='AMQPLAIN',
               deprecated_group='DEFAULT',
               help='The RabbitMQ login method.'),

]


def register_opts(conf):
    #conf.register_group(rabbitmq_section)
    conf.register_opts(rabbit_options, group=rabbitmq_section)


def list_opts():
    return {rabbitmq_section : rabbit_options}
