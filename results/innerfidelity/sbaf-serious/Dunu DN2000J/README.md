# Dunu DN2000J
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.4; 25 -2.8; 28 -3.4; 31 -3.9; 34 -4.3; 37 -4.6; 41 -4.9; 45 -5.3; 49 -5.5; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.3; 87 -7.6; 96 -7.9; 106 -8.1; 116 -8.1; 128 -8.3; 141 -8.4; 155 -8.3; 170 -8.2; 187 -8.0; 206 -7.9; 227 -7.5; 249 -7.3; 274 -6.9; 302 -6.5; 332 -6.2; 365 -5.8; 402 -5.4; 442 -4.8; 486 -4.6; 535 -4.3; 588 -3.6; 647 -3.3; 712 -3.1; 783 -2.8; 861 -2.8; 947 -3.0; 1042 -3.1; 1146 -3.4; 1261 -3.4; 1387 -4.1; 1526 -5.0; 1678 -5.3; 1846 -5.2; 2031 -5.0; 2234 -4.7; 2457 -4.0; 2703 -4.0; 2973 -3.4; 3270 -2.4; 3597 -0.5; 3957 -0.6; 4353 -4.8; 4788 -9.1; 5267 -9.7; 5793 -12.1; 6373 -11.5; 7010 -9.4; 7711 -9.9; 8482 -10.2; 9330 -8.6; 10263 -4.5; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -4.7; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000J GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000J ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 106 Hz   | 0.62 | -4.4 dB |
| Peaking | 237 Hz   | 0.9  | -2.5 dB |
| Peaking | 5859 Hz  | 3.34 | -8.4 dB |
| Peaking | 8569 Hz  | 1.98 | -7.2 dB |
| Peaking | 10847 Hz | 2.66 | 2.8 dB  |
| Peaking | 19 Hz    | 2.19 | 1.6 dB  |
| Peaking | 890 Hz   | 1.63 | 1.1 dB  |
| Peaking | 1812 Hz  | 1.56 | -2.2 dB |
| Peaking | 3817 Hz  | 3.77 | 5.1 dB  |
| Peaking | 4694 Hz  | 6.57 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000J/Dunu%20DN2000J.png)