# BGVP DM6 M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.7; 25 -4.3; 28 -5.0; 31 -5.5; 34 -5.9; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.6; 54 -8.0; 60 -8.4; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.2; 96 -10.6; 106 -11.1; 116 -11.4; 128 -11.7; 141 -11.9; 155 -12.0; 170 -12.2; 187 -12.2; 206 -12.2; 227 -12.1; 249 -11.8; 274 -11.6; 302 -11.3; 332 -11.0; 365 -10.6; 402 -10.1; 442 -9.7; 486 -9.2; 535 -8.7; 588 -8.1; 647 -7.4; 712 -6.7; 783 -6.0; 861 -5.3; 947 -4.9; 1042 -4.9; 1146 -5.3; 1261 -5.7; 1387 -5.9; 1526 -5.5; 1678 -4.8; 1846 -3.8; 2031 -2.9; 2234 -2.0; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.1; 4353 -3.2; 4788 -1.8; 5267 -0.8; 5793 -2.2; 6373 -5.4; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -12.3; 16529 -12.3; 18182 -8.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.26 | 3.9 dB  |
| Peaking | 180 Hz   | 0.51 | -6.0 dB |
| Peaking | 2925 Hz  | 1.03 | 6.3 dB  |
| Peaking | 5338 Hz  | 5.42 | 4.0 dB  |
| Peaking | 16101 Hz | 1.84 | -7.1 dB |
| Peaking | 438 Hz   | 1.62 | -0.8 dB |
| Peaking | 939 Hz   | 1.73 | 2.0 dB  |
| Peaking | 1433 Hz  | 2.53 | -1.4 dB |
| Peaking | 7569 Hz  | 2.51 | -0.6 dB |
| Peaking | 12958 Hz | 5.18 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DM6%20M/BGVP%20DM6%20M.png)