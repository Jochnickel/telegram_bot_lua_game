local t = _G.type
local a = {}
setmetatable(a,{
	__tostring = function()
		return tostring(42)
	end,
	__call = function()
		local h, msg = pcall(42)
		print(debug.traceback(msg,2))
		return "return 22"
	end
})
if (require "Play"(a))==22 then return 18 end