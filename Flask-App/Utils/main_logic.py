import db_helpers, sendemail
import random

subject = 'ConnectNYUAD: Match for this Week'
message = '''Typing the message here'''

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

        # Fire Email function here
        # sendemail.send_email(person, second_person, subject, message)

        print("Person 1", person)
        print("Person 2", second_person)

get_match_pairs()
