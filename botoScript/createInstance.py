import boto 
from boto.ec2.regioninfo import RegionInfo
import time

import connector

#live Security Group
#['ssh','https','couchdb','erlang','icpm']


def create_instance():
	ec2_conn = connector.get_conn()
	avail_zone = 'melbourne-qh2'
	
	print "creating instance"
	instance_pool = ec2_conn.run_instances('ami-00003837', #imageID
							key_name = 'ManualKey',
							instance_type = 'm1.medium',
							security_groups = ['ssh','http'],
							placement = avail_zone) 
	
	instance = instance_pool.instances[0]
	
	print "end of execution"