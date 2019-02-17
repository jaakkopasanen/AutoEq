# Audio Technica ATH-A900X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.3; 25 -1.9; 28 -2.8; 31 -3.6; 34 -4.3; 37 -4.8; 41 -5.4; 45 -5.9; 49 -6.3; 54 -6.6; 60 -7.3; 66 -7.9; 72 -8.0; 79 -8.1; 87 -9.1; 96 -9.5; 106 -9.7; 116 -10.1; 128 -10.8; 141 -11.1; 155 -10.8; 170 -10.4; 187 -10.8; 206 -10.5; 227 -9.8; 249 -9.2; 274 -8.2; 302 -7.5; 332 -7.2; 365 -7.4; 402 -7.5; 442 -7.5; 486 -7.7; 535 -7.8; 588 -7.5; 647 -7.0; 712 -6.3; 783 -6.3; 861 -6.6; 947 -6.6; 1042 -6.4; 1146 -6.3; 1261 -5.7; 1387 -5.1; 1526 -5.3; 1678 -5.7; 1846 -7.2; 2031 -7.8; 2234 -6.9; 2457 -4.7; 2703 -3.0; 2973 -1.8; 3270 -1.7; 3597 -0.9; 3957 -0.6; 4353 -3.4; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.04 | 6.3 dB  |
| Peaking | 139 Hz  | 0.8  | -4.2 dB |
| Peaking | 208 Hz  | 3.1  | -1.2 dB |
| Peaking | 3482 Hz | 2.21 | 5.3 dB  |
| Peaking | 5643 Hz | 2.7  | 5.9 dB  |
| Peaking | 531 Hz  | 5.07 | -1.0 dB |
| Peaking | 1533 Hz | 2.55 | 2.0 dB  |
| Peaking | 2034 Hz | 2.65 | -3.0 dB |
| Peaking | 2669 Hz | 4.57 | 1.9 dB  |
| Peaking | 8256 Hz | 4.52 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A900X/Audio%20Technica%20ATH-A900X.png)