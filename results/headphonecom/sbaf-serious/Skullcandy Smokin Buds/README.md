# Skullcandy Smokin Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.6; 28 3.8; 31 3.1; 34 2.6; 37 2.0; 41 1.4; 45 0.7; 49 0.2; 54 -0.4; 60 -1.1; 66 -1.7; 72 -2.3; 79 -2.8; 87 -3.2; 96 -3.8; 106 -4.0; 116 -4.2; 128 -4.5; 141 -4.8; 155 -5.1; 170 -5.0; 187 -5.1; 206 -5.0; 227 -4.8; 249 -4.6; 274 -4.3; 302 -3.9; 332 -3.4; 365 -2.9; 402 -2.6; 442 -2.4; 486 -2.1; 535 -1.7; 588 -1.5; 647 -1.0; 712 -0.9; 783 -0.7; 861 -0.8; 947 -0.6; 1042 0.7; 1146 3.1; 1261 1.7; 1387 0.0; 1526 -1.7; 1678 -4.1; 1846 -4.5; 2031 -4.5; 2234 -3.9; 2457 -2.3; 2703 -0.1; 2973 2.6; 3270 5.0; 3597 6.0; 3957 4.8; 4353 1.6; 4788 -1.0; 5267 -2.9; 5793 -2.5; 6373 -0.0; 7010 1.0; 7711 -1.0; 8482 -4.1; 9330 -1.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Smokin Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Smokin Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.82 | 6.2 dB  |
| Peaking | 162 Hz  | 0.53 | -5.4 dB |
| Peaking | 2043 Hz | 2.8  | -5.8 dB |
| Peaking | 3607 Hz | 2.55 | 7.6 dB  |
| Peaking | 5230 Hz | 2.84 | -4.2 dB |
| Peaking | 1022 Hz | 3.14 | -1.4 dB |
| Peaking | 1148 Hz | 3.97 | 4.8 dB  |
| Peaking | 1651 Hz | 7.74 | -2.3 dB |
| Peaking | 6891 Hz | 5.51 | 2.1 dB  |
| Peaking | 8517 Hz | 6.08 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Smokin%20Buds/Skullcandy%20Smokin%20Buds.png)