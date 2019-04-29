# AAW W500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.3; 87 -8.6; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.1; 170 -10.1; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.3; 302 -9.0; 332 -9.0; 365 -8.7; 402 -8.4; 442 -8.1; 486 -7.8; 535 -7.5; 588 -7.2; 647 -6.9; 712 -6.5; 783 -6.2; 861 -6.0; 947 -6.0; 1042 -6.3; 1146 -7.0; 1261 -7.7; 1387 -8.3; 1526 -9.2; 1678 -10.4; 1846 -9.7; 2031 -6.2; 2234 -2.8; 2457 -1.3; 2703 -2.4; 2973 -2.8; 3270 -3.2; 3597 -4.1; 3957 -4.5; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -2.3; 7010 -4.9; 7711 -9.5; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW W500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW W500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 175 Hz  | 0.65 | -3.8 dB |
| Peaking | 1756 Hz | 2.89 | -6.3 dB |
| Peaking | 2399 Hz | 2.25 | 6.0 dB  |
| Peaking | 5415 Hz | 1.72 | 6.5 dB  |
| Peaking | 7813 Hz | 5.18 | -5.6 dB |
| Peaking | 22 Hz   | 1.16 | 1.4 dB  |
| Peaking | 395 Hz  | 2.44 | -0.5 dB |
| Peaking | 880 Hz  | 2.11 | 0.9 dB  |
| Peaking | 1050 Hz | 1.99 | 0.3 dB  |
| Peaking | 1272 Hz | 3.5  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AAW%20W500/AAW%20W500.png)