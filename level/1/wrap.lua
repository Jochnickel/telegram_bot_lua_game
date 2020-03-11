local happy, msg = pcall(require,"Play")
if not happy then
	local f = io.open('play.lua','w')
	f:write('Finish the level!')
	f:close()
	print(msg)
end
return 2