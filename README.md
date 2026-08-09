# compilers.C

C/C++ compiler abstractions, extracted from `distutils` and decoupled so
they can evolve as a standalone distribution within the `compilers`
namespace.

Provides the compiler implementations (`compilers.C.unix`,
`compilers.C.msvc`, `compilers.C.cygwin`, `compilers.C.zos`) built on a
common base (`compilers.C.base`), along with `new_compiler` and
`get_compilers` for discovering and instantiating the appropriate
compiler for the host platform.

Shared, language-agnostic pieces live in the sibling `compilers.common`
and `compilers.errors` distributions.
