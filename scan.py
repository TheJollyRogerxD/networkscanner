def scanNetwork(network):
    returnlist = []
    import nmap
    now = raw_input("Sniff Now? y/n: ")
    print(now)
    if now == y:
        nm = nmap.PortScanner()
    a = nm.scan(hosts=network, arguments='-sP')
    for k, v in a['scan'].iteritems():
        if str(v['status']['state']) == 'up':
            try:
                returnlist.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
            except:
                pass
    return returnlist
elif:
    print("Exiting...")
    raise SystemExit
else:
    print("Not a command.")
    raise SystemExit
scanNetwork()