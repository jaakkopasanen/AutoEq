# 1MORE Triple Driver LTNG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.9; 25 -7.2; 28 -7.6; 31 -8.0; 34 -8.2; 37 -8.5; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.5; 60 -9.8; 66 -10.0; 72 -10.3; 79 -10.6; 87 -10.9; 96 -11.2; 106 -11.4; 116 -11.6; 128 -11.7; 141 -11.8; 155 -11.7; 170 -11.6; 187 -11.4; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.1; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.2; 588 -6.8; 647 -6.4; 712 -6.0; 783 -5.7; 861 -5.6; 947 -5.6; 1042 -6.0; 1146 -6.5; 1261 -6.8; 1387 -7.2; 1526 -7.5; 1678 -7.7; 1846 -8.0; 2031 -8.5; 2234 -9.4; 2457 -10.0; 2703 -9.8; 2973 -9.2; 3270 -8.8; 3597 -9.2; 3957 -10.8; 4353 -11.8; 4788 -9.0; 5267 -3.0; 5793 -0.5; 6373 -2.7; 7010 -5.8; 7711 -8.6; 8482 -7.1; 9330 -5.8; 10263 -5.8; 11289 -7.8; 12418 -10.9; 13660 -13.4; 15026 -15.7; 16529 -17.5; 18182 -10.5; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver LTNG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 128 Hz   | 0.43 | -6.0 dB  |
| Peaking | 2450 Hz  | 1.85 | -3.7 dB  |
| Peaking | 4391 Hz  | 2.97 | -6.9 dB  |
| Peaking | 5644 Hz  | 3.83 | 8.5 dB   |
| Peaking | 16016 Hz | 1.22 | -12.4 dB |
| Peaking | 34 Hz    | 2.04 | -0.6 dB  |
| Peaking | 816 Hz   | 2.95 | 1.3 dB   |
| Peaking | 7846 Hz  | 5.62 | -3.7 dB  |
| Peaking | 10596 Hz | 1.36 | 3.2 dB   |
| Peaking | 12615 Hz | 2.3  | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -13.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)