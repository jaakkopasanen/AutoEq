# Audio Technica ATH-ESW9A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.6; 60 -3.2; 66 -3.0; 72 -2.4; 79 -3.0; 87 -3.3; 96 -3.5; 106 -3.7; 116 -3.5; 128 -2.6; 141 -3.0; 155 -3.4; 170 -3.6; 187 -3.7; 206 -3.2; 227 -3.3; 249 -3.8; 274 -4.4; 302 -4.6; 332 -4.1; 365 -3.7; 402 -3.4; 442 -3.1; 486 -3.2; 535 -3.0; 588 -2.8; 647 -3.3; 712 -4.5; 783 -5.3; 861 -5.6; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -7.8; 1387 -8.3; 1526 -8.8; 1678 -8.9; 1846 -8.3; 2031 -7.2; 2234 -6.0; 2457 -4.8; 2703 -2.8; 2973 -1.0; 3270 -0.5; 3597 -1.0; 3957 -1.3; 4353 -2.9; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ESW9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ESW9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.49 | 6.1 dB  |
| Peaking | 175 Hz  | 0.74 | 2.6 dB  |
| Peaking | 527 Hz  | 2.11 | 3.4 dB  |
| Peaking | 3311 Hz | 3.06 | 6.0 dB  |
| Peaking | 5584 Hz | 2.56 | 6.3 dB  |
| Peaking | 649 Hz  | 6.84 | 1.1 dB  |
| Peaking | 856 Hz  | 3.56 | 0.5 dB  |
| Peaking | 1700 Hz | 1.42 | -3.8 dB |
| Peaking | 2513 Hz | 1.49 | 2.0 dB  |
| Peaking | 8258 Hz | 4.45 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ESW9A/Audio%20Technica%20ATH-ESW9A.png)