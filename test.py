from woopra import WoopraTracker

if __name__ == '__main__':
	woopra = WoopraTracker("jadyounan.com")
	woopra.set_secure(False)
	woopra.track("play", {
		"artist" : "Dave Brubeck",
		"song" : "Take Five",
		"genre" : "Jazz"
	})


