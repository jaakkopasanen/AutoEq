# Quad Era-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.9; 25 -5.1; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.8; 45 -6.0; 49 -6.0; 54 -6.3; 60 -6.6; 66 -6.7; 72 -6.9; 79 -7.2; 87 -7.6; 96 -7.9; 106 -8.3; 116 -8.7; 128 -9.1; 141 -9.5; 155 -9.6; 170 -9.5; 187 -9.4; 206 -9.4; 227 -9.3; 249 -8.9; 274 -8.8; 302 -8.8; 332 -8.9; 365 -8.4; 402 -8.2; 442 -8.1; 486 -8.0; 535 -7.8; 588 -8.0; 647 -8.1; 712 -8.6; 783 -9.1; 861 -10.0; 947 -11.3; 1042 -11.7; 1146 -10.6; 1261 -8.8; 1387 -6.6; 1526 -4.4; 1678 -2.5; 1846 -1.1; 2031 -0.6; 2234 -0.5; 2457 -0.6; 2703 -1.0; 2973 -2.2; 3270 -3.1; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.1; 5793 -6.4; 6373 -9.3; 7010 -8.4; 7711 -9.9; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -6.5; 15026 -8.7; 16529 -14.2; 18182 -16.3; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Quad Era-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Quad Era-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 193 Hz   | 0.74 | -3.1 dB  |
| Peaking | 1050 Hz  | 1.75 | -6.6 dB  |
| Peaking | 2085 Hz  | 1.28 | 7.2 dB   |
| Peaking | 4277 Hz  | 3.27 | 5.8 dB   |
| Peaking | 18647 Hz | 0.88 | -11.0 dB |
| Peaking | 19 Hz    | 1.2  | 1.8 dB   |
| Peaking | 39 Hz    | 1.63 | 0.7 dB   |
| Peaking | 5056 Hz  | 5.74 | 3.2 dB   |
| Peaking | 6737 Hz  | 2.17 | -3.7 dB  |
| Peaking | 13189 Hz | 1.97 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.0 dB |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Quad%20Era-1/Quad%20Era-1.png)