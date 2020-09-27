import valve.source.a2s

SERVER_ADDRESS = ('10.0.0.5', 300)

with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
    info = server.info()
    players = server.players()

print("{player_count}/{max_players} {server_name}".format(**info))
for player in sorted(players["players"],
                     key=lambda p: p["score"], reverse=True):
    print("{score} {name}".format(**player))
