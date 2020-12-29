def who_is_online(friends):
    dic = {}
    for friend in friends:
        if friend['status'] == 'online':
            if friend["last_activity"] <= 10:
                if 'online' not in dic:
                    dic['online'] = []
                dic['online'].append(friend['username'])
            else:
                if 'away' not in dic:
                    dic['away'] = []
                dic['away'].append(friend['username'])
        else:
            if 'offline' not in dic:
                dic['offline'] = []
            dic['offline'].append(friend['username'])
    return dic