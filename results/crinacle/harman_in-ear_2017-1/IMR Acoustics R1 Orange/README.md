# IMR Acoustics R1 Orange
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.3; 25 -5.6; 28 -5.9; 31 -6.0; 34 -6.0; 37 -6.1; 41 -6.3; 45 -6.6; 49 -6.8; 54 -6.9; 60 -7.0; 66 -7.4; 72 -7.7; 79 -7.9; 87 -8.4; 96 -9.1; 106 -9.5; 116 -9.9; 128 -10.1; 141 -10.4; 155 -10.6; 170 -10.8; 187 -11.0; 206 -11.3; 227 -11.1; 249 -11.1; 274 -11.0; 302 -10.8; 332 -10.3; 365 -9.8; 402 -9.4; 442 -8.9; 486 -8.4; 535 -7.7; 588 -7.0; 647 -6.3; 712 -5.4; 783 -4.7; 861 -4.0; 947 -3.6; 1042 -3.5; 1146 -3.8; 1261 -3.9; 1387 -3.7; 1526 -3.3; 1678 -2.7; 1846 -2.2; 2031 -1.6; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -1.5; 3597 -3.0; 3957 -5.5; 4353 -8.4; 4788 -10.1; 5267 -7.5; 5793 -3.7; 6373 -1.6; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -11.7; 15026 -22.6; 16529 -30.2; 18182 -29.5; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Orange GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Orange ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 217 Hz   | 0.57 | -5.5 dB  |
| Peaking | 4646 Hz  | 2.41 | -13.5 dB |
| Peaking | 5331 Hz  | 0.43 | 15.9 dB  |
| Peaking | 12604 Hz | 1.67 | 13.1 dB  |
| Peaking | 16759 Hz | 0.4  | -30.2 dB |
| Peaking | 16 Hz    | 1.23 | 1.6 dB   |
| Peaking | 900 Hz   | 2.97 | 1.4 dB   |
| Peaking | 1431 Hz  | 2.86 | -1.0 dB  |
| Peaking | 6527 Hz  | 7.87 | 2.5 dB   |
| Peaking | 7606 Hz  | 4.04 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 16000 Hz | 1.41 | -26.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/IMR%20Acoustics%20R1%20Orange/IMR%20Acoustics%20R1%20Orange.png)