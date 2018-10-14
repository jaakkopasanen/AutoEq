# AudioFly AF140

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.3; 23 -3.6; 25 -3.8; 28 -4.1; 31 -4.3; 34 -4.5; 37 -4.7; 41 -5.0; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.6; 116 -7.7; 128 -7.9; 141 -8.0; 155 -8.0; 170 -7.9; 187 -7.7; 206 -7.5; 227 -7.1; 249 -6.8; 274 -6.3; 302 -5.8; 332 -5.3; 365 -4.6; 402 -4.0; 442 -3.1; 486 -2.9; 535 -2.1; 588 -1.1; 647 -0.4; 712 0.8; 783 1.5; 861 1.3; 947 0.8; 1042 -0.2; 1146 -1.0; 1261 -1.9; 1387 -3.0; 1526 -4.0; 1678 -4.8; 1846 -5.4; 2031 -5.3; 2234 -5.1; 2457 -4.0; 2703 -2.1; 2973 1.0; 3270 3.7; 3597 4.7; 3957 5.9; 4353 6.0; 4788 4.8; 5267 -0.4; 5793 0.9; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -2.7; 11289 -2.0; 12418 -0.0; 13660 -1.6; 15026 -4.1; 16529 -1.2; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 72 Hz    | 0.37 | -5.8 dB |
| Peaking | 209 Hz   | 0.84 | -4.8 dB |
| Peaking | 2114 Hz  | 1.73 | -7.0 dB |
| Peaking | 3737 Hz  | 1.87 | 6.3 dB  |
| Peaking | 4515 Hz  | 5.98 | 2.8 dB  |
| Peaking | 809 Hz   | 0.75 | -3.2 dB |
| Peaking | 813 Hz   | 1.58 | 6.0 dB  |
| Peaking | 6470 Hz  | 9.67 | 5.1 dB  |
| Peaking | 10583 Hz | 6.17 | -3.3 dB |
| Peaking | 15076 Hz | 3.86 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF140/AudioFly%20AF140.png)