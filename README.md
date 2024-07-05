# Mega.nz Account Creator

This script automates the creation of multiple Mega.nz accounts using provided credentials. It utilizes the MegaTools binary for Linux and several Python dependencies. 

## Requirements

Before running the program, ensure you have the following:

1. **MegaTools Binary (Linux Only)**
    - Download and move MegaTools binary to your PATH from the official repository: [MegaTools](https://megatools.megous.com/builds/builds/)

2. **Python Dependencies**
    - Install the required Python packages:
        - `unofficial-xitroo-api==0.9`
        - `requests` or on linux `sudo apt install python3-requests`
        - `pyside6`

## Installation

1. **Install MegaTools**

    Follow the instructions on the MegaTools website to download and install the appropriate binary for your Linux distribution.

2. **Clone or Download the Repository**

    ```bash
    git clone https://github.com/Th3K1n91/mega_nz-Creator
    cd mega_nz-Creator
    ```

3. **Install Python Dependencies**

    ```bash
    pip install unofficial-xitroo-api==0.9 requests pyside6
    ```

## Usage

1. **Run the Program**

    To start the account creation process, run the following command:

    ```bash
    python Main.py
    ```
PS.: Accounts are saved to `accounts.txt`

## Interface

![Account Creator GUI Image](https://github.com/Th3K1n91/mega_nz-Creator/blob/main/images/example.PNG)

- **Username:** Enter the desired username for the Mega.nz account.
- **Password:** Enter a secure password that meets the criteria:
    - At least 8 characters long
    - Contains at least one digit or special character
    - Includes both uppercase and lowercase letters
- **Count:** Specify the number of accounts to create.
- **Threads:** Set the number of threads to use for the account creation process.
- **Start Button:** Click to begin the account creation.

## Notes

- Ensure you comply with Mega.nz's terms of service when using this tool.
- Use responsibly and do not engage in spamming or creating accounts for malicious purposes.


## License

This project is licensed under the GNU License. See the LICENSE file for details.

## Version

- **Current Version:** 5.4.0

## Contact

For any issues or questions, please open an issue on the GitHub repository.

---

**Disclaimer:** This tool is for educational purposes only. The developers are not responsible for any misuse or damage caused by this software.
