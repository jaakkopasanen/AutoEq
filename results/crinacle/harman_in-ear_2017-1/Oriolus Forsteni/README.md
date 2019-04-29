# Oriolus Forsteni
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.1; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.7; 49 -8.7; 54 -8.8; 60 -8.9; 66 -9.0; 72 -9.2; 79 -9.3; 87 -9.5; 96 -9.7; 106 -9.8; 116 -9.9; 128 -10.0; 141 -10.0; 155 -10.0; 170 -9.9; 187 -9.9; 206 -9.7; 227 -9.6; 249 -9.4; 274 -9.2; 302 -8.9; 332 -8.6; 365 -8.3; 402 -8.1; 442 -7.8; 486 -7.6; 535 -7.4; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.9; 1146 -7.6; 1261 -8.1; 1387 -8.2; 1526 -7.5; 1678 -6.0; 1846 -4.4; 2031 -3.0; 2234 -2.0; 2457 -1.5; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.3; 5267 -2.1; 5793 -4.4; 6373 -9.8; 7010 -14.3; 7711 -13.0; 8482 -10.3; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -14.1; 15026 -22.5; 16529 -29.0; 18182 -29.0; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.16 | 0.8 dB   |
| Peaking | 184 Hz   | 0.07 | -2.9 dB  |
| Peaking | 7221 Hz  | 2.45 | -17.5 dB |
| Peaking | 7773 Hz  | 0.33 | 16.6 dB  |
| Peaking | 17117 Hz | 0.6  | -31.6 dB |
| Peaking | 1319 Hz  | 0.65 | 4.2 dB   |
| Peaking | 1387 Hz  | 1.58 | -7.2 dB  |
| Peaking | 8684 Hz  | 4.87 | -2.3 dB  |
| Peaking | 12396 Hz | 3.24 | 4.5 dB   |
| Peaking | 15043 Hz | 2.97 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -23.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriolus%20Forsteni/Oriolus%20Forsteni.png)