# Intime Sora
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.1; 25 -9.0; 28 -8.8; 31 -8.6; 34 -8.4; 37 -8.1; 41 -7.9; 45 -7.6; 49 -7.4; 54 -7.1; 60 -6.9; 66 -6.7; 72 -6.5; 79 -6.4; 87 -6.3; 96 -6.2; 106 -6.2; 116 -6.2; 128 -6.2; 141 -6.1; 155 -6.0; 170 -5.8; 187 -5.7; 206 -5.5; 227 -5.4; 249 -5.2; 274 -5.1; 302 -4.9; 332 -4.8; 365 -4.7; 402 -4.7; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.5; 647 -4.4; 712 -4.3; 783 -4.1; 861 -3.9; 947 -4.0; 1042 -4.4; 1146 -5.0; 1261 -5.6; 1387 -5.8; 1526 -5.6; 1678 -5.0; 1846 -4.2; 2031 -3.7; 2234 -3.4; 2457 -3.4; 2703 -3.7; 2973 -4.2; 3270 -4.6; 3597 -4.6; 3957 -4.4; 4353 -4.4; 4788 -4.7; 5267 -4.4; 5793 -2.6; 6373 -0.5; 7010 -1.9; 7711 -4.9; 8482 -4.9; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -7.7; 15026 -8.8; 16529 -10.4; 18182 -12.9; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Intime Sora GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Intime Sora ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.34 | -4.9 dB |
| Peaking | 146 Hz   | 0.94 | -1.1 dB |
| Peaking | 1377 Hz  | 5.32 | -1.6 dB |
| Peaking | 6489 Hz  | 5.56 | 4.8 dB  |
| Peaking | 17913 Hz | 1.01 | -8.8 dB |
| Peaking | 872 Hz   | 2.29 | 1.0 dB  |
| Peaking | 2130 Hz  | 0.54 | -0.9 dB |
| Peaking | 2326 Hz  | 1.99 | 2.1 dB  |
| Peaking | 12661 Hz | 2.2  | 2.4 dB  |
| Peaking | 14018 Hz | 3.56 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Intime%20Sora/Intime%20Sora.png)