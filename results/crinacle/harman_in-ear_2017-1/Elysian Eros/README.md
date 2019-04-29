# Elysian Eros
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.9; 25 -7.4; 28 -8.0; 31 -8.4; 34 -8.7; 37 -8.9; 41 -9.3; 45 -9.6; 49 -9.9; 54 -10.2; 60 -10.5; 66 -10.8; 72 -11.2; 79 -11.5; 87 -12.0; 96 -12.4; 106 -12.8; 116 -13.1; 128 -13.3; 141 -13.5; 155 -13.6; 170 -13.7; 187 -13.8; 206 -13.8; 227 -13.6; 249 -13.4; 274 -13.2; 302 -13.0; 332 -12.5; 365 -12.0; 402 -11.6; 442 -11.2; 486 -10.7; 535 -10.1; 588 -9.5; 647 -8.9; 712 -8.2; 783 -7.5; 861 -6.9; 947 -6.6; 1042 -6.6; 1146 -6.9; 1261 -7.1; 1387 -6.8; 1526 -6.1; 1678 -5.2; 1846 -4.3; 2031 -3.3; 2234 -2.2; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.8; 15026 -16.7; 16529 -9.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Eros GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Eros ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.5  | -2.4 dB  |
| Peaking | 219 Hz   | 0.47 | -6.3 dB  |
| Peaking | 447 Hz   | 2.48 | -0.5 dB  |
| Peaking | 3788 Hz  | 0.77 | 7.0 dB   |
| Peaking | 15031 Hz | 2.95 | -11.6 dB |
| Peaking | 1410 Hz  | 4.02 | -1.4 dB  |
| Peaking | 2550 Hz  | 3.09 | 1.5 dB   |
| Peaking | 3827 Hz  | 1.99 | -1.3 dB  |
| Peaking | 6363 Hz  | 2.24 | 3.6 dB   |
| Peaking | 7645 Hz  | 2.64 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Elysian%20Eros/Elysian%20Eros.png)