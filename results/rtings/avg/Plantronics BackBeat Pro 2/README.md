# Plantronics BackBeat Pro 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.2; 25 -12.2; 28 -12.2; 31 -12.3; 34 -12.4; 37 -12.3; 41 -11.6; 45 -10.5; 49 -9.3; 54 -7.8; 60 -6.4; 66 -5.3; 72 -4.4; 79 -3.6; 87 -2.9; 96 -2.3; 106 -1.8; 116 -1.4; 128 -1.1; 141 -0.8; 155 -0.6; 170 -0.5; 187 -0.5; 206 -0.6; 227 -0.8; 249 -1.1; 274 -1.6; 302 -1.9; 332 -2.1; 365 -2.5; 402 -3.2; 442 -4.2; 486 -4.7; 535 -4.8; 588 -4.5; 647 -3.3; 712 -3.2; 783 -3.7; 861 -3.4; 947 -3.1; 1042 -3.2; 1146 -3.3; 1261 -3.5; 1387 -3.8; 1526 -3.1; 1678 -4.0; 1846 -5.1; 2031 -4.9; 2234 -3.9; 2457 -3.4; 2703 -3.6; 2973 -4.3; 3270 -5.5; 3597 -6.6; 3957 -6.2; 4353 -5.8; 4788 -4.5; 5267 -4.0; 5793 -4.5; 6373 -5.1; 7010 -6.2; 7711 -6.8; 8482 -6.0; 9330 -5.3; 10263 -5.8; 11289 -6.4; 12418 -6.3; 13660 -6.8; 15026 -7.2; 16529 -4.0; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Pro 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Pro 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.67 | -9.9 dB |
| Peaking | 134 Hz   | 0.71 | 4.1 dB  |
| Peaking | 3703 Hz  | 3.72 | -2.7 dB |
| Peaking | 11781 Hz | 0.56 | -3.1 dB |
| Peaking | 22050 Hz | 1.86 | -1.8 dB |
| Peaking | 460 Hz   | 0.77 | 1.4 dB  |
| Peaking | 503 Hz   | 2.05 | -3.2 dB |
| Peaking | 1956 Hz  | 4.55 | -1.8 dB |
| Peaking | 2464 Hz  | 3.69 | 0.9 dB  |
| Peaking | 17714 Hz | 3.5  | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Pro%202/Plantronics%20BackBeat%20Pro%202.png)