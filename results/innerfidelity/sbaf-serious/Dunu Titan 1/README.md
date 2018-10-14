# Dunu Titan 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -1.6; 23 -1.8; 25 -1.9; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.6; 72 -3.9; 79 -4.3; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.6; 141 -5.8; 155 -5.9; 170 -5.9; 187 -5.8; 206 -5.7; 227 -5.5; 249 -5.3; 274 -5.0; 302 -4.7; 332 -4.4; 365 -3.4; 402 -3.1; 442 -2.9; 486 -2.4; 535 -1.8; 588 -0.9; 647 -0.6; 712 -0.3; 783 0.1; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -1.6; 1526 -2.7; 1678 -3.9; 1846 -4.7; 2031 -4.7; 2234 -4.3; 2457 -3.4; 2703 -2.5; 2973 -1.5; 3270 -0.6; 3597 -0.7; 3957 -1.7; 4353 -3.8; 4788 -4.5; 5267 -3.6; 5793 -2.9; 6373 -1.8; 7010 -1.1; 7711 -0.4; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -0.6; 13660 -1.9; 15026 -2.5; 16529 -0.2; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.3dB` and instead set Global volume in the UI for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.46 | -4.2 dB |
| Peaking | 237 Hz   | 0.91 | -3.3 dB |
| Peaking | 1992 Hz  | 2.35 | -5.1 dB |
| Peaking | 4935 Hz  | 2.8  | -4.4 dB |
| Peaking | 14688 Hz | 3.56 | -2.8 dB |
| Peaking | 25 Hz    | 1.88 | -0.8 dB |
| Peaking | 818 Hz   | 0.64 | -1.7 dB |
| Peaking | 867 Hz   | 1.08 | 2.9 dB  |
| Peaking | 1584 Hz  | 6.8  | -0.7 dB |
| Peaking | 3467 Hz  | 7.5  | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%201/Dunu%20Titan%201.png)