# Audio-Technica ATH-WS50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.6; 54 -2.3; 60 -3.1; 66 -3.8; 72 -4.3; 79 -4.6; 87 -4.8; 96 -5.1; 106 -5.1; 116 -5.0; 128 -4.7; 141 -4.2; 155 -3.9; 170 -3.5; 187 -2.9; 206 -2.2; 227 -1.2; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.2; 535 -4.2; 588 -6.1; 647 -7.2; 712 -7.4; 783 -7.5; 861 -7.6; 947 -7.3; 1042 -6.9; 1146 -7.0; 1261 -7.8; 1387 -8.6; 1526 -9.4; 1678 -10.5; 1846 -11.6; 2031 -12.5; 2234 -12.6; 2457 -11.8; 2703 -10.0; 2973 -7.9; 3270 -5.8; 3597 -3.7; 3957 -2.1; 4353 -0.6; 4788 -0.5; 5267 -6.4; 5793 -14.4; 6373 -17.5; 7010 -20.1; 7711 -21.6; 8482 -20.0; 9330 -15.3; 10263 -10.9; 11289 -9.7; 12418 -11.3; 13660 -12.3; 15026 -10.3; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-WS50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-WS50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.73 | 6.6 dB   |
| Peaking | 312 Hz   | 1.08 | 6.8 dB   |
| Peaking | 2148 Hz  | 1.36 | -6.7 dB  |
| Peaking | 4506 Hz  | 1.63 | 16.1 dB  |
| Peaking | 7089 Hz  | 1.17 | -19.6 dB |
| Peaking | 466 Hz   | 5.15 | 3.2 dB   |
| Peaking | 654 Hz   | 2.42 | -2.5 dB  |
| Peaking | 8593 Hz  | 5.69 | -3.1 dB  |
| Peaking | 10813 Hz | 2.58 | 3.8 dB   |
| Peaking | 13826 Hz | 2.93 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.7 dB   |
| Peaking | 125 Hz   | 1.41 | -0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 6.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -16.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-WS50/Audio-Technica%20ATH-WS50.png)