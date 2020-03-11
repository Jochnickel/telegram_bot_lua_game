print 'write "Hello"'
local p = _G.print
local r = "BAD"
_G.print = function(msg,...)
	if 'Hello'==msg then r = "GOOD" end
	p(msg,...)
	error("No",2)
end
require "play"

if "BAD"==r then error("No",2) end