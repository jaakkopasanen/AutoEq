# Aiaiai TMA-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.3; 31 4.3; 34 3.3; 37 2.4; 41 1.4; 45 0.6; 49 0.0; 54 -0.7; 60 -1.2; 66 -1.6; 72 -1.8; 79 -2.3; 87 -2.5; 96 -2.5; 106 -2.7; 116 -3.3; 128 -3.6; 141 -3.8; 155 -3.9; 170 -3.7; 187 -4.0; 206 -4.2; 227 -4.0; 249 -4.0; 274 -3.7; 302 -4.0; 332 -4.3; 365 -4.3; 402 -3.8; 442 -3.3; 486 -3.0; 535 -2.0; 588 -0.4; 647 1.3; 712 2.5; 783 2.6; 861 1.3; 947 0.1; 1042 0.2; 1146 0.9; 1261 1.8; 1387 2.1; 1526 2.9; 1678 4.0; 1846 5.5; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.8; 5267 4.6; 5793 5.3; 6373 1.9; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.36 | 6.6 dB  |
| Peaking | 151 Hz  | 0.61 | -3.9 dB |
| Peaking | 366 Hz  | 2.04 | -3.1 dB |
| Peaking | 2357 Hz | 0.93 | 5.7 dB  |
| Peaking | 4524 Hz | 1.65 | 3.9 dB  |
| Peaking | 509 Hz  | 4.02 | -1.6 dB |
| Peaking | 749 Hz  | 2.55 | 3.7 dB  |
| Peaking | 977 Hz  | 2.49 | -2.2 dB |
| Peaking | 8661 Hz | 3.09 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1/Aiaiai%20TMA-1.png)