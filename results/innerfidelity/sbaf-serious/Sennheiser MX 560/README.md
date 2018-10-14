# Sennheiser MX 560

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.9; 96 5.0; 106 4.4; 116 3.9; 128 3.5; 141 3.2; 155 3.0; 170 2.7; 187 2.7; 206 2.5; 227 2.5; 249 2.2; 274 2.3; 302 2.3; 332 2.5; 365 1.3; 402 1.6; 442 1.7; 486 2.1; 535 2.0; 588 2.0; 647 1.6; 712 1.2; 783 1.2; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.4; 1387 -2.7; 1526 -4.4; 1678 -6.2; 1846 -8.3; 2031 -10.1; 2234 -11.7; 2457 -12.1; 2703 -12.3; 2973 -10.6; 3270 -8.1; 3597 -6.4; 3957 -6.3; 4353 -8.2; 4788 -9.4; 5267 -10.1; 5793 -10.6; 6373 -8.9; 7010 -7.3; 7711 -7.6; 8482 -7.0; 9330 -2.8; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 -2.0; 15026 -3.6; 16529 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.3  | 6.4 dB   |
| Peaking | 734 Hz   | 0.55 | 2.3 dB   |
| Peaking | 2358 Hz  | 1.34 | -12.4 dB |
| Peaking | 5926 Hz  | 1.44 | -9.1 dB  |
| Peaking | 14606 Hz | 6.79 | -3.9 dB  |
| Peaking | 2905 Hz  | 4.9  | -2.3 dB  |
| Peaking | 3946 Hz  | 1.66 | 2.7 dB   |
| Peaking | 4583 Hz  | 3.4  | -3.1 dB  |
| Peaking | 8422 Hz  | 4.33 | -5.3 dB  |
| Peaking | 9816 Hz  | 1.81 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)