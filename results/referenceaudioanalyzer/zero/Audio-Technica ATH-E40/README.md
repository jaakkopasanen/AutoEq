# Audio-Technica ATH-E40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.4; 25 -11.3; 28 -11.2; 31 -11.1; 34 -11.1; 37 -11.0; 41 -10.9; 45 -10.8; 49 -10.6; 54 -10.5; 60 -10.4; 66 -10.2; 72 -10.1; 79 -9.9; 87 -9.7; 96 -9.5; 106 -9.3; 116 -9.0; 128 -8.8; 141 -8.5; 155 -8.3; 170 -8.0; 187 -7.7; 206 -7.5; 227 -7.2; 249 -7.1; 274 -6.8; 302 -6.5; 332 -6.2; 365 -5.9; 402 -5.6; 442 -5.3; 486 -4.9; 535 -4.7; 588 -4.5; 647 -4.3; 712 -4.3; 783 -4.3; 861 -4.6; 947 -4.9; 1042 -5.4; 1146 -6.1; 1261 -7.1; 1387 -8.5; 1526 -10.5; 1678 -13.2; 1846 -16.2; 2031 -17.8; 2234 -17.1; 2457 -14.3; 2703 -11.4; 2973 -9.9; 3270 -10.1; 3597 -11.1; 3957 -10.6; 4353 -8.0; 4788 -3.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-E40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-E40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.49 | -4.8 dB  |
| Peaking | 96 Hz   | 1.17 | -1.8 dB  |
| Peaking | 2070 Hz | 2.8  | -12.4 dB |
| Peaking | 3880 Hz | 2.53 | -5.6 dB  |
| Peaking | 5471 Hz | 2.37 | 8.4 dB   |
| Peaking | 751 Hz  | 0.98 | 2.8 dB   |
| Peaking | 1681 Hz | 4.96 | -2.3 dB  |
| Peaking | 2439 Hz | 9.96 | -1.4 dB  |
| Peaking | 6562 Hz | 6.79 | 2.6 dB   |
| Peaking | 7534 Hz | 2.08 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-E40/Audio-Technica%20ATH-E40.png)