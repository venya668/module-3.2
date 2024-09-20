def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' and ('.com' or '.ru' or '.net') not in (recipient or sender) or ('@' or ('.com' or '.ru' or '.net')) not in (recipient or sender):

        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('messagje','university.help@gmail.com','venik@.com')
send_email('messagje','university.help@gmail.com')
send_email('messagje','universi@.com')
send_email('messagje','universi@.')
send_email('messagje','uni.com')