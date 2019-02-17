# Audio Technica ATH-W5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.6; 274 -0.9; 302 -1.0; 332 -0.8; 365 -0.7; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -1.1; 647 -3.3; 712 -4.8; 783 -5.2; 861 -5.7; 947 -6.3; 1042 -6.7; 1146 -7.2; 1261 -8.0; 1387 -8.8; 1526 -9.3; 1678 -8.6; 1846 -8.4; 2031 -8.3; 2234 -6.6; 2457 -4.4; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -5.9; 4353 -4.2; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.2; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -11.6; 18182 -14.1; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 114 Hz   | 0.07 | 6.3 dB  |
| Peaking | 1519 Hz  | 0.79 | -6.7 dB |
| Peaking | 2987 Hz  | 2.53 | 7.8 dB  |
| Peaking | 5508 Hz  | 2.88 | 6.6 dB  |
| Peaking | 19126 Hz | 0.76 | -9.0 dB |
| Peaking | 569 Hz   | 2.38 | 3.0 dB  |
| Peaking | 688 Hz   | 2.51 | -2.6 dB |
| Peaking | 6792 Hz  | 8.7  | 1.1 dB  |
| Peaking | 9497 Hz  | 7.22 | -4.3 dB |
| Peaking | 13392 Hz | 2.37 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.6 dB  |
| Peaking | 250 Hz   | 1.41 | 4.2 dB  |
| Peaking | 500 Hz   | 1.41 | 5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-W5000/Audio%20Technica%20ATH-W5000.png)