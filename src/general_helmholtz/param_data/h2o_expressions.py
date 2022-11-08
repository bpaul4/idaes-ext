
##################################################################################
#                                                                                #
# H2O EOS Expressions and Parameters:                                            #
#                                                                                #
# International Association for the Properties of Water and Steam (2016).        #
#     IAPWS R6-95 (2016), "Revised Release on the IAPWS Formulation 1995 for     #
#     the Properties of Ordinary Water Substance for General Scientific Use,"    #
#     URL: http://iapws.org/relguide/IAPWS95-2016.pdf                            #
# Wagner, W.,  A. Pruss (2002). "The IAPWS Formulation 1995 for the              #
#     Thermodynamic Properties of Ordinary Water Substance for General and       #
#     Scientific Use." J. Phys. Chem. Ref. Data, 31, 387-535.                    #
# Wagner, W. et al. (2000). "The IAPWS Industrial Formulation 1997 for the       #
#     Thermodynamic Properties of Water and Steam," ASME J. Eng. Gas Turbines    #
#     and Power, 122, 150-182.                                                   #
#                                                                                #
##################################################################################

import pyomo.environ as pyo
import json
from helmholtz_parameters import WriteParameters


def main():
    m = pyo.ConcreteModel()
    m.delta = pyo.Var()
    m.tau = pyo.Var()

    c = {
        8: 1,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 1,
        14: 1,
        15: 1,
        16: 1,
        17: 1,
        18: 1,
        19: 1,
        20: 1,
        21: 1,
        22: 1,
        23: 2,
        24: 2,
        25: 2,
        26: 2,
        27: 2,
        28: 2,
        29: 2,
        30: 2,
        31: 2,
        32: 2,
        33: 2,
        34: 2,
        35: 2,
        36: 2,
        37: 2,
        38: 2,
        39: 2,
        40: 2,
        41: 2,
        42: 2,
        43: 3,
        44: 3,
        45: 3,
        46: 3,
        47: 4,
        48: 6,
        49: 6,
        50: 6,
        51: 6,
    }

    d = {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 3,
        7: 4,
        8: 1,
        9: 1,
        10: 1,
        11: 2,
        12: 2,
        13: 3,
        14: 4,
        15: 4,
        16: 5,
        17: 7,
        18: 9,
        19: 10,
        20: 11,
        21: 13,
        22: 15,
        23: 1,
        24: 2,
        25: 2,
        26: 2,
        27: 3,
        28: 4,
        29: 4,
        30: 4,
        31: 5,
        32: 6,
        33: 6,
        34: 7,
        35: 9,
        36: 9,
        37: 9,
        38: 9,
        39: 9,
        40: 10,
        41: 10,
        42: 12,
        43: 3,
        44: 4,
        45: 4,
        46: 5,
        47: 14,
        48: 3,
        49: 6,
        50: 6,
        51: 6,
        52: 3,
        53: 3,
        54: 3,
    }

    t = {
        1: -0.5,
        2: 0.875,
        3: 1,
        4: 0.5,
        5: 0.75,
        6: 0.375,
        7: 1,
        8: 4,
        9: 6,
        10: 12,
        11: 1,
        12: 5,
        13: 4,
        14: 2,
        15: 13,
        16: 9,
        17: 3,
        18: 4,
        19: 11,
        20: 4,
        21: 13,
        22: 1,
        23: 7,
        24: 1,
        25: 9,
        26: 10,
        27: 10,
        28: 3,
        29: 7,
        30: 10,
        31: 10,
        32: 6,
        33: 10,
        34: 10,
        35: 1,
        36: 2,
        37: 3,
        38: 4,
        39: 8,
        40: 6,
        41: 9,
        42: 8,
        43: 16,
        44: 22,
        45: 23,
        46: 23,
        47: 10,
        48: 50,
        49: 44,
        50: 46,
        51: 50,
        52: 0,
        53: 1,
        54: 4,
    }

    n = {
        1: 0.12533547935523e-1,
        2: 0.78957634722828e1,
        3: -0.87803203303561e1,
        4: 0.31802509345418,
        5: -0.26145533859358,
        6: -0.78199751687981e-2,
        7: 0.88089493102134e-2,
        8: -0.66856572307965,
        9: 0.20433810950965,
        10: -0.66212605039687e-4,
        11: -0.19232721156002,
        12: -0.25709043003438,
        13: 0.16074868486251,
        14: -0.40092828925807e-1,
        15: 0.39343422603254e-6,
        16: -0.75941377088144e-5,
        17: 0.56250979351888e-3,
        18: -0.15608652257135e-4,
        19: 0.11537996422951e-8,
        20: 0.36582165144204e-6,
        21: -0.13251180074668e-11,
        22: -0.62639586912454e-9,
        23: -0.10793600908932,
        24: 0.17611491008752e-1,
        25: 0.22132295167546,
        26: -0.40247669763528,
        27: 0.58083399985759,
        28: 0.49969146990806e-2,
        29: -0.31358700712549e-1,
        30: -0.74315929710341,
        31: 0.47807329915480,
        32: 0.20527940895948e-1,
        33: -0.13636435110343,
        34: 0.14180634400617e-1,
        35: 0.83326504880713e-2,
        36: -0.29052336009585e-1,
        37: 0.38615085574206e-1,
        38: -0.20393486513704e-1,
        39: -0.16554050063743e-2,
        40: 0.19955571979541e-2,
        41: 0.15870308324157e-3,
        42: -0.16388568342530e-4,
        43: 0.43613615723811e-1,
        44: 0.34994005463765e-1,
        45: -0.76788197844621e-1,
        46: 0.22446277332006e-1,
        47: -0.62689710414685e-4,
        48: -0.55711118565645e-9,
        49: -0.19905718354408,
        50: 0.31777497330738,
        51: -0.11841182425981,
        52: -0.31306260323435e2,
        53: 0.31546140237781e2,
        54: -0.25213154341695e4,
        55: -0.14874640856724,
        56: 0.31806110878444,
    }

    a = {
        52: 20,
        53: 20,
        54: 20,
    }

    b = {
        52: 150,
        53: 150,
        54: 250,
    }

    g = {
        52: 1.21,
        53: 1.21,
        54: 1.25,
    }

    e = {
        52: 1,
        53: 1,
        54: 1,
    }

    n0 = {
        1: -8.3204464837497,
        2: 6.6832105275932,
        3: 3.00632,
        4: 0.012436,
        5: 0.97315,
        6: 1.27950,
        7: 0.96956,
        8: 0.24873,
    }

    g0 = {
        4: 1.28728967,
        5: 3.53734222,
        6: 7.74073708,
        7: 9.24437796,
        8: 27.5075105,
    }

    we = WriteParameters(
        comp="h2o",
        R=0.46151805,
        MW=18.015268,
        T_star=647.096,
        rho_star=322.0,
        Tc=647.096,
        rhoc=322.0,
        Pc=22064.0,
        Tt=273.16,
        Pt=0.611655,
        rhot_l=999.793,
        rhot_v=0.00485458,
        P_min=1e-9,
        P_max=1.1e6,
        rho_max=1250.0,
        T_min=235,
        T_max=1300,
    )
    m = we.model
    we.add(
        {
            "phii": pyo.log(m.delta)
            + n0[1]
            + n0[2] * m.tau
            + n0[3] * pyo.log(m.tau)
            + sum(
                n0[i] * pyo.log(1 - pyo.exp(-g0[i] * m.tau)) for i in range(4, 8 + 1)
            ),
            "phii_d": 1.0 / m.delta,
            "phii_dd": -1.0 / m.delta**2,
            "phii_t": n0[2]
            + n0[3] / m.tau
            + sum(
                n0[i] * g0[i] * ((1 - pyo.exp(-g0[i] * m.tau)) ** (-1) - 1)
                for i in range(4, 8 + 1)
            ),
            "phii_tt": -n0[3] / m.tau**2
            - sum(
                n0[i]
                * g0[i] ** 2
                * pyo.exp(-g0[i] * m.tau)
                * (1 - pyo.exp(-g0[i] * m.tau)) ** (-2)
                for i in range(4, 8 + 1)
            ),
            "phii_dt": 0,
            "phir": sum(n[i] * m.delta ** d[i] * m.tau ** t[i] for i in range(1, 7 + 1))
            + sum(
                n[i] * m.delta ** d[i] * m.tau ** t[i] * pyo.exp(-m.delta ** c[i])
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.delta ** d[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                for i in range(52, 54 + 1)
            ),
            "phir_d": sum(
                n[i] * d[i] * m.delta ** (d[i] - 1) * m.tau ** t[i]
                for i in range(1, 7 + 1)
            )
            + sum(
                n[i]
                * pyo.exp(-m.delta ** c[i])
                * m.delta ** (d[i] - 1)
                * m.tau ** t[i]
                * (d[i] - c[i] * m.delta ** c[i])
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.delta ** d[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                * (d[i] / m.delta - 2 * a[i] * (m.delta - e[i]))
                for i in range(52, 54 + 1)
            ),
            "phir_dd": sum(
                n[i] * d[i] * (d[i] - 1) * m.delta ** (d[i] - 2) * m.tau ** t[i]
                for i in range(1, 7 + 1)
            )
            + sum(
                n[i]
                * pyo.exp(-m.delta ** c[i])
                * m.delta ** (d[i] - 2)
                * m.tau ** t[i]
                * (
                    (d[i] - c[i] * m.delta ** c[i])
                    * (d[i] - 1 - c[i] * m.delta ** c[i])
                    - c[i] ** 2 * m.delta ** c[i]
                )
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                * (
                    -2.0 * a[i] * m.delta ** d[i]
                    + 4 * a[i] ** 2 * m.delta ** d[i] * (m.delta - e[i]) ** 2
                    - 4 * d[i] * a[i] * m.delta ** (d[i] - 1) * (m.delta - e[i])
                    + d[i] * (d[i] - 1) * m.delta ** (d[i] - 2)
                )
                for i in range(52, 54 + 1)
            ),
            "phir_t": sum(
                n[i] * t[i] * m.delta ** d[i] * m.tau ** (t[i] - 1)
                for i in range(1, 7 + 1)
            )
            + sum(
                n[i]
                * t[i]
                * m.delta ** d[i]
                * m.tau ** (t[i] - 1)
                * pyo.exp(-m.delta ** c[i])
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.delta ** d[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                * (t[i] / m.tau - 2 * b[i] * (m.tau - g[i]))
                for i in range(52, 54 + 1)
            ),
            "phir_tt": sum(
                n[i] * t[i] * (t[i] - 1) * m.delta ** d[i] * m.tau ** (t[i] - 2)
                for i in range(1, 7 + 1)
            )
            + sum(
                n[i]
                * t[i]
                * (t[i] - 1)
                * m.delta ** d[i]
                * m.tau ** (t[i] - 2)
                * pyo.exp(-m.delta ** c[i])
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.delta ** d[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                * (
                    (t[i] / m.tau - 2 * b[i] * (m.tau - g[i])) ** 2
                    - t[i] / m.tau**2
                    - 2 * b[i]
                )
                for i in range(52, 54 + 1)
            ),
            "phir_dt": sum(
                n[i] * t[i] * d[i] * m.delta ** (d[i] - 1) * m.tau ** (t[i] - 1)
                for i in range(1, 7 + 1)
            )
            + sum(
                n[i]
                * t[i]
                * m.delta ** (d[i] - 1)
                * m.tau ** (t[i] - 1)
                * (d[i] - c[i] * m.delta ** c[i])
                * pyo.exp(-m.delta ** c[i])
                for i in range(8, 51 + 1)
            )
            + sum(
                n[i]
                * m.delta ** d[i]
                * m.tau ** t[i]
                * pyo.exp(-a[i] * (m.delta - e[i]) ** 2 - b[i] * (m.tau - g[i]) ** 2)
                * (d[i] / m.delta - 2.0 * a[i] * (m.delta - e[i]))
                * (t[i] / m.tau - 2.0 * b[i] * (m.tau - g[i]))
                for i in range(52, 54 + 1)
            ),
            "delta_v_sat_approx": pyo.exp(
                -2.03150240 * (1 - 1.0 / m.tau) ** (2.0 / 6.0)
                - 2.68302940 * (1 - 1.0 / m.tau) ** (4.0 / 6.0)
                - 5.38626492 * (1 - 1.0 / m.tau) ** (8.0 / 6.0)
                - 17.2991605 * (1 - 1.0 / m.tau) ** (18.0 / 6.0)
                - 44.7586581 * (1 - 1.0 / m.tau) ** (37.0 / 6.0)
                - 63.9201063 * (1 - 1.0 / m.tau) ** (71.0 / 6.0)
            ),
            "delta_l_sat_approx": (
                1.001
                + 1.99274064 * (1 - 1.0 / m.tau) ** (1.0 / 3.0)
                + 1.09965342 * (1 - 1.0 / m.tau) ** (2.0 / 3.0)
                - 0.510839303 * (1 - 1.0 / m.tau) ** (5.0 / 3.0)
                - 1.75493479 * (1 - 1.0 / m.tau) ** (16.0 / 3.0)
                - 45.5170352 * (1 - 1.0 / m.tau) ** (43.0 / 3.0)
                - 6.74694450e5 * (1 - 1.0 / m.tau) ** (110.0 / 3.0)
            ),
        }
    )
    we.write()


if __name__ == "__main__":
    main()
