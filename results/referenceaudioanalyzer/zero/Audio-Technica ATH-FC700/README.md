# Audio-Technica ATH-FC700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.6; 365 -1.2; 402 -1.9; 442 -2.8; 486 -3.7; 535 -4.8; 588 -5.9; 647 -7.1; 712 -8.3; 783 -9.0; 861 -9.4; 947 -9.7; 1042 -9.7; 1146 -9.7; 1261 -9.7; 1387 -9.7; 1526 -9.6; 1678 -9.8; 1846 -10.4; 2031 -11.0; 2234 -11.5; 2457 -11.6; 2703 -11.2; 2973 -10.3; 3270 -8.9; 3597 -7.2; 3957 -6.1; 4353 -5.8; 4788 -5.4; 5267 -7.6; 5793 -11.7; 6373 -14.6; 7010 -18.4; 7711 -20.9; 8482 -19.7; 9330 -15.2; 10263 -11.1; 11289 -10.0; 12418 -11.3; 13660 -11.8; 15026 -9.9; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-FC700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 361 Hz   | 0.03 | 6.6 dB   |
| Peaking | 948 Hz   | 0.87 | -9.0 dB  |
| Peaking | 2350 Hz  | 1.34 | -8.9 dB  |
| Peaking | 7781 Hz  | 1.83 | -19.1 dB |
| Peaking | 13691 Hz | 2.11 | -5.0 dB  |
| Peaking | 19 Hz    | 2.13 | 0.9 dB   |
| Peaking | 328 Hz   | 3.53 | 1.2 dB   |
| Peaking | 3094 Hz  | 5.19 | -1.5 dB  |
| Peaking | 5045 Hz  | 2.36 | 3.7 dB   |
| Peaking | 5892 Hz  | 3.27 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 4.3 dB   |
| Peaking | 250 Hz   | 1.41 | 5.8 dB   |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -13.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-FC700/Audio-Technica%20ATH-FC700.png)