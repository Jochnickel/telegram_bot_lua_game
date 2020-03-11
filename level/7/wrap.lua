print "one more. the key is patience."

if (require "play"(setmetatable({},{
	__metatable = false,
	__index = {patience = 'return 42'}
})))==42 then return 8 end

error("No",2)