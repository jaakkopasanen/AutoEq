# Meze 12 Classics
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.6; 54 -5.1; 60 -5.5; 66 -5.9; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.9; 106 -8.3; 116 -8.7; 128 -9.0; 141 -9.2; 155 -9.5; 170 -9.5; 187 -9.5; 206 -9.5; 227 -9.4; 249 -9.3; 274 -9.1; 302 -8.8; 332 -8.4; 365 -8.0; 402 -7.5; 442 -7.0; 486 -6.5; 535 -6.0; 588 -5.4; 647 -4.8; 712 -4.3; 783 -3.6; 861 -2.9; 947 -2.7; 1042 -2.7; 1146 -2.5; 1261 -3.2; 1387 -3.9; 1526 -4.0; 1678 -3.9; 1846 -3.9; 2031 -4.4; 2234 -5.3; 2457 -7.0; 2703 -8.6; 2973 -8.6; 3270 -6.9; 3597 -5.8; 3957 -5.7; 4353 -6.4; 4788 -9.4; 5267 -13.7; 5793 -9.9; 6373 -5.0; 7010 -4.9; 7711 -7.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.2; 16529 -9.5; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 12 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.34 | 7.1 dB  |
| Peaking | 186 Hz   | 0.55 | -3.6 dB |
| Peaking | 1005 Hz  | 1.01 | 4.4 dB  |
| Peaking | 5334 Hz  | 5.65 | -8.2 dB |
| Peaking | 6554 Hz  | 7.17 | 3.4 dB  |
| Peaking | 1970 Hz  | 3.4  | 1.5 dB  |
| Peaking | 2808 Hz  | 3.53 | -3.6 dB |
| Peaking | 3972 Hz  | 2.43 | 1.8 dB  |
| Peaking | 4877 Hz  | 5.56 | -1.1 dB |
| Peaking | 16177 Hz | 2.49 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Meze%2012%20Classics/Meze%2012%20Classics.png)