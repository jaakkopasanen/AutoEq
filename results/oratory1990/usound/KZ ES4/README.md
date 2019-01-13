# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.6; 23 -9.1; 25 -9.3; 28 -9.2; 31 -9.1; 34 -9.1; 37 -9.0; 41 -9.0; 45 -8.8; 49 -8.8; 54 -8.9; 60 -9.0; 66 -9.1; 72 -8.9; 79 -9.2; 87 -8.9; 96 -8.5; 106 -8.5; 116 -8.1; 128 -8.1; 141 -7.6; 155 -7.2; 170 -6.9; 187 -6.6; 206 -6.2; 227 -5.8; 249 -5.3; 274 -4.8; 302 -4.3; 332 -3.9; 365 -3.4; 402 -2.9; 442 -2.5; 486 -2.0; 535 -1.6; 588 -1.2; 647 -0.8; 712 -0.5; 783 -0.0; 861 0.2; 947 0.2; 1042 -0.3; 1146 -1.1; 1261 -2.1; 1387 -3.0; 1526 -3.7; 1678 -4.3; 1846 -5.1; 2031 -6.2; 2234 -7.3; 2457 -7.2; 2703 -5.9; 2973 -4.7; 3270 -4.7; 3597 -5.8; 3957 -4.7; 4353 1.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.2; 8482 -1.5; 9330 0.0; 10263 0.0; 11289 -0.8; 12418 -2.9; 13660 -3.5; 15026 -0.7; 16529 -0.7; 18182 -6.5; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.19 | -9.4 dB  |
| Peaking | 2288 Hz  | 1.65 | -7.6 dB  |
| Peaking | 3789 Hz  | 3.67 | -7.5 dB  |
| Peaking | 5117 Hz  | 2.06 | 9.2 dB   |
| Peaking | 20162 Hz | 1.03 | -11.1 dB |
| Peaking | 851 Hz   | 2.84 | 1.8 dB   |
| Peaking | 6429 Hz  | 7.9  | 2.4 dB   |
| Peaking | 8108 Hz  | 6.46 | -2.8 dB  |
| Peaking | 13239 Hz | 3.83 | -3.3 dB  |
| Peaking | 16038 Hz | 3.58 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ES4/KZ%20ES4.png)