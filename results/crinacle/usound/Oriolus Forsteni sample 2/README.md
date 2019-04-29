# Oriolus Forsteni sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.9; 25 -4.2; 28 -4.6; 31 -4.9; 34 -5.2; 37 -5.4; 41 -5.6; 45 -5.8; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.6; 72 -6.9; 79 -7.1; 87 -7.4; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.4; 141 -8.5; 155 -8.6; 170 -8.6; 187 -8.6; 206 -8.5; 227 -8.4; 249 -8.3; 274 -8.1; 302 -7.9; 332 -7.8; 365 -7.6; 402 -7.4; 442 -7.3; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.2; 783 -6.0; 861 -5.8; 947 -5.9; 1042 -6.3; 1146 -7.1; 1261 -7.8; 1387 -8.1; 1526 -7.5; 1678 -5.9; 1846 -4.3; 2031 -3.2; 2234 -2.7; 2457 -2.7; 2703 -2.6; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.6; 4788 -2.0; 5267 -2.7; 5793 -5.2; 6373 -10.5; 7010 -16.2; 7711 -15.7; 8482 -11.7; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.3; 18182 -11.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.35 | 3.7 dB   |
| Peaking | 170 Hz   | 0.56 | -2.3 dB  |
| Peaking | 4063 Hz  | 0.89 | 6.9 dB   |
| Peaking | 7276 Hz  | 3.18 | -13.9 dB |
| Peaking | 17963 Hz | 2.07 | -5.9 dB  |
| Peaking | 1301 Hz  | 5.26 | -2.0 dB  |
| Peaking | 1515 Hz  | 4.98 | -2.1 dB  |
| Peaking | 2072 Hz  | 3.2  | 1.4 dB   |
| Peaking | 8430 Hz  | 6.27 | -2.9 dB  |
| Peaking | 9231 Hz  | 2.54 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriolus%20Forsteni%20sample%202/Oriolus%20Forsteni%20sample%202.png)