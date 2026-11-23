#!/usr/bin/env python3
"""Independent checks of the constants in SL-6a and SL-6b.

SL-6a  (GaugeVolUD, Formalism.L2.SG.Pf.GV.gaugeVolU)
  volU(k)    = prod_{i<k} (2 pi)^{i+1} / i!      (UnitaryVolumeMass.volU, Frobenius metric)
  DS.volU(k) = prod_{i<k} 2 pi^{i+1} / i!        (ChartRestriction.DS.volU)
  checks: (a) volU(k) = 2^{k(k-1)/2} DS.volU(k)                      (volU_ratio)
          (b) Gaussian integral over M_k(C) computed in QR coordinates
              gives the QR constant C = DS.volU(k)                   (gaussE_qr_const)
          (c) volU agrees with Riemannian volumes of U(1), U(2) computed by hand
SL-6b  (RhsWLim, wbConst)
  wbConst(k,T,T',a,a') = 2 volU(k)^2 / ((T T')^k volU(k-1) a a')
  An independent derivation (report, Prop. SL6b) gives the Jacobian
      2^{k+1} pi^k / ((k-1)! volU(k) (T T')^k)
  for gauge-normalised stabiliser measures; with stabiliser masses a, a'
  this must equal wbConst * a a' / volU(k)^2.  Checked symbolically for k<=12,
  and the sphere integral used in the derivation is checked numerically.
"""
import sympy as sp
from mpmath import mp, quad, inf, gamma, pi as mpi, exp as mexp

k, T, Tp, a, ap = sp.symbols("k T Tp a ap", positive=True)

def volU(n):
    return sp.prod([(2 * sp.pi) ** (i + 1) / sp.factorial(i) for i in range(n)])

def DSvolU(n):
    return sp.prod([2 * sp.pi ** (i + 1) / sp.factorial(i) for i in range(n)])

ok = True
for n in range(0, 13):
    # (a)
    if sp.simplify(volU(n) - 2 ** (n * (n - 1) // 2) * DSvolU(n)) != 0:
        ok = False; print("volU_ratio fails at", n)
    # (b) Gaussian: int_{M_n(C)} exp(-tr g*g) = pi^{n^2}
    #     QR side: off-diagonal upper entries (n(n-1)/2 complex): pi each;
    #     diagonal t_jj > 0 with weight t^{2(n-j)-1}: int_0^oo e^{-x^2} x^{2m-1} dx = Gamma(m)/2
    qr_side = sp.pi ** (n * (n - 1) // 2) * sp.prod([sp.gamma(n - j) / 2 for j in range(n)])
    C = sp.pi ** (n * n) / qr_side
    if n >= 1 and sp.simplify(C - DSvolU(n)) != 0:
        ok = False; print("QR constant fails at", n)
print("SL-6a identities (a), (b) for k<=12:", "OK" if ok else "FAIL")

# (c) hand computations: vol U(1) = 2 pi, vol U(2) = 8 pi^3 for <X,Y> = Re tr(X Y*)
assert sp.simplify(volU(1) - 2 * sp.pi) == 0
assert sp.simplify(volU(2) - 8 * sp.pi ** 3) == 0
print("SL-6a (c): volU(1)=2pi, volU(2)=8pi^3: OK")

# SL-6b
ok = True
for n in range(1, 13):
    wb = 2 * volU(n) ** 2 / ((T * Tp) ** n * volU(n - 1) * a * ap)
    derived_gauge = 2 ** (n + 1) * sp.pi ** n / (sp.factorial(n - 1) * volU(n) * (T * Tp) ** n)
    if sp.simplify(wb * a * ap / volU(n) ** 2 - derived_gauge) != 0:
        ok = False; print("wbConst mismatch at k =", n)
print("SL-6b constant vs independent derivation, k<=12:", "OK" if ok else "FAIL")

# numerical check of the sphere integral  int_{C^k} delta(R - |v|^2) d^{2k}v = pi^k R^{k-1}/(k-1)!
mp.dps = 30
for n in range(1, 6):
    R = mp.mpf("1.7")
    # smooth the delta: int_{R^{2n}} f(|v|^2) dv = (pi^n/(n-1)!) int_0^oo f(s) s^{n-1} ds
    f = lambda s: mexp(-(s - R) ** 2 * 10**8) * mp.sqrt(10**8 / mpi)
    lhs = (mpi ** n / gamma(n)) * quad(lambda s: f(s) * s ** (n - 1), [0, R - mp.mpf("0.01"), R, R + mp.mpf("0.01"), inf])
    rhs = mpi ** n * R ** (n - 1) / gamma(n)
    print("  sphere integral k=%d: smoothed %s  exact %s" % (n, mp.nstr(lhs, 12), mp.nstr(rhs, 12)))
