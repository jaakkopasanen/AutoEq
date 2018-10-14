# Sennheiser CX 300-II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.3; 23 -2.6; 25 -2.9; 28 -3.2; 31 -3.5; 34 -3.7; 37 -4.0; 41 -4.3; 45 -4.5; 49 -4.8; 54 -5.1; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.2; 116 -7.5; 128 -7.5; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.7; 206 -7.5; 227 -7.3; 249 -7.0; 274 -6.6; 302 -6.2; 332 -5.7; 365 -5.0; 402 -4.5; 442 -3.9; 486 -3.3; 535 -2.7; 588 -2.1; 647 -1.4; 712 -0.8; 783 -0.3; 861 -0.1; 947 -0.1; 1042 0.0; 1146 0.0; 1261 -0.1; 1387 -0.0; 1526 0.0; 1678 0.1; 1846 0.4; 2031 0.9; 2234 1.6; 2457 2.5; 2703 3.6; 2973 4.7; 3270 5.8; 3597 5.9; 3957 4.3; 4353 1.7; 4788 -0.2; 5267 -1.5; 5793 -4.8; 6373 -6.0; 7010 -1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 300-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.38 | -4.5 dB |
| Peaking | 168 Hz  | 0.75 | -4.3 dB |
| Peaking | 325 Hz  | 1.16 | -2.8 dB |
| Peaking | 3358 Hz | 2.04 | 6.5 dB  |
| Peaking | 6058 Hz | 4.55 | -7.6 dB |
| Peaking | 511 Hz  | 3.77 | -0.5 dB |
| Peaking | 830 Hz  | 2.63 | 0.7 dB  |
| Peaking | 4773 Hz | 9.63 | -1.1 dB |
| Peaking | 7643 Hz | 9.14 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20300-II/Sennheiser%20CX%20300-II.png)