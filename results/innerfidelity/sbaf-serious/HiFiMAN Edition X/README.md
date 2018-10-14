# HiFiMAN Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 5.0; 34 4.6; 37 4.3; 41 4.0; 45 3.9; 49 3.8; 54 3.6; 60 3.5; 66 3.4; 72 3.2; 79 2.9; 87 2.3; 96 1.9; 106 1.7; 116 1.7; 128 1.5; 141 1.4; 155 1.3; 170 1.2; 187 1.1; 206 1.1; 227 0.9; 249 0.7; 274 0.7; 302 0.5; 332 0.8; 365 1.5; 402 1.6; 442 1.3; 486 0.5; 535 0.1; 588 0.4; 647 0.2; 712 0.8; 783 2.8; 861 1.6; 947 0.5; 1042 1.7; 1146 3.3; 1261 3.5; 1387 2.5; 1526 2.8; 1678 2.1; 1846 2.0; 2031 2.4; 2234 1.9; 2457 2.2; 2703 1.9; 2973 1.5; 3270 2.1; 3597 2.7; 3957 2.1; 4353 0.1; 4788 1.0; 5267 3.8; 5793 4.3; 6373 2.0; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.21 | 5.6 dB  |
| Peaking | 52 Hz   | 0.05 | 0.6 dB  |
| Peaking | 1208 Hz | 5.13 | 2.6 dB  |
| Peaking | 2213 Hz | 0.7  | 2.0 dB  |
| Peaking | 5693 Hz | 4.82 | 4.2 dB  |
| Peaking | 402 Hz  | 5.51 | 1.2 dB  |
| Peaking | 763 Hz  | 1.82 | -1.6 dB |
| Peaking | 789 Hz  | 6.74 | 3.5 dB  |
| Peaking | 3674 Hz | 6.29 | 1.4 dB  |
| Peaking | 4487 Hz | 8.75 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X/HiFiMAN%20Edition%20X.png)