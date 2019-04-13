import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
import asyncio
import os
import json
import urllib.parse
import requests
from PyDictionary import PyDictionary

dictionary=PyDictionary()


command_prefix='?!'
client = commands.Bot(command_prefix)
client.remove_command("help")
os.chdir(r"C:\\Users\\benha\\Documents\\Coding\\Python\\DiscordBots\\Chat")

@client.event
async def on_ready():
	print("Ready")
	owner = await client.get_user_info("330404011197071360")
	await client.send_message(owner, "Ready")

@client.command(pass_context=True)
async def bug(ctx):
	#putting the message into an array
	args = ctx.message.content.split()
	#removing the command
	args.pop(0)

	words = []
	#putting the words into an array
	for l in range(len(args)):
		words.append(args[l])

	bugcontent = ""
	for n in range(len(words)):
		bugcontent += words[n] + " "

	embed = discord.Embed(title="Bug Report", description=bugcontent, color=0x41d8a7)

	await client.send_message(client.get_channel('566282530530131978'), embed=embed)

@client.command(pass_context=True)
async def info(ctx):
    embed=discord.Embed(title="Chat", url="https://discordapp.com/api/oauth2/authorize?client_id=563768980360396821&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3Fclient_id%3D563768980360396821%26scope%3Dbot%26permissions%3D8&response_type=code&scope=messages.read%20bot", description="Chat is a Machine Learning Discord Bot created by user leet_hakker#2582 to provide users with the best interaction possible. Currently still a WIP.", color=0x41d8a7)
    await client.say(embed=embed)


#The following command uses code from Coding Yabe Sei (https://github.com/Academy-Of-Animu/Coding-Yabe-Sei) that I translated into python.

#Thank you to IllusionMan1212#6370 for explaining to me what the fuck that regex was as it allowed me to convert it into an if statement because I can't be bothered to learn regex.

