# Satolex Tubomi DH298-A1Bk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.8; 25 -10.2; 28 -10.6; 31 -10.9; 34 -11.2; 37 -11.4; 41 -11.6; 45 -11.8; 49 -12.0; 54 -12.2; 60 -12.3; 66 -12.5; 72 -12.7; 79 -12.8; 87 -13.0; 96 -13.2; 106 -13.2; 116 -13.2; 128 -13.2; 141 -13.0; 155 -12.9; 170 -12.6; 187 -12.3; 206 -11.8; 227 -11.4; 249 -10.8; 274 -10.2; 302 -9.5; 332 -8.9; 365 -8.2; 402 -7.5; 442 -6.8; 486 -6.1; 535 -5.4; 588 -4.6; 647 -3.9; 712 -3.0; 783 -2.3; 861 -1.8; 947 -1.4; 1042 -1.4; 1146 -1.8; 1261 -2.1; 1387 -2.3; 1526 -2.3; 1678 -2.0; 1846 -1.7; 2031 -1.2; 2234 -0.7; 2457 -0.9; 2703 -2.4; 2973 -3.1; 3270 -2.6; 3597 -1.4; 3957 -0.5; 4353 -0.6; 4788 -1.8; 5267 -4.1; 5793 -7.9; 6373 -8.0; 7010 -3.8; 7711 -5.3; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -9.4; 15026 -19.7; 16529 -21.1; 18182 -17.2; 20000 -18.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH298-A1Bk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH298-A1Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.4  | -4.2 dB  |
| Peaking | 165 Hz   | 0.42 | -6.6 dB  |
| Peaking | 875 Hz   | 1.63 | 2.0 dB   |
| Peaking | 4035 Hz  | 0.11 | 4.0 dB   |
| Peaking | 17048 Hz | 0.72 | -18.2 dB |
| Peaking | 4453 Hz  | 3.03 | 3.1 dB   |
| Peaking | 6154 Hz  | 3.1  | -6.8 dB  |
| Peaking | 6885 Hz  | 7.59 | 3.3 dB   |
| Peaking | 12927 Hz | 2.13 | 6.1 dB   |
| Peaking | 15001 Hz | 3.33 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -17.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Satolex%20Tubomi%20DH298-A1Bk/Satolex%20Tubomi%20DH298-A1Bk.png)