import os
from dotenv import load_dotenv
from vonage_voice import CreateCallRequest, Talk, Phone
from vonage import Auth, Vonage
import argparse

# Set up argument parser

parser = argparse.ArgumentParser(
    prog='make-call',
    description='a simple program to make a hello world call using Vonage Voice API')
parser.add_argument('-f', '--from', type=str, required=True, help='the phone number to make the call from (in E.164 format) like 33612345678')
parser.add_argument('-t', '--to', type=str, required=True, help='the phone number to make the call to. can be a phone number (in E.164 format) like 33612345678 or a SIP URI like sip:')
parser.add_argument('-s', '--sip', type=bool, help='True if the destination is a SIP URI', default=False)
parser.add_argument('-l', '--loop', type=int, default=3, help='number of times to repeat the message')
parser.add_argument('-m', '--message', type=str, default='Hello world', help='the message to be spoken during the call')
args = parser.parse_args()
print(args)

from_number = args.__getattribute__('from')
to_adress = args.to
is_sip = args.sip
loop_count = args.loop
message = args.message

# Load environment variables from .env file

load_dotenv()  # take environment variables from .env.

# Create an Auth instance
auth = Auth(
    application_id=os.getenv("VONAGE_APPLICATION_ID"), private_key=os.getenv("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
)


# Create a Vonage client instance
vonage_client = Vonage(auth=auth)

print("api key:",os.getenv("VONAGE_APPLICATION_ID"))


ncco = [Talk(text=message, loop=loop_count, language='en-GB')]

call = CreateCallRequest(
    from_=Phone(number=from_number),
    to=[{'type': 'sip', 'uri': to_adress}] if is_sip else [{'type': 'phone', 'number': to_adress}],
    ncco=ncco,
)

response = vonage_client.voice.create_call(call)
print(response.model_dump())
