# BGVP DM6 20 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.2; 25 -1.8; 28 -2.4; 31 -3.0; 34 -3.4; 37 -3.8; 41 -4.3; 45 -4.7; 49 -5.1; 54 -5.6; 60 -6.0; 66 -6.4; 72 -6.9; 79 -7.3; 87 -7.9; 96 -8.3; 106 -8.8; 116 -9.3; 128 -9.6; 141 -9.9; 155 -10.1; 170 -10.4; 187 -10.5; 206 -10.7; 227 -10.7; 249 -10.6; 274 -10.6; 302 -10.5; 332 -10.4; 365 -10.1; 402 -9.9; 442 -9.7; 486 -9.4; 535 -9.1; 588 -8.7; 647 -8.2; 712 -7.7; 783 -7.1; 861 -6.6; 947 -6.2; 1042 -6.3; 1146 -6.8; 1261 -7.4; 1387 -7.6; 1526 -7.2; 1678 -6.4; 1846 -5.2; 2031 -4.1; 2234 -3.2; 2457 -2.0; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -2.5; 4353 -4.9; 4788 -3.6; 5267 -1.3; 5793 -1.7; 6373 -5.2; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.3; 16529 -10.9; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 20 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 20 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.42 | 7.3 dB  |
| Peaking | 222 Hz   |  0.49 | -4.5 dB |
| Peaking | 3030 Hz  |  1.52 | 7.3 dB  |
| Peaking | 5544 Hz  |  4.54 | 5.3 dB  |
| Peaking | 13006 Hz |  0.08 | -1.1 dB |
| Peaking | 943 Hz   |  3.34 | 1.3 dB  |
| Peaking | 1418 Hz  |  4.06 | -1.5 dB |
| Peaking | 4438 Hz  | 12.16 | -1.7 dB |
| Peaking | 16245 Hz |  0.57 | 2.9 dB  |
| Peaking | 16251 Hz |  1.86 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DM6%2020%20Ohm/BGVP%20DM6%2020%20Ohm.png)