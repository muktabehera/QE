import observation_queue as observation
import time

def test_action(aname, args, modelResult):
    """
    To indicate success, return None (no return statement).
    To indicate failure, return string that explains failure.
    Test runner also treats unhandled exceptions as failures.

    This is the synchronous stepper so send_call is always immediately
    followed by send_return, etc.  Therefore all the _call branches are
    empty, do all the work in the _return branches.

    send_return always invokes sender.send and recv_return always
    invokes receiver.recv

    model_result must appear in arg list but it is not used here,
    instead model results are passed in _return args

    In the test_action branch for each controllable action, the code for
    the _call action waits (synchronously) for the implemenation to
    return, then uses the observed return value to construct and return
    the _return action (which may include nondeterministic return values).

    For now send_ always invokes sender.send and recv_ always invokes receiver.recv
    """

    # state needed to remember
    global PFEs, Deliveries, Audiences, Broadcasts, Distributions

    if aname == 'create_broadcast':
        (BroadcastId, Audience, Stream, ) = args
        print(
            BroadcastId,
            Audience,
            Stream, )
        time.sleep(1)
        return None

    elif aname == 'activate_broadcast':
        (BroadcastId, ) = args
        print(
            BroadcastId, )
        time.sleep(1)
        return None
        nchars = connection.sender.send(msg)
        if n != nchars:
            return 'send returned %s, expected %s ' % (nchars, n)

    elif aname == 'get_broadcast_uri':
        (BroadcastId, Audience, ) = args

    elif aname == 'delete_broadcast':
        (BroadcastId, ) = args
        print(
            BroadcastId, )
        time.sleep(1)
        return None
        data = connection.receiver.recv(bufsize)
        if data != msg:  # now msg is like old modelresult
            # wrapped failMessage should fit on two 80 char lines,
            # failMessage prefix from pmt is 20 char, fixed text here is > 32
            # char
            maxlen = 40  # max number of chars from msg to print in failMessage
            nd = len(data)
            nm = len(msg)
            sdata = data if nd <= maxlen \
                else data[:maxlen / 2] + '...' + data[-maxlen / 2:]
            smodel = msg if nm <= maxlen \
                else msg[:maxlen / 2] + '...' + msg[-maxlen / 2:]
            return 'recv returned %s (%s), expected %s (%s)' % (sdata, nd,
                                                                smodel, nm)

    # if aname == 'send_call':
    #     (msg,) = args    # extract msg from args tuple, like msg = args[0]
    #     n = connection.sender.send(msg)
    #     observation.queue.append(('send_return', (n,)))
    #     return None    # pmt will check observation_queue
    #
    # elif aname == 'recv_call':
    #     (bufsize,) = args
    #     msg = connection.receiver.recv(bufsize)
    #     observation.queue.append(('recv_return', (msg,)))
    #     return None    # pmt will check observation_queue

    else:
        raise NotImplementedError, 'action not supported by stepper: %s' % aname
