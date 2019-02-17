# Rovking V1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.9; 23 -19.9; 25 -19.9; 28 -19.8; 31 -19.7; 34 -19.7; 37 -19.6; 41 -19.5; 45 -19.5; 49 -19.4; 54 -19.4; 60 -19.3; 66 -19.3; 72 -19.3; 79 -19.2; 87 -19.1; 96 -19.0; 106 -19.0; 116 -19.0; 128 -18.7; 141 -18.3; 155 -17.9; 170 -17.2; 187 -16.5; 206 -15.8; 227 -15.3; 249 -14.9; 274 -14.4; 302 -13.6; 332 -12.8; 365 -11.8; 402 -10.7; 442 -9.6; 486 -8.5; 535 -7.5; 588 -6.5; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.8; 947 -4.4; 1042 -4.1; 1146 -3.8; 1261 -3.6; 1387 -3.6; 1526 -3.4; 1678 -2.6; 1846 -1.9; 2031 -1.1; 2234 -0.5; 2457 -0.8; 2703 -1.7; 2973 -3.4; 3270 -5.0; 3597 -6.3; 3957 -7.8; 4353 -9.3; 4788 -11.6; 5267 -11.3; 5793 -9.5; 6373 -8.0; 7010 -7.3; 7711 -11.3; 8482 -10.4; 9330 -4.5; 10263 -4.3; 11289 -4.4; 12418 -11.5; 13660 -11.9; 15026 -9.4; 16529 -9.1; 18182 -6.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rovking V1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rovking V1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.18 | -15.2 dB |
| Peaking | 184 Hz   | 0.63 | -6.4 dB  |
| Peaking | 5223 Hz  | 2.32 | -7.4 dB  |
| Peaking | 13085 Hz | 4.49 | -6.5 dB  |
| Peaking | 15756 Hz | 1.1  | -4.8 dB  |
| Peaking | 357 Hz   | 2.51 | -1.6 dB  |
| Peaking | 1023 Hz  | 0.81 | 1.2 dB   |
| Peaking | 2272 Hz  | 2.51 | 4.4 dB   |
| Peaking | 8095 Hz  | 5.48 | -7.3 dB  |
| Peaking | 10023 Hz | 2.82 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -16.2 dB |
| Peaking | 62 Hz    | 1.41 | -10.1 dB |
| Peaking | 125 Hz   | 1.41 | -11.3 dB |
| Peaking | 250 Hz   | 1.41 | -8.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Rovking%20V1/Rovking%20V1.png)