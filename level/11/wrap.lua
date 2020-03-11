print "whats the difference?"
local r = _G.round
local asd = require "play"
_G.round = function() return "return 2" end
if 'function'==type(asd) and asd()==2 then
	_G.round = r
	return 12
end