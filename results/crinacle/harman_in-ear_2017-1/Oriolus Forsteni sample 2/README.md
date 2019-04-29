# Oriolus Forsteni sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.4; 28 -5.8; 31 -6.1; 34 -6.3; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.6; 96 -8.9; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.7; 155 -9.8; 170 -9.7; 187 -9.7; 206 -9.7; 227 -9.6; 249 -9.4; 274 -9.3; 302 -9.0; 332 -8.8; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.8; 535 -7.6; 588 -7.4; 647 -7.2; 712 -6.9; 783 -6.6; 861 -6.5; 947 -6.7; 1042 -7.1; 1146 -7.8; 1261 -8.3; 1387 -8.3; 1526 -7.4; 1678 -5.8; 1846 -4.1; 2031 -2.7; 2234 -1.6; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -1.2; 5267 -1.8; 5793 -4.1; 6373 -9.0; 7010 -13.8; 7711 -12.8; 8482 -10.0; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -14.4; 15026 -22.2; 16529 -28.2; 18182 -28.0; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.56 | 2.7 dB   |
| Peaking | 264 Hz   | 0.11 | -2.9 dB  |
| Peaking | 7277 Hz  | 2.4  | -17.3 dB |
| Peaking | 7685 Hz  | 0.33 | 16.4 dB  |
| Peaking | 17071 Hz | 0.6  | -30.4 dB |
| Peaking | 765 Hz   | 1.17 | 1.7 dB   |
| Peaking | 1387 Hz  | 1.93 | -3.9 dB  |
| Peaking | 2301 Hz  | 1.89 | 1.9 dB   |
| Peaking | 12314 Hz | 2.47 | 7.9 dB   |
| Peaking | 13345 Hz | 1.04 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -22.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriolus%20Forsteni%20sample%202/Oriolus%20Forsteni%20sample%202.png)