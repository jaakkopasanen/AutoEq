# Jomo Salsa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.7; 28 -5.0; 31 -5.3; 34 -5.5; 37 -5.7; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.6; 60 -6.9; 66 -7.2; 72 -7.6; 79 -8.1; 87 -8.4; 96 -8.9; 106 -9.3; 116 -9.7; 128 -10.0; 141 -10.3; 155 -10.5; 170 -10.6; 187 -10.7; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.4; 535 -7.9; 588 -7.3; 647 -6.7; 712 -6.0; 783 -5.3; 861 -4.9; 947 -5.2; 1042 -6.3; 1146 -8.1; 1261 -9.5; 1387 -9.9; 1526 -9.3; 1678 -8.3; 1846 -7.0; 2031 -5.3; 2234 -3.2; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.9; 5267 -1.6; 5793 -2.2; 6373 -6.3; 7010 -9.1; 7711 -7.8; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -13.4; 16529 -17.9; 18182 -15.2; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Salsa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Salsa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 199 Hz   | 0.72 | -4.6 dB  |
| Peaking | 1493 Hz  | 2.84 | -4.7 dB  |
| Peaking | 2831 Hz  | 1.49 | 5.7 dB   |
| Peaking | 4403 Hz  | 1.82 | 3.8 dB   |
| Peaking | 17267 Hz | 1.28 | -12.2 dB |
| Peaking | 21 Hz    | 1.13 | 2.4 dB   |
| Peaking | 849 Hz   | 4.09 | 2.5 dB   |
| Peaking | 5694 Hz  | 6.9  | 3.3 dB   |
| Peaking | 6945 Hz  | 4.82 | -4.0 dB  |
| Peaking | 13022 Hz | 3.23 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -10.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Salsa/Jomo%20Salsa.png)