# Audio Technica ATH-AD700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -1.6; 96 -2.3; 106 -2.7; 116 -3.1; 128 -3.6; 141 -4.0; 155 -4.2; 170 -4.4; 187 -4.6; 206 -4.8; 227 -4.9; 249 -5.0; 274 -4.9; 302 -4.9; 332 -4.8; 365 -4.9; 402 -4.8; 442 -4.7; 486 -4.9; 535 -5.0; 588 -4.8; 647 -4.9; 712 -5.2; 783 -5.2; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.5; 1526 -7.5; 1678 -7.1; 1846 -7.1; 2031 -6.8; 2234 -6.2; 2457 -5.4; 2703 -5.4; 2973 -5.2; 3270 -5.6; 3597 -2.7; 3957 -2.2; 4353 -6.0; 4788 -5.4; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.24 | 6.4 dB  |
| Peaking | 149 Hz  | 1.05 | -1.9 dB |
| Peaking | 554 Hz  | 1.8  | 1.2 dB  |
| Peaking | 3718 Hz | 6.84 | 4.7 dB  |
| Peaking | 5934 Hz | 3.79 | 6.7 dB  |
| Peaking | 164 Hz  | 6.66 | 0.2 dB  |
| Peaking | 1501 Hz | 2.19 | -1.3 dB |
| Peaking | 2630 Hz | 4.24 | 1.2 dB  |
| Peaking | 3307 Hz | 7.02 | -0.5 dB |
| Peaking | 9607 Hz | 4.14 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)