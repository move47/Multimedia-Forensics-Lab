import wave
import random
import numpy as np
def case(a):
	if a == 1:
		encode()
	elif a == 2:
		decode()
	elif a == 3:
		quit()
	else:
		print("\nEnter valid Choice!")
def check(secret_msg, decoded_msg):
	for i in range(0,len(decoded_msg)):
		if secret_msg[i] !=decoded_msg[i]:
			print("Error in decoding at",i)
			return
	print("No error")
	return
def generate_random_bits(n):
	random_bits = []
	for i in range(n):
		x = random.random()
		if x>=0.5:
			random_bits.append(1)
		else:
			random_bits.append(0)
	return random_bits
def bit_stuffing(bitts):
	stuffed_bits = list()
	# Now do bit stuffing
	i = 0
	while(i<len(bitts)):
		current_sequence = ''.join(map(str,bitts[i:i+6]))
		if current_sequence == "011111":
			stuffed_bits = stuffed_bits + [0,1,1,1,1,1,0]
			i = i+6
		else:
			stuffed_bits = stuffed_bits + [bitts[i]]
			i = i+1
		
		#print(i,stuffed_bits)
	
	delimiter_bits = [0,1,1,1,1,1,1,0]
	stuffed_bits = stuffed_bits + delimiter_bits

	# Making it multiple of 3
	if(len(stuffed_bits)%3==1):
		stuffed_bits = stuffed_bits + [1,1]
	elif(len(stuffed_bits)%3==2):
		stuffed_bits = stuffed_bits + [1]
	#print(bitts,"\n", stuffed_bits)
	return stuffed_bits


def bit_unstuffing(stuffed_bits):
		# Bit Un-stuffing
	j = 0
	original_msg = []
	last_6_bits = ""
	while(1):
		#print(j)
		if(len(last_6_bits)<6):
			last_6_bits = last_6_bits+ str(stuffed_bits[j])
			original_msg.append(stuffed_bits[j])
		elif(last_6_bits=="011111" and stuffed_bits[j]==1 and stuffed_bits[j+1]==0):
			#print(j,last_6_bits,stuffed_bits[j],stuffed_bits[j+1])
			original_msg = original_msg[:-6]
			break
		elif(last_6_bits=="011111" and stuffed_bits[j]==0):
			last_6_bits = " "#last_6_bits[1:] + str(stuffed_bits[j])
		else:
			original_msg.append(stuffed_bits[j])
			last_6_bits = last_6_bits[1:] + str(stuffed_bits[j])
		#print(j,last_6_bits)
		j = j+1

	
	#print(bitts,'\n',stuffed_bits,'\n',original_msg)
	return original_msg
def unstuffing(original_msg,stuffed_bits,last_6_bits):
		# Bit Un-stuffing
	j = 0
	#original_msg = []
	#last_6_bits = ""
	while(j<3):
		#print(j)
		if(len(last_6_bits)<6):
			last_6_bits = last_6_bits+ str(stuffed_bits[j])
			original_msg.append(stuffed_bits[j])
		elif(last_6_bits=="011111" and stuffed_bits[j]==1 and stuffed_bits[j+1]==0):
			#print(j,last_6_bits,stuffed_bits[j],stuffed_bits[j+1])
			original_msg = original_msg[:-6]
			break
		elif(last_6_bits=="011111" and stuffed_bits[j]==0):
			last_6_bits = " "#last_6_bits[1:] + str(stuffed_bits[j])
		else:
			original_msg.append(stuffed_bits[j])
			last_6_bits = last_6_bits[1:] + str(stuffed_bits[j])
		#print(j,last_6_bits)
		j = j+1

	
	#print(bitts,'\n',stuffed_bits,'\n',original_msg)
	
	return original_msg

