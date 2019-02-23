# EarSonics ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.9; 25 -11.0; 28 -11.2; 31 -11.3; 34 -11.3; 37 -11.3; 41 -11.3; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.3; 72 -11.2; 79 -11.1; 87 -11.0; 96 -10.7; 106 -10.3; 116 -9.8; 128 -9.2; 141 -8.6; 155 -7.8; 170 -7.1; 187 -6.3; 206 -5.7; 227 -5.1; 249 -4.9; 274 -4.8; 302 -5.0; 332 -5.2; 365 -5.5; 402 -5.8; 442 -5.9; 486 -6.2; 535 -6.3; 588 -6.2; 647 -6.2; 712 -6.4; 783 -6.4; 861 -6.9; 947 -7.5; 1042 -8.2; 1146 -8.9; 1261 -9.6; 1387 -10.7; 1526 -11.7; 1678 -12.3; 1846 -11.7; 2031 -9.3; 2234 -6.4; 2457 -4.2; 2703 -2.4; 2973 -0.8; 3270 -0.5; 3597 -1.8; 3957 -1.3; 4353 -0.8; 4788 -1.4; 5267 -1.9; 5793 -1.1; 6373 -4.2; 7010 -8.3; 7711 -7.1; 8482 -6.6; 9330 -7.0; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`EarSonics ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `EarSonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.68 | -5.3 dB |
| Peaking | 88 Hz   | 1.58 | -3.5 dB |
| Peaking | 1687 Hz | 1.77 | -7.5 dB |
| Peaking | 3006 Hz | 1.78 | 6.4 dB  |
| Peaking | 4853 Hz | 2.53 | 4.4 dB  |
| Peaking | 56 Hz   | 4.17 | -0.7 dB |
| Peaking | 136 Hz  | 2.68 | -1.2 dB |
| Peaking | 258 Hz  | 1.27 | 1.9 dB  |
| Peaking | 6067 Hz | 5.65 | 4.8 dB  |
| Peaking | 6806 Hz | 2.86 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/EarSonics%20ES3/EarSonics%20ES3.png)