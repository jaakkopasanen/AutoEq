# Cowin E7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.3; 25 -6.8; 28 -6.3; 31 -6.0; 34 -5.6; 37 -5.4; 41 -5.2; 45 -5.1; 49 -5.1; 54 -5.2; 60 -5.4; 66 -5.7; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.2; 106 -7.6; 116 -8.0; 128 -8.4; 141 -8.8; 155 -9.1; 170 -9.4; 187 -9.6; 206 -9.7; 227 -9.9; 249 -9.9; 274 -9.9; 302 -10.2; 332 -10.3; 365 -10.0; 402 -9.9; 442 -9.7; 486 -9.4; 535 -9.1; 588 -8.8; 647 -8.6; 712 -8.4; 783 -8.1; 861 -6.6; 947 -6.1; 1042 -7.0; 1146 -6.5; 1261 -4.4; 1387 -2.4; 1526 -0.7; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -2.8; 5267 -2.3; 5793 -1.2; 6373 -2.4; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -8.4; 15026 -6.5; 16529 -6.5; 18182 -7.6; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.24 | -2.6 dB |
| Peaking | 55 Hz    | 0.59 | 2.7 dB  |
| Peaking | 275 Hz   | 0.3  | -3.9 dB |
| Peaking | 1755 Hz  | 1.37 | 5.8 dB  |
| Peaking | 3784 Hz  | 0.97 | 5.6 dB  |
| Peaking | 1090 Hz  | 2.23 | 1.9 dB  |
| Peaking | 1111 Hz  | 5.04 | -3.6 dB |
| Peaking | 6014 Hz  | 6.08 | 3.4 dB  |
| Peaking | 9834 Hz  | 0.59 | -1.2 dB |
| Peaking | 19990 Hz | 1.77 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7/Cowin%20E7.png)