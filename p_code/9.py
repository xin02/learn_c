a = ["24","00","05","36","65","07","27","26","2D","01","03","00","0D","56","01","03","65","03","2D","16","02","15","03","65","00","29","44","44","01","44","2B"]
b = 'L3t_ME_T3ll_Y0u_S0m3th1ng_1mp0rtant_A_{FL4G}_W0nt_b3_3X4ctly_th4t_345y_t0_c4ptur3_H0wev3r_1T_w1ll_b3_C00l_1F_Y0u_g0t_1t'
s = ''
for i in range(len(a)):
	s += b[int(a[i],16)]
print(s)

s1 = "this_is_not_flag"
s2 = [0x12, 4, 8, 0x14, 0x24, 0x5c, 0x4a, 0x3d, 0x56, 0xa, 0x10, 0x67, 0,
		0x41, 0, 1, 0x46, 0x5a, 0x44, 0x42, 0x6e, 0x0c,
		0x44, 0x72, 0x0c, 0x0d, 0x40, 0x3e, 0x4b, 0x5f, 2, 1, 0x4c, 0x5e, 
		0x5b, 0x17, 0x6e, 0xc, 0x16, 0x68, 0x5b, 0x12]

flag = ""

for i in range(len(s2)):
	flag += chr(s2[i] ^ ord(s1[i % 16]))
	'''print(ord(s1[i % 16]))
	print(chr(s2[i]))
	print(chr(s2[i] ^ ord(s1[i % 16])))
	print(104 ^ 4)
	print(chr(104 ^ 4))'''
print(flag)