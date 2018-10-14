# Sennheiser HD 205

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.6; 28 5.2; 31 4.8; 34 4.3; 37 3.9; 41 3.6; 45 3.5; 49 3.1; 54 2.3; 60 1.9; 66 1.9; 72 1.9; 79 1.0; 87 0.4; 96 -0.1; 106 -0.4; 116 -0.6; 128 -0.8; 141 -0.2; 155 0.7; 170 -0.0; 187 -0.1; 206 0.4; 227 1.0; 249 0.6; 274 0.8; 302 1.2; 332 1.8; 365 2.9; 402 4.0; 442 4.1; 486 2.5; 535 0.8; 588 0.6; 647 2.2; 712 4.4; 783 3.7; 861 1.9; 947 0.5; 1042 -0.4; 1146 -0.9; 1261 -1.3; 1387 -1.7; 1526 -2.2; 1678 -2.3; 1846 -1.8; 2031 -1.2; 2234 -0.2; 2457 1.2; 2703 3.1; 2973 3.5; 3270 4.2; 3597 5.9; 3957 6.0; 4353 6.0; 4788 3.1; 5267 0.3; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.81 | 5.9 dB  |
| Peaking | 412 Hz   | 3.34 | 4.4 dB  |
| Peaking | 734 Hz   | 5.78 | 4.6 dB  |
| Peaking | 4011 Hz  | 1.85 | 6.4 dB  |
| Peaking | 24000 Hz | 2.5  | 2.6 dB  |
| Peaking | 116 Hz   | 3.61 | -1.3 dB |
| Peaking | 1672 Hz  | 1.8  | -3.1 dB |
| Peaking | 2798 Hz  | 3.95 | 1.7 dB  |
| Peaking | 5152 Hz  | 8.92 | -4.7 dB |
| Peaking | 6129 Hz  | 5.2  | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205/Sennheiser%20HD%20205.png)