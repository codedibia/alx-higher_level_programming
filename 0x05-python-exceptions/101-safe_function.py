def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
