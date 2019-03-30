# Oriolus MK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.6; 25 -12.6; 28 -12.6; 31 -12.5; 34 -12.4; 37 -12.4; 41 -12.3; 45 -12.2; 49 -12.1; 54 -11.9; 60 -11.8; 66 -11.6; 72 -11.4; 79 -11.1; 87 -10.9; 96 -10.6; 106 -10.3; 116 -9.9; 128 -9.6; 141 -9.3; 155 -9.0; 170 -9.0; 187 -8.8; 206 -8.7; 227 -8.5; 249 -8.2; 274 -7.9; 302 -7.6; 332 -7.3; 365 -7.0; 402 -6.8; 442 -6.5; 486 -6.4; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.7; 861 -5.5; 947 -5.5; 1042 -5.8; 1146 -6.0; 1261 -6.4; 1387 -7.0; 1526 -7.9; 1678 -9.3; 1846 -10.9; 2031 -11.7; 2234 -10.9; 2457 -9.1; 2703 -7.7; 2973 -7.1; 3270 -6.8; 3597 -7.5; 3957 -8.0; 4353 -7.0; 4788 -4.8; 5267 -2.6; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus MK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus MK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.13 | -6.1 dB |
| Peaking | 895 Hz  | 0.95 | 1.3 dB  |
| Peaking | 2009 Hz | 2.45 | -5.9 dB |
| Peaking | 4020 Hz | 5.42 | -2.3 dB |
| Peaking | 5913 Hz | 3.29 | 6.7 dB  |
| Peaking | 136 Hz  | 2.52 | 0.3 dB  |
| Peaking | 225 Hz  | 2.91 | -0.5 dB |
| Peaking | 6624 Hz | 9.39 | 1.5 dB  |
| Peaking | 7763 Hz | 2.82 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Oriolus%20MK2/Oriolus%20MK2.png)