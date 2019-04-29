# Oriolus Finschi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.5; 25 -12.7; 28 -12.8; 31 -13.0; 34 -13.1; 37 -13.1; 41 -13.2; 45 -13.2; 49 -13.2; 54 -13.2; 60 -13.2; 66 -13.1; 72 -13.1; 79 -13.1; 87 -13.1; 96 -13.1; 106 -13.1; 116 -13.0; 128 -12.8; 141 -12.7; 155 -12.5; 170 -12.2; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.3; 302 -9.9; 332 -9.4; 365 -8.9; 402 -8.6; 442 -8.2; 486 -7.9; 535 -7.6; 588 -7.3; 647 -7.0; 712 -6.8; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -7.2; 1146 -8.1; 1261 -8.8; 1387 -9.0; 1526 -8.7; 1678 -7.9; 1846 -7.0; 2031 -5.9; 2234 -4.7; 2457 -3.2; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.1; 5267 -1.7; 5793 -6.3; 6373 -6.7; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.7; 15026 -13.9; 16529 -11.8; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Finschi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Finschi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.33 | -6.1 dB |
| Peaking | 158 Hz   | 0.6  | -4.2 dB |
| Peaking | 1487 Hz  | 2.2  | -3.5 dB |
| Peaking | 3501 Hz  | 1.27 | 7.0 dB  |
| Peaking | 15455 Hz | 2.16 | -8.2 dB |
| Peaking | 818 Hz   | 3.71 | 0.8 dB  |
| Peaking | 3576 Hz  | 8.39 | -0.9 dB |
| Peaking | 5144 Hz  | 4.21 | 4.2 dB  |
| Peaking | 5971 Hz  | 2.75 | -3.6 dB |
| Peaking | 12459 Hz | 5.18 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriolus%20Finschi/Oriolus%20Finschi.png)