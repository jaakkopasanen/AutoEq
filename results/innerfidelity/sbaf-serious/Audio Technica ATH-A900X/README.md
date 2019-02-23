# Audio Technica ATH-A900X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -3.0; 28 -3.9; 31 -4.7; 34 -5.3; 37 -5.9; 41 -6.5; 45 -7.0; 49 -7.4; 54 -7.7; 60 -8.3; 66 -8.9; 72 -9.0; 79 -9.2; 87 -10.1; 96 -10.5; 106 -10.7; 116 -11.2; 128 -11.9; 141 -12.2; 155 -11.8; 170 -11.5; 187 -11.8; 206 -11.5; 227 -10.9; 249 -10.2; 274 -9.3; 302 -8.6; 332 -8.2; 365 -8.5; 402 -8.6; 442 -8.5; 486 -8.8; 535 -8.8; 588 -8.6; 647 -8.1; 712 -7.4; 783 -7.3; 861 -7.7; 947 -7.7; 1042 -7.4; 1146 -7.3; 1261 -6.7; 1387 -6.1; 1526 -6.3; 1678 -6.8; 1846 -8.2; 2031 -8.9; 2234 -7.9; 2457 -5.8; 2703 -4.1; 2973 -2.9; 3270 -2.7; 3597 -1.9; 3957 -1.3; 4353 -4.4; 4788 -1.1; 5267 -0.5; 5793 -1.2; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.6; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.18 | 5.3 dB  |
| Peaking | 147 Hz  | 0.59 | -5.4 dB |
| Peaking | 3365 Hz | 1.81 | 6.8 dB  |
| Peaking | 4141 Hz | 0.48 | -4.0 dB |
| Peaking | 5596 Hz | 1.76 | 8.5 dB  |
| Peaking | 314 Hz  | 4.62 | 1.1 dB  |
| Peaking | 536 Hz  | 3.02 | -1.1 dB |
| Peaking | 1522 Hz | 2.88 | 2.4 dB  |
| Peaking | 2039 Hz | 2.2  | -2.5 dB |
| Peaking | 2633 Hz | 4.77 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A900X/Audio%20Technica%20ATH-A900X.png)