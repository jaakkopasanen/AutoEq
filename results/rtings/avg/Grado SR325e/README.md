# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.5; 54 -2.1; 60 -2.6; 66 -3.1; 72 -3.5; 79 -3.8; 87 -4.1; 96 -4.3; 106 -4.6; 116 -4.8; 128 -4.9; 141 -5.0; 155 -5.0; 170 -5.1; 187 -5.0; 206 -4.6; 227 -4.4; 249 -4.5; 274 -4.9; 302 -4.9; 332 -4.8; 365 -4.6; 402 -4.6; 442 -4.8; 486 -4.9; 535 -4.8; 588 -4.7; 647 -4.5; 712 -4.4; 783 -4.3; 861 -4.2; 947 -4.2; 1042 -4.2; 1146 -4.3; 1261 -4.6; 1387 -5.2; 1526 -5.9; 1678 -7.2; 1846 -10.1; 2031 -13.2; 2234 -13.1; 2457 -11.2; 2703 -9.5; 2973 -8.3; 3270 -8.1; 3597 -7.6; 3957 -8.3; 4353 -9.5; 4788 -6.8; 5267 -7.2; 5793 -7.5; 6373 -6.0; 7010 -5.8; 7711 -7.9; 8482 -11.6; 9330 -14.7; 10263 -15.2; 11289 -13.5; 12418 -11.2; 13660 -8.6; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.44 | 6.2 dB  |
| Peaking | 917 Hz   | 0.4  | 2.7 dB  |
| Peaking | 2174 Hz  | 2.33 | -8.7 dB |
| Peaking | 10288 Hz | 2.11 | -9.5 dB |
| Peaking | 22050 Hz | 2.05 | -0.6 dB |
| Peaking | 226 Hz   | 4.48 | 0.9 dB  |
| Peaking | 1473 Hz  | 3.8  | 0.7 dB  |
| Peaking | 4266 Hz  | 7.03 | -2.7 dB |
| Peaking | 7022 Hz  | 4.2  | 2.8 dB  |
| Peaking | 8870 Hz  | 6.47 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR325e/Grado%20SR325e.png)