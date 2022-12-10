import re
import long_reply as long



def message_reliability(user_message, accepted_words, single_reply=False,essential_words=[]):
    message_reliability = 0
    has_essential_words = True

    for word in user_message:
        if word in accepted_words:
            message_reliability += 1

    # Computes the percentage of words that can be recognised in the user message
    percentage = float(message_reliability) / float(len(accepted_words))

    # Matching user message to essential words
    for word in essential_words:
        if word not in user_message:
            has_essential_words = False
            break

    if has_essential_words or single_reply:
        return int(percentage * 100)
    else:
        return 0

    # Creating a dictionery
def check_all_messages(message):
    highest_prob_list = {}

    #makes reply creation easy
    def reply(bot_reply, list_of_words, single_reply =False, essential_words =[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_reply] = message_reliability(message, list_of_words, single_reply, essential_words)

# reply@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    reply('Hello', ['hello' ,'hi', 'sup','hey','heyo'], single_reply=True)
    reply('see you',['bye','goodbye'],single_reply=True)
    reply('I\'m doing fine ,and you?',['how', 'are','you', 'doing'], essential_words=['how'])
    reply('You\re welcome',['thank','thanks'],single_reply=True)
    reply('Thank you',['i','love','code','palace'], essential_words=['code','palace'])
    # Handling long_replys
    reply(long.R_ADVICE,['give','advice'], essential_words=['advice'])
    reply(long.R_EATING, ['what','you' 'eat'], essential_words=['you','eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)


    return best_match

def get_reply(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    reply = check_all_messages(split_message)
    return reply


while True:
    print('Bot:' + get_reply(input('You: ')))
