#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# fcukall.py
from pyroute2.iwutil import IW

iw = IW()
for q in iw.get_interfaces_dump():
    phyname = 'phy%i' % int(q.get_attr('NL80211_ATTR_WIPHY')[:2])
    print('%i\t%s\t%s\t%s' % (q.get_attr('NL80211_ATTR_IFINDEX'), phyname,
                              q.get_attr('NL80211_ATTR_IFNAME'),
                              q.get_attr('NL80211_ATTR_MAC')))
