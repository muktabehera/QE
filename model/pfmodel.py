"""PathFinder Model for stand-alone PFEs, covering broadcasts and distributions."""
from attrdict import AttrDict
from collections import OrderedDict
# import time

# Physical Setup Details

# PathFinder (PF) server under test:
QED = '172.30.5.153'
QED_Name = 'automation-pf03.qumu.media'
QED_Tenant_b = 'automation-pf03b.qumu.media'

# PFEs under test: (IP, Name)
PFE_IPs = [('172.30.4.229', 'ZL-PFE-03'),
           ('172.30.1.76', 'ZL-PFE-05'),
           ('172.30.1.77', 'ZL-PFE-04')]

# Live video source
# testStream = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8'
testStreams = ['http://media.blacktrash.org/stsp.m3u8']
testFiles = ['file://origin1/TestFile1.txt']


### MODEL ###

# state

MaxBroadcasts = 1
MaxDistributions = 1
MaxPFEs = 1


PF = AttrDict()
# PF['broacasts'] = OrderedDict()
# PF['distrubtions'] = OrderedDict()
PF['PFEs'] = AttrDict()

for PFE_IP, PFE_Name in PFE_IPs[:MaxPFEs]:
    PF['PFEs'][PFE_IP] = OrderedDict()
    PF['PFEs'][PFE_IP]['broacasts'] = OrderedDict()
    PF['PFEs'][PFE_IP]['distrubtions'] = OrderedDict()
    PF['PFEs'][PFE_IP]['audiences'] = OrderedDict()


# actions

# broacasts

def create_broadcast(PFE_IP, BroadcastId):
    global PF
    # broadcastIdExt = time.strftime('-%Y%m%d%H%M%S')
    # BroadcastId = 'broadcast-' + PFE_Name + broadcastIdExt
    PF['PFEs']['broacasts'][BroadcastId] = "broadcast created"

def create_broadcast_enabled(PFE_Name):
    global PF
    return len(PF['PFEs']['broacasts'][BroadcastId]) <= MaxBroadcasts

def activate_broadcast(BroadcastId):
    global PF
    PF['PFEs']['broacasts'][BroadcastId] = "broadcast activated"

def activate_broadcast_enabled(BroadcastId):
    global PF
    if BroadcastId not in PF['PFEs']['broacasts']:
        return False
    if PF['PFEs']['broacasts'][BroadcastId] != "broadcast created":
        return False

def get_broadcast_uri(BroadcastId):   #, audience):
    global PF
    PF['PFEs']['broacasts'][BroadcastId] = "broadcast played"

def get_broadcast_uri_enabled(BroadcastId):
    global PF
    if BroadcastId not in PF['PFEs']['broacasts']:
        return False
    if PF['PFEs']['broacasts'][BroadcastId] != "broadcast activated":
        return False


def delete_broadcast(BroadcastId):
    global PF
    PF['PFEs']['broacasts'].pop(BroadcastId)

def delete_broadcast_enabled(BroadcastId):
    global PF
    if BroadcastId not in PF['PFEs']['broacasts']:
        return False
    if PF['PFEs']['broacasts'][BroadcastId] != "broadcast played":
        return False




## Metadata

state = ('broacasts')

actions = {create_broadcast, activate_broadcast, get_broadcast_uri, delete_broadcast}

enablers = {create_broadcast: (create_broadcast_enabled,),
            activate_broadcast: (activate_broadcast_enabled,),
            get_broadcast_uri: (get_broadcast_uri_enabled,),
            delete_broadcast: (delete_broadcast_enabled,)}

# state = ('broacasts', 'distrubtions')
#
# actions = {create_broadcast, activate_broadcast, get_broadcast_uri, delete_broadcast,
#            create_distrubtion, activate_distrubtion, get_distrubtion_uri, delete_distrubtion}
#
# enablers = {create_broadcast: (create_broadcast_enabled,),
#             activate_broadcast: (activate_broadcast_enabled,),
#             get_broadcast_uri: (get_broadcast_uri_enabled,),
#             delete_broadcast: (delete_broadcast_enabled,),
#             create_distrubtion: (create_distrubtion_enabled,),
#             activate_distrubtion: (activate_distrubtion_enabled,),
#             get_distrubtion_uri: (get_distrubtion_uri_enabled,),
#             delete_distrubtion: (delete_distrubtion_enabled,)}

# def state_invariant():
#     """
#     Safety requirement: power == 'On' => door == 'Closed'
#     """
#     # p => q can be expressed:  not p or q
#     return power == 'Off' or door == 'Closed'


def accepting():
    return len(PF['broacasts']) == 0 and len(PF['distrubtions']) == 0

# cleanup = (Logout,)

# default domains

PFE_IPs = ('172.30.4.229', '172.30.1.76', '172.30.1.77')
# PFE_IPs = list()
# audiences = list()
# for PFE_IP, PFE_Name in PFE_IPs[:MaxPFEs]:
#     PFE_IPs.append(PFE_IP)
#     audiences.append(PFE_IP)


domains = {create_broadcast: {'PFE_IP': PFE_IPs, 'BroadcastId': testStreams},
           activate_broadcast: {'BroadcastId': testStreams},
           get_broadcast_uri: {'BroadcastId': testStreams},   # , 'audience': audiences},
           delete_broadcast: {'BroadcastId': testStreams}}

# needed for multiple test runs in one session

def Reset():
    global PF
    PF = AttrDict()
    PF['PFEs'] = AttrDict()
    for PFE_IP, PFE_Name in PFE_IPs[:MaxPFEs]:
        PF['PFEs'][PFE_IP] = OrderedDict()
        PF['PFEs'][PFE_IP]['broacasts'] = OrderedDict()
        PF['PFEs'][PFE_IP]['distrubtions'] = OrderedDict()
        PF['PFEs'][PFE_IP]['audiences'] = OrderedDict()
