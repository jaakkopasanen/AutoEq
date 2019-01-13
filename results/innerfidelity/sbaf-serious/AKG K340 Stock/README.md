# AKG K340 Stock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.3; 72 3.4; 79 2.4; 87 1.3; 96 0.3; 106 -0.4; 116 -1.0; 128 -1.7; 141 -2.2; 155 -2.6; 170 -2.7; 187 -3.1; 206 -3.3; 227 -3.4; 249 -3.5; 274 -3.4; 302 -3.3; 332 -3.1; 365 -2.7; 402 -2.5; 442 -1.8; 486 -1.2; 535 0.1; 588 1.0; 647 1.3; 712 1.5; 783 2.3; 861 1.3; 947 0.4; 1042 -0.2; 1146 2.8; 1261 5.3; 1387 1.5; 1526 -1.0; 1678 -1.4; 1846 -1.2; 2031 -0.9; 2234 -4.0; 2457 -4.8; 2703 -2.9; 2973 -0.1; 3270 1.5; 3597 2.4; 3957 1.6; 4353 3.0; 4788 2.2; 5267 2.7; 5793 1.3; 6373 -0.4; 7010 2.2; 7711 -0.9; 8482 -6.8; 9330 -7.9; 10263 -3.5; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K340 Stock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K340 Stock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 47 Hz   | 0.4  | 9.0 dB   |
| Peaking | 162 Hz  | 0.36 | -6.7 dB  |
| Peaking | 2215 Hz | 0.28 | 5.1 dB   |
| Peaking | 2308 Hz | 1.59 | -9.0 dB  |
| Peaking | 9046 Hz | 3.61 | -10.9 dB |
| Peaking | 701 Hz  | 2.54 | 1.3 dB   |
| Peaking | 1077 Hz | 3.97 | -4.3 dB  |
| Peaking | 1221 Hz | 6.06 | 7.2 dB   |
| Peaking | 1560 Hz | 2.63 | -2.6 dB  |
| Peaking | 1971 Hz | 8.86 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K340%20Stock/AKG%20K340%20Stock.png)