# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.2; 49 -8.3; 54 -8.5; 60 -8.6; 66 -8.8; 72 -8.9; 79 -9.2; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.8; 128 -9.9; 141 -9.9; 155 -9.9; 170 -9.9; 187 -9.8; 206 -9.6; 227 -9.4; 249 -9.2; 274 -9.0; 302 -8.8; 332 -8.6; 365 -8.3; 402 -8.1; 442 -7.9; 486 -7.6; 535 -7.3; 588 -7.1; 647 -6.9; 712 -6.5; 783 -6.2; 861 -6.1; 947 -6.1; 1042 -6.4; 1146 -6.7; 1261 -7.0; 1387 -7.1; 1526 -6.9; 1678 -6.5; 1846 -6.0; 2031 -5.7; 2234 -5.6; 2457 -5.2; 2703 -4.4; 2973 -3.9; 3270 -4.7; 3597 -5.2; 3957 -3.6; 4353 -3.2; 4788 -3.5; 5267 -2.3; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -7.1; 9330 -8.4; 10263 -9.1; 11289 -11.7; 12418 -11.6; 13660 -7.2; 15026 -6.3; 16529 -7.7; 18182 -8.6; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.38 | -1.1 dB |
| Peaking | 162 Hz   | 0.49 | -3.4 dB |
| Peaking | 3898 Hz  | 1.16 | 2.1 dB  |
| Peaking | 6045 Hz  | 3.4  | 5.8 dB  |
| Peaking | 11575 Hz | 2.17 | -6.2 dB |
| Peaking | 862 Hz   | 2.83 | 0.8 dB  |
| Peaking | 1384 Hz  | 2.67 | -1.0 dB |
| Peaking | 2837 Hz  | 7.76 | 1.0 dB  |
| Peaking | 14576 Hz | 3.42 | 1.8 dB  |
| Peaking | 17647 Hz | 2.07 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-M7/Sony%20IER-M7.png)