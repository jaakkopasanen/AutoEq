# AKG K514
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.2; 66 -2.0; 72 -2.7; 79 -3.3; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.9; 128 -5.4; 141 -5.9; 155 -6.3; 170 -6.8; 187 -7.2; 206 -7.4; 227 -7.6; 249 -7.9; 274 -8.1; 302 -8.4; 332 -8.6; 365 -8.9; 402 -9.5; 442 -10.1; 486 -10.8; 535 -11.4; 588 -12.1; 647 -12.4; 712 -12.0; 783 -11.5; 861 -11.3; 947 -10.6; 1042 -9.5; 1146 -9.1; 1261 -9.6; 1387 -9.5; 1526 -8.6; 1678 -7.1; 1846 -5.5; 2031 -4.3; 2234 -3.6; 2457 -2.6; 2703 -2.0; 2973 -1.9; 3270 -2.8; 3597 -2.9; 3957 -0.8; 4353 -0.9; 4788 -2.9; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.2; 9330 -11.5; 10263 -11.3; 11289 -10.4; 12418 -9.9; 13660 -9.2; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K514 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K514 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.49 | 6.6 dB  |
| Peaking | 768 Hz  | 0.52 | -5.8 dB |
| Peaking | 2866 Hz | 0.84 | 5.6 dB  |
| Peaking | 6227 Hz | 1.66 | 6.9 dB  |
| Peaking | 9630 Hz | 1.09 | -6.9 dB |
| Peaking | 641 Hz  | 3.55 | -1.1 dB |
| Peaking | 1320 Hz | 1.23 | 2.2 dB  |
| Peaking | 1430 Hz | 2.8  | -3.4 dB |
| Peaking | 3456 Hz | 5.2  | -1.6 dB |
| Peaking | 4090 Hz | 9.16 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K514/AKG%20K514.png)