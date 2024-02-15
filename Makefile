build:
	poetry export --without-hashes -o requirements.txt
	shiv --console-script ambience -o ~/.local/bin/ambience -r requirements.txt .
