# Stax SR-L700 #4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.8; 66 -3.2; 72 -3.5; 79 -4.0; 87 -4.4; 96 -4.6; 106 -4.7; 116 -5.1; 128 -5.4; 141 -5.5; 155 -5.6; 170 -5.8; 187 -6.0; 206 -6.0; 227 -6.0; 249 -6.0; 274 -6.2; 302 -6.6; 332 -6.6; 365 -6.7; 402 -6.8; 442 -7.0; 486 -7.2; 535 -7.5; 588 -7.8; 647 -8.2; 712 -8.7; 783 -9.0; 861 -8.8; 947 -9.6; 1042 -9.7; 1146 -10.0; 1261 -9.7; 1387 -9.1; 1526 -8.1; 1678 -6.8; 1846 -5.3; 2031 -4.8; 2234 -4.0; 2457 -4.8; 2703 -4.8; 2973 -4.2; 3270 -3.4; 3597 -3.8; 3957 -3.0; 4353 -2.0; 4788 -2.3; 5267 -5.2; 5793 -8.7; 6373 -7.9; 7010 -6.9; 7711 -7.0; 8482 -8.6; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -12.8; 15026 -11.9; 16529 -9.5; 18182 -11.6; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.56 | 6.6 dB  |
| Peaking | 1242 Hz  | 0.89 | -5.2 dB |
| Peaking | 2126 Hz  | 1.04 | 4.5 dB  |
| Peaking | 4382 Hz  | 3.9  | 4.7 dB  |
| Peaking | 20622 Hz | 0.15 | -6.7 dB |
| Peaking | 5065 Hz  | 5.07 | 2.0 dB  |
| Peaking | 5781 Hz  | 5.04 | -3.4 dB |
| Peaking | 11226 Hz | 4.57 | 2.9 dB  |
| Peaking | 18238 Hz | 2.51 | -0.6 dB |
| Peaking | 20012 Hz | 3.81 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-L700%20#4/Stax%20SR-L700%20#4.png)