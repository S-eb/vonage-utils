import os
from dotenv import load_dotenv
from vonage_voice import CreateCallRequest,  PhoneEndpoint, Connect
from vonage import Auth, Vonage
import argparse

# Set up argument parser

parser = argparse.ArgumentParser(
    prog='make-call',
    description='a simple program to make a hello world call using Vonage Voice API')
parser.add_argument('-t', '--to', type=str, required=True, help='the phone number to make the call from (in E.164 format) like 33612345678')
parser.add_argument('-s', '--sip', type=str, required=True, help=' SIP URI')
args = parser.parse_args()
print(args)

to_number = args.to
to_address = args.sip

# Load environment variables from .env file

load_dotenv()  # take environment variables from .env.

# Create an Auth instance
auth = Auth(
    application_id=os.getenv("VONAGE_APPLICATION_ID"), private_key=os.getenv("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
)


# Create a Vonage client instance
vonage_client = Vonage(auth=auth)

print("api key:",os.getenv("VONAGE_APPLICATION_ID"))


ncco = [Connect(randomFromNumber=True,endpoint=[PhoneEndpoint(number=to_number)])]
call = CreateCallRequest(
    random_from_number=True,
    to=[{'type': 'sip', 'uri': to_address}],
    ncco=ncco
)

response = vonage_client.voice.create_call(call)
print(response.model_dump())
