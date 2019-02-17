# Monoprice Enhanced Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.5; 45 -3.7; 49 -4.0; 54 -4.3; 60 -4.8; 66 -5.2; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.7; 116 -7.0; 128 -7.3; 141 -7.6; 155 -7.8; 170 -8.1; 187 -8.5; 206 -8.9; 227 -9.4; 249 -9.9; 274 -10.3; 302 -10.8; 332 -11.3; 365 -11.8; 402 -12.1; 442 -12.2; 486 -12.1; 535 -11.5; 588 -10.4; 647 -8.8; 712 -7.0; 783 -5.6; 861 -4.6; 947 -3.8; 1042 -3.8; 1146 -3.9; 1261 -4.1; 1387 -4.2; 1526 -4.3; 1678 -4.4; 1846 -4.4; 2031 -4.4; 2234 -3.9; 2457 -3.4; 2703 -3.8; 2973 -5.1; 3270 -7.2; 3597 -9.6; 3957 -12.1; 4353 -13.2; 4788 -11.0; 5267 -7.9; 5793 -4.9; 6373 -4.3; 7010 -5.1; 7711 -9.0; 8482 -12.4; 9330 -12.3; 10263 -10.2; 11289 -7.5; 12418 -6.5; 13660 -8.6; 15026 -7.9; 16529 -4.0; 18182 -3.8; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.06 | 3.3 dB  |
| Peaking | 340 Hz   | 0.69 | -8.3 dB |
| Peaking | 4225 Hz  | 3.58 | -9.8 dB |
| Peaking | 9317 Hz  | 2.18 | -8.8 dB |
| Peaking | 20745 Hz | 0.52 | -5.3 dB |
| Peaking | 560 Hz   | 1.78 | -5.7 dB |
| Peaking | 691 Hz   | 0.86 | 4.0 dB  |
| Peaking | 9702 Hz  | 0.6  | 0.5 dB  |
| Peaking | 14498 Hz | 2.61 | -5.1 dB |
| Peaking | 17804 Hz | 1.24 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -8.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)