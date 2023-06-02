#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else

    if x<y:   
        result= "x less than y"
    elif x==y:
        result="x is y"
    else:
        result="x not less than y"


    # conditional statements let you use "a if C else b"

    result="x is less than y" if x<y else "x is greater"
    # match-case makes it easy to compare multiple values
    value = "five"
    match value:
        case "one":
            result=1
        case "three" | "four":
            result=34
        case _:
            result=-1
    
    print(result) 
if __name__ == "__main__":
    main()
