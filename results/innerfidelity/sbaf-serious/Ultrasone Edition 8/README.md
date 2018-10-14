# Ultrasone Edition 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.6; 49 5.0; 54 4.6; 60 4.4; 66 4.1; 72 3.6; 79 3.2; 87 3.2; 96 3.1; 106 2.6; 116 2.2; 128 1.7; 141 1.3; 155 1.3; 170 1.2; 187 0.1; 206 -0.5; 227 -0.4; 249 -0.1; 274 0.4; 302 -0.1; 332 0.0; 365 0.2; 402 0.3; 442 0.5; 486 0.4; 535 0.6; 588 1.1; 647 1.3; 712 1.2; 783 1.3; 861 0.9; 947 0.2; 1042 0.4; 1146 1.0; 1261 1.5; 1387 2.1; 1526 2.5; 1678 3.1; 1846 4.8; 2031 6.0; 2234 6.0; 2457 2.9; 2703 1.4; 2973 3.1; 3270 4.7; 3597 2.9; 3957 2.5; 4353 5.8; 4788 6.0; 5267 6.0; 5793 0.2; 6373 -4.4; 7010 -1.6; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.9; 15026 -4.3; 16529 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.42 | 6.2 dB   |
| Peaking | 2011 Hz  | 2.1  | 5.8 dB   |
| Peaking | 5330 Hz  | 1.06 | 20.0 dB  |
| Peaking | 6302 Hz  | 1.25 | -28.0 dB |
| Peaking | 7141 Hz  | 1.09 | 8.1 dB   |
| Peaking | 216 Hz   | 3.95 | -1.3 dB  |
| Peaking | 719 Hz   | 1.91 | 1.2 dB   |
| Peaking | 970 Hz   | 5.82 | -0.9 dB  |
| Peaking | 12698 Hz | 2.55 | 1.9 dB   |
| Peaking | 14475 Hz | 4.91 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%208/Ultrasone%20Edition%208.png)