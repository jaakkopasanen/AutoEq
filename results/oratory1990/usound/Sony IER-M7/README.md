# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.5; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.6; 72 -8.8; 79 -9.0; 87 -9.2; 96 -9.4; 106 -9.5; 116 -9.7; 128 -9.7; 141 -9.8; 155 -9.8; 170 -9.7; 187 -9.6; 206 -9.4; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.2; 402 -8.0; 442 -7.8; 486 -7.5; 535 -7.2; 588 -6.9; 647 -6.7; 712 -6.4; 783 -6.1; 861 -5.9; 947 -6.0; 1042 -6.2; 1146 -6.6; 1261 -6.9; 1387 -6.9; 1526 -6.8; 1678 -6.4; 1846 -5.9; 2031 -5.6; 2234 -5.4; 2457 -5.0; 2703 -4.2; 2973 -3.7; 3270 -4.5; 3597 -5.0; 3957 -3.5; 4353 -3.0; 4788 -3.3; 5267 -2.1; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.1; 8482 -6.9; 9330 -8.2; 10263 -8.9; 11289 -11.6; 12418 -11.4; 13660 -7.0; 15026 -6.4; 16529 -7.5; 18182 -8.5; 20000 -6.4
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
| Peaking | 59 Hz    | 0.33 | -1.3 dB |
| Peaking | 171 Hz   | 0.57 | -2.7 dB |
| Peaking | 3740 Hz  | 1.07 | 2.2 dB  |
| Peaking | 6001 Hz  | 3.29 | 5.7 dB  |
| Peaking | 11587 Hz | 2.27 | -6.0 dB |
| Peaking | 856 Hz   | 2.83 | 0.8 dB  |
| Peaking | 1386 Hz  | 3.44 | -0.9 dB |
| Peaking | 8905 Hz  | 6.93 | -1.0 dB |
| Peaking | 14544 Hz | 3.14 | 1.6 dB  |
| Peaking | 17696 Hz | 2.3  | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-M7/Sony%20IER-M7.png)