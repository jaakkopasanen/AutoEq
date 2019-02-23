# Audio Technica ATH-AD900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.2; 72 -1.6; 79 -1.3; 87 -0.8; 96 -2.7; 106 -3.3; 116 -3.6; 128 -4.2; 141 -4.8; 155 -5.3; 170 -5.5; 187 -5.7; 206 -5.7; 227 -5.9; 249 -6.1; 274 -6.1; 302 -5.9; 332 -5.8; 365 -5.8; 402 -5.7; 442 -5.8; 486 -6.0; 535 -5.9; 588 -5.9; 647 -5.9; 712 -5.8; 783 -6.0; 861 -6.4; 947 -6.4; 1042 -6.8; 1146 -7.0; 1261 -7.6; 1387 -8.7; 1526 -10.8; 1678 -10.3; 1846 -8.7; 2031 -7.1; 2234 -5.8; 2457 -4.4; 2703 -5.5; 2973 -5.9; 3270 -4.9; 3597 -8.8; 3957 -11.6; 4353 -12.6; 4788 -10.4; 5267 -7.1; 5793 -4.4; 6373 -4.0; 7010 -4.2; 7711 -6.2; 8482 -7.2; 9330 -9.9; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 38 Hz    |  0.42 | 6.6 dB   |
| Peaking | 1611 Hz  |  2.68 | -6.1 dB  |
| Peaking | 4281 Hz  |  2.29 | -13.1 dB |
| Peaking | 4584 Hz  |  0.57 | 6.8 dB   |
| Peaking | 9342 Hz  |  2.74 | -5.7 dB  |
| Peaking | 38 Hz    |  2.88 | -0.7 dB  |
| Peaking | 85 Hz    |  7.39 | 1.7 dB   |
| Peaking | 168 Hz   |  2.09 | -0.7 dB  |
| Peaking | 6634 Hz  | 10.26 | 0.9 dB   |
| Peaking | 14343 Hz |  1.67 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)