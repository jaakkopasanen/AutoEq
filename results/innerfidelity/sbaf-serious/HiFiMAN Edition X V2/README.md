# HiFiMAN Edition X V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.9; 28 3.5; 31 3.3; 34 3.2; 37 3.1; 41 3.1; 45 3.2; 49 3.2; 54 2.9; 60 1.9; 66 1.4; 72 1.1; 79 1.0; 87 0.8; 96 0.4; 106 0.3; 116 0.0; 128 -0.2; 141 -0.3; 155 -0.6; 170 -0.8; 187 -0.8; 206 -1.1; 227 -1.2; 249 -1.5; 274 -1.8; 302 -1.5; 332 -0.3; 365 0.2; 402 -0.2; 442 -0.6; 486 -1.7; 535 -2.7; 588 0.6; 647 -1.8; 712 1.6; 783 0.7; 861 1.7; 947 -0.1; 1042 3.4; 1146 3.6; 1261 3.1; 1387 5.1; 1526 4.5; 1678 4.9; 1846 4.7; 2031 3.5; 2234 2.5; 2457 1.6; 2703 0.7; 2973 1.1; 3270 1.1; 3597 1.5; 3957 1.7; 4353 0.4; 4788 1.1; 5267 2.6; 5793 4.2; 6373 0.2; 7010 0.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.7; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.8  | 5.0 dB  |
| Peaking | 47 Hz   | 1.11 | 2.3 dB  |
| Peaking | 362 Hz  | 0.38 | -1.4 dB |
| Peaking | 1513 Hz | 1.22 | 5.5 dB  |
| Peaking | 5652 Hz | 6.92 | 4.3 dB  |
| Peaking | 393 Hz  | 3.14 | 3.9 dB  |
| Peaking | 426 Hz  | 1.52 | -2.6 dB |
| Peaking | 727 Hz  | 9.69 | 1.9 dB  |
| Peaking | 2724 Hz | 6.16 | -0.9 dB |
| Peaking | 3767 Hz | 7.25 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X%20V2/HiFiMAN%20Edition%20X%20V2.png)