# Yamaha HPH MT220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.3; 25 -8.8; 28 -9.3; 31 -9.6; 34 -9.8; 37 -9.9; 41 -10.0; 45 -10.0; 49 -10.0; 54 -9.9; 60 -9.9; 66 -10.0; 72 -10.0; 79 -9.9; 87 -9.9; 96 -9.9; 106 -9.4; 116 -8.8; 128 -8.2; 141 -8.4; 155 -9.3; 170 -7.5; 187 -8.2; 206 -8.3; 227 -7.9; 249 -7.4; 274 -6.7; 302 -6.3; 332 -6.5; 365 -6.4; 402 -6.4; 442 -6.7; 486 -7.5; 535 -8.1; 588 -8.5; 647 -9.1; 712 -9.8; 783 -10.0; 861 -10.3; 947 -10.3; 1042 -10.2; 1146 -9.9; 1261 -9.3; 1387 -9.5; 1526 -9.1; 1678 -8.1; 1846 -6.4; 2031 -4.6; 2234 -3.1; 2457 -1.7; 2703 -1.5; 2973 -2.2; 3270 -0.9; 3597 -0.7; 3957 -4.0; 4353 -6.9; 4788 -3.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.1; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH MT220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH MT220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.88 | -2.8 dB |
| Peaking | 88 Hz   | 0.87 | -2.6 dB |
| Peaking | 1098 Hz | 0.9  | -4.5 dB |
| Peaking | 2769 Hz | 1.54 | 6.4 dB  |
| Peaking | 5800 Hz | 3.95 | 6.3 dB  |
| Peaking | 383 Hz  | 2.72 | 1.3 dB  |
| Peaking | 693 Hz  | 3.17 | -0.8 dB |
| Peaking | 4224 Hz | 2.41 | 3.9 dB  |
| Peaking | 4311 Hz | 6.29 | -7.4 dB |
| Peaking | 8741 Hz | 5.64 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HPH%20MT220/Yamaha%20HPH%20MT220.png)