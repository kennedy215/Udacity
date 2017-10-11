from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC579b349414e2ab43c186ca84b9a6403b"
# Your Auth Token from twilio.com/console
auth_token  = "f85ea251a7a877325e73d6719fc57660"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16199448565", 
    from_="+16197848217",
    body="I'm going to eat you")

print(message.sid)
