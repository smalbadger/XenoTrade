from UserSelectGUI import UserSelectGUI

if __name__ == '__main__':
	kernel = Kernel()
	app = QApplication(sys.argv)
	frame = UserSelectGUI(kernel)
	frame.show()
	#app.exec_()
