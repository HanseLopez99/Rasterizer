from gl import Renderer

rend = Renderer(1024, 512)

# rend.glClearColor(0, 0.5, 0)
# rend.glColor(1, 1, 0)
# rend.glClear()

rend.glPoint(100, 100, rend.glColor(1, 0, 0))

# for i in range(512):
#     rend.glPoint(i, i)

rend.glFinish("output.bmp")
