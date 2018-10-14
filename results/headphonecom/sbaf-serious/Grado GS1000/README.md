# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.6; 37 4.7; 41 3.8; 45 2.8; 49 1.3; 54 -0.5; 60 -2.0; 66 -3.4; 72 -4.6; 79 -5.8; 87 -6.8; 96 -7.5; 106 -7.7; 116 -7.6; 128 -7.2; 141 -6.7; 155 -6.2; 170 -5.4; 187 -4.7; 206 -4.0; 227 -3.3; 249 -2.6; 274 -2.4; 302 -2.4; 332 -1.9; 365 -1.5; 402 -1.1; 442 -0.9; 486 -0.8; 535 -0.6; 588 -0.3; 647 0.1; 712 0.3; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.2; 1387 -0.6; 1526 -1.3; 1678 -0.5; 1846 -1.3; 2031 -1.3; 2234 -1.3; 2457 -1.1; 2703 -1.2; 2973 -1.3; 3270 -0.8; 3597 -3.5; 3957 -5.2; 4353 -3.2; 4788 -5.7; 5267 -7.0; 5793 -7.8; 6373 -10.0; 7010 -10.2; 7711 -9.5; 8482 -8.1; 9330 -7.1; 10263 -4.7; 11289 -1.2; 12418 -0.2; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.61 | 8.5 dB   |
| Peaking | 98 Hz    | 0.65 | -9.9 dB  |
| Peaking | 794 Hz   | 1.16 | 0.8 dB   |
| Peaking | 1690 Hz  | 1.68 | -0.7 dB  |
| Peaking | 6892 Hz  | 1.27 | -10.7 dB |
| Peaking | 3399 Hz  | 5.29 | 1.9 dB   |
| Peaking | 3775 Hz  | 9.43 | -4.0 dB  |
| Peaking | 9655 Hz  | 2.99 | -3.7 dB  |
| Peaking | 11425 Hz | 1.35 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)