# Audio-Technica ATH-AD1000PRM Premium
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.3; 72 -1.7; 79 -2.2; 87 -2.6; 96 -2.9; 106 -3.2; 116 -3.4; 128 -3.7; 141 -4.0; 155 -4.1; 170 -4.2; 187 -4.4; 206 -4.5; 227 -4.8; 249 -5.1; 274 -5.4; 302 -5.4; 332 -5.4; 365 -5.4; 402 -5.4; 442 -5.2; 486 -5.1; 535 -5.1; 588 -5.4; 647 -5.4; 712 -5.4; 783 -5.4; 861 -5.4; 947 -5.7; 1042 -5.7; 1146 -5.7; 1261 -5.9; 1387 -6.1; 1526 -6.0; 1678 -6.1; 1846 -6.4; 2031 -6.6; 2234 -6.9; 2457 -7.3; 2703 -8.0; 2973 -9.5; 3270 -12.6; 3597 -15.5; 3957 -16.0; 4353 -14.0; 4788 -11.4; 5267 -9.4; 5793 -7.2; 6373 -4.4; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -9.4; 10263 -10.2; 11289 -10.4; 12418 -10.2; 13660 -9.2; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD1000PRM Premium GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD1000PRM Premium ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.33 | 6.2 dB   |
| Peaking | 1403 Hz  | 0.19 | 1.1 dB   |
| Peaking | 3890 Hz  | 2.17 | -11.0 dB |
| Peaking | 6749 Hz  | 3.89 | 5.0 dB   |
| Peaking | 11251 Hz | 1.35 | -4.4 dB  |
| Peaking | 2675 Hz  | 6.46 | 0.7 dB   |
| Peaking | 16059 Hz | 4.05 | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD1000PRM%20Premium/Audio-Technica%20ATH-AD1000PRM%20Premium.png)