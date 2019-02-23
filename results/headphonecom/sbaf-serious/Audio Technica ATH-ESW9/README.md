# Audio Technica ATH-ESW9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.8; 45 -2.5; 49 -3.1; 54 -3.8; 60 -4.5; 66 -4.3; 72 -3.9; 79 -4.6; 87 -5.1; 96 -5.3; 106 -5.5; 116 -5.5; 128 -4.7; 141 -5.2; 155 -5.5; 170 -5.5; 187 -5.4; 206 -5.5; 227 -5.9; 249 -6.2; 274 -6.7; 302 -6.9; 332 -6.3; 365 -6.0; 402 -5.6; 442 -5.5; 486 -5.4; 535 -5.5; 588 -5.6; 647 -6.5; 712 -7.9; 783 -8.8; 861 -9.3; 947 -9.9; 1042 -10.4; 1146 -11.0; 1261 -11.3; 1387 -11.8; 1526 -12.4; 1678 -12.4; 1846 -11.7; 2031 -10.8; 2234 -9.5; 2457 -8.0; 2703 -6.0; 2973 -4.3; 3270 -3.6; 3597 -3.9; 3957 -4.5; 4353 -5.8; 4788 -4.3; 5267 -1.9; 5793 -0.5; 6373 -2.7; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -7.9; 16529 -8.1; 18182 -10.3; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ESW9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ESW9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.35 | 6.5 dB  |
| Peaking | 1581 Hz  |  1.13 | -6.5 dB |
| Peaking | 3200 Hz  |  2.42 | 4.5 dB  |
| Peaking | 5704 Hz  |  4.39 | 6.7 dB  |
| Peaking | 18330 Hz |  1.2  | -3.9 dB |
| Peaking | 181 Hz   |  2.93 | 0.6 dB  |
| Peaking | 549 Hz   |  1.88 | 2.2 dB  |
| Peaking | 827 Hz   |  2.21 | -1.5 dB |
| Peaking | 6777 Hz  | 18.7  | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ESW9/Audio%20Technica%20ATH-ESW9.png)