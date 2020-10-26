#dead or alive?

person = {'name': 'brian', 'status': 'alive'} #making the dictionary

print ('Hello. This is a small program using a dictionary to determine ' +
       'different outcomes based on what the user presses') #welcome message
beenshot =(input('\nWe have a man called brian. He has been shot in the ' +
                     'chest 3 times. Does he die from initial wounds? y/n'))

if beenshot == 'y': #if else to determine whether player has killed brian
    person['status'] = 'dead' #if he dies, this changes the dic val to dead instead of alive
    print ('\nEnding 01: Brian is:',person['status'],'. He has been shot and died on the scene')
else:
    diedhospital =(input('Brian has been rushed to the hospital. Does he die in the ' +
           'hospital later on due to blood loss? y/n'))
#if player decided not to kill him, they get another prompt to see if he dies
    if diedhospital == 'y': #second if/else for second user choice
        person['status'] = 'dead'
        print ('\nEnding 02: Brian is:', person['status'], '. He has died in the hospital')
    else:
        print ('\nEnding 03: Brian is:', person['status'])
#third ending is player decided brian did not die

print ('Thank you for playing my simple game')
#thank you message at the end
    
    
