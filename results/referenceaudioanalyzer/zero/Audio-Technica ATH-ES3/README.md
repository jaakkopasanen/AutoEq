# Audio-Technica ATH-ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.6; 249 -1.1; 274 -1.7; 302 -2.1; 332 -2.5; 365 -2.8; 402 -3.0; 442 -3.2; 486 -3.2; 535 -3.5; 588 -3.6; 647 -3.9; 712 -4.2; 783 -4.9; 861 -5.8; 947 -7.0; 1042 -8.1; 1146 -9.0; 1261 -9.6; 1387 -10.4; 1526 -11.2; 1678 -12.0; 1846 -12.8; 2031 -14.0; 2234 -15.9; 2457 -17.8; 2703 -18.7; 2973 -17.8; 3270 -15.6; 3597 -12.8; 3957 -9.6; 4353 -5.7; 4788 -2.4; 5267 -2.9; 5793 -6.1; 6373 -10.7; 7010 -13.5; 7711 -14.0; 8482 -13.9; 9330 -14.9; 10263 -16.4; 11289 -16.7; 12418 -15.2; 13660 -11.7; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.26 | 5.3 dB   |
| Peaking | 169 Hz   | 0.25 | 5.5 dB   |
| Peaking | 2770 Hz  | 0.92 | -12.8 dB |
| Peaking | 4840 Hz  | 2.45 | 12.6 dB  |
| Peaking | 10174 Hz | 1    | -9.9 dB  |
| Peaking | 1171 Hz  | 4.6  | -0.9 dB  |
| Peaking | 7232 Hz  | 3.5  | -4.3 dB  |
| Peaking | 8528 Hz  | 1.07 | 2.9 dB   |
| Peaking | 12437 Hz | 1.54 | -4.5 dB  |
| Peaking | 15177 Hz | 1.43 | 4.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.8 dB   |
| Peaking | 250 Hz   | 1.41 | 4.3 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-ES3/Audio-Technica%20ATH-ES3.png)