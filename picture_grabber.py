import os
import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    # Create Output folder if not found in system
    if not os.path.exists('CustomSprites'):
        os.mkdir('CustomSprites')

    # Setting Values
    SAVE_DIR = 'CustomSprites/'
    EXT_GEN1 = ['mf', 'md', 'mo', 'fo', 'uk']
    AMT_GEN1_START = 0
    AMT_GEN1_END = 152
    AMT_GEN1_TOTAL = 151

    # Test String
    # https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0001_000_mf_n_00000000_f_n.png

    # Generation 1 Code
    png_url = ['https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_', '_000_', '_n_00000000_f_n.png']

    dex_num_4 = [str(i).zfill(4) for i in range(AMT_GEN1_START+1, AMT_GEN1_END)]
    dex_num_3 = [str(i).zfill(3) + '.png' for i in range(AMT_GEN1_START+1, AMT_GEN1_END)]


    def base_request(filename, png, extension, dex_num):
        png_url_call = png[0] + dex_num + png[1] + extension + png[2]
        print('Calling: ', png_url_call)
        urllib.request.urlretrieve(png_url_call, filename)


    for i in range(len(dex_num_3)):
        filename_save = SAVE_DIR + dex_num_3[i]
        dex_number = dex_num_4[i]

        # Skip current iteration if file is found in SAVE_DIR
        if os.path.exists(filename_save):
            print('File found for ', dex_num_4[i], '. Skipping.')
            continue

        print(dex_number, ': Starting Function Calls.')
        # Looping through base_request function with different extensions
        for ext in EXT_GEN1:
            try:
                base_request(filename_save, png_url, ext, dex_number)
                print('Function run successfully.')
                break  # Moves to the next file
            except HTTPError:
                continue  # Moves to the next function is Exception is found
