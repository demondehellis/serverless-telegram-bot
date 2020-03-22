
# def index_users(event, context):
#         # streams
#     for record in event.get('Records'):
#         if record.get('eventName') in ('INSERT', 'MODIFY'):
#             user_id = record['NewImage']['userId']['N']
#             email = record['NewImage']['emailAddress']['S']
#             fullname = record['NewImage']['fullname']['S']
#             date_of_birth = record['NewImage']['date_of_birth']['S']

#             index_user(
#                 user_id=user_id,
#                 email=email,
#                 fullname=fullname,
#                 date_of_birth=date_of_birth
#             )
            
#             logger.info('Indexed user Id {}'.format(user_id)
#         elif record.get('eventName') == 'DELETE':
#             user_id = record['Keys']['userId']['N']
#             remove_user_from_index(user_id=user_id)

#             logger.info('Removed user Id {} from index'.format(user_id)


# import json

# from crm import save_user, mark_user_as_deleted
# from fullcontact import enrich_user
# from log import logger

# def index_users(event, context):

#     for record in event.get('Records'):
#         email = record['NewImage']['emailAddress']['S']

#         try:
#             if record.get('eventName') in ('INSERT', 'MODIFY'):
#                 # Add additional user info from FullContact
#                 enriched_user = enrich_user(email=email)

#                 # Save to our CRM
#                 save_user(enriched_user)

#                 logger.info('Added {} to CRM'.format(email)
#             elif record.get('eventName') == 'DELETE':
#                 mark_user_as_deleted(email=email)

#                 logger.info('Marked {} as deleted in CRM'.format(email)
        
#     except Exception as e:
#         logger.error("Failed to update {email} in CRM. Error: {error}".format(email=email, error=str(e))