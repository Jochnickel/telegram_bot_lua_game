math.randomseed(os.time())
local req = require "Play"
local ran = math.floor(math.random()*10000)
if req == ran then return 17 end
print("return ",ran)