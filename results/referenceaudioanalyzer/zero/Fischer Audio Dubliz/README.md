# Fischer Audio Dubliz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.5; 23 -18.5; 25 -18.5; 28 -18.4; 31 -18.3; 34 -18.1; 37 -17.9; 41 -17.7; 45 -17.5; 49 -17.2; 54 -17.0; 60 -16.6; 66 -16.2; 72 -15.8; 79 -15.5; 87 -15.0; 96 -14.5; 106 -13.9; 116 -13.4; 128 -12.8; 141 -12.2; 155 -11.6; 170 -10.9; 187 -10.3; 206 -9.6; 227 -8.9; 249 -8.3; 274 -7.6; 302 -7.0; 332 -6.4; 365 -5.7; 402 -5.1; 442 -4.6; 486 -4.1; 535 -3.6; 588 -3.2; 647 -2.9; 712 -2.7; 783 -2.6; 861 -2.1; 947 -1.4; 1042 -1.5; 1146 -1.2; 1261 -0.5; 1387 -1.3; 1526 -3.0; 1678 -4.7; 1846 -6.8; 2031 -9.2; 2234 -11.2; 2457 -12.2; 2703 -12.8; 2973 -13.3; 3270 -13.3; 3597 -12.2; 3957 -10.0; 4353 -8.0; 4788 -6.8; 5267 -5.3; 5793 -4.3; 6373 -4.9; 7010 -4.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Dubliz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Dubliz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.42 | -10.7 dB |
| Peaking | 59 Hz   | 0.36 | -8.4 dB  |
| Peaking | 1388 Hz | 0.54 | 13.2 dB  |
| Peaking | 2686 Hz | 0.63 | -16.2 dB |
| Peaking | 5664 Hz | 1.16 | 6.6 dB   |
| Peaking | 16 Hz   | 0.3  | 0.4 dB   |
| Peaking | 1275 Hz | 1.56 | -1.7 dB  |
| Peaking | 1323 Hz | 3.55 | 2.4 dB   |
| Peaking | 3204 Hz | 2.2  | 1.3 dB   |
| Peaking | 3379 Hz | 4.83 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Dubliz/Fischer%20Audio%20Dubliz.png)