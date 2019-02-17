# Audio Technica ATH-AD900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -0.9; 72 -1.3; 79 -1.1; 87 -0.7; 96 -2.5; 106 -3.1; 116 -3.3; 128 -4.0; 141 -4.6; 155 -5.0; 170 -5.2; 187 -5.4; 206 -5.5; 227 -5.7; 249 -5.9; 274 -5.8; 302 -5.7; 332 -5.5; 365 -5.5; 402 -5.5; 442 -5.6; 486 -5.7; 535 -5.7; 588 -5.7; 647 -5.6; 712 -5.6; 783 -5.7; 861 -6.2; 947 -6.2; 1042 -6.6; 1146 -6.7; 1261 -7.4; 1387 -8.5; 1526 -10.5; 1678 -10.1; 1846 -8.4; 2031 -6.8; 2234 -5.6; 2457 -4.2; 2703 -5.2; 2973 -5.7; 3270 -4.7; 3597 -8.6; 3957 -11.4; 4353 -12.4; 4788 -10.1; 5267 -6.9; 5793 -4.1; 6373 -3.8; 7010 -4.1; 7711 -6.2; 8482 -7.1; 9330 -9.6; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.4  | 6.5 dB  |
| Peaking | 1596 Hz | 2.4  | -4.6 dB |
| Peaking | 3928 Hz | 0.36 | 2.6 dB  |
| Peaking | 4245 Hz | 2.87 | -7.3 dB |
| Peaking | 8840 Hz | 2.46 | -2.7 dB |
| Peaking | 1683 Hz | 1.35 | -3.3 dB |
| Peaking | 2198 Hz | 0.62 | 2.9 dB  |
| Peaking | 4615 Hz | 1.62 | -3.8 dB |
| Peaking | 6034 Hz | 2.09 | 3.5 dB  |
| Peaking | 9584 Hz | 5.97 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)