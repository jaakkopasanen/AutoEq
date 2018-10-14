# Sennheiser HD 438

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.4; 45 4.9; 49 4.6; 54 4.7; 60 4.5; 66 3.6; 72 3.2; 79 4.8; 87 5.9; 96 4.2; 106 3.3; 116 2.9; 128 2.6; 141 2.4; 155 2.7; 170 2.6; 187 3.5; 206 3.8; 227 4.3; 249 4.6; 274 4.3; 302 4.8; 332 4.6; 365 3.9; 402 3.5; 442 3.5; 486 3.0; 535 2.5; 588 2.1; 647 2.2; 712 2.2; 783 1.8; 861 0.9; 947 0.0; 1042 0.4; 1146 0.8; 1261 0.4; 1387 -0.2; 1526 1.0; 1678 2.0; 1846 3.1; 2031 4.5; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 438 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.45 | 6.1 dB  |
| Peaking | 88 Hz   | 4.73 | 3.3 dB  |
| Peaking | 274 Hz  | 1.09 | 4.2 dB  |
| Peaking | 471 Hz  | 1.84 | 1.3 dB  |
| Peaking | 3671 Hz | 0.83 | 6.9 dB  |
| Peaking | 1394 Hz | 3.09 | -2.0 dB |
| Peaking | 2300 Hz | 2.54 | 2.0 dB  |
| Peaking | 3584 Hz | 2.28 | -1.3 dB |
| Peaking | 6177 Hz | 2.4  | 4.9 dB  |
| Peaking | 7592 Hz | 1.54 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20438/Sennheiser%20HD%20438.png)