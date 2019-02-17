# Sony IER-M9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.7; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.5; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.6; 96 -8.7; 106 -8.9; 116 -9.0; 128 -9.0; 141 -9.0; 155 -9.0; 170 -8.9; 187 -8.7; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.8; 302 -7.5; 332 -7.3; 365 -7.1; 402 -6.8; 442 -6.6; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.4; 712 -5.0; 783 -4.8; 861 -4.6; 947 -4.6; 1042 -4.8; 1146 -5.2; 1261 -5.4; 1387 -5.5; 1526 -5.3; 1678 -4.9; 1846 -4.5; 2031 -4.0; 2234 -3.4; 2457 -2.3; 2703 -1.8; 2973 -3.2; 3270 -5.7; 3597 -5.6; 3957 -4.0; 4353 -4.1; 4788 -3.8; 5267 -1.9; 5793 -0.6; 6373 -0.5; 7010 -2.3; 7711 -4.6; 8482 -6.7; 9330 -8.5; 10263 -10.8; 11289 -11.7; 12418 -9.4; 13660 -8.1; 15026 -10.9; 16529 -13.1; 18182 -9.9; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.29 | -2.0 dB |
| Peaking | 168 Hz   | 0.53 | -3.3 dB |
| Peaking | 6165 Hz  | 2.42 | 5.4 dB  |
| Peaking | 10716 Hz | 2.04 | -6.5 dB |
| Peaking | 16680 Hz | 1.38 | -8.6 dB |
| Peaking | 884 Hz   | 2.93 | 0.8 dB  |
| Peaking | 1378 Hz  | 2.11 | -0.9 dB |
| Peaking | 2689 Hz  | 2.75 | 3.5 dB  |
| Peaking | 3358 Hz  | 4.72 | -2.9 dB |
| Peaking | 13469 Hz | 9.01 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -10.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-M9/Sony%20IER-M9.png)