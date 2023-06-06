#initiasiling nominees
contestant1=input("Enter the name of the first contestant: ")
contestant2=input("Enter the name of the second contestant: ")

cnt1_votes= 0
cnt2_votes= 0

voters_id= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
no_of_voters= len(voters_id)

while True:
    voter = int(input("Enter your voter id: "))
    if voter in voters_id:
        print("You are a voter.")
        voters_id.remove(voter) #remove voter from the roll to prevent redudancy
        
        #voting
        print ("To give the vote to,"contestant1,"press 1")
        print("To give the vote to,"contestant2,"press 2")
        
        vote = int(input("Cast your vote: "))
        if vote == 1:
            cnt1_votes +=1
            print("Thank you")
        
        elif vote == 2:
            cnt2_votes +=1 
            print("Thanks")
        else
        print("You have already voted OR You are not a voter")
    
    
    
    
     if voters_id = [] #check voters id
    if cnt1_votes > cnt2_votes
    print ("cnt1 has won by this" percent "%" )
    percent = (cnt1_votes/no_of_voters) * 100
    break
    
     if cnt2_votes > cnt1_votes:
        print ("cnt2 has won by this" percent "%" )
    percent = (cnt2_votes/no_of_voters) * 100
    break
    
    
        
        