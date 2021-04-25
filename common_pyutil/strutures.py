from typing import List, Dict, Any, Callable


def recurse_dict(jdict: Dict[str, Any],
                 pred: Callable[[str, Any], bool],
                 repl: Callable[[str, str], str],
                 repl_only: bool = False) -> Dict[str, Any]:
    """Recurse over a :class:`dict` and perform replacement.

    This function replaces the values of the dictionary in place. Used to
    fix the generated schema :class:`dict`.

    Args:
        jdict: A dictionary
        pred: Predicate to check when to perform replacement
        repl: Function which performs the replacement

    Returns:
        A modified dictionary

    """
    if not (isinstance(jdict, dict) or isinstance(jdict, list)):
        return jdict
    if isinstance(jdict, dict):
        for k, v in jdict.items():
            if pred(k, v):
                jdict[k] = repl(k, v)
                if repl_only:
                    continue
            if isinstance(v, dict):
                jdict[k] = recurse_dict(v, pred, repl, repl_only)
            if isinstance(v, list):
                for i, item in enumerate(v):
                    v[i] = recurse_dict(item, pred, repl, repl_only)
    elif isinstance(jdict, list):
        for i, item in enumerate(jdict):
            jdict[i] = recurse_dict(item, pred, repl, repl_only)
    return jdict
