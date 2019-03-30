# Audio-Technica FAKE ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.6; 141 -1.1; 155 -1.4; 170 -1.7; 187 -2.0; 206 -2.3; 227 -2.7; 249 -3.1; 274 -3.3; 302 -3.4; 332 -3.7; 365 -3.7; 402 -3.7; 442 -4.0; 486 -4.0; 535 -4.0; 588 -4.0; 647 -4.0; 712 -4.1; 783 -4.3; 861 -4.3; 947 -4.3; 1042 -4.4; 1146 -4.6; 1261 -5.4; 1387 -6.8; 1526 -8.5; 1678 -10.7; 1846 -12.7; 2031 -14.5; 2234 -15.1; 2457 -13.3; 2703 -8.5; 2973 -6.1; 3270 -10.0; 3597 -12.2; 3957 -11.1; 4353 -7.0; 4788 -3.4; 5267 -9.3; 5793 -13.7; 6373 -15.1; 7010 -16.0; 7711 -15.7; 8482 -12.5; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica FAKE ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica FAKE ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.17 | 6.2 dB   |
| Peaking | 1058 Hz  | 0.84 | 2.7 dB   |
| Peaking | 1793 Hz  | 2.04 | -3.8 dB  |
| Peaking | 2188 Hz  | 2.88 | -7.5 dB  |
| Peaking | 7028 Hz  | 2.52 | -10.7 dB |
| Peaking | 2922 Hz  | 6.59 | 5.4 dB   |
| Peaking | 3696 Hz  | 2.52 | -5.8 dB  |
| Peaking | 4721 Hz  | 4.81 | 8.1 dB   |
| Peaking | 5655 Hz  | 5.68 | -3.4 dB  |
| Peaking | 10090 Hz | 4.58 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20FAKE%20ATH-ES55/Audio-Technica%20FAKE%20ATH-ES55.png)