# AKG K99 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.1; 96 -1.8; 106 -2.5; 116 -3.1; 128 -3.7; 141 -4.3; 155 -4.8; 170 -5.2; 187 -5.5; 206 -5.8; 227 -5.9; 249 -6.1; 274 -6.4; 302 -6.9; 332 -7.4; 365 -8.1; 402 -8.8; 442 -9.3; 486 -9.6; 535 -9.9; 588 -10.2; 647 -10.5; 712 -10.7; 783 -10.5; 861 -10.3; 947 -10.4; 1042 -10.3; 1146 -10.7; 1261 -11.0; 1387 -10.4; 1526 -9.0; 1678 -7.5; 1846 -5.9; 2031 -4.6; 2234 -3.8; 2457 -2.4; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -4.9; 5267 -5.6; 5793 -4.1; 6373 -5.0; 7010 -7.4; 7711 -9.8; 8482 -11.9; 9330 -12.8; 10263 -11.9; 11289 -10.8; 12418 -10.7; 13660 -10.4; 15026 -8.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K99 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K99 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.35 | 6.6 dB  |
| Peaking | 1284 Hz  | 0.43 | -7.6 dB |
| Peaking | 3119 Hz  | 0.7  | 12.3 dB |
| Peaking | 6433 Hz  | 3.56 | 3.9 dB  |
| Peaking | 8711 Hz  | 0.73 | -8.1 dB |
| Peaking | 80 Hz    | 5.41 | 0.9 dB  |
| Peaking | 1351 Hz  | 6.76 | -1.2 dB |
| Peaking | 1879 Hz  | 5.47 | 0.7 dB  |
| Peaking | 16846 Hz | 3.38 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K99%20PRO/AKG%20K99%20PRO.png)