import random
import socket, threading

class workingThread(threading.Thread):
	def __init__(self, client, ip, port):
		threading.Thread.__init__(self)
		self.client = client
		self.ip = ip
		self.port = port

	def run(self):
		client.sendall("Welcome to Sheldon Cooper presents \"Fun with Bins\"\n")
		client.sendall("In the first episode, we're going to have fun reversing simple binaries\n")
		client.sendall("I will send you a random binary. To pass the stage, you'll need to give me the input to reach the \"Yes\" condition.\n" )
		client.sendall("Lets get started\n\n")

		bins = ['f6896012e7834a40c78647087384cb6b', 'bbc240d93145254d77513e3d43aec77cb7022784ecdea3e72c8c0997', '1b23382da0ccf1a4018f0e28e5ceecd1c44d411013cd9f427cf7672d57a38019890446', '5372c53749edb244c2194f60da3aa99f056b4ace0ac7', '1a79747b711e33982ff5b981febde5dcd96d', '39383e8037779b85cab858b82e1a1dce0ed3f66fc31d2889b4801c5cd42fc22446dfe7724ccf9ac3', '518bbe58939ec68ae54dcc91de4c127af300274dd3110a4eec529d91b7bc4799b937', '553115434d3a53cc7a45f4d8a85be4761df51cf0d64d', '6879decfe6c47168a8d76c96d0eeb70bea24d3d52d0dc1cb72c3a2cce9907f200ec767f757', '78035b65a6778387d8205fd9ae53bac6fc43f2d79c159f8e1430fc6a6b0c0c8a8b81e24e38b4fc', '819e51af6a0423417a2f26cae395580fbcf2c50ece1296', '667c4002f8a7183a357f7c83b00b14dc93', 'd5d83046a1952f6d4de9bd8bd410bd7350c6ee5e70486451f1e689bd314129e2', 'ea07f38743375dfc49bc7997f338e2dc8988758608e8079405c26d63406d49b1867fa8abfd4e9b9d01aaad77da', '6103c63104a4032bd482c40b7832b427', '64a9af7fe08d7dd008e2a95b', 'a27ab0fd28d927005152d3c6cd2a5c1768ff3d8986b192b7e3c9d666', 'bdc0ad42827de5637c0ca2bba3eaf5611aff1461ea1f', 'b20a1a498367a01548d9ac417eac198a79a0f7f72225eeab43490fe41375da380156f0a7efe971', 'f4939c22e709848015c1cbbc2da0c53c80ccbf5b4bc3290e893d213e537042bf98e69ebd0bf3bc68', '14d60e53e2ec2748251266c46fa98d', 'e7f598fb3f88af1a9aa00cf06401636637e9aba41b147281425dceca23deca3abec039cb', '9bd0d6c1209bcae8657138d9f9339bf5', '896de91c8e48608535a9afe5a8aef6c0e7b72f4864', '4f423febeab9fbc67894adb457a382bfd80120479b2bcca67f9bbb2f87a5404ae15fc84f8a6e6150ff2d27', '92fe331d5eff80f5da287e', '8462eac34d18dbf8f0bed88b4d00a84dedbc39d3d359cbf9ce06480a78b43ab6e0', '6c46a86c74053f90fc3c600e0b0fdfc66f39dcaeeb64b2f1e59195944cad92b7a1a72bdbdd0d3bf3a70e293390', 'ce604131e9650b6bb95ebeba2bb5ef179694aad5772d28', 'dd9bba172a8e42e1fb9c8b48ac272e470738e839c4f4c42b149b3ad088b2cc05ffcb6379', '084ea33a829ff2db3ffc1aa874805c606fff387b623d49e5262f59f0ee2f067d875e52a86c7acc', 'e1fb41d4ea4947855f1ca1947d8d178aee3f5d16aef589697d46', '6c78c7e2e5f8af29e99c906222fe95f07943787b', 'eb5dd252eb0cc89b106b3799189a38b582aafa074780dbe703f9', 'cca6a3f8b8941fafd39d659eef4b59e655da8de75b5ff699c235843f604e5335', 'b1dd2174d4742430bc1f766232', '709e24793ab10a7dc5a32eee12e9411dc094b85627a9', '0492740db44909f34d319ec6e37c71872c6ef7472de45f280fe54a645df3e01f2a56c173b7d8eb', '93ccea918b2672349b170440b43a95a694', '8acc4949f63bc6335c383e1b938b6944bfd2ee9c9f25c3f2adaedb5d0cd2933904', '5299d757ed034016bf8b7cd7f3cf825d0eda3f33ee79196cb6', '060ee059b7c00ee998cdd89dc0d04ba05e21f0fdd5065a85d977c6576e5fa714ee429f81f8f466', 'ac8710174f8d442363a5cf269879', '087b1560cdbd910fd144', 'ccefde454234419371b29027967d5927749a09c60da5293a6450865adff9bc0b494b', '5691b5c8b9a314ce1c4de988804262fcf8d2df5402c63ef902ed935b3c3ad1c2f2aef2', '8c43f07c89fa52b0d9401a6aff1b1566ac9ae2', 'd4070592c62138ad9f23e50fb15750b3c75c0be92fe67962a0182dd60f8c41380833894e9f1f4518325873', '15ffc2545c10c9fbc6709f534b3b', '85777f817f81012da26b7be44a9d61e2e0', '1f0245d2b4c9e46945f6130a1508bc4e5e9fa329ce082d9b10', 'c0bfe8716c5a79053e8c21b5479959624fb3d68336fd0b458f8375d94416640ad229366b54cdfe85a2805d', '772ddc93df0305359e566061a23f02c4b210ef28a96ad46d7fc99932b9ae6ba59e48', '50bf52b134aa883400aa553448a9a4d7b4ba273ea218522425', '36d93f04c95e4cfe51fa2472249bba7085', '3566dd7a9a195db588ea3f4206cb940cbc2a074c', 'e980518c3f25e3c1be1b82e53ac0278b5dccbcdcdb8f67fb6a8bd1b40b16d62b7c807acb5061a77bd092473e07', 'e3b615eccce43aba6c4a9a656bc03293b48966a006478c38a1550324db63005a384d94fd', '2e57b7ca45745bbf046d324e6ae14c2d59b9461b45944f6f5ed4a4cef98ed2233249d1301abaea9f3f47aa90', '14f1b4ddb6c1665a56a1ed12c4bf5196e1', 'f0247776bed83269e6497b492e11', 'b7c5077911dd8e9386b878facbbe0054ea82cfab89895819c0bae2d3c1e0eca2215c9b8d5af82dc102b9', 'c3c563f320b0ee52968891a0b4a8b70e47f7337bed7ffdfccd83103eaf1b176a88', '78fd6b92ca87c8f304763e49abf0b1bfaca998e989aa2a80f8854404a56c8ad3e6ce74789982440f98', '58c63aa8c66b9fb97ecff46cbf126288e02d76bf0ffef166d0c85a6c', '34802d1234807c9fd4a8fb0760d88b10c9e35c62f7d9e48125d5f5751f4db64339', '64250f47b4016fe6116fc4105f77e114f85133fcdb0073cc2ef2', '31a078347eed1d14d72f68e6e968b06871b4a218e2e5e964ddcd81fea474', 'd8f707f92950b1e19713fb88c0f1428cdbeab6938176b6c2f409704d51', 'b1d120b395894c7edd5d958fd990ae612146296f8d5f111c20f737a7c2a5d9687215b4fb', '3de73e349e31afb0edc3870aea43f0f071e62905ca1ffa3b9285b09176cd', '88b4a4ec5a758c0bc715d6d85bd3ccc6280417c87ffc', '98c3e3ec7848e8048c96ed57daa41abeb4a700f125bb7fe79947b808db34ce8cc4cd', 'ac232b0f50c110d6bce19141d3916db3e8049fb3031b92e3351ae5b346c8d2c00f95b26b90', '5542cce6b71234dc6a05f44cb4375853c8392001f28ac3a35e1cde62597bce0ac1f113d0cd14e7c559020eaf', '12094f74fc6b578d5bde1fd9a8096dfdd05bc378f266eec0be723588c5effd776e11a081576723a4b2b76d', 'a2d3842a386374a2f26d68f39ec50ae5b1e2047206105398237eeee849a1963bef', '934be159551f84cf9e613b2680fff7e1dc17116eef92fc58cf0f819f7bd4045e', '6980cbacd051a35e84e6905fdad4fb36f4098c46602d273696e1496ee463760810d19c21a84ea2d0', 'b2d88800b98956ef83f2e417295cbad758b3e3a4', '2639481de91f4eb1a50f1412', 'e29e669efe7c2241f315a48907f6ff6af46cb946e49c0a3adafa7917d9bd291d', '481adcd9d550978a172222486b6de7ec3d859a2bdbca', '424a3a436c9c0708fef557c07dbe983a32e64438f49df5', '21e6ac3a01451e06acc101073858f8aa78348954a82e4dec0573', '566369cc29ba0a1f8c5bd239b75ff3d71f', 'dc2aa86892315d8b73495a49c08252bbe14870aab1533a037e', '48f4220875b555094b5ce72a48849094f3482b39086e74732ea0a43ff9820009205b', '2372c2a355b6f50ff33e6979', '059827880a15bf33aaf446008cc5ce5b27f2ea13343e5f97955d02ed60b09c8ca12b67', '0a314fca1b61c712dd889e135cc30ed1fdde8a5ee16ca8bba13a8a82ffbe35823b7907018f4aa111', 'bf9e0d939546f60d6ec10247660ed0ed', '9d6ba7359600ac5df8fb3990247ef7796f9a87', '96a461b9448ddf778a5ec08ff3bb784d914b6171d8', '91b1d9b824aa8ef40944babdadd6670de36db74371f6fcc79319c8a5fd5c2f3ce6f6d3778145b756cb', '4df9438f185ed03dde6415', 'eb89da5ea3bb2ff43f64e800792e852cae68069623e66e9df8e805eef74a7d99e97e6842a6', 'ec42a0d5c20ad16d58c0a9d0e6409c44c9541b42fe03d269e6d47c075a2c07ca18db2c', 'd3cdddc3b586b0f85b13b5d4f38ddc723f077d881bfeadcc4fe3a670f29865393c8d2d99d550af', '390bc0bb9f0cece54ff11aff1172945bb8630cee55a97f5c2c']
		failed = 0

		for a in range(1, 32):
			b = random.randint(0, 99)
			client.sendall("-> Round %d\n" % (a,))
			binary_name = bins[b]
			print binary_name
			fp = open('abc/' + binary_name, 'rb')
			client.sendall(fp.read())
			client.sendall('\nYou got it? ')

			client.settimeout(5.0)
			data = client.recv(100).strip()
			if data != binary_name:
				failed = 1
				break

		if not failed:
			client.sendall("Flag is HACKCON{rolling_up_strings_like_a_pro}")

		else:
			client.sendall("HAHAHAHAHA! You amuse me.")
			client.close()

tcpsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsocket.bind(("0.0.0.0",8000))
while 1:
	tcpsocket.listen(5)
	(client,(ip,port))=tcpsocket.accept()
	newthread= workingThread(client,ip,port)
	newthread.start()