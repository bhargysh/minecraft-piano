from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

mc.setBlock(pos.x + 1, pos.y, pos.z, 3)
