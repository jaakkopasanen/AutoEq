# Koss ESP 950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.3; 72 -2.0; 79 -2.8; 87 -3.7; 96 -4.7; 106 -5.7; 116 -6.5; 128 -7.1; 141 -7.5; 155 -7.8; 170 -7.6; 187 -7.4; 206 -7.3; 227 -7.1; 249 -6.8; 274 -6.4; 302 -6.2; 332 -5.9; 365 -5.8; 402 -5.8; 442 -5.8; 486 -5.7; 535 -5.2; 588 -4.8; 647 -4.8; 712 -5.0; 783 -5.3; 861 -5.5; 947 -5.5; 1042 -5.8; 1146 -6.1; 1261 -6.2; 1387 -6.6; 1526 -7.0; 1678 -7.1; 1846 -7.1; 2031 -7.2; 2234 -7.5; 2457 -7.2; 2703 -6.7; 2973 -6.2; 3270 -5.7; 3597 -4.7; 3957 -3.9; 4353 -3.8; 4788 -4.3; 5267 -6.1; 5793 -8.8; 6373 -11.2; 7010 -11.6; 7711 -9.7; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP 950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP 950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.28 | 7.1 dB  |
| Peaking | 139 Hz  | 0.88 | -5.7 dB |
| Peaking | 647 Hz  | 1.83 | 1.6 dB  |
| Peaking | 4383 Hz | 2.81 | 3.7 dB  |
| Peaking | 6718 Hz | 3.15 | -6.1 dB |
| Peaking | 2134 Hz | 2.06 | -1.1 dB |
| Peaking | 3643 Hz | 6.45 | 0.8 dB  |
| Peaking | 9237 Hz | 5.48 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Koss%20ESP%20950/Koss%20ESP%20950.png)