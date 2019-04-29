# Venture Electronics Monk IE Smalls
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.8; 28 -9.0; 31 -9.2; 34 -9.3; 37 -9.5; 41 -9.6; 45 -9.8; 49 -10.0; 54 -10.2; 60 -10.5; 66 -10.8; 72 -11.1; 79 -11.5; 87 -11.9; 96 -12.3; 106 -12.8; 116 -13.1; 128 -13.5; 141 -13.9; 155 -14.1; 170 -14.3; 187 -14.5; 206 -14.7; 227 -14.7; 249 -14.8; 274 -14.8; 302 -14.7; 332 -14.4; 365 -14.2; 402 -14.0; 442 -13.7; 486 -13.3; 535 -12.8; 588 -12.2; 647 -11.4; 712 -10.5; 783 -9.5; 861 -8.4; 947 -7.5; 1042 -7.0; 1146 -6.7; 1261 -6.4; 1387 -5.7; 1526 -4.7; 1678 -3.7; 1846 -2.7; 2031 -1.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.3; 5267 -3.2; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -19.8; 16529 -22.3; 18182 -14.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk IE Smalls GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk IE Smalls ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 69 Hz    | 0.1  | -1.9 dB  |
| Peaking | 298 Hz   | 0.32 | -7.2 dB  |
| Peaking | 2896 Hz  | 0.69 | 4.9 dB   |
| Peaking | 4534 Hz  | 0.14 | 2.4 dB   |
| Peaking | 16295 Hz | 1.62 | -19.5 dB |
| Peaking | 923 Hz   | 6.33 | 0.8 dB   |
| Peaking | 6329 Hz  | 4.23 | 4.8 dB   |
| Peaking | 7339 Hz  | 1.71 | -3.1 dB  |
| Peaking | 12982 Hz | 5.01 | 4.3 dB   |
| Peaking | 17596 Hz | 4.77 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -7.0 dB  |
| Peaking | 500 Hz   | 1.41 | -5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Venture%20Electronics%20Monk%20IE%20Smalls/Venture%20Electronics%20Monk%20IE%20Smalls.png)