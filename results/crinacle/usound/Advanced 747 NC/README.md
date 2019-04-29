# Advanced 747 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.9; 25 -11.4; 28 -12.1; 31 -12.6; 34 -13.0; 37 -13.3; 41 -13.6; 45 -13.9; 49 -14.2; 54 -14.5; 60 -14.7; 66 -15.0; 72 -15.2; 79 -15.5; 87 -15.7; 96 -16.0; 106 -16.1; 116 -16.1; 128 -16.1; 141 -15.9; 155 -15.8; 170 -15.4; 187 -15.0; 206 -14.5; 227 -13.9; 249 -13.3; 274 -12.6; 302 -11.8; 332 -11.1; 365 -10.2; 402 -9.4; 442 -8.6; 486 -7.8; 535 -6.9; 588 -6.0; 647 -5.0; 712 -4.0; 783 -2.9; 861 -2.0; 947 -1.2; 1042 -0.8; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -0.7; 1678 -0.8; 1846 -0.8; 2031 -0.7; 2234 -0.8; 2457 -1.2; 2703 -2.1; 2973 -2.9; 3270 -2.8; 3597 -1.8; 3957 -0.9; 4353 -0.8; 4788 -1.6; 5267 -3.5; 5793 -6.6; 6373 -5.3; 7010 -4.0; 7711 -7.0; 8482 -6.9; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -9.5; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced 747 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced 747 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.4  | -4.4 dB |
| Peaking | 162 Hz   | 0.38 | -8.3 dB |
| Peaking | 1269 Hz  | 0.52 | 7.0 dB  |
| Peaking | 4278 Hz  | 3.34 | 4.2 dB  |
| Peaking | 995 Hz   | 1.72 | 1.4 dB  |
| Peaking | 1192 Hz  | 0.86 | -1.2 dB |
| Peaking | 2236 Hz  | 3.48 | 1.3 dB  |
| Peaking | 8085 Hz  | 9.44 | -2.3 dB |
| Peaking | 19309 Hz | 1.6  | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20747%20NC/Advanced%20747%20NC.png)