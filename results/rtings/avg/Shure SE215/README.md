# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.7; 25 -2.8; 28 -3.0; 31 -3.1; 34 -3.3; 37 -3.4; 41 -3.6; 45 -3.7; 49 -3.9; 54 -4.2; 60 -4.8; 66 -5.4; 72 -5.9; 79 -6.4; 87 -7.1; 96 -7.8; 106 -8.5; 116 -9.3; 128 -10.0; 141 -10.6; 155 -11.0; 170 -11.3; 187 -11.5; 206 -11.6; 227 -11.6; 249 -11.5; 274 -11.3; 302 -11.1; 332 -10.8; 365 -10.4; 402 -9.9; 442 -9.4; 486 -8.8; 535 -8.2; 588 -7.5; 647 -6.7; 712 -6.0; 783 -5.3; 861 -5.0; 947 -5.1; 1042 -5.8; 1146 -7.0; 1261 -7.3; 1387 -7.8; 1526 -8.2; 1678 -8.7; 1846 -9.3; 2031 -9.7; 2234 -9.0; 2457 -7.4; 2703 -5.7; 2973 -4.7; 3270 -4.6; 3597 -5.4; 3957 -7.2; 4353 -10.5; 4788 -13.2; 5267 -9.6; 5793 -3.7; 6373 -0.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -6.3; 10263 -9.5; 11289 -9.4; 12418 -7.4; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 226 Hz   | 0.75 | -6.7 dB |
| Peaking | 1900 Hz  | 2.7  | -4.2 dB |
| Peaking | 4801 Hz  | 4.97 | -8.9 dB |
| Peaking | 6346 Hz  | 5.39 | 6.5 dB  |
| Peaking | 21189 Hz | 1.18 | -2.9 dB |
| Peaking | 24 Hz    | 1.23 | 3.0 dB  |
| Peaking | 51 Hz    | 2.21 | 1.8 dB  |
| Peaking | 846 Hz   | 4.73 | 1.8 dB  |
| Peaking | 3165 Hz  | 5.01 | 2.2 dB  |
| Peaking | 10891 Hz | 3.48 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE215/Shure%20SE215.png)