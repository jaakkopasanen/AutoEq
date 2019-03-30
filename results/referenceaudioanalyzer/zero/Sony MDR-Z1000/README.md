# Sony MDR-Z1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.2; 28 -3.3; 31 -4.2; 34 -5.0; 37 -5.7; 41 -6.5; 45 -7.1; 49 -7.6; 54 -8.2; 60 -9.0; 66 -9.8; 72 -10.3; 79 -10.8; 87 -11.3; 96 -11.4; 106 -11.4; 116 -11.3; 128 -10.9; 141 -10.2; 155 -9.2; 170 -7.9; 187 -6.6; 206 -4.9; 227 -3.5; 249 -2.8; 274 -2.8; 302 -3.3; 332 -4.3; 365 -5.4; 402 -6.2; 442 -6.8; 486 -7.1; 535 -7.4; 588 -7.5; 647 -7.7; 712 -7.8; 783 -8.1; 861 -8.1; 947 -8.1; 1042 -8.3; 1146 -8.5; 1261 -8.7; 1387 -9.0; 1526 -9.3; 1678 -9.7; 1846 -9.4; 2031 -8.6; 2234 -7.8; 2457 -7.2; 2703 -6.4; 2973 -5.3; 3270 -3.9; 3597 -1.9; 3957 -0.7; 4353 -0.7; 4788 -0.7; 5267 -1.1; 5793 -2.9; 6373 -3.0; 7010 -5.7; 7711 -10.7; 8482 -15.1; 9330 -16.1; 10263 -12.9; 11289 -7.6; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.34 | 14.0 dB  |
| Peaking | 161 Hz   | 0.16 | -23.9 dB |
| Peaking | 255 Hz   | 0.4  | 25.7 dB  |
| Peaking | 4710 Hz  | 1.2  | 8.4 dB   |
| Peaking | 8982 Hz  | 2.84 | -12.1 dB |
| Peaking | 987 Hz   | 1.18 | 1.4 dB   |
| Peaking | 1008 Hz  | 1.63 | -0.2 dB  |
| Peaking | 1743 Hz  | 1.63 | -1.6 dB  |
| Peaking | 3639 Hz  | 2.97 | 0.9 dB   |
| Peaking | 10967 Hz | 2.6  | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)