import LOGGER
import POINTS
import FILES

FILENAME_CURRENT_RIDE = 'currentRide.txt'

def reset():
	LOGGER.resetBaseFile()
	POINTS.reset()
	FILES.resetWithData(FILENAME_CURRENT_RIDE,"0\n1\n2\n")

reset()