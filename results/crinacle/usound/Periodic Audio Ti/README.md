# Periodic Audio Ti
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.8; 28 -7.3; 31 -7.8; 34 -8.1; 37 -8.4; 41 -8.7; 45 -9.0; 49 -9.2; 54 -9.5; 60 -9.7; 66 -10.0; 72 -10.3; 79 -10.6; 87 -10.8; 96 -11.1; 106 -11.2; 116 -11.4; 128 -11.4; 141 -11.4; 155 -11.3; 170 -11.1; 187 -10.8; 206 -10.5; 227 -10.0; 249 -9.5; 274 -9.0; 302 -8.5; 332 -8.1; 365 -7.6; 402 -6.9; 442 -6.3; 486 -5.6; 535 -5.0; 588 -4.2; 647 -3.5; 712 -2.7; 783 -1.9; 861 -1.2; 947 -0.7; 1042 -0.5; 1146 -0.5; 1261 -0.6; 1387 -0.6; 1526 -1.2; 1678 -2.2; 1846 -2.3; 2031 -2.0; 2234 -2.1; 2457 -2.7; 2703 -3.8; 2973 -5.4; 3270 -6.7; 3597 -7.1; 3957 -7.1; 4353 -7.8; 4788 -9.6; 5267 -10.3; 5793 -7.1; 6373 -3.7; 7010 -3.5; 7711 -6.3; 8482 -8.3; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -9.3; 15026 -10.3; 16529 -9.0; 18182 -9.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Ti GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Ti ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 128 Hz   | 0.41 | -5.7 dB |
| Peaking | 1057 Hz  | 0.83 | 6.1 dB  |
| Peaking | 2219 Hz  | 4.15 | 2.2 dB  |
| Peaking | 4921 Hz  | 4.31 | -5.0 dB |
| Peaking | 16856 Hz | 0.88 | -4.2 dB |
| Peaking | 3483 Hz  | 4.39 | -1.8 dB |
| Peaking | 6783 Hz  | 6.46 | 3.9 dB  |
| Peaking | 8409 Hz  | 7.12 | -2.9 dB |
| Peaking | 13389 Hz | 1.23 | 2.7 dB  |
| Peaking | 14224 Hz | 3.25 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Periodic%20Audio%20Ti/Periodic%20Audio%20Ti.png)