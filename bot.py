import discord
from discord.ext import commands
import random
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Card setup
suits = ["♠", "♥", "♦", "♣"]
ranks = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}


games = {}


def draw_card():
    rank = random.choice(list(ranks.keys()))
    suit = random.choice(suits)
    return f"{rank}{suit}", ranks[rank]


def hand_value(hand):
    total = sum(card[1] for card in hand)
    aces = sum(1 for card in hand if "A" in card[0])

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def format_hand(hand):
    return ", ".join(card[0] for card in hand)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def blackjack(ctx):
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    games[ctx.author.id] = {
        "player": player,
        "dealer": dealer,
        "active": True
    }

    await ctx.send(
        f"🃏 **Blackjack Started!**\n\n"
        f"Your hand: {format_hand(player)} ({hand_value(player)})\n"
        f"Dealer shows: {dealer[0][0]} + ?\n\n"
        f"Use `!hit` or `!stand`"
    )


@bot.command()
async def hit(ctx):
    if ctx.author.id not in games:
        await ctx.send("Start a game with `!blackjack`")
        return

    game = games[ctx.author.id]

    if not game["active"]:
        await ctx.send("Game is already finished. Start a new one with `!blackjack`")
        return

    card = draw_card()
    game["player"].append(card)

    total = hand_value(game["player"])

    if total > 21:
        game["active"] = False
        await ctx.send(
            f"You drew {card[0]}\n"
            f"Your hand: {format_hand(game['player'])} ({total})\n"
            f"Bust! You lose."
        )
        return

    await ctx.send(
        f"🃏 You drew {card[0]}\n"
        f"Your hand: {format_hand(game['player'])} ({total})"
    )


@bot.command()
async def stand(ctx):
    if ctx.author.id not in games:
        await ctx.send("Start a game with `!blackjack`")
        return

    game = games[ctx.author.id]

    if not game["active"]:
        await ctx.send("Game already ended. Start a new one with `!blackjack`")
        return

    player_total = hand_value(game["player"])
    dealer = game["dealer"]


    while hand_value(dealer) < 17:
        dealer.append(draw_card())

    dealer_total = hand_value(dealer)

    if dealer_total > 21:
        result = "Dealer busts! You win"
    elif player_total > dealer_total:
        result = "You win"
    elif player_total < dealer_total:
        result = "Dealer wins"
    else:
        result = "Tie"

    game["active"] = False

    await ctx.send(
        f"🃏 **Final Result**\n\n"
        f"Your hand: {format_hand(game['player'])} ({player_total})\n"
        f"Dealer hand: {format_hand(dealer)} ({dealer_total})\n\n"
        f"{result}"
    )


bot.run(TOKEN)
