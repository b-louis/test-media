# We define 2 operations SwapEven and SwapOdd
# SwapEven => we swap two letter with a even position
# SwapOdd => we swap two letter with a odd position
# string C and D are twins if its possible to obtain
# the same string with these two operations 

class Twin :
    val_ok="Yes"
    val_notok="No"
    @staticmethod
    def twins(a,b):
        """
        This function compare the ith string of two list
        and returns, for each ith terms if its are twins


        Parameters
        ----------

        a : list[string]
            the first list of n strings to compare

        b : list[string]
            the second list of n strings to compare


        Returns
        -------
        list[string]
            a list of string with either 'Yes' or 'No'
        """   
        if len(a)!=len(b):
            raise SizeError("Lists' sizes are different")

        result = []
        for i in range (len(a)):
            result.append(Twin.twincompute(a[i],b[i]))

        return result
    
    @staticmethod
    def twincompute(ai,bi):
        """
        This function compare 2 strings and
        return 'Yes' if they are twins and
        'No' if they arent.


        Parameters
        ----------

        ai : string
            the first string to compare

        bi : string
            the second string to compare


        Returns
        -------
        string
            a string with either 'Yes' or 'No'
        """
        
        if( not isinstance(ai, str) ):
            raise ValueError(str(ai)+" is not a string")
        elif(not isinstance(bi, str)):
            raise ValueError(str(bi)+" is not a string")
        elif (ai==bi):
            return Twin.val_ok
        elif(len(ai)!=len(bi) or len(ai)<=2 or len(bi)<=2):
            return Twin.val_notok

        else :
            # we extract the 'even' string (all the even character)
            # and the 'odd' string (all the odd character)
            # if the odd string of ai and bi contain the same letters
            # (same for the even string) they are twins

            #even
            l1 = ai[1::2]
            l2 = bi[1::2]

            #odd
            l1odd = ai[0::2]
            l2odd = bi[0::2]

            return Twin.val_ok if (sorted(l1)==sorted(l2)) and (sorted(l1odd)==sorted(l2odd)) else Twin.val_notok

