# Audio-Technica ATH-W5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.6; 54 -2.6; 60 -3.8; 66 -4.9; 72 -5.6; 79 -6.2; 87 -6.6; 96 -6.9; 106 -7.1; 116 -6.9; 128 -6.7; 141 -6.3; 155 -6.0; 170 -5.6; 187 -5.3; 206 -5.1; 227 -4.9; 249 -4.6; 274 -4.3; 302 -4.2; 332 -4.0; 365 -3.7; 402 -3.3; 442 -3.0; 486 -2.8; 535 -2.7; 588 -3.1; 647 -4.2; 712 -5.2; 783 -6.0; 861 -7.0; 947 -8.0; 1042 -8.7; 1146 -9.3; 1261 -9.9; 1387 -10.8; 1526 -11.5; 1678 -12.1; 1846 -12.3; 2031 -12.3; 2234 -12.3; 2457 -11.2; 2703 -8.5; 2973 -5.0; 3270 -1.2; 3597 -0.9; 3957 -6.1; 4353 -9.1; 4788 -9.7; 5267 -7.9; 5793 -3.0; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -8.6; 9330 -8.9; 10263 -9.3; 11289 -10.7; 12418 -11.6; 13660 -10.3; 15026 -8.6; 16529 -8.2; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.89 | 6.9 dB  |
| Peaking | 1896 Hz  | 1.64 | -5.6 dB |
| Peaking | 3389 Hz  | 4.31 | 10.6 dB |
| Peaking | 6439 Hz  | 3.16 | 10.7 dB |
| Peaking | 7723 Hz  | 0.36 | -5.0 dB |
| Peaking | 99 Hz    | 2.35 | -1.8 dB |
| Peaking | 444 Hz   | 1.2  | 4.1 dB  |
| Peaking | 4732 Hz  | 6.11 | -2.4 dB |
| Peaking | 11289 Hz | 1.19 | 2.3 dB  |
| Peaking | 12234 Hz | 2.51 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-W5000/Audio-Technica%20ATH-W5000.png)