# Oriolus Forsteni sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.7; 28 -9.7; 31 -9.6; 34 -9.6; 37 -9.5; 41 -9.4; 45 -9.4; 49 -9.3; 54 -9.2; 60 -9.1; 66 -9.2; 72 -9.2; 79 -9.2; 87 -9.3; 96 -9.3; 106 -9.3; 116 -9.3; 128 -9.3; 141 -9.2; 155 -9.2; 170 -9.0; 187 -8.8; 206 -8.6; 227 -8.4; 249 -8.2; 274 -7.9; 302 -7.7; 332 -7.4; 365 -7.2; 402 -7.0; 442 -6.8; 486 -6.6; 535 -6.4; 588 -6.2; 647 -6.0; 712 -5.7; 783 -5.5; 861 -5.3; 947 -5.4; 1042 -5.8; 1146 -6.6; 1261 -7.5; 1387 -8.0; 1526 -7.7; 1678 -6.4; 1846 -4.9; 2031 -4.0; 2234 -3.6; 2457 -3.8; 2703 -3.6; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -2.3; 5267 -3.3; 5793 -5.9; 6373 -12.1; 7010 -17.1; 7711 -16.2; 8482 -12.4; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -10.9; 18182 -13.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.19 | -3.2 dB  |
| Peaking | 153 Hz   | 0.82 | -2.0 dB  |
| Peaking | 4076 Hz  | 1.06 | 7.5 dB   |
| Peaking | 7203 Hz  | 3.06 | -14.4 dB |
| Peaking | 17920 Hz | 1.81 | -8.0 dB  |
| Peaking | 887 Hz   | 1.71 | 1.5 dB   |
| Peaking | 1433 Hz  | 2.28 | -3.0 dB  |
| Peaking | 1974 Hz  | 3.45 | 1.4 dB   |
| Peaking | 8186 Hz  | 5.95 | -3.2 dB  |
| Peaking | 9839 Hz  | 1.57 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriolus%20Forsteni%20sample%201/Oriolus%20Forsteni%20sample%201.png)