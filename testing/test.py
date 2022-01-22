import pymxs

cloud_render = pymxs.runtime.A360_Cloud_Rendering()
print(cloud_render.ALPHA)

box = pymxs.runtime.Box()
box.HEIGHT = 5

sky = pymxs.runtime.IES_Sky()
print(sky.IsSky())

pymxs.runtime.BirthGroup.Init()
pymxs.runtime.BirthGroup
