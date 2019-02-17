# Plantronics BackBeat Go 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.1; 25 -5.7; 28 -6.5; 31 -7.1; 34 -7.5; 37 -7.7; 41 -7.8; 45 -7.9; 49 -7.9; 54 -7.8; 60 -7.9; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.5; 106 -9.6; 116 -9.7; 128 -9.6; 141 -9.4; 155 -9.0; 170 -8.5; 187 -7.8; 206 -7.0; 227 -6.2; 249 -5.5; 274 -4.8; 302 -4.1; 332 -3.4; 365 -2.3; 402 -1.1; 442 -0.5; 486 -0.5; 535 -0.9; 588 -1.3; 647 -1.7; 712 -2.4; 783 -3.0; 861 -2.2; 947 -2.3; 1042 -2.9; 1146 -1.9; 1261 -1.5; 1387 -2.2; 1526 -3.2; 1678 -4.1; 1846 -4.6; 2031 -4.3; 2234 -3.1; 2457 -1.3; 2703 -0.8; 2973 -1.5; 3270 -2.3; 3597 -3.7; 3957 -6.0; 4353 -7.9; 4788 -6.8; 5267 -5.1; 5793 -4.3; 6373 -9.8; 7010 -10.4; 7711 -11.0; 8482 -12.8; 9330 -13.3; 10263 -13.0; 11289 -14.0; 12418 -13.0; 13660 -10.5; 15026 -9.2; 16529 -8.2; 18182 -7.4; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Go 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Go 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 1.23 | -2.9 dB |
| Peaking | 123 Hz   | 0.55 | -6.7 dB |
| Peaking | 454 Hz   | 1.03 | 3.9 dB  |
| Peaking | 10045 Hz | 0.92 | -9.2 dB |
| Peaking | 18273 Hz | 0.25 | -3.7 dB |
| Peaking | 1959 Hz  | 2.54 | -4.7 dB |
| Peaking | 2509 Hz  | 1.18 | 4.6 dB  |
| Peaking | 4367 Hz  | 3.7  | -4.3 dB |
| Peaking | 5879 Hz  | 4.47 | 4.6 dB  |
| Peaking | 6469 Hz  | 5.11 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.8 dB |
| Peaking | 16000 Hz | 1.41 | -8.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Go%20600/Plantronics%20BackBeat%20Go%20600.png)