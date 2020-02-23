from parserpackage import AddressParser

if __name__=='__main__':
    # Testing if the package is working or not
    test_object = AddressParser()
    print(test_object.parse_address('JL DAAN MOGOT KM 145 PESAKIH RT 3 RW 14, DURI KOSAMBI KOTA ADM. JAKARTA BA'))

