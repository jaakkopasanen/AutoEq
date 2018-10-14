# Audeze LCD-2 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.6; 28 5.5; 31 5.4; 34 5.3; 37 5.2; 41 5.1; 45 5.0; 49 4.8; 54 4.6; 60 4.4; 66 4.1; 72 3.8; 79 3.4; 87 3.0; 96 2.6; 106 2.5; 116 2.3; 128 2.0; 141 1.8; 155 1.6; 170 1.4; 187 1.3; 206 1.1; 227 1.1; 249 1.0; 274 0.9; 302 0.8; 332 0.7; 365 0.6; 402 0.5; 442 0.8; 486 0.7; 535 0.8; 588 1.0; 647 0.4; 712 -0.2; 783 -0.4; 861 -0.5; 947 0.3; 1042 0.2; 1146 0.6; 1261 0.4; 1387 0.1; 1526 -0.5; 1678 -0.9; 1846 0.3; 2031 1.4; 2234 1.1; 2457 3.2; 2703 3.5; 2973 5.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.4; 6373 3.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.33 | 4.7 dB  |
| Peaking | 513 Hz  | 3.41 | 0.6 dB  |
| Peaking | 1654 Hz | 4.08 | -2.1 dB |
| Peaking | 4022 Hz | 1.12 | 6.8 dB  |
| Peaking | 16 Hz   | 0.73 | 1.7 dB  |
| Peaking | 818 Hz  | 5.56 | -1.0 dB |
| Peaking | 4201 Hz | 3.37 | -2.3 dB |
| Peaking | 5169 Hz | 1.21 | 2.2 dB  |
| Peaking | 8338 Hz | 1.6  | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)