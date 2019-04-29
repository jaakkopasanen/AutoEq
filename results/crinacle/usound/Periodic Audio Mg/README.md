# Periodic Audio Mg
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.8; 28 -10.1; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.6; 49 -10.6; 54 -10.6; 60 -10.7; 66 -10.8; 72 -10.9; 79 -11.0; 87 -11.2; 96 -11.3; 106 -11.4; 116 -11.4; 128 -11.3; 141 -11.2; 155 -11.1; 170 -10.8; 187 -10.5; 206 -10.1; 227 -9.7; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.6; 365 -7.0; 402 -6.4; 442 -5.8; 486 -5.2; 535 -4.5; 588 -3.9; 647 -3.2; 712 -2.5; 783 -1.6; 861 -0.9; 947 -0.5; 1042 -0.5; 1146 -0.8; 1261 -1.2; 1387 -1.3; 1526 -1.4; 1678 -2.6; 1846 -3.7; 2031 -3.4; 2234 -3.1; 2457 -3.3; 2703 -3.6; 2973 -3.6; 3270 -3.3; 3597 -3.0; 3957 -3.2; 4353 -4.2; 4788 -5.3; 5267 -4.4; 5793 -2.1; 6373 -0.8; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.7; 15026 -11.2; 16529 -14.4; 18182 -14.8; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Mg GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Mg ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.1  | -2.0 dB  |
| Peaking | 503 Hz   | 0.13 | -20.6 dB |
| Peaking | 842 Hz   | 0.22 | 23.3 dB  |
| Peaking | 17823 Hz | 0.98 | -11.4 dB |
| Peaking | 5026 Hz  | 3.96 | -3.6 dB  |
| Peaking | 6501 Hz  | 1.58 | 5.8 dB   |
| Peaking | 7668 Hz  | 3.26 | -3.4 dB  |
| Peaking | 12919 Hz | 3.14 | 3.1 dB   |
| Peaking | 16039 Hz | 0.08 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -9.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Periodic%20Audio%20Mg/Periodic%20Audio%20Mg.png)