# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.5; 23 -6.0; 25 -6.3; 28 -6.4; 31 -6.5; 34 -6.7; 37 -6.7; 41 -6.8; 45 -6.9; 49 -7.0; 54 -7.3; 60 -7.4; 66 -7.7; 72 -7.7; 79 -8.0; 87 -7.8; 96 -7.6; 106 -7.8; 116 -7.5; 128 -7.6; 141 -7.2; 155 -7.0; 170 -6.9; 187 -6.7; 206 -6.4; 227 -6.1; 249 -5.8; 274 -5.3; 302 -4.8; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.9; 486 -2.4; 535 -1.9; 588 -1.4; 647 -1.0; 712 -0.5; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.2; 1387 -1.3; 1526 -0.9; 1678 -0.3; 1846 0.2; 2031 0.1; 2234 -0.5; 2457 -1.0; 2703 -0.6; 2973 -0.1; 3270 -0.2; 3597 -0.3; 3957 4.1; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -2.8; 8482 -4.9; 9330 -4.6; 10263 -5.9; 11289 -7.5; 12418 -11.0; 13660 -19.8; 15026 -27.0; 16529 -25.4; 18182 -20.3; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.6  | -4.0 dB  |
| Peaking | 98 Hz    | 0.41 | -6.9 dB  |
| Peaking | 263 Hz   | 1.01 | -1.9 dB  |
| Peaking | 5934 Hz  | 1.11 | 12.7 dB  |
| Peaking | 16178 Hz | 0.7  | -28.7 dB |
| Peaking | 3796 Hz  | 1.86 | -4.9 dB  |
| Peaking | 4205 Hz  | 3.76 | 6.9 dB   |
| Peaking | 8099 Hz  | 5.46 | -4.0 dB  |
| Peaking | 11860 Hz | 1.5  | 5.1 dB   |
| Peaking | 14318 Hz | 3.7  | -6.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS6/KZ%20ZS6.png)