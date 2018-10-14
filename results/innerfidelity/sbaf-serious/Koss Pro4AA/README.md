# Koss Pro4AA

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.2; 28 -0.5; 31 -1.0; 34 -1.5; 37 -1.9; 41 -2.4; 45 -2.7; 49 -3.1; 54 -3.5; 60 -4.0; 66 -4.3; 72 -4.5; 79 -5.0; 87 -6.1; 96 -7.0; 106 -7.0; 116 -7.5; 128 -8.5; 141 -9.0; 155 -9.2; 170 -9.1; 187 -9.6; 206 -9.6; 227 -9.3; 249 -8.8; 274 -7.9; 302 -7.6; 332 -7.9; 365 -7.3; 402 -6.4; 442 -5.3; 486 -4.7; 535 -3.7; 588 -2.6; 647 -1.8; 712 -1.5; 783 -1.0; 861 -0.6; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.8; 1387 0.4; 1526 -0.2; 1678 -0.8; 1846 -1.5; 2031 -2.4; 2234 -3.8; 2457 -4.8; 2703 -5.1; 2973 -5.4; 3270 -3.1; 3597 -0.6; 3957 1.1; 4353 -0.8; 4788 3.1; 5267 5.8; 5793 2.0; 6373 -0.2; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  2.7  | 2.0 dB  |
| Peaking | 156 Hz  |  0.59 | -9.0 dB |
| Peaking | 343 Hz  |  1.52 | -3.4 dB |
| Peaking | 2710 Hz |  2.72 | -5.9 dB |
| Peaking | 5188 Hz |  5.62 | 6.5 dB  |
| Peaking | 493 Hz  |  6.05 | -0.7 dB |
| Peaking | 1180 Hz |  1.45 | 2.0 dB  |
| Peaking | 2645 Hz |  0.46 | -0.8 dB |
| Peaking | 3861 Hz |  7.61 | 2.2 dB  |
| Peaking | 6891 Hz | 10.93 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA/Koss%20Pro4AA.png)