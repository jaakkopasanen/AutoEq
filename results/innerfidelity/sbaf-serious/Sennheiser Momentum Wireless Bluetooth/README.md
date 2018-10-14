# Sennheiser Momentum Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 2.9; 28 2.4; 31 2.5; 34 2.8; 37 3.2; 41 3.5; 45 3.8; 49 4.1; 54 4.3; 60 4.5; 66 4.6; 72 4.7; 79 4.8; 87 4.8; 96 4.8; 106 4.9; 116 5.1; 128 5.0; 141 5.3; 155 5.3; 170 5.6; 187 5.9; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.9; 535 5.1; 588 4.4; 647 3.5; 712 2.5; 783 1.9; 861 1.1; 947 0.5; 1042 -0.2; 1146 -0.8; 1261 -1.7; 1387 -2.9; 1526 -4.3; 1678 -5.4; 1846 -5.8; 2031 -5.4; 2234 -3.9; 2457 -1.2; 2703 1.0; 2973 3.7; 3270 5.7; 3597 6.0; 3957 6.0; 4353 6.0; 4788 1.6; 5267 2.6; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 98 Hz   |  0.22 | 4.5 dB  |
| Peaking | 415 Hz  |  0.72 | 3.8 dB  |
| Peaking | 1891 Hz |  1.28 | -8.0 dB |
| Peaking | 3488 Hz |  1.67 | 8.4 dB  |
| Peaking | 6119 Hz |  5.42 | 5.4 dB  |
| Peaking | 35 Hz   |  3.09 | -0.4 dB |
| Peaking | 866 Hz  |  4.72 | -0.4 dB |
| Peaking | 4673 Hz |  5.67 | 3.5 dB  |
| Peaking | 4895 Hz | 12.26 | -6.6 dB |
| Peaking | 8381 Hz |  4.26 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Bluetooth/Sennheiser%20Momentum%20Wireless%20Bluetooth.png)