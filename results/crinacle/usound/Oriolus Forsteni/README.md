# Oriolus Forsteni
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.8; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.4; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.8; 66 -7.9; 72 -8.0; 79 -8.2; 87 -8.3; 96 -8.5; 106 -8.7; 116 -8.8; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.8; 187 -8.7; 206 -8.6; 227 -8.4; 249 -8.2; 274 -8.0; 302 -7.8; 332 -7.6; 365 -7.4; 402 -7.2; 442 -7.0; 486 -6.8; 535 -6.7; 588 -6.5; 647 -6.3; 712 -6.0; 783 -5.7; 861 -5.6; 947 -5.7; 1042 -6.1; 1146 -6.9; 1261 -7.7; 1387 -8.1; 1526 -7.6; 1678 -6.2; 1846 -4.6; 2031 -3.6; 2234 -3.2; 2457 -3.2; 2703 -3.1; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -2.1; 5267 -3.0; 5793 -5.5; 6373 -11.3; 7010 -16.6; 7711 -15.9; 8482 -12.0; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -10.1; 18182 -12.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 137 Hz   | 0.52 | -2.4 dB  |
| Peaking | 1439 Hz  | 2.81 | -3.9 dB  |
| Peaking | 5135 Hz  | 0.52 | 9.7 dB   |
| Peaking | 7224 Hz  | 2.1  | -19.4 dB |
| Peaking | 17912 Hz | 1.61 | -7.0 dB  |
| Peaking | 820 Hz   | 3.69 | 0.7 dB   |
| Peaking | 2694 Hz  | 5.54 | -2.0 dB  |
| Peaking | 3003 Hz  | 3.75 | 1.3 dB   |
| Peaking | 8286 Hz  | 8.35 | -1.8 dB  |
| Peaking | 9487 Hz  | 7.44 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriolus%20Forsteni/Oriolus%20Forsteni.png)