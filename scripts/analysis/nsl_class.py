from datetime import datetime

# Structured NSL Data
class NSL:
    @staticmethod
    def create_from_csv_line(csv_line):
        issue_date, release_date, company, nsl_file_number, link_to_nsl_file, comment = csv_line.split(",")
        issue_date = NSL.parse_strftime(issue_date)
        release_date = NSL.parse_strftime(release_date)
        return NSL(issue_date, release_date, company, nsl_file_number, link_to_nsl_file, comment)

    @staticmethod
    def format_datetime(timestamp):
        return timestamp.strftime('%Y-%m-%d')

    @staticmethod
    def parse_strftime(timestamp_str):
        """
        Parse string as datetime instance
        """
        return datetime.strptime(timestamp_str, '%Y-%m-%d')
    
    @staticmethod
    def parse_file_number(file_number):
        """
        Some files have letters like (a) or (b) after their number,
        we parse them and add this as a fraction to the file number to
        disambiguate letters.
        """

        if type(file_number) == int:
            return float(file_number)
        
        nsl_file_number_parts = file_number.split("(")
        nsl_file_number_float = float(nsl_file_number_parts[0])
        
        # handle (a)/(b) in file name
        if len(nsl_file_number_parts) > 1:
            letter_fraction = (ord(nsl_file_number_parts[1][:-1]) - ord("a"))/26
            nsl_file_number_float += letter_fraction

        return nsl_file_number_float
    
    @staticmethod
    def export_nsls_as_csv(nsls, csv_file_path):
        with open(csv_file_path, "w") as csv_file:
            csv_file.write("issue date,release date,company,file number,url,comment\n")
            for nsl in nsls:
                csv_file.write(nsl.export_as_csv_line() + "\n")

    def __init__(self, issue_date, nsl_file_number, year=None, company=None, release_date=None, link_to_nsl_file=None, link_to_release_letter=None, comment=None):
        self.issue_date = issue_date
        self.nsl_file_number = nsl_file_number
        self.nsl_file_number_float = NSL.parse_file_number(nsl_file_number)

    
        # The following are not available for all NSLs
        self.company = company
        self.year = year  
        self.release_date = release_date
        self.link_to_nsl_file = link_to_nsl_file
        self.link_to_release_letter = link_to_release_letter
        self.comment = comment

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"NSL({self.nsl_file_number}, {self._format_datetime(self.issue_date)})"
    
    def export_as_csv_line(self):
        """
        Format: issue date, release date, company, file number, url, comment
        """
        line_data = [NSL.format_datetime(self.issue_date), NSL.format_datetime(self.release_date), self.company, self.nsl_file_number, self.link_to_nsl_file, self.comment]
        line_data_filtered = [entry if entry != None else "" for entry in line_data]
        return ",".join(line_data_filtered)