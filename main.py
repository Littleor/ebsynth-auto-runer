import logging
import os
import time

from tqdm import tqdm

from utils.auto_run import get_scaling_factor, launch_ebsynth_with_file, find_and_click, find_all_location
from utils.common import logging_config, close_ebsynth


class EbSynthAutoRuner:
    scaling_factor = 1.0
    software_path = None
    synth_button_confidence_threshold = 0.98
    run_button_confidence_threshold = 0.99
    run_button_reference_image_path = os.path.join(os.path.dirname(__file__), "data/run_button.png")
    synth_button_reference_image_path = os.path.join(os.path.dirname(__file__), "data/synth_button.png")

    def __init__(self, synth_button_confidence_threshold: float = None,
                 run_button_confidence_threshold: float = None,
                 logger=None,
                 software_path: str = None):
        self.scaling_factor = get_scaling_factor()
        self.software_path = software_path
        if synth_button_confidence_threshold is not None:
            self.synth_button_confidence_threshold = synth_button_confidence_threshold
        if run_button_confidence_threshold is not None:
            self.run_button_confidence_threshold = run_button_confidence_threshold
        if logger is not None:
            self.logger = logger
        else:
            logging_config()
            self.logger = logging.getLogger(__name__)

    def run(self, file_path: str):
        self.logger.info(f"EbSynthAutoRuner begin to run the {file_path}")

        # 1. Close EbSynth
        self.logger.info(f"1. close the EbSynth")
        close_ebsynth()
        time.sleep(2)

        # 2. Launch EbSynth with file
        self.logger.info(f"2. launch the {file_path}")
        launch_ebsynth_with_file(file_path, self.software_path)
        time.sleep(2)

        # 3. Get the `Synth` count
        self.logger.info(f"3. get the `Synth` button count")
        all_synth_locations = find_all_location(self.synth_button_reference_image_path,
                                                scaling_factor=self.scaling_factor,
                                                confidence=self.synth_button_confidence_threshold)
        synth_button_count = len(all_synth_locations)
        self.logger.debug(f"synth button count: {synth_button_count}")

        # 4. Find and click the run button
        self.logger.info(f"4. find and click the run button")
        find_and_click(self.run_button_reference_image_path, scaling_factor=self.scaling_factor)

        # 5. Wait for the `Synth` count to be 0, which means running
        self.logger.info(f"5. wait for begin to run")
        current_synth_button_count = synth_button_count
        while current_synth_button_count > 0:
            all_synth_locations = find_all_location(self.synth_button_reference_image_path,
                                                    scaling_factor=self.scaling_factor,
                                                    confidence=self.synth_button_confidence_threshold)
            current_synth_button_count = len(all_synth_locations)
            self.logger.debug(f"synth_button_count: {current_synth_button_count}")
            time.sleep(0.5)

        # 6. Wait for the `Synth` count to be 1, which means running finished
        self.logger.info(f"6. wait for end to run")
        while current_synth_button_count < synth_button_count:
            all_synth_locations = find_all_location(self.synth_button_reference_image_path,
                                                    scaling_factor=self.scaling_factor,
                                                    confidence=self.synth_button_confidence_threshold)
            current_synth_button_count = len(all_synth_locations)
            self.logger.debug(
                f"synth_button_count: {current_synth_button_count}, Processing progress: {current_synth_button_count}/{synth_button_count}")
            time.sleep(3)
        self.logger.debug(f"end to run")

        # 7. Close EbSynth
        self.logger.info(f"7. close the EbSynth")
        close_ebsynth()

        self.logger.info(f"EbSynthAutoRuner end to run the {file_path}")
        time.sleep(1)


def process_ebs_files(
    dir_path: str,
    ebsynth_auto_runer: EbSynthAutoRuner,
    logger
):
    import os
    if not os.path.exists(dir_path):
        logger.error(f"dir_path: {dir_path} not exists")
        return False
    file_names = [
        file_name for file_name in os.listdir(dir_path)
        if file_name.endswith(".ebs")
    ]
    if len(file_names) == 0:
        logger.error(f"dir_path: {dir_path} has no `.ebs` files")
        return False

    # Sorted by the number in the file name
    file_names = sorted(file_names, key=lambda x:
    (x.split("_")[-1].split(".")[0].isdigit(),
     int(x.split("_")[-1].split(".")[0]) if x.split("_")[-1].split(".")[0].isdigit()
     else x))

    logger.info(f"Total {len(file_names)} `.ebs` files")
    failed_file_names = []
    for file_name in tqdm(file_names):
        try:
            file_path = os.path.join(dir_path, file_name)
            ebsynth_auto_runer.run(file_path)
        except Exception as e:
            logger.error(f"process {file_name} error: {e}")
            failed_file_names.append(file_name)
    logger.info(
        f"Success to process {len(file_names) - len(failed_file_names)} files,"
        f" failed {len(failed_file_names)} files")
    if len(failed_file_names) > 0:
        logger.info(f"Failed file names: {failed_file_names}")
        return False
    return True


def args_parser():
    import argparse
    parser = argparse.ArgumentParser(description='EbSynth Auto Runer')
    parser.add_argument('dir_path', type=str, default=None,
                        help='Project dir path, generate by the `ebsynth_utility` extension or others')
    parser.add_argument('--synth_button_confidence_threshold', type=float, default=0.98,
                        help='Synth button confidence threshold')
    parser.add_argument('--run_button_confidence_threshold', type=float, default=0.99,
                        help='Run button confidence threshold')
    parser.add_argument('--software_path', type=str, default=None,
                        help='Ebsynth software path, default to be the `EbSynth`')
    parser.add_argument('--log_level', type=str, default="INFO",
                        help='Log level, default to be the `INFO`')
    args = parser.parse_args()
    return args


def main():
    args = args_parser()

    logging_config()
    logger = logging.getLogger(__name__)
    logger.setLevel(args.log_level)

    ebsynth_auto_runer = EbSynthAutoRuner(logger=logger,
                                          synth_button_confidence_threshold=args.synth_button_confidence_threshold,
                                          run_button_confidence_threshold=args.run_button_confidence_threshold,
                                          software_path=args.software_path)
    process_ebs_files(
        dir_path=args.dir_path,
        ebsynth_auto_runer=ebsynth_auto_runer,
        logger=logger
    )


if __name__ == '__main__':
    main()
