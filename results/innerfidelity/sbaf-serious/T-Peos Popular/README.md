# T-Peos Popular

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -8.4; 23 -8.4; 25 -8.3; 28 -8.2; 31 -8.1; 34 -7.9; 37 -7.8; 41 -7.6; 45 -7.4; 49 -7.3; 54 -7.1; 60 -7.0; 66 -6.8; 72 -6.7; 79 -6.6; 87 -6.5; 96 -6.4; 106 -6.1; 116 -5.8; 128 -5.6; 141 -5.3; 155 -5.0; 170 -4.5; 187 -4.1; 206 -3.7; 227 -3.2; 249 -2.7; 274 -2.2; 302 -1.7; 332 -1.2; 365 -0.7; 402 -0.3; 442 0.3; 486 0.5; 535 0.9; 588 1.4; 647 1.5; 712 1.4; 783 1.5; 861 1.1; 947 0.5; 1042 -0.6; 1146 -0.0; 1261 -1.4; 1387 -2.7; 1526 -4.2; 1678 -5.5; 1846 -6.5; 2031 -7.1; 2234 -6.8; 2457 -4.4; 2703 -1.1; 2973 2.4; 3270 4.6; 3597 5.4; 3957 4.0; 4353 0.5; 4788 -3.1; 5267 -6.3; 5793 -3.5; 6373 0.7; 7010 2.2; 7711 0.3; 8482 -0.7; 9330 -2.8; 10263 -2.4; 11289 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Popular ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.3  | -8.2 dB |
| Peaking | 134 Hz  | 0.99 | -3.1 dB |
| Peaking | 2064 Hz | 2.1  | -8.8 dB |
| Peaking | 3463 Hz | 2.38 | 7.7 dB  |
| Peaking | 5200 Hz | 5.15 | -7.9 dB |
| Peaking | 245 Hz  | 2.04 | -0.9 dB |
| Peaking | 686 Hz  | 1.23 | 2.2 dB  |
| Peaking | 1548 Hz | 4.38 | -1.6 dB |
| Peaking | 6841 Hz | 7.13 | 3.2 dB  |
| Peaking | 9609 Hz | 4.85 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Popular/T-Peos%20Popular.png)