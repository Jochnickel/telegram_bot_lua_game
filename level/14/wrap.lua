print "Theres an easy way here"
local res = require "Play"
if ('number'==type(res)) then
	print(res>0.8401877171547095)
	print(res==0.8401877171547095)
	print(res<0.8401877171547095)
else print(false) end
if (res==0.8401877171547095) then return 15
end