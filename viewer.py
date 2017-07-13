#Ticket Viewer designed for compatibility with Zendesk API and implemented
#to access tickets stored on ckavadias account, some syntax mainly in the
#print statements has been designed to render in the same manner in both
#python 2 and 3 interpreters, however this is written with the intention to
#be interpreted as python 3 and may have undefined behaviour otherwise

#Author: Constantinos Kavadias
#Email: ckavadias@student.unimelb.edu.au or kavacon@icloud.com
#July 2017
from six import print_
import requests as req
import platform

#global shared variables across functions
URL = "https://ckavadias.zendesk.com/api/v2/tickets.json"
AUTH = ("ckavadias@student.unimelb.edu.au", "letmein")
VERSION = platform.python_version()[0]
TOTAL_PAGE = 25
MAX_PAGE = 100
MAX_LINE = 40

#check that input matches python version
def check_input(message):
    try:
        selection = input(message)
    except NameError:
        print_("\nThat doesn't have appeared to be correctly formatted.")
        print_("Don't forget, place your selection in ' ' or \" \" in python 2.")
        selection = check_input(message)
    
    return str(selection)
        
#print sign off message and exit execution
def leave_function():
    print_("\nIt appears my services are no longer required, good bye.\n")
    raise SystemExit

#check that connection was successful
def check_status(raw):
    if raw.status_code != req.codes.ok:
        try:
            raw.json()["error"]
            error = raw.json()["error"]
        except KeyError:
            error = "Connection failed"       
        
        print_("\nThe following error occurred:")
        print_("\n\t - "+error+" -\n")
        print_("Contact your administrator or try again.")
        print_options()

        return False
    return True

#print out a detailed rendering of a selected ticket
def print_ticket(ticket):

    formats = [('\nCREATED:', "created_at"), ("SUBJECT:","subject"),
               ("\nDESCRIPTION:", "description"), ("\nTICKET ID:", "brand_id"),
               ("REQUESTED BY:", "requester_id"),
               ("ASSIGNED TO:", "assignee_id"),("OPEN/CLOSED:", "status")]
    
    #all fields will be tried first to avoid a KeyError crash
    try:
        print_('-'*8,"Ticket number:",ticket["id"],'-'*8)
    except KeyError:
        print_('-'*8,"Ticket number: unavailable",'-'*8)
        
    for pair in formats:
        print_(pair[0], end = ' ')
        try:
    #formatting to esnure fields don't go off page
            if len(str(ticket[pair[1]])) > MAX_LINE - len(pair[0]):
                start = 0
                end = MAX_LINE - len(pair[0])
                while end < len(ticket[pair[1]]):
                    print_(ticket[pair[1]][start:end])
                    start = end
                    end+=MAX_LINE
            else:
                print_(ticket[pair[1]])
        except KeyError:
            print_("unavailable")
    
    #select from more fields to view or finish the viewing
    #this feature has been deactivated as it strays from the spec
    #and makes usage more complicated than necessary
    '''while True:
        print_("\nYou may select from the following options to continue:")
        print_("\t'finish'    | Exit the selection")
        print_("\t'custom'    | Select a custom field to view")
        print_("\t'leave'     | Quit the viewer")

        selection = check_input("\nI pick: ")
        if selection == "finish":
            break
        elif selection == "custom":
            custom = check_input("\nPlease type your selection as a json field: ")
            print_("\nYour selection:", end = ' ')
            try:
               print_(ticket[custom], "\n")
            except KeyError:
                print_("unavailable or invalid\n")
        elif selection == "leave":
            leave_function()
        else:
            print_("That wasn't one of my suggestions, try again :)")'''
    return

    
    
#print all tickets contained in page
def print_tickets(page, count, total):
    
    start = total*TOTAL_PAGE - 24

    print_("\t"+"-"*8 + "Total entries: "+str(count) + "-"*8 +"\t")
    if count == 0:
        print_("\nI'm deeply sorry, it appears there are no tickets to display.")
        return

    print_("Displaying "+ str(start)+" to " + str(start +len(page) - 1))
    print_("Ticket no. | \t\t\tTicket details")
    for entry in page:
        print_(5*' '+ str(start) + (6-len(str(start)))*' '+"|",end = " ")
        print_("'"+entry["subject"] + "'  submitted by", end = "  '")
        print_(str(entry["submitter_id"]) + "'  on the day", end = "  '")
        print_(entry["created_at"], end = "'\n")
        start+=1
    return

