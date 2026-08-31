#!/usr/bin/env python3
from jnpr.junos import Device
with Device() as dev:
  print(dev.facts)
