# Echobox Finder X1 Red Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -10.3; 23 -10.3; 25 -10.3; 28 -10.2; 31 -10.1; 34 -10.0; 37 -9.9; 41 -9.7; 45 -9.6; 49 -9.4; 54 -9.3; 60 -9.1; 66 -8.9; 72 -8.9; 79 -8.8; 87 -8.7; 96 -8.6; 106 -8.3; 116 -7.9; 128 -7.7; 141 -7.4; 155 -7.1; 170 -6.7; 187 -6.2; 206 -5.7; 227 -5.2; 249 -4.7; 274 -4.1; 302 -3.6; 332 -3.0; 365 -2.5; 402 -2.0; 442 -1.3; 486 -1.0; 535 -0.6; 588 0.1; 647 0.5; 712 0.5; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -2.3; 1678 -2.9; 1846 -3.1; 2031 -3.1; 2234 -3.3; 2457 -3.3; 2703 -3.8; 2973 -4.7; 3270 -5.8; 3597 -6.4; 3957 -6.5; 4353 -7.7; 4788 -8.2; 5267 -8.6; 5793 -10.3; 6373 -12.0; 7010 -9.3; 7711 -6.3; 8482 -4.3; 9330 -4.5; 10263 -7.2; 11289 -7.6; 12418 -3.4; 13660 -2.5; 15026 -4.8; 16529 -1.6; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Red Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.47 | -8.8 dB |
| Peaking | 110 Hz   | 0.4  | -6.7 dB |
| Peaking | 700 Hz   | 1.5  | 2.2 dB  |
| Peaking | 5618 Hz  | 0.69 | -9.5 dB |
| Peaking | 11065 Hz | 5.44 | -4.7 dB |
| Peaking | 1702 Hz  | 3.66 | -1.3 dB |
| Peaking | 5249 Hz  | 2.1  | 1.4 dB  |
| Peaking | 6371 Hz  | 4.56 | -3.8 dB |
| Peaking | 8420 Hz  | 4.35 | 2.7 dB  |
| Peaking | 15180 Hz | 5.19 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Red%20Filter/Echobox%20Finder%20X1%20Red%20Filter.png)