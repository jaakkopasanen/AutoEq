# Klipsch Image S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.7; 28 -6.9; 31 -7.0; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.2; 66 -7.2; 72 -7.2; 79 -7.2; 87 -7.1; 96 -7.1; 106 -6.8; 116 -6.6; 128 -6.5; 141 -6.2; 155 -6.0; 170 -5.6; 187 -5.2; 206 -4.8; 227 -4.3; 249 -3.8; 274 -3.3; 302 -2.7; 332 -2.1; 365 -1.5; 402 -0.9; 442 -0.5; 486 0.0; 535 0.5; 588 0.8; 647 1.2; 712 1.4; 783 1.3; 861 1.1; 947 0.4; 1042 -0.3; 1146 -1.3; 1261 -2.4; 1387 -3.1; 1526 -2.7; 1678 -3.0; 1846 -4.0; 2031 -5.0; 2234 -6.0; 2457 -6.3; 2703 -4.6; 2973 -1.1; 3270 2.4; 3597 4.3; 3957 3.4; 4353 0.7; 4788 -1.9; 5267 -5.5; 5793 -6.6; 6373 0.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.0; 15026 -2.5; 16529 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.34 | -7.1 dB |
| Peaking | 152 Hz   | 0.94 | -3.4 dB |
| Peaking | 2405 Hz  | 1.68 | -8.0 dB |
| Peaking | 3530 Hz  | 2.42 | 7.3 dB  |
| Peaking | 5486 Hz  | 6.84 | -8.7 dB |
| Peaking | 734 Hz   | 1.69 | 2.3 dB  |
| Peaking | 1332 Hz  | 3.96 | -2.0 dB |
| Peaking | 5870 Hz  | 8.86 | -2.3 dB |
| Peaking | 6716 Hz  | 6.61 | 4.3 dB  |
| Peaking | 14721 Hz | 5.18 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S2/Klipsch%20Image%20S2.png)