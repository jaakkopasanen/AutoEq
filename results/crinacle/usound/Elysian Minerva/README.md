# Elysian Minerva
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.6; 25 -6.0; 28 -6.5; 31 -6.9; 34 -7.2; 37 -7.5; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.7; 60 -9.0; 66 -9.3; 72 -9.7; 79 -10.1; 87 -10.5; 96 -10.8; 106 -11.2; 116 -11.5; 128 -11.8; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.0; 206 -12.0; 227 -11.8; 249 -11.5; 274 -11.2; 302 -10.9; 332 -10.6; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.3; 783 -7.1; 861 -7.1; 947 -7.4; 1042 -7.9; 1146 -8.6; 1261 -8.7; 1387 -8.0; 1526 -6.7; 1678 -5.3; 1846 -3.9; 2031 -2.8; 2234 -2.2; 2457 -2.1; 2703 -2.1; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -1.0; 6373 -2.0; 7010 -7.2; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -10.8; 16529 -7.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Minerva GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Minerva ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 0.77 | -2.0 dB |
| Peaking | 214 Hz   | 0.56 | -4.8 dB |
| Peaking | 1273 Hz  | 2.49 | -3.8 dB |
| Peaking | 3921 Hz  | 0.6  | 8.3 dB  |
| Peaking | 9276 Hz  | 0.31 | -2.9 dB |
| Peaking | 21 Hz    | 2.4  | 1.8 dB  |
| Peaking | 6170 Hz  | 6.46 | 4.7 dB  |
| Peaking | 6934 Hz  | 3.29 | -4.1 dB |
| Peaking | 15035 Hz | 0.85 | 3.6 dB  |
| Peaking | 15321 Hz | 2.62 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Elysian%20Minerva/Elysian%20Minerva.png)