import requests
def main():
    
    base = input("First Currency:").upper()
    other = input("Second Currency:").upper()
    

    res = requests.get("http://data.fixer.io/api/latest?access_key=1e917c2b206bf0d64c56ac46842dc5ee")
                      
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    baseOutput = data["rates"][base]
    otherOutput = data ["rates"][other]
    ratio = float(otherOutput)/float(baseOutput)
    print("1", base, "is equal to", ratio, other)
    
if __name__ == "__main__":
          main()




