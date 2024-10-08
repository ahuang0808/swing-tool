import sys
from pathlib import Path

import click
from modules.image import SwingImageBuilder


@click.group()
def swing():
    """
    Swing CLI Tool
    """


@swing.command()
@click.option("-i", "--input-path", required=True, help="Input image path.")
@click.option("-o", "--output-path", default="", help="Output image path.")
@click.option(
    "-d",
    "--description",
    default="",
    help="Description in the image footer.",
)
def image(input_path: str, output_path: str, description: str):
    """
    Build swing image with header and footer.
    """
    click.echo("Processing image...")
    input_path = Path(input_path)
    output_path = Path(output_path) if output_path else output_path
    swing_image_builder = SwingImageBuilder()
    image = swing_image_builder.build(input_path, description)
    image_ig = swing_image_builder.build(input_path, description, True)

    # If output is empty, ouput to the same dir as input,
    # and append "_new" to the filename
    if not output_path:
        output_path_base = input_path.parent / f"{input_path.stem}"
    # Is dir, output to this folder with same file name as input.
    elif not output_path.suffix:
        output_path_base = output_path / input_path.stem

    try:
        image.save(f"{output_path_base}_new{input_path.suffix}")
        image_ig.save(f"{output_path_base}_new_ig{input_path.suffix}")
    except FileNotFoundError:
        sys.exit(f"Please make sure the folder {output_path.parent} exist.")


if __name__ == "__main__":
    swing()
