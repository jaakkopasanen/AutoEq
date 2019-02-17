# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.9; 25 -5.8; 28 -6.7; 31 -7.2; 34 -7.4; 37 -7.4; 41 -7.3; 45 -7.2; 49 -7.1; 54 -7.0; 60 -7.0; 66 -7.1; 72 -7.3; 79 -7.7; 87 -8.1; 96 -8.5; 106 -8.8; 116 -8.8; 128 -8.6; 141 -8.3; 155 -8.0; 170 -7.8; 187 -7.8; 206 -7.8; 227 -7.8; 249 -7.8; 274 -7.8; 302 -7.8; 332 -7.8; 365 -7.8; 402 -7.9; 442 -8.0; 486 -7.8; 535 -7.0; 588 -5.7; 647 -4.6; 712 -4.0; 783 -3.2; 861 -2.4; 947 -2.6; 1042 -3.6; 1146 -4.7; 1261 -5.8; 1387 -6.6; 1526 -9.2; 1678 -11.3; 1846 -11.4; 2031 -10.0; 2234 -8.9; 2457 -8.6; 2703 -8.2; 2973 -8.0; 3270 -7.9; 3597 -8.5; 3957 -9.5; 4353 -9.1; 4788 -6.4; 5267 -2.6; 5793 -0.5; 6373 -1.4; 7010 -7.8; 7711 -11.1; 8482 -7.0; 9330 -3.6; 10263 -3.7; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 99 Hz    | 0.33 | -5.3 dB  |
| Peaking | 411 Hz   | 1.96 | -3.1 dB  |
| Peaking | 1801 Hz  | 2.58 | -7.8 dB  |
| Peaking | 3600 Hz  | 1.45 | -5.4 dB  |
| Peaking | 21436 Hz | 2.19 | -4.7 dB  |
| Peaking | 35 Hz    | 3.44 | -1.5 dB  |
| Peaking | 886 Hz   | 4.07 | 2.5 dB   |
| Peaking | 4402 Hz  | 4.71 | -3.4 dB  |
| Peaking | 5998 Hz  | 2.33 | 6.7 dB   |
| Peaking | 7519 Hz  | 4.14 | -10.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)