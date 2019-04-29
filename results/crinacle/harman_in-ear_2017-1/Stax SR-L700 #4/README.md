# Stax SR-L700 #4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -2.9; 66 -4.4; 72 -4.7; 79 -5.1; 87 -5.5; 96 -5.7; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.7; 155 -6.8; 170 -7.0; 187 -7.1; 206 -7.1; 227 -7.1; 249 -7.2; 274 -7.4; 302 -7.7; 332 -7.6; 365 -7.6; 402 -7.6; 442 -7.8; 486 -8.0; 535 -8.2; 588 -8.5; 647 -8.9; 712 -9.4; 783 -9.7; 861 -9.5; 947 -10.3; 1042 -10.5; 1146 -10.8; 1261 -10.2; 1387 -9.3; 1526 -8.0; 1678 -6.7; 1846 -5.1; 2031 -4.2; 2234 -2.9; 2457 -3.1; 2703 -2.7; 2973 -1.9; 3270 -1.2; 3597 -1.9; 3957 -1.4; 4353 -0.9; 4788 -1.4; 5267 -4.3; 5793 -7.6; 6373 -6.4; 7010 -4.8; 7711 -6.2; 8482 -7.0; 9330 -9.4; 10263 -7.1; 11289 -6.5; 12418 -9.2; 13660 -21.7; 15026 -28.2; 16529 -28.4; 18182 -28.1; 20000 -27.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.85 | 7.0 dB   |
| Peaking | 1113 Hz  | 0.68 | -9.1 dB  |
| Peaking | 7328 Hz  | 0.13 | 10.9 dB  |
| Peaking | 15170 Hz | 2.8  | -12.7 dB |
| Peaking | 18402 Hz | 0.31 | -28.1 dB |
| Peaking | 4711 Hz  | 2.98 | 2.2 dB   |
| Peaking | 5786 Hz  | 4.27 | -5.5 dB  |
| Peaking | 9292 Hz  | 5.36 | -3.2 dB  |
| Peaking | 11918 Hz | 2.49 | 7.2 dB   |
| Peaking | 13822 Hz | 3.87 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 16000 Hz | 1.41 | -30.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-L700%20#4/Stax%20SR-L700%20#4.png)