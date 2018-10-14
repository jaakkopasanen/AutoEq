# Grado SR325

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.7; 49 4.8; 54 3.7; 60 2.6; 66 1.8; 72 1.1; 79 0.5; 87 -0.0; 96 -0.4; 106 -0.6; 116 -0.6; 128 -0.6; 141 -0.6; 155 -0.7; 170 -0.6; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.3; 274 -0.2; 302 -0.1; 332 0.1; 365 0.3; 402 0.4; 442 0.5; 486 0.4; 535 0.5; 588 0.5; 647 0.6; 712 0.6; 783 0.5; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.9; 1526 -3.1; 1678 -4.1; 1846 -5.9; 2031 -8.3; 2234 -7.5; 2457 -6.0; 2703 -4.4; 2973 -2.9; 3270 -1.3; 3597 -0.6; 3957 -3.6; 4353 -11.9; 4788 -11.0; 5267 -6.4; 5793 -4.1; 6373 -5.2; 7010 -6.3; 7711 -7.1; 8482 -9.8; 9330 -12.4; 10263 -11.2; 11289 -8.3; 12418 -4.2; 13660 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.18 | 10.3 dB  |
| Peaking | 115 Hz   | 0.42 | -10.3 dB |
| Peaking | 2083 Hz  | 2.53 | -8.4 dB  |
| Peaking | 4585 Hz  | 5.72 | -12.4 dB |
| Peaking | 9453 Hz  | 1.88 | -12.8 dB |
| Peaking | 2652 Hz  | 5.94 | -1.1 dB  |
| Peaking | 3698 Hz  | 4.3  | 4.7 dB   |
| Peaking | 4127 Hz  | 3.33 | -2.8 dB  |
| Peaking | 11697 Hz | 3.27 | -3.6 dB  |
| Peaking | 13408 Hz | 2.01 | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR325/Grado%20SR325.png)