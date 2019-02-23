# Audio Technica ATH-AD700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.7; 87 -2.6; 96 -3.4; 106 -3.7; 116 -4.1; 128 -4.6; 141 -5.0; 155 -5.4; 170 -5.3; 187 -5.8; 206 -6.0; 227 -6.1; 249 -6.3; 274 -6.3; 302 -6.3; 332 -6.3; 365 -6.2; 402 -6.2; 442 -6.2; 486 -6.2; 535 -6.3; 588 -6.2; 647 -6.2; 712 -6.3; 783 -6.7; 861 -7.2; 947 -7.5; 1042 -7.9; 1146 -8.0; 1261 -7.9; 1387 -7.9; 1526 -7.7; 1678 -7.1; 1846 -7.1; 2031 -7.2; 2234 -7.3; 2457 -7.7; 2703 -8.2; 2973 -9.0; 3270 -8.7; 3597 -5.1; 3957 -1.6; 4353 -7.9; 4788 -6.5; 5267 -3.4; 5793 -0.8; 6373 -1.3; 7010 -4.7; 7711 -9.1; 8482 -11.8; 9330 -13.7; 10263 -10.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.48 | 6.7 dB  |
| Peaking | 1614 Hz  | 0.74 | -1.3 dB |
| Peaking | 5812 Hz  | 4.16 | 5.6 dB  |
| Peaking | 6513 Hz  | 6.08 | 3.4 dB  |
| Peaking | 9084 Hz  | 3.25 | -7.9 dB |
| Peaking | 70 Hz    | 5.77 | 1.2 dB  |
| Peaking | 3128 Hz  | 4.83 | -3.0 dB |
| Peaking | 3873 Hz  | 7.04 | 7.4 dB  |
| Peaking | 4342 Hz  | 6.35 | -3.5 dB |
| Peaking | 11375 Hz | 6.93 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)