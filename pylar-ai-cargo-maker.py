import os
import re
import requests

# Read the main.rs file
with open("main.rs", "r") as f:
    main_rs = f.read()

# Find all extern crate statements in the main.rs file
extern_crates = re.findall(
    r"^\s*extern\s+crate\s+(\w+)\s*;\s*$", main_rs, re.MULTILINE)

# Find all use statements in the main.rs file
uses = re.findall(r"^\s*use\s+(\w+)\s*;\s*$", main_rs, re.MULTILINE)

# Prompt the user for the package name
package_name = input("Enter the package name: ")

# Prompt the user for the package version
package_version = input("Enter the package version: ")

# Prompt the user for the author's name
author_name = input("Enter the author's name: ")

# Prompt the user for the author's email
author_email = input("Enter the author's email: ")

# Create the cargo.toml file contents as a string
cargo_toml = f"""[package]
name = "{package_name}"
version = "{package_version}"
authors = ["{author_name} <{author_email}>"]

[dependencies]
"""

# Add the dependencies to the cargo.toml file
for extern_crate in extern_crates:
    # Get the latest version of the crate from crates.io
    r = requests.get(f"https://crates.io/api/v1/crates/{extern_crate}")
    crate_info = r.json()
    version = crate_info["crate"]["max_version"]

    cargo_toml += f"{extern_crate} = \"{version}\"\n"

for use_ in uses:
    # Get the latest version of the crate from crates.io
    r = requests.get(f"https://crates.io/api/v1/crates/{use_}")
    crate_info = r.json()
    version = crate_info["crate"]["max_version"]

    cargo_toml += f"{use_} = \"{version}\"\n"

# Write the cargo.toml file to the current directory
with open("Cargo.toml", "w") as f:
    f.write(cargo_toml)

print("Cargo.toml file created successfully!")
