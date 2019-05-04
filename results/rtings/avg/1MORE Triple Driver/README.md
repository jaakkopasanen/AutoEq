# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.5; 28 -8.8; 31 -9.1; 34 -9.3; 37 -9.5; 41 -9.6; 45 -9.8; 49 -9.9; 54 -10.0; 60 -10.1; 66 -10.3; 72 -10.4; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.9; 116 -10.9; 128 -10.9; 141 -10.7; 155 -10.4; 170 -10.1; 187 -9.6; 206 -9.3; 227 -9.0; 249 -8.9; 274 -8.4; 302 -7.8; 332 -7.3; 365 -6.7; 402 -6.0; 442 -5.3; 486 -4.6; 535 -3.8; 588 -3.2; 647 -2.7; 712 -2.6; 783 -2.8; 861 -3.2; 947 -3.7; 1042 -4.2; 1146 -4.5; 1261 -4.7; 1387 -5.1; 1526 -5.5; 1678 -6.2; 1846 -7.0; 2031 -7.9; 2234 -8.3; 2457 -7.8; 2703 -6.7; 2973 -5.6; 3270 -5.5; 3597 -6.7; 3957 -8.9; 4353 -11.0; 4788 -9.2; 5267 -3.4; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -7.6; 12418 -8.4; 13660 -9.2; 15026 -12.3; 16529 -14.7; 18182 -16.6; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.75 | -1.7 dB  |
| Peaking | 120 Hz   | 0.48 | -4.4 dB  |
| Peaking | 683 Hz   | 1.23 | 4.5 dB   |
| Peaking | 4451 Hz  | 4.3  | -6.4 dB  |
| Peaking | 5912 Hz  | 3.72 | 7.5 dB   |
| Peaking | 2203 Hz  | 2.22 | -5.1 dB  |
| Peaking | 2385 Hz  | 1.05 | 2.8 dB   |
| Peaking | 11491 Hz | 0.86 | 2.5 dB   |
| Peaking | 20113 Hz | 0.3  | -13.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -10.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)