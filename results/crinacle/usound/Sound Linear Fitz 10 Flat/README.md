# Sound Linear Fitz 10 Flat
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.8; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.7; 37 -4.1; 41 -4.5; 45 -4.9; 49 -5.3; 54 -5.8; 60 -6.3; 66 -6.8; 72 -7.3; 79 -7.8; 87 -8.3; 96 -8.9; 106 -9.4; 116 -9.8; 128 -10.3; 141 -10.6; 155 -10.9; 170 -11.1; 187 -11.2; 206 -11.2; 227 -11.3; 249 -11.3; 274 -11.2; 302 -11.0; 332 -10.9; 365 -10.6; 402 -10.4; 442 -10.1; 486 -9.8; 535 -9.4; 588 -9.1; 647 -8.6; 712 -8.1; 783 -7.6; 861 -7.1; 947 -7.0; 1042 -7.2; 1146 -7.9; 1261 -8.6; 1387 -8.9; 1526 -8.6; 1678 -7.8; 1846 -6.4; 2031 -4.9; 2234 -3.6; 2457 -2.4; 2703 -1.6; 2973 -1.2; 3270 -1.6; 3597 -2.7; 3957 -3.2; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -4.6; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Linear Fitz 10 Flat GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Linear Fitz 10 Flat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  0.34 | 6.0 dB  |
| Peaking | 214 Hz  |  0.45 | -5.1 dB |
| Peaking | 1489 Hz |  2.83 | -2.9 dB |
| Peaking | 2807 Hz |  1.67 | 5.2 dB  |
| Peaking | 5102 Hz |  2.72 | 6.0 dB  |
| Peaking | 535 Hz  |  1.95 | -0.5 dB |
| Peaking | 920 Hz  |  2.2  | 0.9 dB  |
| Peaking | 1221 Hz |  5.33 | -0.7 dB |
| Peaking | 5841 Hz | 11.95 | 2.0 dB  |
| Peaking | 7524 Hz |  1.46 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sound%20Linear%20Fitz%2010%20Flat/Sound%20Linear%20Fitz%2010%20Flat.png)