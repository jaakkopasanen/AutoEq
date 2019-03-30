# Audio-Technica ATH-CK7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.4; 31 -2.3; 34 -3.0; 37 -3.7; 41 -4.4; 45 -5.0; 49 -5.4; 54 -6.0; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.1; 96 -7.4; 106 -7.4; 116 -7.4; 128 -7.4; 141 -7.3; 155 -7.1; 170 -6.8; 187 -6.5; 206 -6.2; 227 -6.1; 249 -5.8; 274 -5.6; 302 -5.4; 332 -5.0; 365 -4.6; 402 -4.1; 442 -3.7; 486 -3.2; 535 -2.8; 588 -2.3; 647 -1.9; 712 -1.5; 783 -1.2; 861 -1.0; 947 -0.9; 1042 -0.6; 1146 -0.7; 1261 -0.9; 1387 -1.1; 1526 -1.5; 1678 -1.9; 1846 -2.7; 2031 -3.8; 2234 -5.6; 2457 -7.9; 2703 -11.1; 2973 -14.8; 3270 -17.0; 3597 -16.6; 3957 -14.4; 4353 -12.1; 4788 -11.1; 5267 -11.8; 5793 -13.4; 6373 -13.9; 7010 -12.2; 7711 -9.3; 8482 -8.0; 9330 -8.5; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-CK7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-CK7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.9  | 6.4 dB   |
| Peaking | 99 Hz    | 0.53 | -1.6 dB  |
| Peaking | 1434 Hz  | 0.39 | 7.3 dB   |
| Peaking | 3314 Hz  | 1.69 | -15.2 dB |
| Peaking | 6318 Hz  | 2.45 | -6.9 dB  |
| Peaking | 651 Hz   | 2.89 | 0.2 dB   |
| Peaking | 1806 Hz  | 1.04 | -0.6 dB  |
| Peaking | 2005 Hz  | 2.44 | 1.0 dB   |
| Peaking | 11597 Hz | 7.57 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-CK7/Audio-Technica%20ATH-CK7.png)