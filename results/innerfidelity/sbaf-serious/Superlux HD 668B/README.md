# Superlux HD 668B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.3; 34 4.3; 37 3.1; 41 1.6; 45 0.4; 49 -0.8; 54 -2.1; 60 -3.2; 66 -3.9; 72 -3.9; 79 -4.1; 87 -4.7; 96 -5.7; 106 -5.5; 116 -4.8; 128 -4.9; 141 -4.9; 155 -4.4; 170 -3.9; 187 -3.7; 206 -3.4; 227 -2.7; 249 -2.9; 274 -2.7; 302 -2.5; 332 -2.2; 365 -1.6; 402 -1.4; 442 -0.9; 486 -0.8; 535 -0.8; 588 -0.2; 647 0.4; 712 0.1; 783 0.2; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -1.5; 1526 -2.9; 1678 -4.4; 1846 -5.7; 2031 -6.4; 2234 -6.3; 2457 -6.0; 2703 -5.0; 2973 -4.0; 3270 -3.0; 3597 -1.8; 3957 -1.3; 4353 -1.1; 4788 -0.5; 5267 -3.8; 5793 -10.3; 6373 -5.8; 7010 -5.4; 7711 -8.2; 8482 -11.5; 9330 -11.4; 10263 -7.7; 11289 -4.1; 12418 -2.3; 13660 -3.4; 15026 -6.0; 16529 -5.4; 18182 -2.3; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.87 | 8.2 dB   |
| Peaking | 90 Hz    | 0.49 | -6.3 dB  |
| Peaking | 2170 Hz  | 1.94 | -6.7 dB  |
| Peaking | 8609 Hz  | 1.56 | -11.1 dB |
| Peaking | 15999 Hz | 2.5  | -5.8 dB  |
| Peaking | 837 Hz   | 1.75 | 1.1 dB   |
| Peaking | 5066 Hz  | 4.73 | 6.4 dB   |
| Peaking | 5603 Hz  | 6.44 | -11.1 dB |
| Peaking | 7048 Hz  | 5.65 | 2.5 dB   |
| Peaking | 12159 Hz | 6.08 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)