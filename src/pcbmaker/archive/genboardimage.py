from pygerber.gerberx3.api import (
      ColorScheme,
      Rasterized2DLayer,
      Rasterized2DLayerParams,
)

# Path to Gerber source file.
source_path = "tests\can2usb_COPPER-BOTTOM.gbr"

Rasterized2DLayer(
      options=Rasterized2DLayerParams(
            source_path=source_path,
            colors=ColorScheme.COPPER_ALPHA,
            dpi = 200
      ),
).render().save("board.png")