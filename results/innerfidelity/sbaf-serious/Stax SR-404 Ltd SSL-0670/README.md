# Stax SR-404 Ltd SSL-0670
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -1.0; 31 -1.1; 34 -1.2; 37 -1.2; 41 -1.2; 45 -1.2; 49 -1.2; 54 -1.2; 60 -1.3; 66 -1.7; 72 -2.2; 79 -2.4; 87 -2.6; 96 -2.9; 106 -3.3; 116 -3.5; 128 -3.7; 141 -3.9; 155 -4.0; 170 -4.1; 187 -4.3; 206 -4.4; 227 -4.3; 249 -4.4; 274 -4.4; 302 -4.3; 332 -4.2; 365 -4.3; 402 -4.3; 442 -4.1; 486 -4.4; 535 -4.6; 588 -4.4; 647 -4.6; 712 -5.0; 783 -4.9; 861 -5.5; 947 -5.8; 1042 -6.3; 1146 -6.8; 1261 -7.6; 1387 -8.6; 1526 -9.3; 1678 -9.6; 1846 -8.4; 2031 -5.9; 2234 -4.3; 2457 -4.2; 2703 -5.1; 2973 -5.2; 3270 -5.1; 3597 -5.1; 3957 -3.1; 4353 -3.7; 4788 -4.3; 5267 -3.3; 5793 -5.5; 6373 -3.8; 7010 -3.7; 7711 -5.9; 8482 -7.6; 9330 -9.9; 10263 -8.3; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -8.3; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 Ltd SSL-0670 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 Ltd SSL-0670 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.41 | 3.9 dB  |
| Peaking | 191 Hz   |  0.03 | 1.6 dB  |
| Peaking | 1539 Hz  |  2.2  | -5.3 dB |
| Peaking | 6240 Hz  |  0.76 | 1.9 dB  |
| Peaking | 9338 Hz  |  3.25 | -5.5 dB |
| Peaking | 1028 Hz  |  4.32 | -0.6 dB |
| Peaking | 2316 Hz  |  5.87 | 1.9 dB  |
| Peaking | 3037 Hz  |  3.49 | -0.8 dB |
| Peaking | 6739 Hz  | 16.11 | 2.3 dB  |
| Peaking | 19633 Hz |  1.27 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20Ltd%20SSL-0670/Stax%20SR-404%20Ltd%20SSL-0670.png)