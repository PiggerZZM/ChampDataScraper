replace_dict = {
    'FrontFreeKicks': '前场任意球',
    'Corners': '角球',
    'Freekiscks': '任意球',
    'Goals': '进球',
    'InitAttackRate': '前攻主导率',
    'Pass': '传球数',
    'PassesSuccRate': '传球成功率',
    'Penalties': '点球',
    'PossAve': '控球率',
    'Shots': '射门',
    'ShotsOnTarget': '射正',
    'AttThPass': '进攻30米区传球次数',
    'AttThSucPaAccuracy': '进攻30米区传球成功率',
    'BreakThrows': '突破',
    'Center': '传中',
    'KeyPasses': '关键传球',
    'ShotsInPenaltyArea': '禁区内射门',
    'ShotsOnTargetIbox': '禁区内射正',
    'ShotsOnTargetObox': '禁区外射正',
    'ShotsOutPenaltyArea': '禁区外射门',

    'Clearances': '解围',
    'Foul': '犯规',
    'Intercepttions': '拦截',
    'PassBlocks': '封堵传球',
    'RedCard': '红牌',
    'ShotsBlocks': '封堵射门',
    'Tackles': '抢断',
    'YellowCard': '黄牌'
}

def deal_data(response, team_dict):
    response.pop('matchHalf', None)
    response.pop('matchId', None)
    response.pop('half', None)
    response.pop('guestTacklesConneceded', None)
    response.pop('homeTacklesConneceded', None)
    data_dict = dict()
    for key in response.keys():
        guest = 0
        home = 0
        try:
            if 'guest' in key:
                data_key = key[5:]
                guest = 1
            else:
                data_key = key[4:]
                home = 1
            if data_dict.get(replace_dict[data_key]) is None:
                data_dict[replace_dict[data_key]] = dict()
            data_dict[replace_dict[data_key]][team_dict['客场' if guest > home else '主场']] = response[key]
        except:
            print(key,'替换失败')

    return data_dict

if __name__ == '__main__':
    response = {'guestFrontFreeKicks': 11, 'guestInitAttackRate': 0.341, 'guestFreekiscks': 22, 'guestCorners': 1,
     'guestPassesSuccRate': 0.587, 'guestPass': 254, 'guestShots': 5, 'guestGoals': 1, 'half': '0',
     'homeFreekiscks': 19, 'guestShotsOnTarget': 1, 'homePassesSuccRate': 0.746, 'homeFrontFreeKicks': 12,
     'homePass': 453, 'homeInitAttackRate': 0.659, 'homeGoals': 1, 'homePenalties': 1, 'homeShots': 20,
     'homeCorners': 7, 'guestPenalties': 1, 'homePossAve': 0.599, 'matchHalf': 0, 'matchId': '2761',
     'guestPossAve': 0.401, 'homeShotsOnTarget': 3}
    team_dict = {'home': 'a', 'guest': 'b'}
    a = deal_data(response, team_dict)
    print(a)




