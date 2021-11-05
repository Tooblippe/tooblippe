manim -pqh scene.py SquareToCircle

ffmpeg  -t 5 -i media\videos\scene\1080p60\SquareToCircle.mp4  -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

ren output.gif header_vid.gif
copy header_vid.gif  C:\Users\tobie\PycharmProjects\tooblippe\assets\


