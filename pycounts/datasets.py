from importlib import resources

def get_flatland():
    """ Get path to example "flatland" text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    E. A. Abbott, "Flatland", Seeley & Co., 1884.     
    """

    with resources.path("pycounts.data", "flatland.txt") as f:
        data_file_path = f
    return data_file_path