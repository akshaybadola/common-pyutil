# ChangeLog for common-pyutil

## [2021-05-05 Wed 16:19]
- Added ChangeLog
- Added gitignore.
- Added `decorators.py` and `decorators.Tag`
- Added docs to `monitor.Timer`
- Fixed `get_file_and_stream_logger` and `get_stream_logger` functions in `log.py`.
- Bump version to `0.2.0`.

## [2021-05-18 Tue 05:54]
- Added `apply_list` and `set_lens`.
- Added types to `functional` module
- Added `any_attr` and `all_attrs` in `functional` module.
- Added `functional.zip_with`
- Added `system.Semver`. Got annoyed with existing python semver library with
  its warnings of breaking changes and all that. This is much simpler and I'm
  sure will work well.
- Version bump.

## [2021-07-30 Fri 15:44]
- Added `contexts.py`
- Changed some parts of `get_file_and_stream_logger`
- Added `Tag.add`
- Version bump to "0.6.0"

## [2021-08-13 Fri 04:31]
- Fixed a bug in loading.
- Added types to `io`.
- Added `system.hierarchical_parser`.
- Added example to `Timer`.
- Added `Tag.remove`

## [2021-09-02 Thu 14:38]
- Added `functional.unique`
- Added `functional.exactly_one`
- Added kwargs to `functional.rpartial`
- Added docstring to `prompt`
- Added aborting functionality to `net.Get` and fixed some issues.
- Added `geq` and `leq` to `system.Semver`
- Version bump to "0.7.2"

## [2021-10-20 Wed 07:52]
- Added `dropwhile` and fixed docstring of `takewhile`
- Removed `Timer` from contexts as it was there in `monitor`
- Added docstring and types to `recurse_dict` and function `recurse_dict_pred_val`
- Added global options in `hierarchical_parser` and improved docstring
