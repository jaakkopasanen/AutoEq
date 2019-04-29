# Oriolus Finschi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.0; 28 -11.2; 31 -11.3; 34 -11.4; 37 -11.5; 41 -11.5; 45 -11.5; 49 -11.5; 54 -11.6; 60 -11.5; 66 -11.5; 72 -11.5; 79 -11.5; 87 -11.5; 96 -11.4; 106 -11.5; 116 -11.4; 128 -11.2; 141 -11.1; 155 -10.8; 170 -10.5; 187 -10.2; 206 -9.9; 227 -9.4; 249 -9.1; 274 -8.7; 302 -8.3; 332 -7.9; 365 -7.6; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.4; 588 -6.1; 647 -5.9; 712 -5.6; 783 -5.4; 861 -5.2; 947 -5.4; 1042 -5.9; 1146 -6.9; 1261 -7.8; 1387 -8.3; 1526 -8.3; 1678 -7.6; 1846 -6.7; 2031 -6.0; 2234 -5.4; 2457 -4.5; 2703 -3.1; 2973 -1.8; 3270 -0.8; 3597 -0.5; 3957 -0.8; 4353 -1.5; 4788 -1.5; 5267 -2.0; 5793 -7.0; 6373 -7.7; 7010 -9.3; 7711 -5.8; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Finschi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Finschi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 39 Hz    |  0.31 | -5.3 dB |
| Peaking | 158 Hz   |  0.8  | -2.7 dB |
| Peaking | 1557 Hz  |  2.36 | -3.3 dB |
| Peaking | 4005 Hz  |  1.05 | 6.1 dB  |
| Peaking | 6552 Hz  |  3.13 | -5.6 dB |
| Peaking | 917 Hz   |  1.65 | 2.0 dB  |
| Peaking | 1363 Hz  |  1.32 | -2.0 dB |
| Peaking | 1586 Hz  |  3.57 | 1.7 dB  |
| Peaking | 5112 Hz  | 14.23 | 1.8 dB  |
| Peaking | 11787 Hz |  0.74 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriolus%20Finschi/Oriolus%20Finschi.png)