# Stax SR-009
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.0; 72 -2.0; 79 -1.8; 87 -2.0; 96 -2.2; 106 -2.3; 116 -2.5; 128 -2.8; 141 -2.9; 155 -3.1; 170 -3.4; 187 -3.5; 206 -3.6; 227 -3.5; 249 -3.7; 274 -3.7; 302 -3.8; 332 -3.9; 365 -4.0; 402 -4.1; 442 -4.2; 486 -4.6; 535 -4.7; 588 -4.5; 647 -4.8; 712 -4.9; 783 -4.6; 861 -5.2; 947 -5.9; 1042 -6.5; 1146 -7.1; 1261 -6.9; 1387 -6.5; 1526 -6.6; 1678 -6.6; 1846 -4.8; 2031 -3.5; 2234 -2.9; 2457 -1.6; 2703 -2.4; 2973 -2.4; 3270 -2.9; 3597 -2.8; 3957 -4.5; 4353 -5.7; 4788 -7.7; 5267 -6.0; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.12 | 6.1 dB  |
| Peaking | 381 Hz  | 0.85 | 1.8 dB  |
| Peaking | 2781 Hz | 1.73 | 4.7 dB  |
| Peaking | 4928 Hz | 5.3  | -4.0 dB |
| Peaking | 5993 Hz | 4.03 | 6.7 dB  |
| Peaking | 796 Hz  | 2.58 | 1.5 dB  |
| Peaking | 1292 Hz | 1.11 | -1.6 dB |
| Peaking | 2126 Hz | 3.34 | 1.5 dB  |
| Peaking | 6734 Hz | 7.62 | 1.7 dB  |
| Peaking | 7638 Hz | 2.6  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009/Stax%20SR-009.png)