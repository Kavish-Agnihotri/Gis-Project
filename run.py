import torch
from pathlib import Path

from cyp.data import MODISExporter

import fire


class RunTask:
    """Entry point into the pipeline.

    For convenience, all the parameter descriptions are copied from the classes.
    """

    @staticmethod
    def export(export_limit=None, major_states_only=True, check_if_done=True, download_folder=None,
               yield_data_path='data/yield_data.csv'):
        """
        Export all the data necessary to train the models.

        Parameters
        ----------
        export_limit: int or None, default=None
            If not none, how many .tif files to export (*3, for the image, mask and temperature
            files)
        major_states_only: boolean, default=True
            Whether to only use the 11 states responsible for 75 % of national soybean
            production, as is done in the paper
        check_if_done: boolean, default=False
            If true, will check download_folder for any .tif files which have already been
            downloaded, and won't export them again. This effectively allows for
            checkpointing, and prevents all files from having to be downloaded at once.
        download_folder: None or pathlib Path, default=None
            Which folder to check for downloaded files, if check_if_done=True. If None, looks
            in data/folder_name
        yield_data_path: str, default='data/yield_data.csv'
            A path to the yield data
        """
        yield_data_path = Path(yield_data_path)
        exporter = MODISExporter(locations_filepath=yield_data_path)
        exporter.export_all(export_limit, major_states_only, check_if_done,
                            download_folder)
 

if __name__ == '__main__':
    fire.Fire(RunTask)
