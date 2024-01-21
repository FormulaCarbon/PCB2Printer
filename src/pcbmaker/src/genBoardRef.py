from pygerber.gerberx3.api import (
      ColorScheme,
      Rasterized2DLayer,
      Rasterized2DLayerParams,
)
import os


def genBoardImage(source = "../tests/can2usb_COPPER-BOTTOM.gbr", dpi = 200):
    # Path to Gerber source file.
    _, fileExt = os.path.splitext(source)

    if fileExt != ".gbr":
        raise ValueError("Invalid File Type. Expected .gbr, got %s" % fileExt)

    Rasterized2DLayer(
        options=Rasterized2DLayerParams(
                source_path=source,
                colors=ColorScheme.COPPER_ALPHA,
                dpi = dpi
        ),
    ).render().save("/tmp/__board.png")