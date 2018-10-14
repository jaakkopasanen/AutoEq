# KRK Systems KNS 8400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.3; 28 2.0; 31 1.9; 34 1.9; 37 2.1; 41 2.4; 45 2.6; 49 2.5; 54 2.3; 60 2.5; 66 2.4; 72 1.6; 79 0.0; 87 -1.9; 96 -3.8; 106 -5.4; 116 -6.4; 128 -7.2; 141 -6.9; 155 -6.2; 170 -6.8; 187 -7.4; 206 -6.8; 227 -5.8; 249 -4.8; 274 -4.0; 302 -2.8; 332 -1.7; 365 -0.3; 402 1.1; 442 2.1; 486 1.8; 535 0.6; 588 -0.4; 647 -0.5; 712 0.5; 783 -0.1; 861 -0.5; 947 -0.3; 1042 0.1; 1146 -0.1; 1261 -0.5; 1387 -1.6; 1526 -2.8; 1678 -4.4; 1846 -5.5; 2031 -6.1; 2234 -6.7; 2457 -7.0; 2703 -7.2; 2973 -5.3; 3270 -5.1; 3597 -5.0; 3957 -4.5; 4353 -3.5; 4788 -0.8; 5267 0.1; 5793 0.6; 6373 -0.4; 7010 -0.1; 7711 0.3; 8482 -2.3; 9330 -5.4; 10263 -3.3; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -4.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.3dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.55 | 2.6 dB  |
| Peaking | 64 Hz   | 2.16 | 3.7 dB  |
| Peaking | 148 Hz  | 1    | -8.3 dB |
| Peaking | 2511 Hz | 1.39 | -7.6 dB |
| Peaking | 9478 Hz | 6.18 | -5.9 dB |
| Peaking | 239 Hz  | 2.72 | -1.8 dB |
| Peaking | 443 Hz  | 2.98 | 3.5 dB  |
| Peaking | 1112 Hz | 4.11 | 1.4 dB  |
| Peaking | 4139 Hz | 3.36 | -3.5 dB |
| Peaking | 5037 Hz | 1.98 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%208400/KRK%20Systems%20KNS%208400.png)