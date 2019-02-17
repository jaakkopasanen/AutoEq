# 1MORE Triple Driver In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.6; 25 -3.9; 28 -4.2; 31 -4.5; 34 -4.7; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.3; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.7; 79 -7.0; 87 -7.5; 96 -7.9; 106 -8.4; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.7; 170 -9.7; 187 -9.5; 206 -9.4; 227 -9.4; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.5; 365 -6.9; 402 -6.3; 442 -5.6; 486 -4.8; 535 -4.1; 588 -3.4; 647 -2.8; 712 -2.7; 783 -2.9; 861 -3.3; 947 -3.9; 1042 -4.3; 1146 -4.5; 1261 -4.8; 1387 -5.2; 1526 -5.6; 1678 -6.2; 1846 -6.9; 2031 -7.7; 2234 -7.7; 2457 -7.1; 2703 -6.4; 2973 -5.8; 3270 -6.0; 3597 -7.2; 3957 -9.4; 4353 -11.7; 4788 -9.1; 5267 -3.3; 5793 -0.7; 6373 -0.5; 7010 -1.7; 7711 -4.4; 8482 -6.4; 9330 -5.8; 10263 -5.3; 11289 -6.7; 12418 -8.3; 13660 -10.1; 15026 -12.9; 16529 -15.0; 18182 -16.9; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 163 Hz   | 0.74 | -6.0 dB  |
| Peaking | 2121 Hz  | 2.59 | -3.6 dB  |
| Peaking | 4453 Hz  | 3.08 | -10.1 dB |
| Peaking | 5856 Hz  | 1.94 | 7.4 dB   |
| Peaking | 19737 Hz | 0.35 | -16.3 dB |
| Peaking | 18 Hz    | 2.03 | 1.1 dB   |
| Peaking | 306 Hz   | 2.35 | -1.2 dB  |
| Peaking | 679 Hz   | 2.14 | 2.4 dB   |
| Peaking | 8481 Hz  | 5.96 | -2.0 dB  |
| Peaking | 10454 Hz | 2.86 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -15.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Triple%20Driver%20In-Ear/1MORE%20Triple%20Driver%20In-Ear.png)