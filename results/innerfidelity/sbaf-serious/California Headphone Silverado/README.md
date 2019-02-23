# California Headphone Silverado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.3; 25 -13.2; 28 -13.1; 31 -12.9; 34 -12.7; 37 -12.4; 41 -11.9; 45 -11.2; 49 -10.6; 54 -10.3; 60 -10.1; 66 -10.1; 72 -11.2; 79 -12.8; 87 -14.2; 96 -14.7; 106 -14.6; 116 -14.4; 128 -15.1; 141 -14.4; 155 -13.1; 170 -12.6; 187 -12.5; 206 -11.8; 227 -11.6; 249 -11.4; 274 -11.0; 302 -10.7; 332 -10.1; 365 -10.8; 402 -9.8; 442 -8.3; 486 -7.0; 535 -6.0; 588 -4.6; 647 -3.8; 712 -3.3; 783 -2.6; 861 -2.5; 947 -2.3; 1042 -2.3; 1146 -2.7; 1261 -4.3; 1387 -6.2; 1526 -7.1; 1678 -7.2; 1846 -6.2; 2031 -4.0; 2234 -4.7; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -3.4; 6373 -4.7; 7010 -7.3; 7711 -9.2; 8482 -11.2; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`California Headphone Silverado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Silverado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.28 | -6.2 dB |
| Peaking | 132 Hz  | 0.5  | -7.6 dB |
| Peaking | 816 Hz  | 1.68 | 5.1 dB  |
| Peaking | 3978 Hz | 1.04 | 7.0 dB  |
| Peaking | 8289 Hz | 3.14 | -6.4 dB |
| Peaking | 64 Hz   | 5.44 | 2.1 dB  |
| Peaking | 377 Hz  | 7.02 | -1.9 dB |
| Peaking | 1140 Hz | 4.4  | 2.4 dB  |
| Peaking | 1581 Hz | 2.65 | -2.9 dB |
| Peaking | 2671 Hz | 5.61 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Silverado/California%20Headphone%20Silverado.png)