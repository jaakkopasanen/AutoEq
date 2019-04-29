# Venture Electronics Monk IE Smalls
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.7; 28 -7.9; 31 -8.0; 34 -8.2; 37 -8.3; 41 -8.5; 45 -8.6; 49 -8.8; 54 -9.1; 60 -9.3; 66 -9.6; 72 -10.0; 79 -10.3; 87 -10.7; 96 -11.2; 106 -11.6; 116 -12.0; 128 -12.4; 141 -12.7; 155 -13.0; 170 -13.2; 187 -13.4; 206 -13.5; 227 -13.6; 249 -13.6; 274 -13.6; 302 -13.6; 332 -13.5; 365 -13.3; 402 -13.2; 442 -12.9; 486 -12.5; 535 -12.1; 588 -11.5; 647 -10.7; 712 -9.8; 783 -8.8; 861 -7.7; 947 -6.8; 1042 -6.2; 1146 -6.0; 1261 -5.9; 1387 -5.5; 1526 -4.8; 1678 -3.9; 1846 -2.9; 2031 -2.0; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.1; 5267 -4.0; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk IE Smalls GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk IE Smalls ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 124 Hz   | 0.41 | -3.5 dB |
| Peaking | 253 Hz   | 0.66 | -4.1 dB |
| Peaking | 510 Hz   | 1.27 | -3.2 dB |
| Peaking | 2942 Hz  | 0.88 | 6.7 dB  |
| Peaking | 6194 Hz  | 6.47 | 4.2 dB  |
| Peaking | 2383 Hz  | 2.98 | 1.0 dB  |
| Peaking | 2753 Hz  | 2.35 | -1.1 dB |
| Peaking | 4224 Hz  | 7.29 | 1.8 dB  |
| Peaking | 8012 Hz  | 5.55 | -1.1 dB |
| Peaking | 10110 Hz | 1.84 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -5.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Venture%20Electronics%20Monk%20IE%20Smalls/Venture%20Electronics%20Monk%20IE%20Smalls.png)