# Audio-Technica ATH-AD700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.3; 72 -2.2; 79 -2.9; 87 -3.5; 96 -3.9; 106 -4.3; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.8; 187 -6.0; 206 -6.2; 227 -6.1; 249 -5.9; 274 -5.6; 302 -5.9; 332 -6.0; 365 -6.1; 402 -6.3; 442 -6.3; 486 -6.3; 535 -6.3; 588 -6.3; 647 -6.6; 712 -6.7; 783 -6.9; 861 -7.2; 947 -7.6; 1042 -7.9; 1146 -7.9; 1261 -7.9; 1387 -7.6; 1526 -6.8; 1678 -5.5; 1846 -4.2; 2031 -3.7; 2234 -4.6; 2457 -6.1; 2703 -7.4; 2973 -8.0; 3270 -6.9; 3597 -5.2; 3957 -7.4; 4353 -10.6; 4788 -11.9; 5267 -12.0; 5793 -10.5; 6373 -7.1; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.52 | 6.7 dB  |
| Peaking | 1193 Hz | 1.85 | -1.8 dB |
| Peaking | 1968 Hz | 3.6  | 3.6 dB  |
| Peaking | 5141 Hz | 2.75 | -6.3 dB |
| Peaking | 6884 Hz | 6.92 | 4.1 dB  |
| Peaking | 58 Hz   | 0.91 | -1.4 dB |
| Peaking | 60 Hz   | 2.06 | 2.4 dB  |
| Peaking | 2914 Hz | 5.74 | -1.5 dB |
| Peaking | 3624 Hz | 8.97 | 2.9 dB  |
| Peaking | 9824 Hz | 8.52 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD700/Audio-Technica%20ATH-AD700.png)