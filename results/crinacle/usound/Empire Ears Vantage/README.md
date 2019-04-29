# Empire Ears Vantage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.6; 25 -13.5; 28 -13.3; 31 -13.1; 34 -12.8; 37 -12.7; 41 -12.4; 45 -12.2; 49 -12.0; 54 -11.7; 60 -11.5; 66 -11.3; 72 -11.1; 79 -11.0; 87 -10.8; 96 -10.7; 106 -10.6; 116 -10.4; 128 -10.1; 141 -9.9; 155 -9.6; 170 -9.2; 187 -8.8; 206 -8.3; 227 -7.9; 249 -7.4; 274 -6.9; 302 -6.4; 332 -5.9; 365 -5.4; 402 -5.0; 442 -4.7; 486 -4.0; 535 -3.6; 588 -3.3; 647 -2.8; 712 -2.3; 783 -2.1; 861 -2.1; 947 -2.4; 1042 -3.1; 1146 -4.1; 1261 -5.2; 1387 -6.0; 1526 -6.4; 1678 -6.3; 1846 -6.0; 2031 -5.6; 2234 -5.0; 2457 -4.1; 2703 -3.1; 2973 -2.1; 3270 -1.1; 3597 -0.5; 3957 -2.1; 4353 -4.8; 4788 -6.0; 5267 -4.5; 5793 -1.8; 6373 -0.9; 7010 -3.8; 7711 -4.9; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.9; 16529 -5.3; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Vantage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Vantage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.23 | -8.6 dB |
| Peaking | 143 Hz   | 0.78 | -2.9 dB |
| Peaking | 737 Hz   | 1.86 | 3.3 dB  |
| Peaking | 3449 Hz  | 3.69 | 4.6 dB  |
| Peaking | 22050 Hz | 2.39 | 1.1 dB  |
| Peaking | 484 Hz   | 4.28 | 0.7 dB  |
| Peaking | 987 Hz   | 4.68 | 1.3 dB  |
| Peaking | 1568 Hz  | 2.39 | -2.2 dB |
| Peaking | 4772 Hz  | 6.63 | -2.4 dB |
| Peaking | 6176 Hz  | 5.3  | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Vantage/Empire%20Ears%20Vantage.png)