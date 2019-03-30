# Audio-Technica ATH-AD500X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.4; 25 -2.1; 28 -2.9; 31 -3.7; 34 -4.2; 37 -4.8; 41 -5.3; 45 -5.8; 49 -6.2; 54 -6.6; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.7; 96 -7.8; 106 -8.0; 116 -8.0; 128 -8.0; 141 -8.0; 155 -8.0; 170 -8.0; 187 -7.7; 206 -7.7; 227 -7.6; 249 -7.4; 274 -7.2; 302 -7.0; 332 -7.1; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.7; 588 -6.4; 647 -6.3; 712 -6.2; 783 -6.4; 861 -6.6; 947 -6.8; 1042 -7.0; 1146 -7.2; 1261 -7.4; 1387 -7.5; 1526 -7.7; 1678 -7.5; 1846 -6.7; 2031 -5.7; 2234 -4.6; 2457 -3.8; 2703 -3.2; 2973 -1.5; 3270 -0.5; 3597 -3.5; 3957 -8.6; 4353 -10.2; 4788 -8.9; 5267 -8.0; 5793 -9.3; 6373 -8.4; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD500X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD500X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.93 | 6.4 dB   |
| Peaking | 113 Hz  | 0.56 | -1.8 dB  |
| Peaking | 1544 Hz | 2.23 | -2.0 dB  |
| Peaking | 3400 Hz | 1.85 | 11.9 dB  |
| Peaking | 4055 Hz | 1.97 | -10.5 dB |
| Peaking | 680 Hz  | 4.73 | 0.5 dB   |
| Peaking | 2304 Hz | 6.33 | 0.6 dB   |
| Peaking | 6115 Hz | 6.09 | -2.8 dB  |
| Peaking | 6953 Hz | 7.54 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD500X/Audio-Technica%20ATH-AD500X.png)