import boto3
 
AWS_ACCESS_KEY = 'AKIAIY2232MUPDD4R2UA'
AWS_SECRET_ACCESS_KEY ='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'
AWS_REGION = 'eu-west-1'
 
client_comprehend = boto3.client(
    'comprehend',
    region_name = AWS_REGION ,
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY    
)

# dominant_language_response = client_comprehend.detect_dominant_language(
#     Text='your plain text here'
# )
# #Print the dominant language
# print(sorted(dominant_language_response['Languages'], key=lambda k: k['LanguageCode'])[0]['LanguageCode'])



# response_entities = client_comprehend.detect_entities(
#         Text='your plain text here',
#         LanguageCode='en'
# )
# # get the entities
# entites = list(set([x['Type'] for x in response_entities['Entities']]))


response_sentiment = client_comprehend.detect_sentiment(
    Text='your plain text here',
    LanguageCode='en'
)
# get the sentiment
sentiment = response_sentiment['Sentiment']
print(sentiment)
