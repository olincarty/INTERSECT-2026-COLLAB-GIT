from manim import *

class AnimateIntersectLogo(Scene):
    def construct(self):
        # 1. Use ImageMobject for a PNG file
        logo = ImageMobject("INTERSECT_Logo.png")
        
        # 2. Scale as before
        logo.scale(3)
        
        self.play(
                    GrowFromCenter(logo),
                    rate_func=rate_functions.ease_out_elastic,
                    run_time=2
                )
        
        self.wait(2)