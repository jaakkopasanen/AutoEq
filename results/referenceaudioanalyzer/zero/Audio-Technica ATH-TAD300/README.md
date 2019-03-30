# Audio-Technica ATH-TAD300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.1; 34 -1.9; 37 -2.8; 41 -3.7; 45 -4.4; 49 -5.2; 54 -6.1; 60 -6.8; 66 -7.3; 72 -7.8; 79 -8.2; 87 -8.5; 96 -8.5; 106 -8.5; 116 -8.5; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.8; 187 -7.6; 206 -7.6; 227 -7.4; 249 -7.1; 274 -6.9; 302 -6.7; 332 -6.6; 365 -6.4; 402 -6.2; 442 -6.2; 486 -6.2; 535 -6.2; 588 -5.9; 647 -6.0; 712 -6.2; 783 -6.0; 861 -5.9; 947 -6.0; 1042 -6.3; 1146 -6.1; 1261 -5.8; 1387 -5.4; 1526 -5.2; 1678 -5.7; 1846 -7.2; 2031 -8.1; 2234 -7.8; 2457 -6.6; 2703 -5.4; 2973 -4.3; 3270 -3.0; 3597 -1.4; 3957 -1.4; 4353 -3.4; 4788 -3.2; 5267 -5.1; 5793 -9.0; 6373 -10.9; 7010 -12.1; 7711 -11.3; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-TAD300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-TAD300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.79 | 6.7 dB   |
| Peaking | 88 Hz   | 0.69 | -3.0 dB  |
| Peaking | 2278 Hz | 1.62 | -6.3 dB  |
| Peaking | 3814 Hz | 0.57 | 7.8 dB   |
| Peaking | 6748 Hz | 1.86 | -10.5 dB |
| Peaking | 1110 Hz | 2.85 | -1.8 dB  |
| Peaking | 1165 Hz | 1.61 | 1.2 dB   |
| Peaking | 7802 Hz | 8.27 | -1.3 dB  |
| Peaking | 8830 Hz | 6.72 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-TAD300/Audio-Technica%20ATH-TAD300.png)