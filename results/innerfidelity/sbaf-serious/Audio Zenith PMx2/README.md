# Audio Zenith PMx2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.4; 34 -1.7; 37 -1.9; 41 -2.0; 45 -1.9; 49 -2.1; 54 -2.7; 60 -3.5; 66 -3.9; 72 -4.3; 79 -4.7; 87 -5.1; 96 -5.7; 106 -5.9; 116 -6.2; 128 -6.6; 141 -6.9; 155 -7.2; 170 -7.2; 187 -7.5; 206 -7.6; 227 -7.5; 249 -7.6; 274 -7.6; 302 -7.6; 332 -7.0; 365 -5.9; 402 -5.7; 442 -6.0; 486 -6.4; 535 -6.7; 588 -6.6; 647 -6.8; 712 -6.9; 783 -6.8; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -5.8; 1261 -4.9; 1387 -4.7; 1526 -4.9; 1678 -4.7; 1846 -4.0; 2031 -2.8; 2234 -2.1; 2457 -1.4; 2703 -1.0; 2973 -0.7; 3270 -0.9; 3597 -1.1; 3957 -0.8; 4353 -1.3; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Zenith PMx2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Zenith PMx2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.9  | 5.4 dB  |
| Peaking | 48 Hz   | 1.06 | 2.9 dB  |
| Peaking | 204 Hz  | 1.21 | -1.4 dB |
| Peaking | 2977 Hz | 1.11 | 5.7 dB  |
| Peaking | 5558 Hz | 2.59 | 5.0 dB  |
| Peaking | 397 Hz  | 5.9  | 1.3 dB  |
| Peaking | 755 Hz  | 2.56 | -0.7 dB |
| Peaking | 4431 Hz | 2.75 | 1.2 dB  |
| Peaking | 6554 Hz | 4.89 | 3.7 dB  |
| Peaking | 6898 Hz | 1.33 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Zenith%20PMx2/Audio%20Zenith%20PMx2.png)