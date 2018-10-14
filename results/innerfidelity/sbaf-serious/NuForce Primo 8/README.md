# NuForce Primo 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.4; 28 5.2; 31 5.0; 34 4.9; 37 4.7; 41 4.5; 45 4.4; 49 4.2; 54 3.8; 60 3.5; 66 3.2; 72 2.9; 79 2.5; 87 2.1; 96 1.6; 106 1.3; 116 1.1; 128 0.7; 141 0.4; 155 0.2; 170 -0.0; 187 -0.2; 206 -0.3; 227 -0.3; 249 -0.4; 274 -0.2; 302 -0.2; 332 -0.1; 365 -0.0; 402 0.1; 442 0.3; 486 0.4; 535 0.5; 588 0.9; 647 1.0; 712 0.9; 783 1.1; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -3.0; 1678 -3.8; 1846 -4.1; 2031 -3.5; 2234 -1.7; 2457 1.5; 2703 4.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.6; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.76 | 5.3 dB  |
| Peaking | 58 Hz   | 1.21 | 2.2 dB  |
| Peaking | 740 Hz  | 2.15 | 1.2 dB  |
| Peaking | 1889 Hz | 1.63 | -8.2 dB |
| Peaking | 3437 Hz | 0.86 | 8.4 dB  |
| Peaking | 222 Hz  | 1.98 | -0.6 dB |
| Peaking | 2858 Hz | 5.8  | 2.2 dB  |
| Peaking | 3553 Hz | 1.56 | -1.2 dB |
| Peaking | 5752 Hz | 2.37 | 4.2 dB  |
| Peaking | 7506 Hz | 1.24 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20Primo%208/NuForce%20Primo%208.png)