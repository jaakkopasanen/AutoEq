# Sennheiser RS 195
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.4; 25 -15.3; 28 -15.0; 31 -14.8; 34 -14.4; 37 -14.1; 41 -13.7; 45 -13.6; 49 -13.8; 54 -14.2; 60 -14.7; 66 -14.8; 72 -13.9; 79 -11.8; 87 -9.2; 96 -7.0; 106 -5.7; 116 -4.7; 128 -4.0; 141 -4.1; 155 -4.7; 170 -5.1; 187 -5.2; 206 -4.7; 227 -4.0; 249 -3.5; 274 -3.5; 302 -3.9; 332 -4.4; 365 -4.8; 402 -5.2; 442 -5.7; 486 -6.3; 535 -6.6; 588 -6.6; 647 -6.5; 712 -6.3; 783 -6.0; 861 -6.0; 947 -6.0; 1042 -6.3; 1146 -6.9; 1261 -7.8; 1387 -9.0; 1526 -9.8; 1678 -9.0; 1846 -3.9; 2031 -0.5; 2234 -8.9; 2457 -13.4; 2703 -14.6; 2973 -14.8; 3270 -13.8; 3597 -11.7; 3957 -10.3; 4353 -7.7; 4788 -4.8; 5267 -3.4; 5793 -3.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -8.1; 10263 -10.7; 11289 -10.4; 12418 -8.8; 13660 -9.4; 15026 -12.0; 16529 -10.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.13 | -9.8 dB |
| Peaking | 63 Hz    | 2.93 | -7.8 dB |
| Peaking | 3012 Hz  | 2.59 | -9.7 dB |
| Peaking | 6238 Hz  | 2.21 | 6.8 dB  |
| Peaking | 13342 Hz | 0.58 | -4.5 dB |
| Peaking | 95 Hz    | 0.73 | -2.4 dB |
| Peaking | 121 Hz   | 1.7  | 4.9 dB  |
| Peaking | 269 Hz   | 1.65 | 3.1 dB  |
| Peaking | 1886 Hz  | 1.69 | -5.4 dB |
| Peaking | 1982 Hz  | 6.23 | 14.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB |
| Peaking | 125 Hz   | 1.41 | 3.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20195/Sennheiser%20RS%20195.png)