def encode():
	secret_key = int(input("\nSecret Key:"))
	mapping_info = {	
						"000":["000","001","010","011","001","000","011","010"],
						"001":["000","001","010","011","001","000","011","010"],
						"010":["000","001","010","011","001","000","011","010"],
						"011":["101","001","010","011","001","101","011","010"],
						"100":["101","100","111","110","100","101","110","111"],
						"101":["101","100","111","110","100","101","110","111"],
						"110":["101","100","111","110","100","101","110","111"],
						"111":["101","100","111","110","100","101","110","111"]
					}
	#print(mapping_info["000"][int("010",2)])
	print("\nEncoding Starts..")
	audio = wave.open("cover_audio.wav",mode="rb")
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	print(audio.getnframes())
	print(len(frame_bytes))
	# print(frame_bytes[0:5])
	# for i in range(0,5):
	#  	print(frame_bytes[i])
	
	# So try as each frame as 2 channels and each sample size is 2 bytes so try changin it and see what happens!! 
	
	#string = "Spiderman is Peter Parker"
	#string = 'a'
	#string = "The meeting is regarding discussion on Budget 2021"
	string = "Secure multiparty computation MPC often relies on sources of correlated randomness for better efficiency and simplicity. This is particularly useful for MPC with no honest majority, where input-independent correlated randomness enables a lightweight non-cryptographic online phase once the inputs are known. However, since the amount of correlated randomness typically scales with the circuit size of the function being computed, securely generating correlated randomness forms an efficiency bottleneck, involving a large amount of communication and storage. A natural tool for addressing the above limitations is a pseudorandom correlation generator (PCG). A PCG allows two or more parties to securely generate long sources of useful correlated randomness via a local expansion of correlated short seeds and no interaction. PCG enable MPC with silent preprocessing, where a small amount of interaction used for securely sampling the seeds is followed by silent local generation of correlated pseudorandomness. A concretely efficient PCG for Vector-OLE correlations was recently obtained by Boyle et al. (CCS 2018) based on variants of the learning parity with noise (LPN) assumption over large fields. In this work, we initiate a systematic study of PCG and present concretely efficient constructions for several types of useful MPC correlations. We obtain the following main contributions"
	#string = "The motivation of this offline-online approach is that the online phase is expected to be made fast by using only inexpensive computation. This is particularly useful in settings where parties know in advance that some computation has to be performed, and low online latency is desired. A classical example is the one of an airline company that wants to check the list of passengers on a flight against a database of blacklisted passengers (and neither the list of passenger nor the blacklist should be publicly disclosed). Here the final list of passengers might be ready only few minutes before take-off, while the flight has been scheduled way in advance. We will now see how the offline-online approach can be adopted for secure circuit evaluation. Sharing occurs in the offline phase and the online phase involves only reconstruction."
	#string = "We have seen that one of the major bottleneck in the shared evaluation of the circuit is to evaluate the multiplication gates. Beavers technique for multiplication forms the core of the offline-online paradigm. Beavers circuit-randomization technique is commmonly used in the online phase for the evaluation of multiplication gates. Here, the gates are evaluated using pre-computed, t-shared random multiplication triples. Consider, for now that we have an oracle in the offline phase that generates such triples (a, b, c) where a, b are random and private values independent of the actual inputs to the multiplication gates and c = ab. We will now see how, given such triples, we can evaluate the multiplication gate in the online phase using just two reconstructions. Let x, y be the actual inputs to the multiplication gate. If the product xy can be written as a linear combination of a, b and c(= ab) where the combiners will be publicly known and will not leak any information about x and y then (n, t) Shamir-sharing of a, b and c beforehand will enable each party to easily obtain (n, t) Shamir-sharing of xy"
	
	#print(string)

	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
	
	#bitts =  [0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1]
	#bits = [0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1]
	#bits = generate_random_bits(3999999)
	#bitts = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] 
	print("Message length: ", len(bits))
	#stuffed_bits = bits
	stuffed_bits = bit_stuffing(bits)
	#original_msg = bit_unstuffing(stuffed_bits)
	#print(stuffed_bits)
	print("Stuffing_DONE")
	#check(bits,original_msg)
	#print(bits,'\n',stuffed_bits,'\n',original_msg)
	
	#print(len(stuffed_bits))
	locations = dict.fromkeys(range(0,len(frame_bytes),2), 0) 
	# print(int(z,2))
	random.seed(secret_key)
	for i in range(0,len(stuffed_bits),3):
		while(1):
			random_location = random.randint(0,len(frame_bytes))
			#print("Generating random number:",random_location) 
			if(locations.get(random_location) is not None and  locations[random_location]==0):
				locations[random_location]=1
				break
			else:
				continue
		# Converting current frame byte pointed by random location into binary
		binary_value = format(frame_bytes[random_location],'08b')
		
		#print(binary_value)
		# Taking out the 2nd, 4th and 6th
		current_triple = ""+binary_value[1]+binary_value[3]+binary_value[5]
		#current_triple = ""+binary_value[6]+binary_value[4]+binary_value[2]
		# Current secret_msg bits
		secret_bits = ""+str(stuffed_bits[i])+str(stuffed_bits[i+1])+str(stuffed_bits[i+2])
		replace_triple = mapping_info[current_triple][int(secret_bits,2)]
		#print("replace_triple: ",replace_triple)
		binary_value = binary_value[0:1]+replace_triple[0]+binary_value[2:3]+replace_triple[1]+binary_value[4:5]+replace_triple[2]+binary_value[6:]
		#binary_value = binary_value[0:2]+replace_triple[2]+binary_value[3:4]+replace_triple[1]+binary_value[5:6]+replace_triple[0]+binary_value[7:]
					   
		# if x-or-->1 then replace 1st bit else replace LSB(0th) bit
		if (stuffed_bits[i]^stuffed_bits[i+2]) ==1:
			binary_value = binary_value[:-2] + str(stuffed_bits[i+2]) + binary_value[7]
		else:
			binary_value = binary_value[:-1] + str(stuffed_bits[i+2])

		frame_bytes[random_location] = int(binary_value,2)
		
		
		
	
	
	frame_modified = bytes(frame_bytes)
	newAudio =  wave.open('intelligent_6.wav', 'wb')
	newAudio.setparams(audio.getparams())
	newAudio.writeframes(frame_modified)

	newAudio.close()
	audio.close()
	print(" |---->succesfully encoded inside 4.wav")

