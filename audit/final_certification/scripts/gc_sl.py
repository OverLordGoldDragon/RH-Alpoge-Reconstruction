"""gc_sl.py: resolve the SL-1..SL-4 leaves of Post_Closure_Internal_Residuals.md on the live graph; exclusive sizes."""
import sys, pickle, re; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
L=np.load('/home/claude/idx/gc_live.npy')
SL={'SL-1':"testRest_bound hhTestBound_hhFl flagHeight_holds hhFl_labelInv antisymPerturbation_holds rest_sum_primes_bound lie_term_flag_bound factorial_half_power_sum_le flag_degree_weight_formula flag_shift_total_power_sum sum_log_div_pred_le compact_datum_intersection adapted_family_exists_on_eigenspace exists_action exists_labVal lieMult_constant_along_cmType",
'SL-2':"tan_lowest rank_le_of_lowest eii fibTrdeg fib_gen nicePrimeEx v0e elts2 adj2",
'SL-3':"Kop_contract DnM_diag part_U part_sum part_alt_alt new_vector_letter_plus c_diagonal frame_module_of_word StepImportsQ",
'SL-4':"stepC_of stepDEF_of phi_pair lead_bound RestCols RestPre RestTCore PickStep MembStep NumStep MemStep OntoAll IsTrueTheta RestPad SumFacts WalkSharp valuation_window_lower_bound windowMeanAP admissible_entries_small_chain datum_exists_coprime kills split_of_ss matFg finSub conj_const testEx"}
suf={}
for i,n in enumerate(q.names):
    suf.setdefault(n.rsplit('.',1)[-1],[]).append(i)
out={}
for g,s in SL.items():
    for t in s.split():
        ids=[i for i in suf.get(t,[]) if L[i]]
        out[(g,t)]=ids
        print(g,t,len(suf.get(t,[])),"live:",[(q.names[i],q.kinds[i],q.locs[i][0].split('/')[-1],q.locs[i][2]-q.locs[i][1]) for i in ids][:4])
pickle.dump(out,open('/home/claude/idx/gc_sl.pkl','wb'))
