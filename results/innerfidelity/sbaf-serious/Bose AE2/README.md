# Bose AE2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.9; 23 -3.9; 25 -4.0; 28 -3.9; 31 -3.9; 34 -3.8; 37 -3.6; 41 -3.4; 45 -3.1; 49 -2.9; 54 -2.4; 60 -2.0; 66 -1.6; 72 -1.2; 79 -0.8; 87 -0.5; 96 -0.3; 106 0.1; 116 0.3; 128 -0.1; 141 -1.1; 155 -1.7; 170 0.4; 187 -0.8; 206 -0.5; 227 0.0; 249 1.4; 274 2.5; 302 2.4; 332 3.0; 365 3.7; 402 4.0; 442 4.2; 486 3.9; 535 3.6; 588 3.4; 647 2.7; 712 1.8; 783 1.0; 861 0.3; 947 0.0; 1042 0.4; 1146 1.0; 1261 1.8; 1387 2.3; 1526 2.6; 1678 3.0; 1846 3.3; 2031 3.6; 2234 4.4; 2457 3.8; 2703 2.8; 2973 1.3; 3270 1.0; 3597 1.2; 3957 0.9; 4353 1.0; 4788 3.9; 5267 6.0; 5793 4.6; 6373 2.1; 7010 -0.4; 7711 0.1; 8482 -0.6; 9330 -1.3; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.74 | -4.2 dB |
| Peaking | 194 Hz  | 2.52 | -1.4 dB |
| Peaking | 421 Hz  | 1.16 | 4.4 dB  |
| Peaking | 2110 Hz | 1.79 | 4.1 dB  |
| Peaking | 5336 Hz | 4.87 | 6.6 dB  |
| Peaking | 139 Hz  | 2.03 | 1.2 dB  |
| Peaking | 148 Hz  | 6.43 | -2.8 dB |
| Peaking | 933 Hz  | 4.45 | -1.4 dB |
| Peaking | 1385 Hz | 4.3  | 0.9 dB  |
| Peaking | 8968 Hz | 5.6  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20AE2/Bose%20AE2.png)