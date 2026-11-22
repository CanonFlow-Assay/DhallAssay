# Native scope and sources

The profile is **dhall-standalone**. The qualified versions are
**dhall-haskell 1.42.2** on Linux x86-64.

The qualified CLI's immediate-dependency command lists import nodes
without resolving them. The normalize command independently rejects
imports before checking types. Local, remote, environment, missing, and
fallback imports are outside this closed-expression profile. The format and
lint commands run on stdin without transitive mode.

Keep the type of the configuration explicit and exercise domain constraints
with Dhall assertions or consumer tests. The example uses a typed service
record and a native assertion over its worker count. An assertion with the
wrong count is rejected.

The Linux x86-64 archive is pinned to the observed SHA-256 of the upstream release asset. The pinned release did not expose a digest through GitHub's asset API. See the [toolchain manifest](../toolchain.json).

The profile implements the finite rules in the catalogue. Platform branches,
application behaviors beyond the declared examples, and the effectiveness of
project-specific operating practices need their own evidence.

## Primary sources

- [Dhall language standard](https://github.com/dhall-lang/dhall-lang/tree/master/standard)
- [dhall-haskell 1.42.2 native command paths](https://github.com/dhall-lang/dhall-haskell/blob/1.42.2/dhall/src/Dhall/Main.hs)
- [dhall-haskell 1.42.2 release](https://github.com/dhall-lang/dhall-haskell/releases/tag/1.42.2)
