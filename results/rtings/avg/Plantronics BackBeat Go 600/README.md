# Plantronics BackBeat Go 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.9; 25 -5.5; 28 -6.3; 31 -6.9; 34 -7.3; 37 -7.5; 41 -7.7; 45 -7.7; 49 -7.7; 54 -7.7; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.3; 106 -9.4; 116 -9.5; 128 -9.4; 141 -9.2; 155 -8.8; 170 -8.3; 187 -7.7; 206 -6.9; 227 -6.2; 249 -5.5; 274 -4.8; 302 -4.0; 332 -3.4; 365 -2.3; 402 -1.1; 442 -0.5; 486 -0.6; 535 -0.9; 588 -1.4; 647 -1.8; 712 -2.6; 783 -3.1; 861 -2.3; 947 -2.5; 1042 -3.1; 1146 -2.0; 1261 -1.7; 1387 -2.4; 1526 -3.5; 1678 -4.4; 1846 -4.9; 2031 -4.8; 2234 -4.0; 2457 -2.3; 2703 -1.3; 2973 -1.6; 3270 -2.0; 3597 -3.5; 3957 -5.7; 4353 -7.5; 4788 -7.2; 5267 -5.5; 5793 -4.3; 6373 -8.4; 7010 -10.5; 7711 -11.9; 8482 -12.5; 9330 -11.6; 10263 -12.6; 11289 -15.0; 12418 -13.2; 13660 -9.6; 15026 -8.6; 16529 -7.9; 18182 -7.1; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Go 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Go 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 196 Hz   | 0.34 | -8.0 dB |
| Peaking | 411 Hz   | 0.53 | 9.6 dB  |
| Peaking | 2888 Hz  | 3.37 | 4.0 dB  |
| Peaking | 7768 Hz  | 3.3  | -4.2 dB |
| Peaking | 11472 Hz | 1.16 | -9.0 dB |
| Peaking | 751 Hz   | 5.42 | -1.3 dB |
| Peaking | 1274 Hz  | 4.69 | 1.8 dB  |
| Peaking | 1866 Hz  | 5.02 | -1.3 dB |
| Peaking | 4450 Hz  | 6.6  | -2.6 dB |
| Peaking | 5692 Hz  | 9.02 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Go%20600/Plantronics%20BackBeat%20Go%20600.png)