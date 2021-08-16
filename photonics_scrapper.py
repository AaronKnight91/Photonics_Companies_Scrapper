import argparse
import os
import pandas as pd
from BaseScrapper import BaseScrapper

class GetPhotonicsData(BaseScrapper):
    
    '''Scrape photonics company data
       
       This class inherits from the BaseScrapper class'''
    
    def __init__(self, webpage):
        
        BaseScrapper.__init__(self, webpage)

        # This is the MasterName coloumn on the website
        td_1 = self._soup.find_all("td", {"class":"column-1"})        
        self._td_1 = [i.text for i in td_1]
        
        # This is the OtherName1 coloumn on the website
        td_2 = self._soup.find_all("td", {"class":"column-2"})        
        self._td_2 = [i.text for i in td_2]

        # This is the OtherName2 column on the website
        td_3 = self._soup.find_all("td", {"class":"column-3"})        
        self._td_3 = [i.text for i in td_3]
        
    def create_dataframe(self):
        
        # Create a dataframe of the scraped data
        
        arr = [] # Array to create the dataframe from
        for i in range(len(self._td_1)):
            row = [] # Array for each row in the dataframe
            row.append(self._td_1[i])
            row.append(self._td_2[i])
            row.append(self._td_3[i])
            arr.append(row) # Append the row to the larger array
            
        # Headers used in the dataframe
        headers = ["Master Name", "Other Name 1", "Other Name 2"]
        df = pd.DataFrame(arr, columns=headers)

        return df

def main(args):

    scrapper = GetPhotonicsData(args.website)        
    df = scrapper.create_dataframe()

    df.to_csv(os.path.join(args.outpath, args.outfile), index=False)    

def check_arguments():
    
    # Function to check commmand line input
    # If no command line input is given, default values will be used
    
    parse = argparse.ArgumentParser(description="Check arguments for photonics scrapper")

    parse.add_argument("--website","-w",type=str,help="The URL that data will be scrapped from",default="https://photonicsuk.org/uk-photonics-companies")

    parse.add_argument("--outpath","-o",type=str,help="Path to the output file",default="./")
    parse.add_argument("--outfile","-f",type=str,help="The name of the output file",default="uk_photonics_companies.csv")

    args = parse.parse_args()
    return args
    
if __name__ == "__main__":
    args = check_arguments()
    main(args)        

