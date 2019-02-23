# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.0; 28 -10.3; 31 -10.4; 34 -10.5; 37 -10.5; 41 -10.5; 45 -10.3; 49 -10.0; 54 -9.8; 60 -9.4; 66 -8.2; 72 -6.5; 79 -5.2; 87 -6.9; 96 -9.9; 106 -11.6; 116 -10.5; 128 -11.1; 141 -11.8; 155 -10.8; 170 -9.4; 187 -9.8; 206 -8.5; 227 -7.1; 249 -5.9; 274 -4.8; 302 -3.8; 332 -3.4; 365 -3.3; 402 -3.9; 442 -4.6; 486 -5.6; 535 -6.2; 588 -6.7; 647 -7.0; 712 -7.3; 783 -7.4; 861 -7.2; 947 -7.2; 1042 -7.0; 1146 -6.5; 1261 -7.2; 1387 -7.8; 1526 -8.9; 1678 -9.8; 1846 -10.0; 2031 -9.5; 2234 -8.7; 2457 -7.6; 2703 -6.5; 2973 -4.7; 3270 -3.1; 3597 -2.0; 3957 -3.5; 4353 -6.3; 4788 -3.6; 5267 -0.5; 5793 -1.7; 6373 -2.2; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.08 | -4.5 dB |
| Peaking | 134 Hz  | 2.29 | -5.4 dB |
| Peaking | 1863 Hz | 2.16 | -4.0 dB |
| Peaking | 3463 Hz | 4.24 | 4.5 dB  |
| Peaking | 5645 Hz | 3.08 | 5.9 dB  |
| Peaking | 60 Hz   | 2.76 | -2.0 dB |
| Peaking | 78 Hz   | 2.89 | 3.6 dB  |
| Peaking | 101 Hz  | 6.19 | -3.5 dB |
| Peaking | 191 Hz  | 5.16 | -2.1 dB |
| Peaking | 339 Hz  | 2.25 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)