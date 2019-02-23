# Audio Technica ATH-AD700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.1; 60 -1.7; 66 -1.8; 72 -2.1; 79 -2.8; 87 -3.8; 96 -4.5; 106 -4.9; 116 -5.3; 128 -5.8; 141 -6.2; 155 -6.4; 170 -6.6; 187 -6.8; 206 -7.0; 227 -7.1; 249 -7.3; 274 -7.1; 302 -7.1; 332 -7.0; 365 -7.1; 402 -7.0; 442 -6.9; 486 -7.1; 535 -7.2; 588 -7.0; 647 -7.1; 712 -7.4; 783 -7.4; 861 -8.0; 947 -8.4; 1042 -8.8; 1146 -9.1; 1261 -9.3; 1387 -9.7; 1526 -9.8; 1678 -9.3; 1846 -9.3; 2031 -9.0; 2234 -8.4; 2457 -7.7; 2703 -7.6; 2973 -7.4; 3270 -7.8; 3597 -4.9; 3957 -4.4; 4353 -8.2; 4788 -7.6; 5267 -3.8; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.1; 10263 -9.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.63 | 6.8 dB  |
| Peaking | 1547 Hz |  0.61 | -2.9 dB |
| Peaking | 3774 Hz | 10.53 | 4.1 dB  |
| Peaking | 6081 Hz |  4.14 | 7.2 dB  |
| Peaking | 9724 Hz |  5.58 | -3.7 dB |
| Peaking | 36 Hz   |  3.22 | -0.7 dB |
| Peaking | 71 Hz   |  2.77 | 1.1 dB  |
| Peaking | 193 Hz  |  1.17 | -1.0 dB |
| Peaking | 4561 Hz |  5.8  | -4.5 dB |
| Peaking | 4649 Hz |  2.09 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)