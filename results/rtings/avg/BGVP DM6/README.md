# BGVP DM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.9; 60 -1.6; 66 -2.2; 72 -2.8; 79 -3.4; 87 -4.1; 96 -5.0; 106 -5.8; 116 -6.6; 128 -7.4; 141 -8.1; 155 -8.7; 170 -9.1; 187 -9.5; 206 -9.8; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.5; 332 -9.3; 365 -8.9; 402 -8.6; 442 -8.1; 486 -7.6; 535 -6.9; 588 -6.3; 647 -5.6; 712 -5.0; 783 -4.5; 861 -4.2; 947 -4.4; 1042 -5.0; 1146 -5.4; 1261 -5.7; 1387 -5.7; 1526 -5.4; 1678 -5.0; 1846 -4.6; 2031 -3.8; 2234 -2.1; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.3; 3957 -6.0; 4353 -8.5; 4788 -6.8; 5267 -6.5; 5793 -9.3; 6373 -12.8; 7010 -11.1; 7711 -10.4; 8482 -9.8; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.1; 16529 -12.7; 18182 -11.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.45 | 6.6 dB  |
| Peaking | 205 Hz   | 0.89 | -4.6 dB |
| Peaking | 2772 Hz  | 1.57 | 6.8 dB  |
| Peaking | 6656 Hz  | 2.27 | -6.3 dB |
| Peaking | 17297 Hz | 1.95 | -7.5 dB |
| Peaking | 837 Hz   | 2.63 | 2.6 dB  |
| Peaking | 3524 Hz  | 3.49 | 4.8 dB  |
| Peaking | 4316 Hz  | 1.75 | -6.1 dB |
| Peaking | 5103 Hz  | 3.67 | 5.1 dB  |
| Peaking | 12104 Hz | 1.56 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/BGVP%20DM6/BGVP%20DM6.png)