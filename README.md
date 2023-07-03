# ShadowCipher
![ShadowCipher](https://lh3.googleusercontent.com/pw/AJFCJaVlnnYP7ESIrEHpd_mL4ELdYq5Jw5YH_455y8Xa2zVItjcruZv1524toyAY4vh71NK8UutMpKhnr4__RL65cV7Ft9R6-e2fFEQAV6bUViE7v3VonfhwwWfsVpEsJqywVUnE_BDvipPPWFNHxEeaws02ifgQWhZuKvAJzdM-5e9hrwh1Vb4ZiSA0PDLVRA040dZzuu8XMoNkHlYqZPGNbX7gux3cZNmF7EpM3mtHw7p22Mg9GIhL7qtoyib8ETIheUuoYryF6O8mqi82axtgFwPIAD6oAIVr5h09Hmed8zGDdb8zh5Xp7EFwNFmAaeQCUMQdbp5FLxX4FLi3QEVX6KkWoWr3a1dqv5P0pHHFAg83CERdMlOXFk2Oj8NXZfPU-SLCTkkZgWTuPkzrY3NhwzHurDTzOvENIyfBmuTKPdpYD6yVNnnPQ8QQ0AL2zSKRJAK6UsZExfDfQlltO9V87cHFngnNnDm9HoDtbOw6ykwOih5n4SxY_GsJPfJW2FPtMJ-_daRp4ccamniLPP1VNEeybUtBxfPDkA9sXvitnUGKpujUXNYHL0UbbJ1-ExlbSxakJjCxg9VVlCcarXIhYX5Rvj1dzS--1irF_nMAwkHBC0XNJKJq4a85JUvSUD-bT2Z9r1kSKfsOkwgoO0a9ssR0sISe9h1cKVdTC9rRzI6sAwQq7dSUwl2HJdOIvS968tSgjMN1UgEIcVoELW-JAlR5_tnmwbYNtJxzOJQHxY6Y4GBMoVqoOe-DKCpvYGkmI4heh0ILW-8SLjZ6z192eLLqiAUlPxjKZgy3QWjGoGZeS3_IEesHq7dVDgltZ7vVZcNpE0e5scpuBrSCQ5aWNO01Er-HkWZGkjUjZtuLqrmJL_beWKrmebb9QgRSCTw6HcgwrUrhRtFVl7GmUCmEdK5QGHGahpPJUdVp9AS8i0gNCiWErlo3VVFQldBkx2PDXf1IjbjO8VaL-visLYH9sjAhGu-ZyQ2lM053z5x9JHU6B-HPxvyS7geKNktC32NT_Q=w810-h229-s-no?authuser=3)
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
