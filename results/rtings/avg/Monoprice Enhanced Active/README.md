# Monoprice Enhanced Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.3; 28 -3.9; 31 -4.4; 34 -4.8; 37 -5.1; 41 -5.5; 45 -5.8; 49 -6.0; 54 -6.2; 60 -6.4; 66 -6.5; 72 -6.6; 79 -6.6; 87 -6.6; 96 -6.6; 106 -6.5; 116 -6.3; 128 -6.2; 141 -6.0; 155 -5.9; 170 -5.9; 187 -5.9; 206 -6.2; 227 -6.5; 249 -6.9; 274 -7.4; 302 -7.9; 332 -8.4; 365 -8.9; 402 -9.2; 442 -9.4; 486 -9.3; 535 -8.7; 588 -7.6; 647 -6.0; 712 -4.3; 783 -2.8; 861 -1.8; 947 -1.1; 1042 -1.0; 1146 -1.3; 1261 -1.5; 1387 -1.6; 1526 -1.6; 1678 -1.7; 1846 -1.8; 2031 -1.9; 2234 -1.8; 2457 -1.4; 2703 -1.5; 2973 -2.3; 3270 -4.1; 3597 -6.5; 3957 -9.0; 4353 -10.0; 4788 -8.3; 5267 -4.9; 5793 -1.7; 6373 -0.5; 7010 -2.6; 7711 -6.8; 8482 -9.0; 9330 -7.7; 10263 -6.8; 11289 -5.7; 12418 -5.1; 13660 -5.3; 15026 -5.2; 16529 -5.1; 18182 -5.1; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 528 Hz   | 0.69 | -13.1 dB |
| Peaking | 812 Hz   | 0.54 | 12.3 dB  |
| Peaking | 2908 Hz  | 1.25 | 9.3 dB   |
| Peaking | 4258 Hz  | 0.71 | -12.4 dB |
| Peaking | 6084 Hz  | 2.66 | 11.9 dB  |
| Peaking | 18 Hz    | 0.89 | 3.5 dB   |
| Peaking | 80 Hz    | 0.41 | -1.8 dB  |
| Peaking | 173 Hz   | 1.14 | 1.7 dB   |
| Peaking | 8529 Hz  | 4.81 | -3.3 dB  |
| Peaking | 11134 Hz | 0.66 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -5.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)