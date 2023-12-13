
class BibtexFilter:
    def __init__(self):
        pass

    def filter_by(self, filter_type, keyword, all_references):
        filtered = []
        found = False
        for ref in all_references:
            for row in ref:
                if filter_type in row and keyword in row:
                    found = True
            if found:
                filtered.append(ref)
                found = False
        return filtered
