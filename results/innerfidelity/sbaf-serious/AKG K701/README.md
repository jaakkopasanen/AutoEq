# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.5; 34 5.0; 37 4.5; 41 4.0; 45 3.6; 49 3.2; 54 2.7; 60 2.4; 66 2.7; 72 2.6; 79 1.9; 87 1.6; 96 0.5; 106 -0.2; 116 -0.6; 128 -1.1; 141 -1.5; 155 -1.6; 170 -1.7; 187 -2.0; 206 -2.1; 227 -2.0; 249 -2.1; 274 -2.1; 302 -2.0; 332 -1.7; 365 -1.6; 402 -1.4; 442 -0.9; 486 -0.6; 535 -0.4; 588 0.2; 647 0.7; 712 1.3; 783 1.7; 861 1.0; 947 0.4; 1042 -0.1; 1146 -0.2; 1261 0.0; 1387 -0.2; 1526 -0.4; 1678 -1.2; 1846 -2.0; 2031 -2.8; 2234 -2.6; 2457 -2.3; 2703 -1.5; 2973 0.2; 3270 1.8; 3597 1.3; 3957 0.3; 4353 -1.3; 4788 -1.5; 5267 -1.2; 5793 -3.2; 6373 -4.4; 7010 -2.7; 7711 -2.8; 8482 -3.2; 9330 -2.5; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.5; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.68 | 6.2 dB  |
| Peaking | 72 Hz    | 2.78 | 1.5 dB  |
| Peaking | 202 Hz   | 0.9  | -2.5 dB |
| Peaking | 2115 Hz  | 3.93 | -3.1 dB |
| Peaking | 6947 Hz  | 1.81 | -3.8 dB |
| Peaking | 762 Hz   | 3.79 | 2.1 dB  |
| Peaking | 2602 Hz  | 4.89 | -1.3 dB |
| Peaking | 3355 Hz  | 4.13 | 2.8 dB  |
| Peaking | 14875 Hz | 0.64 | 3.1 dB  |
| Peaking | 18603 Hz | 0.25 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701/AKG%20K701.png)