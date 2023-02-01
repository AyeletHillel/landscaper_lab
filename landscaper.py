# while(True):
#     user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")
    
#     if(user_choice == "Q"):
#         break

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty_scissors", "profit": 5, "cost": 5},
    {"name": "push_lawnmower", "profit": 50, "cost": 25},
    {"name": "fancy_lawnmower", "profit": 100, "cost": 250},
    {"name": "students", "profit": 250, "cost": 500}
]

## Game Option Funtion

def cut_lawns():
    tool = tools[game["tool"]]
    game["money"] += tool["profit"]
    print(f"You cut lawns using your {tool['name']} and are making ${tool['profit']}")
    

def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using {tool['name']}")

check_stats()
cut_lawns()


