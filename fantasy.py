# Heres the selfbot i made for fun fantasy. Skid away! Sorry to break it to you fantasy but i coded a selfbot with 3klines+ and um... how do i say this... im not fucking showing you the code, and ily fantasy :)

from discord.ext import commands
import os
import time


def ifmodulenotfounderror():
    try:
        if ModuleNotFoundError:
            os.system("pip install discord")
    except:
        input("[!] Please install python")
        pass


xnselfbot = commands.Bot(command_prefix="x", self_bot=True)

xnselfbot.remove_command("help")


def runBot(token):
    xnselfbot.run(token, bot=False)


@xnselfbot.event
async def on_connect():
    try:
        print(f"""
[+] Logged in as: {xnselfbot.user}
[+] Prefix: x
        """)
    except:
        input("[-] Error with the code")
        pass


@xnselfbot.command()
async def gp(xnselfbot, message):
    await xnselfbot.message.delete()
    try:
        print(f"[+] Successfully ghost pinged: {message}")
    except:
        print(f"[-] Unsuccessfully ghost pinged: {message}")
        pass


@xnselfbot.command()
async def s(xnselfbot, amount: int, *, message):
    await xnselfbot.message.delete()
    for i in range(amount):
        await xnselfbot.send(message)
        try:
            print(f"[+] Successfully sent: {message}")
        except:
            print(f"[-] Unsuccessfully sent: {message}")
            pass


def run():
    try:
        token = str(input("[?] Token: "))
        os.system("clear")
        time.sleep(3)
        runBot(token)
    except:
        input("[-] Invalid token")
        pass


if __name__ == "__main__":
    run()
