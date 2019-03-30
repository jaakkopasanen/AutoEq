# Audio-Technica ATH-A900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -2.0; 37 -3.1; 41 -4.2; 45 -4.9; 49 -5.4; 54 -5.9; 60 -6.4; 66 -6.9; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.0; 106 -7.6; 116 -7.1; 128 -6.7; 141 -6.2; 155 -5.5; 170 -4.5; 187 -3.4; 206 -2.4; 227 -1.7; 249 -1.8; 274 -2.7; 302 -4.4; 332 -6.1; 365 -7.6; 402 -8.3; 442 -8.6; 486 -8.5; 535 -8.3; 588 -8.3; 647 -8.6; 712 -8.8; 783 -8.6; 861 -8.3; 947 -8.6; 1042 -8.9; 1146 -9.1; 1261 -9.3; 1387 -9.6; 1526 -9.5; 1678 -8.9; 1846 -7.9; 2031 -7.1; 2234 -6.7; 2457 -6.3; 2703 -5.6; 2973 -4.8; 3270 -3.7; 3597 -3.3; 3957 -3.9; 4353 -5.1; 4788 -4.6; 5267 -1.1; 5793 -0.5; 6373 -4.0; 7010 -8.6; 7711 -10.6; 8482 -10.9; 9330 -10.8; 10263 -10.7; 11289 -10.4; 12418 -9.9; 13660 -10.3; 15026 -11.7; 16529 -11.7; 18182 -8.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-A900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-A900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.74 | 6.9 dB   |
| Peaking | 235 Hz   | 2.52 | 6.1 dB   |
| Peaking | 4335 Hz  | 0.49 | 16.4 dB  |
| Peaking | 4966 Hz  | 0.19 | -12.7 dB |
| Peaking | 16242 Hz | 3.48 | -1.9 dB  |
| Peaking | 36 Hz    | 2.97 | 1.2 dB   |
| Peaking | 89 Hz    | 2.19 | -2.0 dB  |
| Peaking | 4629 Hz  | 2.78 | -7.4 dB  |
| Peaking | 5774 Hz  | 1.55 | 10.4 dB  |
| Peaking | 7255 Hz  | 2.02 | -7.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-A900/Audio-Technica%20ATH-A900.png)