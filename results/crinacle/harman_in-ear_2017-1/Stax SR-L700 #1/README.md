# Stax SR-L700 #1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -2.6; 66 -4.2; 72 -4.6; 79 -4.9; 87 -5.5; 96 -5.7; 106 -5.9; 116 -6.2; 128 -6.6; 141 -6.8; 155 -6.9; 170 -6.9; 187 -7.0; 206 -7.1; 227 -7.2; 249 -7.2; 274 -7.5; 302 -7.6; 332 -7.6; 365 -7.9; 402 -8.3; 442 -8.4; 486 -8.1; 535 -8.1; 588 -8.4; 647 -8.8; 712 -9.3; 783 -9.6; 861 -9.6; 947 -10.6; 1042 -10.8; 1146 -11.1; 1261 -10.7; 1387 -9.5; 1526 -8.0; 1678 -6.9; 1846 -5.6; 2031 -4.8; 2234 -3.6; 2457 -3.7; 2703 -3.5; 2973 -2.6; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -5.2; 5793 -7.6; 6373 -5.8; 7010 -4.3; 7711 -6.2; 8482 -7.0; 9330 -10.5; 10263 -8.7; 11289 -6.5; 12418 -8.3; 13660 -18.9; 15026 -26.9; 16529 -30.0; 18182 -30.7; 20000 -26.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.84 | 7.0 dB   |
| Peaking | 1141 Hz  | 0.63 | -9.9 dB  |
| Peaking | 7583 Hz  | 0.12 | 11.3 dB  |
| Peaking | 16420 Hz | 0.54 | -29.4 dB |
| Peaking | 19310 Hz | 0.9  | -13.8 dB |
| Peaking | 4334 Hz  | 2.47 | 2.6 dB   |
| Peaking | 5684 Hz  | 3.8  | -5.4 dB  |
| Peaking | 12025 Hz | 4.32 | 7.5 dB   |
| Peaking | 14492 Hz | 3.96 | -4.6 dB  |
| Peaking | 20292 Hz | 1.99 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB   |
| Peaking | 62 Hz    | 1.41 | 2.4 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -30.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-L700%20#1/Stax%20SR-L700%20#1.png)