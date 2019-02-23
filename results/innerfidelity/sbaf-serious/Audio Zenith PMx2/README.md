# Audio Zenith PMx2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.0; 25 -2.4; 28 -2.9; 31 -3.2; 34 -3.5; 37 -3.7; 41 -3.8; 45 -3.7; 49 -3.8; 54 -4.5; 60 -5.3; 66 -5.7; 72 -6.1; 79 -6.4; 87 -6.9; 96 -7.5; 106 -7.7; 116 -8.0; 128 -8.4; 141 -8.7; 155 -9.0; 170 -9.0; 187 -9.3; 206 -9.4; 227 -9.3; 249 -9.4; 274 -9.4; 302 -9.4; 332 -8.8; 365 -7.7; 402 -7.5; 442 -7.8; 486 -8.2; 535 -8.5; 588 -8.4; 647 -8.6; 712 -8.7; 783 -8.6; 861 -8.3; 947 -8.3; 1042 -8.1; 1146 -7.6; 1261 -6.7; 1387 -6.5; 1526 -6.7; 1678 -6.5; 1846 -5.8; 2031 -4.6; 2234 -3.9; 2457 -3.2; 2703 -2.8; 2973 -2.5; 3270 -2.7; 3597 -2.9; 3957 -2.6; 4353 -3.1; 4788 -2.3; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.6; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Zenith PMx2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Zenith PMx2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.29 | 5.0 dB  |
| Peaking | 186 Hz  | 0.65 | -3.1 dB |
| Peaking | 827 Hz  | 1.12 | -2.0 dB |
| Peaking | 3007 Hz | 1.33 | 4.0 dB  |
| Peaking | 5708 Hz | 3.16 | 5.9 dB  |
| Peaking | 311 Hz  | 2.62 | -2.2 dB |
| Peaking | 375 Hz  | 1.54 | 2.4 dB  |
| Peaking | 494 Hz  | 1.98 | -1.2 dB |
| Peaking | 6535 Hz | 8.17 | 1.6 dB  |
| Peaking | 8992 Hz | 4.39 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Zenith%20PMx2/Audio%20Zenith%20PMx2.png)