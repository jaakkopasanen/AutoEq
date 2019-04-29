# Onkyo E900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.0; 28 -6.3; 31 -6.6; 34 -6.9; 37 -7.1; 41 -7.4; 45 -7.7; 49 -7.9; 54 -8.2; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.9; 96 -10.4; 106 -10.7; 116 -10.9; 128 -11.1; 141 -11.3; 155 -11.4; 170 -11.4; 187 -11.3; 206 -11.2; 227 -11.0; 249 -10.7; 274 -10.5; 302 -10.2; 332 -9.8; 365 -9.4; 402 -9.2; 442 -9.0; 486 -8.8; 535 -8.5; 588 -8.2; 647 -8.0; 712 -7.6; 783 -7.2; 861 -6.8; 947 -6.7; 1042 -6.8; 1146 -7.1; 1261 -7.3; 1387 -7.0; 1526 -6.3; 1678 -5.5; 1846 -4.6; 2031 -3.6; 2234 -2.6; 2457 -1.9; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -3.8; 5793 -4.7; 6373 -8.5; 7010 -10.6; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.2; 12418 -11.4; 13660 -19.1; 15026 -25.9; 16529 -28.8; 18182 -28.1; 20000 -23.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo E900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo E900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 201 Hz   | 0.37 | -5.0 dB  |
| Peaking | 1361 Hz  | 1.16 | -4.8 dB  |
| Peaking | 6812 Hz  | 2.44 | -12.8 dB |
| Peaking | 7618 Hz  | 0.28 | 24.0 dB  |
| Peaking | 16604 Hz | 0.31 | -35.0 dB |
| Peaking | 18 Hz    | 1.31 | 1.6 dB   |
| Peaking | 7734 Hz  | 5.46 | 1.4 dB   |
| Peaking | 8688 Hz  | 2.36 | -2.1 dB  |
| Peaking | 11486 Hz | 2.56 | 3.7 dB   |
| Peaking | 14313 Hz | 3.54 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -28.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Onkyo%20E900/Onkyo%20E900.png)