# AKG K267 Tiesto Club Setting

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.4; 28 1.5; 31 1.6; 34 1.6; 37 1.8; 41 1.9; 45 2.1; 49 2.4; 54 2.6; 60 2.7; 66 2.9; 72 3.0; 79 3.0; 87 2.2; 96 1.1; 106 1.0; 116 0.4; 128 -0.3; 141 -0.4; 155 -0.1; 170 0.3; 187 -0.1; 206 -0.1; 227 0.2; 249 0.5; 274 1.3; 302 2.5; 332 3.5; 365 3.1; 402 2.0; 442 1.2; 486 0.7; 535 0.6; 588 0.8; 647 0.7; 712 0.5; 783 0.7; 861 0.5; 947 0.2; 1042 -0.3; 1146 -0.8; 1261 -1.9; 1387 -3.5; 1526 -3.4; 1678 -2.3; 1846 -0.9; 2031 -0.1; 2234 0.6; 2457 2.1; 2703 2.1; 2973 2.8; 3270 3.1; 3597 4.0; 3957 5.8; 4353 6.0; 4788 6.0; 5267 3.9; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -1.6; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Club Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 1.2  | 3.1 dB  |
| Peaking | 345 Hz  | 3.08 | 3.6 dB  |
| Peaking | 1474 Hz | 3.61 | -4.4 dB |
| Peaking | 4196 Hz | 1.73 | 6.0 dB  |
| Peaking | 6115 Hz | 5.38 | 4.4 dB  |
| Peaking | 26 Hz   | 0.58 | 1.4 dB  |
| Peaking | 75 Hz   | 0.7  | -2.2 dB |
| Peaking | 80 Hz   | 2.13 | 2.7 dB  |
| Peaking | 718 Hz  | 1.85 | 0.7 dB  |
| Peaking | 9039 Hz | 5.25 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Club%20Setting/AKG%20K267%20Tiesto%20Club%20Setting.png)