# 1MORE Triple Driver In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.3; 34 -4.5; 37 -4.6; 41 -4.8; 45 -5.0; 49 -5.1; 54 -5.3; 60 -5.7; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.3; 96 -7.7; 106 -8.2; 116 -8.7; 128 -9.1; 141 -9.4; 155 -9.5; 170 -9.5; 187 -9.3; 206 -9.2; 227 -9.2; 249 -9.0; 274 -8.5; 302 -7.9; 332 -7.3; 365 -6.7; 402 -6.1; 442 -5.4; 486 -4.6; 535 -3.9; 588 -3.1; 647 -2.6; 712 -2.5; 783 -2.7; 861 -3.1; 947 -3.7; 1042 -4.1; 1146 -4.3; 1261 -4.6; 1387 -5.0; 1526 -5.4; 1678 -6.0; 1846 -6.7; 2031 -7.5; 2234 -7.5; 2457 -6.9; 2703 -6.2; 2973 -5.6; 3270 -5.8; 3597 -7.0; 3957 -9.2; 4353 -11.5; 4788 -8.9; 5267 -3.1; 5793 -0.5; 6373 -0.6; 7010 -3.6; 7711 -5.8; 8482 -6.3; 9330 -6.1; 10263 -6.1; 11289 -6.5; 12418 -8.1; 13660 -9.9; 15026 -12.7; 16529 -14.8; 18182 -16.7; 20000 -21.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.19 | 2.8 dB   |
| Peaking | 171 Hz   | 0.61 | -4.0 dB  |
| Peaking | 684 Hz   | 1.22 | 4.4 dB   |
| Peaking | 4418 Hz  | 4.3  | -7.0 dB  |
| Peaking | 5911 Hz  | 3.63 | 7.4 dB   |
| Peaking | 2116 Hz  | 3.15 | -2.5 dB  |
| Peaking | 4411 Hz  | 0.31 | 0.8 dB   |
| Peaking | 11243 Hz | 1.66 | 2.7 dB   |
| Peaking | 20045 Hz | 0.28 | -14.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -11.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Triple%20Driver%20In-Ear/1MORE%20Triple%20Driver%20In-Ear.png)