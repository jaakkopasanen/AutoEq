# AKG N90Q Nominal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -0.2; 23 -0.1; 25 -0.0; 28 0.1; 31 0.3; 34 0.5; 37 0.8; 41 1.0; 45 1.2; 49 1.4; 54 1.6; 60 1.7; 66 1.6; 72 1.3; 79 0.9; 87 0.6; 96 0.2; 106 -0.0; 116 -0.1; 128 -0.4; 141 -0.7; 155 -0.7; 170 -0.7; 187 -0.7; 206 -0.7; 227 -0.6; 249 -0.6; 274 -0.5; 302 -0.5; 332 -0.4; 365 -0.4; 402 -0.6; 442 -0.6; 486 -0.9; 535 -1.0; 588 -0.6; 647 0.1; 712 -0.9; 783 -0.8; 861 -0.5; 947 -0.1; 1042 0.0; 1146 0.3; 1261 0.5; 1387 0.2; 1526 -0.4; 1678 -0.3; 1846 -0.9; 2031 -1.1; 2234 -2.4; 2457 -3.4; 2703 -3.5; 2973 -3.6; 3270 -4.5; 3597 -4.6; 3957 -5.1; 4353 -5.0; 4788 -2.5; 5267 0.3; 5793 0.2; 6373 3.2; 7010 2.5; 7711 0.3; 8482 -3.3; 9330 -5.7; 10263 -3.9; 11289 -0.5; 12418 0.0; 13660 -1.0; 15026 -3.1; 16529 -0.9; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N90Q Nominal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 2.15 | 1.9 dB  |
| Peaking | 3793 Hz  | 1.22 | -5.8 dB |
| Peaking | 6617 Hz  | 2.08 | 5.8 dB  |
| Peaking | 7946 Hz  | 2.4  | -0.4 dB |
| Peaking | 9279 Hz  | 3.21 | -6.6 dB |
| Peaking | 394 Hz   | 0.38 | -0.7 dB |
| Peaking | 1306 Hz  | 1.72 | 1.2 dB  |
| Peaking | 2463 Hz  | 7.7  | -1.2 dB |
| Peaking | 12176 Hz | 3.81 | 1.4 dB  |
| Peaking | 15035 Hz | 3.65 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N90Q%20Nominal/AKG%20N90Q%20Nominal.png)