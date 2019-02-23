# Audio Technica ATH-ESW9A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.1; 37 -3.0; 41 -3.9; 45 -4.5; 49 -5.1; 54 -5.6; 60 -6.2; 66 -6.0; 72 -5.4; 79 -6.1; 87 -6.4; 96 -6.6; 106 -6.8; 116 -6.6; 128 -5.7; 141 -6.0; 155 -6.5; 170 -6.6; 187 -6.8; 206 -6.3; 227 -6.4; 249 -6.8; 274 -7.4; 302 -7.6; 332 -7.2; 365 -6.8; 402 -6.5; 442 -6.2; 486 -6.2; 535 -6.1; 588 -5.9; 647 -6.3; 712 -7.6; 783 -8.3; 861 -8.7; 947 -9.2; 1042 -9.8; 1146 -10.4; 1261 -10.8; 1387 -11.3; 1526 -11.9; 1678 -12.0; 1846 -11.4; 2031 -10.3; 2234 -9.0; 2457 -7.8; 2703 -5.8; 2973 -4.1; 3270 -3.6; 3597 -4.1; 3957 -4.4; 4353 -5.9; 4788 -4.7; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -6.8; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.1; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ESW9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ESW9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.28 | 6.6 dB  |
| Peaking | 132 Hz  | 6.66 | 0.5 dB  |
| Peaking | 1599 Hz | 1.12 | -5.9 dB |
| Peaking | 3158 Hz | 2.53 | 4.5 dB  |
| Peaking | 5719 Hz | 4    | 7.0 dB  |
| Peaking | 104 Hz  | 4.69 | -0.7 dB |
| Peaking | 296 Hz  | 5.63 | -1.2 dB |
| Peaking | 565 Hz  | 3.64 | 1.5 dB  |
| Peaking | 7431 Hz | 9.81 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ESW9A/Audio%20Technica%20ATH-ESW9A.png)