@client.command(pass_context=True)
async def translate(ctx, message):
	try:
		#putting the message into an array
		args = ctx.message.content.split()
		#removing the command
		args.pop(0)
		#will be run if you entered languages and some text
		if len(args) > 2:
			args.append(args[2])
			args[2] = args[1]



			#this unfriendliness here is me filtering out the characters I don't want very ineffieciently
			for i in '!*();,:@&=+$./?%#\\':
				for j in range(len(args)):
					if j > 1:
						if i in args[j]:
							args[j] = args[j].replace(i, '')

		#languages Chat can translate
		langs = {
		        'af': 'Afrikaans',
		        'sq': 'Albanian',
		        'am': 'Amharic',
		        'ar': 'Arabic',
		        'hy': 'Armenian',
		        'az': 'Azerbaijani',
		        'eu': 'Basque',
		        'be': 'Belarusian',
		        'bn': 'Bengali',
		        'bs': 'Bosnian',
		        'bg': 'Bulgarian',
		        'my': 'Burmese',
		        'ca': 'Catalan',
		        'ny': 'Chichewa (Chewa, Nyanja)',
		        'zh': 'Chinese',
		        'hr': 'Croatian',
		        'cs': 'Czech',
		        'da': 'Danish',
		        'nl': 'Dutch',
		        'en': 'English',
		        'eo': 'Esperanto',
		        'et': 'Estonian',
		        'fi': 'Finnish',
		        'fr': 'French',
		        'gl': 'Galician',
		        'gd': 'Gaelic (Scottish)',
		        'ka': 'Georgian',
		        'de': 'German',
		        'el': 'Greek',
		        'gu': 'Gujarati',
		        'ht': 'Haitian Creole',
		        'ha': 'Hausa',
		        'he': 'Hebrew',
		        'hi': 'Hindi',
		        'hu': 'Hungarian',
		        'is': 'Icelandic',
		        'ig': 'Igbo',
		        'id': 'Indonesian',
		        'in': 'Indonesian',
		        'ga': 'Irish',
		        'it': 'Italian',
		        'ja': 'Japanese',
		        'jv': 'Javanese',
		        'kn': 'Kannada',
		        'kk': 'Kazakh',
		        'km': 'Khmer',
		        'ky': 'Kyrgyz',
		        'ko': 'Korean',
		        'ku': 'Kurdish',
		        'lo': 'Lao',
		        'la': 'Latin',
		        'lv': 'Latvian (Lettish)',
		        'lt': 'Lithuanian',
		        'lg': 'Luxembourgish',
		        'mk': 'Macedonian',
		        'mg': 'Malagasy',
		        'ms': 'Malay',
		        'ml': 'Malayalam',
		        'mt': 'Maltese',
		        'mi': 'Maori',
		        'mr': 'Marathi',
		        'mh': 'Marshallese',
		        'mo': 'Moldavian',
		        'mn': 'Mongolian',
		        'ne': 'Nepali',
		        'no': 'Norwegian',
		        'nb': 'Norwegian bokmål',
		        'nn': 'Norwegian nynorsk',
		        'ps': 'Pashto (Pushto)',
		        'fa': 'Persian (Farsi)',
		        'pl': 'Polish',
		        'pt': 'Portuguese',
		        'pa': 'Punjabi (Eastern)',
		        'ro': 'Romanian',
		        'ru': 'Russian',
		        'sm': 'Samoan',
		        'sr': 'Serbian',
		        'sh': 'Serbo-Croatian',
		        'st': 'Sesotho',
		        'sn': 'Shona',
		        'sd': 'Sindhi',
		        'si': 'Sinhalese',
		        'sk': 'Slovak',
		        'sl': 'Slovenian',
		        'so': 'Somali',
		        'es': 'Spanish',
		        'su': 'Sundanese',
		        'sw': 'Swahili (Kiswahili)',
		        'sv': 'Swedish',
		        'tl': 'Tagalog',
		        'tg': 'Tajik',
		        'ta': 'Tamil',
		        'te': 'Telugu',
		        'th': 'Thai',
		        'tr': 'Turkish',
		        'uk': 'Ukrainian',
		        'ur': 'Urdu',
		        'uz': 'Uzbek',
		        'vi': 'Vietnamese',
		        'cy': 'Welsh',
		        'fy': 'Western Frisian',
		        'xh': 'Xhosa',
		        'yi': 'Yiddish',
		        'ji': 'Yiddish',
		        'yo': 'Yoruba',
		        'zu': 'Zulu',
		    }

		#run if you asked for "chat translate list". Returns an embed of all the languages Chat can translate
		if args[0] == 'list':
			listOfDLangs = ''

			for k in langs:
				listOfDLangs += f'{langs.get(k)} - {k}\n'

			embed1 = discord.Embed(
				color=(0x1355A4),
				title=('List of languages Chat can translate:'),
				description=(listOfDLangs))
			embed1.add_field(name="How to use: ", value='?!translate lang1-lang2 <stuff to translate>', inline=False)

			await client.say(embed=embed1)
			return

		else:
			#Translation part
			#Getting the sourceLang and targetLang from the first
			sourceLang = args[0].split('-')[0]
			targetLang = args[0].split('-')[1]
			words = []
			#putting the words into an array
			for l in range(len(args)):
				if l >= 1:
					words.append(args[l])

			#you dum fok
			if sourceLang not in langs:
				return await client.say(f'Source language `{sourceLang}` doesn\'t exist.\n(if you believe this is wrong make a bug report using `?!bug `)')
			if targetLang not in langs:
				return await client.say('Target Language `{targetLang}` doesn\'t exist.\n(if you believe this is wrong make a bug report using `?!bug `)')

			#if words is empty, you didn't enter anything to translate
			if words == "":
				return await client.say('Please provide a word or sentence to translate.')

			#putting the words back into a string
			words2translate = ""
			for m in range(len(words)):
				words2translate += words[m].lower() + " "

			#The actual link for translations
			link = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl=${targetLang}&dt=t&ie=UTF-8&oe=UTF-8&q={urllib.parse.quote(words2translate)}'


			try:
				#getting a json pull of the site
				translation = requests.get(link).json()
				#putting said json pull into a nice embed
				embed = discord.Embed(
					description=(translation[0][0][0]),
					color=(0x1355A4))
				#outputting the embed and the translation source and target
				await client.say(f'Translated from {langs[sourceLang]} to {langs[targetLang]}:')
				await client.say(embed=embed)

			#Error handling - site may have changed, gone down etc
			except Exception as e:
				print(e)
				await client.say("Something went wrong while translating, please check you formatted it correctly and try again.\nOr if you believe this is a bug please report it with `?!bug`")

	#Chat doesn't know wtf went wrong
	except Exception as e:
		raise e
		await client.say("Something went wrong while translating, please check you formatted it correctly and try again.\nOr if you believe this is a bug please report it with `?!bug`")

@client.command(pass_context=True)
async def define(ctx):
	#putting the message into an array
	args = ctx.message.content.split()
	#removing the command
	args.pop(0)

	words = []
	#putting the words into an array
	for l in range(len(args)):
		words.append(args[l])

	#taking the first word of the message as the word to be defined
	definecontent = words[0]

	try:
		#getting neccesary info for the word
		wordinfo = dictionary.meaning(definecontent)
		wordclasses=[]
		meanings=[]
		for p in wordinfo.keys():
			wordclasses.append(p)
			meanings.append(wordinfo[p])

		#putting it all into an embed
		embed=discord.Embed(title=definecontent, description=f"Found {len(meanings)} definitions for {definecontent}", color=0x1355A4)
		for o in range(len(meanings)):
			for q in range(len(meanings[o])):
				embed.add_field(name=f"{o+1} - {q+1})", value=f"{wordclasses[o]}:\n{meanings[o][q]}", inline=False)

		#outputting the embed
		await client.send_message(ctx.message.channel, embed=embed)
	except:
		await client.send_message(ctx.message.channel, "Something went wrong while getting your definition. This may be caused due to the word you inputted not being in the dictionary. Please try again later.\nIf you feel this is wrong use `?!bug` to report the error.")



client.run('YOUR_API_KEY')
