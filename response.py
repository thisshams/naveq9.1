import re
import long_response as long



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calculate the percent of recognised words in user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response-----------------------------------------
    response('Hello,How can i help you? ', ['hello', 'hii','hi', 'hye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','are','you'])
    response('Thank you', ['i', 'love', 'code'], required_words=['love', 'code'])
    response(" i don't like eating anything because i'm a bot obviously!" , ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.acc_off, ['where','is','account','section','?'], required_words=['where','account','section'])
    response(long.acc_off,['where','is','account','office','?'], required_words=['where','account','office'])
    
    response(long.cs_hod,['Who','is','the','hod','of','computer','science','branch','?'], required_words=['hod','computer','science'])
    response(long.cs_hod,['Who','is','the','head','of','department','cs','branch','?'], required_words=['head','department','cs'])
    response(long.cs_hod,['Who','is','the','head','of','department','computer','science','branch','?'], required_words=['head','department','computer','science'])
    response(long.course,['which','type','of','course','conduct','in','srit','?'],required_words=['type','course','srit'])
    response(long.cs_hod,['Who','is','the','hod','of','cs','branch','?'], required_words=['hod','cs'])
    response(long.chairman, ['who','is','chairman','of','shri','ram','group'], required_words=['chairman','shri','ram'])
    response(long.director, ['who','is','director','of','shri','ram','group'], required_words=['director','shri','ram'])
    response(long.principal_srit, ['who','is','principal','of','srit'],required_words=['principal','srit'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match]<1  else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# testing the response system
