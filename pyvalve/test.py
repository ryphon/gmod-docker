import valve.source.a2s
from valve.source import NoResponseError

SERVER_ADDRESS = ('gmod.ttt.itisamystery.com', 27015)
# server.info() = {'response_type': 73, 'protocol': 17, 'server_name': "Garry's Mod", 'map': 'ttt_dolls', 'folder': 'garrysmod', 'game': 'TTT2 (Advanced Update)', 'app_id': 4000, 'player_count': 0, 'max_players': 16, 'bot_count': 0, 'server_type': <ServerType 100 'Dedicated'>, 'platform': <Platform 108 'Linux'>, 'password_protected': 0, 'vac_enabled': 1, 'version': '2020.03.17'}

while True:
    try:
        with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
            info = server.info()
            players = server.players()
            print("{player_count}/{max_players} {server_name}".format(**info))
            for player in sorted(players["players"],
                                 key=lambda p: p["score"], reverse=True):
                print("{score} {name}".format(**player))
        break
    except NoResponseError:
        print('No response yet!')
