print "Getting weird"
local pr = _G.print
_G.print = _G.pairs
_G.pairs = pr

if(require "play"{r = 'return "why"'})=="why" then
	local pr = _G.print
	_G.print = _G.pairs
	_G.pairs = pr
	return 9
end