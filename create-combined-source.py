#!/usr/bin/env python3

import os
from pick import pick
import pulsectl

name = 'virtual-combined-source'
description = 'VirtualCombinedAudioSource'
sink_name='{}.sink'.format(name)

pulse = pulsectl.Pulse(name)

title = '''This utility creates a new virtual audio source by mixing in a selection of audio sources.

Use `up`, `down` and `space` to complete the selection. Hit `enter` when done.

Please choose some source devices to mix in:'''
options = pulse.source_list()

def get_label(option):
    return option.description

selected = pick(options, title, multiselect=True, options_map_func=get_label)

prev_sinks = [ i for i in pulse.module_list() if i.name == 'module-null-sink' and 'sink_name={}'.format(sink_name) in i.argument ]
prev_loopbacks = [ i for i in pulse.module_list() if i.name == 'module-loopback' and 'sink={}'.format(sink_name) in i.argument ]

for m in prev_loopbacks:
    pulse.module_unload(m.index)

for m in prev_sinks:
    pulse.module_unload(m.index)

if(len(selected)):
    index=pulse.module_load(
        'module-null-sink',
        args=[
            'sink_name={}'.format(sink_name),
            'sink_properties="device.description={}"'.format(description),
        ]
    )
    for index, selection in enumerate(selected):
        source = selection[0]
        pulse.module_load(
            'module-loopback',
            args = [
                'source={}'.format(source.name),
                'sink={}'.format(sink_name),
                'latency_msec=1',
            ]
        )
    print('notice: added a virtual source named `{}` and {} loopbacks'.format(description, len(selected)))
else:
    print('warning: removing virtual audio source: no sources selected')