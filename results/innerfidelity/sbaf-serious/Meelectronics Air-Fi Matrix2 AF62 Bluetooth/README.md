# Meelectronics Air-Fi Matrix2 AF62 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.3; 31 4.0; 34 2.7; 37 1.7; 41 0.6; 45 -0.2; 49 -0.8; 54 -1.4; 60 -1.8; 66 -2.0; 72 -2.0; 79 -1.9; 87 -1.8; 96 -1.9; 106 -1.6; 116 -1.4; 128 -1.5; 141 -1.6; 155 -1.8; 170 -1.5; 187 -1.5; 206 -1.7; 227 -1.4; 249 -1.2; 274 -1.7; 302 -1.7; 332 -1.7; 365 -1.7; 402 -1.7; 442 -1.5; 486 -1.8; 535 -2.0; 588 -1.9; 647 -1.8; 712 -1.8; 783 -1.0; 861 -0.1; 947 -0.0; 1042 -0.1; 1146 -0.2; 1261 -0.1; 1387 -0.4; 1526 -0.4; 1678 0.1; 1846 1.4; 2031 2.2; 2234 2.7; 2457 2.9; 2703 3.3; 2973 2.7; 3270 2.0; 3597 2.6; 3957 4.1; 4353 4.9; 4788 6.0; 5267 3.6; 5793 2.2; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -0.7; 10263 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.5  | 8.4 dB  |
| Peaking | 100 Hz   | 0.11 | -2.0 dB |
| Peaking | 2405 Hz  | 2.17 | 2.9 dB  |
| Peaking | 4707 Hz  | 2.03 | 5.5 dB  |
| Peaking | 24000 Hz | 2.22 | 1.7 dB  |
| Peaking | 61 Hz    | 0.55 | 1.3 dB  |
| Peaking | 63 Hz    | 1.14 | -2.1 dB |
| Peaking | 1548 Hz  | 7.37 | -0.7 dB |
| Peaking | 6678 Hz  | 6.55 | 4.6 dB  |
| Peaking | 7156 Hz  | 1.53 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth.png)