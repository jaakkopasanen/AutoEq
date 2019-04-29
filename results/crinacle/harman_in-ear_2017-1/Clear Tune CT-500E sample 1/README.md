# Clear Tune CT-500E sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.8; 28 -5.9; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.4; 45 -6.5; 49 -6.7; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.8; 79 -8.1; 87 -8.5; 96 -9.0; 106 -9.3; 116 -9.7; 128 -10.0; 141 -10.3; 155 -10.5; 170 -10.7; 187 -10.8; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.3; 402 -8.8; 442 -8.3; 486 -7.7; 535 -6.9; 588 -6.1; 647 -5.1; 712 -4.0; 783 -2.7; 861 -1.6; 947 -1.0; 1042 -1.2; 1146 -2.7; 1261 -4.8; 1387 -7.2; 1526 -9.6; 1678 -11.1; 1846 -10.8; 2031 -9.5; 2234 -7.9; 2457 -6.4; 2703 -5.3; 2973 -4.5; 3270 -4.0; 3597 -4.3; 3957 -5.9; 4353 -7.2; 4788 -6.6; 5267 -3.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -17.0; 16529 -10.3; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 401 Hz   | 0.32 | -7.2 dB  |
| Peaking | 1045 Hz  | 0.59 | 12.9 dB  |
| Peaking | 1662 Hz  | 1.69 | -11.6 dB |
| Peaking | 6065 Hz  | 4.68 | 6.3 dB   |
| Peaking | 15244 Hz | 3.62 | -12.0 dB |
| Peaking | 22 Hz    | 1.23 | 1.0 dB   |
| Peaking | 53 Hz    | 2.28 | 0.5 dB   |
| Peaking | 3281 Hz  | 4.01 | 1.8 dB   |
| Peaking | 4461 Hz  | 6.21 | -2.8 dB  |
| Peaking | 12953 Hz | 6.91 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-500E%20sample%201/Clear%20Tune%20CT-500E%20sample%201.png)