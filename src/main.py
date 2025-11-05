import click
from action import uploadFile

copyright_msg = """
========================================================\n
imgbb uploader, Copyright @yanjankaf, 2025.

a dumb tool to upload images to imagbb using requests
========================================================
"""


@click.command(help=copyright_msg)
@click.option("--e", help="Expired after in seconds (60-15552000)")
@click.argument("path", metavar="<path of file to be uploaded>", required=True)
def main(e, path):
    if not path:
        raise click.UsageError("Missing argument 'PATH'. You must specify a file path.")
    try:
        retPath = uploadFile(path, e)
        e = int(e)
        print(f"Image Uploded at {retPath}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
