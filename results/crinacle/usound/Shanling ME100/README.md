# Shanling ME100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.3; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.7; 66 -4.1; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.5; 116 -7.0; 128 -7.5; 141 -8.0; 155 -8.3; 170 -8.6; 187 -8.9; 206 -9.2; 227 -9.4; 249 -9.5; 274 -9.6; 302 -9.7; 332 -9.7; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.5; 535 -7.9; 588 -7.2; 647 -6.3; 712 -5.4; 783 -4.5; 861 -3.6; 947 -3.4; 1042 -4.0; 1146 -5.0; 1261 -6.2; 1387 -6.9; 1526 -7.0; 1678 -6.9; 1846 -6.6; 2031 -6.5; 2234 -6.4; 2457 -6.1; 2703 -5.4; 2973 -4.5; 3270 -3.8; 3597 -3.8; 3957 -4.8; 4353 -7.2; 4788 -9.6; 5267 -7.0; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shanling ME100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shanling ME100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.19 | 6.2 dB  |
| Peaking | 859 Hz   | 0.14 | -5.3 dB |
| Peaking | 921 Hz   | 0.95 | 7.8 dB  |
| Peaking | 3128 Hz  | 1.7  | 6.0 dB  |
| Peaking | 6301 Hz  | 4.69 | 7.8 dB  |
| Peaking | 1335 Hz  | 5.18 | -0.8 dB |
| Peaking | 1913 Hz  | 4.8  | 1.1 dB  |
| Peaking | 3852 Hz  | 7.05 | 1.5 dB  |
| Peaking | 4805 Hz  | 7.79 | -3.6 dB |
| Peaking | 10144 Hz | 0.83 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shanling%20ME100/Shanling%20ME100.png)