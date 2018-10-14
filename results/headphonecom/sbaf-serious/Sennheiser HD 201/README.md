# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 5.3; 861 3.3; 947 1.2; 1042 -0.6; 1146 -1.2; 1261 -1.5; 1387 -1.2; 1526 -1.0; 1678 3.7; 1846 1.3; 2031 1.2; 2234 1.3; 2457 1.4; 2703 2.7; 2973 4.2; 3270 4.7; 3597 4.1; 3957 4.3; 4353 6.0; 4788 6.0; 5267 -1.2; 5793 4.0; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -0.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 90 Hz   |  0.05 | 6.1 dB  |
| Peaking | 730 Hz  |  1.63 | 2.8 dB  |
| Peaking | 1144 Hz |  1.63 | -6.6 dB |
| Peaking | 3134 Hz |  4.81 | 2.5 dB  |
| Peaking | 4405 Hz |  2.29 | 4.9 dB  |
| Peaking | 1554 Hz |  5.53 | -2.9 dB |
| Peaking | 1646 Hz |  9.53 | 5.2 dB  |
| Peaking | 5249 Hz | 12.01 | -7.5 dB |
| Peaking | 5864 Hz |  1.7  | 6.1 dB  |
| Peaking | 6217 Hz |  0.83 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)