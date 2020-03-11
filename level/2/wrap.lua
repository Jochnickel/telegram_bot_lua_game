print 'write "Hello"'
local p = _G.print
local r = ""
_G.print = function(msg,...)
	if 'Hello'==msg then r = 3 end
	p(msg,...)
end
require "play"
return r
