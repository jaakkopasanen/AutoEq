# Audio Technica ATH-A1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.6; 28 -2.5; 31 -3.4; 34 -4.2; 37 -4.8; 41 -5.5; 45 -6.1; 49 -6.6; 54 -7.0; 60 -7.3; 66 -7.4; 72 -7.1; 79 -6.7; 87 -6.7; 96 -6.5; 106 -7.0; 116 -8.1; 128 -8.7; 141 -8.6; 155 -7.7; 170 -6.8; 187 -7.5; 206 -7.0; 227 -6.2; 249 -5.6; 274 -5.3; 302 -5.4; 332 -5.3; 365 -5.4; 402 -5.6; 442 -5.7; 486 -5.9; 535 -6.1; 588 -5.9; 647 -5.9; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -6.4; 1387 -7.0; 1526 -6.9; 1678 -6.6; 1846 -8.1; 2031 -10.7; 2234 -8.3; 2457 -5.5; 2703 -2.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -9.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.83 | 5.9 dB  |
| Peaking | 131 Hz   | 3.46 | -2.5 dB |
| Peaking | 2079 Hz  | 3.87 | -6.3 dB |
| Peaking | 3296 Hz  | 1.54 | 6.6 dB  |
| Peaking | 5737 Hz  | 3.06 | 5.3 dB  |
| Peaking | 60 Hz    | 3.01 | -1.2 dB |
| Peaking | 282 Hz   | 4.07 | 1.0 dB  |
| Peaking | 398 Hz   | 1.86 | 0.9 dB  |
| Peaking | 8233 Hz  | 4.59 | -1.2 dB |
| Peaking | 18389 Hz | 1.98 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A1000X/Audio%20Technica%20ATH-A1000X.png)