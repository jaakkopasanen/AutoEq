# Ocharaku Flat4 Kuro Type II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.9; 28 0.6; 31 0.4; 34 0.2; 37 0.1; 41 -0.1; 45 -0.3; 49 -0.5; 54 -0.6; 60 -0.8; 66 -1.1; 72 -1.3; 79 -1.6; 87 -1.8; 96 -2.1; 106 -2.2; 116 -2.2; 128 -2.2; 141 -2.2; 155 -2.2; 170 -2.1; 187 -1.9; 206 -1.7; 227 -1.3; 249 -1.1; 274 -0.7; 302 -0.4; 332 -0.1; 365 0.3; 402 0.6; 442 1.0; 486 1.1; 535 1.3; 588 1.7; 647 1.7; 712 1.5; 783 1.5; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.5; 1387 -0.3; 1526 0.9; 1678 2.6; 1846 5.2; 2031 6.0; 2234 6.0; 2457 5.7; 2703 3.9; 2973 1.4; 3270 -0.4; 3597 0.5; 3957 0.9; 4353 -1.3; 4788 -4.8; 5267 -4.7; 5793 5.9; 6373 5.5; 7010 -2.3; 7711 -7.9; 8482 -7.6; 9330 -6.4; 10263 -2.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat4 Kuro Type II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 125 Hz   |  1.03 | -2.5 dB  |
| Peaking | 2177 Hz  |  2.51 | 6.9 dB   |
| Peaking | 5061 Hz  |  5.5  | -11.3 dB |
| Peaking | 6026 Hz  |  3.06 | 12.5 dB  |
| Peaking | 7992 Hz  |  2.46 | -11.5 dB |
| Peaking | 20 Hz    |  1.7  | 1.5 dB   |
| Peaking | 635 Hz   |  1.52 | 1.9 dB   |
| Peaking | 1228 Hz  |  3.01 | -1.8 dB  |
| Peaking | 11099 Hz | 10.75 | 1.7 dB   |
| Peaking | 12582 Hz |  4.54 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ocharaku%20Flat4%20Kuro%20Type%20II/Ocharaku%20Flat4%20Kuro%20Type%20II.png)