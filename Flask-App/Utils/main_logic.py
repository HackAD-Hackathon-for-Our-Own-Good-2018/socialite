import db_helpers, sendemail
import random

platforms = ['facebook/messenger', 'instagram', 'whatsapp']
subject = 'ConnectNYUAD: Match for this Week'
message2 = '''
Dear {fname1} and {fname2}!

You have been matched for this week!

In the upcoming week, you have the opportunity to reach out and get to know each other. You can reach out to each other via email (just reply to this thread){platforms}. Don't be afraid to start the conversation - your match is just as willing to meet new people as you are! 

Every person has three things that they want others to know These might turn out to be good conversation starters to move past the generic questions. The three things you want each other to know are:
{pname1} - {things1}
{pname2} - {things2}

Be creative! - Ask people their hobbies and passions, or tell them yours. You are bound to have something in common! Be nice and open-minded. Kindness and mutual respect are not only the cornerstones of the NYUAD spirit, but also of any good friendship. 
Good luck!

Warm Regards
ConnectNYUAD team

(THIS IS A TEST! Thanks for bearing with us. -The Gabrus)
'''

message3 = '''
Dear {fname1}, {fname2} and {fname3},

You have been matched for this week!

In the upcoming week, you have the opportunity to reach out and get to know each other. You can either do this individually or meet as a group. You can reach out to each other via email (reply to this thread){platforms}. Don't be afraid to start the conversation - your match is just as willing to meet new people as you are! 

Every person has three things that they want others to know. These might turn out to be good conversation starters to move past the generic questions. The three things you want each other to know are:
{pname1} - {things1}
{pname2} - {things2}
{pname3} - {things3}

Be creative! - Ask people their hobbies and passions, or tell them yours. You are bound to have something in common! Be nice and openminded! Kindness and mutual respect are not only the cornerstones of the NYUAD spirit, but also of any good friendship. 
Good luck!

Warm regards,
ConnectNYUAD team

(THIS IS A TEST! Thanks for bearing with us. -The Gabrus)
'''

def get_match_pairs():
    allUsers = db_helpers.getFromDatabase()
    all_ids = allUsers.keys()

    # Shuffle the list of all user ids
    random.shuffle(all_ids)
    
    # Make a list to store ones who are already matched
    already_matched = []

    print "All Ids", all_ids

    # odd case
    if len(all_ids)%2:

        # First match 3 people who haven't met 
        p1 = all_ids.pop()
        p1_dont_match = allUsers[p1]['already_met'].split(',')
        p1_ok = [item for item in all_ids if item not in p1_dont_match]

        p2 = p1_ok[random.randint(0, len(p1_ok)-1)]
        p2_dont_match = allUsers[p2]['already_met'].split(',')
        p2_ok = [item for item in all_ids if item not in p2_dont_match]

        p1_p2_ok = [item for item in p1_ok if item in p2_ok]
        p3 = p1_p2_ok[random.randint(0, len(p1_p2_ok)-1)]

        # Update each dontmatch 
        p1_dont_match.append(p2)
        p1_dont_match.append(p3)

        p2_dont_match.append(p1)
        p2_dont_match.append(p3)

        p3_dont_match = allUsers[p3]['already_met'].split(',')
        p3_dont_match.append(p1)
        p3_dont_match.append(p2)

        db_helpers.updateDatabase(p1, p1_dont_match)
        db_helpers.updateDatabase(p2, p2_dont_match)
        db_helpers.updateDatabase(p3, p3_dont_match)

        all_ids.remove(p2)
        all_ids.remove(p3)

        platform = ''
        p1_plat = [int(allUsers[p1]['check_fb']), int(allUsers[p1]['check_ig']), int(allUsers[p1]['check_wa'])]
        p2_plat = [int(allUsers[p2]['check_fb']), int(allUsers[p2]['check_ig']), int(allUsers[p2]['check_wa'])]
        p3_plat = [int(allUsers[p3]['check_fb']), int(allUsers[p3]['check_ig']), int(allUsers[p3]['check_wa'])]
        
        platList = []
        for i in range(3):
            if p1_plat[i] and p2_plat[i] and p3_plat:
                platList.append(platforms[i])

        if platList:
            platform=", or "+", ".join(platList)

        # Email
        msg = message3.format(
            fname1 = allUsers[p1]['full_name'],
            fname2 = allUsers[p2]['full_name'],
            fname3 = allUsers[p3]['full_name'], 
            platforms=platform,
            pname1 = allUsers[p1]['pref_name'],
            things1 = allUsers[p1]['3_things'], 
            pname2 = allUsers[p2]['pref_name'],
            things2 = allUsers[p2]['3_things'], 
            pname3 = allUsers[p3]['pref_name'],
            things3 = allUsers[p3]['3_things']
        )
        # print(msg)
        sendemail.send_email([p1,p2,p3], subject, msg)


    # Iterate over all the ids 
    for person in all_ids:

        # Skip current iteration if person already present
        if person in already_matched:
            continue

        # Get the ids you shouldn't match to, then construct a list of valid ids to match with
        p1_dont_match = allUsers[person]['already_met'].split(',')
        match_ok = []
        match_ok = [item for item in all_ids if item not in p1_dont_match]
        match_ok = [item for item in match_ok if item not in already_matched]

        # Pick the first person from the valid list, add both to the list of already matched people
        second_person = match_ok[0]
        already_matched.append(person)
        already_matched.append(second_person)

        # Update the database to update each user's already met list
        p2_dont_match = allUsers[second_person]['already_met'].split(',')

        # Update each user's dontmatch list to not repeat matching
        p2_dont_match.append(person)
        p1_dont_match.append(second_person)

        db_helpers.updateDatabase(person, p1_dont_match)
        db_helpers.updateDatabase(second_person, p2_dont_match)

        platform = ''
        p1_plat = [int(allUsers[person]['check_fb']), int(allUsers[person]['check_ig']), int(allUsers[person]['check_wa'])]
        p2_plat = [int(allUsers[second_person]['check_fb']), int(allUsers[second_person]['check_ig']), int(allUsers[second_person]['check_wa'])]
        
        platList = []
        for i in range(3):
            if p1_plat[i] and p2_plat[i]:
                platList.append(platforms[i])

        if platList:
            platform=", or "+", ".join(platList)

        # Fire Email function here
        msg = message2.format(
            fname1 = allUsers[person]['full_name'],
            fname2 = allUsers[second_person]['full_name'],
            platforms=platform,
            pname1 = allUsers[person]['pref_name'],
            things1 = allUsers[person]['3_things'], 
            pname2 = allUsers[second_person]['pref_name'], 
            things2 = allUsers[second_person]['3_things']
        )

        # print(msg)
        sendemail.send_email([person, second_person], subject, msg)

        # print("Person 1", person)
        # print("Person 2", second_person)

get_match_pairs()
