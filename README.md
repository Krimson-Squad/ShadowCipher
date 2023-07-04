# ShadowCipher
![ShadowCipher](https://cdn.discordapp.com/attachments/492351145306751004/1125685119525589002/coollogo_com-28641315.gif)

A command-line tool to generate wordlists based on first and last name of a target user.

## About

The ShadowCipher is a simple tool that allows you to generate wordlists based on first and last names. It provides various patterns and variations to create a wide range of potential words for password cracking, data analysis, or other purposes.
## Usage

To use the ShadowCipher, follow the steps below:

1. Clone the repository or download the `ShadowCipher.py` file.
2. Ensure you have Python 3 installed on your machine.
3. Open a terminal or command prompt and navigate to the directory where `ShadowCipher.py` is located.
4. Run the following command:

   ``
   python ShadowCipher.py [-h] [-n COUNT] [-sv FILE_NAME] first_name last_name
``
-   Replace `first_name` with the target's first name.
-   Replace `last_name` with the target's last name.
-   Use the optional `-n` flag followed by the desired count to specify the number of words to generate (default: 100).

**Example**:
`python ShadowCipher.py -n 500 John Doe -sv johndoe_wordlist.txt` 

5.  The tool will generate a wordlist based on the provided names and display the total number of words generated.

## Warning

**Note:** Generating a large number of words (more than 50 million) may slow down your device. Use caution and consider the resources available on your system. If you want to exit the generation of the wordlist, you can use `CTRL + C` to exit/stop.

## Feel Free to Contribute

Contributions are welcome and encouraged! If you have any suggestions, bug reports, or would like to add new features to the this tool, please feel free to submit a pull request or open an issue on the GitHub repository.

To contribute to the project, follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they are well-tested.
4. Commit your changes with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please make sure to adhere to the existing code style and conventions used in the project. Additionally, include relevant information and test cases to support your changes.

Your contributions will be greatly appreciated and will help make the ShadowCipher even better!

## Author/Developer
> Raunak Neupane ([@rezy-dev](https://github.com/Rezy-Dev))

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krimson-Squad/ShadowCipher/blob/main/LICENSE) file for details.
