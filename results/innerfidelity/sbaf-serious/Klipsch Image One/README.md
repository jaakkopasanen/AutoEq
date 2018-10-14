# Klipsch Image One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.1; 49 4.5; 54 3.8; 60 3.2; 66 2.7; 72 2.1; 79 1.3; 87 0.5; 96 -0.3; 106 -0.8; 116 -1.2; 128 -1.7; 141 -2.0; 155 -2.2; 170 -2.2; 187 -2.4; 206 -2.3; 227 -2.0; 249 -1.7; 274 -1.6; 302 -1.5; 332 -1.3; 365 -1.0; 402 -0.9; 442 -0.6; 486 -0.4; 535 0.1; 588 1.1; 647 1.8; 712 1.4; 783 1.5; 861 0.7; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.5; 1387 -2.0; 1526 -2.4; 1678 -3.0; 1846 -3.5; 2031 -3.8; 2234 -4.1; 2457 -4.3; 2703 -5.0; 2973 -5.0; 3270 -4.0; 3597 -1.7; 3957 1.0; 4353 2.6; 4788 3.0; 5267 3.6; 5793 1.5; 6373 -1.0; 7010 -2.7; 7711 -0.4; 8482 -0.4; 9330 -1.5; 10263 -0.1; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.53 | 6.5 dB  |
| Peaking | 153 Hz  | 0.88 | -3.2 dB |
| Peaking | 2821 Hz | 1.16 | -6.5 dB |
| Peaking | 4722 Hz | 1.72 | 6.3 dB  |
| Peaking | 6862 Hz | 4.51 | -3.9 dB |
| Peaking | 458 Hz  | 1.01 | -1.1 dB |
| Peaking | 680 Hz  | 1.61 | 2.9 dB  |
| Peaking | 1507 Hz | 2.5  | -1.0 dB |
| Peaking | 7998 Hz | 5.93 | 0.8 dB  |
| Peaking | 9258 Hz | 6.41 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)