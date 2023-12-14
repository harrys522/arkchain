import sys
import libsnark.alt_bn128 as libsnark

class mysnark:
    def __init__(self):        
        pb=libsnark.ProtoboardPub()
        # create variables
        inv=libsnark.PbVariable()
        inv.allocate(pb)
        pb.setpublic(inv)

        in_t=libsnark.PbVariable()
        in_t.allocate(pb)

        outv=libsnark.PbVariable()
        outv.allocate(pb)
        pb.setpublic(outv)

        # create constraints
        # let int=inv*(2*inv+1)
        pb.add_r1cs_constraint(libsnark.R1csConstraint(libsnark.LinearCombination(inv),
                                                libsnark.LinearCombination(inv)*2+libsnark.LinearCombination(1),
                                                libsnark.LinearCombination(in_t)))
                       
        # let out=(int-1)*inv
        pb.add_r1cs_constraint(libsnark.R1csConstraint(libsnark.LinearCombination(in_t)-libsnark.LinearCombination(1),
                                                libsnark.LinearCombination(inv),
                                                libsnark.LinearCombination(outv)))
        
        # create witnesses
        pb.setval(inv, 3)
        pb.setval(in_t, 21)
        pb.setval(outv, 60)

        self.pb = pb
        
    def generate_proof(self):
        pb = self.pb

        cs=pb.get_constraint_system_pubs()
        pubvals=pb.primary_input_pubs()
        privvals=pb.auxiliary_input_pubs()

        print("*** Trying to read key")
        keypair=libsnark.zk_read_key("ekfile", cs)
        if not keypair:
            print("*** No key or computation changed, generating keys...")
            keypair=libsnark.zk_generator(cs)
            libsnark.zk_write_keys(keypair, "vkfile", "ekfile")
            
        print("*** Generating proof (" +
            "sat=" + str(pb.is_satisfied()) + 
            ", #io=" + str(pubvals.size()) + 
            ", #witness=" + str(privvals.size()) + 
            ", #constraint=" + str(pb.num_constraints()) +
            ")")
            
        proof=libsnark.zk_prover(keypair.pk, pubvals, privvals);
        libsnark.cvar.binary_output = False
        libsnark.cvar.no_pt_compression = False
        libsnark.cvar.montgomery_output = False
        proof.write(sys.stdout)

        libsnark.cvar.no_pt_compression = True
        proof.write(sys.stdout)

        print("proof is", pubvals.str())

        return pubvals, keypair, proof
    
    def verify_proof(self, pubvals, keypair, proof):
        verified=libsnark.zk_verifier_strong_IC(keypair.vk, pubvals, proof);
    
        print("*** Public inputs: " + " ".join([str(pubvals.at(i)) for i in range(pubvals.size())]))
        print("*** Verification status:", verified)

#test = mysnark()
#x,y,z = test.generate_proof()
#test.verify_proof(x,y,z)

