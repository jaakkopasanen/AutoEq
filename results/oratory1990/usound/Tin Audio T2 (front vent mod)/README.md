# Tin Audio T2 (front vent mod)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.3; 25 -12.2; 28 -12.1; 31 -11.9; 34 -11.8; 37 -11.7; 41 -11.5; 45 -11.4; 49 -11.2; 54 -11.1; 60 -10.9; 66 -10.8; 72 -10.8; 79 -10.7; 87 -10.6; 96 -10.5; 106 -10.4; 116 -10.3; 128 -10.1; 141 -9.9; 155 -9.6; 170 -9.2; 187 -8.8; 206 -8.3; 227 -8.5; 249 -8.1; 274 -7.6; 302 -7.2; 332 -6.7; 365 -6.4; 402 -6.1; 442 -5.7; 486 -5.4; 535 -5.0; 588 -4.7; 647 -4.4; 712 -4.0; 783 -3.7; 861 -3.6; 947 -3.8; 1042 -3.3; 1146 -3.3; 1261 -3.2; 1387 -3.0; 1526 -2.5; 1678 -1.9; 1846 -1.2; 2031 -0.9; 2234 -1.1; 2457 -1.8; 2703 -2.9; 2973 -3.2; 3270 -2.5; 3597 -1.8; 3957 -1.7; 4353 -2.3; 4788 -3.8; 5267 -4.6; 5793 -2.2; 6373 -0.5; 7010 -2.4; 7711 -6.4; 8482 -6.2; 9330 -4.8; 10263 -4.8; 11289 -5.5; 12418 -5.0; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 (front vent mod) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 (front vent mod) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.44 | -6.6 dB |
| Peaking | 113 Hz   | 0.39 | -4.6 dB |
| Peaking | 884 Hz   | 0.76 | 1.5 dB  |
| Peaking | 1998 Hz  | 2.23 | 3.2 dB  |
| Peaking | 4182 Hz  | 1.08 | 2.2 dB  |
| Peaking | 3951 Hz  | 5.5  | 0.9 dB  |
| Peaking | 5172 Hz  | 4.38 | -2.9 dB |
| Peaking | 6485 Hz  | 3.34 | 4.5 dB  |
| Peaking | 7904 Hz  | 4.64 | -4.0 dB |
| Peaking | 11638 Hz | 6.85 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Tin%20Audio%20T2%20(front%20vent%20mod)/Tin%20Audio%20T2%20(front%20vent%20mod).png)