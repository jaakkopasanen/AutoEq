# Apple In-Ear 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.3; 25 -5.3; 28 -5.3; 31 -5.3; 34 -5.3; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.8; 54 -5.9; 60 -6.1; 66 -6.4; 72 -6.7; 79 -7.0; 87 -7.4; 96 -7.8; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.8; 155 -9.0; 170 -9.1; 187 -9.3; 206 -9.2; 227 -9.3; 249 -9.2; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.7; 402 -8.5; 442 -8.2; 486 -8.1; 535 -7.7; 588 -6.9; 647 -6.6; 712 -6.6; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.0; 1526 -7.3; 1678 -7.3; 1846 -7.0; 2031 -6.5; 2234 -6.3; 2457 -6.0; 2703 -6.2; 2973 -5.1; 3270 -2.2; 3597 -0.5; 3957 -1.0; 4353 -3.5; 4788 -3.5; 5267 -1.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple In-Ear 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple In-Ear 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.57 | 1.5 dB  |
| Peaking | 202 Hz   | 0.58 | -3.0 dB |
| Peaking | 3639 Hz  | 4.21 | 6.0 dB  |
| Peaking | 5997 Hz  | 2.46 | 6.8 dB  |
| Peaking | 7756 Hz  | 2.04 | -1.8 dB |
| Peaking | 794 Hz   | 2.6  | 0.8 dB  |
| Peaking | 1624 Hz  | 2.58 | -0.6 dB |
| Peaking | 1687 Hz  | 2.26 | -0.3 dB |
| Peaking | 19761 Hz | 1.68 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20In-Ear%202013/Apple%20In-Ear%202013.png)