# Pioneer SE 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.4; 49 -2.8; 54 -4.3; 60 -5.9; 66 -7.5; 72 -9.1; 79 -10.4; 87 -11.3; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.4; 141 -11.3; 155 -11.0; 170 -10.5; 187 -9.9; 206 -9.2; 227 -8.5; 249 -8.0; 274 -7.7; 302 -7.5; 332 -7.2; 365 -6.8; 402 -6.5; 442 -6.4; 486 -6.2; 535 -6.4; 588 -6.7; 647 -6.7; 712 -7.0; 783 -7.3; 861 -7.0; 947 -5.7; 1042 -4.1; 1146 -4.0; 1261 -4.8; 1387 -5.5; 1526 -6.0; 1678 -6.1; 1846 -5.7; 2031 -4.9; 2234 -4.9; 2457 -5.5; 2703 -5.7; 2973 -5.4; 3270 -5.1; 3597 -4.7; 3957 -4.1; 4353 -3.8; 4788 -4.0; 5267 -4.9; 5793 -6.0; 6373 -6.6; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.56 | 8.7 dB  |
| Peaking | 95 Hz   | 0.74 | -8.7 dB |
| Peaking | 1124 Hz | 4.4  | 2.9 dB  |
| Peaking | 2144 Hz | 3.57 | 1.5 dB  |
| Peaking | 4270 Hz | 2.33 | 2.9 dB  |
| Peaking | 116 Hz  | 2.28 | 1.4 dB  |
| Peaking | 144 Hz  | 1.12 | -1.4 dB |
| Peaking | 401 Hz  | 0.59 | 0.8 dB  |
| Peaking | 786 Hz  | 3.48 | -1.4 dB |
| Peaking | 6437 Hz | 7.56 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20SE%20700/Pioneer%20SE%20700.png)