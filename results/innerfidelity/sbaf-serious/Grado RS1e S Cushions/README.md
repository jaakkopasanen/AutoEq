# Grado RS1e S Cushions

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.2; 37 4.5; 41 3.5; 45 2.7; 49 1.9; 54 1.1; 60 0.2; 66 -0.5; 72 -1.1; 79 -1.7; 87 -2.4; 96 -2.9; 106 -3.3; 116 -3.5; 128 -3.7; 141 -3.9; 155 -4.0; 170 -3.9; 187 -3.8; 206 -3.5; 227 -3.2; 249 -3.0; 274 -2.9; 302 -2.8; 332 -2.4; 365 -2.0; 402 -1.7; 442 -1.3; 486 -1.1; 535 -0.9; 588 -0.4; 647 -0.2; 712 -0.2; 783 0.1; 861 0.0; 947 0.1; 1042 0.1; 1146 0.1; 1261 0.4; 1387 0.4; 1526 1.1; 1678 -0.9; 1846 -6.7; 2031 -6.0; 2234 -3.3; 2457 0.0; 2703 2.8; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e S Cushions ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.55 | 7.9 dB   |
| Peaking | 130 Hz  |  0.32 | -5.6 dB  |
| Peaking | 690 Hz  |  0.21 | 1.4 dB   |
| Peaking | 1987 Hz |  3.64 | -10.1 dB |
| Peaking | 4053 Hz |  1    | 6.6 dB   |
| Peaking | 1615 Hz |  7.69 | 2.8 dB   |
| Peaking | 1796 Hz | 10.8  | -2.6 dB  |
| Peaking | 6292 Hz |  2.96 | 4.8 dB   |
| Peaking | 7171 Hz |  1    | -2.0 dB  |
| Peaking | 7473 Hz |  3.12 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20S%20Cushions/Grado%20RS1e%20S%20Cushions.png)