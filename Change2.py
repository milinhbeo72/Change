def main():
    purchase_price = input("Purchase price: ")
    paid_amount_money = input("Paid amount of money: ")
    offer_change = int(paid_amount_money) - int(purchase_price)


    if offer_change <= 0:
        print("No change")
    else:
        print('Offer change:')
        a = offer_change // 10
        if a > 0:
            b = offer_change % 10
            print(a, 'ten-euro notes')
            if b >= 5:
                a1 = b // 5
                b1 = b % 5
                print(a1,'five-euro notes')
                if b1 >= 2:
                    a2 = b1 //2
                    b2 = b1 % 2
                    print(a2, 'two-euro coins')
                    if b2 >=1:
                        print(1,'one-euro coins')
                    else:
                        None

                else:
                    print(1,'one-euro coins')
            elif b >=2:
                a1 = b // 2
                b1 = b % 2
                print(a1,'two-euro coins')
                if b1 ==1:
                    print(1,'one-euro coins')
                else:
                    None
            elif b>1:
                print(1,'one-euro coins')
            else:
                None

        if a == 0:
            a1 = offer_change // 5
            if a1 > 0:
                b1 = offer_change % 5
                print(a1,'five-euro notes')
                if b1 >= 2:
                    a2 = b1 // 2
                    print(a2,'two-euro coins')
                elif b1 >1:
                    print (1,'one-euro coins')
                else:
                    None
            if a1 ==0:
                a2 = offer_change // 2
                if a2 > 0:
                    b2 = offer_change % 2
                    print(a2,'two-euro coins')
                    if b2 >1 :
                        print(1,'one-euro coins')
                    else:
                        None
                if a2 == 0:
                    print(1,'one-euro coins')





main()





