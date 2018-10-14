# Paradigm Shift E1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.9; 23 -6.0; 25 -6.0; 28 -6.2; 31 -6.3; 34 -6.4; 37 -6.4; 41 -6.5; 45 -6.6; 49 -6.7; 54 -6.9; 60 -7.2; 66 -7.4; 72 -7.7; 79 -8.0; 87 -8.3; 96 -8.7; 106 -8.8; 116 -8.9; 128 -9.1; 141 -9.2; 155 -9.2; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.3; 249 -8.0; 274 -7.5; 302 -6.9; 332 -6.3; 365 -5.6; 402 -4.9; 442 -3.9; 486 -3.3; 535 -2.5; 588 -1.6; 647 -0.9; 712 -0.6; 783 0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.4; 1261 1.5; 1387 1.7; 1526 2.3; 1678 2.6; 1846 3.8; 2031 5.4; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.3; 5267 4.6; 5793 4.0; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.2  | -5.6 dB |
| Peaking | 134 Hz  | 0.68 | -4.6 dB |
| Peaking | 277 Hz  | 0.83 | -4.4 dB |
| Peaking | 3178 Hz | 0.72 | 6.8 dB  |
| Peaking | 2178 Hz | 3.22 | 2.5 dB  |
| Peaking | 2404 Hz | 1.05 | -1.3 dB |
| Peaking | 4786 Hz | 2.44 | 1.9 dB  |
| Peaking | 6492 Hz | 5.05 | 4.4 dB  |
| Peaking | 7162 Hz | 1.21 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E1/Paradigm%20Shift%20E1.png)