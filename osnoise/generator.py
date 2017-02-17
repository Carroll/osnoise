#!/usr/bin/env python

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

import osnoise.common.config as config
import osnoise.common.logger as logging
import osnoise.core.messaging as messaging
import osnoise.core.publisher as publisher
import osnoise.conf.opts as opts

import threading
import time
import uuid
# JFP #
import osnoise.common.listq as listq
import pdb

MAXTHREADS = 20

class OSNoise(object):
    """This class inits and runs OSNoise."""

    def run(self, confdir=None):
        try:
            global LOG
            # update config file
            if confdir:
                config.update_conf_dir(confdir=confdir)

            # init config
            conf = config.init_config()
            opts.list_opts()

            # init main log
            LOG = logging.getLogger(__name__)
            LOG.info('Start OSNoise..')


            exc = listq.ReplyExchanges()
            for replyExchange in exc.listQueues():
               # init publisher and start publish
               # JFP get reply and routing-keys
               LOG.info('Exchange %s',replyExchange)
               # init messaging config
               msg = messaging.BasicMessaging(conf)
               pdb.set_trace()
               comp = msg.get_exchange()
               pub = publisher.Publisher(pub_id=uuid.uuid4(),
                                         duration=msg.get_duration(),
                                         publish_rate=msg.get_publish_rate(),
                                         connection=msg.get_connection(),
                                         channel=msg.get_channel(),
                                         # JFP send on all replyExchanges
                                         #exchange=msg.get_exchange(),
                                         #routing_key=msg.get_routing_key(),
                                         exchange=replyExchange,
                                         routing_key=replyExchange,
                                     
                                         body=msg.get_message_body(),
                                         properties=msg.get_message_properties()
                                         )

               # start publishing
               pub.do_publish()

               # JFP go behind 1
               while threading.activeCount() > MAXTHREADS:
                   time.sleep(0.1)
                   pass
            # in case of daemon threads so that they do not stop when main program exits
            #time.sleep(msg.get_duration())

        except KeyboardInterrupt:
            LOG.warning('Program interrupted by user..')
            LOG.info('Stopping..')


if __name__ == '__main__':
    osn = OSNoise()
    osn.run()
