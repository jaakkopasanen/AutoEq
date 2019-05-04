# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.7; 28 -5.9; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.8; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.6; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.0; 170 -10.0; 187 -9.9; 206 -9.8; 227 -9.6; 249 -9.4; 274 -9.3; 302 -9.1; 332 -8.7; 365 -8.3; 402 -7.8; 442 -7.3; 486 -6.8; 535 -6.2; 588 -5.5; 647 -4.8; 712 -4.1; 783 -3.5; 861 -3.2; 947 -3.3; 1042 -4.1; 1146 -5.2; 1261 -5.6; 1387 -6.0; 1526 -6.4; 1678 -6.9; 1846 -7.6; 2031 -8.2; 2234 -7.9; 2457 -6.3; 2703 -4.3; 2973 -2.7; 3270 -2.4; 3597 -3.2; 3957 -5.0; 4353 -8.4; 4788 -11.5; 5267 -7.5; 5793 -1.3; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -7.2; 11289 -8.3; 12418 -6.2; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 177 Hz   | 0.51 | -4.2 dB  |
| Peaking | 861 Hz   | 1.41 | 4.4 dB   |
| Peaking | 3448 Hz  | 1.75 | 10.6 dB  |
| Peaking | 4985 Hz  | 0.98 | -23.8 dB |
| Peaking | 5906 Hz  | 1.45 | 22.4 dB  |
| Peaking | 22 Hz    | 0.99 | 0.7 dB   |
| Peaking | 2138 Hz  | 5.19 | -1.4 dB  |
| Peaking | 2801 Hz  | 7.58 | 1.3 dB   |
| Peaking | 11215 Hz | 5.41 | -2.3 dB  |
| Peaking | 13410 Hz | 1.22 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE215/Shure%20SE215.png)