print 'write "Hello"'
local p = _G.print
local r = ""
_G.print = function(msg,...)
	if 'Hello'==msg then return end
	p(msg,...)
	error("No",2)
end
require "play"
return r
