# Dita Audio Dream
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.3; 25 -9.1; 28 -8.9; 31 -8.6; 34 -8.4; 37 -8.2; 41 -7.9; 45 -7.7; 49 -7.5; 54 -7.3; 60 -7.2; 66 -7.1; 72 -7.1; 79 -7.1; 87 -7.2; 96 -7.3; 106 -7.5; 116 -7.6; 128 -7.7; 141 -7.8; 155 -7.9; 170 -7.8; 187 -7.8; 206 -7.8; 227 -7.7; 249 -7.5; 274 -7.4; 302 -7.2; 332 -6.9; 365 -6.7; 402 -6.4; 442 -6.1; 486 -5.8; 535 -5.5; 588 -5.1; 647 -4.7; 712 -4.1; 783 -3.5; 861 -3.0; 947 -2.7; 1042 -2.7; 1146 -3.2; 1261 -3.7; 1387 -3.8; 1526 -3.5; 1678 -2.8; 1846 -1.9; 2031 -1.2; 2234 -0.7; 2457 -0.5; 2703 -0.6; 2973 -1.1; 3270 -1.9; 3597 -3.0; 3957 -4.4; 4353 -6.2; 4788 -7.3; 5267 -5.8; 5793 -5.8; 6373 -4.3; 7010 -4.7; 7711 -7.9; 8482 -10.4; 9330 -8.6; 10263 -5.5; 11289 -5.2; 12418 -5.2; 13660 -5.6; 15026 -5.2; 16529 -5.3; 18182 -6.7; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.6  | -4.1 dB |
| Peaking | 187 Hz  | 0.52 | -2.6 dB |
| Peaking | 913 Hz  | 1.58 | 2.5 dB  |
| Peaking | 2454 Hz | 1.77 | 5.1 dB  |
| Peaking | 8575 Hz | 4.41 | -5.8 dB |
| Peaking | 3362 Hz | 4.1  | 1.3 dB  |
| Peaking | 4717 Hz | 3.92 | -2.9 dB |
| Peaking | 6747 Hz | 5.72 | 1.7 dB  |
| Peaking | 7786 Hz | 2.95 | 0.4 dB  |
| Peaking | 7865 Hz | 8.75 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Dream/Dita%20Audio%20Dream.png)