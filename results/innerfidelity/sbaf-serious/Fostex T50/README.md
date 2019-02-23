# Fostex T50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.7; 106 -1.1; 116 -1.9; 128 -3.9; 141 -5.5; 155 -5.9; 170 -5.8; 187 -5.8; 206 -6.0; 227 -6.3; 249 -6.4; 274 -6.6; 302 -6.9; 332 -7.1; 365 -7.6; 402 -8.7; 442 -8.5; 486 -8.2; 535 -8.4; 588 -8.5; 647 -8.6; 712 -9.0; 783 -8.9; 861 -8.9; 947 -9.0; 1042 -9.3; 1146 -9.0; 1261 -8.9; 1387 -9.1; 1526 -9.6; 1678 -10.1; 1846 -10.0; 2031 -10.3; 2234 -9.7; 2457 -8.9; 2703 -7.9; 2973 -7.4; 3270 -5.5; 3597 -5.4; 3957 -6.3; 4353 -5.2; 4788 -3.2; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.23 | 6.9 dB  |
| Peaking | 155 Hz  | 2.47 | -3.2 dB |
| Peaking | 448 Hz  | 0.38 | -3.6 dB |
| Peaking | 1928 Hz | 1.86 | -3.1 dB |
| Peaking | 5692 Hz | 2.7  | 6.9 dB  |
| Peaking | 18 Hz   | 1.2  | 1.5 dB  |
| Peaking | 45 Hz   | 0.37 | -0.8 dB |
| Peaking | 97 Hz   | 2.42 | 1.4 dB  |
| Peaking | 3393 Hz | 9.29 | 1.8 dB  |
| Peaking | 8713 Hz | 4.13 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50/Fostex%20T50.png)