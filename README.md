# Currency Conversion Application

This application is a command-line tool that converts an amount from one currency to another. It uses the Exconvert API to fetch the conversion rates.

## Functionality

The application takes three mandatory arguments:
- `base_currency`: The currency you want to convert from.
- `target_currency`: The currency you want to convert to.
- `amount`: The amount you want to convert.

It also takes an optional argument:
- `-c` or `--currency_rate`: If this flag is set, the application will also display the conversion rate.


## Download Instructions

1. Clone the repository to your local machine using `git clone <repository_url>`.
2. Navigate to the directory containing the script.
3. Run the converter.py file.

## Environment Setup for Windows

The application requires an API key from Exconvert, which should be stored as an environment variable. Here are the steps to set it up in Windows:

1. Obtain your API key from Exconvert.
2. Open the start menu, search for 'Environment Variables', and select 'Edit the system environment variables'.
3. In the System Properties window, click on 'Environment Variables'.
4. In the Environment Variables window, click on 'New' under the User variables section.
5. Enter `EXCONVERT_API_KEY` as the Variable name and your actual API key as the Variable value.
6. Click 'OK' in all windows to save the changes.

Alternatively, you can use the `set` or `setx` command in the command prompt:

- `set`: This command sets the environment variable for the current session only.
  - Syntax: `set VariableName=Value`
- `setx`: This command sets the environment variable permanently, but it doesn't affect the current session.
  - Syntax: `setx VariableName Value`
