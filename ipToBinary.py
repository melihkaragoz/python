print("<< Convert ip address to binary >>")
def convert(_decimal):
	_decimal = _decimal.replace(' ','.')
	bits,octets = [],_decimal.split(".")
	for i in range(len(octets)):
		octet,_octet = int(octets[i]),""
		for j in range(8):
			chk = True if (octet-(pow(2,(7-j)))) >= 0 else False
			if(chk):
				octet -= pow(2,(7-j))
				_octet += "1"
			else:   _octet += "0"
		bits.append(_octet)
		_octet = ""
	print(bits)

decimal = str(input("ip : "))
convert(decimal)
