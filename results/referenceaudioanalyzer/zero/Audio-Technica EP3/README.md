# Audio-Technica EP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -5.2; 28 -5.8; 31 -6.3; 34 -6.7; 37 -7.0; 41 -7.3; 45 -7.6; 49 -7.9; 54 -8.1; 60 -8.2; 66 -8.3; 72 -8.5; 79 -8.6; 87 -8.6; 96 -8.6; 106 -8.6; 116 -8.6; 128 -8.6; 141 -8.6; 155 -8.4; 170 -8.2; 187 -8.0; 206 -7.8; 227 -7.5; 249 -7.2; 274 -6.9; 302 -6.5; 332 -6.2; 365 -5.8; 402 -5.4; 442 -4.8; 486 -4.3; 535 -3.7; 588 -3.0; 647 -2.3; 712 -1.6; 783 -0.9; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.8; 1846 -1.2; 2031 -1.8; 2234 -3.0; 2457 -4.7; 2703 -8.3; 2973 -13.2; 3270 -17.2; 3597 -18.6; 3957 -17.5; 4353 -15.1; 4788 -13.8; 5267 -15.1; 5793 -16.2; 6373 -14.8; 7010 -9.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica EP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica EP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 1.15 | 3.7 dB   |
| Peaking | 125 Hz   | 0.28 | -2.5 dB  |
| Peaking | 1939 Hz  | 0.34 | 10.0 dB  |
| Peaking | 3555 Hz  | 1.6  | -20.2 dB |
| Peaking | 5806 Hz  | 2.85 | -9.4 dB  |
| Peaking | 1343 Hz  | 3.26 | -0.8 dB  |
| Peaking | 2408 Hz  | 2.79 | 1.2 dB   |
| Peaking | 2981 Hz  | 6.75 | -2.2 dB  |
| Peaking | 7726 Hz  | 8.07 | 2.3 dB   |
| Peaking | 11122 Hz | 6.9  | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -14.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20EP3/Audio-Technica%20EP3.png)