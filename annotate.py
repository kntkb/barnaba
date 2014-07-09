import pdbreader as pb
import tools as t
import numpy as N

##################### ANNOTATE #######################

def annotate(args,files):

    print "# Annotating RNA structures..."

    fh = open(args.name,'w')
    pb.write_args(args,fh)

    for f in files:
        atoms,sequence = pb.get_coord(f)
        count = 0
        for model,seq in zip(atoms,sequence):
            count += 1
            string = '# ' + f + "-" + str(count) + " "
            lcs,origo = t.coord2lcs(model)
            mat = t.lcs2mat_3d(lcs,origo,args.cutoff)
            int_mat = t.analyze_mat(mat,seq)
            if(args.compact==True):
                for j in range(int_mat.shape[0]):
                    for k in range(j+1,int_mat.shape[0]):
                        string += "%4s " % (t.interactions[int(int_mat[j,k])])
                fh.write(string + "\n")
            else:
                string += "\n"
                fh.write(string)
                for j in range(int_mat.shape[0]):
                    for k in range(j+1,int_mat.shape[0]):
                        if(int_mat[j,k] != 0):
                            string  = "%10s %10s %4s \n" % (seq[j],seq[k],t.interactions[int(int_mat[j,k])])
                            fh.write(string)
    fh.close()
    return 0
            
##################### ANNOTATE #######################
