# Oppo PM2 2014 Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.5; 25 -3.7; 28 -4.0; 31 -4.2; 34 -4.3; 37 -4.4; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.5; 60 -4.3; 66 -4.7; 72 -5.4; 79 -5.8; 87 -6.1; 96 -6.5; 106 -6.8; 116 -7.0; 128 -7.2; 141 -7.4; 155 -7.5; 170 -7.5; 187 -7.9; 206 -8.4; 227 -8.6; 249 -8.7; 274 -8.2; 302 -7.5; 332 -6.7; 365 -6.9; 402 -6.9; 442 -7.0; 486 -7.8; 535 -8.3; 588 -8.2; 647 -8.2; 712 -7.6; 783 -7.2; 861 -7.8; 947 -7.3; 1042 -7.5; 1146 -7.6; 1261 -7.7; 1387 -8.4; 1526 -9.0; 1678 -9.5; 1846 -9.4; 2031 -8.9; 2234 -8.1; 2457 -7.0; 2703 -6.0; 2973 -4.9; 3270 -4.7; 3597 -5.1; 3957 -4.7; 4353 -5.1; 4788 -3.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.6; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.57 | 3.5 dB  |
| Peaking | 59 Hz   | 1.17 | 2.4 dB  |
| Peaking | 174 Hz  | 0.21 | -1.6 dB |
| Peaking | 1735 Hz | 2.63 | -3.1 dB |
| Peaking | 5679 Hz | 2.76 | 6.7 dB  |
| Peaking | 251 Hz  | 2.23 | -2.2 dB |
| Peaking | 329 Hz  | 1.13 | 2.0 dB  |
| Peaking | 566 Hz  | 2.57 | -1.4 dB |
| Peaking | 3146 Hz | 4.58 | 1.8 dB  |
| Peaking | 8846 Hz | 5.12 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20Stock%20Pads/Oppo%20PM2%202014%20Stock%20Pads.png)