# Elysian Hades
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.7; 25 -2.1; 28 -2.5; 31 -2.8; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.7; 66 -5.1; 72 -5.5; 79 -5.8; 87 -6.2; 96 -6.7; 106 -7.0; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.5; 249 -8.4; 274 -8.2; 302 -8.0; 332 -7.8; 365 -7.5; 402 -7.2; 442 -6.8; 486 -6.4; 535 -6.0; 588 -5.5; 647 -4.9; 712 -4.3; 783 -3.6; 861 -3.0; 947 -2.6; 1042 -2.6; 1146 -3.0; 1261 -3.4; 1387 -3.4; 1526 -3.0; 1678 -2.2; 1846 -1.5; 2031 -1.0; 2234 -0.9; 2457 -1.2; 2703 -1.6; 2973 -1.7; 3270 -1.3; 3597 -0.7; 3957 -0.5; 4353 -1.2; 4788 -3.2; 5267 -5.0; 5793 -3.4; 6373 -2.2; 7010 -4.4; 7711 -4.6; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.7; 16529 -7.6; 18182 -8.0; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Hades GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Hades ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.29 | 3.8 dB  |
| Peaking | 206 Hz   | 0.47 | -4.1 dB |
| Peaking | 897 Hz   | 2.13 | 2.1 dB  |
| Peaking | 2736 Hz  | 0.77 | 3.8 dB  |
| Peaking | 17619 Hz | 2.02 | -4.5 dB |
| Peaking | 2064 Hz  | 2.83 | 1.5 dB  |
| Peaking | 3896 Hz  | 0.91 | -3.3 dB |
| Peaking | 4034 Hz  | 2.14 | 4.9 dB  |
| Peaking | 5233 Hz  | 5.97 | -1.9 dB |
| Peaking | 6216 Hz  | 7.15 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Elysian%20Hades/Elysian%20Hades.png)