# Sennheiser RS 195
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.2; 25 -15.1; 28 -14.9; 31 -14.6; 34 -14.3; 37 -13.9; 41 -13.6; 45 -13.4; 49 -13.6; 54 -14.0; 60 -14.6; 66 -14.6; 72 -13.8; 79 -11.8; 87 -9.1; 96 -6.9; 106 -5.5; 116 -4.4; 128 -3.8; 141 -3.9; 155 -4.5; 170 -4.9; 187 -5.0; 206 -4.6; 227 -3.9; 249 -3.4; 274 -3.4; 302 -3.8; 332 -4.4; 365 -4.8; 402 -5.2; 442 -5.7; 486 -6.3; 535 -6.6; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.1; 861 -6.1; 947 -6.2; 1042 -6.4; 1146 -7.0; 1261 -8.0; 1387 -9.2; 1526 -10.1; 1678 -9.2; 1846 -3.8; 2031 -0.5; 2234 -9.4; 2457 -14.3; 2703 -15.2; 2973 -14.9; 3270 -13.5; 3597 -11.5; 3957 -9.9; 4353 -7.3; 4788 -5.1; 5267 -4.0; 5793 -3.1; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -6.7; 10263 -10.3; 11289 -11.4; 12418 -8.9; 13660 -8.7; 15026 -11.6; 16529 -10.0; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.15 | -9.5 dB  |
| Peaking | 62 Hz    | 2.98 | -7.7 dB  |
| Peaking | 2936 Hz  | 2.67 | -10.0 dB |
| Peaking | 6267 Hz  | 2.5  | 6.8 dB   |
| Peaking | 13381 Hz | 0.63 | -4.2 dB  |
| Peaking | 77 Hz    | 4.79 | -2.7 dB  |
| Peaking | 126 Hz   | 2.14 | 3.2 dB   |
| Peaking | 271 Hz   | 1.78 | 3.0 dB   |
| Peaking | 1871 Hz  | 1.68 | -5.8 dB  |
| Peaking | 1972 Hz  | 6.28 | 15.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB |
| Peaking | 125 Hz   | 1.41 | 3.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20195/Sennheiser%20RS%20195.png)