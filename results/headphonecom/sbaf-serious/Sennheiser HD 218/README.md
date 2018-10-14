# Sennheiser HD 218

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.9; 72 5.3; 79 5.1; 87 4.5; 96 3.3; 106 2.2; 116 1.4; 128 0.5; 141 -0.4; 155 -1.0; 170 -0.6; 187 -0.9; 206 -1.9; 227 -2.5; 249 -3.1; 274 -3.6; 302 -3.8; 332 -4.3; 365 -5.0; 402 -3.8; 442 -2.6; 486 -2.2; 535 -2.2; 588 -0.5; 647 0.2; 712 0.4; 783 0.4; 861 0.3; 947 0.1; 1042 -0.0; 1146 0.0; 1261 0.4; 1387 1.0; 1526 1.4; 1678 0.5; 1846 0.5; 2031 1.1; 2234 2.2; 2457 3.3; 2703 3.8; 2973 3.7; 3270 4.3; 3597 5.4; 3957 6.0; 4353 2.3; 4788 -2.4; 5267 -1.9; 5793 -0.4; 6373 1.5; 7010 2.4; 7711 0.3; 8482 -0.4; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -3.2; 18182 -6.5; 20000 -7.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.48 | 6.8 dB  |
| Peaking | 300 Hz   | 1.06 | -4.9 dB |
| Peaking | 3267 Hz  | 1.78 | 5.3 dB  |
| Peaking | 14821 Hz | 1.3  | 4.4 dB  |
| Peaking | 18908 Hz | 0.64 | -8.3 dB |
| Peaking | 142 Hz   | 4.96 | -1.4 dB |
| Peaking | 724 Hz   | 3.18 | 1.3 dB  |
| Peaking | 4089 Hz  | 5.76 | 5.1 dB  |
| Peaking | 4854 Hz  | 3.15 | -5.1 dB |
| Peaking | 6781 Hz  | 6.99 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)