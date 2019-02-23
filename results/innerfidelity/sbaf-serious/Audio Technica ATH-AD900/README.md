# Audio Technica ATH-AD900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.1; 72 -1.6; 79 -1.8; 87 -1.9; 96 -2.8; 106 -3.3; 116 -3.9; 128 -4.6; 141 -5.3; 155 -5.8; 170 -5.9; 187 -5.7; 206 -5.5; 227 -5.7; 249 -5.9; 274 -6.0; 302 -6.1; 332 -6.1; 365 -6.2; 402 -6.2; 442 -6.1; 486 -6.2; 535 -6.3; 588 -6.1; 647 -6.3; 712 -6.4; 783 -6.2; 861 -6.6; 947 -6.9; 1042 -7.2; 1146 -7.5; 1261 -8.1; 1387 -9.0; 1526 -9.9; 1678 -9.9; 1846 -8.2; 2031 -6.8; 2234 -5.8; 2457 -4.9; 2703 -5.4; 2973 -5.8; 3270 -5.1; 3597 -7.5; 3957 -10.8; 4353 -12.3; 4788 -10.9; 5267 -7.8; 5793 -6.3; 6373 -5.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.45 | 6.6 dB  |
| Peaking | 1600 Hz | 2.13 | -4.9 dB |
| Peaking | 2781 Hz | 0.87 | 3.1 dB  |
| Peaking | 4332 Hz | 2.98 | -7.9 dB |
| Peaking | 6723 Hz | 5.13 | 2.9 dB  |
| Peaking | 40 Hz   | 2.68 | -0.8 dB |
| Peaking | 88 Hz   | 1.46 | 0.7 dB  |
| Peaking | 152 Hz  | 2.71 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)