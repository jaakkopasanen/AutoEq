# Sennheiser HD 800 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.6; 28 3.2; 31 2.8; 34 2.5; 37 2.3; 41 2.4; 45 2.8; 49 2.8; 54 2.0; 60 1.6; 66 0.9; 72 0.1; 79 -0.4; 87 -0.9; 96 -1.1; 106 -1.4; 116 -1.7; 128 -2.0; 141 -2.4; 155 -2.6; 170 -2.5; 187 -2.8; 206 -2.8; 227 -2.8; 249 -2.8; 274 -2.6; 302 -2.4; 332 -2.2; 365 -2.0; 402 -1.9; 442 -1.8; 486 -1.5; 535 -1.3; 588 -1.1; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.4; 947 -0.1; 1042 0.1; 1146 0.9; 1261 1.5; 1387 2.0; 1526 1.6; 1678 1.4; 1846 1.8; 2031 1.8; 2234 2.2; 2457 3.2; 2703 3.1; 2973 2.9; 3270 2.4; 3597 1.8; 3957 -0.6; 4353 -1.4; 4788 -1.0; 5267 -2.6; 5793 -7.6; 6373 -5.4; 7010 -0.5; 7711 0.3; 8482 0.0; 9330 -1.9; 10263 -0.2; 11289 0.0; 12418 -0.2; 13660 -4.7; 15026 -5.0; 16529 -2.4; 18182 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.21 | 4.2 dB  |
| Peaking | 162 Hz   | 0.41 | -3.7 dB |
| Peaking | 2389 Hz  | 1.02 | 3.0 dB  |
| Peaking | 5936 Hz  | 5.46 | -9.2 dB |
| Peaking | 14603 Hz | 2.85 | -5.9 dB |
| Peaking | 1347 Hz  | 3.14 | 1.7 dB  |
| Peaking | 2214 Hz  | 0.84 | -1.6 dB |
| Peaking | 3059 Hz  | 1.44 | 2.2 dB  |
| Peaking | 4173 Hz  | 4.9  | -2.5 dB |
| Peaking | 7330 Hz  | 7.53 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%201/Sennheiser%20HD%20800%20sample%201.png)