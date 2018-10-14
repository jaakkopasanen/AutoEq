# Sennheiser HD 449

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.7; 28 1.9; 31 1.2; 34 0.6; 37 -0.0; 41 -0.6; 45 -1.2; 49 -1.6; 54 -2.1; 60 -2.6; 66 -2.8; 72 -2.8; 79 -2.6; 87 -2.6; 96 -1.8; 106 0.1; 116 -0.7; 128 -3.3; 141 -4.0; 155 -2.8; 170 -2.1; 187 -3.7; 206 -3.1; 227 -3.3; 249 -3.0; 274 -1.6; 302 -0.4; 332 0.3; 365 0.8; 402 1.2; 442 1.8; 486 1.5; 535 1.7; 588 1.3; 647 0.6; 712 0.4; 783 0.2; 861 0.3; 947 -0.1; 1042 0.1; 1146 0.1; 1261 -0.7; 1387 -1.7; 1526 -2.3; 1678 -2.1; 1846 -1.6; 2031 -0.4; 2234 1.4; 2457 2.7; 2703 3.0; 2973 3.7; 3270 3.6; 3597 4.1; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 1.74 | -1.8 dB |
| Peaking | 20 Hz   | 1.38 | 4.7 dB  |
| Peaking | 65 Hz   | 1.36 | -3.0 dB |
| Peaking | 186 Hz  | 1.76 | -3.5 dB |
| Peaking | 4685 Hz | 1.41 | 6.9 dB  |
| Peaking | 247 Hz  | 5.33 | -1.8 dB |
| Peaking | 459 Hz  | 1.45 | 2.0 dB  |
| Peaking | 1688 Hz | 2.07 | -3.5 dB |
| Peaking | 2523 Hz | 2.22 | 2.2 dB  |
| Peaking | 8525 Hz | 3.9  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)