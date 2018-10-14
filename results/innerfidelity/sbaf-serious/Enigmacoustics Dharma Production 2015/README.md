# Enigmacoustics Dharma Production 2015

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.3; 28 4.4; 31 3.7; 34 3.0; 37 2.5; 41 2.0; 45 1.5; 49 1.1; 54 0.6; 60 0.1; 66 -0.4; 72 -0.7; 79 -0.9; 87 -1.3; 96 -1.7; 106 -2.0; 116 -2.1; 128 -2.2; 141 -2.1; 155 -1.8; 170 -1.2; 187 -0.8; 206 -0.3; 227 -0.2; 249 -0.3; 274 -0.1; 302 0.4; 332 1.0; 365 1.6; 402 1.8; 442 2.0; 486 2.0; 535 1.9; 588 2.0; 647 1.6; 712 1.3; 783 1.2; 861 0.5; 947 0.0; 1042 0.4; 1146 -0.3; 1261 -0.4; 1387 -0.9; 1526 -1.2; 1678 -2.0; 1846 -2.5; 2031 -1.5; 2234 -0.3; 2457 0.5; 2703 1.6; 2973 3.5; 3270 4.9; 3597 5.2; 3957 4.9; 4353 2.0; 4788 -1.1; 5267 -3.1; 5793 -6.7; 6373 -2.6; 7010 0.6; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -3.5; 15026 -3.2; 16529 -2.5; 18182 -1.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmacoustics Dharma Production 2015 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.72 | 6.2 dB  |
| Peaking | 1829 Hz  | 3.2  | -3.1 dB |
| Peaking | 3542 Hz  | 2.35 | 6.1 dB  |
| Peaking | 5758 Hz  | 5.17 | -7.7 dB |
| Peaking | 15153 Hz | 1.99 | -3.8 dB |
| Peaking | 42 Hz    | 2.12 | 1.0 dB  |
| Peaking | 122 Hz   | 1.09 | -2.5 dB |
| Peaking | 482 Hz   | 1.3  | 2.3 dB  |
| Peaking | 4858 Hz  | 9.48 | -1.6 dB |
| Peaking | 7195 Hz  | 6.38 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmacoustics%20Dharma%20Production%202015/Enigmacoustics%20Dharma%20Production%202015.png)