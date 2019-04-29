# FiiO FH5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.7; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.0; 37 -10.0; 41 -10.0; 45 -10.0; 49 -10.0; 54 -10.0; 60 -9.9; 66 -9.9; 72 -10.0; 79 -10.0; 87 -10.1; 96 -10.2; 106 -10.3; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.2; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.7; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.8; 647 -7.7; 712 -7.6; 783 -7.5; 861 -7.7; 947 -8.1; 1042 -8.8; 1146 -9.6; 1261 -9.8; 1387 -9.3; 1526 -8.3; 1678 -7.7; 1846 -7.5; 2031 -7.6; 2234 -6.8; 2457 -4.8; 2703 -2.8; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -5.2; 5793 -3.7; 6373 -3.7; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -18.8; 16529 -23.3; 18182 -20.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO FH5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO FH5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 75 Hz    | 0.2  | -3.8 dB  |
| Peaking | 1713 Hz  | 0.85 | -4.3 dB  |
| Peaking | 3614 Hz  | 0.92 | 8.4 dB   |
| Peaking | 12298 Hz | 1.4  | 8.3 dB   |
| Peaking | 16587 Hz | 0.74 | -19.4 dB |
| Peaking | 807 Hz   | 2.12 | 0.8 dB   |
| Peaking | 1242 Hz  | 2.4  | -2.1 dB  |
| Peaking | 1663 Hz  | 1.58 | 1.8 dB   |
| Peaking | 2132 Hz  | 4.46 | -1.9 dB  |
| Peaking | 18398 Hz | 5.46 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -17.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20FH5/FiiO%20FH5.png)