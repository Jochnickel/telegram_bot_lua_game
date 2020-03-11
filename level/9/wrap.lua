local t = {[10] = 10, [20] = 13}
require "play"(t)
if (t[20]==20) then return 10 end