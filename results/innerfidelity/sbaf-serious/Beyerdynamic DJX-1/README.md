# Beyerdynamic DJX-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 5.1; 37 4.7; 41 4.2; 45 3.8; 49 3.4; 54 3.0; 60 2.7; 66 2.5; 72 2.4; 79 1.9; 87 2.0; 96 1.7; 106 1.3; 116 0.9; 128 0.5; 141 -0.1; 155 -0.4; 170 -0.3; 187 -0.8; 206 -1.1; 227 -1.2; 249 -1.3; 274 -1.2; 302 -1.0; 332 -0.6; 365 -0.2; 402 0.1; 442 0.1; 486 -0.3; 535 -1.0; 588 -1.1; 647 -1.4; 712 -1.6; 783 -1.3; 861 -1.1; 947 -0.4; 1042 -0.4; 1146 -0.7; 1261 -0.4; 1387 -0.4; 1526 -0.2; 1678 -0.3; 1846 0.1; 2031 0.7; 2234 1.0; 2457 1.3; 2703 2.0; 2973 2.5; 3270 2.8; 3597 3.5; 3957 5.8; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.2; 8482 -3.3; 9330 -3.1; 10263 -0.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DJX-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.55 | 6.3 dB  |
| Peaking | 91 Hz   | 1.75 | 1.4 dB  |
| Peaking | 484 Hz  | 0.1  | -1.1 dB |
| Peaking | 5247 Hz | 0.9  | 7.7 dB  |
| Peaking | 8708 Hz | 2.61 | -7.0 dB |
| Peaking | 248 Hz  | 2.34 | -0.7 dB |
| Peaking | 411 Hz  | 2.69 | 1.3 dB  |
| Peaking | 681 Hz  | 3.33 | -0.8 dB |
| Peaking | 5111 Hz | 4.82 | -1.7 dB |
| Peaking | 5186 Hz | 2.32 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DJX-1/Beyerdynamic%20DJX-1.png)