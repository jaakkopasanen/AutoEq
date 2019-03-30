# Onkyo IE-FC300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.2; 25 -4.5; 28 -4.8; 31 -5.1; 34 -5.3; 37 -5.5; 41 -5.6; 45 -5.7; 49 -5.9; 54 -6.0; 60 -6.0; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.0; 96 -6.0; 106 -6.0; 116 -6.0; 128 -6.0; 141 -6.0; 155 -6.0; 170 -5.7; 187 -5.7; 206 -5.6; 227 -5.4; 249 -5.2; 274 -5.0; 302 -4.8; 332 -4.6; 365 -4.4; 402 -4.1; 442 -3.8; 486 -3.5; 535 -3.1; 588 -2.8; 647 -2.5; 712 -2.1; 783 -1.8; 861 -1.5; 947 -1.2; 1042 -1.2; 1146 -1.2; 1261 -1.2; 1387 -1.6; 1526 -2.1; 1678 -2.0; 1846 -1.6; 2031 -1.8; 2234 -2.5; 2457 -3.0; 2703 -3.1; 2973 -2.7; 3270 -2.3; 3597 -2.1; 3957 -2.5; 4353 -3.7; 4788 -4.8; 5267 -5.4; 5793 -4.8; 6373 -2.7; 7010 -0.5; 7711 -2.4; 8482 -2.7; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo IE-FC300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-FC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.03 | 0.6 dB  |
| Peaking | 95 Hz   | 0.23 | -3.4 dB |
| Peaking | 996 Hz  | 0.9  | 2.0 dB  |
| Peaking | 5326 Hz | 3.41 | -3.1 dB |
| Peaking | 6906 Hz | 7.44 | 3.0 dB  |
| Peaking | 10 Hz   | 1.17 | 0.9 dB  |
| Peaking | 1268 Hz | 1.27 | 0.7 dB  |
| Peaking | 1954 Hz | 3.67 | 1.9 dB  |
| Peaking | 1983 Hz | 1.01 | -1.6 dB |
| Peaking | 3539 Hz | 3.84 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Onkyo%20IE-FC300/Onkyo%20IE-FC300.png)