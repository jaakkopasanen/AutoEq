# Koss SP330

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -3.8; 23 -3.9; 25 -4.0; 28 -4.1; 31 -4.3; 34 -4.4; 37 -4.4; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.4; 60 -4.2; 66 -4.1; 72 -4.2; 79 -4.5; 87 -4.7; 96 -4.8; 106 -4.7; 116 -4.6; 128 -4.5; 141 -4.1; 155 -3.8; 170 -3.4; 187 -2.5; 206 -2.1; 227 -1.8; 249 -1.0; 274 -0.2; 302 0.3; 332 -0.2; 365 -1.0; 402 -1.6; 442 -1.9; 486 -2.1; 535 -2.1; 588 -1.7; 647 -1.5; 712 -1.2; 783 -0.2; 861 -0.6; 947 -0.2; 1042 0.2; 1146 0.7; 1261 1.0; 1387 1.1; 1526 0.9; 1678 0.8; 1846 0.9; 2031 1.3; 2234 1.1; 2457 1.2; 2703 0.9; 2973 0.6; 3270 0.9; 3597 0.4; 3957 -0.3; 4353 -2.1; 4788 -1.8; 5267 1.2; 5793 3.7; 6373 5.1; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -1.1; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -0.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP330 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.43 | -4.2 dB |
| Peaking | 120 Hz  | 1.14 | -3.3 dB |
| Peaking | 520 Hz  | 2.83 | -2.2 dB |
| Peaking | 4581 Hz | 6.68 | -3.3 dB |
| Peaking | 6225 Hz | 4.29 | 5.6 dB  |
| Peaking | 299 Hz  | 3.05 | 2.8 dB  |
| Peaking | 305 Hz  | 1.39 | -1.5 dB |
| Peaking | 814 Hz  | 1.87 | -0.7 dB |
| Peaking | 1688 Hz | 0.74 | 1.3 dB  |
| Peaking | 9138 Hz | 3.82 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP330/Koss%20SP330.png)