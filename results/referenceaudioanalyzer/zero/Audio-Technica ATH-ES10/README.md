# Audio-Technica ATH-ES10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -2.0; 34 -3.3; 37 -4.4; 41 -5.6; 45 -6.5; 49 -7.2; 54 -7.8; 60 -8.3; 66 -8.5; 72 -8.6; 79 -8.6; 87 -8.6; 96 -8.6; 106 -8.4; 116 -8.3; 128 -8.3; 141 -8.1; 155 -7.9; 170 -7.7; 187 -7.5; 206 -7.3; 227 -7.1; 249 -6.9; 274 -6.5; 302 -6.0; 332 -5.5; 365 -5.1; 402 -4.8; 442 -4.7; 486 -4.8; 535 -5.7; 588 -7.1; 647 -8.4; 712 -9.2; 783 -9.8; 861 -10.0; 947 -10.2; 1042 -10.3; 1146 -10.3; 1261 -10.7; 1387 -11.2; 1526 -11.7; 1678 -11.9; 1846 -11.9; 2031 -11.7; 2234 -10.9; 2457 -9.5; 2703 -7.4; 2973 -4.9; 3270 -2.6; 3597 -3.0; 3957 -6.2; 4353 -8.4; 4788 -7.9; 5267 -4.4; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -9.2; 13660 -9.5; 15026 -8.5; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ES10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ES10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 2.55 | 7.4 dB  |
| Peaking | 2457 Hz  | 0.53 | -7.4 dB |
| Peaking | 3240 Hz  | 2.49 | 10.6 dB |
| Peaking | 6091 Hz  | 3.27 | 8.8 dB  |
| Peaking | 13653 Hz | 2.67 | -3.2 dB |
| Peaking | 33 Hz    | 1.97 | 2.6 dB  |
| Peaking | 80 Hz    | 0.49 | -2.5 dB |
| Peaking | 473 Hz   | 1.21 | 3.9 dB  |
| Peaking | 716 Hz   | 1.6  | -2.8 dB |
| Peaking | 4537 Hz  | 8.68 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-ES10/Audio-Technica%20ATH-ES10.png)