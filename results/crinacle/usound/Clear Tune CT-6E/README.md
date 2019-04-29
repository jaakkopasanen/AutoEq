# Clear Tune CT-6E
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.2; 34 -4.3; 37 -4.4; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.3; 66 -5.7; 72 -6.0; 79 -6.4; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.4; 249 -9.4; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.2; 486 -7.8; 535 -7.3; 588 -6.7; 647 -5.9; 712 -4.8; 783 -3.5; 861 -1.5; 947 -0.5; 1042 -0.5; 1146 -2.6; 1261 -5.9; 1387 -8.2; 1526 -9.8; 1678 -11.2; 1846 -12.2; 2031 -11.6; 2234 -10.2; 2457 -8.4; 2703 -7.2; 2973 -6.9; 3270 -7.1; 3597 -7.0; 3957 -7.7; 4353 -6.6; 4788 -2.6; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.23 | 3.0 dB  |
| Peaking | 196 Hz  | 0.42 | -3.7 dB |
| Peaking | 985 Hz  | 1.94 | 8.6 dB  |
| Peaking | 1767 Hz | 1.65 | -6.8 dB |
| Peaking | 5722 Hz | 3.02 | 7.1 dB  |
| Peaking | 2125 Hz | 5.28 | -0.7 dB |
| Peaking | 2705 Hz | 3.4  | 1.1 dB  |
| Peaking | 4123 Hz | 4.78 | -2.4 dB |
| Peaking | 4787 Hz | 7.03 | 2.2 dB  |
| Peaking | 8208 Hz | 4.9  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-6E/Clear%20Tune%20CT-6E.png)