http_status=200

if http_status == 230 or http_status == 200:
    print ('its ok')
elif http_status == 300 :
    print ('also ok')
elif http_status == 400 :
    print ('not ok')
elif http_status == 402 or http_status == 403 :
    print ('also not ok')
else:
    print ('not valid input')


match http_status:
        case 230 | 200 :
            print ('its ok')
        case 300 :
            print ('also ok')
        case 400 :
            print ('not ok')
        case 402 | 403 :
            print ('also not ok')
        case _:
            print ('not valid input')