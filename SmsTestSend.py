from  twilio.rest import Client
from apisms.api import auth_token,account_sid


def seding_sms(text=None,reciever='+37360088398'):

    try:
        client = Client(account_sid,auth_token)

        message = client.messages.create(
            body = text,
            from_ = '13852824398',
            to=reciever
        )

        return 'The message succeseful sent'

    except Exception as ex:

        return f' Error {ex} '


def main():

    text = input('введите свой текст смски : ' )
    print(seding_sms(text=text))

if __name__ == '__main__':
    main()