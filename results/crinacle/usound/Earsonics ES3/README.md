# Earsonics ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.5; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.7; 49 -10.7; 54 -10.6; 60 -10.5; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.3; 96 -10.3; 106 -10.0; 116 -9.6; 128 -9.3; 141 -8.8; 155 -8.2; 170 -7.6; 187 -7.1; 206 -6.7; 227 -6.3; 249 -6.1; 274 -6.1; 302 -6.2; 332 -6.5; 365 -6.7; 402 -6.9; 442 -7.2; 486 -7.3; 535 -7.5; 588 -7.6; 647 -7.6; 712 -7.5; 783 -7.4; 861 -7.4; 947 -7.5; 1042 -8.0; 1146 -8.9; 1261 -9.7; 1387 -10.0; 1526 -9.6; 1678 -8.7; 1846 -7.0; 2031 -4.1; 2234 -2.3; 2457 -2.0; 2703 -1.2; 2973 -1.2; 3270 -2.7; 3597 -4.6; 3957 -4.2; 4353 -0.9; 4788 -0.5; 5267 -2.5; 5793 -3.3; 6373 -7.2; 7010 -6.2; 7711 -5.9; 8482 -7.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.41 | -4.9 dB |
| Peaking | 594 Hz  | 2.89 | -1.0 dB |
| Peaking | 1458 Hz | 1.65 | -5.0 dB |
| Peaking | 2537 Hz | 1.79 | 6.1 dB  |
| Peaking | 4731 Hz | 4.34 | 5.6 dB  |
| Peaking | 23 Hz   | 2.14 | -0.7 dB |
| Peaking | 117 Hz  | 2.02 | -1.0 dB |
| Peaking | 247 Hz  | 1.38 | 1.3 dB  |
| Peaking | 425 Hz  | 2.1  | -0.5 dB |
| Peaking | 7762 Hz | 2.02 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20ES3/Earsonics%20ES3.png)