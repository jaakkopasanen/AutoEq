# Audio-Technica ATH-SJ1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.7; 206 -1.1; 227 -1.4; 249 -1.6; 274 -1.8; 302 -1.9; 332 -2.2; 365 -2.5; 402 -3.2; 442 -4.6; 486 -6.5; 535 -8.9; 588 -11.5; 647 -13.8; 712 -15.3; 783 -16.2; 861 -16.6; 947 -16.8; 1042 -17.0; 1146 -17.4; 1261 -17.4; 1387 -17.2; 1526 -16.2; 1678 -14.5; 1846 -12.3; 2031 -9.6; 2234 -6.7; 2457 -3.9; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -6.1; 5793 -9.9; 6373 -11.6; 7010 -14.9; 7711 -16.7; 8482 -14.8; 9330 -10.6; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-SJ1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-SJ1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.15 | 7.1 dB   |
| Peaking | 1078 Hz  | 0.7  | -15.3 dB |
| Peaking | 2909 Hz  | 1.82 | 9.9 dB   |
| Peaking | 4435 Hz  | 2.72 | 7.5 dB   |
| Peaking | 7505 Hz  | 2.31 | -11.2 dB |
| Peaking | 18 Hz    | 2.51 | 1.8 dB   |
| Peaking | 424 Hz   | 1.26 | 7.4 dB   |
| Peaking | 566 Hz   | 0.73 | -6.2 dB  |
| Peaking | 1022 Hz  | 2.68 | 3.9 dB   |
| Peaking | 11165 Hz | 3.61 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 4.6 dB   |
| Peaking | 250 Hz   | 1.41 | 5.6 dB   |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -14.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-SJ1/Audio-Technica%20ATH-SJ1.png)