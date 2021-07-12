import discord
import asyncio
import random

token = 'ODY0MDA5ODY5Nzk5NDU2Nzcw.YOvN5Q.v3AkgRdEJ7jjITnnIdpldZk4dJg'
serverid = 862926240369475594
rainbowrolename = "Pri"
delay = 5


client = discord.Client()
colours = [discord.Color.orange(),discord.Color.gold(),discord.Color.magenta(),discord.Color.red(),discord.Color.blue(),discord.Color.teal(),discord.Color.green(),discord.Color.purple()]

channel = None

async def rainbowrole(role):
	global channel 

	for role in client.get_guild(serverid).roles:
		if str(role) == str(rainbowrolename):
			print("detected role")

			while not client.is_closed():
					# await role.edit(color=random.choice(colours))
				await role.edit(color = random.choice(colours))

				await asyncio.sleep(delay)
	print('role with the name "' + rainbowrolename +'" not found')
	print("creating the role...")
	try:
		await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
		print("role created!")
		await asyncio.sleep(2)
		client.loop.create_task(rainbowrole(rainbowrolename))
	except Exception as e:
		print("couldn't create the role. Make sure the bot have the perms to edit roles")
		print(e)
		pass
		await asyncio.sleep(10)

# @client.event
# async def on_ready():

@client.event
async def on_ready():
	global channel

	print('Logged in as')
	print(client.user.name) 
	print(client.user.id)
	print('Ready.')
	print('------------')
	channel = client.get_channel(863414576875438111)
	client.loop.create_task(rainbowrole(rainbowrolename))
	
	

@client.event
async def on_message(message):
	None
client.run(token)
