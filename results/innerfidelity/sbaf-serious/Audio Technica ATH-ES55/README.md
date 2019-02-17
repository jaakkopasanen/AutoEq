# Audio Technica ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.9; 128 -2.0; 141 -2.6; 155 -3.0; 170 -2.9; 187 -3.6; 206 -3.9; 227 -4.1; 249 -4.3; 274 -4.0; 302 -3.5; 332 -3.6; 365 -4.0; 402 -4.0; 442 -3.8; 486 -3.9; 535 -3.8; 588 -3.7; 647 -4.1; 712 -4.7; 783 -5.1; 861 -5.8; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -7.9; 1526 -8.5; 1678 -8.7; 1846 -8.1; 2031 -7.1; 2234 -5.6; 2457 -3.7; 2703 -2.3; 2973 -1.1; 3270 -1.0; 3597 -1.4; 3957 -1.1; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -7.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.27 | 6.4 dB  |
| Peaking | 541 Hz   | 1.16 | 2.3 dB  |
| Peaking | 1738 Hz  | 1.33 | -4.1 dB |
| Peaking | 3119 Hz  | 1.27 | 6.1 dB  |
| Peaking | 5498 Hz  | 2.38 | 5.2 dB  |
| Peaking | 105 Hz   | 5.62 | 1.1 dB  |
| Peaking | 6535 Hz  | 6.59 | 2.4 dB  |
| Peaking | 7771 Hz  | 2.29 | -1.6 dB |
| Peaking | 15885 Hz | 3.36 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ES55/Audio%20Technica%20ATH-ES55.png)