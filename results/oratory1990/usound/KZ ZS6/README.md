# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.0; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.5; 49 -6.7; 54 -6.9; 60 -7.1; 66 -7.4; 72 -7.3; 79 -7.7; 87 -7.5; 96 -7.2; 106 -7.5; 116 -7.1; 128 -7.3; 141 -6.9; 155 -6.7; 170 -6.5; 187 -6.3; 206 -6.1; 227 -5.8; 249 -5.4; 274 -5.0; 302 -4.6; 332 -4.2; 365 -3.7; 402 -3.3; 442 -2.9; 486 -2.4; 535 -2.0; 588 -1.6; 647 -1.1; 712 -0.7; 783 -0.3; 861 0.0; 947 0.1; 1042 -0.2; 1146 -0.9; 1261 -1.6; 1387 -2.0; 1526 -1.8; 1678 -1.3; 1846 -0.8; 2031 -1.3; 2234 -2.4; 2457 -3.5; 2703 -3.6; 2973 -3.2; 3270 -3.3; 3597 -3.1; 3957 1.7; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.2; 7711 -6.6; 8482 -7.5; 9330 -4.5; 10263 -4.5; 11289 -6.9; 12418 -9.3; 13660 -11.7; 15026 -11.5; 16529 -7.4; 18182 -4.6; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.54 | -3.5 dB  |
| Peaking | 113 Hz   | 0.33 | -6.9 dB  |
| Peaking | 5712 Hz  | 2.34 | 9.4 dB   |
| Peaking | 8028 Hz  | 5.98 | -7.5 dB  |
| Peaking | 14348 Hz | 0.86 | -11.7 dB |
| Peaking | 879 Hz   | 1.81 | 1.4 dB   |
| Peaking | 1357 Hz  | 3.62 | -1.5 dB  |
| Peaking | 3258 Hz  | 1.54 | -5.1 dB  |
| Peaking | 4352 Hz  | 4.55 | 6.9 dB   |
| Peaking | 19748 Hz | 5.47 | -5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS6/KZ%20ZS6.png)