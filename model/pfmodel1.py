"""PathFinder Model for stand-alone PFEs, covering broadcasts and distributions."""
# from attrdict import AttrDict
from box import Box
from collections import OrderedDict

SUT_PFE_IPs = ('172.30.4.229', '172.30.1.76', '172.30.1.77')
SUT_Deliveries = ('videoedge-ZL-PFE-03', 'videoedge-ZL-PFE-04', 'videoedge-ZL-PFE-05')
SUT_Audiences = ('audiencevne-ZL-PFE-03', 'audiencevne-ZL-PFE-04', 'audiencevne-ZL-PFE-05', )
audience_cases = ('172.30.4.229', '172.30.1.76', '172.30.1.77',
                  ('172.30.4.229', '172.30.1.76'), ('172.30.4.229', '172.30.1.76', '172.30.1.77'))
testStreams = ['http://media.blacktrash.org/stsp.m3u8']
testStreams.append(
    'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8')
testFiles = ['file://origin1/TestFile1.txt']


### MODEL ###

# Test Model Configuration
MaxBroadcasts = 2
MaxDistributions = 1
MaxAudiences = 2
MaxPFEs = 1
MaxDeliveries = 2
MaxTestStreams = 1
GetUrlStep = False
# audiences = audience_cases[:1]

# Model State

PFEs = list(SUT_PFE_IPs[:MaxPFEs])
# Deliveries = list()            # SA PFEs: [ PFE_IP, PFE_IP, ... ]
# Deliveries = list()            # later: [ [id, settings/device(s), type, role ], ... ]
Deliveries = list(SUT_Deliveries[:MaxDeliveries])
# Audiences = list()
Audiences = SUT_Audiences[:MaxAudiences]
# Audiences = [('aud-{}'.format(a), audience_cases[a]) for a in range(MaxAudiences)]
# Audiences = audience_cases[:1]   # list of lists: [ [id, [delivery, delievey, ...],
#                                   later -->       [clients...], [network locations...] ]
Broadcasts = list()   # list of lists: [id, status, audience, stream]
Distributions = list()   # list of lists: [id, status, audience, file]

# actions

# - broacasts

def create_broadcast(BroadcastId, Audience, Stream):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    Broadcasts.append([BroadcastId, 'created', Audience, Stream])

def create_broadcast_enabled(BroadcastId, Audience, Stream):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    if BroadcastId in [b[0] for b in Broadcasts]:
        return False
    if len(Broadcasts) >= MaxBroadcasts:
        return False
    return True

def activate_broadcast(BroadcastId):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    for b in Broadcasts:
        if b[0] == BroadcastId:
            Broadcasts[Broadcasts.index(b)][1] = 'activated'

def activate_broadcast_enabled(BroadcastId):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    if BroadcastId not in [b[0] for b in Broadcasts]:
        return False
    for b in Broadcasts:
        if b[0] == BroadcastId:
            if Broadcasts[Broadcasts.index(b)][1] != 'created':
                return False
    return True

def get_broadcast_uri(BroadcastId, Audience):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    for b in Broadcasts:
        if b[0] == BroadcastId:
            Broadcasts[Broadcasts.index(b)][1] = 'played'

def get_broadcast_uri_enabled(BroadcastId, Audience):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    if BroadcastId not in [b[0] for b in Broadcasts]:
        return False
    for b in Broadcasts:
        if b[0] == BroadcastId:
            if Broadcasts[Broadcasts.index(b)][1] != 'activated':
                return False
    return True

def delete_broadcast(BroadcastId):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    for b in Broadcasts:
        if b[0] == BroadcastId:
            Broadcasts.pop(Broadcasts.index(b))

def delete_broadcast_enabled(BroadcastId):
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    if BroadcastId not in [b[0] for b in Broadcasts]:
        return False
    for b in Broadcasts:
        if b[0] == BroadcastId:
            if GetUrlStep:
                if Broadcasts[Broadcasts.index(b)][1] not in ['played']:
                    return False
            else:
                if Broadcasts[Broadcasts.index(b)][1] not in ['activated', 'played']:
                    return False
    return True


## Metadata

# state = ('PFEs', 'Deliveries', 'Audiences', 'Broadcasts', 'Distributions')
state = ('Broadcasts',)

if GetUrlStep:
    actions = {create_broadcast, activate_broadcast, get_broadcast_uri, delete_broadcast}
else:
    actions = {create_broadcast, activate_broadcast, delete_broadcast}

enablers = {create_broadcast: (create_broadcast_enabled,),
            activate_broadcast: (activate_broadcast_enabled,),
            get_broadcast_uri: (get_broadcast_uri_enabled,),
            delete_broadcast: (delete_broadcast_enabled,)}


def accepting():
    return len(Broadcasts) == 0 and len(Distributions) == 0

broadcastIds = ['brd-{}'.format(b) for b in range(MaxBroadcasts)]
audienceIds = [aud[0] for aud in Audiences]
streams = testStreams[:MaxTestStreams]

domains = {create_broadcast: {'BroadcastId': broadcastIds,
                              'Audience': Audiences,
                              'Stream': streams},
           activate_broadcast: {'BroadcastId': broadcastIds},
           get_broadcast_uri: {'BroadcastId': broadcastIds,
                               'Audience': Audiences, },   # , 'audience': audiences},
           delete_broadcast: {'BroadcastId': broadcastIds}}


def Reset():
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions
    PFEs = list(PFE_IPs[:MaxPFEs])
    # Deliveries = list()
    Deliveries = list(PFE_IPs[:MaxPFEs])
    # Audiences = list()
    Audiences = audience_cases[:1]
    Broadcasts = list()   # list of lists: [id, status]
    Distributions = list()   # list of lists: [id, status]
