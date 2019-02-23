# Fostex TH900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.5; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.1; 41 -9.1; 45 -8.9; 49 -8.7; 54 -8.7; 60 -9.0; 66 -9.2; 72 -9.4; 79 -9.7; 87 -9.9; 96 -10.3; 106 -10.3; 116 -10.2; 128 -10.3; 141 -10.2; 155 -10.0; 170 -9.6; 187 -9.5; 206 -9.1; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.1; 332 -6.4; 365 -5.5; 402 -4.4; 442 -3.1; 486 -2.0; 535 -0.7; 588 -0.5; 647 -1.7; 712 -3.0; 783 -2.9; 861 -4.2; 947 -4.6; 1042 -4.6; 1146 -4.5; 1261 -4.2; 1387 -4.4; 1526 -4.6; 1678 -4.9; 1846 -4.6; 2031 -2.8; 2234 -1.4; 2457 -1.7; 2703 -1.6; 2973 -2.9; 3270 -3.1; 3597 -2.8; 3957 -1.9; 4353 -4.1; 4788 -5.2; 5267 -5.1; 5793 -6.9; 6373 -7.0; 7010 -6.7; 7711 -6.0; 8482 -5.1; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -7.0; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.9  | -2.9 dB |
| Peaking | 130 Hz  | 0.47 | -5.1 dB |
| Peaking | 552 Hz  | 1.75 | 5.8 dB  |
| Peaking | 2471 Hz | 2.73 | 4.0 dB  |
| Peaking | 3799 Hz | 6.1  | 2.9 dB  |
| Peaking | 951 Hz  | 6.49 | -0.5 dB |
| Peaking | 1739 Hz | 4.34 | -1.9 dB |
| Peaking | 1747 Hz | 1.97 | 1.1 dB  |
| Peaking | 5920 Hz | 1.22 | 0.8 dB  |
| Peaking | 6303 Hz | 2.59 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900/Fostex%20TH900.png)