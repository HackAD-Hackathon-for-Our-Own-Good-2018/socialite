import get_from_db
import insert_db
import random

def get_match_pairs():
    allUsers = get_from_db.getFromDatabase()
    all_ids = allUsers.keys()

    # Shuffle the list of all user ids
    random.shuffle(all_ids)
    
    # Make a list to store ones who are already matched
    already_matched = []

    # Iterate over all the ids 
    for nid in all_ids:

        # Get the ids you shouldn't match to, then construct a list of valid ids to match with
        dont_match = allUsers[nid]['already_met'].split(',')
        match_ok = [item for item in all_ids not in dont_match]
        match_ok = [item for item in match_ok not in already_matched]

        # Pick the first person from the valid list, add both to the list of already matched people
        second_person = match_ok[0]
        already_matched.append(nid)
        already_matched.append(second_person)

        # Update the database to update each user's already met list
        p2_dont_match = allUsers[second_person]['already_met'].split(',')
        updateDatabase(nid,dont_match, second_person, p2_dont_match)




get_match_pairs()
