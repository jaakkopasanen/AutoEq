# AKG K501

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.5; 66 4.7; 72 4.6; 79 4.4; 87 3.6; 96 2.5; 106 2.0; 116 1.7; 128 1.3; 141 1.1; 155 0.8; 170 0.9; 187 0.7; 206 0.7; 227 0.6; 249 0.5; 274 0.5; 302 0.7; 332 0.8; 365 0.8; 402 0.8; 442 0.9; 486 0.8; 535 0.9; 588 1.1; 647 1.1; 712 1.3; 783 2.0; 861 0.9; 947 0.3; 1042 -0.3; 1146 -0.8; 1261 -1.5; 1387 -2.2; 1526 -2.6; 1678 -3.1; 1846 -2.9; 2031 -1.7; 2234 -2.1; 2457 -1.4; 2703 -1.5; 2973 -1.7; 3270 -2.2; 3597 -2.2; 3957 -1.4; 4353 -1.1; 4788 -0.2; 5267 1.4; 5793 -0.2; 6373 -4.6; 7010 -1.4; 7711 -1.6; 8482 -3.8; 9330 -2.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.51 | 6.6 dB  |
| Peaking | 747 Hz   | 1.3  | 1.9 dB  |
| Peaking | 1627 Hz  | 1.35 | -3.2 dB |
| Peaking | 3453 Hz  | 3.22 | -1.8 dB |
| Peaking | 8496 Hz  | 3.57 | -3.7 dB |
| Peaking | 78 Hz    | 2.93 | 1.1 dB  |
| Peaking | 114 Hz   | 1.36 | -0.7 dB |
| Peaking | 5455 Hz  | 6.23 | 2.9 dB  |
| Peaking | 6231 Hz  | 9.25 | -5.1 dB |
| Peaking | 10297 Hz | 5.48 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K501/AKG%20K501.png)