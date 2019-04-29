# Massdrop Plus sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.8; 28 -7.2; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.6; 54 -8.9; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.3; 128 -11.5; 141 -11.6; 155 -11.7; 170 -11.7; 187 -11.6; 206 -11.5; 227 -11.3; 249 -11.0; 274 -10.6; 302 -10.3; 332 -9.9; 365 -9.5; 402 -9.0; 442 -8.6; 486 -8.1; 535 -7.7; 588 -7.2; 647 -6.7; 712 -6.2; 783 -5.7; 861 -5.3; 947 -5.2; 1042 -5.6; 1146 -6.4; 1261 -7.4; 1387 -8.0; 1526 -8.1; 1678 -7.9; 1846 -7.5; 2031 -7.0; 2234 -6.5; 2457 -5.9; 2703 -5.1; 2973 -4.2; 3270 -3.2; 3597 -2.1; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.54 | -1.1 dB |
| Peaking | 184 Hz  | 0.48 | -4.6 dB |
| Peaking | 954 Hz  | 1.23 | 3.1 dB  |
| Peaking | 1459 Hz | 1.37 | -3.2 dB |
| Peaking | 4704 Hz | 1.35 | 6.9 dB  |
| Peaking | 13 Hz   | 1.88 | 1.0 dB  |
| Peaking | 3711 Hz | 2.9  | 0.8 dB  |
| Peaking | 4739 Hz | 4.27 | -1.0 dB |
| Peaking | 6389 Hz | 3.32 | 4.1 dB  |
| Peaking | 7371 Hz | 1.64 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Massdrop%20Plus%20sample%201/Massdrop%20Plus%20sample%201.png)