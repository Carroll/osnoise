import subprocess

class ReplyExchanges():

   def listQueues(self):
      # attention, rabbitmqctl must be launched as root
      proc = subprocess.Popen("/usr/sbin/rabbitmqctl list_queues name pid", shell=True, stdout=subprocess.PIPE)
      stdout_value = []
      #for i in proc.communicate():
      #   stdout_value.append(i)
      stdout_value = proc.communicate()[0]
      exchanges = stdout_value.splitlines()
      queues = []
      for i in range(len(exchanges)):
         if "reply" in exchanges[i]:
            queues.append(exchanges[i].split('\t')[0])
      return queues

#exc = ReplyExchanges()
#print exc.listQueues()

