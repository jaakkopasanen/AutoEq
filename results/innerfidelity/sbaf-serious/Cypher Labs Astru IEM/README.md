# Cypher Labs Astru IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.5; 28 3.9; 31 3.4; 34 3.0; 37 2.5; 41 2.0; 45 1.6; 49 1.2; 54 0.7; 60 0.2; 66 -0.3; 72 -0.8; 79 -1.3; 87 -1.8; 96 -2.3; 106 -2.6; 116 -2.9; 128 -3.3; 141 -3.5; 155 -3.7; 170 -3.9; 187 -3.9; 206 -3.9; 227 -3.8; 249 -3.7; 274 -3.5; 302 -3.3; 332 -3.0; 365 -2.7; 402 -2.3; 442 -1.9; 486 -1.6; 535 -1.2; 588 -0.5; 647 -0.2; 712 0.1; 783 0.4; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -2.8; 1678 -3.8; 1846 -4.7; 2031 -5.3; 2234 -5.0; 2457 -3.1; 2703 -2.3; 2973 -0.7; 3270 1.0; 3597 0.6; 3957 -2.0; 4353 -4.1; 4788 -1.8; 5267 -1.1; 5793 -0.6; 6373 2.1; 7010 0.7; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.41 | 6.6 dB  |
| Peaking | 190 Hz  |  0.48 | -4.3 dB |
| Peaking | 1972 Hz |  1.31 | -9.8 dB |
| Peaking | 2093 Hz |  0.47 | 4.6 dB  |
| Peaking | 4417 Hz |  4.79 | -5.4 dB |
| Peaking | 2727 Hz |  3.88 | -0.7 dB |
| Peaking | 3344 Hz |  7.15 | 1.7 dB  |
| Peaking | 5589 Hz | 10.31 | -3.1 dB |
| Peaking | 6202 Hz |  5.89 | 2.2 dB  |
| Peaking | 8908 Hz |  1.37 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM/Cypher%20Labs%20Astru%20IEM.png)