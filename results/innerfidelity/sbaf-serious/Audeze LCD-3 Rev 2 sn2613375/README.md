# Audeze LCD-3 Rev 2 sn2613375

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.3; 25 4.3; 28 3.9; 31 3.2; 34 2.7; 37 2.8; 41 3.0; 45 3.0; 49 2.7; 54 1.9; 60 1.6; 66 1.7; 72 1.6; 79 1.4; 87 1.0; 96 0.7; 106 0.7; 116 0.5; 128 0.1; 141 -0.1; 155 -0.3; 170 -0.5; 187 -0.7; 206 -0.8; 227 -0.8; 249 -0.9; 274 -0.8; 302 -0.9; 332 -0.9; 365 -0.7; 402 -0.6; 442 -0.6; 486 -1.0; 535 -1.3; 588 -0.8; 647 -0.7; 712 -0.6; 783 -0.3; 861 -0.3; 947 -0.2; 1042 0.4; 1146 0.4; 1261 -0.1; 1387 -0.8; 1526 -1.3; 1678 -1.1; 1846 -0.4; 2031 -0.5; 2234 -0.2; 2457 0.9; 2703 1.8; 2973 1.8; 3270 2.8; 3597 5.7; 3957 6.0; 4353 6.0; 4788 5.7; 5267 5.2; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -4.0; 18182 -5.7; 20000 -1.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Rev 2 sn2613375 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.36 | 4.0 dB  |
| Peaking | 48 Hz    | 1.37 | 2.0 dB  |
| Peaking | 4786 Hz  | 1.42 | 6.9 dB  |
| Peaking | 14774 Hz | 1.67 | 4.9 dB  |
| Peaking | 17140 Hz | 0.82 | -7.2 dB |
| Peaking | 351 Hz   | 0.72 | -1.0 dB |
| Peaking | 1678 Hz  | 2.57 | -1.6 dB |
| Peaking | 3707 Hz  | 6.16 | 2.6 dB  |
| Peaking | 6200 Hz  | 1.67 | -3.4 dB |
| Peaking | 6271 Hz  | 4.1  | 5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Rev%202%20sn2613375/Audeze%20LCD-3%20Rev%202%20sn2613375.png)