# Structured NSL Data
class NSL:
    def __init__(self, issue_date, nsl_file_number, year=None, company=None, release_date=None, link_to_nsl_file=None, link_to_release_letter=None, comment=None):
        self.issue_date = issue_date
        self.nsl_file_number = nsl_file_number
        self.nsl_file_number_int = int(nsl_file_number.split("(")[0])

        # The following are not available for all NSLs
        self.company = company
        self.year = year  
        self.release_date = release_date
        self.link_to_nsl_file = link_to_nsl_file
        self.link_to_release_letter = link_to_release_letter
        self.comment = comment

    def __repr__(self):
        return self.__str__()

    def _format_datetime(self, timestamp):
        return timestamp.strftime('%Y-%m-%d')

    def __str__(self):
        return f"NSL({self.nsl_file_number}, {self._format_datetime(self.issue_date)})"
    
    def export_as_csv_line(self):
        """
        Format: issue date, release date, company, file number, url, comment
        """
        line_data = [self._format_datetime(self.issue_date), self._format_datetime(self.release_date), self.company, self.nsl_file_number, self.link_to_nsl_file, self.comment]
        line_data_filtered = [entry if entry != None else "" for entry in line_data]
        return ",".join(line_data_filtered)