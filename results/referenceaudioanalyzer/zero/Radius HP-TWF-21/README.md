# Radius HP-TWF-21
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.5; 28 -8.8; 31 -9.1; 34 -9.3; 37 -9.4; 41 -9.5; 45 -9.6; 49 -9.6; 54 -9.7; 60 -9.9; 66 -9.9; 72 -9.9; 79 -9.9; 87 -9.9; 96 -9.7; 106 -9.6; 116 -9.6; 128 -9.6; 141 -9.6; 155 -9.6; 170 -9.4; 187 -9.3; 206 -9.0; 227 -8.9; 249 -8.9; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.1; 402 -8.0; 442 -8.0; 486 -7.7; 535 -7.4; 588 -6.8; 647 -6.3; 712 -6.0; 783 -6.0; 861 -5.7; 947 -5.6; 1042 -5.3; 1146 -4.9; 1261 -4.7; 1387 -5.0; 1526 -5.6; 1678 -6.4; 1846 -7.3; 2031 -8.1; 2234 -8.3; 2457 -7.8; 2703 -6.5; 2973 -5.2; 3270 -4.0; 3597 -2.7; 3957 -1.4; 4353 -0.7; 4788 -0.5; 5267 -1.0; 5793 -1.9; 6373 -2.1; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-TWF-21 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF-21 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.54 | -0.9 dB |
| Peaking | 114 Hz  | 0.21 | -3.4 dB |
| Peaking | 1334 Hz | 0.79 | 2.2 dB  |
| Peaking | 2180 Hz | 1.78 | -4.5 dB |
| Peaking | 4647 Hz | 1.47 | 6.0 dB  |
| Peaking | 6622 Hz | 5.34 | 2.7 dB  |
| Peaking | 7728 Hz | 1.96 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Radius%20HP-TWF-21/Radius%20HP-TWF-21.png)