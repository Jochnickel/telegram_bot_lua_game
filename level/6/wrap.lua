local o1 = {}
local o2 = {}
o1.asd = o2
o2.asd = o1
o1.efe = o1
o2.efe = {secret = 'return "well done"'}
local require_Play = require "play"
if require_Play(o1)=="well done" then
	return 7
end
error("No",2)