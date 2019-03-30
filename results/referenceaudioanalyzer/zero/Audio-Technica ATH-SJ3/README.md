# Audio-Technica ATH-SJ3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -1.0; 116 -1.4; 128 -1.7; 141 -2.1; 155 -2.3; 170 -2.6; 187 -2.6; 206 -2.6; 227 -2.6; 249 -2.8; 274 -3.1; 302 -3.6; 332 -4.0; 365 -4.3; 402 -4.7; 442 -5.0; 486 -5.4; 535 -5.9; 588 -6.7; 647 -7.4; 712 -8.0; 783 -8.6; 861 -9.1; 947 -9.5; 1042 -9.8; 1146 -10.2; 1261 -10.8; 1387 -11.4; 1526 -11.8; 1678 -12.0; 1846 -12.0; 2031 -11.4; 2234 -9.9; 2457 -8.2; 2703 -6.2; 2973 -4.2; 3270 -2.1; 3597 -1.4; 3957 -1.9; 4353 -0.7; 4788 -0.5; 5267 -3.6; 5793 -6.2; 6373 -9.3; 7010 -14.4; 7711 -18.3; 8482 -17.9; 9330 -12.8; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-SJ3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-SJ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.09 | 6.0 dB   |
| Peaking | 1874 Hz  | 0.62 | -7.1 dB  |
| Peaking | 3079 Hz  | 2.24 | 4.3 dB   |
| Peaking | 4445 Hz  | 1.29 | 8.9 dB   |
| Peaking | 7848 Hz  | 2.73 | -14.9 dB |
| Peaking | 92 Hz    | 1.74 | 0.7 dB   |
| Peaking | 159 Hz   | 1.26 | -1.2 dB  |
| Peaking | 234 Hz   | 1.1  | 0.6 dB   |
| Peaking | 9003 Hz  | 5.88 | -3.3 dB  |
| Peaking | 10543 Hz | 2.54 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 4.8 dB   |
| Peaking | 125 Hz   | 1.41 | 3.7 dB   |
| Peaking | 250 Hz   | 1.41 | 2.9 dB   |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.9 dB |
| Peaking | 16000 Hz | 1.41 | 1.7 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-SJ3/Audio-Technica%20ATH-SJ3.png)