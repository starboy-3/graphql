import argparse
import json

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from pygments import highlight, lexers, formatters

from requests import *

def main():
    transport = AIOHTTPTransport(url="http://localhost:8080")
    client = Client(transport=transport, fetch_schema_from_transport=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="your name")
    args = parser.parse_args()

    print(f"Hello, {args.name}")

    try:
        while True:
            command = input()
            parts = command.split()

            if len(parts) == 0:
                continue

            if parts[0] == "exit":
                print("Good day!")
                return

            if parts[0] == "all" and parts[1] == "games":
                query = gql(request_games())
            elif parts[0] == "games":
                if len(parts) == 2:
                    if parts[1] == "finished":
                        finished = True
                    elif parts[1] == "unfinished":
                        finished = False
                    else:
                        print("Bad command!")
                        continue
                else:
                    print("Bad command!")
                    continue
                query = gql(request_games(finished))
            elif parts[0] == "game":
                if len(parts) == 2:
                    query = gql(request_game(parts[1]))
                elif len(parts) == 3 and parts[2] == "score":
                    query = gql(request_game_score(parts[1]))
                else:
                    print("Bad command!")
                    continue
            elif parts[0] == "add" and parts[1] == "comment":
                if len(parts) < 4:
                    print("Bad command!")
                    continue
                id = parts[2]
                comment = " ".join(parts[3:])
                query = gql(request_add_comment(id, args.name, comment))
            else:
                print("Bad command!")
                continue

            try:
                result = client.execute(query)
            except TransportQueryError as e:
                print(e)
                continue

            formatted_json = json.dumps(result, indent=4)
            colorful_json = highlight(formatted_json.encode("UTF-8"), lexers.JsonLexer(), formatters.TerminalFormatter())
            print(colorful_json)

    except KeyboardInterrupt:
        print("\nGood day!")
        return


if __name__ == "__main__":
    main()
