# Earsonics ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.8; 25 -12.0; 28 -12.3; 31 -12.4; 34 -12.5; 37 -12.5; 41 -12.5; 45 -12.5; 49 -12.3; 54 -12.1; 60 -11.8; 66 -11.4; 72 -11.1; 79 -10.7; 87 -10.2; 96 -9.5; 106 -8.8; 116 -8.1; 128 -7.4; 141 -6.5; 155 -5.6; 170 -4.8; 187 -4.2; 206 -3.8; 227 -3.4; 249 -3.4; 274 -3.4; 302 -3.7; 332 -4.0; 365 -4.4; 402 -4.8; 442 -5.1; 486 -5.4; 535 -5.4; 588 -5.4; 647 -5.4; 712 -5.4; 783 -5.3; 861 -5.6; 947 -5.7; 1042 -5.8; 1146 -6.1; 1261 -6.4; 1387 -6.8; 1526 -7.1; 1678 -7.3; 1846 -6.8; 2031 -5.8; 2234 -4.8; 2457 -4.2; 2703 -3.3; 2973 -2.5; 3270 -2.7; 3597 -3.1; 3957 -2.8; 4353 -2.2; 4788 -2.1; 5267 -1.8; 5793 -0.6; 6373 -0.5; 7010 -1.6; 7711 -3.6; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.5  | -9.4 dB |
| Peaking | 597 Hz  | 2.67 | -1.0 dB |
| Peaking | 1669 Hz | 1.08 | -4.3 dB |
| Peaking | 2874 Hz | 1.06 | 2.5 dB  |
| Peaking | 6074 Hz | 3.33 | 3.5 dB  |
| Peaking | 16 Hz   | 0.98 | -2.0 dB |
| Peaking | 38 Hz   | 1.14 | 1.5 dB  |
| Peaking | 90 Hz   | 1.21 | -1.4 dB |
| Peaking | 217 Hz  | 1.71 | 2.1 dB  |
| Peaking | 8350 Hz | 4.74 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Earsonics%20ES3/Earsonics%20ES3.png)