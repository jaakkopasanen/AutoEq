# Jomo Samba
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.1; 25 -6.3; 28 -6.5; 31 -6.7; 34 -6.9; 37 -7.0; 41 -7.3; 45 -7.6; 49 -7.7; 54 -7.9; 60 -8.2; 66 -8.5; 72 -8.8; 79 -9.2; 87 -9.5; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.0; 187 -11.0; 206 -10.9; 227 -10.7; 249 -10.5; 274 -10.3; 302 -9.9; 332 -9.4; 365 -8.9; 402 -8.6; 442 -8.2; 486 -7.7; 535 -7.2; 588 -6.7; 647 -6.2; 712 -5.7; 783 -5.2; 861 -4.8; 947 -4.7; 1042 -4.9; 1146 -5.4; 1261 -5.8; 1387 -5.9; 1526 -5.6; 1678 -5.1; 1846 -4.5; 2031 -3.8; 2234 -3.3; 2457 -2.2; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -4.1; 4353 -2.7; 4788 -1.0; 5267 -3.0; 5793 -4.2; 6373 -4.1; 7010 -6.4; 7711 -10.2; 8482 -11.3; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -18.4; 16529 -28.5; 18182 -28.3; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Samba GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Samba ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 0.57 | -4.8 dB  |
| Peaking | 5914 Hz  | 0.35 | 8.0 dB   |
| Peaking | 8068 Hz  | 3.56 | -7.3 dB  |
| Peaking | 13089 Hz | 1.52 | 10.9 dB  |
| Peaking | 17034 Hz | 0.64 | -28.3 dB |
| Peaking | 889 Hz   | 1.27 | 3.6 dB   |
| Peaking | 1415 Hz  | 0.52 | -3.1 dB  |
| Peaking | 3000 Hz  | 1.38 | 3.4 dB   |
| Peaking | 4047 Hz  | 9.21 | -4.0 dB  |
| Peaking | 18311 Hz | 5.7  | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -20.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Samba/Jomo%20Samba.png)