# AKG K701 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.5; 37 -2.0; 41 -2.5; 45 -2.9; 49 -3.4; 54 -3.8; 60 -3.9; 66 -3.3; 72 -3.5; 79 -5.0; 87 -5.0; 96 -6.2; 106 -6.8; 116 -7.1; 128 -7.5; 141 -7.8; 155 -8.0; 170 -8.1; 187 -8.2; 206 -8.4; 227 -8.2; 249 -8.2; 274 -8.2; 302 -8.0; 332 -7.6; 365 -7.5; 402 -7.3; 442 -6.7; 486 -6.4; 535 -6.2; 588 -5.7; 647 -5.3; 712 -4.6; 783 -4.2; 861 -5.2; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.1; 1387 -7.3; 1526 -7.5; 1678 -8.2; 1846 -9.0; 2031 -9.7; 2234 -9.5; 2457 -9.2; 2703 -8.8; 2973 -7.5; 3270 -5.8; 3597 -6.2; 3957 -6.8; 4353 -8.4; 4788 -8.5; 5267 -7.6; 5793 -9.4; 6373 -11.3; 7010 -10.1; 7711 -10.3; 8482 -11.0; 9330 -9.7; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.0; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.11 | 6.5 dB  |
| Peaking | 68 Hz    | 4.57 | 2.6 dB  |
| Peaking | 758 Hz   | 4.33 | 2.6 dB  |
| Peaking | 2097 Hz  | 2.37 | -3.3 dB |
| Peaking | 7381 Hz  | 1.58 | -4.5 dB |
| Peaking | 206 Hz   | 1.08 | -2.1 dB |
| Peaking | 2743 Hz  | 4.49 | -1.2 dB |
| Peaking | 3390 Hz  | 3.54 | 2.1 dB  |
| Peaking | 4477 Hz  | 7.28 | -1.3 dB |
| Peaking | 11377 Hz | 4.88 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20B/AKG%20K701%20sample%20B.png)