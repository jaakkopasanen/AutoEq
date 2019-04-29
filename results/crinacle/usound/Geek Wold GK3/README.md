# Geek Wold GK3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.1; 25 -11.4; 28 -11.7; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.3; 60 -12.3; 66 -12.3; 72 -12.4; 79 -12.4; 87 -12.4; 96 -12.4; 106 -12.5; 116 -12.4; 128 -12.3; 141 -12.1; 155 -11.9; 170 -11.6; 187 -11.3; 206 -10.9; 227 -10.5; 249 -10.1; 274 -9.6; 302 -9.1; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.4; 486 -7.0; 535 -6.6; 588 -6.3; 647 -5.9; 712 -5.5; 783 -5.1; 861 -4.8; 947 -5.0; 1042 -5.6; 1146 -6.4; 1261 -6.3; 1387 -7.3; 1526 -7.8; 1678 -8.0; 1846 -8.8; 2031 -10.3; 2234 -12.2; 2457 -13.1; 2703 -11.9; 2973 -11.1; 3270 -11.9; 3597 -14.4; 3957 -13.7; 4353 -8.0; 4788 -3.8; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Geek Wold GK3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Geek Wold GK3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.36 | -5.6 dB |
| Peaking | 161 Hz  | 0.89 | -3.3 dB |
| Peaking | 2408 Hz | 2.8  | -6.3 dB |
| Peaking | 3750 Hz | 3.62 | -9.4 dB |
| Peaking | 5593 Hz | 2.43 | 7.6 dB  |
| Peaking | 298 Hz  | 2.47 | -0.6 dB |
| Peaking | 831 Hz  | 2.08 | 2.2 dB  |
| Peaking | 6590 Hz | 6.7  | 2.4 dB  |
| Peaking | 7554 Hz | 2.15 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Geek%20Wold%20GK3/Geek%20Wold%20GK3.png)