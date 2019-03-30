# OPPO PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.2; 25 -9.0; 28 -8.6; 31 -8.2; 34 -7.6; 37 -7.0; 41 -6.5; 45 -6.5; 49 -6.9; 54 -7.6; 60 -8.0; 66 -8.1; 72 -8.6; 79 -9.2; 87 -9.7; 96 -10.0; 106 -10.2; 116 -10.3; 128 -10.0; 141 -9.7; 155 -9.3; 170 -8.7; 187 -7.9; 206 -6.9; 227 -5.7; 249 -4.6; 274 -3.8; 302 -2.9; 332 -1.7; 365 -0.8; 402 -0.5; 442 -0.5; 486 -0.9; 535 -1.5; 588 -2.1; 647 -2.4; 712 -2.5; 783 -2.4; 861 -2.1; 947 -1.5; 1042 -1.2; 1146 -1.2; 1261 -1.2; 1387 -1.1; 1526 -1.4; 1678 -2.3; 1846 -3.2; 2031 -4.1; 2234 -4.8; 2457 -5.2; 2703 -5.3; 2973 -4.8; 3270 -3.8; 3597 -2.8; 3957 -1.8; 4353 -1.5; 4788 -2.0; 5267 -3.1; 5793 -5.0; 6373 -6.6; 7010 -5.7; 7711 -3.3; 8482 -3.4; 9330 -3.5; 10263 -3.5; 11289 -3.5; 12418 -3.5; 13660 -3.5; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`OPPO PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `OPPO PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.15 | -5.4 dB |
| Peaking | 99 Hz   | 0.77 | -5.1 dB |
| Peaking | 183 Hz  | 0.73 | -7.4 dB |
| Peaking | 282 Hz  | 0.49 | 6.6 dB  |
| Peaking | 6477 Hz | 6.62 | -3.8 dB |
| Peaking | 434 Hz  | 1.87 | 2.2 dB  |
| Peaking | 624 Hz  | 0.83 | -2.7 dB |
| Peaking | 1370 Hz | 0.88 | 3.8 dB  |
| Peaking | 2446 Hz | 1.03 | -3.8 dB |
| Peaking | 4135 Hz | 2.49 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/OPPO%20PM3/OPPO%20PM3.png)