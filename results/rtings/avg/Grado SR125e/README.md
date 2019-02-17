# Grado SR125e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.6; 37 -2.3; 41 -3.0; 45 -3.7; 49 -4.2; 54 -4.8; 60 -5.3; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.2; 116 -7.4; 128 -7.5; 141 -7.6; 155 -7.7; 170 -7.7; 187 -7.6; 206 -7.4; 227 -7.0; 249 -6.8; 274 -6.9; 302 -7.4; 332 -7.4; 365 -7.3; 402 -7.3; 442 -7.3; 486 -7.3; 535 -7.3; 588 -7.1; 647 -7.0; 712 -6.8; 783 -6.7; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -6.9; 1387 -7.5; 1526 -8.3; 1678 -9.6; 1846 -13.6; 2031 -16.0; 2234 -15.0; 2457 -13.5; 2703 -12.1; 2973 -10.8; 3270 -10.3; 3597 -11.0; 3957 -13.6; 4353 -10.8; 4788 -7.1; 5267 -10.4; 5793 -11.5; 6373 -12.0; 7010 -14.3; 7711 -14.5; 8482 -16.3; 9330 -17.3; 10263 -13.8; 11289 -9.6; 12418 -8.1; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.71 | 6.4 dB   |
| Peaking | 121 Hz   | 0.5  | -1.5 dB  |
| Peaking | 2146 Hz  | 2.6  | -9.5 dB  |
| Peaking | 3910 Hz  | 4.95 | -4.9 dB  |
| Peaking | 8611 Hz  | 1.6  | -10.7 dB |
| Peaking | 1206 Hz  | 2.33 | 1.0 dB   |
| Peaking | 2788 Hz  | 6.12 | -1.0 dB  |
| Peaking | 4912 Hz  | 7.45 | 5.0 dB   |
| Peaking | 5300 Hz  | 3.07 | -2.8 dB  |
| Peaking | 13632 Hz | 1.8  | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -9.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR125e/Grado%20SR125e.png)