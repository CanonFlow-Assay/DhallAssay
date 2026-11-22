# DhallAssay

DhallAssay checks closed Dhall expressions. It uses the native CLI to parse and enumerate immediate dependencies, then to type-check and normalize the import-free input. Three blocking rules cover parsing, imports, and type checking. Formatting and native lint are advisory.

The initial native lane is Linux x86-64, Python 3.12, and **dhall-haskell 1.42.2**.
The [source verification contract](CONTRACT.md) explains the four verdicts
and evidence boundaries. [Native scope and sources](docs/native.md) documents
the selected profile and primary references.

## Run an example

From the repository root, install the pinned native tools into the ignored
artifact directory, then run the example's named policy.

~~~sh
python3 eng/install-native.py
export PATH="$PWD/artifacts/toolchain/bin:$PATH"
PYTHONPATH=src python3 -m dhall_assay doctor
PYTHONPATH=src python3 -m dhall_assay catalog
PYTHONPATH=src python3 -m dhall_assay scan --policy examples/policy.json
PYTHONPATH=src python3 -m dhall_assay verify --policy examples/policy.json --out artifacts/receipt.json
~~~

The example scan returns Inconclusive, exit 2. Verification runs the real
behavior checks declared by the example. Replace the policy's explicit
source and test paths for your project. Use scan to review static findings
before authorizing behavior commands.

## Qualify and package

~~~sh
python3 eng/qualify.py
python3 artifacts/dhall_assay.pyz doctor
~~~

Qualification checks native positive and negative cases, validates receipt
outcomes, builds a reproducible zipapp, and runs it from an independent
directory. Raw command evidence and the example receipt are under
artifacts/qualification/. The pinned archive identities are in
[toolchain.json](toolchain.json).

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
