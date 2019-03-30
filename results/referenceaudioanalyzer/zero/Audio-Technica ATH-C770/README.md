# Audio-Technica ATH-C770
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.6; 106 -3.1; 116 -4.5; 128 -5.8; 141 -6.9; 155 -7.9; 170 -8.6; 187 -9.0; 206 -9.1; 227 -9.1; 249 -9.1; 274 -9.1; 302 -8.8; 332 -8.8; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.1; 647 -6.5; 712 -6.2; 783 -6.3; 861 -6.8; 947 -7.4; 1042 -8.0; 1146 -8.7; 1261 -9.2; 1387 -9.2; 1526 -8.2; 1678 -6.3; 1846 -4.3; 2031 -3.3; 2234 -4.0; 2457 -6.2; 2703 -8.2; 2973 -8.8; 3270 -7.9; 3597 -6.2; 3957 -4.6; 4353 -3.9; 4788 -5.0; 5267 -8.1; 5793 -10.9; 6373 -10.6; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-C770 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-C770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.3  | 8.9 dB  |
| Peaking | 194 Hz  | 0.6  | -8.4 dB |
| Peaking | 1270 Hz | 3.12 | -3.9 dB |
| Peaking | 2187 Hz | 0.27 | 1.1 dB  |
| Peaking | 6000 Hz | 5.65 | -6.2 dB |
| Peaking | 20 Hz   | 2.84 | 1.4 dB  |
| Peaking | 90 Hz   | 6.89 | 1.3 dB  |
| Peaking | 2129 Hz | 2.83 | 5.9 dB  |
| Peaking | 2813 Hz | 1.25 | -5.1 dB |
| Peaking | 4147 Hz | 2.87 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-C770/Audio-Technica%20ATH-C770.png)