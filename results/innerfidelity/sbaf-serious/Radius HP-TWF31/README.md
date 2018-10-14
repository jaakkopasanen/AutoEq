# Radius HP-TWF31

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -0.9; 31 -1.1; 34 -1.2; 37 -1.4; 41 -1.5; 45 -1.7; 49 -1.9; 54 -2.1; 60 -2.4; 66 -2.7; 72 -3.0; 79 -3.4; 87 -3.8; 96 -4.3; 106 -4.6; 116 -4.8; 128 -5.1; 141 -5.3; 155 -5.6; 170 -5.6; 187 -5.7; 206 -5.7; 227 -5.6; 249 -5.5; 274 -5.4; 302 -5.2; 332 -4.9; 365 -4.4; 402 -4.3; 442 -3.8; 486 -3.4; 535 -2.7; 588 -1.9; 647 -1.5; 712 -1.2; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.2; 1387 0.1; 1526 -0.2; 1678 -0.1; 1846 0.2; 2031 0.6; 2234 1.1; 2457 1.9; 2703 2.7; 2973 3.9; 3270 4.5; 3597 4.2; 3957 2.8; 4353 0.9; 4788 1.9; 5267 5.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.2; 10263 -3.0; 11289 -0.6; 12418 -0.2; 13660 -1.0; 15026 -2.2; 16529 -4.2; 18182 -3.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 148 Hz   | 0.53 | -5.0 dB |
| Peaking | 338 Hz   | 1.11 | -2.5 dB |
| Peaking | 3190 Hz  | 2.42 | 4.7 dB  |
| Peaking | 5944 Hz  | 3.09 | 7.1 dB  |
| Peaking | 16183 Hz | 0.36 | -2.5 dB |
| Peaking | 987 Hz   | 2.78 | 0.8 dB  |
| Peaking | 8871 Hz  | 6.84 | 1.6 dB  |
| Peaking | 9859 Hz  | 3.39 | -4.0 dB |
| Peaking | 11904 Hz | 1.74 | 2.7 dB  |
| Peaking | 16896 Hz | 3.38 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF31/Radius%20HP-TWF31.png)