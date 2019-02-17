# Audio Technical ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.7; 141 -1.3; 155 -1.7; 170 -2.1; 187 -2.6; 206 -2.9; 227 -3.2; 249 -3.3; 274 -2.9; 302 -2.7; 332 -2.8; 365 -3.3; 402 -3.3; 442 -2.9; 486 -3.1; 535 -3.1; 588 -3.0; 647 -3.6; 712 -4.6; 783 -5.2; 861 -5.9; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.0; 1526 -8.6; 1678 -8.7; 1846 -8.5; 2031 -7.5; 2234 -6.2; 2457 -4.3; 2703 -2.8; 2973 -1.5; 3270 -1.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -7.2; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technical ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.1  | 6.0 dB  |
| Peaking | 119 Hz  | 0.78 | 2.7 dB  |
| Peaking | 469 Hz  | 0.94 | 3.1 dB  |
| Peaking | 1663 Hz | 1.51 | -4.1 dB |
| Peaking | 4099 Hz | 0.96 | 7.0 dB  |
| Peaking | 300 Hz  | 7.66 | 0.7 dB  |
| Peaking | 2855 Hz | 3.08 | 2.4 dB  |
| Peaking | 3405 Hz | 1.29 | -1.5 dB |
| Peaking | 6347 Hz | 2.52 | 5.1 dB  |
| Peaking | 7232 Hz | 1.49 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-ES55/Audio%20Technical%20ATH-ES55.png)