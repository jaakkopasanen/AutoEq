# Phiaton Bridge M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 4.7; 72 4.3; 79 4.5; 87 4.3; 96 3.6; 106 2.9; 116 2.6; 128 2.7; 141 2.7; 155 3.1; 170 3.4; 187 3.9; 206 4.5; 227 5.2; 249 5.7; 274 6.0; 302 5.7; 332 5.4; 365 4.9; 402 4.1; 442 3.4; 486 2.8; 535 2.2; 588 1.8; 647 1.4; 712 1.0; 783 0.7; 861 0.5; 947 0.1; 1042 0.0; 1146 0.3; 1261 0.3; 1387 0.7; 1526 1.4; 1678 0.9; 1846 0.1; 2031 1.9; 2234 4.2; 2457 5.9; 2703 6.0; 2973 5.2; 3270 2.9; 3597 2.5; 3957 3.4; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.29 | 6.2 dB  |
| Peaking | 120 Hz  | 1.87 | -1.5 dB |
| Peaking | 293 Hz  | 1.11 | 5.3 dB  |
| Peaking | 2606 Hz | 3.16 | 5.9 dB  |
| Peaking | 5216 Hz | 2    | 6.6 dB  |
| Peaking | 1008 Hz | 3.26 | -0.7 dB |
| Peaking | 5371 Hz | 5.4  | -2.4 dB |
| Peaking | 6458 Hz | 1.94 | 3.5 dB  |
| Peaking | 7457 Hz | 4.53 | -2.2 dB |
| Peaking | 8401 Hz | 1.46 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)