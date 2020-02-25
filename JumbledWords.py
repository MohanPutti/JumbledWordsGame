import random
def choice():
	words=['science','player','computer','accident','condition','feather','science','mathematics','pinnacle','banana','import','problem','question',
       'structure','dictionary','separate','anarchy','paragon','piety','monarchy','social','assumption','activity','contribution','communication','panegyric','placid','compare','perfidious','challenge','request','search',
'generator','education','quagmire','pusillanimous','purpose','purport','difficult','repository','jumble','quiescent','petulant','salutary','reprobate','verdict','dynamic','usher',
'interpolate','delegate','maintain','emperical','saturate','specious']
	pick=random.choice(words)
	return pick
def jumble(word):
	jumbled_word="".join(random.sample(word,len(word)))
	return jumbled_word
def thank(p1n,p2n,p1,p2):
	print('*****************')
	print(p1n,' your score is:', p1)
	print(p2n,'your score is":', p2)
	if(p1>p2):
		print(p1n,'wins..')
	elif(p1==p2):
		print('tie')
	else:
		print(p2n,'wins..')
	print('thank you...')
	
	
def play():
	print('JUMBLED WORDS')
	print('-------------')
	p1name=input('player1,Please enter your name: ')
	p2name=input('player2,please enter tour name: ')
	print('Good luck both of you..')
	print('')
	print('....BEGIN....')
	pp1=0
	pp2=0
	turn=0
	while(1):
		picked_word=choice()
		qn=jumble(picked_word)
		
		if(turn%2==0):
			print('you have 2 choices')
			chance=0
			while(1):
				
				print('')
				print(p1name,'it\'s your turn')
				print('the jumbled word for you:' ,qn)
				ans=input('what is in my mind? ')
				if(ans==picked_word):
					if (chance==0):
						pp1+=2
						print('you got it..')
						print(p1name,' your points :',pp1)
						break
					if (chance==1):
						pp1=pp1+1
						print('you got it')
						print(p1name,' your points :',pp1)
						break
					
				else:
					chance+=1
					print('better luck next time')
				if(chance>1):
					print('better luck next time the word is',picked_word)
					print('')
					break;
			c=int(input('press 1 to continue ,0 to quit'))
			
			if(c==0):
				thank(p1name,p2name,pp1,pp2)
				break
		else:
			print('you have 2 choices')
			chance=0
			while(1):
	
				print('')
				print(p2name,'it\'s your turn')
				print('the jumbled word for you:' ,qn)
				ans=input('what is in my mind? ')
				if(ans==picked_word):
					if(chance==0):
						pp2=pp2+2
						print('you got it..')
						print(p2name,' your points :',pp2)
						break
					if(chance==1):
						pp2+=1
						print('you got it..')
						print(p2name,' your points :',pp2)
						break
				else:
					chance+=1
					print('better luck next time')
				if(chance>1):
					print('better luck next time the word is: ',picked_word)
					print('')
					break
			c=int(input('press 1 to continue ,0 to quit'))
			if(c==0):
				thank(p1name,p2name,pp1,pp2)
				break
		turn=turn+1
play()

		

		