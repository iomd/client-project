on run {input, parameters}
	tell application "Finder"
		# Unix syntax
		open POSIX file "/Applications/Visual Studio Code.app"
	end tell
	return input
end run
