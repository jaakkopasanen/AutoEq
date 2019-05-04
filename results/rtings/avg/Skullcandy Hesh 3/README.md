# Skullcandy Hesh 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.2; 25 -12.8; 28 -12.2; 31 -11.5; 34 -10.9; 37 -10.2; 41 -9.4; 45 -8.6; 49 -7.9; 54 -7.2; 60 -6.7; 66 -6.6; 72 -6.9; 79 -7.5; 87 -8.4; 96 -9.4; 106 -9.9; 116 -10.1; 128 -9.9; 141 -9.5; 155 -8.7; 170 -7.9; 187 -7.0; 206 -5.8; 227 -4.6; 249 -3.5; 274 -2.6; 302 -1.9; 332 -1.3; 365 -0.8; 402 -0.5; 442 -0.5; 486 -0.8; 535 -1.0; 588 -1.3; 647 -1.7; 712 -2.1; 783 -2.4; 861 -2.4; 947 -2.4; 1042 -2.4; 1146 -2.2; 1261 -1.7; 1387 -1.2; 1526 -1.0; 1678 -1.2; 1846 -2.0; 2031 -3.1; 2234 -4.2; 2457 -4.9; 2703 -5.2; 2973 -5.7; 3270 -6.0; 3597 -5.9; 3957 -4.7; 4353 -5.2; 4788 -6.7; 5267 -7.5; 5793 -9.9; 6373 -10.6; 7010 -12.2; 7711 -12.4; 8482 -11.4; 9330 -8.5; 10263 -6.5; 11289 -6.3; 12418 -5.6; 13660 -7.3; 15026 -10.4; 16529 -8.0; 18182 -5.6; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.01 | -8.6 dB |
| Peaking | 130 Hz   | 1.14 | -5.9 dB |
| Peaking | 411 Hz   | 0.75 | 4.9 dB  |
| Peaking | 1523 Hz  | 2    | 3.7 dB  |
| Peaking | 7407 Hz  | 1.55 | -7.8 dB |
| Peaking | 65 Hz    | 3.99 | 1.1 dB  |
| Peaking | 3395 Hz  | 2.75 | -1.3 dB |
| Peaking | 4147 Hz  | 3.15 | 2.2 dB  |
| Peaking | 10715 Hz | 1.72 | 3.1 dB  |
| Peaking | 20882 Hz | 0.07 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Hesh%203/Skullcandy%20Hesh%203.png)