# Oriolus Forsteni
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.9; 25 -9.9; 28 -9.8; 31 -9.7; 34 -9.6; 37 -9.5; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.2; 60 -9.0; 66 -8.9; 72 -8.7; 79 -8.5; 87 -8.3; 96 -8.1; 106 -7.8; 116 -7.5; 128 -7.2; 141 -6.8; 155 -6.6; 170 -6.5; 187 -6.2; 206 -5.9; 227 -5.6; 249 -5.7; 274 -5.5; 302 -5.2; 332 -5.0; 365 -4.7; 402 -4.5; 442 -4.4; 486 -4.3; 535 -4.0; 588 -4.0; 647 -4.0; 712 -4.0; 783 -4.0; 861 -4.2; 947 -4.4; 1042 -4.9; 1146 -5.5; 1261 -6.1; 1387 -6.1; 1526 -5.7; 1678 -5.3; 1846 -4.7; 2031 -4.3; 2234 -4.5; 2457 -5.3; 2703 -6.5; 2973 -6.3; 3270 -3.9; 3597 -0.5; 3957 -1.3; 4353 -3.8; 4788 -4.8; 5267 -4.6; 5793 -5.3; 6373 -8.4; 7010 -10.3; 7711 -9.3; 8482 -6.8; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.44 | -4.2 dB |
| Peaking | 78 Hz   | 0.7  | -1.9 dB |
| Peaking | 571 Hz  | 1.21 | 1.6 dB  |
| Peaking | 3762 Hz | 5.44 | 5.6 dB  |
| Peaking | 7155 Hz | 4.28 | -5.6 dB |
| Peaking | 939 Hz  | 2.51 | 0.9 dB  |
| Peaking | 1347 Hz | 1.64 | -2.0 dB |
| Peaking | 2143 Hz | 1.2  | 1.8 dB  |
| Peaking | 2797 Hz | 4.29 | -3.0 dB |
| Peaking | 5475 Hz | 8.2  | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Oriolus%20Forsteni/Oriolus%20Forsteni.png)