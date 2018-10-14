# Radius HP-TWF41

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.1; 28 2.5; 31 2.1; 34 1.7; 37 1.4; 41 1.0; 45 0.6; 49 0.3; 54 -0.1; 60 -0.5; 66 -1.0; 72 -1.4; 79 -1.9; 87 -2.3; 96 -2.9; 106 -3.2; 116 -3.5; 128 -3.8; 141 -4.2; 155 -4.4; 170 -4.6; 187 -4.8; 206 -4.8; 227 -4.8; 249 -4.8; 274 -4.7; 302 -4.6; 332 -4.5; 365 -4.4; 402 -4.1; 442 -3.7; 486 -3.5; 535 -3.1; 588 -2.4; 647 -2.0; 712 -1.2; 783 -0.6; 861 -0.3; 947 -0.0; 1042 0.1; 1146 0.3; 1261 0.3; 1387 0.2; 1526 0.1; 1678 0.2; 1846 0.6; 2031 1.0; 2234 1.4; 2457 2.1; 2703 2.4; 2973 3.9; 3270 5.1; 3597 5.4; 3957 4.5; 4353 3.0; 4788 3.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -2.0; 10263 -1.4; 11289 -0.7; 12418 0.0; 13660 0.0; 15026 -0.8; 16529 -3.1; 18182 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF41 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.64 | 4.6 dB  |
| Peaking | 216 Hz   | 0.48 | -5.2 dB |
| Peaking | 3367 Hz  | 1.83 | 4.7 dB  |
| Peaking | 5961 Hz  | 2.22 | 7.0 dB  |
| Peaking | 8671 Hz  | 1.12 | -2.7 dB |
| Peaking | 508 Hz   | 2.06 | -0.9 dB |
| Peaking | 921 Hz   | 1.37 | 1.1 dB  |
| Peaking | 4235 Hz  | 0.24 | -0.1 dB |
| Peaking | 13764 Hz | 1.82 | 1.2 dB  |
| Peaking | 16298 Hz | 3.59 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF41/Radius%20HP-TWF41.png)