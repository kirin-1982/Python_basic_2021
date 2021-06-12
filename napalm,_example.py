#! /user/bin/env python3

from napalm import get_network_driver
import json

driver = get_network_driver('ios')
sw1 = driver('192.168.245.11','python', '123')
sw1.open()
#
# output = sw1.get_interfaces_counters()
# print(json.dumps(output, indent=2))
# print(type(output))

sw1.load_merge_candidate(filename='napalm_cfg.txt')
# sw1.commit_config()

differences = sw1.compare_config()
if len(differences) > 0:
    print(differences)
    sw1.commit_config()
else:
    print('No changes needed!')
    sw1.discard_config()


