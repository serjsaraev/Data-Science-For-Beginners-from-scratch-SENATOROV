"""Conventional commits."""

# ## Questions
#
# 1. Опишите своими словами назначение каждого из этих типов коммитов:
# feat, fix, docs, style, refactor, test, build, ci, perf, chore.
#
# 2. Представьте, что вы исправили баг в функции, которая некорректно округляет числа. Сделайте фиктивный коммит и напишите для него сообщение в соответствии с Conventional Commits (используя тип fix).
#
# 3. Добавление новой функциональности:
# Допустим, вы реализовали новую функцию generateReport в проекте. Сделайте фиктивный коммит с типом feat, отражающий добавление этой функциональности
#
# 4. Модификация формата кода или стилей:
# Представьте, что вы поправили отступы и форматирование во всём проекте, не меняя логики кода. Сделайте фиктивный коммит с типом style
#
# 5. Документация и тестирование:
#
# Сделайте фиктивный коммит с типом docs, добавляющий или улучшающий документацию для вашей новой функции.
# Сделайте фиктивный коммит с типом test, добавляющий тесты для этой же функции.

# ## Answers
#
# 1. Purpose of Commit Types:
#
# - `feat` — adding a new feature.
# - `fix` — fixing a bug.
# - `docs` — changes only in documentation.
# - `style` — formatting adjustments that do not affect logic (indentation, spaces, etc.).
# - `refactor` — improving code without changing functionality.
# - `test` — adding or modifying tests.
# - `build` — changes affecting the build system or dependencies.
# - `ci` — modifications to CI/CD configuration.
# - `perf` — performance optimizations.
# - `chore` — technical changes that do not affect the code (e.g., dependency updates).
#
#
# 2. Fixing a bug in the rounding function
#
# ```
# fix(math): correct number rounding issue
#
# Previously, the rounding function incorrectly rounded 2.5 down instead of up.
# This fix ensures proper rounding based on standard rules.
#
# Fixes #42
# ```
#
# 3. Adding the generateReport function
#
# ```
# feat(reports): add generateReport function
#
# This function generates detailed reports in PDF format.
# It supports multiple data sources and customizable templates.
# ```
#
# 4. Formatting adjustments
#
# ```
# style: fix indentation and formatting across the project
# ```
#
# 5. Updating documentation for generateReport
#
# ```
# docs: added description of generateReport function to README
#
# test: added unit tests for generateReport
# ```