#print all command options available(may be referred to as main menu
#in documentation
def print_options():
    print_("\nType one of the following then press enter:")
    print_("\t'tickets' | View all available tickets.")
    print_("\t'select'  | View a specific ticket (have the ticket number ready).")
    print_("\t'leave'   | Quit the viewer.")
    print_("\t'options' | Make me repeat myself.")
    return

#helping function to perform GET for tickets and related operations
def get_tickets():
    params = {"per_page":TOTAL_PAGE, "page": 1}

    while True:

        #retrieve page and check for any possible errors 
        raw = req.get(url = URL, params = params, auth = AUTH)
        if check_status(raw):
            data = raw.json()
        else:
            break
        
        try:
            page = data["tickets"]
        except KeyError:
            print_("No tickets appear to have been returned,", end=' ')
            print_("maybe try again later, good bye.")
        
        next_page = data["next_page"]
        prev_page = data["previous_page"]

        #provide further options to continue session
        print_tickets(page, data["count"], params["page"])
        print_("\nYou may type the following and press enter to proceed:")
        print_("\t'next'      | View next page")
        print_("\t'previous'  | View previous page")
        print_("\t'select'    | View a specific ticket (have the", end = ' ')
        print_("ticket number ready")
        print_("\t'options'   | Return to the options menu")
        print_("\t'leave'     | Quit the viewer.")

        selection = check_input("\nI pick: ")

        if selection == "leave":
            leave_function()
            break
        
        elif selection == "next":
            if next_page == None:
                print_("\nThere is no next page, try another option")
                print_("Here's that page again in case you need it\n")
            else:
                print_()
                params["page"]+=1
                
        elif selection == "previous":
            if prev_page == None:
                print_("\nThere is no previous page, try another option")
                print_("Here's that page again in case you need it\n")
            else:
                params["page"]-=1
                
        elif selection == "select":
            get_ticket()
            break
        
        elif selection == "options":
            print_options()
            break

        else:
            print_("That wasn't one of my suggestions, try again :)")
            print_("Here's that page again in case you need it\n")
              
    return

#render a selected ticket
def get_ticket():
    ticket = int(check_input("\nPlease type the ticket number and press enter: "))
    params = {"per_page": MAX_PAGE, "page": ticket//MAX_PAGE + 1}
    
    print ("Retrieving ticket number "+str(ticket)+" one moment please.\n")

    #retrieve page containing ticket and check for any possible errors         
    raw = req.get(url = URL, params = params, auth = AUTH)
    if check_status(raw):
        data = raw.json()
    else:
        return
    
    try:
        page = data["tickets"]
    except KeyError:
        print_("No tickets appear to have been returned,", end=' ')
        print_("maybe try again later, good bye.")

    try:
        retrieved = page[ticket%MAX_PAGE - 1]
    except IndexError:
        print_("\nThat ticket doesn't appear to be available.")
        print_("I'm now returning to the options menu")
        print_options()
        return

    #print ticket content
    print_ticket(retrieved)
    #provide further options to continue with session
    while True:
        print_("\nYou may type the following and press enter to proceed:")
        print_("\t'options'   | Return to the options menu")
        print_("\t'leave'     | Quit the viewer")

        selection = check_input("\nI pick: ")

        if selection == "leave":
            leave_function()
            return
        elif selection == "options":
            print_options()
            return
        else:
            print_("That wasn't one of my suggestions, try again :)")
        
    return

#usage warning for python 2 users
if VERSION == '2':
    print_("\nWARNING: Python 2 will behave differently to Python 3.")
    print_("When selecting from the options presented please ensure")
    print_("you surround your chosen option with ' ' or \" \" so that")
    print_("the Python 2 interpreter can recognise it.")
    print_("example: type 'leave' to select leave.\n\n")

#startup welcome message    
print_("\nWelcome, my name's Alfred\nI will be assisting with your tickets\n")
print_("    To view command options type 'options' then press enter")
print_("    Alternatively to quit type 'leave' then press enter.\n")

#body and decision maker, uses linguistic input to determine what the user
#is requesting 
while True:
    option = check_input("\nI pick: ")
    
    if len(option.split() )> 1:
        print_("I'm sorry I can't understand sentences with more than one")
        print_("word, you'll have to try again, for a list of options please")
        print_("type options, alternatively you may end your session by typing")
        print_("leave.")
        
    elif option == "leave":
        break
    
    elif option == "options":
        print_options()

    elif option == "tickets":
        get_tickets()

    elif option == "select":
        get_ticket()
        
    else:
        print_("That wasn't one of my suggestions, here they are again :)")
        print_options()


leave_function()
