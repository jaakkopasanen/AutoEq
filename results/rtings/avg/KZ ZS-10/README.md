# KZ ZS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.2; 28 0.9; 31 0.7; 34 0.6; 37 0.4; 41 0.2; 45 0.0; 49 -0.1; 54 -0.4; 60 -0.9; 66 -1.4; 72 -1.8; 79 -2.3; 87 -2.8; 96 -3.4; 106 -4.0; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.8; 170 -5.9; 187 -6.1; 206 -6.0; 227 -5.9; 249 -5.6; 274 -5.2; 302 -4.8; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.8; 486 -2.2; 535 -1.5; 588 -0.9; 647 -0.2; 712 0.4; 783 0.8; 861 0.9; 947 0.6; 1042 -0.5; 1146 -1.5; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.4; 1846 -5.5; 2031 -6.7; 2234 -7.2; 2457 -6.6; 2703 -5.8; 2973 -5.6; 3270 -6.7; 3597 -7.9; 3957 -8.1; 4353 -4.7; 4788 -0.0; 5267 -2.0; 5793 -6.6; 6373 -3.4; 7010 1.9; 7711 0.3; 8482 -0.4; 9330 -3.8; 10263 -5.8; 11289 -5.2; 12418 -4.9; 13660 -5.9; 15026 -5.5; 16529 -2.7; 18182 -2.5; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 188 Hz   | 0.74 | -6.5 dB  |
| Peaking | 2174 Hz  | 1.78 | -6.7 dB  |
| Peaking | 3718 Hz  | 3.2  | -7.0 dB  |
| Peaking | 13027 Hz | 1.12 | -5.9 dB  |
| Peaking | 20088 Hz | 2.51 | -6.9 dB  |
| Peaking | 21 Hz    | 1.03 | 1.8 dB   |
| Peaking | 818 Hz   | 3.4  | 2.3 dB   |
| Peaking | 5966 Hz  | 6.13 | -10.2 dB |
| Peaking | 6730 Hz  | 1.85 | 5.3 dB   |
| Peaking | 10016 Hz | 4.73 | -3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20ZS-10/KZ%20ZS-10.png)