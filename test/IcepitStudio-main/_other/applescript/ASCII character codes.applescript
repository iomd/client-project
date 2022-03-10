
set theCodes to {73, 79, 77, 68}
set theResult to ""
repeat with theChar in theCodes
	set addThis to ASCII character of theChar
	set theResult to theResult & addThis
end repeat
display dialog theResult buttons "OK" default button 1
-->Result:"IOMD"
--------------------------------------------------
set theCodes to {73, 67, 69, 77, 65, 78, 78}
set theResult to ""
repeat with theChar in theCodes
	set addThis to ASCII character of theChar
	set theResult to theResult & addThis
end repeat
display dialog theResult buttons "OK" default button 1
-->Result:"ICEMANN"
--------------------------------------------------
