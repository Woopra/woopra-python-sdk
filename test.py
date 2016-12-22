from woopra import WoopraTracker

if __name__ == '__main__':
	woopra = WoopraTracker("jadyounan.com")
	woopra.set_secure(False)

	woopra.set_ip_address("66.228.55.185")

	woopra.identify({
			"email": "jad@mail.com",
			"name": "Jad"
			})

	woopra.track("play", {
		"artist" : "Dave Brubeck",
		"song" : "Take Five",
		"genre" : "Jazz"
	})


