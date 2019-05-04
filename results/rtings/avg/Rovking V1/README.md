# Rovking V1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -22.2; 23 -22.2; 25 -22.1; 28 -22.1; 31 -22.0; 34 -22.0; 37 -21.9; 41 -21.9; 45 -21.8; 49 -21.7; 54 -21.6; 60 -21.2; 66 -21.0; 72 -20.7; 79 -20.4; 87 -20.0; 96 -19.6; 106 -19.1; 116 -18.6; 128 -18.0; 141 -17.1; 155 -16.2; 170 -15.3; 187 -14.3; 206 -13.4; 227 -12.7; 249 -12.3; 274 -11.8; 302 -11.0; 332 -10.2; 365 -9.2; 402 -8.2; 442 -7.1; 486 -6.1; 535 -5.0; 588 -4.1; 647 -3.5; 712 -3.2; 783 -2.8; 861 -2.3; 947 -2.0; 1042 -1.7; 1146 -1.4; 1261 -1.2; 1387 -1.2; 1526 -1.0; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.8; 3270 -2.1; 3597 -3.4; 3957 -4.8; 4353 -6.3; 4788 -9.4; 5267 -9.1; 5793 -6.9; 6373 -4.4; 7010 -4.8; 7711 -9.4; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.5; 13660 -8.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rovking V1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rovking V1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.22 | -14.3 dB |
| Peaking | 1831 Hz  | 0.24 | 6.7 dB   |
| Peaking | 4857 Hz  | 3.33 | -6.9 dB  |
| Peaking | 9499 Hz  | 0.63 | -2.8 dB  |
| Peaking | 16 Hz    | 0.76 | -5.6 dB  |
| Peaking | 6679 Hz  | 9.5  | 2.9 dB   |
| Peaking | 7842 Hz  | 6.43 | -4.3 dB  |
| Peaking | 12232 Hz | 1.33 | 2.6 dB   |
| Peaking | 12961 Hz | 3.72 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -16.7 dB |
| Peaking | 62 Hz    | 1.41 | -10.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Rovking%20V1/Rovking%20V1.png)