def decode():
	secret_key = int(input("\nSecret Key:"))
	print("Decoding\n\n")
	audio = wave.open("intelligent_6.wav", mode='rb')
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	locations = dict.fromkeys(range(0,len(frame_bytes),2), 0) 
	#random.seed(956)
	random.seed(secret_key)
	decoded_string = list()
	last_6_bits = ""
	last_7_bits = ""
	count = 0
	while(1):
		while(1):
			random_location = random.randint(0,len(frame_bytes))
			#print("Generating random number:",random_location)
			if(locations.get(random_location) is not None and  locations[random_location]==0):
				locations[random_location]=1
				break
			else:
				continue
		# Converting current frame byte pointed by random location into binary
		binary_value = format(frame_bytes[random_location],'08b')
		secret_triple = ""
		#print(binary_value)
		# Taking out the 2nd, 4th and 6th
		triple_xor = int(binary_value[1])^int(binary_value[3])^int(binary_value[5])
		first_third_xor = int(binary_value[1])^int(binary_value[5])
		#print("t_x:", triple_xor,"f_t_x: ", first_third_xor)
		if(triple_xor==1):
			if(first_third_xor==0):  # Look out for LSB bit
				if(int(binary_value[7])==0):
					secret_triple = "010"
				else:
					secret_triple = "111"
			else:
				if(int(binary_value[6])==0):
					secret_triple ="100"
				else:
					secret_triple ="001"
		elif(triple_xor==0):
			if(first_third_xor==0):  # Look out for LSB bit
				if(int(binary_value[7])==0):
					secret_triple = "000"
				else:
					secret_triple =  "101"
			else:
				if(int(binary_value[6])==0):
					secret_triple =  "110"
				else:
					secret_triple = "011"
		j = 0
		flag = 0
		
		while(j<3):
			#print(j,last_6_bits,last_7_bits,secret_triple[j])
			if(len(last_6_bits)<6):
				last_6_bits = last_6_bits+ str(secret_triple[j])
				decoded_string.append(int(secret_triple[j]))
			elif(last_6_bits=="011111" and int(secret_triple[j])==0):
				last_6_bits = " "#last_6_bits[1:] + str(stuffed_bits[j])
			elif(j<2 and last_6_bits=="011111" and int(secret_triple[j])==1 and int(secret_triple[j+1])==0):
				decoded_string = decoded_string[:-6]
				flag = 1
				break
			elif(last_7_bits=="0111111" and int(secret_triple[j])==0):
				#print(j,last_6_bits,stuffed_bits[j],stuffed_bits[j+1])
				decoded_string = decoded_string[:-7]
				flag = 1
				break
			else:
				decoded_string.append(int(secret_triple[j]))
				last_7_bits = last_6_bits + str(secret_triple[j])
				last_6_bits = last_6_bits[1:] + str(secret_triple[j])
			#print(j,last_6_bits,last_7_bits)
			j = j+1
		if(flag==1):
			break
				
	
	#print(decoded_string)
	#check(decoded_string)
	decodded_string = "".join(chr(int("".join(map(str,decoded_string[i:i+8])),2)) for i in range(0,len(decoded_string),8))
	print(decodded_string)
	audio.close()	

while(1):
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)exit")
	val = int(input("\nChoice:"))
	print(val)
	case(val)