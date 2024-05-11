bianca = 0
edward = 0
felicia = 0
votes = []

def id_check(voter_id)-> bool:
    '''
    :param: voter_id
    :return: False if ID is not a number or the voter ID has already been used
    :return: True if ID is a number and hasn't been used
    Saves the voter ID in list when ID button is pressed and returns true or false based on if it was valid
    '''
    if not voter_id.isdigit():
        return False
    if voter_id in votes:
        return False
    votes.append(voter_id)
    return True

def vote_for(candidate_name)-> None:
    '''
    :param: candidate name

    Makes bianca, edward, and felicia global variables that can be changed
    When a vote button is clicked for the candidate, it adds 1 to the selected candidate
    '''
    global bianca, edward, felicia
    if candidate_name == "Bianca":
        bianca += 1
    elif candidate_name == "Edward":
        edward += 1
    elif candidate_name == "Felicia":
        felicia += 1



def get_individual_votes()-> int:
    '''
    :returns: bianca, edward, and felicia 
    Returns the total of each candidates votes
    '''
    return bianca, edward, felicia
