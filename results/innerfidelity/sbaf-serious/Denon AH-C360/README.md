# Denon AH-C360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -7.7; 23 -7.8; 25 -7.9; 28 -8.0; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.5; 45 -8.6; 49 -8.7; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.8; 87 -10.0; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.4; 227 -8.9; 249 -8.5; 274 -7.9; 302 -7.3; 332 -6.7; 365 -6.0; 402 -5.3; 442 -4.5; 486 -4.0; 535 -3.2; 588 -2.3; 647 -1.6; 712 -1.1; 783 -0.4; 861 -0.1; 947 0.0; 1042 0.1; 1146 0.0; 1261 0.0; 1387 -0.6; 1526 -1.3; 1678 -1.1; 1846 0.5; 2031 0.9; 2234 0.4; 2457 0.7; 2703 0.4; 2973 0.2; 3270 -0.1; 3597 -1.2; 3957 -2.9; 4353 -5.7; 4788 -7.5; 5267 -8.0; 5793 -7.5; 6373 -5.0; 7010 -3.3; 7711 -3.8; 8482 -4.6; 9330 -2.4; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.2dB` and instead set Global volume in the UI for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.25 | -7.8 dB |
| Peaking | 150 Hz   | 0.7  | -5.7 dB |
| Peaking | 314 Hz   | 1.24 | -3.3 dB |
| Peaking | 5418 Hz  | 2.02 | -8.6 dB |
| Peaking | 24000 Hz | 2.32 | -2.4 dB |
| Peaking | 898 Hz   | 3.58 | 1.0 dB  |
| Peaking | 2871 Hz  | 1.58 | 1.6 dB  |
| Peaking | 4436 Hz  | 5.15 | -2.2 dB |
| Peaking | 8580 Hz  | 3.64 | -5.6 dB |
| Peaking | 8596 Hz  | 1.24 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)