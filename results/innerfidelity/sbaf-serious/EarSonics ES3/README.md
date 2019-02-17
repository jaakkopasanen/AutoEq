# EarSonics ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.7; 28 -9.8; 31 -9.9; 34 -10.0; 37 -10.0; 41 -10.0; 45 -10.0; 49 -10.0; 54 -10.0; 60 -9.9; 66 -9.9; 72 -9.8; 79 -9.8; 87 -9.6; 96 -9.4; 106 -8.9; 116 -8.4; 128 -7.8; 141 -7.2; 155 -6.4; 170 -5.7; 187 -4.9; 206 -4.3; 227 -3.7; 249 -3.6; 274 -3.5; 302 -3.6; 332 -3.8; 365 -4.1; 402 -4.4; 442 -4.5; 486 -4.8; 535 -4.9; 588 -4.8; 647 -4.8; 712 -5.1; 783 -5.1; 861 -5.6; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.2; 1387 -9.3; 1526 -10.3; 1678 -10.9; 1846 -10.3; 2031 -8.0; 2234 -5.0; 2457 -2.9; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -0.5; 6373 -2.9; 7010 -7.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`EarSonics ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `EarSonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.31 | -3.6 dB |
| Peaking | 117 Hz  | 0.77 | -3.5 dB |
| Peaking | 204 Hz  | 0.51 | 5.1 dB  |
| Peaking | 1695 Hz | 1.9  | -7.7 dB |
| Peaking | 3423 Hz | 0.86 | 7.6 dB  |
| Peaking | 762 Hz  | 4.82 | 0.7 dB  |
| Peaking | 2703 Hz | 5.03 | 1.2 dB  |
| Peaking | 3513 Hz | 3.01 | -1.1 dB |
| Peaking | 6017 Hz | 2.74 | 6.7 dB  |
| Peaking | 6672 Hz | 1.93 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/EarSonics%20ES3/EarSonics%20ES3.png)