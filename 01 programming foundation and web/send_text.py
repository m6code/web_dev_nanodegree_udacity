from twilio.rest import Client

account_sid = "AC5b213cabb4007b167882da6ba576db5d"
auth_token = "404089f2a7fd84edb75fe7d89cc35328"
client = Client(account_sid, auth_token)

# # Making Call
# call = client.calls.create(
# 	to="+23408087737820",
# 	from_="+18065471588",
# 	url="http://demo.twilio.com/docs/voice.xml"
# )
#
# print(call.sid)

# Sending SMS
message = client.messages.create(
	to="+23408087737820",
	from_="+18065471588",
	body="Web development test Sent By Benjamin")

print(message.sid)
