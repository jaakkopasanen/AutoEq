# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -0.9; 28 -1.0; 31 -1.0; 34 -1.1; 37 -1.2; 41 -1.3; 45 -1.3; 49 -1.4; 54 -1.5; 60 -1.7; 66 -1.8; 72 -2.0; 79 -2.2; 87 -2.3; 96 -2.5; 106 -2.6; 116 -2.7; 128 -2.7; 141 -2.6; 155 -2.4; 170 -2.2; 187 -2.0; 206 -1.8; 227 -1.5; 249 -1.3; 274 -0.9; 302 -0.6; 332 -0.3; 365 -0.1; 402 0.1; 442 0.4; 486 0.6; 535 0.7; 588 0.8; 647 1.0; 712 1.0; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.2; 1261 -2.0; 1387 -2.7; 1526 -3.2; 1678 -3.5; 1846 -3.5; 2031 -3.2; 2234 -2.0; 2457 0.1; 2703 2.2; 2973 4.0; 3270 5.3; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.3; 6373 3.8; 7010 1.9; 7711 -1.2; 8482 -6.1; 9330 -9.9; 10263 -10.6; 11289 -7.6; 12418 -1.7; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -4.3; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.4  | -0.9 dB  |
| Peaking | 135 Hz   | 0.76 | -2.4 dB  |
| Peaking | 1874 Hz  | 0.92 | -13.9 dB |
| Peaking | 3349 Hz  | 0.35 | 12.4 dB  |
| Peaking | 9785 Hz  | 1.82 | -16.9 dB |
| Peaking | 716 Hz   | 2.46 | 0.7 dB   |
| Peaking | 1779 Hz  | 9.36 | 0.8 dB   |
| Peaking | 5913 Hz  | 5.88 | 0.7 dB   |
| Peaking | 16131 Hz | 1.14 | 4.0 dB   |
| Peaking | 20061 Hz | 1.04 | -12.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20KSE1500/Shure%20KSE1500.png)