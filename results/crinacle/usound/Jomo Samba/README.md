# Jomo Samba
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.6; 25 -3.8; 28 -4.0; 31 -4.2; 34 -4.4; 37 -4.5; 41 -4.8; 45 -5.1; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.0; 96 -7.4; 106 -7.7; 116 -8.0; 128 -8.2; 141 -8.4; 155 -8.5; 170 -8.5; 187 -8.5; 206 -8.4; 227 -8.2; 249 -8.0; 274 -7.7; 302 -7.4; 332 -7.1; 365 -6.7; 402 -6.4; 442 -6.1; 486 -5.6; 535 -5.2; 588 -4.7; 647 -4.2; 712 -3.7; 783 -3.1; 861 -2.7; 947 -2.5; 1042 -2.7; 1146 -3.3; 1261 -4.0; 1387 -4.3; 1526 -4.3; 1678 -3.9; 1846 -3.4; 2031 -3.0; 2234 -3.1; 2457 -2.6; 2703 -1.2; 2973 -0.6; 3270 -0.7; 3597 -1.0; 3957 -4.4; 4353 -2.5; 4788 -0.5; 5267 -2.5; 5793 -4.0; 6373 -4.2; 7010 -7.4; 7711 -11.9; 8482 -11.7; 9330 -5.9; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -8.3; 18182 -10.4; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Samba GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Samba ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 188 Hz   | 0.64 | -3.8 dB  |
| Peaking | 3185 Hz  | 0.21 | 2.8 dB   |
| Peaking | 4828 Hz  | 6.97 | 2.5 dB   |
| Peaking | 8061 Hz  | 3.53 | -10.3 dB |
| Peaking | 17607 Hz | 1.93 | -6.6 dB  |
| Peaking | 22 Hz    | 1.04 | 1.8 dB   |
| Peaking | 943 Hz   | 1.49 | 3.6 dB   |
| Peaking | 1214 Hz  | 0.8  | -3.1 dB  |
| Peaking | 3217 Hz  | 2.11 | 2.9 dB   |
| Peaking | 4022 Hz  | 8.53 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Samba/Jomo%20Samba.png)