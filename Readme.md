# Pylar AI Cargo Maker

<img width="640" alt="Pylar AI-Cargo Maker-miguelgargallo" src="https://user-images.githubusercontent.com/5947268/210122458-e209926f-4ae9-4b5e-ab0a-72c24783cfce.png">

- [Pylar AI Cargo Maker](#pylar-ai-cargo-maker)
  - [Usage](#usage)
  - [Example](#example)
  - [Credits](#credits)
  - [License](#license)

Welcome to Pylar AI Cargo Maker, a Python script for generating Cargo.toml files for Rust projects!

This script allows you to easily create Cargo.toml files for your Rust projects by prompting you for the necessary information and automatically adding dependencies based on extern crate and use statements in your main.rs file.

## Usage

To use Pylar AI Cargo Maker, simply run the script and follow the prompts:

```bash
python pylar-ai-cargo-maker.py
```

The script will ask you for the package name, package version, author's name, and author's email. It will then parse your main.rs file for extern crate and use statements, retrieve the latest versions of the relevant crates from crates.io, and generate a Cargo.toml file based on this information.

## Example

Here's an example of what the script's output might look like:

```bash
Enter the package name: my-cool-project
Enter the package version: 0.1.0
Enter the author's name: Jane Doe
Enter the author's email: jane@example.com
Cargo.toml file created successfully!
```

The resulting Cargo.toml file would look something like this:

```toml
[package]
name = "my-cool-project"
version = "0.1.0"
authors = ["Jane Doe <jane@example.com>"]

[dependencies]
crate1 = "1.2.3"
crate2 = "4.5.6"
```

## Credits

Pylar AI Cargo Maker was developed by the team at Pylar AI, a leading provider of artificial intelligence solutions. We hope you find this script useful!

## License

Pylar AI creative ML License. See the LICENSE file for details. [./LICENSE.md](https://github.com/miguelgargallo/Pylar-AI-Cargo-Maker/blob/master/License.md)
