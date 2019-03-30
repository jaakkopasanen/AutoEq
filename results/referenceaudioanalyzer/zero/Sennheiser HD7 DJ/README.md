# Sennheiser HD7 DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.7; 25 -16.0; 28 -16.4; 31 -16.6; 34 -16.8; 37 -16.9; 41 -17.1; 45 -17.2; 49 -17.4; 54 -17.5; 60 -17.4; 66 -17.2; 72 -17.2; 79 -17.0; 87 -16.8; 96 -16.5; 106 -16.5; 116 -16.5; 128 -16.6; 141 -16.4; 155 -15.9; 170 -15.2; 187 -13.7; 206 -11.5; 227 -8.8; 249 -6.7; 274 -5.6; 302 -5.2; 332 -5.2; 365 -5.6; 402 -6.0; 442 -6.3; 486 -6.5; 535 -6.7; 588 -6.8; 647 -6.8; 712 -6.8; 783 -6.8; 861 -6.9; 947 -7.1; 1042 -6.9; 1146 -6.9; 1261 -6.4; 1387 -5.7; 1526 -5.7; 1678 -5.9; 1846 -5.8; 2031 -5.9; 2234 -6.0; 2457 -5.6; 2703 -4.7; 2973 -2.8; 3270 -0.6; 3597 -0.5; 3957 -2.8; 4353 -6.2; 4788 -6.3; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD7 DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD7 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.57 | -10.0 dB |
| Peaking | 87 Hz   | 1.17 | -6.1 dB  |
| Peaking | 152 Hz  | 2.45 | -6.7 dB  |
| Peaking | 3396 Hz | 3.73 | 6.5 dB   |
| Peaking | 6041 Hz | 4.53 | 6.5 dB   |
| Peaking | 57 Hz   | 4.29 | -1.0 dB  |
| Peaking | 189 Hz  | 5.51 | -1.8 dB  |
| Peaking | 208 Hz  | 4.02 | -1.0 dB  |
| Peaking | 289 Hz  | 2.03 | 3.1 dB   |
| Peaking | 4511 Hz | 9.58 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -10.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB   |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD7%20DJ/Sennheiser%20HD7%20DJ.png)